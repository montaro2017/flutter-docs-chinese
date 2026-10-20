from pathlib import Path
import json
p = Path(__file__).resolve().parent/'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsProperty/toDescription.html']={
 '0':'<p>返回节点自身的简短摘要描述，不包含子节点或属性。</p>',
 '1':'<p><code>parentConfiguration</code> 指定父节点如何渲染为字符图。例如，如果父节点不在属性之间换行，则属性描述也应尽可能保持为单行。</p>',
}
d['foundation/DiagnosticsProperty/getChildren.html']={
 '0':'<p>此 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 的子节点。</p>',
 '1':'<p>另请参阅：</p>',
}
d['foundation/DiagnosticsProperty/getProperties.html']={
 '0':'<p>此 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 的属性。</p>',
 '1':'<p>属性和子节点虽然都是 <a href="dart-core/List-class.html">List&lt;DiagnosticsNode&gt;</a>，但仍保持分离，因为它们应采用不同的分组方式。</p>',
}
p.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
