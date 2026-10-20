from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/IterableProperty/level.html'] = {'0': '<p>诊断信息的优先级，用于控制哪些诊断信息应显示或被过滤。</p>', '1': '<p>如果 <a href="foundation/DiagnosticsProperty/ifEmpty.html">ifEmpty</a> 为 null，且 <a href="foundation/DiagnosticsProperty/value.html">value</a> 是空的 <a href="dart-core/Iterable-class.html">Iterable</a>，则返回 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.fine</a> 级别。这类似于 <a href="foundation/ObjectFlagProperty-class.html">ObjectFlagProperty</a> 对 <a href="foundation/DiagnosticsProperty/ifNull.html">ifNull</a> 为 null 且 <a href="foundation/DiagnosticsProperty/value.html">value</a> 为 null 的情况的处理方式。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
