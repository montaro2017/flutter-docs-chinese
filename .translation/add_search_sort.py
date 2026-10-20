from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/binarySearch.html': {
 '0': '<p>如果 <code>value</code> 存在于 <code>sortedList</code> 中，返回它的位置。</p>',
 '1': '<p>如果 <code>value</code> 不在列表中，则返回 <code>-1</code>。列表元素必须实现 <a href="dart-core/Comparable-class.html">Comparable</a>，且 <code>sortedList</code> 必须已经排序。</p>',
 },
 'foundation/mergeSort.html': {
 '0': '<p>使用归并排序算法，对列表中从 <code>start</code>（包含）到 <code>end</code>（不包含）的范围进行排序。</p>',
 '1': '<p>如果省略 <code>compare</code>，默认调用对象的 <a href="dart-core/Comparable/compareTo.html">Comparable.compareTo</a>。如果任何对象未实现 <a href="dart-core/Comparable-class.html">Comparable</a>，会抛出 <a href="dart-core/TypeError-class.html">TypeError</a>。堆栈跟踪可能将其称为 <code>_CastError</code> 或 <code>_TypeError</code>，但捕获时应使用 <a href="dart-core/TypeError-class.html">TypeError</a>。</p>',
 '2': '<p>归并排序将任务分为两部分，分别递归排序，然后合并两个已排序的部分。</p>',
 '3': '<p>对 <code>n</code> 个元素排序，需要大约 <code>n * log(n)</code> 次比较和移动，但还需要与待排序列表大小大致相同的额外空间。</p>',
 '4': '<p>此归并排序是稳定的：相等元素排序后的相对顺序与原来相同。</p>',
 '5': '<p>对于较小的列表（少于 32 个元素），<a href="foundation/mergeSort.html">mergeSort</a> 会自动改用插入排序，因为它对小列表更高效。该插入排序同样是稳定的。</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
