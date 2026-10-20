from pathlib import Path
import json, re
from case_paths import read_source
r = Path(__file__).resolve().parent
p = r / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d.update({
 'foundation/kDebugMode-constant.html': {
 '0': '<p>应用以调试模式编译时为 true 的常量。</p>',
 '1': '<p>更具体地说，当应用编译时既未启用 -Ddart.vm.product=true，也未启用 -Ddart.vm.profile=true，此常量为 true。</p>',
 '2': '<p>由于这是 const 值，可以用它向编译器表明某段代码不会在调试模式下执行，因此可以将其移除。</p>',
 '3': '<p>另一种策略是使用断言，例如：</p>',
 '4': '<p>另请参阅：</p>',
 },
 'foundation/kReleaseMode-constant.html': {
 '0': '<p>应用以发布模式编译时为 true 的常量。</p>',
 '1': '<p>更具体地说，当应用使用 -Ddart.vm.product=true 标志在 Dart 中编译时，此常量为 true。</p>',
 '2': '<p>由于这是 const 值，可以用它向编译器表明某段代码不会在发布模式下执行，因此可以将其移除。</p>',
 '3': '<p>通常最好使用 <a href="foundation/kDebugMode-constant.html">kDebugMode</a> 或 <code>assert</code> 控制代码是否执行，因为使用 <a href="foundation/kReleaseMode-constant.html">kReleaseMode</a> 会使发布构建与性能分析构建产生差异，降低性能测试的代表性。</p>',
 '4': '<p>另请参阅：</p>',
 },
 'foundation/kProfileMode-constant.html': {
 '0': '<p>应用以性能分析模式编译时为 true 的常量。</p>',
 '1': '<p>更具体地说，当应用使用 -Ddart.vm.profile=true 标志在 Dart 中编译时，此常量为 true。</p>',
 '2': '<p>由于这是 const 值，可以用它向编译器表明某段代码不会在性能分析模式下执行，因此可以将其移除。</p>',
 '3': '<p>另请参阅：</p>',
 },
})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = r / 'translations-fragments.json'
d = json.loads(p.read_text(encoding='utf-8'))
for mode in ['Debug', 'Release', 'Profile']:
 page = f'foundation/k{mode}Mode-constant.html'
 section = re.search(r'<section class="desc markdown">(.*?)</section>', read_source(page), re.S).group(1)
 fragments = []
 for item in re.findall(r'<li>.*?</li>', section, re.S):
  translated = item.replace(', which is true in debug builds.', '，在调试构建中为 true。').replace(', which is true in release builds.', '，在发布构建中为 true。').replace(', which is true in profile builds.', '，在性能分析构建中为 true。')
  assert translated != item
  fragments.append({'source': item, 'translation': translated})
 d[page] = fragments
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
