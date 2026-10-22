from pathlib import Path
import json, re, sys
from case_paths import read_source,output_relative,rewrite_links
from shared_translation import translate_shared
data_root = Path(__file__).resolve().parent
root = data_root.parent
site_root = root / 'flutter.docs.cn'
source = root / 'flutter.docs' / 'flutter'
output = site_root / 'flutter'
translations = json.loads((data_root / 'translations.json').read_text(encoding='utf-8'))
extras = json.loads((data_root / 'translations-extra.json').read_text(encoding='utf-8'))
fragments = json.loads((data_root / 'translations-fragments.json').read_text(encoding='utf-8'))
missing = [] if '--pages-only' in sys.argv else [p.relative_to(source).as_posix() for p in source.rglob('*') if p.is_file() and not (output / p.relative_to(source)).is_file()]
if missing:
    raise RuntimeError(f'Missing {len(missing)} copied files: {missing[:10]}')
skipped_mappings = 0
reachable_file = data_root / 'reachable-pages.json'
reachable_pages = set(json.loads(reachable_file.read_text(encoding='utf-8'))['pages']) if reachable_file.is_file() else None
translation_pages = sorted({
    page.removeprefix('flutter/') for page in (*translations, *extras)
    if reachable_pages is None or 'flutter/' + page.removeprefix('flutter/') in reachable_pages
})
for page in translation_pages:
    entries = dict(translations.get(page, {}))
    entries.update(translations.get('flutter/' + page, {}))
    source_html = read_source(page)
    original = rewrite_links(source_html,'flutter/'+page)
    translated = (output / output_relative(page)).read_text(encoding='utf-8')
    section = re.search(r'<section class="desc markdown">(.*?)</section>', source_html, re.S)
    source_blocks = list(re.finditer(r'<(p|h[2-6])\b[^>]*>.*?</\1>', section.group(1), re.S)) if section else []
    for number, block in entries.items():
        # Snippet content can span parser blocks because its markup contains nested paragraphs;
        # snippet descriptions are checked through fragments below and code/links structurally.
        if '<div class="snippet' in block or '<div class="copyable-container' in block:
            continue
        index = int(number)
        if index >= len(source_blocks):
            skipped_mappings += 1
            continue
        source_block = source_blocks[index].group(0)
        source_hrefs = re.findall(r'<a\b[^>]*href="([^"]*)"[^>]*>.*?</a>', source_block, re.S)
        mapped_hrefs = re.findall(r'<a\b[^>]*href="([^"]*)"[^>]*>.*?</a>', block, re.S)
        code_pattern = r'<code\b.*?</code>'
        anchor_patterns = [r'\bid="([^"]*)"', r'\bname="([^"]*)"']
        anchors_match = all(sorted(re.findall(pattern, source_block, re.S)) == sorted(re.findall(pattern, block, re.S)) for pattern in anchor_patterns)
        if sorted(source_hrefs) != sorted(mapped_hrefs) or sorted(re.findall(code_pattern, source_block, re.S)) != sorted(re.findall(code_pattern, block, re.S)) or not anchors_match:
            # The applier deliberately leaves mappings that alter links, code, or anchors untouched.
            skipped_mappings += 1
            continue
        # Shared UI labels and separately translated snippet fragments can occur inside a mapped block.
        # Relative API links can depend on a document-level <base href>.
        # Include that context while rewriting this isolated description block.
        base_tags = re.findall(r'<base\b[^>]*>', source_html, re.I)
        expected = rewrite_links((base_tags[0] if base_tags else '') + block, 'flutter/'+page)
        expected = re.sub(r'<base\b[^>]*>', '', expected, count=1, flags=re.I)
        for fragment in fragments.get(page, []):
            fragment_source = rewrite_links(fragment['source'],'flutter/'+page)
            if fragment_source in expected:
                fragment_translation = rewrite_links(fragment['translation'],'flutter/'+page)
                expected = expected.replace(fragment_source,fragment_translation,1)
        expected = translate_shared(expected)
        assert expected in translated, page
    for block in extras.get(page, {}).values():
        assert block in translated, page
    page_fragments = list({item['source']: item for item in fragments.get(page, [])}.values())
    page_fragments = [item for item in page_fragments if not any(
        item['source'] != other['source'] and item['source'] in other['source']
        for other in page_fragments
    )]
    for fragment in page_fragments:
        if fragment['source'] not in original:
            continue
        fragment_hrefs = re.findall(r'<a\b[^>]*href="([^"]*)"[^>]*>.*?</a>', fragment['source'], re.S)
        translated_fragment_hrefs = re.findall(r'<a\b[^>]*href="([^"]*)"[^>]*>.*?</a>', fragment['translation'], re.S)
        fragment_code = r'<code\b.*?</code>'
        if sorted(fragment_hrefs) != sorted(translated_fragment_hrefs) or sorted(re.findall(fragment_code, fragment['source'], re.S)) != sorted(re.findall(fragment_code, fragment['translation'], re.S)):
            skipped_mappings += 1
            continue
        expected_fragment = rewrite_links(translate_shared(fragment['translation']), 'flutter/' + page)
        assert expected_fragment in translated, page
    for pattern in [r'href="([^"]*)"', r'\bid="([^"]*)"', r'<pre\b.*?</pre>', r'<code\b.*?</code>']:
        assert sorted(re.findall(pattern, original, re.S)) == sorted(re.findall(pattern, translated, re.S)), (page, pattern)
assert (output / 'static-assets' / 'styles.css').is_file()
assert not any((root / p.name).exists() for p in source.iterdir() if p.name != 'index.html'), 'Flattened documentation remains in root'
homepage_source = rewrite_links((root / 'flutter.docs' / 'index.html').read_text(encoding='utf-8'),'index.html')
homepage = (site_root / 'index.html').read_text(encoding='utf-8')
homepage_data = json.loads((data_root / 'homepage-translations.json').read_text(encoding='utf-8'))
for block in homepage_data.values():
    assert block in homepage
for pattern in [r'href="([^"]*)"', r'\bid="([^"]*)"', r'<pre\b.*?</pre>', r'<code\b.*?</code>']:
    assert sorted(re.findall(pattern, homepage_source, re.S)) == sorted(re.findall(pattern, homepage, re.S)), ('homepage', pattern)
assert 'URL=../index.html' in (output / 'index.html').read_text(encoding='utf-8')
sidebars = json.loads((data_root / 'translated-sidebars.json').read_text(encoding='utf-8'))
for sidebar in sidebars:
    sidebar_original = rewrite_links((source / sidebar).read_text(encoding='utf-8'),'flutter/'+sidebar)
    sidebar_translated = (output / sidebar).read_text(encoding='utf-8')
    for pattern in [r'href="([^"]*)"', r'\bid="([^"]*)"', r'<code\b.*?</code>']:
        assert sorted(re.findall(pattern, sidebar_original, re.S)) == sorted(re.findall(pattern, sidebar_translated, re.S)), (sidebar, pattern)
assert (data_root / '翻译进度.md').is_file()
print(f'Verified {"translated pages" if "--pages-only" in sys.argv else "complete source file copy"}, {len(translations)} translated library pages plus root homepage and Chinese redirect, {len(sidebars)} sidebar fragments, {sum(map(len, translations.values())) + len(homepage_data)} mapped description blocks ({skipped_mappings} skipped for mismatched markup or stale fragments), {sum(map(len, extras.values()))} library summary blocks, unchanged links/anchors/code.')



