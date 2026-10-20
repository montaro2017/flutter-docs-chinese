from pathlib import Path
import json
path = Path(__file__).resolve().parent / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'foundation/AbstractNode/redepthChild.html': {
  '0': '<p>调整给定 <code>child</code> 的 <a href="foundation/AbstractNode/depth.html">depth</a>，使其大于此节点自身的 <a href="foundation/AbstractNode/depth.html">depth</a>。</p>',
  '1': '<p>仅应在重写的 <a href="foundation/AbstractNode/redepthChildren.html">redepthChildren</a> 方法中调用此方法。</p>',
 },
 'foundation/AbstractNode/redepthChildren.html': {
  '0': '<p>调整此节点的子节点（如果存在）的 <a href="foundation/AbstractNode/depth.html">depth</a>。</p>',
  '1': '<p>具有子节点的子类应重写此方法，对每个子节点调用 <a href="foundation/AbstractNode/redepthChild.html">redepthChild</a>。不要直接调用此方法。</p>',
 },
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
