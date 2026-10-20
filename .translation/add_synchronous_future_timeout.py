from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/SynchronousFuture/timeout.html'] = {
 '0': '<p>经过 <code>timeLimit</code> 指定的时间后，停止等待此 future。</p>',
 '1': '<p>创建一个新的<em>超时 future</em>。<em>如果</em>此 future（即<em>源 future</em>）在规定时间内完成，超时 future 就会以相同的结果完成。</p>',
 '2': '<p>如果源 future 未在 <code>timeLimit</code> 指定的时间内完成，则执行 <code>onTimeout</code>，并将其结果（返回值或抛出的错误）用作超时 future 的结果。<code>onTimeout</code> 函数必须返回 <code>T</code> 或 <code>Future&lt;T&gt;</code>。如果 <code>onTimeout</code> 返回一个 future（即<em>替代结果 future</em>），则使用替代结果 future 的最终结果来完成超时 future，即使源 future 比替代结果 future 更早完成也是如此。决定因素仅在于源 future 未能按时完成。</p>',
 '3': '<p>如果省略 <code>onTimeout</code>，超时会使返回的 future 以 <a href="dart-async/TimeoutException-class.html">TimeoutException</a> 完成。</p>',
 '4': '<p>无论哪种情况，源 future 都仍可在稍后正常完成。只是除非它在时间限制内完成，否则其结果不会被用作超时 future 的结果。即使源 future 以错误完成，如果错误发生在 <code>timeLimit</code> 指定的时间之后，也会像值结果一样被忽略。</p>',
 '5': '<p>示例：</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
