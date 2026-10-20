from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/debugPrintDone.html'] = {
 '0': '<p>一个 Future，当 <a href="foundation/debugPrintThrottled.html">debugPrintThrottled</a> 不再有待输出的缓冲内容时完成。该函数是 <a href="rendering/debugPrint.html">debugPrint</a> 的默认实现，后者用于将错误报告到控制台。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
page = 'foundation/debugInstrumentationEnabled.html'
section = re.search(r'<section class="desc markdown">(.*?)</section>', read_source(page), re.S).group(1)
source = re.findall(r'<li>.*?</li>', section, re.S)
target = [
 '<li><a href="cupertino/debugProfileBuildsEnabled.html">debugProfileBuildsEnabled</a> 启用对 <a href="widgets/Widget-class.html">Widget</a> 构建过程的额外跟踪。</li>',
 '<li><a href="rendering/debugProfileLayoutsEnabled.html">debugProfileLayoutsEnabled</a> 启用对 <a href="rendering/RenderObject-class.html">RenderObject</a> 布局事件的额外跟踪。</li>',
 '<li><a href="rendering/debugProfilePaintsEnabled.html">debugProfilePaintsEnabled</a> 启用对 <a href="rendering/RenderObject-class.html">RenderObject</a> 绘制事件的额外跟踪。</li>',
]
assert len(source) == len(target)
d[page] = [{'source': a, 'translation': b} for a, b in zip(source, target)]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
