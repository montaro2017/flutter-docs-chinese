from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/ComputeCallback.html'] = {
 '0': '<p>传给 <a href="foundation/compute.html">compute</a> 的回调签名。</p>',
 '1': '<p><code>callback</code>、传给它的 <code>message</code> 以及返回结果，都必须是可在 isolate 之间发送的对象，因为必要时可能会连同它们间接引用的对象一起复制。大多数对象都可以在 isolate 之间发送。</p>',
 '2': '<p>有关例外情况，以及发送闭包时可能捕获超出所需范围的状态的注意事项，请参阅 <a href="dart-isolate/SendPort/send.html">SendPort.send</a>。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
