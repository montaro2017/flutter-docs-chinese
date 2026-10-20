from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/Unicode/ALM-constant.html'] = {'0': '<p><code>U+061C ARABIC LETTER MARK</code> 字符。</p>', '1': '<p>从右到左的零宽阿拉伯字符。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/Unicode-class.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
entries = {}
for i, block in enumerate(blocks):
 code = re.search(r'<code>.*?</code>', block, re.S).group(0)
 entries[str(i)] = block.replace('The ' + code + ' character.', code + ' 字符。')
d[page] = entries
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
