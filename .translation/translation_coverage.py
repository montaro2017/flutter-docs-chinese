"""Source-word-weighted coverage, verified against the generated site."""
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from contextlib import nullcontext
from html.parser import HTMLParser
import json
import re
import sys

from case_paths import output_relative, read_source
from text_language_stats import DATA, ROOT, VOID, counts
from shared_translation import translate_shared
try:
    from lxml import html as lxml_html
except ImportError:
    lxml_html = None

WORDS = re.compile(r"[A-Za-z]+(?:['’-][A-Za-z]+)*")
URL = re.compile(r'https?://[^\s<>]+|www\.[^\s<>]+')
IDENTIFIER = re.compile(r'\b(?:[a-z]+[A-Z][A-Za-z0-9]*|[A-Z][a-z]+[A-Z][A-Za-z0-9]*|[A-Za-z]\w*[_.$]\w[\w.$]*|[A-Z][A-Z0-9_]+)\b')
UNIT_TAGS = {'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'dd', 'td', 'th', 'dt'}
_WORKER_MAPPINGS = None
_WORKER_EXTRAS = None
_WORKER_FRAGMENTS = None


class Units(HTMLParser):
    """Collect outer prose blocks once, including list/table/direct section text."""
    def __init__(self, scope='prose', fragment=False):
        super().__init__(convert_charrefs=True)
        self.scope = scope
        self.fragment = fragment
        self.stack = []
        self.units = []
        self.parts = []
        self.kind = 'direct'

    def flush(self):
        text = ' '.join(''.join(self.parts).split())
        if text:
            self.units.append((self.kind, text))
        self.parts = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        parent = self.stack[-1] if self.stack else (None, self.fragment, False, False)
        selected = parent[1] or tag == 'section' and {'desc', 'markdown'} <= set(a.get('class', '').split()) or self.scope == 'prose' and tag == 'dd'
        # API link labels containing a single identifier are names, not prose.
        skip = parent[2] or tag in {'code', 'pre', 'script', 'style', 'template', 'noscript'}
        atomic = parent[3]
        if selected and not skip and tag in UNIT_TAGS and not atomic:
            self.flush()
            self.kind = tag
            atomic = True
        if tag in {'br', 'hr'}:
            self.parts.append(' ')
        if tag not in VOID:
            self.stack.append((tag, selected, skip, atomic))
        if tag == 'a' and a.get('href'):
            self.parts.append(' ')

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                ending = self.stack[i:]
                del self.stack[i:]
                parent_atomic = self.stack[-1][3] if self.stack else False
                if any(row[3] for row in ending) and not parent_atomic:
                    self.flush()
                    self.kind = 'direct'
                break
        if tag in UNIT_TAGS or tag in {'div', 'section', 'a', 'code', 'pre'}:
            self.parts.append(' ')

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_data(self, value):
        if (self.stack and self.stack[-1][1] and not self.stack[-1][2]) or (not self.stack and self.fragment):
            self.parts.append(value)


def remove_names(markup):
    def link(m):
        label = re.sub('<[^>]+>', '', m[1]).strip()
        return ' ' if re.fullmatch(r'[A-Za-z_$][\w.$]*(?:\(\))?', label) else m[0]
    return re.sub(r'<a\b[^>]*>(.*?)</a>', link, markup, flags=re.S | re.I)


def units_stdlib(markup, scope='prose', fragment=False):
    parser = Units(scope, fragment)
    parser.feed(remove_names(markup))
    parser.close()
    parser.flush()
    return parser.units


def units_lxml(markup, scope='prose', fragment=False):
    """C-backed HTML parsing with the same unit boundaries as Units."""
    parser = lxml_html.HTMLParser(encoding='utf-8', recover=True, no_network=True)
    clean_markup = remove_names(markup)
    if fragment:
        root = lxml_html.fragment_fromstring(clean_markup, create_parent='div', parser=parser)
    else:
        root = lxml_html.document_fromstring(clean_markup, parser=parser)
    result = []
    parts = []
    kind = 'direct'

    def flush():
        nonlocal parts, kind
        text = ' '.join(''.join(parts).split())
        if text:
            result.append((kind, text))
        parts = []

    def visit(element, parent_selected=False, parent_skip=False, parent_atomic=False):
        nonlocal kind
        tag = element.tag.lower() if isinstance(element.tag, str) else ''
        attrs = element.attrib if tag else {}
        selected = (parent_selected or scope == 'page' or
                    tag == 'section' and {'desc', 'markdown'} <= set(attrs.get('class', '').split()) or
                    scope == 'prose' and tag == 'dd')
        skip = parent_skip or tag in {'code', 'pre', 'script', 'style', 'template', 'noscript'}
        atomic = parent_atomic
        if selected and not skip and tag in UNIT_TAGS and not atomic:
            flush()
            kind = tag
            atomic = True
        if tag in {'br', 'hr'}:
            parts.append(' ')
        if tag == 'a' and attrs.get('href'):
            parts.append(' ')
        if element.text and ((selected and not skip) or (element.getparent() is None and fragment)):
            parts.append(element.text)
        for child in element:
            visit(child, selected, skip, atomic)
            if child.tail and selected and not skip:
                parts.append(child.tail)
        if tag in UNIT_TAGS or tag in {'div', 'section', 'a', 'code', 'pre'}:
            parts.append(' ')
        if atomic and not parent_atomic:
            flush()
            kind = 'direct'

    visit(root, fragment, False, False)
    flush()
    return result


def units(markup, scope='prose', fragment=False):
    if lxml_html is not None:
        return units_lxml(markup, scope, fragment)
    return units_stdlib(markup, scope, fragment)


def plain(markup):
    return ' '.join(text for _, text in units(markup, fragment=True))


def clean(text):
    return IDENTIFIER.sub(' ', URL.sub(' ', text))


def word_matches(text):
    return list(WORDS.finditer(clean(text)))


def merged(mapping, page, default):
    if isinstance(default, dict):
        return dict(mapping.get(page, {}), **mapping.get('flutter/' + page, {}))
    return list(mapping.get(page, [])) + list(mapping.get('flutter/' + page, []))


def evidence(source, page, mappings, extras, fragments):
    section = re.search(r'<section class="desc markdown">(.*?)</section>', source, re.S)
    body = list(re.finditer(r'<(p|h[2-6])\b[^>]*>.*?</\1>', section[1], re.S)) if section else []
    summaries = list(re.finditer(r'<dd\b[^>]*>.*?</dd>', source, re.S))
    pairs = []
    for blocks, mapping in ((body, merged(mappings, page, {})), (summaries, merged(extras, page, {}))):
        for number, translation in mapping.items():
            index = int(number)
            if 0 <= index < len(blocks):
                pairs.append((blocks[index][0], translation))
    fragments = merged(fragments, page, [])
    pairs += [(f['source'], f['translation']) for f in fragments]
    result = []
    for old, new in pairs:
        for f in fragments:
            if f['source'] in new:
                new = new.replace(f['source'], f['translation'])
        old, new = plain(old), plain(translate_shared(new))
        if old and new and old != new and counts(new)['chinese_chars']:
            result.append((old, new))
    return result


def analyze(source_units, target_units, pairs):
    total = Counter(units=0, source_words=0, mapped_words=0, mapped_units=0,
                    partial_units=0, uncovered_units=0, alignment_mismatch_pages=0,
                    residual_candidates=0)
    details = []
    aligned = [k for k, _ in source_units] == [k for k, _ in target_units]
    if not aligned:
        total['alignment_mismatch_pages'] = 1
    for index, (kind, source) in enumerate(source_units):
        # Mask ignored text in place so word spans retain source offsets. This
        # avoids cleaning and tokenizing every source unit twice.
        masked = list(source)
        for pattern in (URL, IDENTIFIER):
            for match in pattern.finditer(source):
                masked[match.start():match.end()] = ' ' * len(match[0])
        word_spans = list(WORDS.finditer(''.join(masked)))
        if not word_spans:
            continue
        target = target_units[index][1] if aligned else None
        spans = []
        if target is not None:
            for old, new in pairs:
                # The mapped source and translation must both occur in this unit.
                if new in target:
                    start = 0
                    while (pos := source.find(old, start)) >= 0:
                        spans.append((pos, pos + len(old)))
                        start = pos + len(old)
        # Merge mapped ranges and sweep them alongside source words instead of
        # testing every word against every mapping range.
        spans.sort()
        merged_spans = []
        for start, end in spans:
            if merged_spans and start <= merged_spans[-1][1]:
                if end > merged_spans[-1][1]:
                    merged_spans[-1] = (merged_spans[-1][0], end)
            else:
                merged_spans.append((start, end))
        covered = 0
        span_index = 0
        for word in word_spans:
            while span_index < len(merged_spans) and merged_spans[span_index][1] <= word.start():
                span_index += 1
            if (span_index < len(merged_spans) and
                    merged_spans[span_index][0] <= word.start() and
                    word.end() <= merged_spans[span_index][1]):
                covered += 1
        status = ('mapped' if covered == len(word_spans) else 'partial' if covered or
                  target is not None and target != source and counts(target)['chinese_chars'] else 'uncovered')
        total.update(units=1, source_words=len(word_spans), mapped_words=covered)
        total[status + '_units'] += 1
        candidates = []
        if target is not None:
            for sentence in re.split(r'(?<=[.!?。！？;；])\s*|\n+', clean(target)):
                ordinary = [w[0] for w in WORDS.finditer(sentence) if w[0].islower() or w[0].istitle()]
                if len(ordinary) >= 4:
                    candidates.append(sentence.strip())
        total['residual_candidates'] += len(candidates)
        if status != 'mapped' or candidates:
            details.append(dict(unit=index, kind=kind, status=status, source_words=len(word_spans),
                                mapped_words=covered, source=source, target=target,
                                residual_candidates=candidates))
    return total, details


def summary(values):
    values = dict(values)
    denominator = values.get('source_words', 0)
    values['weighted_mapping_percent'] = round(values.get('mapped_words', 0) * 100 / denominator, 4) if denominator else None
    return values


def tree_report(rows):
    root = dict(name='flutter/', path='flutter/', children={}, values=Counter())
    for row in rows:
        node = root
        values = {k: v for k, v in row.items() if k not in {'page', 'weighted_mapping_percent'}}
        values['page_count'] = 1
        node['values'].update(values)
        parts = row['page'].removeprefix('flutter/').split('/')
        path = 'flutter'
        for part in parts:
            path += '/' + part
            node = node['children'].setdefault(part, dict(name=part, path=path, children={}, values=Counter()))
            node['values'].update(values)
    def finish(node):
        return dict(name=node['name'], path=node['path'], totals=summary(node['values']),
                    children=[finish(child) for _, child in sorted(node['children'].items(),
                              key=lambda item: (not bool(item[1]['children']), item[0].lower()))])
    return finish(root)


def write_tree(path, tree):
    payload = json.dumps(tree, ensure_ascii=False).replace('<', '\\u003c').replace('&', '\\u0026')
    document = '''<!doctype html><html lang="zh-CN"><meta charset="utf-8">
<title>Flutter 翻译覆盖率树形报告</title><style>
body{font:15px/1.65 system-ui,sans-serif;margin:32px;color:#233044;background:#f7f9fc}
h1{font-size:25px}p{max-width:1000px;color:#536278}main{background:white;padding:20px;border:1px solid #dde4ef;border-radius:10px}
details{margin-left:20px}summary{cursor:pointer;padding:5px 0}summary:hover,.leaf:hover{background:#eef4ff}
.name{display:inline-block;min-width:330px}.metrics{color:#52647b;font-size:13px}.leaf{margin-left:40px;padding:5px 0}
.low{color:#a94d19}button{padding:6px 12px;cursor:pointer}code{background:#edf0f5;padding:2px 5px}
</style><h1>Flutter 翻译覆盖率</h1>
<p>按库 → 子目录 → 页面展开。覆盖率 = 经中文站实际文本核对的映射所覆盖的原文词数 ÷ 原文总词数。
代码、网址和可识别的 API 标识符不计入词数。部分覆盖只计已核对的词，不把整段视为已译。
英文残留为至少含 4 个普通英文词的句子候选，需人工复核。映射覆盖率不代表翻译质量。</p>
<p>页面数字依次显示：加权覆盖率、映射词数/原文词数、已映射/部分/未覆盖单元数、英文候选数。
结构无法对齐的页面按 0 已验证覆盖计入，并单独标记。详细句子见同批生成的 JSONL 明细。</p>
<button id="collapse">收起所有</button><main id="tree"></main>
<script id="data" type="application/json">PAYLOAD</script><script>
const data=JSON.parse(document.getElementById('data').textContent);
function row(node){const v=node.totals,box=document.createElement('span');
 const name=document.createElement('span');name.className='name';name.textContent=node.name;box.append(name);
 const m=document.createElement('span');m.className='metrics';
 m.textContent=`${v.weighted_mapping_percent===null?'—':v.weighted_mapping_percent.toFixed(2)+'%'} · ${(v.mapped_words||0).toLocaleString()}/${(v.source_words||0).toLocaleString()} 词 · ${v.mapped_units||0}/${v.partial_units||0}/${v.uncovered_units||0} 单元 · 英文候选 ${v.residual_candidates||0}`+
 (v.alignment_mismatch_pages?` · 对齐异常 ${v.alignment_mismatch_pages} 页`:'');box.append(m);return box;}
function render(node,parent){if(!node.children.length){const leaf=document.createElement('div');leaf.className='leaf';leaf.title=node.path;leaf.append(row(node));parent.append(leaf);return;}
 const d=document.createElement('details'),s=document.createElement('summary');s.append(row(node));d.append(s);parent.append(d);
 let loaded=false;d.addEventListener('toggle',()=>{if(d.open&&!loaded){loaded=true;for(const child of node.children)render(child,d);}});return d;}
const root=render(data,document.getElementById('tree'));if(root)root.open=true;
document.getElementById('collapse').onclick=()=>document.querySelectorAll('details').forEach(d=>d.open=false);
</script></html>'''.replace('PAYLOAD', payload)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(document, encoding='utf-8')


def _init_worker():
    """Load large translation maps once per worker, not once per page."""
    global _WORKER_MAPPINGS, _WORKER_EXTRAS, _WORKER_FRAGMENTS
    _WORKER_MAPPINGS, _WORKER_EXTRAS, _WORKER_FRAGMENTS = [
        json.loads((DATA / name).read_text(encoding='utf-8')) for name in
        ('translations.json', 'translations-extra.json', 'translations-fragments.json')]


def _process_page(task):
    page, scope = task
    source = read_source(page)
    target = (ROOT / 'flutter.docs.cn' / 'flutter' / output_relative(page)).read_text(encoding='utf-8')
    stats, details = analyze(units(source, scope), units(target, scope),
                             evidence(source, page, _WORKER_MAPPINGS, _WORKER_EXTRAS,
                                      _WORKER_FRAGMENTS))
    return page, stats, details


def run(args, pages):
    totals = Counter()
    rows = []
    libraries = {}
    detail_path = args.details or DATA / 'language-stats' / 'coverage-details.jsonl'
    detail_path.parent.mkdir(parents=True, exist_ok=True)
    if args.workers == 1:
        _init_worker()
    with detail_path.open('w', encoding='utf-8') as detail_file:
        executor = (ProcessPoolExecutor(max_workers=args.workers, initializer=_init_worker)
                    if args.workers > 1 else nullcontext())
        with executor as pool:
            tasks = ((page, args.scope) for page in pages)
            results = (pool.map(_process_page, tasks, chunksize=16) if pool else
                       map(_process_page, tasks))
            for number, (page, stats, details) in enumerate(results, 1):
                totals.update(stats)
                library = page.split('/')[0]
                libraries.setdefault(library, Counter()).update(stats)
                rows.append(dict(page='flutter/' + page, **summary(stats)))
                for detail in details:
                    detail_file.write(json.dumps(dict(page='flutter/' + page, **detail), ensure_ascii=False) + '\n')
                if number % 5000 == 0:
                    print(f'Compared {number}/{len(pages)} pages', file=sys.stderr, flush=True)
    report = dict(method='source_word_weighted_mapping', scope=args.scope, page_count=len(pages),
                  totals=summary(totals), libraries={k: summary(v) for k, v in sorted(libraries.items())},
                  details=str(detail_path), pages=rows,
                  definition='Source English words covered by translation mappings whose Chinese text is present in the aligned site unit. This measures mapping coverage, not translation quality. Code, URLs and recognizable API identifiers excluded. Unaligned pages receive zero verified coverage.')
    output = args.json or DATA / 'language-stats' / 'coverage.json'
    tree = tree_report(rows)
    report['tree'] = tree
    tree_path = args.tree or output.with_suffix('.html')
    write_tree(tree_path, tree)
    report['tree_html'] = str(tree_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k not in {'pages', 'libraries', 'tree'}}, ensure_ascii=False, indent=2))
