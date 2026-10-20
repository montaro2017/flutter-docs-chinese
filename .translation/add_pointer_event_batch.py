import json
from pathlib import Path
p=Path('.translation/translations.json')
d=json.loads(p.read_text(encoding='utf-8'))
d.update({
'flutter/gestures/PointerAddedEvent-class.html': {'0':'<p>该设备已开始追踪此指针。</p>','1':'<p>例如，指针可能悬停在设备上方，尚未接触设备表面。</p>'},
'flutter/gestures/PointerAddedEvent/PointerAddedEvent.html': {'0':'<p>创建指针添加事件。</p>'},
'flutter/gestures/PointerAddedEvent/copyWith.html': {'0':'<p>创建事件副本，并替换指定属性。</p>','1':'<p>在经过变换的事件上调用此方法，会基于当前 <a href="gestures/PointerEvent/transform.html">transform</a> 和提供的属性返回一个新的变换后事件。</p>'},
'flutter/gestures/PointerCancelEvent-class.html': {'0':'<p>指针输入不再定向到此接收器。</p>','1':'<p>另请参阅：</p>'},
'flutter/gestures/PointerCancelEvent/PointerCancelEvent.html': {'0':'<p>创建指针取消事件。</p>'},
'flutter/gestures/PointerCancelEvent/copyWith.html': {'0':'<p>创建事件副本，并替换指定属性。</p>','1':'<p>在经过变换的事件上调用此方法，会基于当前 <a href="gestures/PointerEvent/transform.html">transform</a> 和提供的属性返回一个新的变换后事件。</p>'},
'flutter/gestures/PointerDownEvent-class.html': {'0':'<p>指针已与设备接触。</p>','1':'<p>另请参阅：</p>'},
'flutter/gestures/PointerDownEvent/PointerDownEvent.html': {'0':'<p>创建指针按下事件。</p>'},
'flutter/gestures/PointerDownEvent/copyWith.html': {'0':'<p>创建事件副本，并替换指定属性。</p>','1':'<p>在经过变换的事件上调用此方法，会基于当前 <a href="gestures/PointerEvent/transform.html">transform</a> 和提供的属性返回一个新的变换后事件。</p>'}
})
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
