from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/CachingIterable/length.html': {
 '0': '<p>此 <a href="dart-core/Iterable-class.html">Iterable</a> 中的元素数量。</p>',
 '1': '<p>统计全部元素可能需要遍历所有元素，因此可能较慢。某些可迭代对象有更高效的方式获取元素数量；它们<em>必须</em>重写 <code>length</code> 的默认实现。</p>',
 },
 'foundation/CachingIterable/toList.html': {
 '0': '<p>创建一个包含此 <a href="dart-core/Iterable-class.html">Iterable</a> 所有元素的 <a href="dart-core/List-class.html">List</a>。</p>',
 '1': '<p>元素按迭代顺序排列。如果 <code>growable</code> 为 false，列表长度固定。</p>',
 '2': '<p>示例：</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
