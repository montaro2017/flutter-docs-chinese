from pathlib import Path
import json,re
from case_paths import read_source
r = Path(__file__).resolve().parent
p=r/'translations.json'
d=json.loads(p.read_text(encoding='utf-8'))
for member in ['level','valueToString','toJsonMap']:
 source=f'foundation/FlagProperty/{member}.html'
 target=f'foundation/DiagnosticsProperty/{member}.html'
 def section(page):
  return re.search(r'<section class="desc markdown">(.*?)</section>',read_source(page),re.S).group(1)
 assert section(target).replace('DiagnosticsProperty/'+member,'FlagProperty/'+member)==section(source).replace('DiagnosticsProperty/'+member,'FlagProperty/'+member)
 d[target]={k:v.replace('FlagProperty/', 'DiagnosticsProperty/') for k,v in d[source].items()}
p.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
p=r/'translations-fragments.json'
d=json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsProperty/toJsonMap.html']=d['foundation/FlagProperty/toJsonMap.html'].copy()
p.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
