from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/RepetitiveStackFrameFilter/RepetitiveStackFrameFilter.html'] = {'0': '<p>创建一个新的 RepetitiveStackFrameFilter。</p>'}
d['foundation/RepetitiveStackFrameFilter/filter.html'] = dict(d['foundation/StackFilter/filter.html'])
d['foundation/PartialStackFrame/asynchronousSuspension-constant.html'] = {'0': '<p>堆栈跟踪中的 <code>&lt;asynchronous suspension&gt;</code> 行。</p>'}
d['foundation/StackFilter/StackFilter.html'] = {'0': '<p>此构造函数允许子类提供 const 构造函数，使其能够用于 const 表达式。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/PartialStackFrame-class.html'] = [{'source': '<li><a href="foundation/RepetitiveStackFrameFilter-class.html">RepetitiveStackFrameFilter</a>, which uses this class to compare against <a href="foundation/StackFrame-class.html">StackFrame</a>s.</li>', 'translation': '<li><a href="foundation/RepetitiveStackFrameFilter-class.html">RepetitiveStackFrameFilter</a>，使用此类与 <a href="foundation/StackFrame-class.html">StackFrame</a> 进行比较。</li>'}]
d['foundation/RepetitiveStackFrameFilter-class.html'] = [
 {'source': '<li><a href="foundation/FlutterError/addDefaultStackFilter.html">FlutterError.addDefaultStackFilter</a>, a method to register additional\nstack filters for <a href="foundation/FlutterError/defaultStackFilter.html">FlutterError.defaultStackFilter</a>.</li>', 'translation': '<li><a href="foundation/FlutterError/addDefaultStackFilter.html">FlutterError.addDefaultStackFilter</a>，用于为 <a href="foundation/FlutterError/defaultStackFilter.html">FlutterError.defaultStackFilter</a> 注册额外的堆栈过滤器。</li>'},
 {'source': '<li><a href="foundation/StackFrame-class.html">StackFrame</a>, a class that can help with parsing stack frames.</li>', 'translation': '<li><a href="foundation/StackFrame-class.html">StackFrame</a>，可帮助解析堆栈帧的类。</li>'},
 {'source': '<li><a href="foundation/PartialStackFrame-class.html">PartialStackFrame</a>, a class that helps match partial method information\nto a stack frame.</li>', 'translation': '<li><a href="foundation/PartialStackFrame-class.html">PartialStackFrame</a>，帮助将部分方法信息与堆栈帧匹配的类。</li>'},
]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
