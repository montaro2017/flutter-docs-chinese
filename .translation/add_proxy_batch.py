from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'animation/ProxyAnimation-class.html': {
  '0': '<p>代理另一个动画的动画。</p>',
  '1': '<p>代理动画的用途在于可以更换父动画。例如，一个对象可以创建代理动画并将其交给另一个对象，随后再更换代理动画获取值的来源动画。</p>',
 },
 'animation/ProxyAnimation/ProxyAnimation.html': {
  '0': '<p>创建代理动画。</p>',
  '1': '<p>如果省略 animation 参数，代理动画的状态将为 <a href="animation/AnimationStatus.html">AnimationStatus.dismissed</a>，值为 0.0。</p>',
 },
 'animation/ProxyAnimation/parent.html': {
  '0': '<p>此动画所代理的值的来源动画。</p>',
  '1': '<p>此值可以修改。修改时，代理动画上的监听器会自动更新为监听新的父动画。</p>',
 },
 'animation/ProxyAnimation/value.html': {'0': '<p>动画的当前值。</p>'},
 'animation/ProxyAnimation/status.html': {'0': '<p>此动画的当前状态。</p>'},
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
path = data / 'shared-text.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({'Creates a proxy animation.': '创建代理动画。', 'The animation whose value this animation will proxy.': '此动画所代理的值的来源动画。'})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
