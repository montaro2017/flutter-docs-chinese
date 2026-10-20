from pathlib import Path
import json,zipfile,hashlib,re
from case_paths import rewrite_links
DATA=Path(__file__).resolve().parent
ROOT=DATA.parent
SITE_ROOT=ROOT/'flutter.docs.cn'
conflicts=json.loads((DATA/'case-conflicts.json').read_text(encoding='utf-8'))
paths={}
with zipfile.ZipFile(ROOT/'flutter.docs'/'flutter.docs.zip') as archive:
    all_names=set(archive.namelist())
    for group in conflicts:
        ordered=sorted(group,key=lambda n:(Path(n).name!=Path(n).name.lower(),n))
        for i,name in enumerate(ordered):
            suffix=hashlib.sha256(name.encode()).hexdigest()[:8]
            target=name if i==0 else name[:-5]+f'.case-{suffix}.html'
            if i and target.casefold() in {n.casefold() for n in group}:
                raise RuntimeError('Alias collision')
            paths[name]=target
    assert len(set(n.casefold() for n in paths.values()))==len(paths)
    assert not any(new in all_names for old,new in paths.items() if old!=new)
    (DATA/'case-paths.json').write_text(json.dumps(paths,indent=2),encoding='utf-8')
    for original,target in paths.items():
        destination=(SITE_ROOT/target).resolve()
        assert destination.is_relative_to((SITE_ROOT/'flutter').resolve())
        destination.write_text(rewrite_links(archive.read(original).decode('utf-8'),original,paths),encoding='utf-8')
print(f'Restored {len(paths)} distinct archive pages; {sum(k!=v for k,v in paths.items())} aliases.',flush=True)
changed=0
for page in (SITE_ROOT/'flutter').rglob('*.html'):
    text=page.read_text(encoding='utf-8')
    revised=rewrite_links(text,page.relative_to(SITE_ROOT).as_posix(),paths)
    if revised!=text:
        page.write_text(revised,encoding='utf-8');changed+=1
root_page=SITE_ROOT/'index.html'
root_page.write_text(rewrite_links(root_page.read_text(encoding='utf-8'),'index.html',paths),encoding='utf-8')
relative={k[len('flutter/'):]:v[len('flutter/'):] for k,v in paths.items() if k!=v}
for page in (SITE_ROOT/'flutter').glob('*.json'):
    text=page.read_text(encoding='utf-8')
    for old,new in relative.items():
        text=text.replace('"'+old+'"','"'+new+'"').replace('"'+old+'#','"'+new+'#')
    page.write_text(text,encoding='utf-8')
(DATA/'case-restoration.json').write_text(json.dumps({'restored_pages':len(paths),'alias_count':sum(k!=v for k,v in paths.items()),'rewritten_html_pages':changed},indent=2),encoding='utf-8')
print(f'Rewrote links in {changed} HTML pages and root search indexes.',flush=True)
