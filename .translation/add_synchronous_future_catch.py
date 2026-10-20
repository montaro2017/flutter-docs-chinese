from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/SynchronousFuture/catchError.html'] = {
 '0': '<p>处理此 <a href="dart-async/Future-class.html">Future</a> 发出的错误。</p>',
 '1': '<p>这是 catch 块的异步对应形式。</p>',
 '2': '<p>返回一个新的 <a href="dart-async/Future-class.html">Future</a>，它将以此 future 的结果或调用 <code>onError</code> 回调的结果完成。</p>',
 '3': '<p>如果此 future 以一个值完成，返回的 future 也会以相同的值完成。</p>',
 '4': '<p>如果此 future 以错误完成，则先以该错误值为参数调用 <code>test</code>。</p>',
 '5': '<p>如果 <code>test</code> 返回 false，此 <code>catchError</code> 不会处理该异常，返回的 future 会以与此 future 相同的错误和堆栈跟踪完成。</p>',
 '6': '<p>如果 <code>test</code> 返回 <code>true</code>，则以错误以及可能的堆栈跟踪为参数调用 <code>onError</code>。返回的 future 将以此次调用的结果完成，处理方式与 <a href="foundation/SynchronousFuture/then.html">then</a> 的 <code>onError</code> 完全相同。</p>',
 '7': '<p>如果省略 <code>test</code>，默认使用一个始终返回 true 的函数。<code>test</code> 函数不应抛出异常；如果它抛出异常，则按 <code>onError</code> 函数抛出异常的方式处理。</p>',
 '8': '<p>请注意，future 不会等到添加监听器后才报告错误。如果首次调用 <code>catchError</code>（或 <code>then</code>）时，此 future 已经以错误完成，该错误就会被报告为未处理的错误。参见 <a href="dart-async/Future-class.html">Future</a> 的说明。</p>',
 '9': '<p>示例：</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
