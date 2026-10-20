from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'StackFilter-class.html': ['<p>用于过滤堆栈帧的类，为 <a href="foundation/FlutterError/defaultStackFilter.html">FlutterError.defaultStackFilter</a> 提供额外的过滤功能。</p>'],
 'PartialStackFrame-class.html': ['<p>用于堆栈过滤的堆栈帧部分信息。</p>', '<p>另请参阅：</p>'],
 'RepetitiveStackFrameFilter-class.html': ['<p>一种 <a href="foundation/StackFilter-class.html">StackFilter</a>，根据重复出现的 <a href="foundation/PartialStackFrame-class.html">PartialStackFrame</a> 列表进行过滤。</p>', '<p>另请参阅：</p>'],
 'StackFilter/filter.html': ['<p>通过更新 <code>reasons</code> 中对应索引处的值来过滤 <a href="foundation/StackFrame-class.html">StackFrame</a> 列表。</p>', '<p>要省略一个或多个帧，请设置相应的字符串。</p>'],
 'PartialStackFrame/className.html': ['<p>该方法所属的类名。</p>', '<p>在 Web 上，此值会被忽略，因为无法获取类名。</p>', '<p>在所有平台上，顶层方法都应使用空字符串。</p>'],
 'PartialStackFrame/method.html': ['<p>此堆栈帧行的方法名。</p>', '<p>在 Web 上，私有方法名会被 <code>[]</code> 包裹。</p>'],
 'PartialStackFrame/package.html': ['<p>要匹配的包，例如 <code>package:flutter/src/foundation/assertions.dart</code> 或 <code>dart:ui/window.dart</code>。</p>'],
 'PartialStackFrame/matches.html': ['<p>检查 <a href="foundation/StackFrame-class.html">StackFrame</a> 是否与此 <a href="foundation/PartialStackFrame-class.html">PartialStackFrame</a> 中的信息匹配。</p>'],
 'PartialStackFrame/PartialStackFrame.html': ['<p>创建一个新的 <a href="foundation/PartialStackFrame-class.html">PartialStackFrame</a> 实例。</p>'],
 'RepetitiveStackFrameFilter/frames.html': ['<p>此重复堆栈模式的结构。</p>'],
 'RepetitiveStackFrameFilter/numFrames.html': ['<p>此模式中的帧数。</p>'],
 'RepetitiveStackFrameFilter/replacement.html': ['<p>用于替换这些帧的字符串。</p>', '<p>如果连续多次使用相同的替换字符串，<a href="foundation/FlutterError/defaultStackFilter.html">FlutterError.defaultStackFilter</a> 会在此行后插入重复次数，而不是重复显示该行。</p>'],
}
for page, blocks in pages.items():
 d['foundation/' + page] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
