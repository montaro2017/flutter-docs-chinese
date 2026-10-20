from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'Factory-class.html': {'0': '<p>一个工厂接口，同时报告所创建对象的类型。</p>'},
 'Factory/Factory.html': {'0': '<p>创建一个新工厂。</p>'},
 'Factory/constructor.html': {'0': '<p>创建一个类型为 T 的新对象。</p>'},
 'Factory/type.html': {'0': '<p>此工厂创建的对象的类型。</p>'},
 'Category-class.html': {
 '0': '<p>用于为类添加文档分类的注解。</p>',
 '1': '<p>分类通常由一个一级分类和一个二级分类表示，两者都是字符串。类所属库的工程团队负责定义该库中各类使用的分类。例如，Flutter 工程团队为 Flutter 组件定义了“Basic/Buttons”和“Material Design/Buttons”等分类。</p>',
 '2': '<p>一个类可以属于多个分类。</p>',
 '4': '<p>另请参阅：</p>'},
 'Category/Category.html': {'0': '<p>创建一个注解，用于为类提供分类。</p>'},
 'Category/sections.html': {'0': '<p>与此对象所表示分类的一级分类和二级分类对应的字符串。</p>', '1': '<p>按照惯例，此列表通常包含两个元素。允许使用的值由被注解类所属库的团队定义。</p>'},
 'Summary-class.html': {'0': '<p>为类提供简短描述、供索引使用的注解。</p>', '1': '<p>通常可以使用类文档的第一段作为摘要，但有时第一段过短或过长，无法在脱离文档其余内容时单独使用。</p>', '3': '<p>另请参阅：</p>'},
 'Summary/Summary.html': {'0': '<p>创建一个注解，用于为类提供简短描述。</p>'},
 'Summary/text.html': {'0': '<p>被注解类的摘要文本。</p>'},
 'DocumentationIcon-class.html': {'0': '<p>为类提供代表该类的图片 URL 的注解。</p>', '1': '<p>每个类应只有一个 <a href="foundation/DocumentationIcon-class.html">DocumentationIcon</a>。</p>', '3': '<p>另请参阅：</p>'},
 'DocumentationIcon/DocumentationIcon.html': {'0': '<p>创建一个注解，用于提供描述某个类的图片 URL。</p>'},
 'DocumentationIcon/url.html': {'0': '<p>代表被注解类的图片 URL。</p>'},
}
for page, blocks in pages.items():
 d['foundation/' + page] = blocks
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
icon = {'source': '<li><a href="foundation/DocumentationIcon-class.html">DocumentationIcon</a>, which is used to give the URL to an image that\nrepresents the class.</li>', 'translation': '<li><a href="foundation/DocumentationIcon-class.html">DocumentationIcon</a>，用于提供代表该类的图片 URL。</li>'}
d['foundation/Category-class.html'] = [icon, {'source': '<li><a href="foundation/Summary-class.html">Summary</a>, which is used to provide a one-line description of a\nclass that overrides the inline documentations\' own description.</li>', 'translation': '<li><a href="foundation/Summary-class.html">Summary</a>，用于提供类的单行描述，以替代内联文档本身的描述。</li>'}]
d['foundation/Summary-class.html'] = [{'source': '<li><a href="foundation/Category-class.html">Category</a>, to help place the class in an index.</li>', 'translation': '<li><a href="foundation/Category-class.html">Category</a>，帮助将类归入索引中的相应分类。</li>'}, icon]
d['foundation/DocumentationIcon-class.html'] = [d['foundation/Summary-class.html'][0], d['foundation/Category-class.html'][1]]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
