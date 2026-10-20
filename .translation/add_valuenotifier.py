from pathlib import Path
import json
root = Path(__file__).resolve().parent
p = root / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/ValueNotifier-class.html': {
 '0': '<p>保存单个值的 <a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a>。</p>',
 '1': '<p>当 <a href="foundation/ValueNotifier/value.html">value</a> 被替换为新值，且相等运算符（<code>==</code>）判定新旧值<strong>不相等</strong>时，此类会通知其监听器。</p>',
 '2': '<h2 id="limitations">限制</h2>',
 '3': '<p>通知的触发依据是<strong>相等性（<code>==</code>）</strong>，而非值内部的变化。因此，对可变对象进行不会影响其相等性的修改，不会通知监听器。</p>',
 '4': '<p>例如，原地修改现有列表的内容时，<code>ValueNotifier&lt;List&lt;int&gt;&gt;</code> 不会通知监听器；只有为 <code>value</code> 属性赋予新值（即 <code>value = newValue</code>），且通过 <code>==</code> 判断新旧值不相等时，才会发送通知。</p>',
 '5': '<p>由于这种行为，<a href="foundation/ValueNotifier-class.html">ValueNotifier</a> 最适合与不可变数据类型一起使用。</p>',
 '6': '<p>对于可变数据类型，可以考虑直接继承 <a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a>，并在发生变化时手动调用 <a href="foundation/ChangeNotifier/notifyListeners.html">notifyListeners</a>。</p>',
 },
 'foundation/ValueNotifier/value.html': {
 '0': '<p>此通知器中保存的当前值。</p>',
 '1': '<p>当值被替换，且相等运算符 == 判定新旧值不相等时，此类会通知其监听器。</p>',
 },
 'foundation/ValueNotifier/ValueNotifier.html': {'0': '<p>创建一个包装此值的 <a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a>。</p>'},
 'foundation/ValueNotifier/toString.html': d['foundation/ValueKey/toString.html'].copy(),
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = root / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/ValueNotifier-class.html'] = {
 '3': '<dd>创建一个包装此值的 <a href="foundation/ChangeNotifier-class.html">ChangeNotifier</a>。</dd>',
 '4': '<dd>此通知器中保存的当前值。<div class="features"><span class="feature">getter/setter 对</span><span class="feature">override-getter</span></div></dd>',
 '5': '<dd>此对象的字符串表示。<div class="features"><span class="feature">重写</span></div></dd>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
