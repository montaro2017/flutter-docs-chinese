from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
common = '<p>字符串调试表示由中间的 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 表示生成。<a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 表示也供调试工具使用，用于显示对象及属性的交互式树。</p>'
d['foundation/DiagnosticableTree-class.html'] = {'0': '<p>一个基类，提供描述对象属性和子节点的字符串及 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 调试表示。</p>', '1': common, '2': '<p>另请参阅：</p>'}
d['foundation/Diagnosticable-mixin.html'] = {'0': '<p>一个混入类，提供描述对象属性的字符串及 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 调试表示。</p>', '1': common, '2': '<p>另请参阅：</p>'}
d['foundation/DiagnosticableTreeMixin-mixin.html'] = {'0': '<p>帮助输出树的字符串及 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 表示的混入。</p>', '1': '<p>此混入与 <a href="foundation/DiagnosticableTree-class.html">DiagnosticableTree</a> 类相同。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticableTree-class.html'] = [
 {'source': '<li><a href="foundation/DiagnosticableTreeMixin-mixin.html">DiagnosticableTreeMixin</a>, a mixin that implements this class.</li>', 'translation': '<li><a href="foundation/DiagnosticableTreeMixin-mixin.html">DiagnosticableTreeMixin</a>，实现此类的混入。</li>'},
 {'source': '<li><a href="foundation/Diagnosticable-mixin.html">Diagnosticable</a>, which should be used instead of this class to\nprovide diagnostics for objects without children.</li>', 'translation': '<li><a href="foundation/Diagnosticable-mixin.html">Diagnosticable</a>，为没有子节点的对象提供诊断信息时，应使用它。</li>'},
]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
