from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/SynchronousFuture-class.html'
blocks = re.findall(r'<dd>.*?</dd>', read_source(page), re.S)
replacements = {
 3: [
 ('Available on ', '适用于 '),
 (',\n        provided by the ', '，\n        由 '),
 (' extension</span>', ' 扩展提供</span>'),
 ('A <a href="dart-js_interop/JSPromise-extension-type.html">JSPromise</a> that either resolves with the result of the completed\n<a href="dart-async/Future-class.html">Future</a> or rejects with an object that contains its error.', '一个 <a href="dart-js_interop/JSPromise-extension-type.html">JSPromise</a>，它会以已完成的 <a href="dart-async/Future-class.html">Future</a> 的结果兑现，或以包含其错误的对象拒绝。'),
 ('>no setter<', '>无 setter<'),
 ],
 4: [
 ('Available on ', '适用于 '),
 (',\n        provided by the ', '，\n        由 '),
 (' extension</span>', ' 扩展提供</span>'),
 ('A <a href="dart-js_interop/JSPromise-extension-type.html">JSPromise</a> that either resolves once this <a href="dart-async/Future-class.html">Future</a> completes or rejects\nwith an object that contains its error.', '一个 <a href="dart-js_interop/JSPromise-extension-type.html">JSPromise</a>，它会在此 <a href="dart-async/Future-class.html">Future</a> 完成时兑现，或以包含其错误的对象拒绝。'),
 ('>no setter<', '>无 setter<'),
 ],
 7: [('Available on ', '适用于 '), (',\n        provided by the ', '，\n        由 '), (' extension</span>', ' 扩展提供</span>'), ('Completely ignores this future and its result.', '完全忽略此 future 及其结果。')],
 8: [('Available on ', '适用于 '), (',\n        provided by the ', '，\n        由 '), (' extension</span>', ' 扩展提供</span>'), ('Handles errors on this future.', '处理此 future 的错误。')],
}
for i, pairs in replacements.items():
 text = blocks[i]
 for old, new in pairs:
  assert old in text, (i, old)
  text = text.replace(old, new)
 d[page][str(i)] = text
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
