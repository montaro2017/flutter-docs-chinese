from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/Unicode-class.html'] = {'0': '<p>实用 Unicode 字符的常量。</p>', '1': '<p>目前，这些字符都与双向文本有关。</p>', '2': '<p>另请参阅：</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
