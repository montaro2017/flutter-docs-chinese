from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/MessageProperty-class.html'] = {'0': '<p>以属性样式显示的调试消息。</p>', '3': '<p>另请参阅：</p>'}
d['foundation/MessageProperty/MessageProperty.html'] = {'0': '<p>创建一个显示消息的诊断属性。</p>', '1': '<p>消息没有具体的 <a href="foundation/DiagnosticsProperty/value.html">value</a>（因此 <a href="foundation/DiagnosticsProperty/value.html">value</a> 会返回 null）。消息存储在描述中。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/MessageProperty-class.html'] = [
 {'source': 'The following two properties are better expressed using this\n<a href="foundation/MessageProperty-class.html">MessageProperty</a> class, rather than <a href="foundation/StringProperty-class.html">StringProperty</a>, as the intent is to\nshow a message with property style display rather than to describe the value\nof an actual property of the object:', 'translation': '以下两个属性更适合使用 <a href="foundation/MessageProperty-class.html">MessageProperty</a> 类表达，而不是 <a href="foundation/StringProperty-class.html">StringProperty</a>，因为目的是以属性样式显示消息，而不是描述对象某个实际属性的值：'},
 {'source': 'On the other hand, <a href="foundation/StringProperty-class.html">StringProperty</a> is better suited when the property has a\nconcrete value that is a string:', 'translation': '当属性具有具体的字符串值时，则更适合使用 <a href="foundation/StringProperty-class.html">StringProperty</a>：'},
]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
