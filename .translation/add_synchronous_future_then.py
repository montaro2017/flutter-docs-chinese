from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/SynchronousFuture/then.html'] = {
 '0': '<p>注册在此 future 完成时调用的回调。</p>',
 '1': '<p>此 future 以值完成时，会以该值为参数调用 <code>onValue</code> 回调。如果此 future 已经完成，回调不会立即调用，而会安排在稍后的微任务中执行。</p>',
 '2': '<p>如果提供了 <code>onError</code>，且此 future 以错误完成，则会以该错误及其堆栈跟踪为参数调用 <code>onError</code> 回调。<code>onError</code> 回调必须接受一个或两个参数，接受两个参数时，后一个参数为 <a href="dart-core/StackTrace-class.html">StackTrace</a>。如果 <code>onError</code> 接受两个参数，则传入错误和堆栈跟踪；否则仅传入错误对象。<code>onError</code> 回调必须返回可用于完成返回的 future 的值或 future，因此其返回结果必须能够赋值给 <code>FutureOr&lt;R&gt;</code>。</p>',
 '3': '<p>返回一个新的 <a href="dart-async/Future-class.html">Future</a>，它会以调用 <code>onValue</code>（此 future 以值完成时）或 <code>onError</code>（此 future 以错误完成时）的结果完成。</p>',
 '4': '<p>如果被调用的回调抛出错误，返回的 future 会以该错误及其堆栈跟踪完成。对于 <code>onError</code>，如果抛出的异常与传给 <code>onError</code> 的错误参数满足 <code>identical</code>，且异常是<em>同步</em>抛出的，则视为重新抛出，并使用原始堆栈跟踪。要在异步回调中使用相同的堆栈跟踪重新抛出错误，请使用 <a href="dart-core/Error/throwWithStackTrace.html">Error.throwWithStackTrace</a>。</p>',
 '5': '<p>如果回调返回一个 <a href="dart-async/Future-class.html">Future</a>，则 <code>then</code> 返回的 future 会以与回调返回的 future 相同的结果完成。</p>',
 '6': '<p>如果未提供 <code>onError</code>，且此 future 以错误完成，该错误会直接转发给返回的 future。</p>',
 '7': '<p>多数情况下，单独使用 <a href="foundation/SynchronousFuture/catchError.html">catchError</a>（可带有 <code>test</code> 参数），比在一次 <a href="foundation/SynchronousFuture/then.html">then</a> 调用中同时处理值和错误更易读。</p>',
 '8': '<p>请注意，future 不会等到添加监听器后才报告错误。如果首次调用 <code>then</code> 或 <code>catchError</code> 时，此 future 已经以错误完成，该错误就会被报告为未处理的错误。参见 <a href="dart-async/Future-class.html">Future</a> 的说明。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
