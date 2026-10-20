from pathlib import Path
import json
path = Path(__file__).resolve().parent / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
for name, kind, detail in [
 ('listEquals','列表','长度相同，并按相同顺序包含相同元素'),
 ('setEquals','集合','长度相同，并包含相同元素'),
 ('mapEquals','映射','长度相同，并包含相同的键以及各键对应的相同值'),
]:
 ending = '不比较顺序。' if name == 'setEquals' else ''
 obj[f'foundation/{name}.html'] = {
  '0': f'<p>逐元素比较两个{kind}是否相等。</p>',
  '1': f'<p>如果两个{kind}都为 null，或者都非 null、{detail}，则返回 true。否则返回 false。{ending}</p>',
  '2': '<p>如果元素是映射、列表、集合或其他集合及复合对象，则不会逐元素比较这些元素内部的内容，除非它们的相等运算符（<a href="dart-core/Object/operator_equals.html">Object.==</a>）执行了这种比较。要检查深度相等性，可考虑使用 <a href="package-collection_collection/DeepCollectionEquality-class.html">DeepCollectionEquality</a> 类。</p>',
  '3': '<p>另请参阅：</p>',
 }
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
