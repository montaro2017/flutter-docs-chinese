from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'ComputePropertyValueCallback.html': ['<p>用于计算属性值的函数签名。</p>', '<p>如果访问属性会抛出异常，此函数也可能抛出异常，调用方必须妥善处理这种情况。例如，访问属性可能触发表示违反布局约束的断言。</p>'],
 'DiagnosticPropertiesTransformer.html': ['<p><a href="foundation/DiagnosticPropertiesBuilder-class.html">DiagnosticPropertiesBuilder</a> 转换函数的签名。</p>'],
 'FlutterExceptionHandler.html': ['<p><a href="foundation/FlutterError/onError.html">FlutterError.onError</a> 处理函数的签名。</p>'],
 'InformationCollector.html': ['<p><a href="foundation/FlutterErrorDetails/informationCollector.html">FlutterErrorDetails.informationCollector</a> 回调及其他收集错误描述信息的回调的签名。</p>'],
 'IterableFilter.html': ['<p>用于筛选可迭代对象的回调签名。</p>'],
 'ObjectEventListener.html': ['<p><a href="foundation/ObjectEvent-class.html">ObjectEvent</a> 的监听器。</p>'],
 'ServiceExtensionCallback.html': ['<p>服务扩展的函数签名。</p>', '<p>返回的映射不得包含“type”或“method”键，因为在将值发送到客户端之前，这些键会被替换。“type”键将设置为字符串 <code>_extensionType</code>，表示这是服务扩展的返回值；“method”键将设置为方法的完整名称。</p>'],
 'StackTraceDemangler.html': ['<p>用于将 <a href="dart-core/StackTrace-class.html">StackTrace</a> 对象还原为 <a href="foundation/StackFrame-class.html">StackFrame</a> 可解析格式的函数签名。</p>', '<p>另请参阅：</p>'],
 'ComputeImpl.html': ['<p><a href="foundation/compute.html">compute</a> 的函数签名。它会创建一个 isolate，在该 isolate 上运行 <code>callback</code>，将 <code>message</code> 传给它，并最终返回 <code>callback</code> 的返回值。</p>'],
}
for page, blocks in pages.items():
 d['foundation/' + page] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/StackTraceDemangler.html'] = [{'source': '<li><a href="foundation/FlutterError/demangleStackTrace.html">FlutterError.demangleStackTrace</a>, which shows an example implementation.</li>', 'translation': '<li><a href="foundation/FlutterError/demangleStackTrace.html">FlutterError.demangleStackTrace</a>，其中展示了一个示例实现。</li>'}]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
