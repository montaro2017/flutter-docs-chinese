from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/EnumProperty-class.html'] = {'0': '<p>以 <a href="dart-core/Enum-class.html">Enum</a> 为值的 <a href="foundation/DiagnosticsProperty-class.html">DiagnosticsProperty</a>。</p>', '1': '<p>显示枚举值时会去掉枚举类型名。例如，<a href="rendering/HitTestBehavior.html">HitTestBehavior.deferToChild</a> 显示为 <code>deferToChild</code>。</p>', '2': '<p>此类可用于枚举，并返回枚举的 name getter。也可用于可空属性；空值表示为 <code>null</code>。</p>', '3': '<p>另请参阅：</p>'}
d['foundation/EnumProperty/EnumProperty.html'] = {'0': '<p>创建一个显示枚举值的诊断属性。</p>', '1': '<p><code>level</code> 参数也不能为 null。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/EnumProperty-class.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
d[page] = {'1': blocks[1].replace('Create a diagnostics property that displays an enum.', '创建一个显示枚举值的诊断属性。'), '2': blocks[2].replace('Returns a string representation of the property value.', '返回属性值的字符串表示。').replace('>override<', '>重写<')}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
