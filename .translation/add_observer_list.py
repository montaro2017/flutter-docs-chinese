from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/ObserverList-class.html'] = {
 '0': '<p>针对观察者数量较少时的观察者模式优化的列表。</p>',
 '1': '<p>当 <a href="foundation/ObserverList/contains.html">contains</a> 的调用次数远多于 <a href="foundation/ObserverList/add.html">add</a> 和 <a href="foundation/ObserverList/remove.html">remove</a> 的调用次数时，可以考虑使用 <a href="foundation/ObserverList-class.html">ObserverList</a> 替代 <a href="dart-core/List-class.html">List</a>。</p>',
 '2': '<p>此类的 <a href="foundation/ObserverList/iterator.html">iterator</a> 会按添加顺序返回每个元素；一个元素添加了多少次，就会返回多少次。</p>',
 '3': '<p>如果观察者数量较多，可以考虑改用 <a href="foundation/HashedObserverList-class.html">HashedObserverList</a>。它的迭代语义略有不同，但用途相似，并且在观察者较多时更高效。</p>',
 '4': '<p>另请参阅：</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/ObserverList-class.html'] = [{
 'source': '<li><a href="foundation/HashedObserverList-class.html">HashedObserverList</a> for a list that is optimized for larger numbers of\nobservers.</li>',
 'translation': '<li><a href="foundation/HashedObserverList-class.html">HashedObserverList</a>，针对较多观察者优化的列表。</li>',
}]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
