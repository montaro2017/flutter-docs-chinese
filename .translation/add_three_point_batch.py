from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'shared-text.json'
shared = json.loads(path.read_text(encoding='utf-8'))
labels = {
 'Creates a cubic curve.': '创建一条三次曲线。',
 'Creates two cubic curves that share a common control point.': '创建两条共享同一控制点的三次曲线。',
 ', where many more predefined curves are available.': '，其中提供了更多预定义曲线。',
 ', a curve which passes through specific values.': '，一种经过指定值的曲线。',
 ', which defines a single cubic polynomial.': '，用于定义单个三次多项式。',
 'The coordinates of the middle shared point.': '两条曲线共享的中间点的坐标。',
}
for key, ordinal in [('a','第一'), ('b','第一'), ('c','第二'), ('d','第二')]:
 axis = 'x' if key in ['a','c'] else 'y'
 en = 'first' if ordinal == '第一' else 'second'
 labels[f'The {axis} coordinate of the {en} control point.'] = f'{ordinal}个控制点的 {axis} 坐标。'
for key, control, curve in [('a1','第一','第一'), ('b1','第二','第一'), ('a2','第一','第二'), ('b2','第二','第二')]:
 en_control = 'first' if control == '第一' else 'second'
 en_curve = 'first' if curve == '第一' else 'second'
 labels[f'The coordinates of the {en_control} control point of the {en_curve} curve.'] = f'{curve}条曲线的{control}个控制点的坐标。'
shared.update(labels)
path.write_text(json.dumps(shared, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/ThreePointCubic/ThreePointCubic.html'] = {
 '0': '<p>创建两条共享同一控制点的三次曲线。</p>',
 '1': '<p>可以考虑使用 <a href="animation/Curves-class.html">Curves</a> 中的常用三点三次曲线，而不必创建新实例。</p>',
 '2': '<p>参数对应两条曲线的控制点，包括 <code>midpoint</code>，但不包括两个隐含的固定端点 (0,0) 和 (1,1)。</p>',
}
for key, control, curve in [('a1','第一','第一'), ('b1','第二','第一'), ('a2','第一','第二'), ('b2','第二','第二')]:
 if key == 'a1':
  tangent = '<p>经过点 (0, 0) 和此控制点的直线，在点 (0, 0) 处与曲线相切。</p>'
 elif key == 'b2':
  tangent = '<p>经过点 (1, 1) 和此控制点的直线，在 (1, 1) 处与曲线相切。</p>'
 else:
  link = '<a href="animation/ThreePointCubic/midpoint.html">midpoint</a>'
  tangent = f'<p>经过 {link} 和此控制点的直线，与趋近 {link} 时的曲线相切。</p>'
 obj[f'animation/ThreePointCubic/{key}.html'] = {'0': f'<p>{curve}条曲线的{control}个控制点的坐标。</p>', '1': tangent}
obj['animation/ThreePointCubic/midpoint.html'] = {
 '0': '<p>两条曲线共享的中间点的坐标。</p>',
 '1': '<p>曲线将经过此点。如果此中间点两侧的控制点（<a href="animation/ThreePointCubic/b1.html">b1</a> 和 <a href="animation/ThreePointCubic/a2.html">a2</a>）与此点不共线，则曲线的导数在此点处不连续（形成尖点）。</p>',
}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
