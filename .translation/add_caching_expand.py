from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/CachingIterable/expand.html'] = {
 '0': '<p>将此 <a href="dart-core/Iterable-class.html">Iterable</a> 的每个元素展开为零个或多个元素。</p>',
 '1': '<p>生成的 Iterable 按当前对象的迭代顺序，依次遍历对每个元素调用 <code>toElements</code> 所返回的元素。</p>',
 '2': '<p>返回的 <a href="dart-core/Iterable-class.html">Iterable</a> 是惰性的。每次遍历返回的对象时，都会为当前可迭代对象的每个元素调用 <code>toElements</code>。</p>',
 '3': '<p>示例：</p>',
 '4': '<p>等价于：</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
