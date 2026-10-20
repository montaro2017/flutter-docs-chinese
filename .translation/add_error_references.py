from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
descriptions = {
 'ErrorSummary': '对检测到的问题提供简短（单行）描述。',
 'ErrorDescription': '提供问题及其原因的解释、可能有助于定位问题的信息、背景信息等。',
 'ErrorHint': '提供可能适用的、具体且不明显的建议。',
 'ErrorSpacer': '显示为空白行。',
}
for cls in ('ErrorSummary', 'ErrorDescription', 'ErrorHint'):
 page = f'foundation/{cls}-class.html'
 section = re.search(r'<section class="desc markdown">(.*?)</section>', read_source(page), re.S).group(1)
 entries = []
 for source in re.findall(r'<li>.*?</li>', section, re.S):
  links = re.findall(r'<a\b[^>]*>.*?</a>', source, re.S)
  name = re.search(r'>([^<]+)</a>', links[0]).group(1)
  if name == 'FlutterError':
   translation = f'<li>{links[0]}，是最常使用 {links[1]} 的地方。</li>'
  else:
   translation = f'<li>{links[0]}，{descriptions[name]}</li>'
  entries.append({'source': source, 'translation': translation})
 d[page] = entries
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
