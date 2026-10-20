from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/describeIdentity.html'] = {'0': '<p>返回 <code>object</code> 的运行时类型和哈希码摘要。</p>', '1': '<p>另请参阅：</p>'}
d['foundation/shortHash.html'] = {'0': '<p>返回由 <a href="dart-core/Object/hashCode.html">Object.hashCode</a> 的最低 20 位生成的、长度为 5 个字符的十六进制字符串。</p>'}
d['foundation/objectRuntimeType.html'] = {
 '0': '<p>框架代码应使用此方法，而不是对 <a href="dart-core/Object/runtimeType.html">Object.runtimeType</a> 调用 <code>toString</code>。</p>',
 '1': '<p>对运行时类型调用 <code>toString</code> 并非低开销操作，可能对性能产生不利影响。如果启用了断言，此方法返回 <code>object.runtimeType.toString()</code>；否则返回 <code>optimizedValue</code>，该值必须是简单的常量字符串。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/describeIdentity.html'] = [
 {'source': '<li><a href="dart-core/Object/hashCode.html">Object.hashCode</a>, a value used when placing an object in a <a href="dart-core/Map-class.html">Map</a> or\nother similar data structure, and which is also used in debug output to\ndistinguish instances of the same class (hash collisions are\npossible, but rare enough that its use in debug output is useful).</li>', 'translation': '<li><a href="dart-core/Object/hashCode.html">Object.hashCode</a>，将对象放入 <a href="dart-core/Map-class.html">Map</a> 或其他类似数据结构时使用的值，也用于在调试输出中区分同一类的实例（哈希冲突可能发生，但足够少见，因此在调试输出中使用它仍有价值）。</li>'},
 {'source': '<li><a href="dart-core/Object/runtimeType.html">Object.runtimeType</a>, the <a href="dart-core/Type-class.html">Type</a> of an object.</li>', 'translation': '<li><a href="dart-core/Object/runtimeType.html">Object.runtimeType</a>，对象的 <a href="dart-core/Type-class.html">Type</a>。</li>'},
]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
