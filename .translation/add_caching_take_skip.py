from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/CachingIterable/take.html': {
 '0': '<p>创建一个包含此可迭代对象前 <code>count</code> 个元素的惰性可迭代对象。</p>',
 '1': '<p>如果 <code>this</code> 包含的元素少于 <code>count</code> 个，返回的 <code>Iterable</code> 也可能包含少于 <code>count</code> 个元素。</p>',
 '2': '<p>可以逐步遍历 <a href="foundation/CachingIterable/iterator.html">iterator</a>，直到访问了 <code>count</code> 个元素，来获取这些元素。</p>',
 '3': '<p><code>count</code> 不能为负数。</p>',
 '4': '<p>示例：</p>',
 },
 'foundation/CachingIterable/skip.html': {
 '0': '<p>创建一个 <a href="dart-core/Iterable-class.html">Iterable</a>，提供除前 <code>count</code> 个元素之外的所有元素。</p>',
 '1': '<p>遍历返回的可迭代对象时，会开始遍历 <code>this</code>，先跳过前 <code>count</code> 个元素。如果 <code>this</code> 的元素少于 <code>count</code> 个，结果就是空的 Iterable。随后按照与当前可迭代对象相同的顺序遍历剩余元素。</p>',
 '2': '<p>某些可迭代对象无需先遍历前面的元素就能找到后面的元素，例如遍历 <a href="dart-core/List-class.html">List</a> 时。这些可迭代对象可以直接忽略开头被跳过的元素。</p>',
 '3': '<p>示例：</p>',
 '4': '<p><code>count</code> 不能为负数。</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
