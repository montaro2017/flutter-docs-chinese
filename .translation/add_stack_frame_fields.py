from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'className': ['<p>此帧对应的类名（如果有）。</p>', '<p>对于库中的顶层方法或匿名闭包方法，此值可能为 null。</p>'],
 'column': ['<p>源代码列号。</p>'],
 'isConstructor': ['<p>异常是否从构造函数中抛出。</p>'],
 'line': ['<p>源代码行号。</p>'],
 'method': ['<p>此帧对应的方法名。</p>', '<p>如果堆栈帧来自默认构造函数，此值为空字符串。</p>'],
 'number': ['<p>从零开始编号的帧序号。</p>', '<p>此值可以为 -1，表示帧序号未知。</p>'],
 'package': ['<p>此帧对应的包，例如 dart:core/errors_patch.dart 对应“core”，package:flutter/src/widgets/text.dart 对应“flutter”。</p>'],
 'packagePath': ['<p>此帧对应文件的路径，例如 dart:core/errors_patch.dart 对应“errors_patch.dart”，package:flutter/src/widgets/text.dart 对应“src/widgets/text.dart”。</p>'],
 'source': ['<p>此堆栈帧的原始来源文本。</p>'],
}
d['foundation/StackFrame-class.html'] = {'0': '<p>堆栈跟踪中一个帧的对象表示。</p>'}
for member, blocks in pages.items():
 d[f'foundation/StackFrame/{member}.html'] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/StackFrame-class.html'] = [{'source': 'This example creates a traversable list of parsed <a href="foundation/StackFrame-class.html">StackFrame</a> objects from\nthe current <a href="dart-core/StackTrace-class.html">StackTrace</a>.', 'translation': '此示例从当前 <a href="dart-core/StackTrace-class.html">StackTrace</a> 创建一个可遍历的列表，其中包含解析后的 <a href="foundation/StackFrame-class.html">StackFrame</a> 对象。'}]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
