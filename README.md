# Flutter API 中文文档

本仓库是 Flutter API 文档的中文翻译版本。中文翻译由 OpenAI Codex 协助完成，当前仍在持续翻译和校对中。进度通过 Dart 审计工具从原始文档和中文站即时统计；开始翻译前先扫描并查看 Markdown 报告。

## 浏览文档

打开 [`flutter.docs.cn/index.html`](flutter.docs.cn/index.html) 即可浏览离线文档。

## 目录说明

- `flutter.docs.cn/`：中文文档站点。
- `flutter.docs/`：原始英文文档来源，不纳入 Git。
- `.translation/`：Dart 统计工具和本地统计快照。

## 工具说明

- [翻译进度统计工具](.translation/audit-tool/README.md)：翻译前运行扫描并查看按文档目录渐进展开的 Markdown 报告。

开始翻译前先统计；优先修复未对齐页面，再翻译未翻译内容。翻译任务通过子代理按不重叠页面分工；累积一批、复核并重新统计后，再集中提交和推送。

翻译前还要查看 [.translation/audit-tool/results/unreachable-pages.md](.translation/audit-tool/results/unreachable-pages.md)，跳过其中列出的首页不可达页面。原始文档或首页链接范围变化后，可运行审计工具的 `scan --record-unreachable` 更新清单。
