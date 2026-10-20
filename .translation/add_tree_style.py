from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsTreeStyle.html'] = {
 '0': '<p>用于显示 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 树中节点的样式。</p>',
 '1': '<p>在发布模式下，这些样式可能被忽略，因为诊断信息会被压缩或截断，以减小二进制文件大小。</p>',
 '2': '<p>另请参阅：</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
v = d.setdefault('foundation/DiagnosticsTreeStyle.html', {})
v.update({
 '2': '<dd><p>不显示树的样式，用于发布模式。</p></dd>',
 '3': '<dd><p>用于显示树的稀疏样式。</p><p>另请参阅：</p><ul><li><a href="rendering/RenderObject-class.html">RenderObject</a>，使用此样式。</li></ul></dd>',
 '4': '<dd><p>用虚线将节点连接到其父节点。</p><p>另请参阅：</p><ul><li><a href="rendering/RenderSliverMultiBoxAdaptor-class.html">RenderSliverMultiBoxAdaptor</a>，使用此样式区分不在显示区域中的子节点与正在显示的子节点。</li></ul></dd>',
 '5': '<dd><p>比 <a href="foundation/DiagnosticsTreeStyle.html">sparse</a> 样式稍紧凑的版本。</p><p>另请参阅：</p><ul><li><a href="widgets/Element-class.html">Element</a>，使用此样式。</li></ul></dd>',
 '6': '<dd><p>支持从一种样式的节点过渡到另一种样式的子节点的样式。</p><p>另请参阅：</p><ul><li><a href="rendering/RenderParagraph-class.html">RenderParagraph</a>，使用此样式显示 <a href="painting/TextSpan-class.html">TextSpan</a> 子节点，使其与 <a href="foundation/DiagnosticsTreeStyle.html">DiagnosticsTreeStyle.sparse</a> 样式的 <a href="rendering/RenderObject-class.html">RenderObject</a> 树兼容。</li></ul></dd>',
 '7': '<dd><p>用于显示错误描述内容的样式。</p><p>另请参阅：</p><ul><li><a href="foundation/FlutterError-class.html">FlutterError</a>，在描述错误的树中，将此样式用于根节点。</li></ul></dd>',
 '8': '<dd><p>仅使用空白字符渲染树，不使用线条连接父子节点。</p><p>另请参阅：</p><ul><li><a href="rendering/SliverGeometry-class.html">SliverGeometry</a>，使用此样式。</li></ul></dd>',
 '9': '<dd><p>渲染树时完全不缩进子节点。</p><p>另请参阅：</p><ul><li><a href="foundation/DiagnosticsStackTrace-class.html">DiagnosticsStackTrace</a>，使用此样式。</li></ul></dd>',
 '10': '<dd><p>将树渲染为单行，不显示子节点。</p></dd>',
 '11': '<dd><p>使用适合错误消息中属性的样式渲染树。</p><p>名称单独占一行，值和属性放在下一行。</p><p>另请参阅：</p><ul><li><a href="foundation/DiagnosticsTreeStyle.html">singleLine</a>，显示相同的信息，但将属性和值保留在同一行。</li></ul></dd>',
 '12': '<dd><p>仅渲染节点的直接属性，而不是整棵树。</p><p>另请参阅：</p><ul><li><a href="rendering/DebugOverflowIndicatorMixin-mixin.html">DebugOverflowIndicatorMixin</a>，使用此样式仅显示节点的直接子节点。</li></ul></dd>',
 '13': '<dd><p>仅渲染节点的子节点，在树变得过大之前截断。</p></dd>',
 '15': '<dd>按声明顺序包含此枚举所有值的常量列表。</dd>',
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.setdefault('foundation/DiagnosticsTreeStyle.html', []).append({
 'source': '<li><a href="foundation/DiagnosticsNode/toStringDeep.html">DiagnosticsNode.toStringDeep</a>, which dumps text art trees for these\nstyles.</li>',
 'translation': '<li><a href="foundation/DiagnosticsNode/toStringDeep.html">DiagnosticsNode.toStringDeep</a>，按这些样式输出字符图形式的树。</li>',
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
