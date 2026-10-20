from pathlib import Path
import json
data = Path(__file__).resolve().parent
path = data / 'translations.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/Animation/Animation.fromValueListenable.html'] = {
 '0': '<p>从 <a href="foundation/ValueListenable-class.html">ValueListenable</a> 创建新动画。</p>',
 '1': '<p>返回的动画状态始终为 <a href="animation/AnimationStatus.html">AnimationStatus.forward</a>。可以选择使用 <code>transformer</code> 函数转换所提供 listenable 的值。</p>',
}
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
path = data / 'translations-fragments.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj['animation/Animation/Animation.fromValueListenable.html'] = [{
 'source': 'This constructor can be used to replace instances of <a href="widgets/ValueListenableBuilder-class.html">ValueListenableBuilder</a>\nwidgets with a corresponding animated widget, like a <a href="widgets/FadeTransition-class.html">FadeTransition</a>.',
 'translation': '此构造函数可将 <a href="widgets/ValueListenableBuilder-class.html">ValueListenableBuilder</a> 组件实例替换为相应的动画组件，例如 <a href="widgets/FadeTransition-class.html">FadeTransition</a>。',
}]
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
path = data / 'shared-text.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({'Before:': '替换前：', 'After:': '替换后：'})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
