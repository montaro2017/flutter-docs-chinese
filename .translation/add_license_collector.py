from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/LicenseEntryCollector.html': {'0': '<p>传给 <a href="foundation/LicenseRegistry/addLicense.html">LicenseRegistry.addLicense</a> 的回调签名。</p>'},
 'foundation/LicenseRegistry/addLicense.html': {
 '0': '<p>向注册表添加许可证。</p>',
 '1': '<p>为了仅在确有必要时才处理许可证，添加许可证时会注册一个返回 <a href="foundation/LicenseEntry-class.html">LicenseEntry</a> 对象列表的闭包。只有访问 <a href="foundation/LicenseRegistry/licenses.html">licenses</a> 时才会调用该闭包；正常运行时，如果用户没有请求查看许可证，该闭包就不会被调用。</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
