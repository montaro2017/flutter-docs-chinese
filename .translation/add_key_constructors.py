from pathlib import Path
import json
path = Path(__file__).resolve().parent / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'foundation/Key/Key.html': {
  '0': '<p>使用给定的 <a href="dart-core/String-class.html">String</a> 构造 <a href="foundation/ValueKey-class.html">ValueKey&lt;String&gt;</a>。</p>',
  '1': '<p>这是创建键最简单的方式。</p>',
 },
 'foundation/Key/Key.empty.html': {
  '0': '<p>供子类使用的默认构造函数。</p>',
  '1': '<p>由于 <a href="foundation/Key/Key.html">Key.new</a> 工厂构造函数遮蔽了隐式构造函数，此构造函数使子类能够调用父类构造函数。</p>',
 },
 'foundation/LocalKey/LocalKey.html': {'0': '<p>此构造函数使子类能够提供 const 构造函数，从而用于 const 表达式。</p>'},
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
