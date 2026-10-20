from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/debugPrintStack.html'] = {
 '0': '<p>使用 <a href="rendering/debugPrint.html">debugPrint</a> 和 <a href="foundation/FlutterError/defaultStackFilter.html">FlutterError.defaultStackFilter</a> 将堆栈输出到控制台。</p>',
 '1': '<p>如果 <code>stackTrace</code> 参数为 null，则使用 <a href="dart-core/StackTrace/current.html">StackTrace.current</a> 获取堆栈。</p>',
 '2': '<p>可以通过 <code>maxFrames</code> 参数，在应用过滤之前将堆栈限制为指定的行数。默认包含所有堆栈行。</p>',
 '3': '<p>如果提供了 <code>label</code> 参数，会先输出该标签，再输出堆栈。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
