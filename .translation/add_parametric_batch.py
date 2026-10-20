from pathlib import Path
import json
data = Path(__file__).resolve().parent
def update(name, entries):
 path = data / name
 obj = json.loads(path.read_text(encoding='utf-8'))
 obj.update(entries)
 path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
update('translations.json', {
 'animation/ParametricCurve-class.html': {
  '0': '<p>提供参数曲线求值接口的抽象类。</p>',
  '1': '<p>参数曲线将参数 <code>t</code>（名称由此而来）沿曲线映射为曲线在该 <code>t</code> 值处的值。曲线可以具有任意维度，但通常是一维、二维或三维曲线。</p>',
  '2': '<p>另请参阅：</p>',
 },
 'animation/ParametricCurve/transform.html': {
  '0': '<p>返回曲线在点 <code>t</code> 处的值。</p>',
  '1': '<p>此方法先断言 t 在 0 到 1 之间，再委托给 <a href="animation/ParametricCurve/transformInternal.html">transformInternal</a>。</p>',
  '2': '<p>建议子类重写 <a href="animation/ParametricCurve/transformInternal.html">transformInternal</a>，而不是此函数，因为 <a href="animation/ParametricCurve/transform.html">transform</a> 的默认实现已处理上述情况，并将其余逻辑委托给 <a href="animation/ParametricCurve/transformInternal.html">transformInternal</a>。</p>',
 },
 'animation/ParametricCurve/transformInternal.html': {
  '0': '<p>返回曲线在点 <code>t</code> 处的值。</p>',
  '1': '<p>给定参数值 <code>t</code> 将位于 0.0 到 1.0 之间，包含两个端点。</p>',
 },
 'animation/ParametricCurve/ParametricCurve.html': {'0': '<p>抽象 const 构造函数，使子类能够提供 const 构造函数，从而用于 const 表达式。</p>'},
 'animation/Curve/transform.html': {
  '0': '<p>返回曲线在点 <code>t</code> 处的值。</p>',
  '1': '<p>此函数必须保证：</p>',
  '2': '<p>建议子类重写 <a href="animation/ParametricCurve/transformInternal.html">transformInternal</a>，而不是此函数，因为 <a href="animation/Curve/transform.html">transform</a> 的默认实现已处理上述情况，并将其余逻辑委托给 <a href="animation/ParametricCurve/transformInternal.html">transformInternal</a>。</p>',
 },
})
update('shared-text.json', {
 ', a 1D animation easing curve that starts at 0.0 and ends at 1.0.': '，一种从 0.0 开始、到 1.0 结束的一维动画缓动曲线。',
 ', a parametric curve that transforms the parameter to a 2D point.': '，一种将参数映射为二维点的参数曲线。',
})
path = data / 'translations-fragments.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/Curve/transform.html'] = [
 {'source': '<li>The value of <code>t</code> must be between 0.0 and 1.0</li>', 'translation': '<li><code>t</code> 的值必须在 0.0 到 1.0 之间</li>'},
 {'source': '<li>Values of <code>t</code>=0.0 and <code>t</code>=1.0 must be mapped to 0.0 and 1.0,\nrespectively.</li>', 'translation': '<li><code>t</code>=0.0 和 <code>t</code>=1.0 必须分别映射为 0.0 和 1.0。</li>'},
]
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
