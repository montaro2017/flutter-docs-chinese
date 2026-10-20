from pathlib import Path
import json
path = Path(__file__).resolve().parent / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'foundation/Factory-class.html': {'0': '<p>同时报告所创建对象类型的工厂接口。</p>'},
 'foundation/Factory/Factory.html': {'0': '<p>创建新工厂。</p>'},
 'foundation/Factory/constructor.html': {'0': '<p>创建类型为 T 的新对象。</p>'},
 'foundation/Factory/type.html': {'0': '<p>此工厂创建的对象的类型。</p>'},
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
