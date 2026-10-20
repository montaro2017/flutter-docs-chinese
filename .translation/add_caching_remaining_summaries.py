from pathlib import Path
import json, re
from case_paths import read_source
p = Path(__file__).resolve().parent / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/CachingIterable-class.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
pairs = {
67: ('Creates a shuffled list of the elements of the iterable.', '创建一个包含此可迭代对象元素、顺序随机打乱的列表。'),
68: ('The single element satisfying <code>test</code>.', '满足 <code>test</code> 的唯一元素。'),
69: ('The single element satisfying <code>test</code>.', '满足 <code>test</code> 的唯一元素。'),
72: ('Contiguous slices of <code>this</code> with the given <code>length</code>.', '将 <code>this</code> 划分为给定 <code>length</code> 的连续切片。'),
77: ('Splits the elements into chunks after some elements.', '在某些元素之后将元素序列分块。'),
78: ('Splits the elements into chunks after some elements and indices.', '根据某些元素及其索引，在这些元素之后将序列分块。'),
79: ('Splits the elements into chunks before some elements.', '在某些元素之前将元素序列分块。'),
80: ('Splits the elements into chunks before some elements and indices.', '根据某些元素及其索引，在这些元素之前将序列分块。'),
81: ('Splits the elements into chunks between some elements.', '在某些元素之间将元素序列分块。'),
82: ('Splits the elements into chunks between some elements and indices.', '根据某些元素及其索引，在元素之间将序列分块。'),
87: ('The elements whose value and index satisfies <code>test</code>.', '值与索引满足 <code>test</code> 的元素。'),
88: ('The elements that do not satisfy <code>test</code>.', '不满足 <code>test</code> 的元素。'),
89: ('The elements whose value and index do not satisfy <code>test</code>.', '值与索引不满足 <code>test</code> 的元素。'),
90: ('The non-<code>null</code> elements of this <code>Iterable</code>.', '此 <code>Iterable</code> 中非 <code>null</code> 的元素。'),
}
for i in range(73,77):
 pairs[i] = ('Creates a sorted list of the elements of the iterable.', '创建一个包含此可迭代对象元素的已排序列表。')
for i, (old,new) in pairs.items():
 assert old in blocks[i], i
 d[page][str(i)] = blocks[i].replace(old,new).replace('Available on ', '适用于 ').replace(',\n        provided by the ', '，\n        由 ').replace(' extension</span>', ' 扩展提供</span>')
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
