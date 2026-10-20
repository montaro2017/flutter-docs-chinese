from pathlib import Path
import json
data = Path(__file__).resolve().parent
def update(name, entries):
 path = data / name
 obj = json.loads(path.read_text(encoding='utf-8'))
 obj.update(entries)
 path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
update('translations.json', {
 'animation/Curve2DSample-class.html': {
  '0': '<p>保存二维参数曲线采样点的类，包含曲线在参数值 <a href="animation/Curve2DSample/t.html">t</a> 处的 <a href="animation/Curve2DSample/value.html">value</a>（X、Y 坐标）。</p>',
  '1': '<p>另请参阅：</p>',
 },
 'animation/Curve2DSample/Curve2DSample.html': {'0': '<p>创建保存采样点的对象，与 <a href="animation/Curve2D-class.html">Curve2D</a> 的子类配合使用。</p>'},
 'animation/Curve2DSample/t.html': {'0': '<p>此采样点沿曲线的参数位置。</p>'},
 'animation/Curve2DSample/value.html': {'0': '<p>曲线在参数值 <a href="animation/Curve2DSample/t.html">t</a> 处的值（X、Y 坐标）。</p>'},
 'animation/Curve2D/samplingSeed.html': {
  '0': '<p>返回供 <a href="animation/Curve2D/generateSamples.html">generateSamples</a> 使用的种子值，用于初始化随机数生成器，以避免采样混叠。</p>',
  '1': '<p>子类应重写此属性并提供自定义种子。</p>',
  '2': '<p>除非曲线定义发生变化，否则每次调用都应返回相同的值。</p>',
 },
})
update('shared-text.json', {
 'To create a local project with this code sample, run:': '要使用此代码示例创建本地项目，请运行：',
 'Returns a seed value used by': '返回供',
 'to seed a random number generator to avoid sample aliasing.': '使用的种子值，用于初始化随机数生成器，以避免采样混叠。',
 'Returns the parameter': '返回参数',
 'that corresponds to the given x value of the spline.': '，它对应样条曲线的给定 x 值。',
 'Generates a list of samples with a recursive subdivision until a tolerance of': '通过递归细分生成采样点列表，直到达到以下容差：',
 'is reached.': '。',
 ', which generates samples of this type.': '，用于生成此类型的采样点。',
 ', a parametric curve that maps a double parameter to a 2D location.': '，一种将 double 参数映射为二维位置的参数曲线。',
 'Creates an object that holds a sample; used with': '创建保存采样点的对象，与',
 'subclasses.': '的子类配合使用。',
 'The parametric location of this sample point along the curve.': '此采样点沿曲线的参数位置。',
 'The value (the X, Y coordinates) of the curve at parametric value': '曲线在以下参数值处的值（X、Y 坐标）：',
})
