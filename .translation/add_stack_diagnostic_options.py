from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/DiagnosticsStackTrace/DiagnosticsStackTrace.singleFrame.html'] = {'0': '<p>创建描述 StackTrace 中单个帧的诊断信息。</p>'}
d['foundation/DiagnosticsStackTrace/allowTruncate.html'] = {'0': '<p>显示节点及其子节点时是否允许截断。</p>'}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
