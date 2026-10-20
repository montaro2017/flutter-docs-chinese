from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/StringProperty/quoted.html'] = {'0': '<p>是否将该值用双引号包裹。</p>'}
d['foundation/StringProperty/valueToString.html'] = {i: text.replace('foundation/IntProperty/valueToString.html', 'foundation/StringProperty/valueToString.html') for i, text in d['foundation/IntProperty/valueToString.html'].items()}
d['foundation/StringProperty/toJsonMap.html'] = dict(d['foundation/FlagsSummary/toJsonMap.html'])
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
