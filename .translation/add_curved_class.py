from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/CurvedAnimation-class.html'] = {
 '0': '<p>对另一个动画应用曲线的动画。</p>',
 '1': '<p>当需要对动画对象应用非线性的 <a href="animation/Curve-class.html">Curve</a> 时，<a href="animation/CurvedAnimation-class.html">CurvedAnimation</a> 很有用，尤其是在希望动画正向和反向运行时使用不同曲线的情况下。</p>',
 '2': '<p>根据给定曲线，<a href="animation/CurvedAnimation-class.html">CurvedAnimation</a> 的输出范围可能比输入范围更宽。例如，<a href="animation/Curves/elasticIn-constant.html">Curves.elasticIn</a> 等弹性曲线会明显超过或低于默认的 0.0 到 1.0 范围。</p>',
 '3': '<p>如果要对 <a href="animation/Tween-class.html">Tween</a> 应用 <a href="animation/Curve-class.html">Curve</a>，可考虑使用 <a href="animation/CurveTween-class.html">CurveTween</a>。</p>',
 '4': '<p>不再需要 <a href="animation/CurvedAnimation-class.html">CurvedAnimation</a> 时应释放它，以清理可能添加的监听器。释放父动画（通常是 <a href="animation/AnimationController-class.html">AnimationController</a>）也会清理此对象。不要在 <code>build</code> 方法内创建 <a href="animation/CurvedAnimation-class.html">CurvedAnimation</a>，否则每次重建都会泄漏已添加的监听器。如果不需要 <a href="animation/CurvedAnimation/reverseCurve.html">reverseCurve</a>，优先使用 <code>parent.drive(CurveTween(curve: curve))</code>，它不需要单独释放。</p>',
 '7': '<p>默认情况下，<a href="animation/CurvedAnimation/reverseCurve.html">reverseCurve</a> 与正向的 <a href="animation/CurvedAnimation/curve.html">curve</a> 相同。</p>',
 '8': '<p>另请参阅：</p>',
}
obj['animation/CurvedAnimation/value.html'] = {'0': '<p>动画的当前值。</p>'}
obj['animation/CurvedAnimation/isDisposed.html'] = {'0': '<p>如果此 CurvedAnimation 已被释放，则为 true。</p>'}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
path = data / 'translations-fragments.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/CurvedAnimation-class.html'] = [
 {'source': 'The following code snippet shows how you can apply a curve to a linear\nanimation produced by an <a href="animation/AnimationController-class.html">AnimationController</a> <code>controller</code>.', 'translation': '下面的代码片段展示如何将曲线应用于 <a href="animation/AnimationController-class.html">AnimationController</a> <code>controller</code> 生成的线性动画。'},
 {'source': "This second code snippet shows how to apply a different curve in the forward\ndirection than in the reverse direction. This can't be done using a\n<a href=\"animation/CurveTween-class.html\">CurveTween</a> (since <a href=\"animation/Tween-class.html\">Tween</a>s are not aware of the animation direction when\nthey are applied).", 'translation': '第二个代码片段展示如何在正向和反向运行时应用不同的曲线。<a href="animation/CurveTween-class.html">CurveTween</a> 无法做到这一点，因为应用 <a href="animation/Tween-class.html">Tween</a> 时，它并不知道动画的运行方向。'},
]
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
