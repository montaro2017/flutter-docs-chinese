from pathlib import Path
import json, re
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
e = json.loads((r / 'translations-extra.json').read_text(encoding='utf-8'))
names = 'addBlankLineIfNoChildren afterDescription afterDescriptionIfBody afterName afterProperties beforeName beforeProperties bodyIndent childLinkSpace footer isBlankLineBetweenPropertiesAndChildren isNameOnOwnLine lineBreak lineBreakProperties linkCharacter mandatoryAfterProperties mandatoryFooter prefixLastChildLineOne prefixLineOne prefixOtherLines prefixOtherLinesRootNode propertyPrefixIfChildren propertyPrefixNoChildren propertySeparator showChildren suffixLineOne'.split()
for i, name in enumerate(names, 1):
 text = e['foundation/TextTreeConfiguration-class.html'][str(i)].split('<div')[0][4:]
 d[f'foundation/TextTreeConfiguration/{name}.html'] = {'0': '<p>' + text + '</p>'}
extras = {
 'addBlankLineIfNoChildren': '将此值设为 false 的示例，请参阅 <a href="foundation/denseTextConfiguration.html">denseTextConfiguration</a>。',
 'afterName': '使用非冒号值实现自定义字符线条样式的示例，请参阅 <a href="foundation/transitionTextConfiguration.html">transitionTextConfiguration</a>。',
 'afterProperties': '请参阅 <a href="foundation/TextTreeConfiguration/beforeProperties.html">beforeProperties</a> 的文档。',
 'beforeName': '使用此字段实现自定义字符线条样式的示例，请参阅 <a href="foundation/errorTextConfiguration.html">errorTextConfiguration</a>。',
 'beforeProperties': '仅当节点具有属性时显示。使用此字段将属性列表括在圆括号中的示例，请参阅 <a href="foundation/singleLineTextConfiguration.html">singleLineTextConfiguration</a>。',
 'bodyIndent': '主体是节点中除名称和描述之外的全部内容。',
 'footer': '使用页脚在节点周围绘制边框的示例，请参阅 <a href="foundation/transitionTextConfiguration.html">transitionTextConfiguration</a>。<a href="foundation/TextTreeConfiguration/footer.html">footer</a> 的缩进量与 <a href="foundation/TextTreeConfiguration/prefixOtherLines.html">prefixOtherLines</a> 相同。',
 'lineBreak': "通常保留默认值 '\\n'，除非此样式需要以不同方式处理行，例如 <a href=\"foundation/singleLineTextConfiguration.html\">singleLineTextConfiguration</a>。",
 'linkCharacter': '第一个子节点不需要连接线，但后续所有子节点都需要，连接线紧靠前一个兄弟节点的左边缘之前绘制。',
 'prefixOtherLines': '<a href="foundation/TextTreeConfiguration/prefixOtherLines.html">prefixOtherLines</a> 通常应比 <a href="foundation/TextTreeConfiguration/prefixLineOne.html">prefixLineOne</a> 短一个字符。',
 'propertyPrefixIfChildren': '作用类似于 <a href="foundation/TextTreeConfiguration/linkCharacter.html">linkCharacter</a>，但某些配置会有意使用与 <a href="foundation/TextTreeConfiguration/linkCharacter.html">linkCharacter</a> 不同的线条样式。',
 'propertyPrefixNoChildren': '此字符串通常由空白字符组成，长度与 <a href="foundation/TextTreeConfiguration/propertyPrefixIfChildren.html">propertyPrefixIfChildren</a> 相同，但也可以采用不同长度。',
 'propertySeparator': '使用此字段将属性渲染为逗号分隔列表的示例，请参阅 <a href="foundation/singleLineTextConfiguration.html">singleLineTextConfiguration</a>。',
 'showChildren': '使用此字段隐藏节点所有子节点的示例，请参阅 <a href="foundation/singleLineTextConfiguration.html">singleLineTextConfiguration</a>。',
}
for name, text in extras.items():
 d[f'foundation/TextTreeConfiguration/{name}.html']['1'] = '<p>' + text + '</p>'
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
