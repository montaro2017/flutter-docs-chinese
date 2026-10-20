from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
pages = {
 'activeDevToolsServerAddress.html': ['<p>用于调试此应用的当前 DevTools 服务器地址。</p>'],
 'connectedVmServiceUri.html': ['<p>已连接的 VM 服务协议的 URI。</p>'],
 'debugDoublePrecision.html': ['<p>配置 <a href="foundation/debugFormatDouble.html">debugFormatDouble</a>，使其使用 <a href="dart-core/num/toStringAsPrecision.html">num.toStringAsPrecision</a>。</p>', '<p>默认为 null，此时使用 <a href="foundation/debugFormatDouble.html">debugFormatDouble</a> 的默认逻辑。</p>'],
 'debugFormatDouble.html': ['<p>以标准格式格式化 double 值。</p>', '<p>可以通过 <a href="foundation/debugDoublePrecision.html">debugDoublePrecision</a> 覆盖此行为。</p>'],
 'debugBrightnessOverride.html': ['<p>用于覆盖 <a href="foundation/BindingBase/platformDispatcher.html">BindingBase.platformDispatcher</a> 所提供的平台 <a href="dart-ui/Brightness.html">Brightness</a> 的设置。</p>', '<p>另请参阅：</p>'],
 'debugAssertAllFoundationVarsUnset.html': ['<p>如果 foundation 库的所有调试变量均未被更改，则返回 true。</p>', '<p>测试框架使用此函数，确保调试变量未被意外更改。</p>', '<p>可以指定 <code>debugPrintOverride</code> 参数，以指明 <a href="rendering/debugPrint.html">debugPrint</a> 变量的预期值。对于自行重写 <a href="rendering/debugPrint.html">debugPrint</a> 的测试框架，这有助于检查其自定义值是否被某个测试覆盖。</p>', '<p>完整列表请参阅 <a href="foundation/foundation-library.html">the foundation library</a>。</p>'],
 'kIsWasm-constant.html': ['<p>如果应用编译为 WebAssembly，此常量为 true。</p>', '<p>另请参阅：</p>'],
 'kMaxUnsignedSMI-constant.html': ['<p>最大的 SMI 值。</p>', '<p>参见 <a href="https://www.dartlang.org/articles/numeric-computation/#smis-and-mints">www.dartlang.org/articles/numeric-computation/#smis-and-mints</a></p>', '<p>编译为 JavaScript 时，不支持此值，因为它大于最大的安全 32 位整数。</p>'],
 'DebugPrintCallback.html': ['<p><a href="rendering/debugPrint.html">debugPrint</a> 实现的函数签名。</p>', '<p>如果提供了 <code>wrapWidth</code>，则 <code>message</code> 的每一行都会按该宽度进行单词换行。（各行可以使用换行字符分隔，例如“\\n”。）</p>', '<p>默认情况下，此函数以较为粗略的方式限制消息发送速率，以避免 Android 上的数据丢失。因此，交错调用此函数（直接调用，或通过 <a href="rendering/debugDumpRenderTree.html">debugDumpRenderTree</a>、<a href="widgets/debugDumpApp.html">debugDumpApp</a> 等间接调用）与 Dart 的 <a href="dart-core/print.html">print</a> 方法，可能导致日志中的消息顺序混乱。</p>', '<p>将 <a href="rendering/debugPrint.html">debugPrint</a> 变量设置为符合 <a href="foundation/DebugPrintCallback.html">DebugPrintCallback</a> 签名的新实现，即可替换此函数的实现。例如，flutter_test 就采用了这种做法。</p>', '<p>默认值为 <a href="foundation/debugPrintThrottled.html">debugPrintThrottled</a>。如需行为相同但不限制发送速率的版本，请使用 <a href="foundation/debugPrintSynchronously.html">debugPrintSynchronously</a>。</p>'],
}
for page, blocks in pages.items():
 d['foundation/' + page] = {str(i): b for i, b in enumerate(blocks)}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/debugBrightnessOverride.html'] = [{'source': '<li><a href="widgets/WidgetsApp-class.html">WidgetsApp</a>, which uses the <a href="foundation/debugBrightnessOverride.html">debugBrightnessOverride</a> setting in debug mode\nto construct a <a href="widgets/MediaQueryData-class.html">MediaQueryData</a>.</li>', 'translation': '<li><a href="widgets/WidgetsApp-class.html">WidgetsApp</a>，在调试模式下使用 <a href="foundation/debugBrightnessOverride.html">debugBrightnessOverride</a> 设置来构建 <a href="widgets/MediaQueryData-class.html">MediaQueryData</a>。</li>'}]
existing = d.get('foundation/kIsWeb-constant.html')
if existing:
 d['foundation/kIsWasm-constant.html'] = existing
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

