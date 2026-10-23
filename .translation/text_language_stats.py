"""Extract translation-scope prose and count Han characters / ASCII letters."""
import argparse
from collections import Counter
from html.parser import HTMLParser
import json
import os
from pathlib import Path

from case_paths import output_relative, read_source

DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
BLOCK = {'p', 'div', 'section', 'dd', 'dt', 'li', 'ul', 'ol', 'blockquote', 'br', 'tr', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}


class ProseParser(HTMLParser):
    def __init__(self, scope='prose', include_code=False):
        super().__init__(convert_charrefs=True)
        self.scope = scope
        self.include_code = include_code
        self.stack = []
        self.parts = []

    def handle_starttag(self, tag, attrs):
        classes = set(dict(attrs).get('class', '').split())
        selected = (self.scope == 'page' or
                    tag == 'section' and {'desc', 'markdown'} <= classes or
                    self.scope == 'prose' and tag == 'dd')
        parent_selected = self.stack[-1][1] if self.stack else False
        parent_skip = self.stack[-1][2] if self.stack else False
        skip = parent_skip or tag in {'script', 'style', 'template', 'noscript'} or (
            not self.include_code and tag in {'code', 'pre'})
        if tag in BLOCK:
            self.parts.append('\n')
        if tag not in VOID:
            self.stack.append((tag, selected or parent_selected, skip))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break
        if tag in BLOCK:
            self.parts.append('\n')

    def handle_data(self, data):
        if self.stack and self.stack[-1][1] and not self.stack[-1][2]:
            self.parts.append(data)

    def text(self):
        return '\n'.join(line for raw in ''.join(self.parts).splitlines()
                         if (line := ' '.join(raw.split())))


def counts(text):
    han = sum(0x3400 <= ord(c) <= 0x4DBF or 0x4E00 <= ord(c) <= 0x9FFF or
              0xF900 <= ord(c) <= 0xFAFF or 0x20000 <= ord(c) <= 0x2FA1F or
              0x30000 <= ord(c) <= 0x323AF for c in text)
    english = sum('a' <= c <= 'z' or 'A' <= c <= 'Z' for c in text)
    return {'chinese_chars': han, 'english_letters': english,
            'other_nonspace_chars': sum(not c.isspace() for c in text) - han - english}


def ratios(values):
    total = values['chinese_chars'] + values['english_letters']
    return dict(values, chinese_percent=round(values['chinese_chars'] * 100 / total, 4) if total else None,
                english_percent=round(values['english_letters'] * 100 / total, 4) if total else None)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--method', choices=['characters', 'coverage'], default='characters')
    ap.add_argument('--details', type=Path, help='coverage: write unresolved units and English candidates as JSONL')
    ap.add_argument('--tree', type=Path, help='coverage: write an offline expandable HTML tree')
    ap.add_argument('--source', choices=['site', 'original'], default='site', help='site=flutter.docs.cn; original=flutter.docs')
    ap.add_argument('--scope', choices=['body', 'prose', 'page'], default='prose', help='body=description; prose=description + dd summaries; page=all text')
    ap.add_argument('--page', action='append', default=[], help='API page or library prefix, e.g. flutter/widgets/ (repeatable)')
    ap.add_argument('--include-code', action='store_true')
    ap.add_argument('--workers', type=int, default=min(8, os.cpu_count() or 1),
                    help='coverage: parallel page workers (default: up to 8)')
    ap.add_argument('--text-dir', type=Path, help='export UTF-8 plain text preserving page paths')
    ap.add_argument('--json', type=Path, help='write totals and per-page counts')
    args = ap.parse_args()
    inventory = json.loads((DATA / 'reachable-pages.json').read_text(encoding='utf-8'))
    prefixes = [p.replace('\\', '/').removeprefix('flutter/').rstrip('*') for p in args.page]
    pages = sorted({p.removeprefix('flutter/') for p in inventory['pages']
                    if p.startswith('flutter/') and p.endswith('.html')})
    if prefixes:
        pages = [p for p in pages if any(p == s or s.endswith('/') and p.startswith(s) for s in prefixes)]
    if not pages:
        ap.error('No reachable API pages match --page')
    if args.method == 'coverage':
        if args.workers < 1:
            ap.error('--workers must be at least 1')
        if args.source != 'site' or args.scope == 'page' or args.include_code or args.text_dir:
            ap.error('coverage requires --source site, --scope body/prose, and no --include-code/--text-dir')
        from translation_coverage import run
        run(args, pages)
        return
    totals = Counter(chinese_chars=0, english_letters=0, other_nonspace_chars=0)
    rows = []
    for page in pages:
        relative = output_relative(page)
        markup = (read_source(page) if args.source == 'original' else
                  (ROOT / 'flutter.docs.cn' / 'flutter' / relative).read_text(encoding='utf-8'))
        parser = ProseParser(args.scope, args.include_code)
        parser.feed(markup)
        parser.close()
        text = parser.text()
        result = counts(text)
        totals.update(result)
        rows.append(dict(page='flutter/' + page, **ratios(result)))
        if args.text_dir:
            target = args.text_dir / 'flutter' / Path(relative).with_suffix('.txt')
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text + '\n', encoding='utf-8')
    report = dict(source=args.source, scope=args.scope, include_code=args.include_code,
                  denominator='chinese_chars + english_letters; punctuation, digits and whitespace excluded',
                  page_count=len(rows), totals=ratios(totals), pages=rows)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'pages'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
