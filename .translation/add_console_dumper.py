from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/ErrorToConsoleDumper-class.html'] = {'0': '<p>将错误消息输出到控制台。</p>'}
d['foundation/ErrorToConsoleDumper/addWebDumpListener.html'] = {'0': '<p>添加一个监听器，用于捕获 Web 上输出的错误消息。</p>'}
d['foundation/ErrorToConsoleDumper/clearWebDumpListeners.html'] = {'0': '<p>清除所有用于捕获 Web 上输出的错误消息的监听器。</p>'}
d['foundation/ErrorToConsoleDumper/dump.html'] = {'0': '<p>将给定的错误 <code>message</code> 输出到控制台。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
