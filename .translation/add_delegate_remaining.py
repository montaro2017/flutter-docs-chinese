from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'additionalNodeProperties': ['<p>返回包含额外信息的可序列化映射，这些信息将包含在给定 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 的序列化结果中。</p>', '<p>对于序列化结果中包含的每个 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a>，都会调用此方法。</p>'],
 'copyWith': ['<p>使用提供的值创建此 <a href="foundation/DiagnosticsSerializationDelegate-class.html">DiagnosticsSerializationDelegate</a> 的副本。</p>'],
 'delegateForNode': ['<p>返回将给定 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 加入序列化结果时使用的 <a href="foundation/DiagnosticsSerializationDelegate-class.html">DiagnosticsSerializationDelegate</a>。</p>', '<p>默认返回此委托的副本，其 <a href="foundation/DiagnosticsSerializationDelegate/subtreeDepth.html">subtreeDepth</a> 减少一。</p>', '<p>对于将作为另一个节点的属性或子节点加入序列化结果的节点，会调用此方法。如果无需更改委托，可以返回同一个委托。</p>'],
 'truncateNodesList': ['<p>截断给定的 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 列表，该列表将作为 <code>owner</code> 节点的子节点或属性加入序列化结果。</p>', '<p>此方法必须返回所提供节点的子集，不得替换任何节点。<a href="foundation/DiagnosticsSerializationDelegate/filterProperties.html">filterProperties</a> 和 <a href="foundation/DiagnosticsSerializationDelegate/filterChildren.html">filterChildren</a> 会将节点完全从序列化结果中隐藏，而截断节点会在序列化结果中留下提示，说明结果中还有未包含在当前序列化结果中的节点。</p>', '<p>默认原样返回 <code>nodes</code>。</p>'],
 'DiagnosticsSerializationDelegate': ['<p>创建一个简单的 <a href="foundation/DiagnosticsSerializationDelegate-class.html">DiagnosticsSerializationDelegate</a>，用于控制 <code>subtreeDepth</code> 以及是否 <code>includeProperties</code>。</p>', '<p>如需额外的配置选项，请扩展 <a href="foundation/DiagnosticsSerializationDelegate-class.html">DiagnosticsSerializationDelegate</a>，并为此类的方法提供自定义实现。</p>'],
}
for member, blocks in pages.items():
 d[f'foundation/DiagnosticsSerializationDelegate/{member}.html'] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
