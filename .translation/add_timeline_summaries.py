from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
translations = json.loads((r / 'translations.json').read_text(encoding='utf-8'))
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/FlutterTimeline-class.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
members = ('debugCollectionEnabled', 'now', 'debugCollect', 'debugReset', 'finishSync', 'instantSync', 'startSync', 'timeSync')
entries = {}
for i, member in enumerate(members):
 member_page = f'foundation/FlutterTimeline/{member}.html'
 desc = re.search(r'<section class="desc markdown">(.*?)</section>', read_source(member_page), re.S).group(1)
 source = re.search(r'<p>(.*?)</p>', desc, re.S).group(1)
 assert source in blocks[i]
 entries[str(i)] = blocks[i].replace(source, translations[member_page]['0'][3:-4]).replace('getter/setter pair', 'getter/setter 对').replace('no setter', '无 setter')
d[page] = entries
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
