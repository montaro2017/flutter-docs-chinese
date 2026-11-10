# Dart 翻译进度审计工具

这是翻译前统计用的 Dart 命令行工具。它对比 `flutter.docs/` 原始文档文件夹与 `flutter.docs.cn/` 中文文档文件夹中对应 HTML 页面的正文和成员摘要。统计范围按原始文档首页可达的页面确定；工具只读取本地文件，不访问网站。统计快照写入 `.translation/audit/`。

## 环境

- Windows PowerShell
- Dart SDK 3.3 或更新版本
- 仓库包含 `flutter.docs/` 和 `flutter.docs.cn/`

首次运行在本目录解析依赖：

```powershell
cd .translation/audit-tool
dart pub get
```

后续命令从仓库根目录运行：

```powershell
dart run .translation/audit-tool/bin/audit_progress.dart --help
```

## 命令

### 扫描

```powershell
# 全站扫描，生成新快照及轻量目录汇总 Markdown
dart run .translation/audit-tool/bin/audit_progress.dart scan

# 仅扫描一个库；结果在报告中标为局部扫描
dart run .translation/audit-tool/bin/audit_progress.dart scan --page widgets/

# 调整并行 worker 数（默认为逻辑处理器数量，最多 12）
dart run .translation/audit-tool/bin/audit_progress.dart scan --workers 8

# 同一次扫描额外更新首页不可达页面清单（可选）
dart run .translation/audit-tool/bin/audit_progress.dart scan --record-unreachable
```

添加 `--record-unreachable` 时，会把同次遍历得到的不可达页面和缺失链接写入 Git 跟踪文件 `.translation/audit-tool/results/unreachable-pages.md`。该选项不要求每轮翻译都运行；原始文档或首页链接范围变化后再更新。翻译前查看该清单，并跳过其中列出的页面。

扫描首先从原始首页遍历本地链接。只有 `flutter/` 下可达的 HTML 页面进入统计；断链、缺失目标、不可达页面和文件变化会写入快照的异常清单。输入未变化时，全站扫描按文件大小和修改时间复用最近一次完整快照；只有译文文件变化时，只重新分析受影响页面并复用其他页的数据；原始文档变化、首次扫描或缺少缓存时执行全量扫描。每次实际扫描都会生成新快照，完全无变化时不创建重复快照。

### 查看报告

```powershell
dart run .translation/audit-tool/bin/audit_progress.dart report --run <运行ID>
```

扫描默认只生成按目录逐层展开的轻量 Markdown 汇总，不重复读取数百 MB 的单元快照，也不为每一页创建单独文件。用 Markdown 查看器打开 `.translation/audit/runs/<运行ID>/report/index.md`，可从总览逐层查看目录和页面进度。

需要完整的单元级原文/译文详情时，显式添加 `--full`：

```powershell
dart run .translation/audit-tool/bin/audit_progress.dart report --run <运行ID> --full
```

完整报告会为每一页生成详情文件，处理时间和磁盘占用明显更高。

目录覆盖率先汇总该范围的原文词数再计算比例，不对页面百分比取平均。报告提供文本改动率、已确认翻译率、已审核率、页面完成率、状态单元数和异常数。没有人工确认记录时会标明“未建立确认基线”；文本变化本身不等同于翻译完成。

### 导出待审核条目

```powershell
dart run .translation/audit-tool/bin/audit_progress.dart export-review --run <运行ID> --out .translation/audit/review.jsonl
```

逐行编辑 JSONL 的 `decision` 和 `reason` 字段。`decision` 可为 `translated`、`reviewed` 或 `excluded`；排除必须填写原因。不要修改导出条目的 `run_id`、`unit_id`、规则版本、哈希或正文。

### 导入确认

```powershell
dart run .translation/audit-tool/bin/audit_progress.dart import-review --file .translation/audit/review.jsonl
```

导入会先核对整份文件、对应扫描快照和当前原译文哈希，再一次性追加到 `.translation/audit/reviews.jsonl`。任何一条无效都会拒绝整批导入。之后运行 `report --run <运行ID>` 更新该快照的报告。源文、译文或结构变化后，旧确认不再计入进度。

## 输出布局

```text
.translation/audit/
  reviews.jsonl
  runs/<运行ID>/
    manifest.json
    pages.jsonl
    units.jsonl
    summary.json
    report/index.md
    report/<目录>/index.md
    report/pages/<页面路径哈希>.md
```

## 统计范围和状态

只统计 API 页面中的 `section.desc.markdown` 正文和正文外 `dd` 成员摘要；导航、页脚、签名、`code`、`pre`、脚本和样式不纳入词数。英文词按字母序列计数，内部撇号和连字符保留。链接文字保留，URL 与可识别 API 标识符排除。

自动状态包括 `unchanged`、`changed`、`suspicious`、`unaligned`、`missing_target`、`missing_unit` 和 `excluded`。人工确认状态包括 `pending`、`translated`、`reviewed`、`excluded`。结构不一致的区域不按位置猜测；链接或代码变化会作为单元异常阻止确认；缺失目标和未对齐单元保留在原文分母中。

## 翻译工作顺序

每轮翻译前先运行全站扫描，并打开该运行的 `report/index.md`。如果报告有 `unaligned` 页面，先用完整报告检查原文与译文的结构和单元对应关系，修复并重新扫描；不能可靠对应时先人工核对，不要按位置猜测。确认未对齐问题处理完后，再按最新报告选择未翻译页面和单元。`unchanged` 可作为未翻译候选；`suspicious` 需要人工检查，不能仅凭文本变化认定翻译完成。

并行翻译时使用子代理分配互不重叠的页面范围，避免代理同时编辑同一文件。主代理负责复核各批结果。累积一批页面后重新扫描和检查，再集中提交并推送，不逐页提交推送。

退出码：`0` 扫描/报告完成且没有完整性异常；`1` 输入缺失、损坏或运行失败；`2` 已生成报告，但存在断链、缺页、未对齐或输入扫描期间变化等完整性异常。
