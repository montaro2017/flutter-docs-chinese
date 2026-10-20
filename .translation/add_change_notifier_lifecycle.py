from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/ChangeNotifier/dispose.html': {
 '0': '<p>释放此对象使用的所有资源。</p>',
 '1': '<p>调用此方法后，对象将不再可用，应将其丢弃（对象释放后调用 <a href="foundation/ChangeNotifier/addListener.html">addListener</a> 会抛出异常）。</p>',
 '2': '<p>只有对象的所有者才应调用此方法。</p>',
 '3': '<p>此方法不会通知监听器，并会在调用时清空监听器列表。此类的使用方必须自行决定是否在释放对象前立即通知监听器。</p>',
 },
 'foundation/ChangeNotifier/notifyListeners.html': {
 '0': '<p>调用所有已注册的监听器。</p>',
 '1': '<p>每当对象发生变化时调用此方法，通知使用方对象可能已改变。在此次遍历期间添加的监听器不会被调用；在此次遍历期间移除的监听器，在移除后不会再被调用。</p>',
 '2': '<p>监听器抛出的异常会被捕获，并通过 <a href="foundation/FlutterError/reportError.html">FlutterError.reportError</a> 报告。</p>',
 '3': '<p>调用 <a href="foundation/ChangeNotifier/dispose.html">dispose</a> 后，不得再调用此方法。</p>',
 '4': '<p>如果在重入调用中移除一个注册了多次的监听器（例如在响应通知时移除），可能会出现意外行为。参见 <a href="foundation/ChangeNotifier/removeListener.html">removeListener</a> 中的说明。</p>',
 },
 'foundation/ChangeNotifier/hasListeners.html': {
 '0': '<p>当前是否注册了监听器。</p>',
 '1': '<p>使用方的行为不应依赖此值，因为如果一个监听器的逻辑会因另一个监听器开始或停止监听而改变，就会产生极难追踪的错误。不过，子类可以利用此信息决定在没有监听器时是否继续执行某些工作；例如，添加监听器时恢复 <a href="dart-async/Stream-class.html">Stream</a>，移除监听器时将其暂停。</p>',
 '2': '<p>通常可以重写 <a href="foundation/ChangeNotifier/addListener.html">addListener</a>，在调用 <code>super.addListener()</code> 之前检查 <a href="foundation/ChangeNotifier/hasListeners.html">hasListeners</a> 是否为 false；如果是，则开始执行判断何时调用 <a href="foundation/ChangeNotifier/notifyListeners.html">notifyListeners</a> 所需的工作。同样，重写 <a href="foundation/ChangeNotifier/removeListener.html">removeListener</a>，在调用 <code>super.removeListener()</code> 之后检查 <a href="foundation/ChangeNotifier/hasListeners.html">hasListeners</a> 是否为 false；如果是，则停止这些工作。</p>',
 '3': '<p>调用 <a href="foundation/ChangeNotifier/dispose.html">dispose</a> 后，此方法返回 false。</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
