from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'debugMaybeDispatchCreated.html': [
 '<p>如果已启用内存分配跟踪，则派发 Flutter 对象创建事件。</p>',
 '<p>此方法不属于 FlutterMemoryAllocations，因为禁用内存分配跟踪时，<a href="foundation/FlutterMemoryAllocations-class.html">FlutterMemoryAllocations</a> 不应增加 Flutter 应用的体积。</p>',
 '<p><code>flutterLibrary</code> 参数是声明该对象的 Flutter 库名称。例如，widgets.dart 对应“widgets”。</p>',
 '<p>只能在 assert 内部调用，且只能在 Flutter 框架内部使用。</p>',
 '<p>返回 true，以便将调用包裹在 <code>assert</code> 中。</p>'],
 'debugMaybeDispatchDisposed.html': [
 '<p>如果已启用内存分配跟踪，则派发对象释放事件。</p>',
 '<p>只能在 assert 内部调用。</p>',
 '<p>返回 true，以便将调用包裹在 <code>assert</code> 中。</p>'],
 'kFlutterMemoryAllocationsEnabled-constant.html': [
 '<p>如果为 true，Flutter 对象会派发内存分配事件。</p>',
 '<p>默认情况下，此常量在调试模式下为 true，在性能分析模式和发布模式下为 false。要在发布模式下启用事件派发，请传入编译标志 <code>--dart-define=flutter.memory_allocations=true</code>。</p>'],
 'MemoryAllocations.html': ['<p>用于监听对象生命周期事件的接口。</p>'],
 'kNoDefaultValue-constant.html': ['<p>用于表示 <a href="foundation/DiagnosticsNode-class.html">DiagnosticsNode</a> 没有默认值的标记对象。</p>'],
}
for page, blocks in pages.items():
 d['foundation/' + page] = {str(i): block for i, block in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
