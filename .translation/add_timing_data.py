from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
name_hint = '<p>此字段应具有足够的唯一性和描述性，使人能够轻松识别测量的是哪部分代码。</p>'
pages = {
 'TimedBlock-class.html': ['<p>提供由 <a href="foundation/FlutterTimeline-class.html">FlutterTimeline</a> 计时的具名代码区块的 <a href="foundation/TimedBlock/start.html">start</a>、<a href="foundation/TimedBlock/end.html">end</a> 和 <a href="foundation/TimedBlock/duration.html">duration</a>。</p>'],
 'AggregatedTimedBlock-class.html': ['<p>汇总具有相同 <a href="foundation/AggregatedTimedBlock/name.html">name</a> 的多个 <a href="foundation/TimedBlock-class.html">TimedBlock</a> 对象。</p>', '<p>同一代码区块在一帧内执行多次是常见情况。合并多次执行并报告该代码区块的总耗时很有用。</p>'],
 'AggregatedTimings-class.html': ['<p>提供 <a href="foundation/FlutterTimeline-class.html">FlutterTimeline</a> 所收集计时数据的汇总结果。</p>'],
 'TimedBlock/duration.html': ['<p>所测量代码区块的执行耗时，以微秒为单位。</p>'],
 'TimedBlock/end.html': ['<p>标记所测量代码区块结束时刻的时间戳，以微秒为单位。</p>'],
 'TimedBlock/start.html': ['<p>标记所测量代码区块开始时刻的时间戳，以微秒为单位。</p>'],
 'TimedBlock/TimedBlock.html': ['<p>根据 <code>name</code>、<code>start</code> 和 <code>end</code> 创建一个代码计时区块。</p>', '<p><code>name</code> 应具有足够的唯一性和描述性，使人能够轻松识别测量的是哪部分代码。</p>'],
 'AggregatedTimedBlock/AggregatedTimedBlock.html': ['<p>根据 <code>name</code> 和 <code>duration</code> 创建一个代码计时区块。</p>', '<p><code>name</code> 应具有足够的唯一性和描述性，使人能够轻松识别测量的是哪部分代码。</p>'],
 'AggregatedTimedBlock/count.html': ['<p>已汇总的 <a href="foundation/TimedBlock-class.html">TimedBlock</a> 对象数量。</p>'],
 'AggregatedTimedBlock/duration.html': ['<p>已汇总代码区块的 <a href="foundation/TimedBlock/duration.html">TimedBlock.duration</a> 值之和。</p>'],
 'AggregatedTimings/aggregatedBlocks.html': ['<p>从上次重置到调用 <a href="foundation/FlutterTimeline/debugCollect.html">FlutterTimeline.debugCollect</a> 期间收集的计时区块汇总。</p>', '<p>不保证报告所有代码区块。这里只列出上次重置后执行过的区块。请使用 <a href="foundation/AggregatedTimings/getAggregated.html">getAggregated</a> 妥善处理缺失的代码区块。</p>'],
 'AggregatedTimings/AggregatedTimings.html': ['<p>为提供的计时区块创建计时汇总。</p>'],
 'AggregatedTimings/getAggregated.html': ['<p>返回具名代码区块的汇总数据。</p>', '<p>如果该区块自上次重置后从未执行，则返回耗时和次数均为零的汇总。</p>'],
 'AggregatedTimings/timedBlocks.html': ['<p>从上次重置到调用 <a href="foundation/FlutterTimeline/debugCollect.html">FlutterTimeline.debugCollect</a> 期间收集的所有计时区块。</p>'],
}
for cls in ('TimedBlock', 'AggregatedTimedBlock'):
 pages[f'{cls}/name.html'] = ['<p>所测量代码区块的可读标签。</p>', name_hint]
for page, blocks in pages.items():
 d['foundation/' + page] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
