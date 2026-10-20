from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
v = d.setdefault('foundation/DiagnosticableTreeMixin-mixin.html', {})
flag = '<div class="features"><span class="feature">重写</span></div>'
for target, page, source in [(2, 'foundation/DiagnosticableTree-class.html', 3), (3, 'foundation/Diagnosticable-mixin.html', 1), (4, 'foundation/DiagnosticableTree-class.html', 4), (5, 'foundation/Diagnosticable-mixin.html', 3), (6, 'foundation/DiagnosticableTree-class.html', 5), (7, 'foundation/DiagnosticableTree-class.html', 6), (8, 'foundation/DiagnosticableTree-class.html', 7)]:
 text = d[page][str(source)]
 if flag not in text:
  text = text.replace('</dd>', flag + '</dd>')
 v[str(target)] = text
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
