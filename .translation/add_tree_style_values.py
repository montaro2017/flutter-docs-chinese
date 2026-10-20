from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsTreeStyle/values-constant.html'] = {'0': '<p>按声明顺序包含此枚举所有值的常量列表。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsTreeStyle.html']['14'] = '<dd><p class="from-extension"><span>适用于 <a href="dart-core/Enum-class.html">Enum</a>，由 <a href="dart-core/EnumName.html">EnumName</a> 扩展提供</span></p>枚举值的名称。<div class="features"><span class="feature">无 setter</span></div></dd>'
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
