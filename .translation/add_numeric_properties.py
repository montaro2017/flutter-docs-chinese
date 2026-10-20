from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'IntProperty-class.html': ['<p>值为 int 的属性，可选择指定该值的计量单位。</p>', '<p>单位示例包括“px”和“ms”。</p>'],
 'IntProperty/IntProperty.html': ['<p>创建一个用于整数的诊断属性。</p>'],
 'DoubleProperty-class.html': ['<p>描述 <a href="dart-core/double-class.html">double</a> 类型的 <a href="foundation/DiagnosticsProperty/value.html">value</a> 的属性，可选择指定计量 <code>unit</code>。</p>', '<p>数值格式针对调试消息的可读性进行了优化。</p>'],
 'DoubleProperty/DoubleProperty.html': ['<p>如果指定了 <code>unit</code>，它表示 <code>value</code> 的单位（例如 px）。</p>'],
 'PercentProperty-class.html': ['<p>将 <a href="dart-core/double-class.html">double</a> 限制在 0 到 1 之间，并将其格式化为百分比的属性。</p>'],
 'PercentProperty/PercentProperty.html': ['<p>为表示百分比或比例的 double 值创建诊断属性。</p>', '<p>对于 <a href="foundation/PercentProperty-class.html">PercentProperty</a> 对象，将 <code>showName</code> 设置为 false 通常是合理的，因为以百分比形式显示通常足以明确该属性的含义。</p>'],
}
for page, blocks in pages.items():
 d['foundation/' + page] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
