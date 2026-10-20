from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'animation/TweenSequenceItem-class.html': {'0': '<p>用于保存 <a href="animation/TweenSequence-class.html">TweenSequence</a> 中一个元素的简单容器。</p>'},
 'animation/TweenSequenceItem/TweenSequenceItem.html': {'0': '<p>构造一个 TweenSequenceItem。</p>', '1': '<p><code>weight</code> 必须大于 0.0。</p>'},
 'animation/TweenSequenceItem/tween.html': {'0': '<p>定义 <a href="animation/TweenSequence-class.html">TweenSequence</a> 在动画时长中某个区间内的值，该区间由 <a href="animation/TweenSequenceItem/weight.html">weight</a> 和此条目在列表中的位置确定。</p>'},
 'animation/TweenSequenceItem/weight.html': {
  '0': '<p>一个任意权重值，表示使用 <a href="animation/TweenSequenceItem/tween.html">tween</a> 的时间占 <a href="animation/TweenSequence-class.html">TweenSequence</a> 动画总时长的相对比例。</p>',
  '1': '<p>单个条目的比例等于该条目的权重除以所有条目权重之和。</p>',
 },
 'animation/FlippedTweenSequence-class.html': {
  '0': '<p>用于创建值由一系列 <a href="animation/Tween-class.html">Tween</a> 定义的翻转 <a href="animation/Animation-class.html">Animation</a>。</p>',
  '1': '<p>创建一个 <a href="animation/TweenSequence-class.html">TweenSequence</a>，其求值结果使补间在水平方向和垂直方向上同时翻转。</p>',
  '2': '<p>此补间序列假定求值结果必须是 0.0 到 1.0 之间的 double 值。</p>',
 },
 'animation/FlippedTweenSequence/FlippedTweenSequence.html': {
  '0': '<p>创建一个翻转的 <a href="animation/TweenSequence-class.html">TweenSequence</a>。</p>',
  '1': '<p><code>items</code> 参数必须是包含一个或多个 <a href="animation/TweenSequenceItem-class.html">TweenSequenceItem</a> 的列表。</p>',
  '2': '<p>构建 <code>TweenSequence</code> 有少量开销，因此在可能的情况下最好复用它，而不是每帧重新构建。</p>',
 },
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
path = data / 'translations-fragments.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/TweenSequenceItem/tween.html'] = [{
 'source': 'The value of this item can be "curved" by chaining it to a <a href="animation/CurveTween-class.html">CurveTween</a>.\nFor example to create a tween that eases from 0.0 to 10.0:',
 'translation': '将此条目与 <a href="animation/CurveTween-class.html">CurveTween</a> 链式组合，可对其值应用曲线。例如，创建从 0.0 缓动到 10.0 的补间：',
}]
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
