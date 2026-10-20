from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'animation/AnimationLazyListenerMixin/didRegisterListener.html': {
  '0': '<p>每当注册监听器使原本为空的监听器列表变为非空时，调用 <a href="animation/AnimationLazyListenerMixin/didStartListening.html">didStartListening</a>。</p>',
  '1': '<p>另请参阅：</p>',
 },
 'animation/AnimationLazyListenerMixin/didUnregisterListener.html': {
  '0': '<p>注销最后一个监听器、使监听器列表变为空时，调用 <a href="animation/AnimationLazyListenerMixin/didStopListening.html">didStopListening</a>。</p>',
  '1': '<p>另请参阅：</p>',
 },
 'animation/AnimationLazyListenerMixin/didStartListening.html': {'0': '<p>监听器数量从零变为一时调用。</p>'},
 'animation/AnimationLazyListenerMixin/didStopListening.html': {'0': '<p>监听器数量从一变为零时调用。</p>'},
 'animation/AnimationLazyListenerMixin/isListening.html': {'0': '<p>是否存在监听器。</p>'},
 'animation/AnimationEagerListenerMixin/didRegisterListener.html': {'0': '<p>此实现忽略监听器的注册。</p>'},
 'animation/AnimationEagerListenerMixin/didUnregisterListener.html': {'0': '<p>此实现忽略监听器的注册。</p>'},
 'animation/AnimationEagerListenerMixin/dispose.html': {'0': '<p>释放此对象使用的资源。调用此方法后，该对象将无法继续使用。</p>'},
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
path = data / 'shared-text.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'Called when the number of listeners changes from zero to one.': '监听器数量从零变为一时调用。',
 'Called when the number of listeners changes from one to zero.': '监听器数量从一变为零时调用。',
 'Whether there are any listeners.': '是否存在监听器。',
 'This implementation ignores listener registrations.': '此实现忽略监听器的注册。',
 'Release the resources used by this object. The object is no longer usable after this method is called.': '释放此对象使用的资源。调用此方法后，该对象将无法继续使用。',
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
