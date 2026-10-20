from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
for cls, add, remove, clear, subject in [
 ('AnimationLocalListenersMixin', 'addListener', 'removeListener', 'clearListeners', '值'),
 ('AnimationLocalStatusListenersMixin', 'addStatusListener', 'removeStatusListener', 'clearStatusListeners', '状态'),
]:
 def link(member):
  return f'<a href="animation/{cls}/{member}.html">{member}</a>'
 obj[f'animation/{cls}/{add}.html'] = {
  '0': f'<p>每当动画的{subject}发生变化时调用监听器。</p>',
  '1': f'<p>可以使用 {link(remove)} 移除监听器。</p>',
 }
 obj[f'animation/{cls}/{remove}.html'] = {
  '0': f'<p>停止在动画的{subject}发生变化时调用此监听器。</p>',
  '1': f'<p>可以使用 {link(add)} 添加监听器。</p>',
 }
 obj[f'animation/{cls}/{clear}.html'] = {
  '0': f'<p>移除通过 {link(add)} 添加的所有监听器。</p>',
  '1': '<p>如果使用此 mixin 的类也使用了 <a href="animation/AnimationEagerListenerMixin-mixin.html">AnimationEagerListenerMixin</a>，通常会从该类的 <code>dispose</code> 方法中调用此方法。</p>',
  '2': f'<p>调用此方法不会触发 {link("didUnregisterListener")}。</p>',
 }
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
