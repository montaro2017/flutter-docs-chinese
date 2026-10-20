from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations-extra.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.setdefault('foundation/DiagnosticableNode-class.html', {}).update({
 '2': '<dd>创建描述 <a href="foundation/Diagnosticable-mixin.html">Diagnosticable</a> 值的诊断信息。</dd>',
 '3': '<dd>获取当前节点的 <a href="foundation/DiagnosticPropertiesBuilder-class.html">DiagnosticPropertiesBuilder</a>。<div class="features"><span class="feature">无 setter</span></div></dd>',
 '4': '<dd>当节点没有可显示的属性或子节点时显示的描述。<div class="features"><span class="feature">无 setter</span><span class="feature">重写</span></div></dd>',
 '5': '<dd>关于节点应如何显示的提示。<div class="features"><span class="feature">无 setter</span><span class="feature">重写</span></div></dd>',
 '6': '<dd>此诊断数据所描述的实际对象。<div class="features"><span class="feature">final</span></div></dd>',
 '7': '<dd>此 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 的子节点。<div class="features"><span class="feature">重写</span></div></dd>',
 '8': '<dd>此 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 的属性。<div class="features"><span class="feature">重写</span></div></dd>',
 '9': '<dd>返回节点自身的简短摘要描述，不包含子节点或属性。<div class="features"><span class="feature">重写</span></div></dd>',
})
d.setdefault('foundation/DiagnosticableTreeNode-class.html', {}).update({
 '1': '<dd>创建一个 <a href="foundation/DiagnosticableTreeNode-class.html">DiagnosticableTreeNode</a>。</dd>',
 '2': '<dd>此 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 的子节点。<div class="features"><span class="feature">重写</span></div></dd>',
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
