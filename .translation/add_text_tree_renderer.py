from pathlib import Path
import json

r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/TextTreeRenderer-class.html'] = {
 '0': '<p>将 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 对象组成的树渲染为 ASCII 字符图的渲染器。</p>',
 '1': '<p>另请参阅：</p>',
}
d['foundation/TextTreeRenderer/render.html'] = {'0': '<p>将 <code>node</code> 渲染为字符串。</p>'}
d['foundation/TextTreeRenderer/TextTreeRenderer.html'] = {
 '0': '<p>创建一个 <a href="foundation/TextTreeRenderer-class.html">TextTreeRenderer</a> 对象，通过给定参数指定树的渲染方式。</p>',
 '1': '<p>行的换行宽度取 <code>wrapWidth</code> 与当前缩进宽度加上 <code>wrapWidthProperties</code> 个字符这两者中的较大值。这样可以避免在显示很深的树时过度换行，并且只有在树的缩进较小时，才按整体的 <code>wrapWidth</code> 换行。如果指定了 <code>maxDescendentsTruncatableNode</code>，则对于 <code>allowTruncate</code> 设置为 <code>true</code> 的 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 对象，在包含待截断节点的 <code>maxDescendentsTruncatableNode</code> 个后代节点后截断。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/TextTreeRenderer-class.html'] = {
 '0': '<dd>创建一个 <a href="foundation/TextTreeRenderer-class.html">TextTreeRenderer</a> 对象，通过给定参数指定树的渲染方式。</dd>',
 '1': '<dd>将 <code>node</code> 渲染为字符串。</dd>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/TextTreeRenderer-class.html'] = [{
 'source': '<li><a href="foundation/DiagnosticsNode/toStringDeep.html">DiagnosticsNode.toStringDeep</a>, which uses a <a href="foundation/TextTreeRenderer-class.html">TextTreeRenderer</a> to return a\nstring representation of this node and its descendants.</li>',
 'translation': '<li><a href="foundation/DiagnosticsNode/toStringDeep.html">DiagnosticsNode.toStringDeep</a>，使用 <a href="foundation/TextTreeRenderer-class.html">TextTreeRenderer</a> 返回此节点及其后代节点的字符串表示。</li>',
}]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
