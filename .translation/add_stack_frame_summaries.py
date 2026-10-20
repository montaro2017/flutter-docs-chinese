from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
translations = json.loads((r / 'translations.json').read_text(encoding='utf-8'))
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/StackFrame-class.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
members = {1:'StackFrame', 2:'className', 3:'column', 5:'isConstructor', 6:'line', 7:'method', 8:'number', 9:'package', 10:'packagePath', 11:'packageScheme', 12:'source', 15:'fromStackString', 16:'fromStackTrace', 17:'fromStackTraceLine', 18:'asynchronousSuspension-constant', 19:'stackOverFlowElision-constant'}
entries = {}
for i, member in members.items():
 member_page = f'foundation/StackFrame/{member}.html'
 desc = re.search(r'<section class="desc markdown">(.*?)</section>', read_source(member_page), re.S).group(1)
 source = re.search(r'<p>(.*?)</p>', desc, re.S).group(1)
 assert source in blocks[i]
 entries[str(i)] = blocks[i].replace(source, translations[member_page]['0'][3:-4])
for i, src, dst in ((4,'The hash code for this object.','此对象的哈希码。'), (13,'A string representation of this object.','此对象的字符串表示。'), (14,'The equality operator.','相等运算符。')):
 entries[str(i)] = blocks[i].replace(src, dst).replace('no setter', '无 setter').replace('>override<', '>重写<')
d[page] = entries
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
