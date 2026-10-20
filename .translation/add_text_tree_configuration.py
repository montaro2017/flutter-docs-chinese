from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/TextTreeConfiguration-class.html'] = {
 '0': '<p>指定如何将特定 <a href="foundation/DiagnosticsTreeStyle.html">DiagnosticsTreeStyle</a> 渲染为字符图的配置。</p>',
 '1': '<p>在发布模式下，这些配置可能被忽略，因为诊断信息会被压缩或截断，以减小二进制文件大小。</p>',
 '2': '<p>另请参阅：</p>',
}
d['foundation/TextTreeConfiguration/TextTreeConfiguration.html'] = {'0': '<p>创建一个配置对象，描述如何将树渲染为文本。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
texts = [
 '如果节点没有子节点，是否在其输出末尾添加空行。',
 '紧接在具有属性和／或子节点的节点的描述行后添加的文本。',
 '如果节点具有主体，紧接在具有属性和／或子节点的节点的描述行后添加的文本。',
 '紧接在节点名称后添加的文本。',
 '在节点属性后添加的可选字符串。',
 '紧接在节点名称前添加的文本。',
 '在节点属性前添加的可选字符串。',
 '添加到树节点主体所有行前的前缀。',
 '当此节点是其父节点的最后一个子节点、不需要连接线时，代替 childLink 字符绘制的空白字符。',
 '在非根节点末尾单独占一行的页脚。',
 '如果属性和子节点同时存在，在两者之间添加空行。',
 '名称是否应与描述显示在同一行。',
 '用于分隔行的字符。',
 '是否在属性之间换行，或将所有属性保留在同一行。',
 '用于绘制父子节点连接线的字符。',
 '无论节点是否具有属性，都必须在其属性后添加的字符串。',
 '即使对于根节点也要添加的页脚。',
 '使用此样式显示节点的最后一个子节点时，添加到首行的前缀。',
 '使用此样式显示子节点时，添加到首行的前缀。',
 '使用此样式显示子节点时，添加到其他行的前缀。',
 '如果节点是树的根节点，添加到该节点其他行的额外前缀。',
 '如果节点具有子节点，在每个属性前添加的前缀。',
 '如果节点没有子节点，在每个属性前添加的前缀。',
 '添加到属性之间的属性分隔符。',
 '是否显示节点的子节点。',
 '添加到首行末尾、使其长度与页脚一致的后缀。',
]
v = d.setdefault('foundation/TextTreeConfiguration-class.html', {})
v['0'] = '<dd>创建一个配置对象，描述如何将树渲染为文本。</dd>'
for i, text in enumerate(texts, 1):
 v[str(i)] = '<dd>' + text + '<div class="features"><span class="feature">final</span></div></dd>'
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
