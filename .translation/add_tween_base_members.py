from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/Tween/Tween.html'] = {
 '0': '<p>创建补间。</p>',
 '1': obj['animation/IntTween/IntTween.html']['1'],
}
obj['animation/Tween/lerp.html'] = dict(obj['animation/ReverseTween/lerp.html'])
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
