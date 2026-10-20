from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
duration = '<p><code>duration</code> 是此动画应持续的时长。</p>'
debug = '<p><code>debugLabel</code> 是帮助在调试时识别此动画的字符串（由 <a href="animation/Animation/toString.html">toString</a> 使用）。</p>'
vsync = '<p><code>vsync</code> 是当前上下文必需的 <a href="scheduler/TickerProvider-class.html">TickerProvider</a>，可以通过调用 <a href="animation/AnimationController/resync.html">resync</a> 更换。有关获取 ticker provider 的建议，请参阅 <a href="scheduler/TickerProvider-class.html">TickerProvider</a>。</p>'
obj['animation/AnimationController/AnimationController.html'] = {
 '0': '<p>创建动画控制器。</p>',
 '1': '<p><code>value</code> 是动画的初始值，默认为下界。</p>',
 '2': duration, '3': debug,
 '4': '<p><code>lowerBound</code> 是此动画可以达到的最小值，也是动画被视为处于 dismissed 状态时的值。</p>',
 '5': '<p><code>upperBound</code> 是此动画可以达到的最大值，也是动画被视为已完成时的值。</p>',
 '6': vsync,
}
obj['animation/AnimationController/AnimationController.unbounded.html'] = {
 '0': '<p>创建值没有上界或下界的动画控制器。</p>',
 '1': '<p><code>value</code> 是动画的初始值。</p>',
 '2': duration, '3': debug, '4': vsync,
 '5': '<p>此构造函数最适合由物理模拟驱动的动画，尤其是物理模拟没有预定边界的情况。</p>',
}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
