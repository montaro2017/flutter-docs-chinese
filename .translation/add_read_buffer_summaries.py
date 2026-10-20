from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
entries = {
 '0': '<dd>创建一个 <a href="foundation/ReadBuffer-class.html">ReadBuffer</a>，用于读取指定的 <code>data</code>。</dd>',
 '1': '<dd>正在读取的底层数据。<div class="features"><span class="feature">final</span></div></dd>',
 '2': '<dd>缓冲区是否仍有待读取的数据。<div class="features"><span class="feature">无 setter</span></div></dd>',
}
for i, kind in [(3,'Float32'), (5,'Float64'), (7,'Int32'), (9,'Int64'), (13,'Uint8')]:
 entries[str(i)] = f'<dd>从缓冲区读取指定数量的 {kind} 值。</dd>'
for i, kind in [(4,'Float64'), (6,'Int32'), (8,'Int64'), (10,'Uint16'), (11,'Uint32'), (12,'Uint8')]:
 entries[str(i)] = f'<dd>从缓冲区读取一个 {kind}。</dd>'
d['foundation/ReadBuffer-class.html'] = entries
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
