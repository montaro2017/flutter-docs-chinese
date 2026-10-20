from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/ChangeNotifier-class.html'] = {
 '0': '<p>可被继承或作为 mixin 使用的类，提供通过 <a href="dart-ui/VoidCallback.html">VoidCallback</a> 发送通知的变化通知 API。</p>',
 '1': '<p>添加监听器的时间复杂度为 O(1)，移除监听器和派发通知的时间复杂度为 O(N)，其中 N 为监听器数量。</p>',
 '2': '<h2 id="using-changenotifier-subclasses-for-data-models">使用 ChangeNotifier 子类作为数据模型</h2>',
 '3': '<p>数据结构可以继承 <a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a> 或将其作为 mixin 使用，以实现 <a href="foundation/Listenable-class.html">Listenable</a> 接口。这样就能与监听 <a href="foundation/Listenable-class.html">Listenable</a> 变化的 widget（例如 <a href="widgets/ListenableBuilder-class.html">ListenableBuilder</a>）一起使用。</p>',
 '6': '<p>另请参阅：</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/ChangeNotifier-class.html'] = [
 {'source': '<li><a href="foundation/ValueNotifier-class.html">ValueNotifier</a>, which is a <a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a> that wraps a single value.</li>',
 'translation': '<li><a href="foundation/ValueNotifier-class.html">ValueNotifier</a> 是包装单个值的 <a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a>。</li>'},
 {'source': 'The following example implements a simple counter that utilizes a\n<a href="widgets/ListenableBuilder-class.html">ListenableBuilder</a> to limit rebuilds to only the <a href="widgets/Text-class.html">Text</a> widget containing\nthe count. The current count is stored in a <a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a> subclass, which\nrebuilds the <a href="widgets/ListenableBuilder-class.html">ListenableBuilder</a>\'s contents when its value is changed.',
 'translation': '下面的示例实现了一个简单计数器，使用 <a href="widgets/ListenableBuilder-class.html">ListenableBuilder</a>，使重新构建仅发生在显示计数的 <a href="widgets/Text-class.html">Text</a> widget 上。当前计数保存在 <a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a> 子类中；值发生变化时，会重新构建 <a href="widgets/ListenableBuilder-class.html">ListenableBuilder</a> 的内容。'},
 {'source': 'In this case, the <a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a> subclass encapsulates a list, and notifies\nthe clients any time an item is added to the list. This example only supports\nadding items; as an exercise, consider adding buttons to remove items from\nthe list as well.',
 'translation': '在此示例中，<a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a> 子类封装了一个列表，每次向列表添加元素时都会通知使用方。此示例仅支持添加元素；作为练习，可以考虑再添加按钮，用于移除列表中的元素。'},
]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/ChangeNotifier-class.html'] = {
 '3': '<dd>当前是否注册了监听器。<div class="features"><span class="feature">无 setter</span></div></dd>',
 '4': '<dd>注册一个闭包，在对象发生变化时调用。<div class="features"><span class="feature">重写</span></div></dd>',
 '5': '<dd>释放此对象使用的所有资源。</dd>',
 '6': '<dd>调用所有已注册的监听器。</dd>',
 '7': '<dd>从对象变化时通知的闭包列表中移除此前注册的闭包。<div class="features"><span class="feature">重写</span></div></dd>',
 '8': '<dd>供子类断言 <a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a> 尚未被释放。</dd>',
 '9': '<dd>将 <code>object</code> 的创建事件派发给 <a href="foundation/FlutterMemoryAllocations/instance.html">FlutterMemoryAllocations.instance</a>。</dd>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
