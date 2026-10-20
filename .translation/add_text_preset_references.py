from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
for name, style in [('dashed', 'offstage'), ('dense', 'dense'), ('errorProperty', 'errorProperty'), ('error', 'error'), ('flat', 'flat'), ('singleLine', 'singleLine'), ('sparse', 'sparse'), ('transition', 'transition'), ('whitespace', 'whitespace')]:
 a = f'<a href="foundation/DiagnosticsTreeStyle.html">DiagnosticsTreeStyle.{style}</a>'
 suffix = ', uses this style for ASCII art\ndisplay.' if name == 'errorProperty' else ', uses this style for ASCII art display.'
 entry = {'source': '<li>' + a + suffix + '</li>', 'translation': '<li>' + a + '，使用此样式显示 ASCII 字符图。</li>'}
 entries = d.setdefault(f'foundation/{name}TextConfiguration.html', [])
 entries[:] = [x for x in entries if x['source'] != entry['source']]
 entries.append(entry)
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
