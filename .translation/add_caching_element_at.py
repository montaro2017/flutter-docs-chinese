from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/CachingIterable/elementAt.html'] = {
 '0': '<p>返回索引为 <code>index</code> 的元素。</p>',
 '1': '<p><code>index</code> 必须非负且小于 <a href="foundation/CachingIterable/length.html">length</a>。索引零表示第一个元素，因此 <code>iterable.elementAt(0)</code> 等价于 <code>iterable.first</code>。</p>',
 '2': '<p>可能按迭代顺序遍历元素，忽略前 <code>index</code> 个元素，再返回下一个元素。某些可迭代对象可能有更高效的元素查找方式。</p>',
 '3': '<p>示例：</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
