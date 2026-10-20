from html.parser import HTMLParser
from pathlib import Path
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.skip = 0; self.stack=[]
    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)
        if tag in ['script','style','code','pre']:
            self.skip += 1
    def handle_endtag(self, tag):
        if tag in ['script','style','code','pre']:
            self.skip = max(0,self.skip-1)
        if tag in self.stack:
            self.stack=self.stack[:len(self.stack)-1-self.stack[::-1].index(tag)]
    def handle_data(self, data):
        text=' '.join(data.split())
        if not self.skip and re.search('[A-Za-z]',text) and not re.search('[\u4e00-\u9fff]',text):
            print(text)
Text().feed((Path(__file__).resolve().parent.parent/(sys.argv[1] if len(sys.argv)>1 else 'index.html')).read_text(encoding='utf-8'))
