from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
for page, renderer in (('isCanvasKit.html', 'CanvasKit'), ('isSkiaWeb.html', 'CanvasKit 或 Skwasm'), ('isSkwasm.html', 'Skwasm')):
 d['foundation/' + page] = {'0': f'<p>如果应用正在使用 {renderer}，则返回 true。</p>', '1': '<p>仅用于 Web。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
