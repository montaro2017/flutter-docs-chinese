from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/AbstractNode-class.html'] = {
 '0': '<p>已弃用；框架不再使用此类，它将在未来的 Flutter 版本中移除。</p>',
 '1': '<p>如有需要，请将此类中所需的功能直接内联到子类中。</p>',
 '2': '<p>树中的抽象节点。</p>',
 '3': '<p>AbstractNode 具有深度、附着状态和父节点的概念，但不定义子节点模型。</p>',
 '4': '<p>当子类更改某个子节点的父节点时，应根据情况调用 <code>parent.adoptChild(child)</code> 或 <code>parent.dropChild(child)</code>。子类可按需公开操作树的 API（例如用于 <code>child</code> 属性的 setter，或用于操作列表的 <code>add()</code> 方法）。</p>',
 '5': '<p>当前父节点通过 <a href="foundation/AbstractNode/parent.html">parent</a> 属性公开。</p>',
 '6': '<p>当前附着状态通过 <a href="foundation/AbstractNode/attached.html">attached</a> 公开。对于任何应视为已附着的树，都应调用 <a href="foundation/AbstractNode/attach.html">attach</a> 手动附着其根节点。除此之外，不应直接调用 <a href="foundation/AbstractNode/attach.html">attach</a> 和 <a href="foundation/AbstractNode/detach.html">detach</a> 方法；附着状态由前述 <a href="foundation/AbstractNode/adoptChild.html">adoptChild</a> 和 <a href="foundation/AbstractNode/dropChild.html">dropChild</a> 方法自动管理。</p>',
 '7': '<p>具有子节点的子类必须按照相关方法文档中的说明，重写 <a href="foundation/AbstractNode/attach.html">attach</a> 和 <a href="foundation/AbstractNode/detach.html">detach</a>。</p>',
 '8': '<p>节点的 <a href="foundation/AbstractNode/depth.html">depth</a> 始终大于其祖先节点的深度，但兄弟节点之间的深度关系没有保证。节点深度用于确保按深度顺序处理节点。子节点的 <a href="foundation/AbstractNode/depth.html">depth</a> 与父节点的 <a href="foundation/AbstractNode/depth.html">depth</a> 之差可以大于 1，因为 <a href="foundation/AbstractNode/depth.html">depth</a> 值从不减小：只要大于父节点即可。考虑一棵具有根节点 A、子节点 B 和孙节点 C 的树。最初，A 的 <a href="foundation/AbstractNode/depth.html">depth</a> 为 0，B 的 <a href="foundation/AbstractNode/depth.html">depth</a> 为 1，C 的 <a href="foundation/AbstractNode/depth.html">depth</a> 为 2。如果将 C 移为 A 的子节点、B 的兄弟节点，这些数值不会改变。C 的 <a href="foundation/AbstractNode/depth.html">depth</a> 仍为 2。<a href="foundation/AbstractNode/depth.html">depth</a> 由 <a href="foundation/AbstractNode/adoptChild.html">adoptChild</a> 和 <a href="foundation/AbstractNode/dropChild.html">dropChild</a> 方法自动维护。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
