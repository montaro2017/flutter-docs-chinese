from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/Cubic-class.html'] = {
 '0': '<p>单位区间上的三次多项式映射。</p>',
 '1': '<p><a href="animation/Curves-class.html">Curves</a> 类包含一些常用的三次曲线：</p>',
 '2': '<p><a href="animation/Cubic-class.html">Cubic</a> 类实现三阶贝塞尔曲线。</p>',
 '3': '<p>另请参阅：</p>',
}
obj['animation/ThreePointCubic-class.html'] = {
 '0': '<p>由两条共享同一中间点的曲线组成的三次多项式。</p>',
 '1': '<p>曲线经过三个点：(0,0)、<a href="animation/ThreePointCubic/midpoint.html">midpoint</a> 和 (1,1)。</p>',
 '2': '<p><a href="animation/Curves-class.html">Curves</a> 类包含一条使用此类定义的曲线：<a href="animation/Curves/easeInOutCubicEmphasized-constant.html">Curves.easeInOutCubicEmphasized</a>。</p>',
 '3': '<p><a href="animation/ThreePointCubic-class.html">ThreePointCubic</a> 类实现三阶贝塞尔曲线，两条曲线共享一个内部的 <a href="animation/ThreePointCubic/midpoint.html">midpoint</a>，曲线经过该点。如果中间点两侧的控制点（<a href="animation/ThreePointCubic/b1.html">b1</a> 和 <a href="animation/ThreePointCubic/a2.html">a2</a>）与中间点不共线，则曲线的导数在这个共享的中间点处不连续（形成尖点）。</p>',
 '4': '<p>另请参阅：</p>',
}
for name, axis, ordinal, point in [('a','x','第一','0'),('b','y','第一','0'),('c','x','第二','1'),('d','y','第二','1')]:
 obj[f'animation/Cubic/{name}.html'] = {
  '0': f'<p>{ordinal}个控制点的 {axis} 坐标。</p>',
  '1': f'<p>经过点 ({point}, {point}) 和{ordinal}个控制点的直线，在点 ({point}, {point}) 处与曲线相切。</p>',
 }
obj['animation/Cubic/Cubic.html'] = {
 '0': '<p>创建一条三次曲线。</p>',
 '1': '<p>可以考虑使用 <a href="animation/Curves-class.html">Curves</a> 中的常用三次曲线，而不必创建新实例。</p>',
}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
