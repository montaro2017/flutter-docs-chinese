from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/ObjectFlagProperty-class.html'] = {
 '0': '<p>一种属性，其主要诊断信息是 <a href="foundation/DiagnosticsProperty/value.html">value</a> 是否存在（非 null）或缺失（null），而不是属性自身的实际值。</p>',
 '1': '<p><a href="foundation/ObjectFlagProperty/ifPresent.html">ifPresent</a> 和 <a href="foundation/DiagnosticsProperty/ifNull.html">ifNull</a> 字符串分别描述属性 <a href="foundation/DiagnosticsProperty/value.html">value</a> 为非 null 和 null 时的情况。如果省略 <a href="foundation/ObjectFlagProperty/ifPresent.html">ifPresent</a> 或 <a href="foundation/DiagnosticsProperty/ifNull.html">ifNull</a>，则分别表示当 <a href="foundation/DiagnosticsProperty/value.html">value</a> 为非 null 或 null 时，<a href="foundation/ObjectFlagProperty/level.html">level</a> 应为 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.hidden</a>。</p>',
 '2': '<p>此类诊断属性通常用于闭包等不透明值。对于这些值，展示实际对象的价值有限，而报告该值是否存在更有用。</p>',
 '3': '<p>另请参阅：</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
