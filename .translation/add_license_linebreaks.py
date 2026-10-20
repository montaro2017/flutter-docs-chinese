from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/LicenseEntryWithLineBreaks-class.html': {
 '0': '<p><a href="foundation/LicenseEntry-class.html">LicenseEntry</a> 的一种变体，适用于用空行分隔段落、并在段落内部使用显式换行的许可证。</p>',
 '1': '<p>以一个或多个空格开头的行也会被视为新段落的起始，除非其开头空格数与上一行相同；此时会将其视为缩进段落的延续。</p>',
 '3': '<p>这会产生包含六个<a href="foundation/LicenseEntryWithLineBreaks/paragraphs.html">paragraphs</a>的许可证，其中第三、第四和第五段缩进一级。</p>',
 '4': '<h2 id="performance-considerations">性能考量</h2>',
 '5': '<p>解析段落的开销相对较大。每帧处理一个许可证是合理的，但不建议同时处理更多。可以考虑使用 <a href="foundation/compute.html">compute</a> 将工作移到另一个线程，一次处理全部内容；或者使用 <a href="scheduler/SchedulerBinding/scheduleTask.html">SchedulerBinding.scheduleTask</a> 将工作分散到多个帧中。</p>',
 },
 'foundation/LicenseEntryWithLineBreaks/LicenseEntryWithLineBreaks.html': {
 '0': '<p>为段落内部使用显式换行、通过空行或缩进文本标记段落边界的许可证创建一个许可证条目。</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/LicenseEntryWithLineBreaks-class.html'] = [{
 'source': 'For example, the BSD license in this format could be encoded as follows:',
 'translation': '例如，采用此格式的 BSD 许可证可以按如下方式表示：',
}]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
