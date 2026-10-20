from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/AnimationController/value.html'] = {
 '0': '<p>动画的当前值。</p>',
 '1': '<p>设置此值会通知所有监听器，告知值已发生变化。</p>',
 '2': '<p>如果控制器当前正在运行，设置此值还会停止控制器；发生这种情况时，也会通知所有状态监听器。</p>',
}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
