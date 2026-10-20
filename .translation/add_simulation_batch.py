from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
for method, status in [('animateWith', 'forward'), ('animateBackWith', 'reverse')]:
 first = '<p>根据给定的模拟驱动动画。</p>' if method == 'animateWith' else '<p>根据给定的模拟驱动动画，<a href="animation/AnimationController/status.html">status</a> 为 <a href="animation/AnimationStatus.html">AnimationStatus.reverse</a>。</p>'
 obj[f'animation/AnimationController/{method}.html'] = {
  '0': first,
  '1': '<p>模拟产生的值会被限制在 <a href="animation/AnimationController/lowerBound.html">lowerBound</a> 和 <a href="animation/AnimationController/upperBound.html">upperBound</a> 之间。若要避免此限制，可考虑使用 <a href="animation/AnimationController/AnimationController.unbounded.html">AnimationController.unbounded</a> 构造函数创建 <a href="animation/AnimationController-class.html">AnimationController</a>。</p>',
  '2': '<p>返回一个 <a href="scheduler/TickerFuture-class.html">TickerFuture</a>，它将在动画完成时完成。</p>',
  '3': obj['animation/AnimationController/reset.html']['1'],
  '4': f'<p>在整个模拟过程中，<a href="animation/AnimationController/status.html">status</a> 始终为 <a href="animation/AnimationStatus.html">AnimationStatus.{status}</a>。</p>',
  '5': '<p>另请参阅：</p>',
 }
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
