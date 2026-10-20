from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
for method, direction, status, terminal, sign in [('animateTo','正向','forward','completed','&gt;'),('animateBack','反向','reverse','dismissed','&lt;')]:
 obj[f'animation/AnimationController/{method}.html'] = {
  '0': f'<p>以“{direction}”方式驱动动画，从当前值运行到给定目标值。</p>',
  '1': '<p>返回一个 <a href="scheduler/TickerFuture-class.html">TickerFuture</a>，它将在动画完成时完成。</p>',
  '2': obj['animation/AnimationController/reset.html']['1'],
  '3': f'<p>动画运行期间，无论 <code>target</code> {sign} <a href="animation/AnimationController/value.html">value</a> 是否成立，<a href="animation/AnimationController/status.html">status</a> 都为 <a href="animation/AnimationStatus.html">AnimationStatus.{status}</a>。动画结束、到达 <code>target</code> 时，<a href="animation/AnimationController/status.html">status</a> 为 <a href="animation/AnimationStatus.html">AnimationStatus.{terminal}</a>。</p>',
  '4': '<p>如果 <code>target</code> 参数与动画当前的 <a href="animation/AnimationController/value.html">value</a> 相同，则不会运行动画，返回的 <a href="scheduler/TickerFuture-class.html">TickerFuture</a> 已处于完成状态。</p>',
 }
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
