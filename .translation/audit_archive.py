from pathlib import Path
from collections import defaultdict
import zipfile,json
root=Path(__file__).resolve().parent.parent
groups=defaultdict(list)
with zipfile.ZipFile(root/'flutter.docs'/'flutter.docs.zip') as archive:
    for name in archive.namelist():
        if name.startswith('flutter/') and name.endswith('.html'):
            groups[name.casefold()].append(name)
conflicts=[names for names in groups.values() if len(names)>1]
(root/'.translation'/'case-conflicts.json').write_text(json.dumps(conflicts,indent=2),encoding='utf-8')
print(json.dumps({'groups':len(conflicts),'files':sum(map(len,conflicts)),'examples':conflicts[:8]},indent=2))
