from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
t = json.loads((r / 'translations.json').read_text(encoding='utf-8'))
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/DiagnosticsSerializationDelegate-class.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
members = ('DiagnosticsSerializationDelegate', 'expandPropertyValues', 'includeProperties', 'subtreeDepth', 'additionalNodeProperties', 'copyWith', 'delegateForNode', 'filterChildren', 'filterProperties', 'truncateNodesList')
entries = {}
for i, member in enumerate(members, 1):
 member_page = f'foundation/DiagnosticsSerializationDelegate/{member}.html'
 desc = re.search(r'<section class="desc markdown">(.*?)</section>', read_source(member_page), re.S).group(1)
 src = re.search(r'<p>(.*?)</p>', desc, re.S).group(1)
 assert src in blocks[i]
 entries[str(i)] = blocks[i].replace(src, t[member_page]['0'][3:-4]).replace('no setter', '无 setter')
d[page] = entries
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
