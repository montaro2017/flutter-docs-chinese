from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
for add, remove, subject, kind in [('addListener','removeListener','值','监听器'),('addStatusListener','removeStatusListener','状态','状态监听器')]:
 def link(member):
  return f'<a href="animation/Animation/{member}.html">{member}</a>'
 obj[f'animation/Animation/{add}.html'] = {
  '0': f'<p>每当动画的{subject}发生变化时调用监听器。</p>',
  '1': f'<p>可以使用 {link(remove)} 移除监听器。</p>',
 }
 obj[f'animation/Animation/{remove}.html'] = {
  '0': f'<p>停止在动画的{subject}发生变化时调用此监听器。</p>',
  '1': f'<p>如果 <code>listener</code> 当前未注册为{kind}，此方法不执行任何操作。</p>',
  '2': f'<p>可以使用 {link(add)} 添加监听器。</p>',
 }
obj.update({
 'animation/Animation/isCompleted.html': {'0': '<p>此动画是否停在终点。</p>'},
 'animation/Animation/isDismissed.html': {'0': '<p>此动画是否停在起点。</p>'},
 'animation/Animation/isAnimating.html': {
  '0': '<p>此动画是否正在沿任一方向运行。</p>',
  '1': '<p>默认情况下，此值等于 <code>status.isAnimating</code>，但 <a href="animation/AnimationController-class.html">AnimationController</a> 重写了此方法，使其结果取决于控制器是否正在持续接收时钟更新。</p>',
 },
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
