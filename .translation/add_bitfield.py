from pathlib import Path
import json
path = Path(__file__).resolve().parent / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'foundation/BitField-class.html': {'0': '<p>以枚举（或值实现了“index”的其他类）为索引的位字段。</p>', '1': '<p>只有枚举的前 62 个值可用作索引。</p>', '2': '<p>编译为 JavaScript 时不支持此类。</p>'},
 'foundation/BitField/BitField.html': {'0': '<p>创建所有位均为零的位字段。</p>', '1': '<p>给定长度最多为 62。</p>'},
 'foundation/BitField/BitField.filled.html': {'0': '<p>创建填充了特定值的位字段。</p>', '1': '<p>如果 value 参数为 true，则将所有位填充为一；否则填充为零。</p>', '2': '<p>给定长度最多为 62。</p>'},
 'foundation/BitField/reset.html': {'0': '<p>将所有位设为给定值。</p>', '1': '<p>如果 value 为 true，则将所有位设为一；否则设为零。默认将所有位设为零。</p>'},
 'foundation/BitField/operator_get.html': {'0': '<p>返回给定索引处的位是否为一。</p>'},
 'foundation/BitField/operator_put.html': {'0': '<p>将给定索引处的位设为给定值。</p>', '1': '<p>如果 value 为 true，则将给定索引处的位设为一；否则设为零。</p>'},
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
