from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
for cls, typ, meaning in [('ColorTween','Color','透明色'),('SizeTween','Size','空尺寸'),('RectTween','Rect','位于左上角的空矩形')]:
 obj[f'animation/{cls}/{cls}.html'] = {
  '0': f'<p>创建一个 <a href="dart-ui/{typ}-class.html">{typ}</a> 补间。</p>',
  '1': f'<p><code>begin</code> 和 <code>end</code> 属性可以为 null；null 值被视为{meaning}。</p>',
 }
 obj[f'animation/{cls}/lerp.html'] = {'0': '<p>返回此变量在给定动画时钟值处的值。</p>'}
obj['animation/ColorTween/ColorTween.html']['2'] = '<p>如果希望实现从透明状态淡入或淡出的效果，建议不要将 <a href="material/Colors/transparent-constant.html">Colors.transparent</a> 作为 <code>begin</code> 或 <code>end</code>，而应使用 null。<a href="material/Colors/transparent-constant.html">Colors.transparent</a> 表示透明黑色，因此会从黑色淡入或向黑色淡出，这很可能并非预期效果。</p>'
obj['animation/ReverseTween/ReverseTween.html'] = {'0': '<p>构造一个对其 <code>parent</code> 反向求值的 <a href="animation/Tween-class.html">Tween</a>。</p>'}
obj['animation/ReverseTween/lerp.html'] = {
 '0': '<p>返回此变量在给定动画时钟值处的值。</p>',
 '1': '<p>此方法的默认实现对 <code>T</code> 使用 <code>+</code>、<code>-</code> 和 <code>*</code> 运算符。因此，调用此方法时，<a href="animation/Tween/begin.html">begin</a> 和 <a href="animation/Tween/end.html">end</a> 属性必须非 null。</p>',
 '2': '<p>不过，一般情况下此方法仍可能返回 null，尤其是在 <code>t</code>=0.0 且 <a href="animation/Tween/begin.html">begin</a> 为 null，或 <code>t</code>=1.0 且 <a href="animation/Tween/end.html">end</a> 为 null 时。</p>',
}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
