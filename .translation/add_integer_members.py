from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
common = '<p>首次使用补间之前，<code>begin</code> 和 <code>end</code> 属性必须非 null；如果准备稍后填入这些值，构造函数参数可以为 null。</p>'
obj['animation/IntTween/IntTween.html'] = {'0': '<p>创建整数补间。</p>', '1': common}
obj['animation/StepTween/StepTween.html'] = {'0': '<p>创建结果向下取整的 <a href="dart-core/int-class.html">int</a> 补间。</p>', '1': common}
obj['animation/StepTween/lerp.html'] = dict(obj['animation/ReverseTween/lerp.html'])
obj['animation/ReverseTween/parent.html'] = {
 '0': '<p>此补间的值等于对父补间反向求值的结果。</p>',
 '1': '<p>此补间的 <a href="animation/Tween/begin.html">begin</a> 是父补间的 <a href="animation/Tween/end.html">end</a>，而其 <a href="animation/Tween/end.html">end</a> 是父补间的 <a href="animation/Tween/begin.html">begin</a>。<a href="animation/ReverseTween/lerp.html">lerp</a> 方法返回 <code>parent.lerp(1.0 - t)</code>，<a href="animation/Animatable/evaluate.html">evaluate</a> 方法也采用类似方式。</p>',
}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
