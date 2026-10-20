from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
for kind in ['Uint8', 'Uint16', 'Uint32', 'Int32', 'Int64', 'Float64']:
 d[f'foundation/ReadBuffer/get{kind}.html'] = {'0': f'<p>从缓冲区读取一个 {kind}。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
