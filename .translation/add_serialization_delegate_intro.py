from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsSerializationDelegate-class.html'] = {'0': '<p>用于配置如何序列化 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 层次结构的委托。</p>', '1': '<p>在子类中实现此类，即可全面配置 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 的序列化方式。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
