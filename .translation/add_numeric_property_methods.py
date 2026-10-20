from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
for cls in ('IntProperty', 'DoubleProperty', 'PercentProperty'):
 pages = {
 'numberToString': ['<p>仅描述数值 <a href="foundation/DiagnosticsProperty/value.html">value</a> 的字符串，不包含单位后缀。</p>'],
 'valueToString': ['<p>返回属性值的字符串表示。</p>', '<p>子类应重写此方法，而不是 <a href="foundation/DiagnosticsProperty/toDescription.html">toDescription</a>，以自定义属性值转换为字符串的方式。</p>', f'<p>重写此方法可确保所有实现以一致的方式修饰属性值，从而生成易读的 <a href="foundation/DiagnosticsProperty/toDescription.html">toDescription</a>。调试工具也可以选择直接使用 <a href="foundation/{cls}/valueToString.html">valueToString</a>，而不是 <a href="foundation/DiagnosticsProperty/toDescription.html">toDescription</a>。</p>', '<p><code>parentConfiguration</code> 指定父节点如何呈现为文本图形。例如，如果父节点将所有属性放在同一行，则属性值也应尽可能不换行。</p>'],
 }
 if cls != 'PercentProperty':
  pages['unit'] = ['<p><a href="foundation/DiagnosticsProperty/value.html">value</a> 的可选计量单位。</p>', '<p>单位必须适合紧接在数字后显示，中间不加空格。例如，“每个逻辑像素对应的物理像素数”应放在 <a href="foundation/DiagnosticsProperty/tooltip.html">tooltip</a> 中，而不是作为 <code>unit</code>。</p>']
 for member, blocks in pages.items():
  d[f'foundation/{cls}/{member}.html'] = {str(i): block for i, block in enumerate(blocks)}
d['foundation/DoubleProperty/DoubleProperty.lazy.html'] = {'0': '<p>仅在需要时才计算 <a href="foundation/DiagnosticsProperty/value.html">value</a> 的属性。</p>', '1': '<p>当计算属性 <a href="foundation/DiagnosticsProperty/value.html">value</a> 可能抛出异常或开销较大时使用。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
