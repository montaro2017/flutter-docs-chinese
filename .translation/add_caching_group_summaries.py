from pathlib import Path
import json, re
from case_paths import read_source
p = Path(__file__).resolve().parent / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/CachingIterable-class.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
pairs = {
43: ('The <code>index</code>th element, or <code>null</code> if there is no such element.', '索引为 <code>index</code> 的元素；如果不存在该元素，则为 <code>null</code>。'),
45: ('Expands each element and index to a number of elements in a new iterable.', '根据每个元素及其索引，将其展开为新可迭代对象中的若干元素。'),
46: ('The first element whose value and index satisfies <code>test</code>.', '值与索引满足 <code>test</code> 的第一个元素。'),
47: ('The first element satisfying <code>test</code>, or <code>null</code> if there are none.', '满足 <code>test</code> 的第一个元素；如果没有，则为 <code>null</code>。'),
48: ('Combine the elements with a value and the current index.', '结合累积值和当前索引来合并元素。'),
49: ('Takes an action for each element.', '对每个元素执行操作。'),
50: ('Takes an action for each element and index as long as desired.', '对每个元素及其索引执行操作，直到要求停止。'),
51: ('Takes an action for each element as long as desired.', '对每个元素执行操作，直到要求停止。'),
52: ('Groups elements by <code>keyOf</code> then folds the elements in each group.', '按 <code>keyOf</code> 对元素分组，然后对每组元素进行折叠聚合。'),
53: ('Groups elements into lists by <code>keyOf</code>.', '按 <code>keyOf</code> 将元素分组为列表。'),
54: ('Groups elements into sets by <code>keyOf</code>.', '按 <code>keyOf</code> 将元素分组为集合。'),
}
for i, (old,new) in pairs.items():
 assert old in blocks[i], i
 text = blocks[i].replace(old,new).replace('Available on ', '适用于 ').replace(',\n        provided by the ', '，\n        由 ').replace(' extension</span>', ' 扩展提供</span>')
 d[page][str(i)] = text
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
