from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsBlock/allowTruncate.html'] = dict(d['foundation/DiagnosticsStackTrace/allowTruncate.html'])
d['foundation/DiagnosticsBlock/toDescription.html'] = dict(d['foundation/DiagnosticableNode/toDescription.html'])
d['foundation/DiagnosticsBlock/level.html'] = {'0': '<p>诊断信息的优先级，用于控制哪些诊断信息应显示或被过滤。</p>', '1': '<p>通常，只有对于表示属性的诊断信息，将其设置为不同于 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.info</a> 的值才有意义。某些子类的构造函数具有 <a href="foundation/DiagnosticsBlock/level.html">level</a> 参数，会影响此处返回的值，但其他因素也会产生影响。例如，计算属性值时抛出异常，则返回 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.error</a>。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
