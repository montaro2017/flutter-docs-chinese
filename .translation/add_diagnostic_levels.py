from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticLevel.html'] = {
 '0': '<p>用于筛选显示或省略哪些诊断信息的各种优先级。</p>',
 '1': '<p>Flutter 诊断树可能非常庞大，因此筛选显示的诊断信息很重要。通常适合仅显示级别至少为 <a href="foundation/DiagnosticLevel.html">debug</a> 的诊断信息。</p>',
 '2': '<p>在发布模式下，此级别可能不起作用，因为发布模式中的诊断信息会被压缩或截断，以减少二进制文件的体积。</p>',
}
d['foundation/DiagnosticLevel/values-constant.html'] = {'0': '<p>一个常量 List，按声明顺序包含此枚举的所有值。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/DiagnosticLevel.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
paragraphs = {
 2: ['<p>不应显示的诊断信息。</p>', '<p>如果用户选择显示 <a href="foundation/DiagnosticLevel.html">hidden</a> 诊断信息，就不应期望其格式与其他诊断信息一致，并且应预期它们有时可能产生误导。例如，当属性 <code>value</code> 与具有自定义标志描述的值不匹配时，<a href="foundation/FlagProperty-class.html">FlagProperty</a> 和 <a href="foundation/ObjectFlagProperty-class.html">ObjectFlagProperty</a> 的格式会较为难看。可能产生误导的一个例子是：对象的其他属性设置导致某个隐藏属性不起作用，但仍显示该属性的诊断信息。</p>'],
 3: ['<p>可能价值较低，但显示质量与更高级别诊断信息同样良好的诊断信息。</p>', '<p>对于值与默认值相同的诊断属性，以及显示诊断信息不会增加太多价值的其他情况，应使用此级别。例如，值为空的 <a href="foundation/IterableProperty-class.html">IterableProperty</a>。</p>'],
 4: ['<p>仅在对对象进行细致调试时才应显示的诊断信息。</p>', '<p>与 <a href="foundation/DiagnosticLevel.html">fine</a> 诊断信息不同，这些诊断信息提供了调试时可能需要的对象重要信息。适用于重要但属性值过于冗长（例如超过 300 个字符）、不适合以更高级别显示的属性。</p>'],
 5: ['<p>通常应显示的有用诊断信息。</p>'],
 6: ['<p>表明属性值存在问题的非常重要的诊断信息。</p>', '<p>例如，如果你会将属性描述消息全部用大写字母书写，就可以使用此级别。</p>'],
 7: ['<p>提供最佳实践提示的诊断信息。</p>', '<p>例如，描述修复错误的最佳实践的诊断信息。</p>'],
 8: ['<p>概括其他现有诊断信息的诊断信息。</p>', '<p>例如，用此级别提供一两行简短摘要，描述其他现有诊断信息。</p>'],
 9: ['<p>表明错误或意外情况的诊断信息。</p>', '<p>例如，可用于计算属性值时抛出异常的情况。</p>'],
 10: ['<p>表示不应显示任何诊断信息的特殊级别。</p>', '<p>不要为诊断信息指定此级别。此级别仅用于筛选要显示的诊断信息。</p>'],
}
entries = {}
for i, targets in paragraphs.items():
 originals = re.findall(r'<p>.*?</p>', blocks[i], re.S)
 assert len(originals) == len(targets)
 translated = blocks[i]
 for src, dst in zip(originals, targets):
  translated = translated.replace(src, dst, 1)
 entries[str(i)] = translated
entries['11'] = blocks[11].replace('Available on ', '适用于 ').replace(',\n        provided by the ', '，\n        由 ').replace(' extension</span>', ' 扩展提供</span>').replace('The name of the enum value.', '枚举值的名称。').replace('no setter', '无 setter')
entries['12'] = blocks[12].replace('A constant List of the values in this enum, in order of their declaration.', '一个常量 List，按声明顺序包含此枚举的所有值。')
d[page] = entries
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
