from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
translations = json.loads((r / 'translations.json').read_text(encoding='utf-8'))
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
members = {
 'TimedBlock': ['TimedBlock', 'duration', 'end', 'name', 'start'],
 'AggregatedTimedBlock': ['AggregatedTimedBlock', 'count', 'duration', 'name'],
 'AggregatedTimings': ['AggregatedTimings', 'aggregatedBlocks', 'timedBlocks', 'getAggregated'],
}
for cls, names in members.items():
 page = f'foundation/{cls}-class.html'
 blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
 entries = {}
 for i, member in enumerate(names, 1):
  member_page = f'foundation/{cls}/{member}.html'
  desc = re.search(r'<section class="desc markdown">(.*?)</section>', read_source(member_page), re.S).group(1)
  src = re.search(r'<p>(.*?)</p>', desc, re.S).group(1)
  dst = translations[member_page]['0'][3:-4]
  assert src in blocks[i]
  entries[str(i)] = blocks[i].replace(src, dst).replace('no setter', '无 setter')
 if cls != 'AggregatedTimings':
  i = len(names) + 1
  entries[str(i)] = blocks[i].replace('A string representation of this object.', '此对象的字符串表示。').replace('>override<', '>重写<')
 d[page] = entries
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
