from pathlib import Path
import json, re
from case_paths import read_source
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
tails = {
 'FSI': ['将后续文本视为隔离文本，其方向由不在嵌套隔离范围内的第一个强方向字符决定。', '这实际上是在“自动检测”文本方向，但并非完全可靠。例如，以英文引文开头的阿拉伯文本会被识别为从左到右（LTR），而非从右到左（RTL），从而导致文本顺序异常。', '使用 <a href="foundation/Unicode/PDI-constant.html">PDI</a> 结束隔离范围。'],
 'LRE': ['将后续文本视为从左到右的嵌入文本。', '使用 <a href="foundation/Unicode/PDF-constant.html">PDF</a> 结束嵌入。'],
 'LRI': ['将后续文本视为从左到右的隔离文本。', '使用 <a href="foundation/Unicode/PDI-constant.html">PDI</a> 结束隔离范围。'],
 'LRM': ['从左到右的零宽字符。'],
 'LRO': ['强制将后续字符视为强从左到右字符。', '例如，这会使希伯来文本反向显示。', '使用 <a href="foundation/Unicode/PDF-constant.html">PDF</a> 结束方向覆盖。'],
 'PDF': ['结束最近一个 <a href="foundation/Unicode/LRE-constant.html">LRE</a>、<a href="foundation/Unicode/RLE-constant.html">RLE</a>、<a href="foundation/Unicode/RLO-constant.html">RLO</a> 或 <a href="foundation/Unicode/LRO-constant.html">LRO</a> 的作用范围。'],
 'PDI': ['结束最近一个 <a href="foundation/Unicode/LRI-constant.html">LRI</a>、<a href="foundation/Unicode/RLI-constant.html">RLI</a> 或 <a href="foundation/Unicode/FSI-constant.html">FSI</a> 的作用范围。'],
 'RLE': ['将后续文本视为从右到左的嵌入文本。', '使用 <a href="foundation/Unicode/PDF-constant.html">PDF</a> 结束嵌入。'],
 'RLI': ['将后续文本视为从右到左的隔离文本。', '使用 <a href="foundation/Unicode/PDI-constant.html">PDI</a> 结束隔离范围。'],
 'RLM': ['从右到左的零宽非阿拉伯字符。'],
 'RLO': ['强制将后续字符视为强从右到左字符。', '例如，这会使英文文本反向显示。', '使用 <a href="foundation/Unicode/PDF-constant.html">PDF</a> 结束方向覆盖。'],
}
for name, paragraphs in tails.items():
 page = f'foundation/Unicode/{name}-constant.html'
 code = re.search(r'<code>.*?</code>', read_source(page), re.S).group(0)
 entries = {'0': '<p>' + code + ' 字符。</p>'}
 entries.update({str(i): '<p>' + text + '</p>' for i, text in enumerate(paragraphs, 1)})
 d[page] = entries
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
