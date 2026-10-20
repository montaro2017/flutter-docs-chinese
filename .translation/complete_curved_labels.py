from pathlib import Path
import json
path = Path(__file__).resolve().parent / 'shared-text.json'
obj = json.loads(path.read_text(encoding='utf-8'))
obj.update({
 'Creates a curved animation.': '创建曲线动画。',
 'The curve to use in the forward direction.': '正向运行时使用的曲线。',
 'The curve to use in the reverse direction.': '反向运行时使用的曲线。',
 'True if this CurvedAnimation has been disposed.': '如果此 CurvedAnimation 已被释放，则为 true。',
 'The animation to which this animation applies a curve.': '此动画对其应用曲线的来源动画。',
 'Cleans up any listeners added by this CurvedAnimation.': '清理此 CurvedAnimation 添加的所有监听器。',
 ', for an alternative way of expressing the first sample above.': '，提供另一种表达上方第一个示例的方式。',
 ', which provide the reverse of a': '，用于获得以下曲线的反转形式：',
})
path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
