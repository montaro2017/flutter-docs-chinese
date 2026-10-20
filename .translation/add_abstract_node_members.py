from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'adoptChild': ['<p>将给定节点标记为此节点的子节点。</p>', '<p>子类获得新的子节点时，应调用此函数。</p>'],
 'attach': ['<p>将此节点标记为已附着到给定的所有者。</p>', '<p>通常仅由 <a href="foundation/AbstractNode/parent.html">parent</a> 的 <a href="foundation/AbstractNode/attach.html">attach</a> 方法调用，或由 <code>owner</code> 调用以将树的根节点标记为已附着。</p>', '<p>具有子节点的子类应重写此方法，在调用继承的方法（如 <code>super.attach(owner)</code>）后，将所有子节点 <a href="foundation/AbstractNode/attach.html">attach</a> 到同一个 <code>owner</code>。</p>'],
 'attached': ['<p>此节点所在树的根节点是否已附着到某个对象。</p>', '<p>调用 <a href="foundation/AbstractNode/attach.html">attach</a> 时，此值变为 true。</p>', '<p>调用 <a href="foundation/AbstractNode/detach.html">detach</a> 时，此值变为 false。</p>'],
 'depth': ['<p>此节点在树中的深度。</p>', '<p>沿树向下遍历时，节点深度单调递增。</p>'],
 'detach': ['<p>将此节点标记为已分离。</p>', '<p>通常仅由 <a href="foundation/AbstractNode/parent.html">parent</a> 的 <a href="foundation/AbstractNode/detach.html">detach</a> 调用，或由 <a href="foundation/AbstractNode/owner.html">owner</a> 调用以将树的根节点标记为已分离。</p>', '<p>具有子节点的子类应重写此方法，在调用继承的方法（如 <code>super.detach()</code>）后，对所有子节点调用 <a href="foundation/AbstractNode/detach.html">detach</a>。</p>'],
 'dropChild': ['<p>断开给定节点与此节点的连接。</p>', '<p>子类失去一个子节点时，应调用此函数。</p>'],
 'owner': ['<p>此节点的所有者（未附着时为 null）。</p>', '<p>此节点所属的整个子树具有相同的所有者。</p>'],
 'parent': ['<p>此节点在树中的父节点。</p>'],
 'redepthChild': ['<p>调整给定 <code>child</code> 的 <a href="foundation/AbstractNode/depth.html">depth</a>，使其大于此节点自身的 <a href="foundation/AbstractNode/depth.html">depth</a>。</p>', '<p>仅应在重写的 <a href="foundation/AbstractNode/redepthChildren.html">redepthChildren</a> 方法中调用此方法。</p>'],
 'redepthChildren': ['<p>调整此节点的子节点（如果有）的 <a href="foundation/AbstractNode/depth.html">depth</a>。</p>', '<p>具有子节点的子类应重写此方法，并对每个子节点调用 <a href="foundation/AbstractNode/redepthChild.html">redepthChild</a>。不要直接调用此方法。</p>'],
}
for member, blocks in pages.items():
 d[f'foundation/AbstractNode/{member}.html'] = {str(i): b for i, b in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
