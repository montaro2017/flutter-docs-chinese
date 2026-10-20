from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/consolidateHttpClientResponseBytes.html'] = {
 '0': '<p>高效地将 <a href="foundation/HttpClientResponse-class.html">HttpClientResponse</a> 的响应体转换为 <a href="dart-typed_data/Uint8List-class.html">Uint8List</a>。</p>',
 '1': '<p>返回的 future 会转发 <code>response</code> 发出的任何错误。</p>',
 '2': '<p>如果指定了 <code>onBytesReceived</code> 回调，在合并响应字节的过程中，每收到一个字节块都会调用它。如果回调抛出错误，将停止处理响应，返回的 future 会以回调抛出的错误完成。有关如何理解回调参数的更多信息，请参阅 <a href="foundation/BytesReceivedCallback.html">BytesReceivedCallback</a> 的文档。</p>',
 '3': '<p>如果 <code>response</code> 使用 gzip 压缩，且 <code>autoUncompress</code> 参数为 true，那么只要尚未通过 <a href="dart-io/HttpClient/autoUncompress.html">HttpClient.autoUncompress</a> 解压，此方法就会自动解压返回列表中的字节。要从此方法获取压缩后的字节（假定响应发送的是压缩字节），请将 <a href="dart-io/HttpClient/autoUncompress.html">HttpClient.autoUncompress</a> 和 <code>autoUncompress</code> 参数都设为 false。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
