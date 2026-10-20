from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'DiagnosticPropertiesBuilder-class.html': '<p>用于收集属性和配置的构建器，以便从 <a href="foundation/Diagnosticable-mixin.html">Diagnosticable</a> 对象构建 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a>。</p>',
 'DiagnosticPropertiesBuilder/add.html': '<p>向属性列表添加一个属性。</p>',
 'DiagnosticPropertiesBuilder/defaultDiagnosticsTreeStyle.html': '<p>未指定样式时，<a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 使用的默认样式。</p>',
 'DiagnosticPropertiesBuilder/DiagnosticPropertiesBuilder.fromProperties.html': '<p>使用给定的 <code>properties</code> 创建一个 <a href="foundation/DiagnosticPropertiesBuilder-class.html">DiagnosticPropertiesBuilder</a>。</p>',
 'DiagnosticPropertiesBuilder/DiagnosticPropertiesBuilder.html': '<p>创建一个 <a href="foundation/DiagnosticPropertiesBuilder-class.html">DiagnosticPropertiesBuilder</a>，并将 <a href="foundation/DiagnosticPropertiesBuilder/properties.html">properties</a> 初始化为空数组。</p>',
 'DiagnosticPropertiesBuilder/emptyBodyDescription.html': '<p>节点没有显示的属性或子节点时，要显示的描述。</p>',
 'DiagnosticPropertiesBuilder/properties.html': '<p>目前已收集的属性列表。</p>',
}
for page, text in pages.items():
 d['foundation/' + page] = {'0': text}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/DiagnosticPropertiesBuilder-class.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
members = ('DiagnosticPropertiesBuilder', 'DiagnosticPropertiesBuilder.fromProperties', 'defaultDiagnosticsTreeStyle', 'emptyBodyDescription', 'properties', 'add')
entries = {}
for i, member in enumerate(members):
 member_page = f'DiagnosticPropertiesBuilder/{member}.html'
 desc = re.search(r'<section class="desc markdown">(.*?)</section>', read_source('foundation/' + member_page), re.S).group(1)
 source = re.search(r'<p>(.*?)</p>', desc, re.S).group(1)
 assert source in blocks[i]
 entries[str(i)] = blocks[i].replace(source, pages[member_page][3:-4]).replace('getter/setter pair', 'getter/setter 对')
d[page] = entries
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
