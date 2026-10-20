from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsStackTrace-class.html'] = {'0': '<p>具有 <a href="dart-core/StackTrace-class.html">StackTrace</a> 类型的 <a href="foundation/DiagnosticsBlock/value.html">value</a> 的诊断信息，适合将堆栈跟踪作为 <a href="foundation/FlutterError-class.html">FlutterError</a> 对象的一部分显示。</p>'}
d['foundation/DiagnosticsStackTrace/DiagnosticsStackTrace.html'] = {'0': '<p>为堆栈跟踪创建诊断信息。</p>', '1': '<p><code>name</code> 表示为堆栈跟踪指定的名称，例如 <code>When the exception was thrown, this was the stack</code>。<code>stackFilter</code> 提供可选的过滤器，用于筛选要包含的帧。如果未指定过滤器，则使用 <a href="foundation/FlutterError/defaultStackFilter.html">FlutterError.defaultStackFilter</a>。<code>showSeparator</code> 表示是否在 <code>name</code> 后添加“:”。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
