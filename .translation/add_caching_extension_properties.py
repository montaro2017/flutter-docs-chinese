from pathlib import Path
import json, re
from case_paths import read_source
p = Path(__file__).resolve().parent / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/CachingIterable-class.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
pairs = {
 'The arithmetic mean of the elements of a non-empty iterable.': '非空可迭代对象中元素的算术平均值。',
 'The first element, or <code>null</code> if the iterable is empty.': '第一个元素；如果可迭代对象为空，则为 <code>null</code>。',
 'The first element of this iterator, or <code>null</code> if the iterable is empty.': '此迭代器的第一个元素；如果可迭代对象为空，则为 <code>null</code>。',
 'The sequential elements of each iterable in this iterable.': '按顺序连接此可迭代对象中每个可迭代对象的元素。',
 'The unique sequential elements of each iterable in this iterable.': '按顺序连接此可迭代对象中每个可迭代对象的元素，并去除重复元素。',
 'Pairs of elements of the indices and elements of this iterable.': '由此可迭代对象的索引与对应元素组成的配对。',
 'The last element, or <code>null</code> if the iterable is empty.': '最后一个元素；如果可迭代对象为空，则为 <code>null</code>。',
 'The last element of this iterable, or <code>null</code> if the iterable is empty.': '此可迭代对象的最后一个元素；如果对象为空，则为 <code>null</code>。',
 'A maximal element of the iterable.': '此可迭代对象中的一个最大元素。',
}
for i in [3,4,5,6,7,8,9,10,12,13,15,16,17,18]:
 text = blocks[i]
 matches = [(a,b) for a,b in pairs.items() if a in text]
 assert len(matches) == 1, i
 old, new = matches[0]
 text = text.replace(old,new).replace('Available on ', '适用于 ').replace(',\n        provided by the ', '，\n        由 ').replace(' extension</span>', ' 扩展提供</span>').replace('>no setter<', '>无 setter<')
 d[page][str(i)] = text
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
