from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/TrainHoppingAnimation/value.html'] = {'0': '<p>动画的当前值。</p>'}
obj['animation/TrainHoppingAnimation/status.html'] = {'0': '<p>此动画的当前状态。</p>'}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
path = data / 'shared-text.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'Creates a train-hopping animation.': '创建跳跃切换动画。',
 'The animation that is currently driving this animation.': '当前驱动此动画的动画。',
 'Called when this animation switches to be driven by the second animation.': '此动画切换为由第二个动画驱动时调用。',
 'Frees all the resources used by this performance. After this is called, this object is no longer usable.': '释放此动画使用的所有资源。调用后，此对象将无法继续使用。',
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
