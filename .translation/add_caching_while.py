from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/CachingIterable/takeWhile.html': {
 '0': '<p>创建一个惰性可迭代对象，包含开头连续满足 <code>test</code> 的元素。</p>',
 '1': '<p>筛选以惰性方式执行。返回的可迭代对象的每个新迭代器都会从头开始遍历 <code>this</code> 的元素。</p>',
 '2': '<p>可以逐步遍历 <a href="foundation/CachingIterable/iterator.html">iterator</a> 来获取元素，直到找到使 <code>test(element)</code> 为 false 的元素。此时返回的可迭代对象停止迭代，其 <code>moveNext()</code> 返回 false。</p>',
 '3': '<p>示例：</p>',
 },
 'foundation/CachingIterable/skipWhile.html': {
 '0': '<p>创建一个 <code>Iterable</code>，跳过开头连续满足 <code>test</code> 的元素。</p>',
 '1': '<p>筛选以惰性方式执行。返回的可迭代对象的每个新 <a href="dart-core/Iterator-class.html">Iterator</a> 都会遍历 <code>this</code> 的所有元素。</p>',
 '2': '<p>返回的可迭代对象通过遍历当前对象来提供元素，但会跳过开头所有使 <code>test(element)</code> 返回 true 的元素。如果所有元素都满足 <code>test</code>，结果就是空的可迭代对象；否则，从首个使 <code>test(element)</code> 返回 <code>false</code> 的元素开始，按原始顺序遍历剩余元素。</p>',
 '3': '<p>示例：</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
