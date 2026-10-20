from pathlib import Path
import json
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/kIsWeb-constant.html'] = {
 '0': '<p>应用被编译为在 Web 上运行时为 true 的常量。</p>',
 '1': '<p>另请参阅：</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/kIsWeb-constant.html'] = [
 {'source': '<li><a href="foundation/defaultTargetPlatform.html">defaultTargetPlatform</a>, which is used by themes to find out which\nplatform the application is running on (or, in the case of a web app,\nwhich platform the application\'s browser is running in). Can be overridden\nin tests with <a href="foundation/debugDefaultTargetPlatformOverride.html">debugDefaultTargetPlatformOverride</a>.</li>',
 'translation': '<li><a href="foundation/defaultTargetPlatform.html">defaultTargetPlatform</a>，主题使用它来判断应用运行的平台；对于 Web 应用，则是应用浏览器所运行的平台。在测试中可通过 <a href="foundation/debugDefaultTargetPlatformOverride.html">debugDefaultTargetPlatformOverride</a> 覆盖此值。</li>'},
 {'source': '<li><a href="dart-io/Platform-class.html">dart:io.Platform</a>, a way to find out the browser\'s platform that is not\noverridable in tests.</li>',
 'translation': '<li><a href="dart-io/Platform-class.html">dart:io.Platform</a>，一种判断浏览器平台的方式，无法在测试中覆盖。</li>'},
]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
