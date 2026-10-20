from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsBlock-class.html'] = {'0': '<p>一种 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a>，主要用作其他诊断信息的容器，通常自身没有有意义的值。</p>', '1': '<p>此类通常用于显示复杂的嵌套错误消息。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
