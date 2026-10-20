from pathlib import Path
import json
path = Path(__file__).resolve().parent / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'foundation/LocalKey-class.html': {
  '0': '<p>不是 <a href="widgets/GlobalKey-class.html">GlobalKey</a> 的键。</p>',
  '1': '<p>键必须在具有相同父节点的 <a href="widgets/Element-class.html">Element</a> 之间保持唯一。相比之下，<a href="widgets/GlobalKey-class.html">GlobalKey</a> 必须在整个应用中保持唯一。</p>',
  '2': '<p>另请参阅：</p>',
 },
 'foundation/UniqueKey-class.html': {
  '0': '<p>仅与自身相等的键。</p>',
  '1': '<p>不能使用 const 构造函数创建此键，因为这会使所有实例化的键成为同一个实例，从而不再唯一。</p>',
 },
 'foundation/UniqueKey/UniqueKey.html': {
  '0': '<p>创建仅与自身相等的键。</p>',
  '1': '<p>不能使用 const 构造函数创建此键，因为这会使所有实例化的键成为同一个实例，从而不再唯一。</p>',
 },
 'foundation/ValueKey/ValueKey.html': {'0': '<p>创建一个将 <a href="foundation/ValueKey/operator_equals.html">operator==</a> 委托给给定值的键。</p>'},
 'foundation/ValueKey/value.html': {'0': '<p>此键将 <a href="foundation/ValueKey/operator_equals.html">operator==</a> 委托给的值。</p>'},
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
