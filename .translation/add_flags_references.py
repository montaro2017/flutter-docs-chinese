from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
pairs = {
 'foundation/FlagsSummary-class.html': [
 ('<li><a href="foundation/ObjectFlagProperty-class.html">ObjectFlagProperty</a>, which provides similar functionality but accepts\nonly one flag, and is preferred if there is only one entry.</li>', '<li><a href="foundation/ObjectFlagProperty-class.html">ObjectFlagProperty</a>，提供类似功能，但只接受一个标志；如果只有一个条目，应优先使用它。</li>'),
 ('<li><a href="foundation/IterableProperty-class.html">IterableProperty</a>, which provides similar functionality describing\nthe values a collection of objects.</li>', '<li><a href="foundation/IterableProperty-class.html">IterableProperty</a>，提供类似功能，用于描述对象集合中的值。</li>')],
 'foundation/FlagsSummary/value.html': [('<li><a href="foundation/FlagsSummary/valueToString.html">valueToString</a>, which converts the property value to a string.</li>', '<li><a href="foundation/FlagsSummary/valueToString.html">valueToString</a>，将属性值转换为字符串。</li>')],
 'foundation/FlagsSummary/toJsonMap.html': [('<li><a href="widgets/WidgetInspectorService-mixin.html">WidgetInspectorService</a>, which forms the bridge between JSON returned\nby this method and interactive tree views in the Flutter IntelliJ\nplugin.</li>', '<li><a href="widgets/WidgetInspectorService-mixin.html">WidgetInspectorService</a>，连接此方法返回的 JSON 与 Flutter IntelliJ 插件中的交互式树视图。</li>')],
}
for page, entries in pairs.items():
 d[page] = [{'source': src, 'translation': dst} for src, dst in entries]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
