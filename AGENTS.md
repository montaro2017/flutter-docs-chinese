# AGENTS.md

## 项目结构
- `flutter.docs.cn/` 是可离线浏览的中文 Flutter API 文档站点：入口为 `index.html`，页面在 `flutter/`，静态资源在 `assets/` 和 `snippets/`。
- `flutter.docs/` 保存原始文档源，翻译页面应基于此目录，避免直接改写源文件。
- `.translation/` 仅保留 Dart 翻译进度审计工具及本地统计快照。

## 下载原始文档
- 打开 [Flutter API 文档首页](https://api.flutter.dev/)，在 **Offline Documentation** 部分下载 **Main channel** 的 HTML 文档 ZIP。
- 解压后将原始文档放入仓库根目录的 `flutter.docs/`，确保存在 `flutter.docs/flutter/`、`flutter.docs/assets/`、`flutter.docs/snippets/` 和 `flutter.docs/index.html`；不要覆盖 `flutter.docs.cn/`。
- 原始文档只作为翻译来源，不要添加到 Git；翻译后的站点输出写入 `flutter.docs.cn/`。

## 工作约定
- 静态站点文件统一放在 `flutter.docs.cn/`；工作区根目录保持干净，不在根目录生成站点文件或临时脚本。
- 每轮开始翻译前，先运行 `dart run .translation/audit-tool/bin/audit_progress.dart scan`，查看输出的 Markdown 报告 `.translation/audit/runs/<运行ID>/report/index.md`，按报告安排任务。
- 翻译前同时查看 Git 跟踪的 `.translation/audit-tool/results/unreachable-pages.md`；其中列出的首页不可达页面跳过常规翻译任务。该清单由审计工具的可选参数更新，不要求每轮主动运行；原始文档或首页链接范围变化时再更新。
- 先处理 `unaligned` 页面：用 `report --run <运行ID> --full` 检查原文和译文结构，修复页面结构或内容单元对应关系；无法确定对应关系时先记录并人工核对，不按位置猜测。修复后重新扫描，确认对齐情况，再进入翻译阶段。
- 对齐问题处理后，再依据最新统计翻译未翻译页面和单元。`unchanged` 表示对应文本仍与原文相同，可作为待翻译候选；`suspicious` 表示可能有英文残留，先人工判断。文本发生变化本身不代表译文已完成。
- 翻译任务使用子代理并行处理。按不重叠的页面范围分配任务，禁止多个代理同时修改同一 HTML 文件；每个代理报告完成页面、未完成项和疑问，由主代理汇总并复核。
- 同一时间最多运行 5 个子代理。
- 翻译页面、首页、资源和代码片段都应写入 `flutter.docs.cn/`。
- 翻译 HTML 时保留链接目标、锚点、代码和页面结构。累积一批页面后重新扫描并检查结构异常、断链和译文；确认该批结果后再集中提交并推送，不逐页提交推送。
