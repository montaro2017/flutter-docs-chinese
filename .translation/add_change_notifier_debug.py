from pathlib import Path
import json
root = Path(__file__).resolve().parent
p = root / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/ChangeNotifier/debugAssertNotDisposed.html': {
 '0': '<p>供子类断言 <a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a> 尚未被释放。</p>',
 },
 'foundation/ChangeNotifier/maybeDispatchObjectCreation.html': {
 '0': '<p>将 <code>object</code> 的创建事件派发给 <a href="foundation/FlutterMemoryAllocations/instance.html">FlutterMemoryAllocations.instance</a>。</p>',
 '1': '<p>如果事件已经派发，或 <a href="foundation/kFlutterMemoryAllocationsEnabled-constant.html">kFlutterMemoryAllocationsEnabled</a> 为 false，此方法不执行任何操作。</p>',
 '2': '<p>leak_tracker 等工具会在对象创建事件发生时获取堆栈跟踪，帮助开发者识别对象的所有者，以便排查问题。</p>',
 '3': '<p>但由于 <a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a> 是 mixin，它没有自己的构造函数。因此，它会在首次调用 <code>addListener</code> 时报告对象创建事件，导致堆栈跟踪指向 <code>addListener</code>，而非构造函数。</p>',
 '4': '<p>为了便于调试，请在类的构造函数中调用 <a href="foundation/ChangeNotifier/maybeDispatchObjectCreation.html">ChangeNotifier.maybeDispatchObjectCreation</a>。这有助于识别对象的所有者。</p>',
 '5': '<p>请务必使用条件 <code>if (kFlutterMemoryAllocationsEnabled) ...</code> 进行调用，以便在该标志为 false 时，通过 tree shaking 移除此方法。</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = root / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/ChangeNotifier/debugAssertNotDisposed.html'] = [{
 'source': 'The <a href="foundation/ChangeNotifier/debugAssertNotDisposed.html">debugAssertNotDisposed</a> function should only be called inside of an\nassert, as in this example.',
 'translation': '<a href="foundation/ChangeNotifier/debugAssertNotDisposed.html">debugAssertNotDisposed</a> 函数只能在 assert 中调用，如本例所示。',
}]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
