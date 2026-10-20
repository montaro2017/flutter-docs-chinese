from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'TargetPlatform.html': [
 '<p>用户交互应适配的目标平台。</p>',
 '<p><a href="foundation/defaultTargetPlatform.html">defaultTargetPlatform</a> getter 返回当前平台。</p>',
 '<p>使用“flutter run”命令时，按“o”键会在更新 <a href="foundation/debugDefaultTargetPlatformOverride.html">debugDefaultTargetPlatformOverride</a> 时切换此枚举的值。这样无需切换模拟器或实体设备，就可以测试应用在不同平台上的表现。</p>'],
 'TargetPlatform/values-constant.html': ['<p>一个常量 List，按声明顺序包含此枚举的所有值。</p>'],
 'BitField-class.html': ['<p>基于枚举（或其他值实现了“index”的类）的位字段。</p>', '<p>只有枚举的前 62 个值可以用作索引。</p>', '<p>编译为 JavaScript 时，不支持此类。</p>'],
 'BitField/BitField.html': ['<p>创建一个所有位均为零的位字段。</p>', '<p>给定的长度最多为 62。</p>'],
 'BitField/BitField.filled.html': ['<p>创建一个用指定值填充的位字段。</p>', '<p>如果 value 参数为 true，则所有位填充为一。否则，所有位填充为零。</p>', '<p>给定的长度最多为 62。</p>'],
 'BitField/operator_get.html': ['<p>返回给定索引处的位是否为一。</p>'],
 'BitField/operator_put.html': ['<p>将给定索引处的位设置为给定值。</p>', '<p>如果 value 为 true，则将给定索引处的位设置为一。否则，将该位设置为零。</p>'],
 'BitField/reset.html': ['<p>将所有位设置为给定值。</p>', '<p>如果 value 为 true，则所有位均设置为一。否则，所有位均设置为零。默认将所有位设置为零。</p>'],
}
for page, blocks in pages.items():
 d['foundation/' + page] = {str(i): b for i, b in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/BitField-class.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
pairs = [
 ('Creates a bit field of all zeros.', '创建一个所有位均为零的位字段。'),
 ('Creates a bit field filled with a particular value.', '创建一个用指定值填充的位字段。'),
 ('Sets all the bits to the given value.', '将所有位设置为给定值。'),
 ('Returns whether the bit with the given index is set to one.', '返回给定索引处的位是否为一。'),
 ('Sets the bit with the given index to the given value.', '将给定索引处的位设置为给定值。'),
]
d[page] = {}
for i, (src, dst) in enumerate(pairs):
 assert src in blocks[i]
 d[page][str(i)] = blocks[i].replace(src, dst)
page = 'foundation/TargetPlatform.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
d[page] = {
 '8': blocks[8].replace('Available on ', '适用于 ').replace(',\n        provided by the ', '，\n        由 ').replace(' extension</span>', ' 扩展提供</span>').replace('The name of the enum value.', '枚举值的名称。').replace('no setter', '无 setter'),
 '9': blocks[9].replace('A constant List of the values in this enum, in order of their declaration.', '一个常量 List，按声明顺序包含此枚举的所有值。'),
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
