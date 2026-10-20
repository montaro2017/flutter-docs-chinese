from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/CachingIterable-class.html'] = {
 '0': '<p><a href="dart-core/Iterable-class.html">Iterable</a> 的惰性缓存版本。</p>',
 '1': '<p>此可迭代对象在以下方面较为高效：</p>',
 '2': '<p>只会按请求的数量遍历给定迭代器，不会额外遍历。</p>',
 '3': '<p>如果使用它两次（例如先检查 <a href="dart-core/Iterable/isNotEmpty.html">isNotEmpty</a>，再使用 <a href="dart-core/Iterable/single.html">single</a>），它只会遍历给定迭代器一次。即使同时在同一个可迭代对象上使用两个迭代器，缓存仍然高效。</p>',
 '4': '<p><a href="foundation/CachingIterable/toList.html">toList</a> 使用其 EfficientLength 变体快速创建列表。</p>',
 '5': '<p>它在以下方面存在额外开销：</p>',
 '6': '<p>首次遍历时有缓存开销。</p>',
 '7': '<p>所需内存比不使用缓存的迭代器更多。</p>',
 '8': '<p><a href="foundation/CachingIterable/length.html">length</a> 和 <a href="foundation/CachingIterable/toList.html">toList</a> 会立即预先缓存整个列表。因此，使用它们会失去此可迭代对象的惰性，不过数据仍会被缓存。</p>',
 '9': '<p>缓存行为会传递给通过 <a href="foundation/CachingIterable/map.html">map</a>、<a href="foundation/CachingIterable/where.html">where</a>、<a href="foundation/CachingIterable/expand.html">expand</a>、<a href="foundation/CachingIterable/take.html">take</a>、<a href="foundation/CachingIterable/takeWhile.html">takeWhile</a>、<a href="foundation/CachingIterable/skip.html">skip</a> 和 <a href="foundation/CachingIterable/skipWhile.html">skipWhile</a> 创建的迭代器，也会被 <a href="dart-core/Iterable/isNotEmpty.html">isNotEmpty</a> 和 <a href="dart-core/Iterable/single.html">single</a> 等使用迭代器的内置方法利用。</p>',
 '10': '<p>由于 CachingIterable 只遍历底层数据一次，如果底层数据在每次使用之间发生变化，就不能重复使用同一个实例，而必须每次创建新的可迭代对象。此限制也适用于由它派生的可迭代对象，例如 <code>where</code> 返回的对象。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
