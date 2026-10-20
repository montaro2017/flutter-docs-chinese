from pathlib import Path
import json
p = Path(__file__).resolve().parent / 'translations.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['foundation/debugDefaultTargetPlatformOverride.html'] = {
 '0': '<p>在调试构建中覆盖 <a href="foundation/defaultTargetPlatform.html">defaultTargetPlatform</a>。</p>',
 '1': '<p>将此值设为 null，会使 <a href="foundation/defaultTargetPlatform.html">defaultTargetPlatform</a> 恢复原始值，即根据实际当前平台确定的值。</p>',
 '2': '<p>通常，此覆盖设置仅对测试有用。要改变 widget 模拟的平台外观与行为，可以考虑使用平台覆盖 API，例如 material 库中的 <a href="material/ThemeData/platform.html">ThemeData.platform</a>。</p>',
 '3': '<p>设置 <a href="foundation/debugDefaultTargetPlatformOverride.html">debugDefaultTargetPlatformOverride</a> 而非 <a href="material/ThemeData/platform.html">ThemeData.platform</a> 等属性，会产生意外且不理想的影响。例如，当应用在 Android 上运行时，将其设为 <a href="foundation/TargetPlatform.html">TargetPlatform.iOS</a> 会使 Android 的 TalkBack 无障碍工具接收到原本供 iOS VoiceOver 使用的数据，从而产生混乱。同样，在 iOS 上将其设为 <a href="foundation/TargetPlatform.html">TargetPlatform.android</a>，会使某些 widget 假定系统具有全局返回按钮；由于 iOS 没有该按钮，这些 widget 将无法使用。</p>',
 '4': '<p>在非调试构建中尝试覆盖此属性会导致错误。</p>',
}
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
