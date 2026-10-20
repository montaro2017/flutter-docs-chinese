"""Preserve case-sensitive archive pages on a case-insensitive filesystem."""
from pathlib import Path
from functools import lru_cache
from urllib.parse import urljoin,urlsplit,unquote
import json,re,html,posixpath,zipfile
DATA=Path(__file__).resolve().parent
ROOT=DATA.parent
@lru_cache(maxsize=1)
def mapping():
    path=DATA/'case-paths.json'
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
def read_source(page):
    original='flutter/'+page
    paths=mapping()
    if original in paths:
        archive_path=ROOT/'flutter.docs'/'flutter.docs.zip'
        if archive_path.exists():
            with zipfile.ZipFile(archive_path) as archive:
                return archive.read(original).decode('utf-8')
    candidate=ROOT/'flutter.docs'/original
    if candidate.exists():
        return candidate.read_text(encoding='utf-8')
    candidate=ROOT/'flutter.docs'/page
    if candidate.exists():
        return candidate.read_text(encoding='utf-8')
    return (ROOT/'flutter.docs'/'flutter'/page).read_text(encoding='utf-8')
def output_relative(page):
    value=mapping().get('flutter/'+page,'flutter/'+page)
    prefix='flutter/flutter/'
    return value[len(prefix):] if value.startswith(prefix) else value[len('flutter/'):] if value.startswith('flutter/') else value
def rewrite_links(text,page,paths=None):
    paths=mapping() if paths is None else paths
    if not paths:
        return text
    current='https://offline.local/'+page
    bases=re.findall(r'<base\b[^>]*href="([^"]+)"',text,re.I)
    base=urljoin(current,html.unescape(bases[0])) if bases else current
    if page.endswith('-sidebar.html') and not bases:
        base='https://offline.local/flutter/'
    def convert(raw):
        value=html.unescape(raw)
        url=urlsplit(urljoin(base,value))
        if url.netloc!='offline.local':
            return raw
        target=unquote(url.path).lstrip('/')
        if target not in paths or paths[target]==target:
            return raw
        new=paths[target]
        if value.startswith('/'):
            new='/'+new
        else:
            basepath=urlsplit(base).path.lstrip('/')
            directory=basepath if basepath.endswith('/') else posixpath.dirname(basepath)
            new=posixpath.relpath(new,directory or '.')
        if url.query: new+='?'+url.query
        if url.fragment: new+='#'+url.fragment
        return html.escape(new,quote=True)
    text=re.sub(r'\b(href|src|data-above-sidebar|data-below-sidebar)="([^"]*)"',lambda m:m[1]+'="'+convert(m[2])+'"',text)
    text=re.sub(r'(<meta\b[^>]*content="[^"<>]*?[Uu][Rr][Ll]\s*=\s*)([^"<>]+)(")',lambda m:m[1]+convert(m[2])+m[3],text)
    return text
