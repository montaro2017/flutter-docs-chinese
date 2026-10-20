from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'animation/AnimationWithParentMixin-mixin.html': {
  '0': '<p>通过将行为委托给指定的 <a href="animation/AnimationWithParentMixin/parent.html">parent</a> 动画，实现 <a href="animation/Animation-class.html">Animation</a> 接口的大部分功能。</p>',
  '1': '<p>要实现由父动画驱动的 <a href="animation/Animation-class.html">Animation</a>，只需混入此类，实现 <a href="animation/AnimationWithParentMixin/parent.html">parent</a>，并实现 <code>T get value</code>。</p>',
  '2': '<p>如果要定义从 0..1 范围内的值进行映射的规则，可考虑继承 <a href="animation/Tween-class.html">Tween</a>。</p>',
 },
 'animation/AnimationWithParentMixin/parent.html': {
  '0': '<p>此动画所代理的值的来源动画。</p>',
  '1': '<p>此对象的整个生命周期内，来源动画必须保持不变。如果希望在不同时间代理不同动画，可考虑使用 <a href="animation/ProxyAnimation-class.html">ProxyAnimation</a>。</p>',
 },
 'animation/AnimationWithParentMixin/status.html': {'0': '<p>此动画的当前状态。</p>'},
})
for add, remove, subject in [('addListener','removeListener','值'),('addStatusListener','removeStatusListener','状态')]:
 def link(member):
  return f'<a href="animation/AnimationWithParentMixin/{member}.html">{member}</a>'
 obj[f'animation/AnimationWithParentMixin/{add}.html'] = {'0': f'<p>每当动画的{subject}发生变化时调用监听器。</p>', '1': f'<p>可以使用 {link(remove)} 移除监听器。</p>'}
 obj[f'animation/AnimationWithParentMixin/{remove}.html'] = {'0': f'<p>停止在动画的{subject}发生变化时调用此监听器。</p>', '1': f'<p>可以使用 {link(add)} 添加监听器。</p>'}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
