from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/StringProperty-class.html'] = {'0': '<p>将字符串 <a href="foundation/DiagnosticsProperty/value.html">value</a> 用引号包裹的属性。</p>', '1': '<p>另请参阅：</p>'}
d['foundation/StringProperty/StringProperty.html'] = {'0': '<p>创建一个用于字符串的诊断属性。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
