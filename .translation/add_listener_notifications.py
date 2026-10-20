from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
for cls, add, remove, notify, kind in [
 ('AnimationLocalListenersMixin', 'addListener', 'removeListener', 'notifyListeners', '监听器'),
 ('AnimationLocalStatusListenersMixin', 'addStatusListener', 'removeStatusListener', 'notifyStatusListeners', '状态监听器'),
]:
 def link(member):
  return f'<a href="animation/{cls}/{member}.html">{member}</a>'
 obj[f'animation/{cls}/{notify}.html'] = {
  '0': f'<p>调用所有{kind}。</p>',
  '1': '<p>如果在此函数执行期间添加或移除监听器，这些修改不会改变本次遍历中调用的监听器集合。</p>',
 }
 obj[f'animation/{cls}/didRegisterListener.html'] = {
  '0': f'<p>在通过 {link(add)} 添加{kind}之前立即调用。</p>',
  '1': f'<p>调用此方法时，正在注册的监听器尚未接收 {link(notify)} 的通知。</p>',
 }
 obj[f'animation/{cls}/didUnregisterListener.html'] = {
  '0': f'<p>在通过 {link(remove)} 移除{kind}之后立即调用。</p>',
  '1': f'<p>调用此方法时，被移除的监听器已不再接收 {link(notify)} 的通知。</p>',
 }
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
