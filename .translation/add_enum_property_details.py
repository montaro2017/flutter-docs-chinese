from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/EnumProperty/valueToString.html'] = {i: text.replace('foundation/IntProperty/valueToString.html', 'foundation/EnumProperty/valueToString.html') for i, text in d['foundation/IntProperty/valueToString.html'].items()}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/EnumProperty-class.html'] = [{'source': '<li><a href="foundation/DiagnosticsProperty-class.html">DiagnosticsProperty</a> which documents named parameters common to all\n<a href="foundation/DiagnosticsProperty-class.html">DiagnosticsProperty</a>.</li>', 'translation': '<li><a href="foundation/DiagnosticsProperty-class.html">DiagnosticsProperty</a>，其文档介绍了所有 <a href="foundation/DiagnosticsProperty-class.html">DiagnosticsProperty</a> 共用的命名参数。</li>'}]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
