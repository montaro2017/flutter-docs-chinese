from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/debugWordWrap.html'] = {
 '0': '<p>按给定宽度对指定字符串进行换行。</p>',
 '1': '<p><code>message</code> 不应包含换行符（<code>\\n</code>，U+000A）。可能包含换行符的字符串应先使用 <a href="dart-core/String/split.html">String.split</a> 拆分，再进行换行处理。</p>',
 '2': '<p>换行发生在空格字符（U+0020）处。以井号（“#”，U+0023）开头的行不会换行，因此例如 Dart 堆栈跟踪不会被换行。</p>',
 '3': '<p>后续行会尝试复制首行的缩进，例如首行以多个空格开头时。此外，如果提供了 <code>wrapIndent</code> 参数，首行之后的每一行都会以该字符串作为前缀。</p>',
 '4': '<p>此函数不适合处理任意 Unicode 文本。例如，它未实现 UAX #14，无法处理表意文字，也不支持连字符断词等功能。它仅用于格式化错误消息。</p>',
 '5': '<p>默认的 <a href="rendering/debugPrint.html">debugPrint</a> 实现使用此函数进行换行。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
