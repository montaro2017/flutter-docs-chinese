from pathlib import Path
import json, re
from case_paths import read_source
p = Path(__file__).resolve().parent / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/CachingIterable-class.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
pairs = {
55: ('Whether the elements are sorted by the <code>compare</code> ordering.', '元素是否已按 <code>compare</code> 定义的顺序排序。'),
56: ('Whether the elements are sorted by the <code>compare</code> ordering.', '元素是否已按 <code>compare</code> 定义的顺序排序。'),
57: ('Whether the elements are sorted by their <code>keyOf</code> property.', '元素是否已按 <code>keyOf</code> 得到的键排序。'),
58: ('Whether the elements are <code>compare</code>-sorted by their <code>keyOf</code> property.', '元素是否已使用 <code>compare</code>，按 <code>keyOf</code> 得到的键排序。'),
59: ('Associates the elements in <code>this</code> by the value returned by <code>key</code>.', '将 <code>this</code> 中的元素关联到 <code>key</code> 返回的值。'),
60: ('The last element whose index and value satisfies <code>test</code>.', '索引与值满足 <code>test</code> 的最后一个元素。'),
61: ('The last element satisfying <code>test</code>, or <code>null</code> if there are none.', '满足 <code>test</code> 的最后一个元素；如果没有，则为 <code>null</code>。'),
63: ('Maps each element and its index to a new value.', '将每个元素及其索引映射为一个新值。'),
64: ('Whether no element satisfies <code>test</code>.', '是否没有任何元素满足 <code>test</code>。'),
65: ('Combine the elements with each other and the current index.', '结合当前索引，将元素彼此合并。'),
66: ('Selects <code>count</code> elements at random from this iterable.', '从此可迭代对象中随机选择 <code>count</code> 个元素。'),
}
for i, (old,new) in pairs.items():
 assert old in blocks[i], i
 d[page][str(i)] = blocks[i].replace(old,new).replace('Available on ', '适用于 ').replace(',\n        provided by the ', '，\n        由 ').replace(' extension</span>', ' 扩展提供</span>')
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
