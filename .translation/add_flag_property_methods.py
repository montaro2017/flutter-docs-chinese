from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/FlagProperty/level.html'] = {
 '0': '<p>诊断信息的优先级，用于控制哪些诊断信息应显示或被过滤。</p>',
 '1': '<p>属性级别默认为构造函数参数 <a href="foundation/FlagProperty/level.html">level</a> 指定的值。如果获取属性 <a href="foundation/DiagnosticsProperty/value.html">value</a> 时抛出了 <a href="foundation/DiagnosticsProperty/exception.html">exception</a>，级别提升为 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.error</a>。如果属性 <a href="foundation/DiagnosticsProperty/value.html">value</a> 为 null，且 <a href="foundation/DiagnosticsProperty/missingIfNull.html">missingIfNull</a> 不允许该属性为 null，级别提升为 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.warning</a>。如果属性 <a href="foundation/DiagnosticsProperty/value.html">value</a> 等于 <a href="foundation/DiagnosticsProperty/defaultValue.html">defaultValue</a>，优先级降低为 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.fine</a>。</p>',
}
d['foundation/FlagProperty/showName.html'] = {'0': '<p>显示树的默认视图时是否显示属性名称。</p>', '1': '<p>如果值的描述已足以使名称的含义不言自明，可将此值设为 false（隐藏名称）。</p>'}
d['foundation/FlagProperty/valueToString.html'] = {k: v.replace('ErrorSummary/valueToString', 'FlagProperty/valueToString') for k,v in d['foundation/ErrorSummary/valueToString.html'].items()}
d['foundation/FlagProperty/toJsonMap.html'] = d['foundation/IntProperty/toJsonMap.html'].copy()
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/FlagProperty/toJsonMap.html'] = d['foundation/IntProperty/toJsonMap.html'].copy()
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
