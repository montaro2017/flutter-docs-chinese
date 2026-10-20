from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/FlagProperty-class.html'] = {
 '0': '<p>根据 <a href="foundation/DiagnosticsProperty/value.html">value</a> 为 true 还是 false，使用 <a href="foundation/FlagProperty/ifTrue.html">ifTrue</a> 或 <a href="foundation/FlagProperty/ifFalse.html">ifFalse</a> 作为描述的属性。</p>',
 '1': '<p>使用 <a href="foundation/FlagProperty-class.html">FlagProperty</a> 代替 <a href="foundation/DiagnosticsProperty-class.html">DiagnosticsProperty&lt;bool&gt;</a>，可使诊断信息的显示更加精炼。例如，对于通常为 true、名为 <code>visible</code> 的属性，以下代码在 <code>visible</code> 为 false 时返回“hidden”，为 true 时不显示任何内容，而不是显示 <code>visible: true</code> 或 <code>visible: false</code>。</p>',
 '4': '<p>另请参阅：</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.setdefault('foundation/FlagProperty-class.html', []).append({
 'source': '<a href="foundation/FlagProperty-class.html">FlagProperty</a> should also be used instead of <a href="foundation/DiagnosticsProperty-class.html">DiagnosticsProperty&lt;bool&gt;</a>\nif showing the bool value would not clearly indicate the meaning of the\nproperty value.',
 'translation': '如果显示布尔值无法清楚表达属性值的含义，也应使用 <a href="foundation/FlagProperty-class.html">FlagProperty</a> 代替 <a href="foundation/DiagnosticsProperty-class.html">DiagnosticsProperty&lt;bool&gt;</a>。',
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
