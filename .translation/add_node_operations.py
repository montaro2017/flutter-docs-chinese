from pathlib import Path
import json
path = Path(__file__).resolve().parent / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'foundation/AbstractNode/parent.html': {'0': '<p>此节点在树中的父节点。</p>'},
 'foundation/AbstractNode/adoptChild.html': {'0': '<p>将给定节点标记为此节点的子节点。</p>', '1': '<p>子类获得新的子节点时应调用此函数。</p>'},
 'foundation/AbstractNode/dropChild.html': {'0': '<p>断开给定节点与此节点的连接。</p>', '1': '<p>子类移除子节点时应调用此函数。</p>'},
 'foundation/AbstractNode/attach.html': {
  '0': '<p>将此节点标记为已附着到给定所有者。</p>',
  '1': '<p>通常仅从 <a href="foundation/AbstractNode/parent.html">parent</a> 的 <a href="foundation/AbstractNode/attach.html">attach</a> 方法调用，或由 <code>owner</code> 调用，以将树的根节点标记为已附着。</p>',
  '2': '<p>具有子节点的子类应重写此方法，先调用继承的方法（例如 <code>super.attach(owner)</code>），再将所有子节点 <a href="foundation/AbstractNode/attach.html">attach</a> 到同一个 <code>owner</code>。</p>',
 },
 'foundation/AbstractNode/detach.html': {
  '0': '<p>将此节点标记为已分离。</p>',
  '1': '<p>通常仅从 <a href="foundation/AbstractNode/parent.html">parent</a> 的 <a href="foundation/AbstractNode/detach.html">detach</a> 方法调用，或由 <a href="foundation/AbstractNode/owner.html">owner</a> 调用，以将树的根节点标记为已分离。</p>',
  '2': '<p>具有子节点的子类应重写此方法，先调用继承的方法（例如 <code>super.detach()</code>），再对所有子节点调用 <a href="foundation/AbstractNode/detach.html">detach</a>。</p>',
 },
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
