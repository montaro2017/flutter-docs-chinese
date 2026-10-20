from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/LicenseEntry-class.html': {
 '0': '<p>适用于应用部分软件或资源的许可证，可显示在 <a href="material/LicensePage-class.html">LicensePage</a> 等界面中。</p>',
 '1': '<p>为了获得最佳性能，应仅在传给 <a href="foundation/LicenseRegistry/addLicense.html">LicenseRegistry.addLicense</a> 的 <a href="foundation/LicenseEntryCollector.html">LicenseEntryCollector</a> 回调中，按需创建 <a href="foundation/LicenseEntry-class.html">LicenseEntry</a> 对象。</p>',
 },
 'foundation/LicenseEntry/packages.html': {'0': '<p>此许可证条目适用的软件包名称。</p>'},
 'foundation/LicenseEntry/paragraphs.html': {
 '0': '<p>许可证的段落，每段由一个 <a href="foundation/LicenseParagraph-class.html">LicenseParagraph</a> 表示，其中包含字符串和格式信息。</p>',
 '1': '<p>段落可以包含换行符，但不建议这样做，因为会使排版不美观。</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
