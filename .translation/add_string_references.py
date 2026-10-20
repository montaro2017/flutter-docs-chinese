from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/StringProperty-class.html'] = [{'source': '<li><a href="foundation/MessageProperty-class.html">MessageProperty</a>, which is a better fit for showing a message\ninstead of describing a property with a string value.</li>', 'translation': '<li><a href="foundation/MessageProperty-class.html">MessageProperty</a>，更适合显示消息，而非描述具有字符串值的属性。</li>'}]
d['foundation/StringProperty/toJsonMap.html'] = list(d['foundation/FlagsSummary/toJsonMap.html'])
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
