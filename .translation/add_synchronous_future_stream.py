from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/SynchronousFuture/asStream.html'] = {
 '0': '<p>创建一个包含此 future 结果的 <a href="dart-async/Stream-class.html">Stream</a>。</p>',
 '1': '<p>该流会发出一个包含此 future 完成结果的数据事件或错误事件，然后发出 done 事件并关闭。</p>',
 '2': '<p>如果 future 永不完成，该流就不会发出任何事件。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
