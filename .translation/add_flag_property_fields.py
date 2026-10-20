from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/FlagProperty/FlagProperty.html'] = {
 '0': '<p>使用给定描述构造 FlagProperty。</p>',
 '1': '<p><code>showName</code> 默认为 false，因为通常 <code>ifTrue</code> 和 <code>ifFalse</code> 的描述已经足以表达含义，无需再显示属性名称。</p>',
}
d['foundation/FlagProperty/ifTrue.html'] = {
 '0': '<p>属性的 <a href="foundation/DiagnosticsProperty/value.html">value</a> 为 true 时使用的描述。</p>',
 '1': '<p>如果未指定此描述且 <a href="foundation/DiagnosticsProperty/value.html">value</a> 为 true，则属性的优先级 <a href="foundation/FlagProperty/level.html">level</a> 为 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.hidden</a>。</p>',
}
d['foundation/FlagProperty/ifFalse.html'] = {
 '0': '<p>属性值为 false 时使用的描述。</p>',
 '1': '<p>如果未指定此描述且 <a href="foundation/DiagnosticsProperty/value.html">value</a> 为 false，则属性的优先级 <a href="foundation/FlagProperty/level.html">level</a> 为 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.hidden</a>。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
