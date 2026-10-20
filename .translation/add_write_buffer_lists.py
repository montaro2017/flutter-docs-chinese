from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
for kind in ['Uint8List', 'Int32List', 'Int64List', 'Float32List', 'Float64List']:
 d[f'foundation/WriteBuffer/put{kind}.html'] = {'0': f'<p>将 <a href="dart-typed_data/{kind}-class.html">{kind}</a> 中的所有值写入缓冲区。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
entries = {
 '0': '<dd>创建用于逐步构建 <a href="dart-typed_data/ByteData-class.html">ByteData</a> 实例的接口。<div class="constructor-modifier features">factory</div></dd>',
 '1': '<dd>完成写入并返回已写入的 <a href="dart-typed_data/ByteData-class.html">ByteData</a>。</dd>',
}
for i, kind in [(2,'Float32List'), (4,'Float64List'), (6,'Int32List'), (8,'Int64List'), (12,'Uint8List')]:
 entries[str(i)] = f'<dd>将 <a href="dart-typed_data/{kind}-class.html">{kind}</a> 中的所有值写入缓冲区。</dd>'
for i, kind in [(3,'Float64'), (5,'Int32'), (7,'Int64'), (9,'Uint16'), (10,'Uint32'), (11,'Uint8')]:
 entries[str(i)] = f'<dd>向缓冲区写入一个 {kind}。</dd>'
d['foundation/WriteBuffer-class.html'] = entries
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
