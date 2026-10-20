# AGENTS.md

## 项目结构
- `flutter.docs.cn/` 是可离线浏览的中文 Flutter API 文档站点：入口为 `index.html`，页面在 `flutter/`，静态资源在 `assets/` 和 `snippets/`。
- `flutter.docs/` 保存原始文档源，翻译页面应基于此目录，避免直接改写源文件。
- `.translation/` 保存翻译映射、校验工具和按模块拆分的进度说明。

## 下载原始文档
- 打开 [Flutter API 文档首页](https://api.flutter.dev/)，在 **Offline Documentation** 部分下载 **Main channel** 的 HTML 文档 ZIP。
- 解压后将原始文档放入仓库根目录的 `flutter.docs/`，确保存在 `flutter.docs/flutter/`、`flutter.docs/assets/`、`flutter.docs/snippets/` 和 `flutter.docs/index.html`；不要覆盖 `flutter.docs.cn/`。
- 原始文档只作为翻译来源，不要添加到 Git；翻译后的站点输出写入 `flutter.docs.cn/`。

## 工作约定
- 静态站点文件统一放在 `flutter.docs.cn/`；工作区根目录保持干净，不在根目录生成站点文件或临时脚本。
- 运行翻译/复制/校验工具前，遵循 `.translation/progress/README.md` 的模块读取指引；只读取仍未完成模块的对应进度文件。
- 使用现有 `.translation/` 工具时，生成的页面、首页、资源和代码片段都应写入 `flutter.docs.cn/`。
- 翻译 HTML 时保留链接目标、锚点、代码和页面结构；完成后使用现有校验工具检查。
