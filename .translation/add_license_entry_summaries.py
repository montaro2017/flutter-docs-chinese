from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/LicenseEntry/LicenseEntry.html'] = {
 '0': '<p>此构造函数使子类能够提供 const 构造函数，从而用于 const 表达式。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/LicenseEntry-class.html'] = {
 '1': '<dd>此构造函数使子类能够提供 const 构造函数，从而用于 const 表达式。<div class="constructor-modifier features">const</div></dd>',
 '2': '<dd>此许可证条目适用的软件包名称。<div class="features"><span class="feature">无 setter</span></div></dd>',
 '3': '<dd>许可证的段落，每段由一个 <a href="foundation/LicenseParagraph-class.html">LicenseParagraph</a> 表示，其中包含字符串和格式信息。<div class="features"><span class="feature">无 setter</span></div></dd>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
