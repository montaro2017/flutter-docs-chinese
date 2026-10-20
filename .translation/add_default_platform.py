from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/defaultTargetPlatform.html'] = {
 '0': '<p>与框架当前运行平台相匹配的 <a href="foundation/TargetPlatform.html">TargetPlatform</a>。</p>',
 '1': '<p>这是 <a href="material/ThemeData/platform.html">ThemeData.platform</a> 的默认值，名称也由此而来。material 库中的 widget 应通过 <a href="material/Theme/of.html">Theme.of</a> 判断用于样式适配的当前平台，而非使用 <a href="foundation/defaultTargetPlatform.html">defaultTargetPlatform</a>。尝试模拟底层平台行为的较低层 widget 和渲染对象可以直接依赖 <a href="foundation/defaultTargetPlatform.html">defaultTargetPlatform</a>。只有必须获知真实的当前平台、且不能允许任何覆盖设置时，才应直接使用 <a href="dart-io/Platform-class.html">dart:io.Platform</a> 对象，例如即将调用系统 API 时。</p>',
 '2': '<p>在测试环境中，无论宿主平台是什么，返回的平台都是 <a href="foundation/TargetPlatform.html">TargetPlatform.android</a>。（选择 Android 是因为最初编写测试时假定了类似 Android 的行为，后来才加入 iOS 平台适配。）测试可以通过平台覆盖 API（例如 material 库中的 <a href="material/ThemeData/platform.html">ThemeData.platform</a>），或在调试构建中设置 <a href="foundation/debugDefaultTargetPlatformOverride.html">debugDefaultTargetPlatformOverride</a>，来检查 iOS 行为。</p>',
 '3': '<p>测试也可以添加 <code>variant:</code> 参数并使用 <a href="flutter_test/TargetPlatformVariant-class.html">TargetPlatformVariant</a>，来创建针对特定平台的测试。</p>',
 '4': '<p>另请参阅：</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/defaultTargetPlatform.html'] = [{
 'source': '<li><a href="foundation/kIsWeb-constant.html">kIsWeb</a>, a boolean which is true if the application is running on the\nweb, where <a href="foundation/defaultTargetPlatform.html">defaultTargetPlatform</a> returns which platform the browser is\nrunning on.</li>',
 'translation': '<li><a href="foundation/kIsWeb-constant.html">kIsWeb</a>，应用在 Web 上运行时为 true 的布尔值。在 Web 上，<a href="foundation/defaultTargetPlatform.html">defaultTargetPlatform</a> 返回浏览器运行的平台。</li>',
}]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
