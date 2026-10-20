from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsBlock/DiagnosticsBlock.html'] = {'0': '<p>创建一个诊断，其属性由 <code>properties</code> 指定，子节点由 <code>children</code> 指定。</p>'}
for member in ('getChildren', 'getProperties', 'value'):
 d[f'foundation/DiagnosticsBlock/{member}.html'] = dict(d[f'foundation/DiagnosticableNode/{member}.html'])
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
