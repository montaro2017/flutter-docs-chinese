from pathlib import Path
import json
data = Path(__file__).resolve().parent
def update(name, entries):
 path = data / name
 obj = json.loads(path.read_text(encoding='utf-8'))
 obj.update(entries)
 path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
update('translations.json', {
 'animation/AnimationStatusListener.html': {'0': '<p>通过 <a href="animation/Animation/addStatusListener.html">Animation.addStatusListener</a> 注册的监听器的函数签名。</p>'},
 'animation/AnimationBehavior.html': {
  '0': '<p>配置禁用动画时 <a href="animation/AnimationController-class.html">AnimationController</a> 的行为。</p>',
  '1': '<p>当 <a href="dart-ui/AccessibilityFeatures/disableAnimations.html">AccessibilityFeatures.disableAnimations</a> 为 true 时，设备请求 Flutter 尽可能减少或禁用动画。为遵循此请求，我们会缩短动画时长，并相应减少帧数。此枚举允许某些 <a href="animation/AnimationController-class.html">AnimationController</a> 不采用这一行为。</p>',
  '2': '<p>例如，控制可滚动列表物理模拟的 <a href="animation/AnimationController-class.html">AnimationController</a> 会使用 <a href="animation/AnimationBehavior.html">AnimationBehavior.preserve</a>，这样用户尝试滚动时，列表就不会过快跳到终点或起点。</p>',
 },
 'animation/AnimationBehavior/values-constant.html': {'0': '<p>包含此枚举所有值的常量列表，按声明顺序排列。</p>'},
})
update('translations-extra.json', {
 'animation/AnimationBehavior.html': {
  '2': '<dd>\n  <p>当 <a href="dart-ui/AccessibilityFeatures/disableAnimations.html">AccessibilityFeatures.disableAnimations</a> 为 true 时，<a href="animation/AnimationController-class.html">AnimationController</a> 会缩短动画时长。</p>\n  \n\n</dd>',
  '3': '<dd>\n  <p><a href="animation/AnimationController-class.html">AnimationController</a> 将保持原有行为。</p>\n<p>这是重复动画的默认行为，用于避免组件未考虑 <a href="dart-ui/AccessibilityFeatures/disableAnimations.html">AccessibilityFeatures.disableAnimations</a> 标志时，动画在屏幕上快速闪烁。</p>\n  \n\n</dd>',
 },
})
