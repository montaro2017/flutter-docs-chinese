from pathlib import Path
import json
path = Path(__file__).resolve().parent / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
descriptions = {
 'ValueChanged': '<p>报告底层值已发生变化的回调函数签名。</p>',
 'ValueSetter': '<p>报告某个值已被设置的回调函数签名。</p>',
 'ValueGetter': '<p>按需返回值的回调函数签名。</p>',
 'AsyncCallback': '<p>不接受参数、不返回数据，但返回 <a href="dart-async/Future-class.html">Future</a> 以指示工作何时完成的回调函数签名。</p>',
 'AsyncValueSetter': '<p>报告某个值已被设置，并返回一个在该值保存完成时完成的 <a href="dart-async/Future-class.html">Future</a> 的回调函数签名。</p>',
 'AsyncValueGetter': '<p>按需异步返回值的回调函数签名。</p>',
}
for name, text in descriptions.items():
 obj[f'foundation/{name}.html'] = {'0': text, '1': '<p>另请参阅：</p>'}
obj['foundation/ValueSetter.html'] = {
 '0': descriptions['ValueSetter'],
 '1': '<p>此签名与 <a href="foundation/ValueChanged.html">ValueChanged</a> 相同，但用于即使底层值未发生变化也会调用回调的情况。例如，服务扩展使用此回调，因为每当以某个值调用扩展时，都会调用该回调，而不论给定值是否为新值。</p>',
 '2': '<p>另请参阅：</p>',
}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
