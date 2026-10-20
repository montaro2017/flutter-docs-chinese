from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
for kind in ['Uint8', 'Int32', 'Int64', 'Float32', 'Float64']:
 d[f'foundation/ReadBuffer/get{kind}List.html'] = {'0': f'<p>从缓冲区读取指定数量的 {kind} 值。</p>'}
d['foundation/ReadBuffer/hasRemaining.html'] = {'0': '<p>缓冲区是否仍有待读取的数据。</p>'}
d['foundation/ReadBuffer/data.html'] = {'0': '<p>正在读取的底层数据。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
