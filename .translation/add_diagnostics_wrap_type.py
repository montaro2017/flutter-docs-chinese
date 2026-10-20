from pathlib import Path
import json
p=Path(__file__).resolve().parent/'translations.json'
d=json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsProperty/allowNameWrap.html']={'0':'<p>是否允许名称换行显示。</p>'}
d['foundation/DiagnosticsProperty/allowWrap.html']={'0':'<p>是否允许文本换行显示。</p>'}
d['foundation/DiagnosticsProperty/expandableValue.html']={'0':'<p>是否将值的属性和子节点公开为此诊断节点的属性和子节点。</p>'}
d['foundation/DiagnosticsProperty/propertyType.html']={
 '0':'<p>属性 <a href="foundation/DiagnosticsProperty/value.html">value</a> 的类型。</p>',
 '1':'<p>此类型由实例化 <a href="foundation/DiagnosticsProperty-class.html">DiagnosticsProperty</a> 类时使用的类型参数 <code>T</code> 决定。因此，即使 <a href="foundation/DiagnosticsProperty/value.html">value</a> 为 null，仍可获得该类型；但这也意味着 <a href="foundation/DiagnosticsProperty/propertyType.html">propertyType</a> 的准确性取决于调用构造函数时提供的类型。</p>',
 '2':'<p>通常，这仅对需要根据属性类型一致地显示 null 值的诊断工具有用。例如，工具可以将 null 的 <a href="dart-ui/Color-class.html">Color</a> 值显示为空矩形，而不是单词“null”。</p>',
}
p.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
