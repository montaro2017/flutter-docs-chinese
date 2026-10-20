from pathlib import Path
import json
p = Path(__file__).resolve().parent/'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsProperty/defaultValue.html'] = {
 '0':'<p>此属性未设置为具体值时的默认值。</p>',
 '1':'<p>对于大多数 <a href="foundation/DiagnosticsProperty-class.html">DiagnosticsProperty</a> 类，如果属性的 <a href="foundation/DiagnosticsProperty/value.html">value</a> 等于 <a href="foundation/DiagnosticsProperty/defaultValue.html">defaultValue</a>，则认为该属性值没有显示价值，将其优先级 <a href="foundation/DiagnosticsProperty/level.html">level</a> 降低为 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.fine</a>。此行为由 <a href="foundation/DiagnosticsProperty/isInteresting.html">isInteresting</a> 实现。</p>',
 '2':'<p><a href="foundation/DiagnosticsProperty/defaultValue.html">defaultValue</a> 默认为 <a href="foundation/kNoDefaultValue-constant.html">kNoDefaultValue</a>。否则，它必须为 <code>T?</code> 类型。</p>',
}
d['foundation/DiagnosticsProperty/exception.html'] = {
 '0':'<p>访问属性的 <a href="foundation/DiagnosticsProperty/value.html">value</a> 时抛出的异常。</p>',
 '1':'<p>如果计算属性值时没有抛出异常，则返回 null。</p>',
}
d['foundation/DiagnosticsProperty/missingIfNull.html'] = {'0':'<p>是否在 <a href="foundation/DiagnosticsProperty/value.html">value</a> 为 null 时，将属性的 <a href="foundation/DiagnosticsProperty/level.html">level</a> 设为 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.warning</a>，以警告该属性缺少 <a href="foundation/DiagnosticsProperty/value.html">value</a>。</p>'}
p.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
