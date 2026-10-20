from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/SynchronousFuture/whenComplete.html'] = {
 '0': '<p>注册在此 future 完成时调用的函数。</p>',
 '1': '<p>此 future 完成时，无论以值还是以错误完成，都会调用 <code>action</code> 函数。</p>',
 '2': '<p>这是 finally 块的异步对应形式。</p>',
 '3': '<p>此次调用返回的 future <code>f</code> 将以与此 future 相同的方式完成，除非调用 <code>action</code> 时发生错误，或 <code>action</code> 返回的 <a href="dart-async/Future-class.html">Future</a> 发生错误。如果调用 <code>action</code> 没有返回 future，则忽略其返回值。</p>',
 '4': '<p>如果调用 <code>action</code> 抛出错误，则 <code>f</code> 会以该错误完成。</p>',
 '5': '<p>如果调用 <code>action</code> 返回一个 <a href="dart-async/Future-class.html">Future</a> <code>f2</code>，则 <code>f</code> 会等待 <code>f2</code> 完成后再完成。如果 <code>f2</code> 以错误完成，该错误也会成为 <code>f</code> 的结果。<code>f2</code> 的值始终会被忽略。</p>',
 '6': '<p>此方法等价于：</p>',
 '7': '<p>示例：</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
