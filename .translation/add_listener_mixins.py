from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/AnimationLazyListenerMixin-mixin.html'] = {
 '0': '<p>仅在当前对象已注册监听器时才监听另一个对象的 mixin。</p>',
 '1': '<p>此 mixin 提供 <a href="animation/AnimationLazyListenerMixin/didRegisterListener.html">didRegisterListener</a> 和 <a href="animation/AnimationLazyListenerMixin/didUnregisterListener.html">didUnregisterListener</a> 的实现，因此可与要求这些方法的 <a href="animation/AnimationLocalListenersMixin-mixin.html">AnimationLocalListenersMixin</a> 和 <a href="animation/AnimationLocalStatusListenersMixin-mixin.html">AnimationLocalStatusListenersMixin</a> 配合使用。</p>',
}
obj['animation/AnimationLocalListenersMixin-mixin.html'] = {
 '0': '<p>实现 <a href="animation/AnimationLocalListenersMixin/addListener.html">addListener</a>/<a href="animation/AnimationLocalListenersMixin/removeListener.html">removeListener</a> 协议的 mixin，在调用 <a href="animation/AnimationLocalListenersMixin/notifyListeners.html">notifyListeners</a> 时通知所有已注册的监听器。</p>',
 '1': '<p>此 mixin 要求混入它的类提供 <a href="animation/AnimationLocalListenersMixin/didRegisterListener.html">didRegisterListener</a> 和 <a href="animation/AnimationLocalListenersMixin/didUnregisterListener.html">didUnregisterListener</a> 方法。可以通过混入此库中的另一个 mixin，例如 <a href="animation/AnimationLazyListenerMixin-mixin.html">AnimationLazyListenerMixin</a>，获得这些方法的实现。</p>',
}
obj['animation/AnimationLocalStatusListenersMixin-mixin.html'] = {
 '0': '<p>实现 addStatusListener/removeStatusListener 协议的 mixin，在调用 notifyStatusListeners 时通知所有已注册的监听器。</p>',
 '1': '<p>此 mixin 要求混入它的类提供 <a href="animation/AnimationLocalStatusListenersMixin/didRegisterListener.html">didRegisterListener</a> 和 <a href="animation/AnimationLocalStatusListenersMixin/didUnregisterListener.html">didUnregisterListener</a> 方法。可以通过混入此库中的另一个 mixin，例如 <a href="animation/AnimationLazyListenerMixin-mixin.html">AnimationLazyListenerMixin</a>，获得这些方法的实现。</p>',
}
obj['animation/AnimationEagerListenerMixin-mixin.html'] = {
 '0': '<p>用 dispose 约定替代 <a href="animation/AnimationEagerListenerMixin/didRegisterListener.html">didRegisterListener</a>/<a href="animation/AnimationEagerListenerMixin/didUnregisterListener.html">didUnregisterListener</a> 约定的 mixin。</p>',
 '1': '<p>此 mixin 提供 <a href="animation/AnimationEagerListenerMixin/didRegisterListener.html">didRegisterListener</a> 和 <a href="animation/AnimationEagerListenerMixin/didUnregisterListener.html">didUnregisterListener</a> 的实现，因此可与要求这些方法的 <a href="animation/AnimationLocalListenersMixin-mixin.html">AnimationLocalListenersMixin</a> 和 <a href="animation/AnimationLocalStatusListenersMixin-mixin.html">AnimationLocalStatusListenersMixin</a> 配合使用。</p>',
}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
