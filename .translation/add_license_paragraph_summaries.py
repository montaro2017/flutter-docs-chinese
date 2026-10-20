from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/LicenseParagraph/centeredIndent-constant.html'] = {
 '0': '<p>用于 <a href="foundation/LicenseParagraph/indent.html">indent</a> 的常量，表示居中对齐。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/LicenseParagraph-class.html'] = {
 '0': '<dd>为许可证条目的段落创建一个字符串。<div class="constructor-modifier features">const</div></dd>',
 '1': '<dd>段落的缩进级数。<div class="features"><span class="feature">final</span></div></dd>',
 '2': '<dd>段落的文本。<div class="features"><span class="feature">final</span></div></dd>',
 '3': '<dd>用于 <a href="foundation/LicenseParagraph/indent.html">indent</a> 的常量，表示居中对齐。</dd>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
