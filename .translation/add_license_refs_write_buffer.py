from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/WriteBuffer-class.html'] = {
 '0': '<p>用于逐步构建 <a href="dart-typed_data/ByteData-class.html">ByteData</a> 实例的只写缓冲区。</p>',
 '1': '<p>WriteBuffer 实例只能使用一次。尝试重复使用会抛出 <a href="dart-core/StateError-class.html">StateError</a>。</p>',
 '2': '<p>始终使用 <a href="dart-typed_data/Endian/host.html">Endian.host</a> 字节序。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/LicenseRegistry-class.html'] = [
 {'source': '<li><a href="material/showAboutDialog.html">showAboutDialog</a>, which shows a Material-style dialog with information\nabout the application, including a button that shows a <a href="material/LicensePage-class.html">LicensePage</a> that\nuses this API to select licenses to show.</li>',
 'translation': '<li><a href="material/showAboutDialog.html">showAboutDialog</a> 显示包含应用信息的 Material 风格对话框，其中包含打开 <a href="material/LicensePage-class.html">LicensePage</a> 的按钮；该页面使用此 API 选择要显示的许可证。</li>'},
 {'source': '<li><a href="material/AboutListTile-class.html">AboutListTile</a>, which is a widget that can be added to a <a href="material/Drawer-class.html">Drawer</a>. When\ntapped it calls <a href="material/showAboutDialog.html">showAboutDialog</a>.</li>',
 'translation': '<li><a href="material/AboutListTile-class.html">AboutListTile</a> 是可添加到 <a href="material/Drawer-class.html">Drawer</a> 的 widget，点击时会调用 <a href="material/showAboutDialog.html">showAboutDialog</a>。</li>'},
]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
