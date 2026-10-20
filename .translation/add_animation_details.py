from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/Animation/isForwardOrCompleted.html'] = dict(obj['animation/AnimationStatus/isForwardOrCompleted.html'])
obj.update({
 'animation/Animation/status.html': {'0': '<p>此动画的当前状态。</p>'},
 'animation/Animation/value.html': {'0': '<p>动画的当前值。</p>'},
 'animation/Animation/Animation.html': {'0': '<p>抽象 const 构造函数。此构造函数使子类能够提供 const 构造函数，从而用于 const 表达式。</p>'},
 'animation/Animation/toStringDetails.html': {
  '0': '<p>提供描述此对象状态的字符串，但不包含对象本身的信息。</p>',
  '1': '<p><a href="animation/Animation/toString.html">Animation.toString</a> 使用此函数，使 <a href="animation/Animation-class.html">Animation</a> 子类能够提供额外细节，同时确保所有 <a href="animation/Animation-class.html">Animation</a> 子类具有一致的 <a href="animation/Animation/toString.html">toString</a> 风格。</p>',
  '2': '<p>此函数的结果包含一个描述此 <a href="animation/Animation-class.html">Animation</a> 对象状态的图标：</p>',
 },
 'animation/Animation/toString.html': {
  '0': '<p>此对象的字符串表示。</p>',
  '1': '<p>某些类具有默认的文本表示，通常还提供静态 <code>parse</code> 函数（例如 <a href="dart-core/int/parse.html">int.parse</a>）。这些类会将该文本表示作为其字符串表示。</p>',
  '2': '<p>其他类没有程序关心的、有意义的文本表示。这些类通常会重写 <code>toString</code>，在检查对象时提供有用信息，主要用于调试或日志记录。</p>',
 },
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
path = data / 'shared-text.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({'increasing)': '递增）', 'decreasing)': '递减）'})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
