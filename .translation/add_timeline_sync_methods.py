from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'instantSync': ['<p>发出一个瞬时事件。</p>', '<p>可以直接替代 <a href="dart-developer/Timeline/instantSync.html">Timeline.instantSync</a>。</p>'],
 'startSync': ['<p>启动一个标记为 <code>name</code> 的同步操作。</p>', '<p>可以选择传入 <code>arguments</code> 映射。此时间片也可以选择关联一个 <a href="dart-developer/Flow-class.html">Flow</a> 事件。返回事件队列之前，必须调用 <a href="foundation/FlutterTimeline/finishSync.html">finishSync</a> 结束此操作。</p>', '<p>可以直接替代 <a href="dart-developer/Timeline/startSync.html">Timeline.startSync</a>。</p>'],
 'timeSync': ['<p>用于测量同步 <code>function</code> 耗时的实用方法。</p>', '<p>内部调用 <code>function</code>，并在调用前后分别调用 <a href="foundation/FlutterTimeline/startSync.html">startSync</a> 和 <a href="foundation/FlutterTimeline/finishSync.html">finishSync</a>。</p>', '<p>可以直接替代 <a href="dart-developer/Timeline/timeSync.html">Timeline.timeSync</a>。</p>'],
}
for member, blocks in pages.items():
 d[f'foundation/FlutterTimeline/{member}.html'] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
