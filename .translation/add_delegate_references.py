from pathlib import Path
import json, re
from case_paths import read_source
p = Path(__file__).resolve().parent / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
descriptions = {'subtreeDepth': '提供筛选将包含的子节点的方法。', 'includeProperties': '提供筛选将包含的属性的方法。', 'filterChildren': '控制序列化结果中包含多少层子节点。', 'filterProperties': '控制是否包含属性。'}
for member, description in descriptions.items():
 page = f'foundation/DiagnosticsSerializationDelegate/{member}.html'
 section = re.search(r'<section class="desc markdown">(.*?)</section>', read_source(page), re.S).group(1)
 source = re.search(r'<li>.*?</li>', section, re.S).group(0)
 link = re.search(r'<a\b[^>]*>.*?</a>', source, re.S).group(0)
 d[page] = [{'source': source, 'translation': '<li>' + link + '，' + description + '</li>'}]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
