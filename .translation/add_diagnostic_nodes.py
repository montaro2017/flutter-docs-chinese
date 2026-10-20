from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'DiagnosticableNode-class.html': ['<p>一种 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a>，通过惰性调用关联的 <a href="foundation/Diagnosticable-mixin.html">Diagnosticable</a> 类型的 <a href="foundation/DiagnosticableNode/value.html">value</a>，实现 <a href="foundation/DiagnosticableNode/getChildren.html">getChildren</a> 和 <a href="foundation/DiagnosticableNode/getProperties.html">getProperties</a>。</p>'],
 'DiagnosticableTreeNode-class.html': ['<p>用于 <a href="foundation/DiagnosticableTree-class.html">DiagnosticableTree</a> 实例的 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a>。</p>'],
 'DiagnosticableNode/DiagnosticableNode.html': ['<p>创建描述 <a href="foundation/Diagnosticable-mixin.html">Diagnosticable</a> 值的诊断信息。</p>'],
 'DiagnosticableNode/builder.html': ['<p>获取当前节点的 <a href="foundation/DiagnosticPropertiesBuilder-class.html">DiagnosticPropertiesBuilder</a>。</p>', '<p>结果会被缓存，以避免重复操作。</p>'],
 'DiagnosticableNode/emptyBodyDescription.html': ['<p>节点没有显示的属性或子节点时，要显示的描述。</p>'],
 'DiagnosticableNode/style.html': ['<p>关于如何显示此节点的提示。</p>'],
 'DiagnosticableTreeNode/DiagnosticableTreeNode.html': ['<p>创建一个 <a href="foundation/DiagnosticableTreeNode-class.html">DiagnosticableTreeNode</a>。</p>'],
 'DiagnosticableTreeNode/getChildren.html': ['<p>此 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 的子节点。</p>', '<p>另请参阅：</p>'],
}
for page, blocks in pages.items():
 d['foundation/' + page] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
