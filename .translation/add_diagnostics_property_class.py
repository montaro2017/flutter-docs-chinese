from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsProperty-class.html'] = {
 '0': '<p>具有 <code>T</code> 类型的 <a href="foundation/DiagnosticsProperty/value.html">value</a> 的属性。</p>',
 '1': '<p>如果默认的 <code>value.toString()</code> 无法充分描述该值，请指定 <code>description</code> 以定义自定义描述。</p>',
 '2': '<p><a href="foundation/DiagnosticsNode/showSeparator.html">showSeparator</a> 属性指示是否应在属性的 <a href="foundation/DiagnosticsNode/name.html">name</a> 与其 <a href="foundation/DiagnosticsProperty/value.html">value</a> 之间放置分隔符。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1)+'\n',encoding='utf-8')
