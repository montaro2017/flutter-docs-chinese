from pathlib import Path
import json
path = Path(__file__).resolve().parent / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/ValueListenableTransformer.html'] = {'0': '<p><a href="animation/Animation/Animation.fromValueListenable.html">Animation.fromValueListenable</a> 中用于转换值的方法的函数签名。</p>'}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
