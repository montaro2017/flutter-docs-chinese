from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/compute.html'] = {
 '0': '<p>在后台异步执行给定的 <code>callback</code>，将提供的 <code>message</code> 传给它，并以执行结果完成。</p>',
 '1': '<p>适用于耗时超过几毫秒、因而可能导致掉帧的操作。对于耗时不超过一毫秒的任务，可以考虑使用 <a href="scheduler/SchedulerBinding/scheduleTask.html">SchedulerBinding.scheduleTask</a>。</p>',
 '3': '<p>在 Web 平台上，会在当前事件循环中执行 <code>callback</code>。在原生平台上，会在独立的 isolate 中执行 <code>callback</code>。</p>',
 '4': d['foundation/ComputeCallback.html']['1'],
 '5': d['foundation/ComputeCallback.html']['2'],
 '6': '<p>在原生平台上，<code>await compute(fun, message)</code> 等价于 <code>await Isolate.run(() =&gt; fun(message))</code>。另请参阅 <a href="dart-isolate/Isolate/run.html">Isolate.run</a>。</p>',
 '7': '<p>如果提供了 <code>debugLabel</code>，它会用作执行 <code>callback</code> 的 isolate 的名称。该 isolate 产生的 <a href="dart-developer/Timeline-class.html">Timeline</a> 事件会关联此名称，这有助于分析应用性能。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/compute.html'] = [{
 'source': 'The following code uses the <a href="foundation/compute.html">compute</a> function to check whether a given\ninteger is a prime number.',
 'translation': '下面的代码使用 <a href="foundation/compute.html">compute</a> 函数检查给定整数是否为质数。',
}]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
