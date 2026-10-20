from pathlib import Path
import json

root = Path(__file__).resolve().parent
path = root / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['foundation/ValueKey-class.html'] = {
 '0': '<p>使用特定类型的值标识自身的键。</p>',
 '1': '<p>当且仅当两个 <a href="foundation/ValueKey-class.html">ValueKey</a> 的值相等（使用 <a href="foundation/ValueKey/operator_equals.html">operator==</a> 判断）时，一个 <a href="foundation/ValueKey-class.html">ValueKey</a> 才与另一个相等。</p>',
 '2': '<p>可以通过继承此类创建值键，使其不与恰好使用相同值的其他值键相等。如果子类是私有的，得到的值键类型就不会与其他来源的键发生冲突。当备用键与其他 widget 提供的键处于同一作用域时，这种做法很有用。</p>',
 '3': '<p>从数据集合构建 widget 时，尤其当集合会随时间变化（例如插入、移除或重新排序元素）时，可以使用键来保留 widget 与底层数据之间的关联。</p>',
 '4': '<p>如果没有键，框架可能无法区分现有 widget 的数据变化与列表的结构变化。因此，widget 可能被错误地更新，<a href="widgets/StatefulWidget-class.html">StatefulWidget</a> 保存的状态也可能被用于另一条数据。</p>',
 '5': '<p>指定键会将 widget 子树绑定到特定数据，使框架能够正确匹配新旧 widget，并按预期保留状态。</p>',
 '6': '<p>在这种情况下，通常适合使用 <a href="foundation/ValueKey-class.html">ValueKey</a>，并为每个元素提供稳定且唯一的值，例如数据模型中的标识符。</p>',
 '8': '<h3 id="the-key-difference">键带来的差异</h3>',
 '10': '<p>另请参阅：</p>',
}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
path = root / 'translations-fragments.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['foundation/ValueKey-class.html'] = [
 {'source': 'The following example demonstrates the importance of using <a href="foundation/ValueKey-class.html">ValueKey</a>s when reordering\na list of <a href="widgets/StatefulWidget-class.html">StatefulWidget</a>s.',
  'translation': '下面的示例展示了对 <a href="widgets/StatefulWidget-class.html">StatefulWidget</a> 列表重新排序时使用 <a href="foundation/ValueKey-class.html">ValueKey</a> 的重要性。'},
 {'source': 'To see the difference, find the <code>ColoredWidgetsList</code> widget inside the <code>map</code>\nfunction and comment/uncomment the <code>key: ValueKey(color)</code> line.',
  'translation': '要查看差异，请找到 <code>map</code> 函数中的 <code>ColoredWidgetsList</code> widget，然后注释或取消注释 <code>key: ValueKey(color)</code> 这一行。'},
]
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
