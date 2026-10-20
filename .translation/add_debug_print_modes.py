from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/debugPrintSynchronously.html': {
 '0': '<p><a href="rendering/debugPrint.html">debugPrint</a> 的另一种实现，不对输出进行限速。</p>',
 '1': '<p>用于测试。</p>',
 },
 'foundation/debugPrintThrottled.html': {
 '0': '<p>对消息输出进行限速的 <a href="rendering/debugPrint.html">debugPrint</a> 实现。</p>',
 '1': '<p>这可以避免在限制日志输出速率的平台（例如 Android）上丢失消息。</p>',
 '2': '<p>如果 <code>wrapWidth</code> 不为 null，则使用 <a href="foundation/debugWordWrap.html">debugWordWrap</a> 对消息进行换行。</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
