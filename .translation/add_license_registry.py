from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/LicenseRegistry-class.html': {
 '0': '<p>供软件包添加许可证的注册表，以便在 <a href="material/LicensePage-class.html">LicensePage</a> 等界面中集中显示。</p>',
 '1': '<p>软件包可以通过 <a href="foundation/LicenseRegistry/addLicense.html">addLicense</a> 注册许可证。需要显示全部许可证的用户界面可以通过访问 <a href="foundation/LicenseRegistry/licenses.html">licenses</a> 获取它们。</p>',
 '2': '<p>flutter 工具会自动收集每个软件包根目录中 LICENSE 文件的内容，将其合并为默认资源包中的一个 NOTICES 文件（或其压缩版本 <code>NOTICES.Z</code>）。文件中各许可证之间用一行八十个连字符（<code>-</code>）分隔。每项许可证以其适用的软件包名称列表开头，每行一个名称，名称列表与许可证正文之间以空行分隔。<code>services</code> 包会注册一个许可证收集器，拆分此文件并将每个条目添加到注册表中。</p>',
 '3': '<p>每个软件包的 LICENSE 文件可以只包含一个许可证，也可以采用上述格式。采用后一种格式时，每项组成许可证及其软件包名称列表都会独立合并。</p>',
 '4': '<p>另请参阅：</p>',
 },
 'foundation/LicenseRegistry/licenses.html': {'0': '<p>返回已注册的许可证。</p>', '1': '<p>生成许可证列表的开销较大。</p>'},
 'foundation/LicenseRegistry/reset.html': {'0': '<p>重置 <a href="foundation/LicenseRegistry-class.html">LicenseRegistry</a> 的内部状态。</p>', '1': '<p>用于测试。</p>'},
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/LicenseRegistry-class.html'] = {
 '0': '<dd>返回已注册的许可证。<div class="features"><span class="feature">无 setter</span></div></dd>',
 '1': '<dd>向注册表添加许可证。</dd>',
 '2': '<dd>重置 <a href="foundation/LicenseRegistry-class.html">LicenseRegistry</a> 的内部状态。</dd>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
