from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
debug = '返回对象的调试表示，供调试工具和 <a href="foundation/DiagnosticsNode/toStringDeep.html">DiagnosticsNode.toStringDeep</a> 使用。'
brief = '此对象的简短描述，通常仅包含 <a href="dart-core/Object/runtimeType.html">runtimeType</a> 和 <a href="dart-core/Object/hashCode.html">hashCode</a>。'
override = '<div class="features"><span class="feature">重写</span></div>'
d.setdefault('foundation/Diagnosticable-mixin.html', {}).update({
 '1': '<dd>添加与节点关联的其他属性。</dd>',
 '2': '<dd>' + debug + '</dd>',
 '3': '<dd>此对象的字符串表示。' + override + '</dd>',
 '4': '<dd>' + brief + '</dd>',
})
d.setdefault('foundation/DiagnosticableTree-class.html', {}).update({
 '2': '<dd>抽象 const 构造函数。此构造函数使子类能够提供 const 构造函数，从而可用于常量表达式。<div class="constructor-modifier features">const</div></dd>',
 '3': '<dd>返回描述此节点子节点的 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 对象列表。</dd>',
 '4': '<dd>' + debug + override + '</dd>',
 '5': '<dd>返回此节点及其后代节点的字符串表示。</dd>',
 '6': '<dd>返回对象的单行详细描述。</dd>',
 '7': '<dd>' + brief + override + '</dd>',
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
