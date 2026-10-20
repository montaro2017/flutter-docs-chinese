from pathlib import Path
import json
data = Path(__file__).resolve().parent
labels = {
 'The status of an animation.': '动画的状态。',
 'The animation is stopped at the beginning.': '动画停在起点。',
 'The animation is running from beginning to end.': '动画正从起点向终点运行。',
 'The animation is running backwards, from end to beginning.': '动画正反向运行，从终点返回起点。',
 'The animation is stopped at the end.': '动画停在终点。',
 'Whether the animation is running in either direction.': '动画是否正在沿任一方向运行。',
 'Whether the animation is stopped at the end.': '动画是否停在终点。',
 'Whether the animation is stopped at the beginning.': '动画是否停在起点。',
 'Whether the current aim of the animation is toward completion.': '动画当前是否朝完成方向推进。',
 'A constant List of the values in this enum, in order of their declaration.': '包含此枚举所有值的常量列表，按声明顺序排列。',
 'The name of the enum value.': '枚举值的名称。',
}
path = data / 'shared-text.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update(labels)
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/AnimationStatus.html'] = {'0': '<p>动画的状态。</p>'}
for name, english in [
 ('isAnimating', 'Whether the animation is running in either direction.'),
 ('isCompleted', 'Whether the animation is stopped at the end.'),
 ('isDismissed', 'Whether the animation is stopped at the beginning.'),
 ('isForwardOrCompleted', 'Whether the current aim of the animation is toward completion.'),
 ('values-constant', 'A constant List of the values in this enum, in order of their declaration.'),
]:
 obj[f'animation/AnimationStatus/{name}.html'] = {'0': f'<p>{labels[english]}</p>'}
obj['animation/AnimationStatus/isForwardOrCompleted.html']['1'] = '<p>具体来说，对于 <a href="animation/AnimationStatus.html">AnimationStatus.forward</a> 或 <a href="animation/AnimationStatus.html">AnimationStatus.completed</a> 返回 <code>true</code>；对于 <a href="animation/AnimationStatus.html">AnimationStatus.reverse</a> 或 <a href="animation/AnimationStatus.html">AnimationStatus.dismissed</a> 返回 <code>false</code>。</p>'
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
