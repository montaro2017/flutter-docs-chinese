from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/TweenSequence-class.html'] = {
 '0': '<p>用于创建值由一系列 <a href="animation/Tween-class.html">Tween</a> 定义的 <a href="animation/Animation-class.html">Animation</a>。</p>',
 '1': '<p>每个 <a href="animation/TweenSequenceItem-class.html">TweenSequenceItem</a> 都有一个权重，用于确定它占动画总时长的比例。每个补间定义由其权重确定的时间区间内的动画值。</p>',
}
obj['animation/TweenSequence/TweenSequence.html'] = {
 '0': '<p>构造一个 TweenSequence。</p>',
 '1': '<p><code>items</code> 参数必须是包含一个或多个 <a href="animation/TweenSequenceItem-class.html">TweenSequenceItem</a> 的列表。</p>',
 '2': '<p>构建 <a href="animation/TweenSequence-class.html">TweenSequence</a> 有少量开销，因此在可能的情况下最好复用它，而不是每帧重新构建。</p>',
}
for cls in ['TweenSequence', 'FlippedTweenSequence']:
 obj[f'animation/{cls}/transform.html'] = {
  '0': '<p>返回对象在点 <code>t</code> 处的值。</p>',
  '1': '<p><code>t</code> 通常表示 0.0 到 1.0 范围内的比例，但实际上也可能超出此范围。</p>',
  '2': '<p>另请参阅：</p>',
 }
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
path = data / 'translations-fragments.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/TweenSequence-class.html'] = [{
 'source': 'This example defines an animation that uses an easing curve to interpolate\nbetween 5.0 and 10.0 during the first 40% of the animation, remains at 10.0\nfor the next 20%, and then returns to 5.0 for the final 40%.',
 'translation': '此示例定义一个动画：在前 40% 的时间内，使用缓动曲线在 5.0 和 10.0 之间插值；在接下来的 20% 时间内保持 10.0；最后在剩余 40% 的时间内返回 5.0。',
}]
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
