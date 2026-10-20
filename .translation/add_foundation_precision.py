from pathlib import Path
import json
path = Path(__file__).resolve().parent / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'foundation/precisionErrorTolerance-constant.html': {
  '0': '<p>可容忍的双精度浮点误差阈值 epsilon。</p>',
  '1': '<p>框架在多处使用此值，以容许计算中的浮点精度损失。低于此阈值的差异可以安全忽略。</p>',
 },
 'foundation/objectRuntimeType.html': {
  '0': '<p>框架代码应优先使用此方法，而不是对 <a href="dart-core/Object/runtimeType.html">Object.runtimeType</a> 调用 <code>toString</code>。</p>',
  '1': '<p>对运行时类型调用 <code>toString</code> 并非轻量操作，可能影响性能。如果启用了断言，此方法返回 <code>object.runtimeType.toString()</code>；否则返回 <code>optimizedValue</code>，该值必须是简单的常量字符串。</p>',
 },
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
