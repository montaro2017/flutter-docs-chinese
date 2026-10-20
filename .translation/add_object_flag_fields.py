from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/ObjectFlagProperty/ObjectFlagProperty.html'] = {
 '0': '<p>为可能存在（非 null）或缺失（null）的值创建诊断属性，这些值的 <a href="dart-core/Object/toString.html">Object.toString</a> 表示无法清楚表达其具体含义（例如回调）。</p>',
 '1': '<p><code>ifPresent</code> 和 <code>ifNull</code> 中至少一个必须为非 null。</p>',
}
d['foundation/ObjectFlagProperty/ObjectFlagProperty.has.html'] = {
 '0': '<p>描述属性是否具有值的简写构造函数。</p>',
 '1': '<p>仅当在属性名称前加上“has”能够形成合适的标志名称时使用。</p>',
}
d['foundation/ObjectFlagProperty/ifPresent.html'] = {
 '0': '<p>属性的 <a href="foundation/DiagnosticsProperty/value.html">value</a> 不为 null 时使用的描述。</p>',
 '1': '<p>如果属性的 <a href="foundation/DiagnosticsProperty/value.html">value</a> 不为 null，而 <a href="foundation/ObjectFlagProperty/ifPresent.html">ifPresent</a> 为 null，则该属性的 <a href="foundation/ObjectFlagProperty/level.html">level</a> 为 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.hidden</a>，并使用父类提供的描述。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
