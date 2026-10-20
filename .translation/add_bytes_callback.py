from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/BytesReceivedCallback.html'] = {
 '0': '<p>将 <a href="foundation/HttpClientResponse-class.html">HttpClientResponse</a> 的字节合并为 <a href="dart-typed_data/Uint8List-class.html">Uint8List</a> 时，每收到一个字节块便获得通知的回调签名。</p>',
 '1': '<p><code>cumulative</code> 参数包含截至当前已接收的字节总数。如果响应经过 gzip 压缩，此数值表示<em>通过网络传输</em>接收到的压缩字节数。</p>',
 '2': '<p><code>total</code> 参数包含<em>预计</em>通过网络接收的字节总数，该值取自 HTTP 响应头 <code>Content-Length</code>；如果无法预先获知响应体大小，则为 null。这在 HTTP 分块传输编码中很常见；当服务器向客户端返回大量数据，且只有请求处理完毕后才能确定响应总大小时，通常会使用这种编码。</p>',
 '3': '<p>此回调用于 <a href="foundation/consolidateHttpClientResponseBytes.html">consolidateHttpClientResponseBytes</a>。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
