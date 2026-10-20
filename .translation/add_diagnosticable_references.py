from pathlib import Path
import json,re
from case_paths import read_source
r = Path(__file__).resolve().parent
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/Diagnosticable-mixin.html'
section = re.search(r'<section class="desc markdown">(.*?)</section>', read_source(page), re.S).group(1)
sources = re.findall(r'<li>.*?</li>', section, re.S)
texts = [
 '<li><a href="foundation/Diagnosticable/debugFillProperties.html">debugFillProperties</a>，列出指定 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 属性的最佳实践。最常见的用法是重写 <a href="foundation/Diagnosticable/debugFillProperties.html">debugFillProperties</a>，使用现有的 <a href="foundation/DiagnosticableTreeMixin-mixin.html">DiagnosticableTreeMixin</a> 子类及 <a href="foundation/DiagnosticsProperty-class.html">DiagnosticsProperty</a> 子类来定义自定义属性。</li>',
 '<li><a href="foundation/DiagnosticableTree-class.html">DiagnosticableTree</a>，扩展此类，还可描述树结构对象的子节点。</li>',
 '<li><a href="foundation/DiagnosticableTree/debugDescribeChildren.html">DiagnosticableTree.debugDescribeChildren</a>，列出描述 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 子节点的最佳实践。通常基类已正确描述节点的子节点，或者节点没有子节点。</li>',
 '<li><a href="foundation/DiagnosticsProperty-class.html">DiagnosticsProperty</a>，应用于创建不含属性或子节点的叶诊断节点。有许多 <a href="foundation/DiagnosticsProperty-class.html">DiagnosticsProperty</a> 子类可处理常见用例。</li>',
]
# The order of inline links is retained; clarify the subclass relationship.
texts[0] = '<li><a href="foundation/Diagnosticable/debugFillProperties.html">debugFillProperties</a>，列出指定 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 属性的最佳实践。最常见的用法是重写 <a href="foundation/Diagnosticable/debugFillProperties.html">debugFillProperties</a>，为 <a href="foundation/DiagnosticableTreeMixin-mixin.html">DiagnosticableTreeMixin</a> 的子类使用现有的 <a href="foundation/DiagnosticsProperty-class.html">DiagnosticsProperty</a> 子类定义自定义属性。</li>'
assert len(sources) == len(texts)
d[page] = [{'source': a, 'translation': b} for a,b in zip(sources,texts)]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
