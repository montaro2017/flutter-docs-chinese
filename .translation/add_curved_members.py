from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'animation/CurvedAnimation/CurvedAnimation.html': {'0': '<p>创建曲线动画。</p>'},
 'animation/CurvedAnimation/curve.html': {'0': '<p>正向运行时使用的曲线。</p>'},
 'animation/CurvedAnimation/parent.html': {'0': '<p>此动画对其应用曲线的来源动画。</p>'},
 'animation/CurvedAnimation/dispose.html': {'0': '<p>清理此 CurvedAnimation 添加的所有监听器。</p>'},
 'animation/CurvedAnimation/reverseCurve.html': {
  '0': '<p>反向运行时使用的曲线。</p>',
  '1': '<p>如果父动画尚未达到 <a href="animation/AnimationStatus.html">AnimationStatus.completed</a> 或 <a href="animation/AnimationStatus.html">AnimationStatus.dismissed</a> 状态就改变方向，<a href="animation/CurvedAnimation-class.html">CurvedAnimation</a> 会继续使用同一条曲线（但沿相反方向运行），以避免视觉上的不连续。</p>',
  '2': '<p>由于 <a href="animation/CurvedAnimation-class.html">CurvedAnimation</a> 可能向父动画添加监听器，必须只创建一次（例如在 <a href="widgets/State/initState.html">State.initState</a> 中），并在 <a href="widgets/State/dispose.html">State.dispose</a> 中释放。不要在每次 build 时重新创建，否则每次重建都会泄漏已添加的监听器。如果不需要 <a href="animation/CurvedAnimation/reverseCurve.html">reverseCurve</a>，优先使用 <code>parent.drive(CurveTween(curve: curve))</code>，它不需要单独释放。</p>',
  '3': '<p>如果此字段为 null，则两个方向都使用 <a href="animation/CurvedAnimation/curve.html">curve</a>。</p>',
 },
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
