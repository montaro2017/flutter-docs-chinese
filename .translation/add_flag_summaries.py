from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
v = d.setdefault('foundation/FlagProperty-class.html', {})
flags = {1:'',2:'final',3:'final',4:'无 setter|重写',5:'无 setter|重写',6:'重写',7:'重写'}
texts = {
 1:'使用给定描述构造 FlagProperty。',
 2:'属性值为 false 时使用的描述。',
 3:'属性的 <a href="foundation/DiagnosticsProperty/value.html">value</a> 为 true 时使用的描述。',
 4:'诊断信息的优先级，用于控制哪些诊断信息应显示或被过滤。',
 5:'显示树的默认视图时是否显示属性名称。',
 6:'根据 <a href="foundation/DiagnosticsSerializationDelegate-class.html">DiagnosticsSerializationDelegate</a> 提供的配置，将节点序列化为 JSON 映射。',
 7:'返回属性值的字符串表示。',
}
for i,t in texts.items():
 f = '<div class="features">' + ''.join('<span class="feature">'+x+'</span>' for x in flags[i].split('|')) + '</div>' if flags[i] else ''
 v[str(i)] = '<dd>' + t + f + '</dd>'
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/FlagProperty-class.html'].append({'source':'<li><a href="foundation/ObjectFlagProperty-class.html">ObjectFlagProperty</a>, which provides similar behavior describing whether\na <a href="foundation/DiagnosticsProperty/value.html">value</a> is null.</li>', 'translation':'<li><a href="foundation/ObjectFlagProperty-class.html">ObjectFlagProperty</a>，提供类似行为，用于描述 <a href="foundation/DiagnosticsProperty/value.html">value</a> 是否为 null。</li>'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
