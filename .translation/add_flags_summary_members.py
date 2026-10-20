from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/FlagsSummary/level.html'] = {'0': '<p>诊断信息的优先级，用于控制哪些诊断信息应显示或被过滤。</p>', '1': '<p>如果 <a href="foundation/DiagnosticsProperty/ifEmpty.html">ifEmpty</a> 为 null，且 <a href="foundation/FlagsSummary/value.html">value</a> 不包含非 null 条目，则返回 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.hidden</a> 级别。</p>'}
d['foundation/FlagsSummary/value.html'] = {'0': '<p>从缓存中获取属性值，或通过调用 <a href="foundation/ComputePropertyValueCallback.html">ComputePropertyValueCallback</a> 获取属性值。</p>', '1': '<p>如果调用 <a href="foundation/ComputePropertyValueCallback.html">ComputePropertyValueCallback</a> 时抛出异常，<a href="foundation/FlagsSummary/value.html">value</a> 会返回 null，并且可以通过 <a href="foundation/DiagnosticsProperty/exception.html">exception</a> 属性获取所抛出的异常。</p>', '2': '<p>另请参阅：</p>'}
d['foundation/FlagsSummary/valueToString.html'] = {i: text.replace('foundation/IntProperty/valueToString.html', 'foundation/FlagsSummary/valueToString.html') for i, text in d['foundation/IntProperty/valueToString.html'].items()}
d['foundation/FlagsSummary/toJsonMap.html'] = {'0': '<p>根据 <a href="foundation/DiagnosticsSerializationDelegate-class.html">DiagnosticsSerializationDelegate</a> 提供的配置，将节点序列化为 JSON 映射。</p>', '1': '<p>如果子类具有对使用此 JSON 的图形界面工具有用的额外属性，则应重写此方法。</p>', '2': '<p>另请参阅：</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
