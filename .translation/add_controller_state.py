from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'animation/AnimationController/isAnimating.html': {
  '0': '<p>此动画当前是否正在沿正向或反向运行。</p>',
  '1': '<p>这与是否正在接收时钟更新是不同的概念。动画控制器的 ticker 可能被静默，此时即使时间仍在流逝，动画控制器的回调也不会再触发。请参阅 <a href="scheduler/Ticker/muted.html">Ticker.muted</a> 和 <a href="widgets/TickerMode-class.html">TickerMode</a>。</p>',
  '2': '<p>如果动画已停止（例如调用 <a href="animation/AnimationController/stop.html">stop</a> 或设置新的 <a href="animation/AnimationController/value.html">value</a>），<a href="animation/AnimationController/isAnimating.html">isAnimating</a> 将返回 <code>false</code>，但 <a href="animation/AnimationController/status.html">status</a> 不会改变，因此 <a href="animation/AnimationStatus/isAnimating.html">AnimationStatus.isAnimating</a> 的值可能仍为 <code>true</code>。</p>',
 },
 'animation/AnimationController/velocity.html': {
  '0': '<p><a href="animation/AnimationController/value.html">value</a> 每秒的变化率。</p>',
  '1': '<p>如果 <a href="animation/AnimationController/isAnimating.html">isAnimating</a> 为 false，则 <a href="animation/AnimationController/value.html">value</a> 不再变化，变化率为零。</p>',
 },
 'animation/AnimationController/lastElapsedDuration.html': {
  '0': '<p>从动画开始到最近一次动画时钟更新之间经过的时间。</p>',
  '1': '<p>如果控制器未在运行动画，最近经过的时长为 null。</p>',
 },
 'animation/AnimationController/view.html': {'0': '<p>返回此动画控制器对应的 <a href="animation/Animation-class.html">Animation&lt;double&gt;</a>，使此对象的引用可以传递给其他使用方，而不允许使用方修改 <a href="animation/AnimationController-class.html">AnimationController</a> 的状态。</p>'},
 'animation/AnimationController/status.html': {'0': '<p>此动画的当前状态。</p>'},
 'animation/AnimationController/reset.html': {
  '0': '<p>将控制器的值设为 <a href="animation/AnimationController/lowerBound.html">lowerBound</a>，停止正在运行的动画，并重置到起点，即 dismissed 状态。</p>',
  '1': '<p>最近返回的 <a href="scheduler/TickerFuture-class.html">TickerFuture</a>（如果存在）会被标记为已取消，这意味着该 future 永远不会完成，而其派生的 <a href="scheduler/TickerFuture/orCancel.html">TickerFuture.orCancel</a> future 将以 <a href="scheduler/TickerCanceled-class.html">TickerCanceled</a> 错误完成。</p>',
  '2': '<p>另请参阅：</p>',
 },
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
