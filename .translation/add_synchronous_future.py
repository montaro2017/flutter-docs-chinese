from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/SynchronousFuture-class.html': {
 '0': '<p>其 <a href="foundation/SynchronousFuture/then.html">then</a> 实现会立即调用回调的 <a href="dart-async/Future-class.html">Future</a>。</p>',
 '1': '<p>它类似于 <a href="dart-async/Future/Future.value.html">Future.value</a>，但值在同一次事件循环迭代中即可使用。</p>',
 '2': '<p>⚠ 如果希望提供一个统一的 API，通常同步执行所有操作，但在少数情况下能够切换为异步模式，此类会很有用。<strong>通常应避免使用此类，因为这种兼具同步和异步两种模式的行为非常难以调试。</strong></p>',
 '3': '<p><a href="foundation/SynchronousFuture-class.html">SynchronousFuture</a> 永远不会以错误完成。</p>',
 },
 'foundation/SynchronousFuture/SynchronousFuture.html': {
 '0': '<p>创建一个同步 future。</p>',
 '1': '<p>另请参阅：</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/SynchronousFuture/SynchronousFuture.html'] = [{
 'source': '<li><a href="dart-async/Future/Future.value.html">Future.value</a> for information about creating a regular\n<a href="dart-async/Future-class.html">Future</a> that completes with a value.</li>',
 'translation': '<li><a href="dart-async/Future/Future.value.html">Future.value</a>，介绍如何创建以一个值完成的普通 <a href="dart-async/Future-class.html">Future</a>。</li>',
}]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/SynchronousFuture-class.html'] = {
 '2': '<dd>创建一个同步 future。</dd>',
 '5': '<dd>创建一个包含此 future 结果的 <a href="dart-async/Stream-class.html">Stream</a>。<div class="features"><span class="feature">重写</span></div></dd>',
 '6': '<dd>处理此 <a href="dart-async/Future-class.html">Future</a> 发出的错误。<div class="features"><span class="feature">重写</span></div></dd>',
 '9': '<dd>注册在此 future 完成时调用的回调。<div class="features"><span class="feature">重写</span></div></dd>',
 '10': '<dd>经过 <code>timeLimit</code> 指定的时间后，停止等待此 future。<div class="features"><span class="feature">重写</span></div></dd>',
 '11': '<dd>注册在此 future 完成时调用的函数。<div class="features"><span class="feature">重写</span></div></dd>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
