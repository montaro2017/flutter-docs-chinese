from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/Curve2D-class.html'] = {
 '0': '<p>定义二维参数曲线求值 API 的抽象类。</p>',
 '1': '<p><a href="animation/Curve2D-class.html">Curve2D</a> 与 <a href="animation/Curve-class.html">Curve</a> 的区别在于，插值结果是 <a href="dart-ui/Offset-class.html">Offset</a> 值而非 <a href="dart-core/double-class.html">double</a> 值，名称中的“2D”由此而来。两者都将一个范围为 0.0 到 1.0（包含端点）的 double 参数 <code>t</code> 作为 <a href="animation/ParametricCurve/transform.html">transform</a> 函数的输入。与 <a href="animation/Curve-class.html">Curve</a> 不同，<a href="animation/Curve2D-class.html">Curve2D</a> 不要求将 <code>t=0.0</code> 和 <code>t=1.0</code> 映射为特定的输出值。</p>',
 '2': '<p>传给 <a href="animation/ParametricCurve/transform.html">transform</a> 的插值参数 <code>t</code> 表示沿曲线的进度，但不一定以恒定速度推进。因此，将 <code>t</code> 增加例如 0.1，可能在曲线的某一段移动很长距离，在另一段却几乎没有移动，具体取决于曲线的定义。</p>',
}
obj['animation/Curve2D/Curve2D.html'] = {'0': '<p>抽象 const 构造函数，使子类能够提供 const 构造函数，从而用于 const 表达式。</p>'}
obj['animation/Curve2D/generateSamples.html'] = {
 '0': '<p>通过递归细分生成采样点列表，直到达到 <code>tolerance</code> 指定的容差。</p>',
 '1': '<p>采样点按顺序生成。</p>',
 '2': '<p>采样点可以用于高效绘制曲线，因为相邻采样点形成的线段长度会随曲线的曲率变化。还可以通过查找所需的 X 区间，并在采样点之间进行线性插值，得到目标 X 值对应的 Y 近似值，从而快速估算曲线的值。<a href="animation/CatmullRomCurve-class.html">CatmullRomCurve</a> 的实现内部正是这样使用采样点的。</p>',
 '3': '<p>容差按新采样点与其前后两个采样点构成的三角形面积计算。</p>',
 '4': '<p>另请参阅：</p>',
}
obj['animation/Curve2D/findInverse.html'] = {
 '0': '<p>返回与样条曲线给定 x 值对应的参数 <code>t</code>。</p>',
 '1': '<p>此方法仅对关于 x 为单值的曲线有效，即每个 <code>x</code> 值只对应一个 y 值，曲线不会形成环或折返。对于非单值曲线，它只返回给定 <code>x</code> 位置的其中一个值所对应的参数。</p>',
}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
path = data / 'translations-fragments.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/Curve2D-class.html'] = [{
 'source': 'This example shows how to use a <a href="animation/Curve2D-class.html">Curve2D</a> to modify the position of a widget\nso that it can follow an arbitrary path.',
 'translation': '此示例展示如何使用 <a href="animation/Curve2D-class.html">Curve2D</a> 修改组件的位置，使其沿任意路径移动。',
}]
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
