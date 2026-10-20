from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/IterableProperty-class.html'] = {'0': '<p>具有 <code>Iterable&lt;T&gt;</code> 类型的 <a href="foundation/DiagnosticsProperty/value.html">value</a> 的属性，可使用不同的 <a href="foundation/DiagnosticsTreeStyle.html">DiagnosticsTreeStyle</a> 自定义显示方式。</p>', '1': '<p>如果 <a href="foundation/DiagnosticsNode/style.html">style</a> 为 <a href="foundation/DiagnosticsTreeStyle.html">DiagnosticsTreeStyle.singleLine</a>，则将可迭代对象描述为逗号分隔的列表；否则，将其描述为换行分隔的列表。</p>'}
d['foundation/IterableProperty/IterableProperty.html'] = {'0': '<p>为可迭代对象（例如列表）创建诊断属性。</p>', '1': '<p><code>ifEmpty</code> 参数用于指定如何显示包含 0 个元素的可迭代 <code>value</code>。如果 <code>ifEmpty</code> 为 null，表示空的可迭代 <code>value</code> 没有显示价值，类似于使用 <code>defaultValue</code> 表示某个具体值没有显示价值。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
