from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
for cls in ['ErrorSummary', 'ErrorDescription', 'ErrorHint']:
 d.setdefault(f'foundation/{cls}-class.html', {})['1'] = '<dd>静态检查规则要求此构造函数只能使用字符串字面量调用，以适应 Dart Kernel 转换器的限制。该转换器可选择从传入消息中提取通过字符串插值引用的对象。</dd>'
d.setdefault('foundation/ErrorSpacer-class.html', {})['1'] = '<dd>创建一个空白间隔，插入 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 对象列表中，通常位于 <a href="foundation/FlutterError-class.html">FlutterError</a> 对象内。</dd>'
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
