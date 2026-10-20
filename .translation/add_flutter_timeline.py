from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'FlutterTimeline-class.html': ['<p>测量代码区块的运行耗时。</p>', '<p>此类可直接替代 <a href="dart-developer/Timeline-class.html">Timeline</a>，因为它提供的方法在签名上与 <a href="dart-developer/Timeline-class.html">Timeline</a> 兼容，并且开销很小。</p>', '<p>提供 <a href="foundation/FlutterTimeline/debugReset.html">debugReset</a> 和 <a href="foundation/FlutterTimeline/debugCollect.html">debugCollect</a> 方法，便于在以帧为单位的环境中使用。在这种环境中，可以将收集的指标归属于某一帧，再汇总为帧统计数据，例如每帧平均值。</p>', '<p>将测量结果转发给 <a href="dart-developer/Timeline-class.html">Timeline</a>，使其显示在 Flutter DevTools 中。</p>'],
 'FlutterTimeline/debugCollect.html': ['<p>返回自以下事件中最近一次发生以来收集的计时数据：将 <a href="foundation/FlutterTimeline/debugCollectionEnabled.html">debugCollectionEnabled</a> 设置为 true、上次调用 <a href="foundation/FlutterTimeline/debugCollect.html">debugCollect</a>，或上次调用 <a href="foundation/FlutterTimeline/debugReset.html">debugReset</a>。</p>', '<p>重置已收集的计时数据。</p>', '<p>仅供非发布模式使用，通常用于性能分析模式，因为该模式提供的计时结果接近发布模式。</p>'],
 'FlutterTimeline/debugCollectionEnabled.html': ['<p>是否收集代码区块的计时数据，并允许通过 <a href="foundation/FlutterTimeline/debugCollect.html">debugCollect</a> 方法获取。</p>', '<p>在发布模式下始终为 false。</p>'],
 'FlutterTimeline/debugReset.html': ['<p>清除此前收集的所有计时数据。</p>', '<p>使用此方法将指标限定到某一帧、指针事件或其他事件。具体做法是在事件开始时调用 <a href="foundation/FlutterTimeline/debugReset.html">debugReset</a>，在事件结束时调用 <a href="foundation/FlutterTimeline/debugCollect.html">debugCollect</a>。</p>', '<p>仅供非发布模式使用。</p>'],
 'FlutterTimeline/finishSync.html': ['<p>结束最近启动的同步操作。</p>', '<p>可以直接替代 <a href="dart-developer/Timeline/finishSync.html">Timeline.finishSync</a>。</p>'],
 'FlutterTimeline/now.html': ['<p>时间线所使用时钟的当前时间戳，以微秒为单位。</p>', '<p>在 Dart VM 上运行时，使用与嵌入 API 的 <code>Dart_TimelineGetMicros</code> 相同的单调时钟。</p>', '<p>在 Web 上运行时，使用 <code>window.performance.now</code>。</p>', '<p>可以直接替代 <a href="dart-developer/Timeline/now.html">Timeline.now</a>。</p>'],
}
for page, blocks in pages.items():
 d['foundation/' + page] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
