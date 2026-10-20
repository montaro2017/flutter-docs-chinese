from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/FlagsSummary-class.html'] = {
 '0': '<p>多个属性的摘要，指出各属性是否存在（非 null）或缺失（null）。</p>',
 '1': '<p><a href="foundation/FlagsSummary/value.html">value</a> 中的每个条目由其键描述。最终描述是所有非 null 条目的键组成的列表。</p>',
 '2': '<p>当 <a href="foundation/FlagsSummary/value.html">value</a> 中没有非 null 条目时，<a href="foundation/DiagnosticsProperty/ifEmpty.html">ifEmpty</a> 用于描述整个集合。如果省略 <a href="foundation/DiagnosticsProperty/ifEmpty.html">ifEmpty</a>，则当 <a href="foundation/FlagsSummary/value.html">value</a> 不包含非 null 条目时，<a href="foundation/FlagsSummary/level.html">level</a> 为 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.hidden</a>。</p>',
 '3': '<p>此类诊断属性通常用于闭包等不透明值。对于这些值，展示实际对象的价值有限，而报告该值是否存在更有用。</p>',
 '4': '<p>另请参阅：</p>',
}
d['foundation/FlagsSummary/FlagsSummary.html'] = {'0': '<p>为多个属性创建摘要，指出各属性是否存在（非 null）或缺失（null）。</p>', '1': '<p><code>value</code>、<code>showName</code>、<code>showSeparator</code> 和 <code>level</code> 参数不能为 null。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
