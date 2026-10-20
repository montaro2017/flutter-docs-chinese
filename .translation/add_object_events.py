from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
map_text = '以不依赖 Flutter 的纯 Dart 库可以接受的形式表示此事件。'
pages = {
 'ObjectEvent-class.html': ['<p>对象的生命周期事件。</p>'],
 'ObjectCreated-class.html': ['<p>描述对象创建的事件。</p>'],
 'ObjectDisposed-class.html': ['<p>描述对象释放的事件。</p>'],
 'ObjectEvent/object.html': ['<p>对该对象的引用。</p>', '<p>不应将此引用保存在任何长期存活的位置，否则会阻止垃圾回收。</p>'],
 'ObjectCreated/className.html': ['<p>被监测类的名称。</p>'],
 'ObjectCreated/library.html': ['<p>被监测库的名称。</p>', '<p>此参数应采用库 URI 的格式。例如：<code>\'package:flutter/rendering.dart\'</code>。</p>'],
}
for cls in ('ObjectEvent', 'ObjectCreated', 'ObjectDisposed'):
 pages[f'{cls}/{cls}.html'] = [f'<p>创建一个 <a href="foundation/{cls}-class.html">{cls}</a> 实例。</p>']
 pages[f'{cls}/toMap.html'] = [f'<p>{map_text}</p>', '<p>此方法支持编写如下代码：</p>']
for page, blocks in pages.items():
 d['foundation/' + page] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
mapping = {
 'Reference to the object.': '对该对象的引用。',
 'Name of the instrumented class.': '被监测类的名称。',
 'Name of the instrumented library.': '被监测库的名称。',
 'The representation of the event in a form, acceptable by a\npure dart library, that cannot depend on Flutter.': map_text,
}
for cls in ('ObjectEvent', 'ObjectCreated', 'ObjectDisposed'):
 page = f'foundation/{cls}-class.html'
 blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
 pairs = dict(mapping)
 pairs[f'Creates an instance of <a href="foundation/{cls}-class.html">{cls}</a>.'] = f'创建一个 <a href="foundation/{cls}-class.html">{cls}</a> 实例。'
 entries = {}
 for i, block in enumerate(blocks):
  translated = block
  for source, target in pairs.items():
   translated = translated.replace(source, target)
  if translated != block:
   entries[str(i)] = translated.replace('>override<', '>重写<')
 d[page] = entries
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
