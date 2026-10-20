from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
for method, direction, terminal, bound, endpoint in [('forward','正向','completed','upperBound','终点'),('reverse','反向','dismissed','lowerBound','起点')]:
 obj[f'animation/AnimationController/{method}.html'] = {
  '0': f'<p>开始{direction}运行此动画（朝向{endpoint}）。</p>',
  '1': f'<p>返回一个 <a href="scheduler/TickerFuture-class.html">TickerFuture</a>，它将在动画到达{endpoint}时完成。</p>',
  '2': '<p>如果 <code>from</code> 非 null，将在运行动画之前把它设为当前的 <a href="animation/AnimationController/value.html">value</a>。</p>',
  '3': obj['animation/AnimationController/reset.html']['1'],
  '4': f'<p>动画运行期间，<a href="animation/AnimationController/status.html">status</a> 为 <a href="animation/AnimationStatus.html">AnimationStatus.{method}</a>；动画结束时达到 <a href="animation/AnimationController/{bound}.html">{bound}</a> 后，状态切换为 <a href="animation/AnimationStatus.html">AnimationStatus.{terminal}</a>。</p>',
 }
obj['animation/AnimationController/resync.html'] = {'0': '<p>使用新的 <a href="scheduler/TickerProvider-class.html">TickerProvider</a> 重新创建 <a href="scheduler/Ticker-class.html">Ticker</a>。</p>'}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
