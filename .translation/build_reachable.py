"""Inventory local navigation starting at the original offline homepage."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit, unquote
from collections import deque
import json, re
from case_paths import read_source,mapping
data_root = Path(__file__).resolve().parent
root = data_root.parent
source = root / 'flutter.docs'
class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.base = None
        self.links = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'base' and self.base is None and a.get('href'):
            self.base = a['href']
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])
        for key in ['data-above-sidebar', 'data-below-sidebar']:
            if a.get(key):
                self.links.append(a[key])
        if tag == 'meta' and a.get('http-equiv', '').lower() == 'refresh':
            match = re.search(r'url\s*=\s*(.*)', a.get('content', ''), re.I)
            if match:
                self.links.append(match.group(1).strip(' \"\''))
files = {'index.html'} | {p.relative_to(source).as_posix() for p in (source / 'flutter').rglob('*.html')}
files.update(mapping())
queue = deque(['index.html'])
seen = set()
missing = set()
while queue:
    page = queue.popleft()
    if page in seen:
        continue
    seen.add(page)
    parser = Links()
    parser.feed((source / page).read_text(encoding='utf-8', errors='replace') if page=='index.html' else read_source(page[len('flutter/'):]))
    current = 'https://offline.local/' + page
    base = 'https://offline.local/flutter/' if page.endswith('-sidebar.html') and parser.base is None else urljoin(current, parser.base or '')
    for link in parser.links:
        url = urlsplit(urljoin(base, link))
        if url.netloc != 'offline.local':
            continue
        path = unquote(url.path).lstrip('/')
        if not path or path.endswith('/'):
            path += 'index.html'
        if path != 'index.html' and not path.startswith('flutter/'):
            continue
        if path in files and path not in seen:
            queue.append(path)
        elif path.endswith('.html') and path not in files:
            missing.add(path)
    if len(seen) % 10000 == 0:
        print(f'Visited {len(seen)} pages', flush=True)
result = {'entry': 'index.html', 'scope': 'root index.html and reachable HTML under flutter/', 'reachable_count': len(seen), 'pages': sorted(seen), 'missing_local_links': sorted(missing), 'unreachable_html_count': len(files-seen)}
(data_root / 'reachable-pages.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'reachable_count': len(seen), 'missing_local_link_count': len(missing), 'unreachable_html_count':len(files-seen)}, ensure_ascii=False), flush=True)
