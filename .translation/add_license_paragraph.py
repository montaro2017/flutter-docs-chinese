from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/LicenseParagraph-class.html': {
 '0': '<p>表示 <a href="foundation/LicenseEntry-class.html">LicenseEntry</a> 中一个段落的字符串。</p>',
 '1': '<p>参见 <a href="foundation/LicenseEntry/paragraphs.html">LicenseEntry.paragraphs</a>。</p>',
 },
 'foundation/LicenseParagraph/text.html': {'0': '<p>段落的文本。</p>', '1': '<p>不应包含前导或尾随空白。</p>'},
 'foundation/LicenseParagraph/LicenseParagraph.html': {'0': '<p>为许可证条目的段落创建一个字符串。</p>'},
 'foundation/LicenseParagraph/indent.html': {
 '0': '<p>段落的缩进级数。</p>',
 '1': '<p>依此类推。</p>',
 '2': '<p>此外，可以使用特殊值 <a href="foundation/LicenseParagraph/centeredIndent-constant.html">centeredIndent</a> 表示段落居中，而非缩进。</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = p.parent / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/LicenseParagraph/indent.html'] = [
 {'source': '<li>0 means the paragraph is not indented.</li>', 'translation': '<li>0 表示段落不缩进。</li>'},
 {'source': '<li>1 means the paragraph is indented one unit of indentation.</li>', 'translation': '<li>1 表示段落缩进一个单位。</li>'},
 {'source': '<li>2 means the paragraph is indented two units of indentation.</li>', 'translation': '<li>2 表示段落缩进两个单位。</li>'},
]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
