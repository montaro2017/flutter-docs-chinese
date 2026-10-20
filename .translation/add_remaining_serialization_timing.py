from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
for cls in ['IntProperty', 'DoubleProperty']:
 d[f'foundation/{cls}/toJsonMap.html'] = {
  '0': '<p>根据 <a href="foundation/DiagnosticsSerializationDelegate-class.html">DiagnosticsSerializationDelegate</a> 提供的配置，将节点序列化为 JSON 映射。</p>',
  '1': '<p>如果子类具有其他属性，且这些属性对使用此 JSON 的图形界面工具有用，则应重写此方法。</p>',
  '2': '<p>另请参阅：</p>',
 }
for cls in ['TimedBlock', 'AggregatedTimedBlock']:
 d[f'foundation/{cls}/toString.html'] = {
  '0': '<p>此对象的字符串表示。</p>',
  '1': '<p>某些类具有默认的文本表示，通常还配有静态 <code>parse</code> 函数（例如 <a href="dart-core/int/parse.html">int.parse</a>）。这些类会将该文本表示作为自身的字符串表示。</p>',
  '2': '<p>其他类没有程序会关注的、有意义的文本表示。这类对象通常会重写 <code>toString</code>，以便在检查对象时提供有用的信息，主要用于调试或日志记录。</p>',
 }
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
for cls in ['IntProperty', 'DoubleProperty']:
 d[f'foundation/{cls}/toJsonMap.html'] = [{
  'source': '<li><a href="widgets/WidgetInspectorService-mixin.html">WidgetInspectorService</a>, which forms the bridge between JSON returned\nby this method and interactive tree views in the Flutter IntelliJ\nplugin.</li>',
  'translation': '<li><a href="widgets/WidgetInspectorService-mixin.html">WidgetInspectorService</a>，在此方法返回的 JSON 与 Flutter IntelliJ 插件中的交互式树视图之间建立桥梁。</li>',
 }]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
