from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
v = d.setdefault('foundation/AbstractNode-class.html', {})
for i, text in [(2, '此节点是否位于根节点已附着到某个对象的树中。'), (3, '此节点在树中的深度。'), (4, '此节点的所有者（未附着时为 null）。'), (5, '此节点在树中的父节点。')]:
 v[str(i)] = f'<dd>{text}<div class="features"><span class="feature">无 setter</span></div></dd>'
v.update({
 '6': '<dd>将给定节点标记为此节点的子节点。</dd>',
 '7': '<dd>将此节点标记为已附着到给定的所有者。</dd>',
 '8': '<dd>将此节点标记为已分离。</dd>',
 '9': '<dd>断开给定节点与此节点的连接。</dd>',
 '10': '<dd>调整给定 <code>child</code> 的 <a href="foundation/AbstractNode/depth.html">depth</a>，使其大于此节点自身的 <a href="foundation/AbstractNode/depth.html">depth</a>。</dd>',
 '11': '<dd>调整此节点的子节点（如果存在）的 <a href="foundation/AbstractNode/depth.html">depth</a>。</dd>',
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
