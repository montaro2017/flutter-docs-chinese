from pathlib import Path
import json, re
from case_paths import read_source
p = Path(__file__).resolve().parent / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/CachingIterable-class.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
for i in range(19, 31):
 if i < 23:
  old = 'A maximal element of the iterable, or <code>null</code> if the iterable is empty.'
  new = '此可迭代对象中的一个最大元素；如果对象为空，则为 <code>null</code>。'
 elif i < 27:
  old = 'A minimal element of the iterable.'
  new = '此可迭代对象中的一个最小元素。'
 else:
  old = 'A minimal element of the iterable, or <code>null</code> it the iterable is empty.'
  new = '此可迭代对象中的一个最小元素；如果对象为空，则为 <code>null</code>。'
 assert old in blocks[i], i
 text = blocks[i].replace(old,new).replace('Available on ', '适用于 ').replace(',\n        provided by the ', '，\n        由 ').replace(' extension</span>', ' 扩展提供</span>').replace('>no setter<', '>无 setter<')
 d[page][str(i)] = text
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
