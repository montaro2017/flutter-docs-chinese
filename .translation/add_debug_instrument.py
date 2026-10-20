from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/debugInstrumentAction.html': {
 '0': '<p>执行指定的 <code>action</code>；在调试构建中，如果 <a href="foundation/debugInstrumentationEnabled.html">debugInstrumentationEnabled</a> 为 true，还会测量该操作的耗时。</p>',
 '1': '<p>测量结果会通过 <a href="rendering/debugPrint.html">debugPrint</a> 输出到日志。在非调试构建中，或 <a href="foundation/debugInstrumentationEnabled.html">debugInstrumentationEnabled</a> 为 false 时，只执行 <code>action</code>，不进行测量。</p>',
 '2': '<p>返回执行 <code>action</code> 的结果。</p>',
 '3': '<p>另请参阅：</p>',
 },
 'foundation/debugInstrumentationEnabled.html': {
 '0': '<p>布尔值，表示 <a href="foundation/debugInstrumentAction.html">debugInstrumentAction</a> 是否在调试构建中测量操作的耗时。</p>',
 '1': '<p>框架内部不使用 <a href="foundation/debugInstrumentAction.html">debugInstrumentAction</a>，因此此标志不会为框架自身启用额外的测量。</p>',
 '2': '<p>另请参阅：</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/debugInstrumentAction.html'] = [{
 'source': '<li><a href="dart-developer/Timeline-class.html">Timeline</a>, which is used to record synchronous tracing events for\nvisualization in Chrome\'s tracing format. This method does not\nimplicitly add any timeline events.</li>',
 'translation': '<li><a href="dart-developer/Timeline-class.html">Timeline</a> 用于记录同步跟踪事件，以 Chrome 跟踪格式进行可视化。此方法不会隐式添加任何时间线事件。</li>',
}]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
