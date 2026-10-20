from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
common = {
 '3': '<p>如果某个监听器被添加了两次，并在一次遍历期间（例如响应通知时）被移除一次，它仍会再次被调用。反之，如果移除次数与注册次数相同，它就不会再被调用。这种特殊行为源于 <a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a> 无法区分正在移除的是哪个监听器，因为它们完全相同。因此，只要知道仍有注册未被移除，它就会保守地继续调用所有这些监听器。</p>',
 '4': '<p>当在两个不同对象上注册同一个监听器，而这两个对象都将所有注册转发给同一个上游对象时，也可能意外遇到这种行为。</p>',
 '5': '<p>另请参阅：</p>',
}
d['foundation/ChangeNotifier/addListener.html'] = {
 '0': '<p>注册一个闭包，在对象发生变化时调用。</p>',
 '1': '<p>如果给定闭包已经注册，会再添加一次注册；必须移除与添加次数相同的次数，才会停止调用它。</p>',
 '2': '<p>调用 <a href="foundation/ChangeNotifier/dispose.html">dispose</a> 后，不得再调用此方法。</p>',
 **common,
}
d['foundation/ChangeNotifier/removeListener.html'] = {
 '0': '<p>从对象变化时通知的闭包列表中移除此前注册的闭包。</p>',
 '1': '<p>如果给定监听器未注册，则忽略此次调用。</p>',
 '2': '<p>如果已经调用 <a href="foundation/ChangeNotifier/dispose.html">dispose</a>，此方法会立即返回。</p>',
 **common,
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = p.parent / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/ChangeNotifier/addListener.html'] = [{
 'source': '<li><a href="foundation/ChangeNotifier/removeListener.html">removeListener</a>, which removes a previously registered closure from\nthe list of closures that are notified when the object changes.</li>',
 'translation': '<li><a href="foundation/ChangeNotifier/removeListener.html">removeListener</a> 从对象变化时通知的闭包列表中移除此前注册的闭包。</li>',
}]
d['foundation/ChangeNotifier/removeListener.html'] = [{
 'source': '<li><a href="foundation/ChangeNotifier/addListener.html">addListener</a>, which registers a closure to be called when the object\nchanges.</li>',
 'translation': '<li><a href="foundation/ChangeNotifier/addListener.html">addListener</a> 注册一个闭包，在对象发生变化时调用。</li>',
}]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
