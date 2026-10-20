from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'animation/TrainHoppingAnimation-class.html': {
  '0': '<p>此动画起初代理第一个动画。当第一个动画的值越过第二个动画的值时（可能因为第二个动画沿相反方向运行，也可能因为一个动画追上并超过另一个），它会跳转为代理第二个动画。</p>',
  '1': '<p>当 <a href="animation/TrainHoppingAnimation-class.html">TrainHoppingAnimation</a> 从代理第一个动画切换为代理第二个动画时，会调用 <a href="animation/TrainHoppingAnimation/onSwitchedTrain.html">onSwitchedTrain</a> 回调。</p>',
  '2': '<p>如果两个动画的初始值相同，<a href="animation/TrainHoppingAnimation-class.html">TrainHoppingAnimation</a> 会立即跳转到第二个动画，但不会调用 <a href="animation/TrainHoppingAnimation/onSwitchedTrain.html">onSwitchedTrain</a> 回调。如果只提供一个动画（即第二个为 null），<a href="animation/TrainHoppingAnimation-class.html">TrainHoppingAnimation</a> 就只代理第一个动画。</p>',
  '3': '<p>由于此对象即使没有自身的监听器，也必须跟踪两个动画，因此它不会在所有监听器被移除时关闭，而是提供 <a href="animation/TrainHoppingAnimation/dispose.html">dispose()</a> 方法。调用此方法可关闭此对象。</p>',
 },
 'animation/TrainHoppingAnimation/TrainHoppingAnimation.html': {
  '0': '<p>创建跳跃切换动画。</p>',
  '1': '<p>当前动画参数不能为 null，但下一个动画参数可以为 null。如果下一个动画为 null，此对象将只代理第一个动画，永远不会切换。</p>',
 },
 'animation/TrainHoppingAnimation/currentTrain.html': {
  '0': '<p>当前驱动此动画的动画。</p>',
  '1': '<p>调用 <a href="animation/TrainHoppingAnimation/onSwitchedTrain.html">onSwitchedTrain</a> 时，此属性引用的对象会从第一个动画变为第二个动画。</p>',
 },
 'animation/TrainHoppingAnimation/onSwitchedTrain.html': {
  '0': '<p>此动画切换为由第二个动画驱动时调用。</p>',
  '1': '<p>如果传给构造函数的两个动画在调用构造函数时具有相同的值，则不会调用此回调。在这种情况下，从一开始就使用第二个动画，并忽略第一个动画。</p>',
 },
 'animation/TrainHoppingAnimation/dispose.html': {'0': '<p>释放此动画使用的所有资源。调用后，此对象将无法继续使用。</p>'},
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
