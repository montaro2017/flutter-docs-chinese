from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/CachingIterable/CachingIterable.html'] = {
 '0': '<p>使用给定的 <a href="dart-core/Iterator-class.html">Iterator</a> 作为数据源，创建 <a href="foundation/CachingIterable-class.html">CachingIterable</a>。</p>',
 '1': '<p>迭代器不得抛出异常。</p>',
 '2': '<p>由于参数是 <a href="dart-core/Iterator-class.html">Iterator</a>，而非 <a href="dart-core/Iterable-class.html">Iterable</a>，因此可以保证只遍历底层数据集一次。如果已有 <a href="dart-core/Iterable-class.html">Iterable</a>，可以将其 <a href="foundation/CachingIterable/iterator.html">iterator</a> 字段作为此构造函数的参数。</p>',
 '3': '<p>可以按如下方式与现有的 <code>sync*</code> 函数一起使用：</p>',
 '4': '<p>请注意，这会立即求值 <code>range</code> 可迭代对象。因此，如果可行，最好直接将 <code>range</code> 实现为返回 <code>List</code> 的函数。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
