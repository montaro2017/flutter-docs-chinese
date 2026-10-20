import html, json, re
from html.parser import HTMLParser
from pathlib import Path
ROOT = Path(__file__).resolve().parent
MAPPING = json.loads((ROOT / 'shared-text.json').read_text(encoding='utf-8'))
def translate_shared(text):
    mapping = MAPPING
    offsets = [0]
    for match in re.finditer('\n', text):
        offsets.append(match.end())
    changes = []
    class DataTranslator(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=False)
            self.skip = 0
        def handle_starttag(self, tag, attrs):
            if tag in ['script','style','pre','code']:
                self.skip += 1
        def handle_endtag(self, tag):
            if tag in ['script','style','pre','code']:
                self.skip = max(0,self.skip-1)
        def handle_data(self, raw):
            key = ' '.join(raw.split())
            if self.skip:
                return
            translated = mapping.get(key)
            if translated is None:
                title = re.fullmatch(r'(\w+) class - (\w+) library - Dart API',key)
                member_title = re.fullmatch(r'(.+) (method|property|constructor) - (.+) class - (\w+) library - Dart API',key)
                constructor_title = re.fullmatch(r'(.+) constructor - (.+) - (\w+) library - Dart API',key)
                label = re.fullmatch(r'([\w.]+) (class|library|method|property|constructor)',key)
                if title:
                    translated = f'{title[1]} 类 - {title[2]} 库 - Dart API 中文文档'
                elif member_title:
                    kind = {'method':'方法','property':'属性','constructor':'构造函数'}[member_title[2]]
                    translated = f'{member_title[1]} {kind} - {member_title[3]} 类 - {member_title[4]} 库 - Dart API 中文文档'
                elif constructor_title:
                    translated = f'{constructor_title[1]} 构造函数 - {constructor_title[2]} - {constructor_title[3]} 库 - Dart API 中文文档'
                elif label:
                    translated = label[1] + ' ' + {'class':'类','library':'库','method':'方法','property':'属性','constructor':'构造函数'}[label[2]]
                else:
                    return
            line,column = self.getpos()
            start = offsets[line-1] + column
            leading = raw[:len(raw)-len(raw.lstrip())]
            trailing = raw[len(raw.rstrip()):]
            changes.append((start, start+len(raw), leading+html.escape(translated)+trailing))
    DataTranslator().feed(text)
    for start,end,new in reversed(changes):
        text = text[:start] + new + text[end:]
    text = re.sub(r'content="API docs for the ([^"<>]+) class from the ([^"<>]+) library, for the Dart programming language\."',lambda m:'content="'+html.escape(f'{m[2]} 库中 {m[1]} 类的 API 中文文档，适用于 Dart 编程语言。')+'"',text)
    text = re.sub(r'content="([^"<>]+) library API docs, for the Dart programming language\."',lambda m:'content="'+html.escape(f'{m[1]} 库 API 文档，适用于 Dart 编程语言。')+'"',text)
    text = re.sub(r'<title>([^<]+) library - Dart API</title>',lambda m:'<title>'+html.escape(m[1])+' 库 - Dart API 中文文档</title>',text)
    for old,new in {
        'Loading search...':'正在加载搜索…',
        'Toggle between light and dark mode':'切换浅色与深色模式',
        'Light and dark mode toggle':'切换浅色与深色模式',
        'View source code':'查看源代码',
        'Copy link to clipboard':'复制链接到剪贴板',
        'Copy to clipboard':'复制到剪贴板'
    }.items():
        for attr in ['placeholder','title','aria-label']:
            text = text.replace(f'{attr}="{old}"',f'{attr}="{new}"')
    return text
