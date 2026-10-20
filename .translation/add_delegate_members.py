from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'subtreeDepth': ['<p>控制序列化的 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 层次结构中包含多少层子节点。</p>', '<p>默认为零。</p>', '<p>另请参阅：</p>'],
 'includeProperties': ['<p>序列化时是否包含 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 的属性。</p>', '<p>默认为 false。</p>', '<p>另请参阅：</p>'],
 'expandPropertyValues': ['<p>是否展开以 <a href="foundation/Diagnosticable-mixin.html">Diagnosticable</a> 为值的属性。</p>'],
 'filterChildren': ['<p>筛选将作为给定 <code>owner</code> 节点的子节点包含的 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 列表。</p>', '<p>此回调可以返回所提供列表中子节点的子集，也可以用新的子节点替换整个列表。</p>', '<p>另请参阅：</p>'],
 'filterProperties': ['<p>筛选将作为给定 <code>owner</code> 节点的属性包含的 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 列表。</p>', '<p>此回调可以返回所提供列表中属性的子集，也可以用新的属性节点替换整个列表。</p>', '<p>默认原样返回 <code>nodes</code>。</p>', '<p>另请参阅：</p>'],
}
for member, blocks in pages.items():
 d[f'foundation/DiagnosticsSerializationDelegate/{member}.html'] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
