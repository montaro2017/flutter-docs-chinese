from pathlib import Path
import json, re, html
from case_paths import rewrite_links
data_root = Path(__file__).resolve().parent
root = data_root.parent
site_root = root / 'flutter.docs.cn'
source = (root / 'flutter.docs' / 'index.html').read_text(encoding='utf-8')
section = re.search(r'<section class="desc markdown">(.*?)</section>', source, re.S)
matches = list(re.finditer(r'<(p|h[1-6])\b[^>]*>.*?</\1>', section.group(1), re.S))
data_file = data_root / 'homepage-translations.json'
if not data_file.exists():
    for i, match in enumerate(matches):
        print(f'{i}: {match.group(0)}')
else:
    translations = json.loads(data_file.read_text(encoding='utf-8'))
    body = section.group(1)
    for key, translated in sorted(translations.items(), key=lambda x:int(x[0]), reverse=True):
        match = matches[int(key)]
        for pattern in [r'href="([^"]*)"', r'\bid="([^"]*)"', r'<code\b.*?</code>']:
            assert sorted(re.findall(pattern, match.group(0), re.S)) == sorted(re.findall(pattern, translated, re.S)), key
        body = body[:match.start()] + translated + body[match.end():]
    output = source[:section.start(1)] + body + source[section.end(1):]
    output = output.replace('<html lang="en">', '<html lang="zh-CN">', 1)
    labels = json.loads((data_root / 'homepage-labels.json').read_text(encoding='utf-8'))
    applied = set()
    def translate_label(match):
        raw = match.group(1)
        key = ' '.join(html.unescape(raw).split())
        if key not in labels:
            return match.group(0)
        applied.add(key)
        leading = raw[:len(raw)-len(raw.lstrip())]
        trailing = raw[len(raw.rstrip()):]
        return '>' + leading + html.escape(labels[key]) + trailing + '<'
    output = re.sub(r'>([^<>]+)<', translate_label, output)
    output = output.replace('content="Flutter API docs, for the Dart programming language."', 'content="Flutter API 中文文档，适用于 Dart 编程语言。"')
    output = output.replace('placeholder="Loading search..."', 'placeholder="正在加载搜索…"')
    output = output.replace('title="Toggle between light and dark mode"', 'title="切换浅色与深色模式"')
    output = output.replace('aria-label="Light and dark mode toggle"', 'aria-label="切换浅色与深色模式"')
    output = rewrite_links(output,'index.html')
    source = rewrite_links(source,'index.html')
    (site_root / 'index.html').write_text(output, encoding='utf-8')
    # Keep the original redirect target, adding a translated accessible fallback.
    (site_root / 'flutter' / 'index.html').write_text('<!doctype html>\n<html lang="zh-CN"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;URL=../index.html"><title>Flutter 中文 API 文档</title></head><body><p>正在跳转到 <a href="../index.html">Flutter 中文 API 文档首页</a>。</p></body></html>\n', encoding='utf-8')
    for pattern in [r'href="([^"]*)"', r'\bid="([^"]*)"', r'<pre\b.*?</pre>', r'<code\b.*?</code>']:
        assert sorted(re.findall(pattern, source, re.S)) == sorted(re.findall(pattern, output, re.S)), pattern
    print(f'Root homepage: {len(translations)}/{len(matches)} description blocks and {len(applied)} unique labels/summaries translated; links, anchors and code verified.')
