import json
from pathlib import Path
p=Path('.translation/translations.json');d=json.loads(p.read_text(encoding='utf-8'))
# Reuse common key-data descriptions, changing only this class's self links.
for src,tgt in [
 ('services/RawKeyEventDataAndroid/getModifierSide.html','services/RawKeyEventDataIos/getModifierSide.html'),
 ('services/RawKeyEventDataAndroid/isModifierPressed.html','services/RawKeyEventDataIos/isModifierPressed.html'),
 ('services/RawKeyEventDataAndroid/keyLabel.html','services/RawKeyEventDataIos/keyLabel.html'),
 ('services/RawKeyEventDataAndroid/logicalKey.html','services/RawKeyEventDataIos/logicalKey.html'),
 ('services/RawKeyEventDataAndroid/physicalKey.html','services/RawKeyEventDataIos/physicalKey.html')]:
 d[tgt]={i:t.replace('RawKeyEventDataAndroid','RawKeyEventDataIos') for i,t in d[src].items()}
base_hash=d['services/PhysicalKeyboardKey/hashCode.html'];e=d.setdefault('services/RawKeyEventDataIos/hashCode.html',{})
for i in ['1','2','4','6']:e[i]=base_hash[i].replace('PhysicalKeyboardKey','RawKeyEventDataIos')
d.setdefault('services/RawKeyEventDataIos/operator_equals.html',{})['8']=d['services/PhysicalKeyboardKey/operator_equals.html']['8'].replace('PhysicalKeyboardKey','RawKeyEventDataIos')
d.update({
'services/RawKeyEventDataIos-class.html':{
 '0':'<p>iOS 平台特定的键盘事件数据。</p>',
 '1':'<p>此类已弃用，之后将被移除。届时将不再提供平台特定的键盘事件数据。有关可用功能，请参阅 <a href="services/KeyEvent-class.html">KeyEvent</a>。</p>',
 '2':'<p>此对象包含通过 iOS 的 <code>UIKey</code> 接口获取的按键事件信息。</p>',
 '3':'<p>另请参阅：</p>'},
'services/RawKeyEventDataIos/RawKeyEventDataIos.html':{'0':'<p>创建 iOS 特定的键盘事件数据结构。</p>'},
'services/RawKeyEventDataIos/characters.html':{'0':'<p>与按键抬起或按下事件关联的 Unicode 字符。</p>'},
'services/RawKeyEventDataIos/charactersIgnoringModifiers.html':{'0':'<p>按键事件生成的字符，假定除 Shift 外没有其他修饰键生效。</p>'},
'services/RawKeyEventDataIos/deviceIndependentMask-constant.html':{'0':'<p>用于仅获取与设备无关的修饰键标志，使应用可以屏蔽与设备相关的修饰键标志，包括事件合并信息。</p>'},
'services/RawKeyEventDataIos/keyCode.html':{'0':'<p>与按键事件关联的键盘按键虚拟键码。</p>'},
'services/RawKeyEventDataIos/modifiers.html':{'0':'<p>使用 Modifier Flags 中的值表示当前修饰键状态的掩码。</p>'}
})
conditions={
'modifierCapsLock-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否启用了 CAPS LOCK 修饰键。',
'modifierCommand-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否按下了任一 CMD 修饰键。',
'modifierControl-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否按下了任一 CTRL 修饰键。',
'modifierFunction-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否按下了任一 FUNCTION 修饰键。',
'modifierHelp-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否按下了 HELP 修饰键。',
'modifierLeftCommand-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否按下了左侧 CMD 修饰键。',
'modifierLeftControl-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否按下了左侧 CTRL 修饰键。',
'modifierLeftOption-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否按下了左侧 ALT 修饰键。',
'modifierLeftShift-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否按下了左侧 SHIFT 修饰键。',
'modifierNumericPad-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否按下了数字键盘上的任意按键。',
'modifierOption-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否按下了任一 ALT 修饰键。',
'modifierRightCommand-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否按下了右侧 CMD 修饰键。',
'modifierRightControl-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否按下了右侧 CTRL 修饰键。',
'modifierRightOption-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否按下了右侧 ALT 修饰键。',
'modifierRightShift-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否按下了右侧 SHIFT 修饰键。',
'modifierShift-constant.html':'此掩码用于检查 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，以判断是否按下了任一 SHIFT 修饰键。'}
second='<p>如果需要自行解码 <a href="services/RawKeyEventDataIos/modifiers.html">modifiers</a> 字段，可以使用此值；但如果只想知道是否按下了修饰键，使用 <a href="services/RawKeyEventDataIos/isModifierPressed.html">isModifierPressed</a> 会简单得多。</p>'
for filename,first in conditions.items():
 d.setdefault('services/RawKeyEventDataIos/'+filename,{})['0']='<p>'+first+'</p>'
 d['services/RawKeyEventDataIos/'+filename]['1']=second
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
