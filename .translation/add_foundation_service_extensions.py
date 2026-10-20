from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/FoundationServiceExtensions.html'] = {
 '0': '<p>基础库的服务扩展常量。</p>',
 '1': '<p>框架注册服务扩展时会使用这些常量，调用这些服务扩展的工具和服务也会使用它们。</p>',
 '2': '<p>应通过枚举值的 <code>.name</code> 属性获取各扩展名称的字符串值。</p>',
}
d['foundation/FoundationServiceExtensions/values-constant.html'] = {'0': '<p>按声明顺序包含此枚举所有值的常量列表。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
reg = '<li><a href="foundation/BindingBase/initServiceExtensions.html">BindingBase.initServiceExtensions</a>，在此处注册该服务扩展。</li>'
v = d.setdefault('foundation/FoundationServiceExtensions.html', {})
v['2'] = '<dd><p>调用后会使整个应用重新绘制的服务扩展名称。</p><p>另请参阅：</p><ul>' + reg + '</ul></dd>'
v['3'] = '<dd><p>调用后会终止 Flutter 应用的服务扩展名称。</p><p>另请参阅：</p><ul>' + reg + '</ul></dd>'
for i, name, info in [(4, 'connectedVmServiceUri', '存储已连接虚拟机服务协议的 URI'), (5, 'activeDevToolsServerAddress', '存储用于调试此应用的当前 DevTools 服务器地址')]:
 a = f'<a href="foundation/FoundationServiceExtensions.html">{name}</a>'
 v[str(i)] = f'<dd><p>调用后会获取或设置 {a} 值的服务扩展名称。</p><p>另请参阅：</p><ul><li>{a}，{info}。</li>{reg}</ul></dd>'
v['6'] = '<dd><p>调用后会更改 <a href="foundation/defaultTargetPlatform.html">defaultTargetPlatform</a> 值的服务扩展名称，该值控制框架针对哪个 <a href="foundation/TargetPlatform.html">TargetPlatform</a> 执行。</p><p>另请参阅：</p><ul><li><a href="foundation/debugDefaultTargetPlatformOverride.html">debugDefaultTargetPlatformOverride</a>，此服务扩展公开的标志。</li>' + reg + '</ul></dd>'
v['7'] = '<dd><p>调用后会覆盖平台 <a href="dart-ui/Brightness.html">Brightness</a> 的服务扩展名称。</p><p>另请参阅：</p><ul><li><a href="foundation/debugBrightnessOverride.html">debugBrightnessOverride</a>，此服务扩展公开的标志。</li>' + reg + '</ul></dd>'
v['8'] = d['foundation/DiagnosticsTreeStyle.html']['14']
v['9'] = '<dd>按声明顺序包含此枚举所有值的常量列表。</dd>'
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
