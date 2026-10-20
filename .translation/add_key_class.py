from pathlib import Path
import json
path = Path(__file__).resolve().parent / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['foundation/Key-class.html'] = {
 '0': '<p><a href="foundation/Key-class.html">Key</a> 是 <a href="widgets/Widget-class.html">Widget</a>、<a href="widgets/Element-class.html">Element</a> 和 <a href="semantics/SemanticsNode-class.html">SemanticsNode</a> 的标识符。</p>',
 '1': '<p>只有当新组件的键与现有元素当前关联组件的键相同时，才会使用新组件更新该元素。</p>',
 '2': '<p>通常，未提供键时默认值为 null，表示组件没有键。在这种情况下，Flutter 在重建时根据组件的 <a href="dart-core/Object/runtimeType.html">Widget.runtimeType</a> 和它在树中的位置进行匹配。</p>',
 '3': '<p>键必须在具有相同父节点的 <a href="widgets/Element-class.html">Element</a> 之间保持唯一。</p>',
 '4': '<p><a href="foundation/Key-class.html">Key</a> 的子类应继承 <a href="foundation/LocalKey-class.html">LocalKey</a> 或 <a href="widgets/GlobalKey-class.html">GlobalKey</a>。</p>',
 '5': '<p>一个常见错误是重建组件树时，Flutter 将错误的 State 对象关联到没有键的 StatefulWidget。通常可以通过为 <a href="widgets/StatefulWidget-class.html">StatefulWidget</a> 设置合适的 <a href="foundation/Key-class.html">Key</a> 来解决。</p>',
 '6': '<p>请参阅 <a href="foundation/ValueKey-class.html">ValueKey</a>，其中说明了如何使用该类解决此问题的一种常见情况。</p>',
 '7': '<p>另请参阅：</p>',
}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
