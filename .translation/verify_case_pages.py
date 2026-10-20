from pathlib import Path
import json,zipfile,re
from case_paths import mapping,rewrite_links
ROOT=Path(__file__).resolve().parent.parent
SITE_ROOT=ROOT/'flutter.docs.cn'
paths=mapping()
translated=json.loads((ROOT/'.translation'/'translations.json').read_text(encoding='utf-8'))
assert len(paths)==len(set(p.casefold() for p in paths.values()))
with zipfile.ZipFile(ROOT/'flutter.docs'/'flutter.docs.zip') as archive:
    for original,target in paths.items():
        expected=rewrite_links(archive.read(original).decode('utf-8'),original,paths)
        actual=(SITE_ROOT/target).read_text(encoding='utf-8')
        if original[len('flutter/'):] not in translated:
            assert expected==actual,(original,target)
        else:
            for pattern in [r'href="([^"]*)"',r'\bid="([^"]*)"',r'<pre\b.*?</pre>',r'<code\b.*?</code>']:
                assert sorted(re.findall(pattern,expected,re.S))==sorted(re.findall(pattern,actual,re.S)),(original,target,pattern)
        assert rewrite_links(actual,target,paths)==actual,('non-idempotent',target)
property_page=SITE_ROOT/paths['flutter/animation/Threshold/threshold.html']
constructor_page=SITE_ROOT/paths['flutter/animation/Threshold/Threshold.html']
assert property_page.resolve()!=constructor_page.resolve()
assert any(s in property_page.read_text(encoding='utf-8') for s in ['<title>threshold property','<title>threshold 属性'])
assert any(s in constructor_page.read_text(encoding='utf-8') for s in ['<title>Threshold.new constructor','<title>Threshold.new 构造函数'])
for index in (SITE_ROOT/'flutter').glob('*.json'):
    text=index.read_text(encoding='utf-8')
    json.loads(text)
    for old,new in paths.items():
        if old==new: continue
        old=old[len('flutter/'):]
        assert '"'+old+'"' not in text,(index.name,old)
        assert '"'+old+'#' not in text,(index.name,old)
print(f'Verified {len(paths)} archive pages, distinct case-insensitive output names, content equality, and idempotent link normalization.')
