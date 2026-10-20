from pathlib import Path
import zipfile
root = Path(__file__).resolve().parent.parent
with zipfile.ZipFile(root/'flutter.docs'/'flutter.docs.zip') as archive:
    names = [n for n in archive.namelist() if n.lower().endswith('/animation/threshold/threshold.html')]
    for name in names:
        print(name)
        content = archive.read(name).decode('utf-8')
        import re
        print(re.search(r'<title>(.*?)</title>',content,re.S).group(1))
