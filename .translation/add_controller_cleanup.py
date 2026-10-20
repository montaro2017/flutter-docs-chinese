from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/AnimationController/stop.html'] = {
 '0': '<p>停止运行此动画。</p>',
 '1': '<p>此方法不会触发任何通知。动画停留在当前状态。</p>',
 '2': '<p>默认情况下，最近返回的 <a href="scheduler/TickerFuture-class.html">TickerFuture</a> 会被标记为已取消，这意味着该 future 永远不会完成，而其派生的 <a href="scheduler/TickerFuture/orCancel.html">TickerFuture.orCancel</a> future 将以 <a href="scheduler/TickerCanceled-class.html">TickerCanceled</a> 错误完成。如果传入值为 false 的 <code>canceled</code> 参数，则不会取消，两个 future 都会成功完成。</p>',
 '3': '<p>另请参阅：</p>',
}
obj['animation/AnimationController/dispose.html'] = {
 '0': '<p>释放此对象使用的资源。调用此方法后，该对象将无法继续使用。</p>',
 '1': obj['animation/AnimationController/reset.html']['1'],
}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
