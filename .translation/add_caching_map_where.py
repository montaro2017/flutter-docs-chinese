from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/CachingIterable/map.html': {
 '0': '<p>将此可迭代对象的当前元素通过 <code>toElement</code> 转换后得到的元素。</p>',
 '1': '<p>返回一个新的惰性 <a href="dart-core/Iterable-class.html">Iterable</a>，按迭代顺序对当前 <code>Iterable</code> 的每个元素调用 <code>toElement</code>，生成其元素。</p>',
 '2': '<p>返回的可迭代对象是惰性的，只有遍历它时才会遍历当前对象，并调用 <code>toElement</code>，每次生成一个元素。转换后的元素不会被缓存。多次遍历返回的 <a href="dart-core/Iterable-class.html">Iterable</a> 时，每次遍历都会为每个元素调用一次提供的 <code>toElement</code> 函数。</p>',
 '3': '<p>返回的可迭代对象上的方法可以不为无需使用结果的元素调用 <code>toElement</code>。例如，<a href="foundation/CachingIterable/elementAt.html">elementAt</a> 可能只调用一次 <code>toElement</code>。</p>',
 '4': '<p>等价于：</p>',
 '5': '<p>示例：</p>',
 },
 'foundation/CachingIterable/where.html': {
 '0': '<p>创建一个新的惰性 <a href="dart-core/Iterable-class.html">Iterable</a>，包含所有满足谓词 <code>test</code> 的元素。</p>',
 '1': '<p>匹配元素在返回的可迭代对象中的顺序与它们在 <a href="foundation/CachingIterable/iterator.html">iterator</a> 中的顺序相同。</p>',
 '2': '<p>此方法返回映射元素的视图。只要不遍历返回的 <a href="dart-core/Iterable-class.html">Iterable</a>，就不会调用提供的 <code>test</code> 函数。遍历不会缓存结果，因此多次遍历返回的 <a href="dart-core/Iterable-class.html">Iterable</a> 时，可能会对同一元素多次调用提供的 <code>test</code> 函数。</p>',
 '3': '<p>示例：</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
