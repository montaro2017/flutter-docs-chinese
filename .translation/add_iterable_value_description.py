from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/IterableProperty/valueToString.html'] = {i: text.replace('foundation/IntProperty/valueToString.html', 'foundation/IterableProperty/valueToString.html') for i, text in d['foundation/IntProperty/valueToString.html'].items()}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
