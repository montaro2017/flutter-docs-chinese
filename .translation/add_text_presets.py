from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
data = {
 'dashed': ['与 <a href="foundation/sparseTextConfiguration.html">sparseTextConfiguration</a> 相同，但连接父子节点的线条为虚线。', '示例：', '另请参阅：'],
 'dense': ['尽量减少水平空白的紧凑文本树配置。', '示例：', '另请参阅：'],
 'errorProperty': ['将名称渲染在一行，主体和属性放在下一行，省略子节点。', '示例：', '另请参阅：'],
 'error': ['在节点周围绘制边框、忽略其与父节点连接的配置。', '如果嵌套在树中，最好在属性框中显示此节点，而不是将其作为常规子节点显示。', '用于在异常的详细描述周围绘制装饰性边框。', '示例：', '另请参阅：'],
 'flat': ['仅使用空白字符、不缩进子节点的配置。', '当无需通过缩进区分父子节点时使用此样式，例如 <a href="foundation/DiagnosticsStackTrace-class.html">DiagnosticsStackTrace</a>。', '示例：', '另请参阅：'],
 'shallow': ['将节点渲染为多行，省略子节点。', '示例：\n<code>&lt;name&gt;: &lt;description&gt;   &lt;property1&gt;   &lt;property2&gt;   &lt;propertyN&gt;</code>', '另请参阅：'],
 'singleLine': ['将节点渲染为单行，省略子节点。', '示例：\n<code>&lt;name&gt;: &lt;description&gt;(&lt;property1&gt;, &lt;property2&gt;, ..., &lt;propertyN&gt;)</code>', '另请参阅：'],
 'sparse': ['默认的文本树配置。', '示例：', '另请参阅：'],
 'transition': ['在叶节点周围绘制边框的配置。', '供 <a href="painting/TextSpan-class.html">TextSpan</a> 等叶节点使用，以在节点内容周围绘制清晰的边框。', '示例：', '另请参阅：'],
 'whitespace': ['仅使用空白字符、统一将子节点缩进两个空格的配置。', '使用此样式显示具有结构化值的属性，或显示 <a href="foundation/transitionTextConfiguration.html">transitionTextConfiguration</a> 内的子节点，因为在这些情况下使用字符线条样式会分散视觉注意力。', '示例：', '另请参阅：'],
}
for name, texts in data.items():
 d[f'foundation/{name}TextConfiguration.html'] = {str(i): '<p>' + text + '</p>' for i, text in enumerate(texts)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.setdefault('foundation/TextTreeConfiguration-class.html', []).extend([
 {'source': '<li><a href="foundation/sparseTextConfiguration.html">sparseTextConfiguration</a>, which is a typical style.</li>', 'translation': '<li><a href="foundation/sparseTextConfiguration.html">sparseTextConfiguration</a>，一种典型样式。</li>'},
 {'source': '<li><a href="foundation/transitionTextConfiguration.html">transitionTextConfiguration</a>, which is an example of a complex tree style.</li>', 'translation': '<li><a href="foundation/transitionTextConfiguration.html">transitionTextConfiguration</a>，复杂树样式的示例。</li>'},
 {'source': '<li><a href="foundation/DiagnosticsNode/toStringDeep.html">DiagnosticsNode.toStringDeep</a>, for code using <a href="foundation/TextTreeConfiguration-class.html">TextTreeConfiguration</a>\nto render text art for arbitrary trees of <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> objects.</li>', 'translation': '<li><a href="foundation/DiagnosticsNode/toStringDeep.html">DiagnosticsNode.toStringDeep</a>，包含使用 <a href="foundation/TextTreeConfiguration-class.html">TextTreeConfiguration</a> 将任意 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 对象树渲染为字符图的代码。</li>'},
])
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
