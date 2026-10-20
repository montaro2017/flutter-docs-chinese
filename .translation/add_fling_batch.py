from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/AnimationController/fling.html'] = {
 '0': '<p>使用弹簧和初始速度驱动动画，范围限制在 <a href="animation/AnimationController/lowerBound.html">lowerBound</a> 与 <a href="animation/AnimationController/upperBound.html">upperBound</a> 之间。</p>',
 '1': '<p>如果速度为正，动画将运行到完成状态；否则运行到 dismissed 状态。速度以每秒单位数表示。如果设置了 <a href="semantics/SemanticsBinding/disableAnimations.html">SemanticsBinding.disableAnimations</a> 标志，速度会乘以一个较为任意的系数 200。</p>',
 '2': '<p><code>springDescription</code> 参数可用于指定驱动动画的自定义 <a href="physics/SpringType.html">SpringType.criticallyDamped</a> 或 <a href="physics/SpringType.html">SpringType.overDamped</a> 弹簧。默认使用 <a href="physics/SpringType.html">SpringType.criticallyDamped</a> 弹簧。有关如何创建合适的 <a href="physics/SpringDescription-class.html">SpringDescription</a>，请参阅 <a href="physics/SpringDescription/SpringDescription.withDampingRatio.html">SpringDescription.withDampingRatio</a>。</p>',
 '3': '<p>生成的弹簧模拟不能是 <a href="physics/SpringType.html">SpringType.underDamped</a> 类型，因为这种弹簧会振荡，而不是执行 fling。</p>',
 '4': '<p>返回一个 <a href="scheduler/TickerFuture-class.html">TickerFuture</a>，它将在动画完成时完成。</p>',
 '5': obj['animation/AnimationController/reset.html']['1'],
}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
