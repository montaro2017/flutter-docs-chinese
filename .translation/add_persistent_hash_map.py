from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'PersistentHashMap-class.html': [
 '<p>键值对集合，支持通过键高效检索值。</p>',
 '<p>此类实现了持久化映射：向映射添加新的键值对不会修改现有实例，而是创建一个新实例。</p>',
 '<p>与 <a href="dart-core/Map-class.html">Map</a> 不同，此类不支持将 <code>null</code> 用作键，并且仅实现框架核心中特定使用场景所需的功能。</p>',
 '<p>底层实现采用<em>哈希数组映射字典树（hash array mapped trie）</em>数据结构的一种变体，其节点经过压缩并使用位图索引。</p>',
 '<p>另请参阅：</p>'],
 'PersistentHashMap/operator_get.html': ['<p>返回与给定 <code>key</code> 关联的值；如果映射中不存在该 <code>key</code>，则返回 <code>null</code>。</p>'],
 'PersistentHashMap/PersistentHashMap.empty.html': ['<p>创建一个空哈希映射。</p>'],
 'PersistentHashMap/put.html': ['<p>如果此映射尚未包含给定 <code>key</code> 到 <code>value</code> 的映射，则创建映射的新版本，其中包含当前映射中的所有映射关系，以及给定 <code>key</code> 到 <code>value</code> 的映射。</p>'],
}
for page, blocks in pages.items():
 d['foundation/' + page] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/PersistentHashMap-class.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
d[page] = {}
for i, member in enumerate(('PersistentHashMap.empty', 'put', 'operator_get')):
 src = re.search(r'<p>(.*?)</p>', read_source(f'foundation/PersistentHashMap/{member}.html'), re.S)
 # The first paragraph outside the description can be UI text, so locate the description explicitly.
 desc = re.search(r'<section class="desc markdown">(.*?)</section>', read_source(f'foundation/PersistentHashMap/{member}.html'), re.S).group(1)
 src = re.search(r'<p>(.*?)</p>', desc, re.S).group(1)
 dst = pages[f'PersistentHashMap/{member}.html'][0][3:-4]
 assert src in blocks[i]
 d[page][str(i)] = blocks[i].replace(src, dst)
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
