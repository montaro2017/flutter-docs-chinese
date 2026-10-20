from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/MessageProperty-class.html'
entries = d.get(page, [])
pairs = [
 ('<li><a href="foundation/DiagnosticsNode/DiagnosticsNode.message.html">DiagnosticsNode.message</a>, which serves the same role for messages\nwithout a clear property name.</li>', '<li><a href="foundation/DiagnosticsNode/DiagnosticsNode.message.html">DiagnosticsNode.message</a>，为没有明确属性名称的消息提供相同功能。</li>'),
 ('<li><a href="foundation/StringProperty-class.html">StringProperty</a>, which is a better fit for properties with string values.</li>', '<li><a href="foundation/StringProperty-class.html">StringProperty</a>，更适合具有字符串值的属性。</li>'),
]
for source, translation in pairs:
 assert source in read_source(page)
 entries = [e for e in entries if e['source'] != source]
 entries.append({'source': source, 'translation': translation})
d[page] = entries
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
d[page] = {'1': blocks[1].replace('Create a diagnostics property that displays a message.', '创建一个显示消息的诊断属性。')}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
