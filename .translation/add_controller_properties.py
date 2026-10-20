from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'animation/AnimationController/duration.html': {
  '0': '<p>此动画应持续的时长。</p>',
  '1': '<p>如果指定了 <a href="animation/AnimationController/reverseDuration.html">reverseDuration</a>，则 <a href="animation/AnimationController/duration.html">duration</a> 仅用于 <a href="animation/AnimationController/forward.html">forward</a> 方向的运行。否则，它指定两个方向的运行时长。</p>',
 },
 'animation/AnimationController/reverseDuration.html': {
  '0': '<p>此动画沿 <a href="animation/AnimationController/reverse.html">reverse</a> 方向运行时应持续的时长。</p>',
  '1': '<p>如果未指定 <a href="animation/AnimationController/reverseDuration.html">reverseDuration</a> 或将其设为 null，则使用 <a href="animation/AnimationController/duration.html">duration</a> 的值。</p>',
 },
 'animation/AnimationController/lowerBound.html': {'0': '<p>此动画被视为处于 dismissed 状态时的值。</p>'},
 'animation/AnimationController/upperBound.html': {'0': '<p>此动画被视为已完成时的值。</p>'},
 'animation/AnimationController/debugLabel.html': {'0': '<p>用于 <a href="animation/Animation/toString.html">toString</a> 输出的标签，便于在调试输出中识别动画控制器实例。</p>'},
 'animation/AnimationController/animationBehavior.html': {
  '0': '<p>当 <a href="dart-ui/AccessibilityFeatures/disableAnimations.html">AccessibilityFeatures.disableAnimations</a> 为 true 时控制器的行为。</p>',
  '1': '<p><a href="animation/AnimationController/AnimationController.html">AnimationController.new</a> 构造函数默认使用 <a href="animation/AnimationBehavior.html">AnimationBehavior.normal</a>，而 <a href="animation/AnimationController/AnimationController.unbounded.html">AnimationController.unbounded</a> 构造函数默认使用 <a href="animation/AnimationBehavior.html">AnimationBehavior.preserve</a>。</p>',
 },
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
