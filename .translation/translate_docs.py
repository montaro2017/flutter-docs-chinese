"""Apply reviewed Chinese HTML blocks without modifying source documentation."""
from pathlib import Path
import json, re, shutil, argparse, subprocess, sys, html
from shared_translation import translate_shared
from case_paths import read_source, output_relative, rewrite_links

DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
SOURCE = ROOT / 'flutter.docs' / 'flutter'
SITE_ROOT = ROOT / 'flutter.docs.cn'
OUTPUT = SITE_ROOT / 'flutter'
def blocks(text):
    section = re.search(r'<section class="desc markdown">(.*?)</section>', text, re.S)
    if not section:
        return []
    return list(re.finditer(r'<(p|h[2-6])\b[^>]*>.*?</\1>', section.group(1), re.S))

parser = argparse.ArgumentParser()
parser.add_argument('action', choices=['inspect', 'inspect-extra', 'apply', 'copy'])
parser.add_argument('page', nargs='?', default='all')
parser.add_argument('--from-page', help='for apply, skip sorted translation pages before this page')
parser.add_argument('--page-list', type=Path, help='for apply, limit output to source page paths listed one per line')
args = parser.parse_args()
if args.action == 'copy':
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for item in SOURCE.iterdir():
        target = OUTPUT / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)
    # Generated HTML references these sibling resources through ../assets etc.
    for name in ['assets', 'snippets']:
        if (SOURCE.parent / name).exists():
            shutil.copytree(SOURCE.parent / name, SITE_ROOT / name, dirs_exist_ok=True)
    if (DATA / 'case-paths.json').exists():
        subprocess.run([sys.executable, str(DATA / 'restore_case_pages.py')], check=True)
    print('Copied documentation to flutter.docs.cn/flutter/ with supporting assets.')
elif args.action == 'inspect-extra':
    text = read_source(args.page)
    for i, match in enumerate(re.finditer(r'<dd\b[^>]*>.*?</dd>', text, re.S)):
        print(f'{i}: {match.group(0)}')
elif args.action == 'inspect':
    text = read_source(args.page)
    for i, match in enumerate(blocks(text)):
        print(f'{i}: {match.group(0)}')
else:
    translations = json.loads((DATA / 'translations.json').read_text(encoding='utf-8'))
    selected_pages = None
    if args.page_list:
        selected_pages = {
            line.strip().removeprefix('flutter/')
            for line in args.page_list.read_text(encoding='utf-8').splitlines()
            if line.strip()
        }
    sidebars_file = DATA / 'translated-sidebars.json'
    sidebars = set(json.loads(sidebars_file.read_text(encoding='utf-8'))) if sidebars_file.exists() else set()
    extras_file = DATA / 'translations-extra.json'
    extras_all = json.loads(extras_file.read_text(encoding='utf-8')) if extras_file.exists() else {}
    fragments_file = DATA / 'translations-fragments.json'
    fragments_all = json.loads(fragments_file.read_text(encoding='utf-8')) if fragments_file.exists() else {}
    pages = sorted(
        {page.removeprefix('flutter/') for page in translations}
        | {page.removeprefix('flutter/') for page in extras_all}
        | {page.removeprefix('flutter/') for page in fragments_all}
    )
    target_page = args.page.removeprefix('flutter/')
    for page in pages:
        if args.from_page and page < args.from_page.removeprefix('flutter/'):
            continue
        if selected_pages is not None:
            if page not in selected_pages:
                continue
        elif args.page != "all":
            if target_page.endswith('*'):
                if not page.startswith(target_page[:-1]):
                    continue
            elif page != target_page:
                continue
        entries = dict(translations.get(page, {}))
        entries.update(translations.get('flutter/' + page, {}))
        try:
            text = read_source(page)
        except FileNotFoundError:
            print(f'{page}: skipped because the source page is missing')
            continue
        section = re.search(r'<section class="desc markdown">(.*?)</section>', text, re.S)
        matches = blocks(text)
        content = section.group(1) if section else ''
        for number, translated in sorted(entries.items(), key=lambda x:int(x[0]), reverse=True):
            if int(number) < 0 or int(number) >= len(matches):
                print(f'{page} block {number}: skipped out-of-range translation')
                continue
            match = matches[int(number)]
            # Preserve API destinations and inline code while allowing linked labels to be translated.
            source_hrefs = re.findall(r'<a\b[^>]*href="([^"]*)"[^>]*>.*?</a>', match.group(0), re.S)
            translated_hrefs = re.findall(r'<a\b[^>]*href="([^"]*)"[^>]*>.*?</a>', translated, re.S)
            if sorted(source_hrefs) != sorted(translated_hrefs):
                print(f'{page} block {number}: skipped translation with altered link destinations')
                continue
            pattern = r'<code\b.*?</code>'
            if sorted(re.findall(pattern, match.group(0), re.S)) != sorted(re.findall(pattern, translated, re.S)):
                print(f'{page} block {number}: skipped translation with altered inline code')
                continue
            altered_anchor = False
            for attribute in [r'\bid="([^"]*)"', r'\bname="([^"]*)"']:
                if sorted(re.findall(attribute, match.group(0), re.S)) != sorted(re.findall(attribute, translated, re.S)):
                    print(f'{page} block {number}: skipped translation with altered anchor attributes')
                    altered_anchor = True
                    break
            if altered_anchor:
                continue
            content = content[:match.start()] + translated + content[match.end():]
        if section:
            text = text[:section.start(1)] + content + text[section.end(1):]
        if extras_all:
            extras = extras_all.get(page, {})
            matches = list(re.finditer(r'<dd\b[^>]*>.*?</dd>', text, re.S))
            for number, translated in sorted(extras.items(), key=lambda x:int(x[0]), reverse=True):
                if int(number) < 0 or int(number) >= len(matches):
                    print(f'{page} summary {number}: skipped out-of-range summary')
                    continue
                match = matches[int(number)]
                for tag in ['a', 'code']:
                    pattern = rf'<{tag}\b[^>]*>.*?</{tag}>'
                    if sorted(re.findall(pattern, match.group(0), re.S)) != sorted(re.findall(pattern, translated, re.S)):
                        print(f'{page} summary {number}: skipped summary with altered {tag} markup')
                        break
                else:
                    text = text[:match.start()] + translated + text[match.end():]
                    continue
                continue
                text = text[:match.start()] + translated + text[match.end():]
        if fragments_all:
            fragments = list(fragments_all.get(page, [])) + list(fragments_all.get('flutter/' + page, []))
            fragments = list({item['source']: item for item in fragments}.values())
            fragments = [item for item in fragments if not any(item['source'] != other['source'] and item['source'] in other['source'] for other in fragments)]
            for fragment in fragments:
                old, new = fragment['source'], fragment['translation']
                if text.count(old) == 0 and new in text:
                    continue  # The containing translated block already includes this fragment.
                if text.count(old) != 1:
                    print(f'{page}: skipped fragment that does not match exactly once')
                    continue
                for pattern in [r'href="([^"]*)"', r'<code\b.*?</code>']:
                    if sorted(re.findall(pattern, old, re.S)) != sorted(re.findall(pattern, new, re.S)):
                        print(f'{page}: skipped fragment with altered link/code')
                        break
                else:
                    text = text.replace(old, new, 1)
                    continue
                continue
        text = translate_shared(text)
        text = text.replace('<html lang="en">', '<html lang="zh-CN">', 1)
        text = rewrite_links(text,'flutter/'+page)
        (OUTPUT / output_relative(page)).write_text(text, encoding='utf-8')
        for sidebar in re.findall(r'data-(?:above|below)-sidebar="([^"]+)"', text):
            sidebar = html.unescape(sidebar)
            sidebar_source = (SOURCE / sidebar).resolve()
            if not sidebar_source.is_relative_to(SOURCE.resolve()):
                raise ValueError('Sidebar outside source')
            if sidebar_source.is_file():
                sidebar_output = OUTPUT / sidebar
                if not sidebar_output.exists():
                    sidebar_output.parent.mkdir(parents=True, exist_ok=True)
                    sidebar_output.write_text(rewrite_links(translate_shared(sidebar_source.read_text(encoding='utf-8')),'flutter/'+sidebar),encoding='utf-8')
                sidebars.add(sidebar)
        print(f'{page}: translated {len(entries)}/{len(blocks(text))} description blocks')
    subprocess.run([sys.executable, str(DATA / 'homepage_translation.py')], check=True)
    sidebars_file.write_text(json.dumps(sorted(sidebars), indent=2),encoding='utf-8')
