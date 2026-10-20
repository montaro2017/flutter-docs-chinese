from pathlib import Path
import json
from case_paths import read_source
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
f = json.loads((r / 'translations-fragments.json').read_text(encoding='utf-8'))
for cls in ['ErrorSummary', 'ErrorDescription', 'ErrorHint']:
 for member in ['value', 'toString', 'valueToString']:
  page = f'foundation/{cls}/{member}.html'
  if cls != 'ErrorSummary':
   import re
   def section(s):
    return re.search(r'<section class="desc markdown">(.*?)</section>', s, re.S).group(1)
   assert section(read_source(page)).replace(cls, 'ErrorSummary') == section(read_source(f'foundation/ErrorSummary/{member}.html'))
 d[f'foundation/{cls}/value.html'] = {
  '0': '<p>从缓存中返回属性值，或通过调用 <a href="foundation/ComputePropertyValueCallback.html">ComputePropertyValueCallback</a> 获取属性值。</p>',
  '1': '<p>如果调用 <a href="foundation/ComputePropertyValueCallback.html">ComputePropertyValueCallback</a> 时抛出异常，<code>value</code> 返回 null，抛出的异常可通过 <a href="foundation/DiagnosticsProperty/exception.html">exception</a> 属性获取。</p>',
  '2': '<p>另请参阅：</p>',
 }
 d[f'foundation/{cls}/toString.html'] = {
  '0': '<p>返回此诊断信息的字符串表示；如果节点不是根节点，则该表示与父节点的样式兼容。</p>',
  '1': f'<p><code>parentConfiguration</code> 指定父节点如何渲染为字符图。例如，如果父节点将所有属性放在同一行，则每个属性的 <a href="foundation/{cls}/toString.html">toString</a> 应尽可能避免换行。</p>',
  '2': '<p><code>minLevel</code> 指定输出中包含的属性所需达到的最低 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel</a>。</p>',
  '3': '<p>在发布模式下，保留的信息会少得多，某些信息可能完全不会输出。</p>',
 }
 d[f'foundation/{cls}/valueToString.html'] = {
  '0': '<p>返回属性值的字符串表示。</p>',
  '1': '<p>子类应重写此方法，而不是 <a href="foundation/DiagnosticsProperty/toDescription.html">toDescription</a>，以自定义属性值转换为字符串的方式。</p>',
  '2': f'<p>重写此方法可确保各个实现以一致的方式修饰属性值，生成易读的 <a href="foundation/DiagnosticsProperty/toDescription.html">toDescription</a>。调试工具也可以选择直接使用 <a href="foundation/{cls}/valueToString.html">valueToString</a>，而不使用 <a href="foundation/DiagnosticsProperty/toDescription.html">toDescription</a>。</p>',
  '3': '<p><code>parentConfiguration</code> 指定父节点如何渲染为字符图。例如，如果父节点将所有属性放在同一行，则属性值应尽可能不换行地显示。</p>',
 }
 f[f'foundation/{cls}/value.html'] = [{
  'source': f'<li><a href="foundation/{cls}/valueToString.html">valueToString</a>, which converts the property value to a string.</li>',
  'translation': f'<li><a href="foundation/{cls}/valueToString.html">valueToString</a>，将属性值转换为字符串。</li>',
 }]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(r / 'translations-fragments.json').write_text(json.dumps(f, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
