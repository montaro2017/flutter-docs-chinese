from pathlib import Path
import json, re
from case_paths import read_source
root = Path(__file__).resolve().parent
p = root / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/Listenable-class.html': {
 '0': '<p>维护监听器列表的对象。</p>',
 '1': '<p>监听器通常用于通知使用方：此对象已更新。</p>',
 '2': '<p>此接口有两种扩展形式：</p>',
 '3': '<p><a href="foundation/ValueListenable-class.html">ValueListenable</a> 接口在 <a href="foundation/Listenable-class.html">Listenable</a> 接口的基础上增加了<em>当前值</em>的概念。</p>',
 '4': '<p><a href="animation/Animation-class.html">Animation</a> 接口在 <a href="foundation/ValueListenable-class.html">ValueListenable</a> 接口的基础上增加了方向（正向或反向）的概念。</p>',
 '5': '<p>Flutter API 中的许多类使用或实现这些接口。以下子类尤其值得关注：</p>',
 '6': '<p>可以继承 <a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a>，或将其作为 mixin 使用，来创建实现 <a href="foundation/Listenable-class.html">Listenable</a> 接口的对象。</p>',
 '7': '<p><a href="foundation/ValueNotifier-class.html">ValueNotifier</a> 实现了 <a href="foundation/ValueListenable-class.html">ValueListenable</a> 接口，提供一个可变的值，并在该值被修改时触发通知。</p>',
 '8': '<p>文档中的“通知使用方”“发送通知”和“触发通知”等表述含义相同。</p>',
 '9': '<p>另请参阅：</p>',
 },
 'foundation/ValueListenable-class.html': {
 '0': '<p>供公开 <a href="foundation/ValueListenable/value.html">value</a> 的 <a href="foundation/Listenable-class.html">Listenable</a> 子类使用的接口。</p>',
 '1': '<p><a href="foundation/ValueNotifier-class.html">ValueNotifier&lt;T&gt;</a> 和 <a href="animation/Animation-class.html">Animation&lt;T&gt;</a> 都实现了此接口，因此其他 API 可以互换地接受这两种实现。</p>',
 '2': '<p>另请参阅：</p>',
 },
 'foundation/Listenable/addListener.html': {'0': '<p>注册一个闭包，在对象通知其监听器时调用。</p>'},
 'foundation/Listenable/removeListener.html': {'0': '<p>从对象通知时调用的闭包列表中移除此前注册的闭包。</p>'},
 'foundation/Listenable/Listenable.html': {'0': '<p>此构造函数使子类能够提供 const 构造函数，从而用于 const 表达式。</p>'},
 'foundation/Listenable/Listenable.merge.html': {
 '0': '<p>返回一个 <a href="foundation/Listenable-class.html">Listenable</a>，当任意给定的 <a href="foundation/Listenable-class.html">Listenable</a> 触发通知时，它也会触发通知。</p>',
 '1': '<p>调用工厂构造函数后，不得向可迭代对象中添加或移除元素，否则会导致内存泄漏或异常。</p>',
 '2': '<p>可迭代对象中可以包含 null，这些值会被忽略。</p>',
 },
 'foundation/ValueListenable/value.html': {
 '0': '<p>对象的当前值。</p>',
 '1': '<p>当值发生变化时，将调用通过 <a href="foundation/Listenable/addListener.html">addListener</a> 注册的回调。</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = root / 'translations-fragments.json'
f = json.loads(p.read_text(encoding='utf-8'))
builder = '<li><a href="widgets/ValueListenableBuilder-class.html">ValueListenableBuilder</a> 是一个 widget，每当 <a href="foundation/ValueListenable-class.html">ValueListenable</a> 对象触发通知时，它都会通过构建回调重新构建，并向该回调提供对象的值。</li>'
texts = {
 'foundation/Listenable-class.html': [
 '<li><a href="widgets/AnimatedBuilder-class.html">AnimatedBuilder</a> 是一个 widget，每当给定的 <a href="foundation/Listenable-class.html">Listenable</a> 触发通知时，它都会通过构建回调重新构建。它通常与 <a href="animation/Animation-class.html">Animation</a> 子类一起使用，因此得名，但它可以用于任何 <a href="foundation/Listenable-class.html">Listenable</a>。它继承自 <a href="widgets/AnimatedWidget-class.html">AnimatedWidget</a>，后者可用于创建由 <a href="foundation/Listenable-class.html">Listenable</a> 驱动的 widget。</li>',
 builder,
 '<li><a href="widgets/InheritedNotifier-class.html">InheritedNotifier</a> 是 widget 的抽象父类，这些 widget 使用 <a href="foundation/Listenable-class.html">Listenable</a> 的通知，并借助 <a href="widgets/InheritedWidget-class.html">InheritedWidget</a> 机制，触发声明依赖于它们的后代 widget 重新构建。</li>',
 '<li><a href="foundation/Listenable/Listenable.merge.html">Listenable.merge</a> 创建一个 <a href="foundation/Listenable-class.html">Listenable</a>，当列表中任意其他 <a href="foundation/Listenable-class.html">Listenable</a> 触发通知时，它也会触发通知。</li>',
 ],
 'foundation/ValueListenable-class.html': [builder],
}
for page, translations in texts.items():
 section = re.search(r'<section class="desc markdown">(.*?)</section>', read_source(page), re.S).group(1)
 source = re.findall(r'<li>.*?</li>', section, re.S)[-len(translations):]
 assert len(source) == len(translations)
 f[page] = [{'source': s, 'translation': t} for s, t in zip(source, translations)]
p.write_text(json.dumps(f, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = root / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/Listenable-class.html'] = {
 '1': '<dd>此构造函数使子类能够提供 const 构造函数，从而用于 const 表达式。<div class="constructor-modifier features">const</div></dd>',
 '2': '<dd>返回一个 <a href="foundation/Listenable-class.html">Listenable</a>，当任意给定的 <a href="foundation/Listenable-class.html">Listenable</a> 触发通知时，它也会触发通知。<div class="constructor-modifier features">factory</div></dd>',
 '3': '<dd>注册一个闭包，在对象通知其监听器时调用。</dd>',
 '4': '<dd>从对象通知时调用的闭包列表中移除此前注册的闭包。</dd>',
}
d['foundation/ValueListenable-class.html'] = {
 '2': '<dd>此构造函数使子类能够提供 const 构造函数，从而用于 const 表达式。<div class="constructor-modifier features">const</div></dd>',
 '3': '<dd>对象的当前值。<div class="features"><span class="feature">无 setter</span></div></dd>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

