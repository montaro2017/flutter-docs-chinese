from pathlib import Path
import json

data = Path(__file__).resolve().parent
def update(name, entries):
    path = data / name
    obj = json.loads(path.read_text(encoding='utf-8'))
    obj.update(entries)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

update('shared-text.json', {
 'Creates an animation that tracks the mean of two other animations.': '创建一个跟踪另外两个动画平均值的动画。',
 'The first sub-animation. Its status takes precedence if neither are animating.': '第一个子动画。如果两个子动画都未运行，则优先采用此动画的状态。',
 'The second sub-animation.': '第二个子动画。',
 'Gets the status of this animation based on the': '根据',
 'status.': '的状态获取此动画的状态。',
 'Calls all the listeners.': '调用所有监听器。',
 'Calls all the status listeners.': '调用所有状态监听器。',
})
update('translations.json', {
 'animation/CompoundAnimation-class.html': {
  '0': '<p>用于组合多个动画的接口。子类只需实现 <code>value</code> getter，即可控制子动画的组合方式。可以通过链式组合将两个以上的动画组合起来。</p>',
  '1': '<p>例如，要创建一个值为另外两个动画之和的动画，可继承此类并定义 <code>T get value = first.value + second.value;</code></p>',
  '2': '<p>默认情况下，如果 <a href="animation/CompoundAnimation/next.html">next</a> 动画正在运行，<a href="animation/CompoundAnimation-class.html">CompoundAnimation</a> 的 <a href="animation/CompoundAnimation/status.html">status</a> 就是 <a href="animation/CompoundAnimation/next.html">next</a> 动画的状态；否则为 <a href="animation/CompoundAnimation/first.html">first</a> 动画的状态。</p>',
 },
 'animation/CompoundAnimation/first.html': {'0': '<p>第一个子动画。如果两个子动画都未运行，则优先采用此动画的状态。</p>'},
 'animation/CompoundAnimation/next.html': {'0': '<p>第二个子动画。</p>'},
 'animation/CompoundAnimation/status.html': {
  '0': '<p>根据 <a href="animation/CompoundAnimation/first.html">first</a> 和 <a href="animation/CompoundAnimation/next.html">next</a> 的状态获取此动画的状态。</p>',
  '1': '<p>默认情况下，如果 <a href="animation/CompoundAnimation/next.html">next</a> 动画正在运行，就使用它的状态。否则默认使用 <a href="animation/CompoundAnimation/first.html">first</a> 的状态。</p>',
 },
})
