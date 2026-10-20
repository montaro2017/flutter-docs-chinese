from pathlib import Path
import json, re
from case_paths import read_source
p = Path(__file__).resolve().parent / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/CachingIterable-class.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
pairs = {
31: ('The non-<code>null</code> elements of this iterable.', '此可迭代对象中非 <code>null</code> 的元素。'),
32: ('The single element of this iterator, or <code>null</code>.', '此迭代器的唯一元素，或 <code>null</code>。'),
33: ('The single element of the iterable, or <code>null</code>.', '此可迭代对象的唯一元素，或 <code>null</code>。'),
34: ('The sum of the elements.', '元素之和。'),
35: ('The sum of the elements.', '元素之和。'),
36: ('The sum of the elements.', '元素之和。'),
37: ('A <a href="dart-js_interop/JSIterable-extension-type.html">JSIterable</a> wrapper that proxies to the Dart iterable API.', '一个 <a href="dart-js_interop/JSIterable-extension-type.html">JSIterable</a> 包装器，将操作代理到 Dart 可迭代对象 API。'),
38: ('Waits for futures in parallel.', '并行等待多个 future 完成。'),
39: ('Creates a map from the names of enum values to the values.', '创建从枚举值名称到对应枚举值的映射。'),
40: ('Finds the enum value in this list with name <code>name</code>.', '查找此列表中名称为 <code>name</code> 的枚举值。'),
42: ('The element at position <code>index</code> of this iterable, or <code>null</code>.', '此可迭代对象中索引为 <code>index</code> 的元素，或 <code>null</code>。'),
}
for i, (old,new) in pairs.items():
 assert old in blocks[i], i
 text = blocks[i].replace(old,new).replace('Available on ', '适用于 ').replace(',\n        provided by the ', '，\n        由 ').replace(' extension</span>', ' 扩展提供</span>').replace('>no setter<', '>无 setter<')
 d[page][str(i)] = text
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
