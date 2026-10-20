from pathlib import Path
import json

data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
for cls in ['CompoundAnimation', 'AnimationMin', 'AnimationMax']:
    link = f'<a href="animation/{cls}-class.html">{cls}</a>'
    obj[f'animation/{cls}/{cls}.html'] = {
        '0': f'<p>创建一个 {link}。</p>',
        '1': f'<p>任一参数都可以是 {link}，以组合多个动画。</p>',
    }
obj['animation/AnimationMean/AnimationMean.html'] = {
    '0': '<p>创建一个跟踪另外两个动画平均值的动画。</p>',
}
for cls in ['AnimationMean', 'AnimationMin', 'AnimationMax']:
    obj[f'animation/{cls}/value.html'] = {'0': '<p>动画的当前值。</p>'}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
