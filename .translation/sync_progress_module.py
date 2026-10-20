"""Update one pending-only module ledger after applying a translation batch.

Usage: python sync_progress_module.py material/ToggleButtons.md
The path is relative to .translation/progress/ and points to an existing module
ledger. Completed modules are removed from indexes and no longer need reading.
"""
from pathlib import Path
import argparse, json, re
from datetime import date
from case_paths import output_relative, read_source, rewrite_links
from shared_translation import translate_shared

ap = argparse.ArgumentParser()
ap.add_argument('module', help='module ledger relative to progress/, e.g. material/ToggleButtons.md')
ap.add_argument('--dry-run', action='store_true')
args = ap.parse_args()
root = Path(__file__).resolve().parent.parent
data = root / '.translation'
progress = data / 'progress'
ledger = progress / args.module
if not ledger.is_file():
    raise SystemExit(f'Module ledger not found (completed modules have no ledger): {args.module}')
module_parts = Path(args.module.replace('\\', '/')).parts

text = ledger.read_text(encoding='utf-8')
mapping_all = json.loads((data / 'translations.json').read_text(encoding='utf-8'))
fragments_all = json.loads((data / 'translations-fragments.json').read_text(encoding='utf-8'))
head = re.search(r'模块共 ([\d,]+) 页：已完整 ([\d,]+) 页，部分翻译 ([\d,]+) 页，未翻译 ([\d,]+) 页；正文已译 ([\d,]+)/([\d,]+) 段。', text)
if not head:
    raise SystemExit(f'Unrecognized module summary: {ledger}')
pages_n, complete_n, partial_n, untranslated_n, translated_n, body_n = [int(x.replace(',', '')) for x in head.groups()]
old_translated_n = translated_n
line_re = re.compile(r'^- `([^`]+)` — (部分|未译)；已译 ([\d,]+)/([\d,]+) 段；待译段落：.*$', re.M)

def get_blocks(html_text):
    section = re.search(r'<section class="desc markdown">(.*?)</section>', html_text, re.S)
    return [] if section is None else list(re.finditer(r'<(p|h[2-6])\b[^>]*>.*?</\1>', section.group(1), re.S))

def page_mapping(page):
    normalized = page.removeprefix('flutter/')
    merged = dict(mapping_all.get(normalized, {}))
    merged.update(mapping_all.get('flutter/' + normalized, {}))
    return merged

def covered_fragments(page):
    fragment_entries = list(fragments_all.get(page, [])) + list(fragments_all.get('flutter/' + page, []))
    fragments = list({item['source']: item for item in fragment_entries}.values())
    fragments = [item for item in fragments if not any(item['source'] != other['source'] and item['source'] in other['source'] for other in fragments)]
    if not fragments:
        return set()
    source_page = page.removeprefix('flutter/')
    source_html = read_source(source_page)
    output_html = (root / 'flutter.docs.cn' / 'flutter' / output_relative(source_page)).read_text(encoding='utf-8')
    fragment_html = source_html
    for item in fragments:
        if fragment_html.count(item['source']) == 1:
            fragment_html = fragment_html.replace(item['source'], item['translation'], 1)
    source_blocks, fragment_blocks = get_blocks(source_html), get_blocks(fragment_html)
    expected_html = rewrite_links(translate_shared(fragment_html), 'flutter/' + source_page)
    expected_blocks, output_blocks = get_blocks(expected_html), get_blocks(output_html)
    mapped = {int(i) for i in page_mapping(page)}
    result = set()
    for i, match in enumerate(source_blocks):
        if i in mapped or i >= len(output_blocks) or i >= len(fragment_blocks) or i >= len(expected_blocks):
            continue
        fragment_changed = fragment_blocks[i].group(0) != match.group(0)
        if fragment_changed and expected_blocks[i].group(0) == output_blocks[i].group(0):
            result.add(i)
    return result

pending_pages = {match.group(1).removeprefix('flutter/') for match in line_re.finditer(text)}
fragment_coverage = {page: covered_fragments(page) for page in pending_pages if page in fragments_all or 'flutter/' + page in fragments_all}
candidate_pages = {page.removeprefix('flutter/') for page in mapping_all}
candidate_pages.update(page.removeprefix('flutter/') for page in fragments_all)
rows = []
for m in line_re.finditer(text):
    path = m.group(1).removeprefix('flutter/')
    source = read_source(path)
    blocks = get_blocks(source)
    mapping = page_mapping(path)
    valid = {int(i) for i in mapping if 0 <= int(i) < len(blocks)} | fragment_coverage.get(path, set())
    count = len(valid)
    status = 'complete' if len(blocks) == count else 'partial' if count else 'untranslated'
    pending = ', '.join(str(i) for i in range(len(blocks)) if i not in valid) or '无'
    rows.append({'path': m.group(1), 'old_status': m.group(2), 'old_count': int(m.group(3).replace(',', '')),
                 'blocks': len(blocks), 'count': count, 'status': status, 'pending': pending})

for row in rows:
    if row['old_status'] == '部分':
        partial_n -= 1
    else:
        untranslated_n -= 1
    translated_n += row['count'] - row['old_count']
    if row['status'] == 'complete':
        complete_n += 1
    elif row['status'] == 'partial':
        partial_n += 1
    else:
        untranslated_n += 1

name = text.splitlines()[0].removeprefix('# ').removesuffix(' 待翻译清单').split(' / ', 1)[-1]
new_rows = [r for r in rows if r['status'] != 'complete']
new_text = re.sub(r'模块共 .*?。',
                  f'模块共 {pages_n:,} 页：已完整 {complete_n:,} 页，部分翻译 {partial_n:,} 页，未翻译 {untranslated_n:,} 页；正文已译 {translated_n:,}/{body_n:,} 段。', text, count=1)
for row in rows:
    if row['status'] == 'complete':
        line = f"- `{row['path']}` — {row['old_status']}；已译 {row['old_count']}/{row['blocks']} 段；待译段落："
        # Replace the exact old row even when its pending list was nonempty.
        pattern = re.compile(r'^- `' + re.escape(row['path']) + r'` — .*$', re.M)
        new_text = pattern.sub('', new_text)
    else:
        status_label = '部分' if row['status'] == 'partial' else '未译'
        replacement = f"- `{row['path']}` — {status_label}；已译 {row['count']}/{row['blocks']} 段；待译段落：{row['pending']}"
        pattern = re.compile(r'^- `' + re.escape(row['path']) + r'` — .*$', re.M)
        new_text = pattern.sub(lambda _: replacement, new_text)
new_text = re.sub(r'\n{3,}', '\n\n', new_text).rstrip() + '\n'

idx_path = ledger.parent / 'README.md'
idx = idx_path.read_text(encoding='utf-8')
if new_rows:
    summary = f"- [{name}](./{ledger.name})"
    pattern = re.compile(r'^- \[' + re.escape(name) + r'\]\(\./' + re.escape(ledger.name) + r'\)(?: — .*)?$', re.M)
    if pattern.search(idx):
        idx_new = pattern.sub(lambda _: summary, idx)
    else:
        idx_new = idx.rstrip() + '\n' + summary + '\n'
else:
    pattern = re.compile(r'^- \[' + re.escape(name) + r'\]\(\./' + re.escape(ledger.name) + r'\)(?: — .*)?\n?', re.M)
    idx_new = pattern.sub('', idx)

# Material's root index routes through letter-group files. Keep that second
# level in sync as module ledgers are created or removed.
if module_parts[0] == 'material':
    letter = name[0].upper()
    group_path = ledger.parent / f'group-{letter}.md'
    if group_path.is_file():
        group_text = group_path.read_text(encoding='utf-8')
        group_pattern = re.compile(r'^- \[' + re.escape(name) + r'\]\(\./' + re.escape(ledger.name) + r'\)\n?', re.M)
        if new_rows:
            group_line = f'- [{name}](./{ledger.name})'
            if group_pattern.search(group_text):
                group_text = group_pattern.sub(lambda _: group_line + '\n', group_text)
            else:
                group_text = group_text.rstrip() + '\n' + group_line + '\n'
        else:
            group_text = group_pattern.sub('', group_text)
        # Remove old links that no longer have a module ledger.
        group_text = re.sub(
            r'^- \[([^]]+)\]\(\./([^/)]+\.md)\)\n?',
            lambda m: m.group(0) if (ledger.parent / m.group(2)).is_file() else '',
            group_text, flags=re.M)
        group_links = [line for line in group_text.splitlines() if line.startswith('- [')]
        if group_links:
            if not group_text.endswith('\n'):
                group_text += '\n'
            if not args.dry_run:
                group_path.write_text(group_text, encoding='utf-8')
            if not re.search(r'^- \[' + re.escape(letter) + r' 组\]\(\./group-' + re.escape(letter) + r'\.md\)$', idx_new, re.M):
                idx_new = idx_new.rstrip() + f'\n- [{letter} 组](./group-{letter}.md)\n'
        else:
            if not args.dry_run:
                group_path.unlink(missing_ok=True)
            idx_new = re.sub(r'^- \[' + re.escape(letter) + r' 组\]\(\./group-' + re.escape(letter) + r'\.md\)\n?', '', idx_new, flags=re.M)

# Maintain concise library and module indexes, removing completed entries.
if module_parts[0] != 'material':
    lib = module_parts[1]
    lib_dir = progress / 'libraries' / lib
    module_files = sorted((p for p in lib_dir.glob('*.md') if p.name != 'README.md'), key=lambda p:p.name.lower())
    lib_index_path = lib_dir / 'README.md'
    if module_files:
        links = [f"- [{p.stem}](./{p.name})" for p in module_files]
        lib_index_path.write_text(f"# {lib} 待翻译模块\n\n仅列出仍有正文待译的模块；选定后再打开清单查看具体页面与段落。\n\n" + "\n".join(links) + "\n", encoding='utf-8')
    else:
        lib_index_path.unlink(missing_ok=True)
    root_index = progress / 'libraries' / 'README.md'
    root_lines = [line for line in root_index.read_text(encoding='utf-8').splitlines() if line.startswith('- [')]
    root_lines = [line for line in root_lines if not line.startswith(f"- [{lib}](")]
    if module_files:
        root_lines.append(f"- [{lib}](./{lib}/README.md)")
    root_lines.sort(key=lambda line:line.lower())
    root_index.write_text("# 其他库索引\n\n仅列出仍有正文待译的库。处理某个库时，再打开该库索引选择未完成模块。\n\n" + "\n".join(root_lines) + ("\n" if root_lines else ""), encoding='utf-8')

state_path = data / '页面翻译状态.json'
state = json.loads(state_path.read_text(encoding='utf-8'))
total_translated = state['totals']['translated_blocks'] + translated_n - old_translated_n
state['totals']['translated_blocks'] = total_translated
state['totals']['pending_blocks'] = state['totals']['body_blocks'] - total_translated
state['totals']['complete_pages'] += complete_n - int(head.group(2).replace(',', ''))
state['totals']['partial_pages'] += partial_n - int(head.group(3).replace(',', ''))
state['totals']['untranslated_pages'] += untranslated_n - int(head.group(4).replace(',', ''))
if module_parts[0] == 'material':
    mat = state['material']
    mat['translated_blocks'] += translated_n - old_translated_n
    mat['pending_blocks'] = mat['body_blocks'] - mat['translated_blocks']
    mat['complete_pages'] += complete_n - int(head.group(2).replace(',', ''))
    mat['partial_pages'] += partial_n - int(head.group(3).replace(',', ''))
    mat['untranslated_pages'] += untranslated_n - int(head.group(4).replace(',', ''))
else:
    lib = module_parts[1]
    if lib in state.get('libraries', {}):
        summary = state['libraries'][lib]
        for k, value in [('complete_pages', complete_n), ('partial_pages', partial_n), ('untranslated_pages', untranslated_n)]:
            old_value = int(head.group({'complete_pages': 2, 'partial_pages': 3, 'untranslated_pages': 4}[k]).replace(',', ''))
            summary[k] += value - old_value
        summary['translated_blocks'] += translated_n - old_translated_n
        summary['pending_blocks'] = summary['body_blocks'] - summary['translated_blocks']

report = {
    'module': args.module, 'updated_pages': len(rows), 'remaining_pages': len(new_rows),
    'module_complete': not new_rows, 'translated_blocks': total_translated,
    'material_translated_blocks': state['material']['translated_blocks'],
}
if not args.dry_run:
    if new_rows:
        ledger.write_text(new_text, encoding='utf-8')
    else:
        ledger.unlink()
    idx_path.write_text(idx_new, encoding='utf-8')
    # Rebuild the library index after removing the completed ledger. The
    # earlier index update runs before this unlink and can otherwise leave a
    # stale README entry for a library whose last module just completed.
    if module_parts[0] != 'material':
        lib_dir = progress / 'libraries' / module_parts[1]
        module_files = sorted(
            (item for item in lib_dir.glob('*.md') if item.name != 'README.md'),
            key=lambda item: item.name.lower())
        lib_index_path = lib_dir / 'README.md'
        if module_files:
            links = [f"- [{item.stem}](./{item.name})" for item in module_files]
            lib_index_path.write_text(
                f"# {module_parts[1]} 待翻译模块\n\n仅列出仍有正文待译的模块；选定后再打开清单查看具体页面与段落。\n\n"
                + "\n".join(links) + "\n", encoding='utf-8')
        else:
            lib_index_path.unlink(missing_ok=True)
        root_index = progress / 'libraries' / 'README.md'
        root_lines = [line for line in root_index.read_text(encoding='utf-8').splitlines()
                      if line.startswith('- [') and not line.startswith(f"- [{module_parts[1]}](")]
        if module_files:
            root_lines.append(f"- [{module_parts[1]}](./{module_parts[1]}/README.md)")
        root_lines.sort(key=lambda line: line.lower())
        root_index.write_text(
            "# 其他库索引\n\n仅列出仍有正文待译的库。处理某个库时，再打开该库索引选择未完成模块。\n\n"
            + "\n".join(root_lines) + ("\n" if root_lines else ""), encoding='utf-8')
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    p = data / '翻译进度.md'
    overview = p.read_text(encoding='utf-8')
    mat = state['material']
    overall_percent = total_translated * 100 / state['totals']['body_blocks']
    status_line = (
        f"**最新状态（{date.today().isoformat()}）**：全站正文已译 {total_translated:,}/"
        f"{state['totals']['body_blocks']:,} 段（约 {overall_percent:.1f}%）；"
        f"Material 已译 {mat['translated_blocks']:,}/{mat['body_blocks']:,} 段"
        f"（剩 {mat['pending_blocks']:,} 段）。"
    )
    overview = re.sub(r'^\*\*最新状态（.*?）\*\*：.*$', status_line, overview, count=1, flags=re.M)
    p.write_text(overview, encoding='utf-8')

    if module_parts[0] == 'material':
        material_dir = progress / 'material'
        pending_modules = sorted(
            (item for item in material_dir.glob('*.md')
             if item.name not in {'README.md'} and not item.name.startswith('group-')),
            key=lambda item: item.name.lower())
        grouped = {}
        for item in pending_modules:
            grouped.setdefault(item.stem[0].upper(), []).append(item)
        for group_file in material_dir.glob('group-*.md'):
            letter = group_file.stem.removeprefix('group-')
            if letter not in grouped:
                group_file.unlink(missing_ok=True)
        for letter, items in grouped.items():
            group_file = material_dir / f'group-{letter}.md'
            lines = [f'- [{item.stem}](./{item.name})' for item in items]
            group_file.write_text(
                f'# Material / {letter} 组未完成模块\n\n' + '\n'.join(lines) + '\n',
                encoding='utf-8')
        root_links = [f'- [{letter} 组](./group-{letter}.md)' for letter in sorted(grouped)]
        (material_dir / 'README.md').write_text(
            '# Material 模块索引\n\n仅列出仍有正文待译的模块。按组件名首字母打开分组，再选取一个未完成模块；具体页面和待译段落只在对应模块清单中查看。\n\n'
            + '\n'.join(root_links) + ('\n' if root_links else ''),
            encoding='utf-8')
print(json.dumps(report, ensure_ascii=False))
