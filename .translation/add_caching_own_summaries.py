from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
translations = json.loads((r / 'translations.json').read_text(encoding='utf-8'))
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/CachingIterable-class.html'
summaries = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
entries = d.setdefault(page, {})
for member in ['CachingIterable', 'iterator', 'length', 'elementAt', 'expand', 'map', 'skip', 'skipWhile', 'take', 'takeWhile', 'toList', 'where']:
 source = read_source(f'foundation/CachingIterable/{member}.html')
 section = re.search(r'<section class="desc markdown">(.*?)</section>', source, re.S).group(1)
 first = re.search(r'<p>(.*?)</p>', section, re.S).group(1)
 translated = translations[f'foundation/CachingIterable/{member}.html']['0'][3:-4]
 matches = [(i, s) for i, s in enumerate(summaries) if first in s]
 assert len(matches) == 1, member
 i, summary = matches[0]
 entries[str(i)] = summary.replace(first, translated).replace('>override<', '>重写<').replace('>no setter<', '>无 setter<')
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
