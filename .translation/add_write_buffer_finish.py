from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/WriteBuffer/WriteBuffer.html': {
 '0': '<p>创建用于逐步构建 <a href="dart-typed_data/ByteData-class.html">ByteData</a> 实例的接口。</p>',
 '1': '<p><code>startCapacity</code> 决定 <a href="foundation/WriteBuffer-class.html">WriteBuffer</a> 的初始容量，单位为字节。该值越接近实际使用的大小，性能越好。</p>',
 },
 'foundation/WriteBuffer/done.html': {'0': '<p>完成写入并返回已写入的 <a href="dart-typed_data/ByteData-class.html">ByteData</a>。</p>'},
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
