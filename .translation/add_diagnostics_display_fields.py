from pathlib import Path
import json
p = Path(__file__).resolve().parent/'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsProperty/ifEmpty.html']={'0':'<p>属性描述原本为空时使用的描述。</p>'}
d['foundation/DiagnosticsProperty/ifNull.html']={'0':'<p>属性的 <a href="foundation/DiagnosticsProperty/value.html">value</a> 为 null 时使用的描述。</p>'}
d['foundation/DiagnosticsProperty/tooltip.html']={
 '0':'<p>可选的工具提示，通常用于描述属性。</p>',
 '1':'<p>工具提示示例：“每个逻辑像素对应的物理像素数”。</p>',
 '2':'<p>如果提供了工具提示，生成字符串描述时会将其放在圆括号中，添加在原始值之后。</p>',
}
d['foundation/DiagnosticsProperty/isInteresting.html']={'0':'<p>是否认为属性值值得关注。如果属性值不值得关注，则无论构造函数的 <code>level</code> 参数提供了什么值，其 <a href="foundation/DiagnosticsProperty/level.html">level</a> 都会降低为 <a href="foundation/DiagnosticLevel.html">DiagnosticLevel.fine</a>。</p>'}
d['foundation/DiagnosticsProperty/value.html']={
 '0':d['foundation/ErrorSummary/value.html']['0'],
 '1':'<p>如果调用 <a href="foundation/ComputePropertyValueCallback.html">ComputePropertyValueCallback</a> 时抛出异常，<a href="foundation/DiagnosticsProperty/value.html">value</a> 返回 null，抛出的异常可通过 <a href="foundation/DiagnosticsProperty/exception.html">exception</a> 属性获取。</p>',
 '2':'<p>另请参阅：</p>',
}
p.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
