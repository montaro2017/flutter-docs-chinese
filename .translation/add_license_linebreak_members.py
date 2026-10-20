from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/LicenseEntryWithLineBreaks/paragraphs.html': {
 '0': '<p>许可证的段落，每段由一个 <code>LicenseParagraph</code> 表示，其中包含字符串和格式信息。</p>',
 '1': '<p>段落可以包含换行符，但不建议这样做，因为会使排版不美观。</p>',
 },
 'foundation/LicenseEntryWithLineBreaks/packages.html': {'0': '<p>此许可证条目适用的软件包名称。</p>'},
 'foundation/LicenseEntryWithLineBreaks/text.html': {
 '0': '<p>许可证的文本。</p>',
 '1': '<p>文本将按照以下约定拆分为段落：</p>',
 '2': '<p>算法会对每个段落使用粗略的启发式规则，尝试判断其缩进程度或是否居中。</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/LicenseEntryWithLineBreaks/text.html'] = [
 {'source': '<li>Lines starting with a different number of space characters than the\nprevious line start a new paragraph, with those spaces removed.</li>', 'translation': '<li>如果一行开头的空格数与上一行不同，则开始一个新段落，并移除这些空格。</li>'},
 {'source': '<li>Blank lines start a new paragraph.</li>', 'translation': '<li>空行开始一个新段落。</li>'},
 {'source': '<li>Other line breaks are replaced by a single space character.</li>', 'translation': '<li>其他换行符替换为一个空格。</li>'},
 {'source': '<li>Leading spaces on a line are removed.</li>', 'translation': '<li>移除行首空格。</li>'},
]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/LicenseEntryWithLineBreaks-class.html'] = {
 '1': '<dd>为段落内部使用显式换行、通过空行或缩进文本标记段落边界的许可证创建一个许可证条目。<div class="constructor-modifier features">const</div></dd>',
 '2': '<dd>此许可证条目适用的软件包名称。<div class="features"><span class="feature">final</span></div></dd>',
 '3': '<dd>许可证的段落，每段由一个 <code>LicenseParagraph</code> 表示，其中包含字符串和格式信息。<div class="features"><span class="feature">无 setter</span><span class="feature">重写</span></div></dd>',
 '4': '<dd>许可证的文本。<div class="features"><span class="feature">final</span></div></dd>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
