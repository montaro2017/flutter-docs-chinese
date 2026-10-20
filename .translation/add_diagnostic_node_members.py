from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'getChildren': ['<p>此 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 的子节点。</p>', '<p>另请参阅：</p>'],
 'getProperties': ['<p>此 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 的属性。</p>', '<p>虽然属性和子节点的类型都是 <a href="dart-core/List-class.html">List&lt;DiagnosticsNode&gt;</a>，但它们应以不同方式分组，因此需要保持区分。</p>'],
 'toDescription': ['<p>返回对节点自身的简短摘要描述，不包含子节点或属性。</p>', '<p><code>parentConfiguration</code> 指定父节点如何呈现为文本图形。例如，如果父节点的属性之间不换行，那么属性描述也应尽可能保持为单行。</p>'],
 'value': ['<p>此诊断数据所对应的实际对象。</p>'],
}
for member, blocks in pages.items():
 d[f'foundation/DiagnosticableNode/{member}.html'] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
fragment = {'source': '<li><a href="foundation/DiagnosticableNode/getProperties.html">getProperties</a>, which returns the properties of the <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a>\nobject.</li>', 'translation': '<li><a href="foundation/DiagnosticableNode/getProperties.html">getProperties</a>，返回 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 对象的属性。</li>'}
for cls in ('DiagnosticableNode', 'DiagnosticableTreeNode'):
 d[f'foundation/{cls}/getChildren.html'] = [fragment]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
