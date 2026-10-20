from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
common = {
 'contains': [
 '<p>集合中是否包含与 <code>element</code> 相等的元素。</p>',
 '<p>此操作会依次检查每个元素是否与 <code>element</code> 相等，除非有更高效的方法来查找与 <code>element</code> 相等的元素。找到第一个相等的元素时即停止迭代。</p>',
 '<p>判断 <code>element</code> 是否与可迭代对象中的元素相等时，默认使用该元素的 <a href="dart-core/Object/operator_equals.html">Object.==</a>。</p>',
 '<p>某些可迭代对象类型可能使用不同的元素相等规则。例如，<a href="dart-core/Set-class.html">Set</a> 可以使用自定义的相等规则（参见 <a href="dart-core/Set/Set.identity.html">Set.identity</a>），其 <code>contains</code> 也会使用该规则。同样，调用 <a href="dart-core/Map/keys.html">Map.keys</a> 返回的 <code>Iterable</code> 应使用与该 <code>Map</code> 的键相同的相等规则。</p>',
 '<p>示例：</p>',
 ],
 'isEmpty': ['<p>此集合是否没有元素。</p>', '<p>可以通过检查 <code>iterator.moveNext()</code> 是否返回 <code>false</code> 来计算。</p>', '<p>示例：</p>'],
 'isNotEmpty': ['<p>此集合是否至少包含一个元素。</p>', '<p>可以通过检查 <code>iterator.moveNext()</code> 是否返回 <code>true</code> 来计算。</p>', '<p>示例：</p>'],
 'iterator': [
 '<p>一个新的 <code>Iterator</code>，可用于遍历此 <code>Iterable</code> 中的元素。</p>',
 '<p>可迭代对象的类可以规定元素的迭代顺序（例如 <a href="dart-core/List-class.html">List</a> 始终按索引顺序迭代），也可以不作规定（例如基于哈希的 <a href="dart-core/Set-class.html">Set</a> 可以按任意顺序迭代）。</p>',
 '<p>每次读取 <code>iterator</code> 都会返回一个新的迭代器，可用于再次遍历所有元素。同一可迭代对象的迭代器可以独立推进，但只要底层集合没有变化，它们就应按相同顺序返回相同元素。</p>',
 '<p>修改集合可能使新迭代器返回不同的元素，也可能改变已有元素的顺序。<a href="dart-core/List-class.html">List</a> 精确规定了迭代顺序，因此修改列表会以可预测的方式改变迭代顺序。向基于哈希的 <a href="dart-core/Set-class.html">Set</a> 添加新元素时，其迭代顺序可能完全改变。</p>',
 '<p>创建新迭代器后修改底层集合，可能导致下次在该迭代器上调用 <a href="dart-core/Iterator/moveNext.html">Iterator.moveNext</a> 时出错。任何<em>可修改</em>的可迭代对象类都应说明哪些操作会破坏迭代。</p>',
 ],
}
for cls in ('ObserverList', 'HashedObserverList'):
 pages = dict(common)
 pages['add'] = ['<p>向此列表末尾添加一个元素。</p>', '<p>此操作的时间复杂度为常数。</p>']
 pages['remove'] = ['<p>从列表中移除一个元素。</p>', '<p>此操作的时间复杂度为常数。</p>' if cls == 'HashedObserverList' else '<p>此操作的时间复杂度为 O(N)，其中 N 为列表中的元素数量。</p>', '<p>返回该元素是否原本存在于列表中。</p>']
 pages['clear'] = [f'<p>移除 <a href="foundation/{cls}-class.html">{cls}</a> 中的所有元素。</p>']
 pages['toList'] = [f'<p>创建一个包含 <a href="foundation/{cls}-class.html">{cls}</a> 中各元素的 List。</p>', '<p>重写 <a href="dart-core/Iterable-class.html">Iterable</a> 的默认实现，以减少内存分配次数。</p>']
 for member, blocks in pages.items():
  d[f'foundation/{cls}/{member}.html'] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
