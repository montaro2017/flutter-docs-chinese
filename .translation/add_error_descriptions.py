from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
interpolation = '<p>在调试构建中，插入 <code>message</code> 的值会被展开并放入 <code>value</code>，其类型为 <a href="dart-core/List-class.html">List&lt;Object&gt;</a>。这使 IDE 能够检查插入错误消息中的值。</p>'
pages = {
 'ErrorSummary-class.html': ['<p>对检测到的问题的简短（单行）描述。</p>', '<p>来自同一源代码位置的错误摘要应尽量保持一致，以便识别它们之间的关联。例如，不应包含哈希码。</p>', '<p><a href="foundation/FlutterError-class.html">FlutterError</a> 必须以 <a href="foundation/ErrorSummary-class.html">ErrorSummary</a> 开头，并且不能包含多个摘要。</p>', interpolation, '<p>另请参阅：</p>'],
 'ErrorDescription-class.html': ['<p>对问题及其原因的解释，以及可能有助于定位问题的信息、背景信息等。</p>', '<p>对于错误消息中不适合使用 <a href="foundation/ErrorSummary-class.html">ErrorSummary</a> 或 <a href="foundation/ErrorHint-class.html">ErrorHint</a> 的部分，请使用 <a href="foundation/ErrorDescription-class.html">ErrorDescription</a>。</p>', interpolation, '<p>另请参阅：</p>'],
 'ErrorHint-class.html': ['<p><a href="foundation/ErrorHint-class.html">ErrorHint</a> 提供可能适用的、具体且不明显的建议。</p>', '<p>如果消息提供的是显而易见且始终适用的建议，则应使用 <a href="foundation/ErrorDescription-class.html">ErrorDescription</a>，而不是提示。</p>', interpolation, '<p>另请参阅：</p>'],
 'ErrorSpacer-class.html': ['<p><a href="foundation/ErrorSpacer-class.html">ErrorSpacer</a> 创建一个空的 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a>，可用于调整其他 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 对象之间的间距。</p>'],
 'ErrorSpacer/ErrorSpacer.html': ['<p>创建一个空白间隔，用于插入 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 对象列表，通常位于 <a href="foundation/FlutterError-class.html">FlutterError</a> 对象内部。</p>'],
}
for cls in ('ErrorSummary', 'ErrorDescription', 'ErrorHint'):
 pages[f'{cls}/{cls}.html'] = ['<p>一条 lint 规则要求此构造函数只能使用字符串字面量调用，以符合 Dart Kernel 转换器的限制。该转换器可以选择提取传入消息中通过字符串插值引用的对象。</p>', '<p>无论是否使用 Kernel 转换器，消息都会显示相同的文本。要让调试工具以交互方式展示错误中描述的对象，则需要使用 Kernel 转换器。</p>']
for page, blocks in pages.items():
 d['foundation/' + page] = {str(i): b for i, b in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
