from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/CachingIterable/iterator.html'] = {
 '0': '<p>一个新的 <code>Iterator</code>，用于遍历此 <code>Iterable</code> 的元素。</p>',
 '1': '<p>可迭代类可以规定元素的迭代顺序，例如 <a href="dart-core/List-class.html">List</a> 始终按索引顺序迭代；也可以不规定顺序，例如基于哈希的 <a href="dart-core/Set-class.html">Set</a> 可以按任意顺序迭代。</p>',
 '2': '<p>每次读取 <code>iterator</code> 都会返回一个新迭代器，可用于重新遍历所有元素。同一个可迭代对象的迭代器可以独立推进；只要底层集合没有改变，它们就应按相同顺序返回相同元素。</p>',
 '3': '<p>修改集合可能使新迭代器返回不同的元素，也可能改变现有元素的顺序。<a href="dart-core/List-class.html">List</a> 精确定义了迭代顺序，因此修改列表会以可预测的方式改变该顺序。向基于哈希的 <a href="dart-core/Set-class.html">Set</a> 添加新元素时，其迭代顺序可能完全改变。</p>',
 '4': '<p>创建新迭代器后修改底层集合，可能使下一次对该迭代器调用 <a href="dart-core/Iterator/moveNext.html">Iterator.moveNext</a> 时发生错误。任何<em>可修改的</em>可迭代类都应说明哪些操作会破坏迭代。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
