from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/HashedObserverList-class.html'] = {
 '0': '<p>针对观察者数量较多时的观察者模式优化的列表。</p>',
 '1': '<p>当观察者数量较少时（例如少于 10 个），请改用 <a href="foundation/ObserverList-class.html">ObserverList</a>。</p>',
 '2': '<p>此类的迭代语义与 <a href="foundation/ObserverList-class.html">ObserverList</a> 略有不同。无论某个元素被添加了多少次，此类的 <a href="foundation/HashedObserverList/iterator.html">iterator</a> 都只会返回该元素一次。不过，必须移除该元素与添加时相同的次数，它才会停止出现在 <a href="foundation/HashedObserverList/iterator.html">iterator</a> 中。元素按首次添加的顺序返回。</p>',
 '3': '<p>另请参阅：</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/HashedObserverList-class.html'] = [{
 'source': '<li><a href="foundation/ObserverList-class.html">ObserverList</a> for a list that is fast for small numbers of observers.</li>',
 'translation': '<li><a href="foundation/ObserverList-class.html">ObserverList</a>，适用于少量观察者的高效列表。</li>',
}]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
