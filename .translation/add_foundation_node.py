from pathlib import Path
import json
path = Path(__file__).resolve().parent / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'foundation/AbstractNode/depth.html': {
  '0': '<p>此节点在树中的深度。</p>',
  '1': '<p>沿树向下遍历时，节点深度单调递增。</p>',
 },
 'foundation/AbstractNode/attached.html': {
  '0': '<p>此节点所在树的根节点是否已附着到某个对象。</p>',
  '1': '<p>调用 <a href="foundation/AbstractNode/attach.html">attach</a> 时，此值变为 true。</p>',
  '2': '<p>调用 <a href="foundation/AbstractNode/detach.html">detach</a> 时，此值变为 false。</p>',
 },
 'foundation/AbstractNode/owner.html': {
  '0': '<p>此节点的所有者（未附着时为 null）。</p>',
  '1': '<p>此节点所属的整个子树具有相同的所有者。</p>',
 },
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
