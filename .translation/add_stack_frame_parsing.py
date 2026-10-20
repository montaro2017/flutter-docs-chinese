from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'fromStackString': ['<p>从 <a href="dart-core/StackTrace/toString.html">StackTrace.toString</a> 方法的结果中解析出 <a href="foundation/StackFrame-class.html">StackFrame</a> 列表。</p>'],
 'fromStackTrace': ['<p>从 <a href="dart-core/StackTrace-class.html">StackTrace</a> 对象中解析出 <a href="foundation/StackFrame-class.html">StackFrame</a> 列表。</p>', '<p>通常适合与 <a href="dart-core/StackTrace/current.html">StackTrace.current</a> 配合使用。</p>'],
 'fromStackTraceLine': ['<p>从 <a href="dart-core/StackTrace-class.html">StackTrace</a> 的单行文本中解析出一个 <a href="foundation/StackFrame-class.html">StackFrame</a>。</p>', '<p>如果格式不符合预期，则返回 null。</p>'],
 'StackFrame': ['<p>创建一个新的 StackFrame 实例。</p>', '<p>如果没有所属类（例如库中的顶层方法），<code>className</code> 可以为空字符串。</p>'],
 'packageScheme': ['<p>此帧对应包的 URI scheme，例如 dart:core/errors_patch.dart 对应“dart”，package:flutter/src/widgets/text.dart 对应“package”。</p>', '<p>path 属性指向源文件。</p>'],
 'asynchronousSuspension-constant': ['<p>表示异步挂起的堆栈帧。</p>'],
 'stackOverFlowElision-constant': ['<p>表示 Dart 省略的堆栈溢出帧的堆栈帧。</p>'],
}
for member, blocks in pages.items():
 d[f'foundation/StackFrame/{member}.html'] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
