from pathlib import Path
import json,re
from case_paths import read_source
r = Path(__file__).resolve().parent
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
t = json.loads((r/'translations.json').read_text(encoding='utf-8'))
v = d.setdefault('foundation/ObjectFlagProperty-class.html', {})
for i, member in [(1,'ObjectFlagProperty'),(2,'ObjectFlagProperty.has'),(3,'ifPresent')]:
 text = t[f'foundation/ObjectFlagProperty/{member}.html']['0'][3:-4]
 flag = '<div class="features"><span class="feature">final</span></div>' if i == 3 else ''
 v[str(i)] = '<dd>' + text + flag + '</dd>'
for i in range(4,8):
 v[str(i)] = d['foundation/FlagProperty-class.html'][str(i)]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1)+'\n', encoding='utf-8')
p = r/'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/ObjectFlagProperty-class.html'
section = re.search(r'<section class="desc markdown">(.*?)</section>',read_source(page),re.S).group(1)
sources = re.findall(r'<li>.*?</li>',section,re.S)
texts = [
 '<li><a href="foundation/FlagsSummary-class.html">FlagsSummary</a>，提供类似功能，但接受同一名称下的多个标志。如果多个此类值可归入同一类别（例如“listeners”），应优先使用它。</li>',
 '<li><a href="foundation/FlagProperty-class.html">FlagProperty</a>，提供类似功能，用于描述 <a href="foundation/DiagnosticsProperty/value.html">value</a> 为 true 还是 false。</li>',
]
assert len(sources)==2
d[page]=[{'source':a,'translation':b} for a,b in zip(sources,texts)]
p.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
