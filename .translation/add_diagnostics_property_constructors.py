from pathlib import Path
import json
p = Path(__file__).resolve().parent/'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsProperty/DiagnosticsProperty.html'] = {
 '0':'<p>创建诊断属性。</p>',
 '1':'<p><code>level</code> 参数仅是建议值。如果属性的其他情况使其级别更低或更高，此值可能被覆盖。例如，如果属性值为 null 且 <code>missingIfNull</code> 为 true，则 <code>level</code> 提升为 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.warning</a>。</p>',
}
d['foundation/DiagnosticsProperty/DiagnosticsProperty.lazy.html'] = {
 '0':'<p>仅在需要时才计算 <a href="foundation/DiagnosticsProperty/value.html">value</a> 的属性。</p>',
 '1':'<p>如果计算属性的 <a href="foundation/DiagnosticsProperty/value.html">value</a> 可能抛出异常或开销较大，请使用此构造函数。</p>',
 '2':'<p><code>level</code> 参数仅是建议值。如果属性的其他情况使其级别更低或更高，此值可能被覆盖。例如，如果调用 <code>computeValue</code> 抛出异常，<code>level</code> 将始终返回 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.error</a>。</p>',
}
p.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
