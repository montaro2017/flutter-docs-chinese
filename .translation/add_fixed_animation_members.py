from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'animation/ReverseAnimation/ReverseAnimation.html': {'0': '<p>创建反向动画。</p>'},
 'animation/ReverseAnimation/parent.html': {'0': '<p>此动画所反转的值和方向的来源动画。</p>'},
 'animation/AlwaysStoppedAnimation/AlwaysStoppedAnimation.html': {
  '0': '<p>使用给定值创建 <a href="animation/AlwaysStoppedAnimation-class.html">AlwaysStoppedAnimation</a>。</p>',
  '1': '<p>由于 <a href="animation/AlwaysStoppedAnimation-class.html">AlwaysStoppedAnimation</a> 的 <code>value</code> 和 <a href="animation/AlwaysStoppedAnimation/status.html">status</a> 永远不会改变，监听器也永远不会被调用。因此，可以安全地在多个位置复用同一个 <a href="animation/AlwaysStoppedAnimation-class.html">AlwaysStoppedAnimation</a> 实例。如果要使用的 <code>value</code> 在编译时已知，应以 <code>const</code> 构造函数的方式调用此构造函数。</p>',
 },
})
for cls in ['ReverseAnimation', 'AlwaysStoppedAnimation']:
 obj[f'animation/{cls}/value.html'] = {'0': '<p>动画的当前值。</p>'}
 obj[f'animation/{cls}/status.html'] = {'0': '<p>此动画的当前状态。</p>'}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
