from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/AnimationController/repeat.html'] = {
 '0': '<p>开始正向运行此动画，并在完成后重新开始。</p>',
 '1': '<p>如果未显式设置 <code>min</code> 和 <code>max</code>，默认在 <a href="animation/AnimationController-class.html">AnimationController</a> 的 <a href="animation/AnimationController/lowerBound.html">lowerBound</a> 与 <a href="animation/AnimationController/upperBound.html">upperBound</a> 之间重复运行。</p>',
 '2': '<p>将 <code>reverse</code> 设为 true 后，每次重复的起始值会在 <code>min</code> 和 <code>max</code> 之间交替，而不是始终从 <code>min</code> 重新开始。动画从 <code>max</code> 运行到 <code>min</code> 时，<a href="animation/AnimationController/status.html">status</a> 为 <a href="animation/AnimationStatus.html">AnimationStatus.reverse</a>。</p>',
 '3': '<p>动画每次运行的时长为 <code>period</code>。如果未提供 <code>period</code>，则使用 <a href="animation/AnimationController/duration.html">duration</a>。必须在调用 <a href="animation/AnimationController/repeat.html">repeat</a> 之前设置该时长，可以在构造函数中设置，也可以稍后通过 <a href="animation/AnimationController/duration.html">duration</a> setter 设置。</p>',
 '4': '<p>如果为 <code>count</code> 传入值，动画将在运行指定次数后停止。否则，动画会无限重复。</p>',
 '5': '<p>返回一个永远不会完成的 <a href="scheduler/TickerFuture-class.html">TickerFuture</a>，除非指定了 <code>count</code>。动画停止时（例如调用 <a href="animation/AnimationController/stop.html">stop</a>），<a href="scheduler/TickerFuture/orCancel.html">TickerFuture.orCancel</a> future 会以错误完成。</p>',
 '6': obj['animation/AnimationController/reset.html']['1'],
}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
