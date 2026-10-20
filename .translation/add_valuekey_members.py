from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/ValueKey/operator_equals.html': {
 '0': '<p>相等运算符。</p>',
 '1': '<p>所有 <a href="dart-core/Object-class.html">Object</a> 的默认行为是：当且仅当此对象与 <code>other</code> 是同一个对象时返回 true。</p>',
 '2': '<p>重写此方法可为类指定不同的相等关系。重写后的方法仍必须定义等价关系，即满足以下要求：</p>',
 '3': '<p>全定义性：必须对所有参数返回布尔值，绝不能抛出异常。</p>',
 '4': '<p>自反性：对于所有对象 <code>o</code>，<code>o == o</code> 必须为 true。</p>',
 '5': '<p>对称性：对于所有对象 <code>o1</code> 和 <code>o2</code>，<code>o1 == o2</code> 与 <code>o2 == o1</code> 必须同时为 true 或同时为 false。</p>',
 '6': '<p>传递性：对于所有对象 <code>o1</code>、<code>o2</code> 和 <code>o3</code>，如果 <code>o1 == o2</code> 和 <code>o2 == o3</code> 为 true，则 <code>o1 == o3</code> 必须为 true。</p>',
 '7': '<p>此方法还应随时间保持一致；只有至少一个对象被修改时，两个对象是否相等才应发生变化。</p>',
 '8': '<p>如果子类重写相等运算符，也应重写 <a href="foundation/ValueKey/hashCode.html">hashCode</a> 方法以保持一致。</p>',
 },
 'foundation/ValueKey/toString.html': {
 '0': '<p>此对象的字符串表示。</p>',
 '1': '<p>某些类具有默认的文本表示，通常还配有静态 <code>parse</code> 函数（例如 <a href="dart-core/int/parse.html">int.parse</a>）。这些类会将该文本表示用作字符串表示。</p>',
 '2': '<p>其他类没有程序需要使用的有意义的文本表示。这些类通常会重写 <code>toString</code>，以便在检查对象时提供有用信息，主要用于调试或日志记录。</p>',
 },
 'foundation/ValueKey/hashCode.html': {
 '0': '<p>此对象的哈希码。</p>',
 '1': '<p>哈希码是一个整数，表示对象中会影响 <a href="foundation/ValueKey/operator_equals.html">operator ==</a> 比较的状态。</p>',
 '2': '<p>所有对象都有哈希码。<a href="dart-core/Object-class.html">Object</a> 实现的默认哈希码仅表示对象的身份，正如默认的 <a href="foundation/ValueKey/operator_equals.html">operator ==</a> 实现仅在对象是同一对象时才认为它们相等（参见 <a href="dart-core/identityHashCode.html">identityHashCode</a>）。</p>',
 '3': '<p>如果重写 <a href="foundation/ValueKey/operator_equals.html">operator ==</a>，改为使用对象状态进行比较，则也必须更改哈希码，使其表示该状态；否则，对象无法用于基于哈希的数据结构，例如默认的 <a href="dart-core/Set-class.html">Set</a> 和 <a href="dart-core/Map-class.html">Map</a> 实现。</p>',
 '4': '<p>根据 <a href="foundation/ValueKey/operator_equals.html">operator ==</a> 判断为相等的对象必须具有相同的哈希码。只有对象发生影响相等性的变化时，其哈希码才应改变。哈希码没有其他要求：它们无需在同一程序的不同运行之间保持一致，也不保证任何分布特性。</p>',
 '5': '<p>不相等的对象可以具有相同的哈希码。技术上甚至允许所有实例具有相同的哈希码，但如果冲突过于频繁，可能会降低基于哈希的数据结构的效率，例如 <a href="dart-collection/HashSet-class.html">HashSet</a> 或 <a href="dart-collection/HashMap-class.html">HashMap</a>。</p>',
 '6': '<p>如果子类重写 <a href="foundation/ValueKey/hashCode.html">hashCode</a>，也应重写 <a href="foundation/ValueKey/operator_equals.html">operator ==</a> 运算符以保持一致。</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
