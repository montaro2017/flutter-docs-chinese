from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/ReadBuffer-class.html': {
 '0': '<p>用于从 <a href="dart-typed_data/ByteData-class.html">ByteData</a> 实例中顺序读取数据的只读缓冲区。</p>',
 '1': '<p>始终使用 <a href="dart-typed_data/Endian/host.html">Endian.host</a> 字节序。</p>',
 },
 'foundation/ReadBuffer/ReadBuffer.html': {'0': '<p>创建一个 <a href="foundation/ReadBuffer-class.html">ReadBuffer</a>，用于读取指定的 <code>data</code>。</p>'},
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
