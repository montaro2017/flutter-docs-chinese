# 中英文文本统计

## 原文加权覆盖率与树形报告（推荐）

```powershell
python -X utf8 .translation/text_language_stats.py --method coverage

# 控制并行度；设为 1 可串行运行
python -X utf8 .translation/text_language_stats.py --method coverage --workers 12

# 仅统计某个库，自定义输出位置
python -X utf8 .translation/text_language_stats.py --method coverage --page widgets/ --json .translation/language-stats/widgets.json --tree .translation/language-stats/widgets.html --details .translation/language-stats/widgets-details.jsonl
```

默认生成 `.translation/language-stats/coverage.html`（离线可展开的树形报告）、`coverage.json`（含同一棵树和逐页数据）、`coverage-details.jsonl`（待核查文本）。树按库、子目录、页面逐层组织；每层展示汇总覆盖率、映射词数/原文词数、三类单元数量和英文残留候选数。点击节点按需展开，不需要网络或安装依赖。

覆盖率模式默认最多使用 12 个进程；可通过 `--workers` 调整。对当前 12 逻辑核环境的 `widgets/` 页面基准，8 个进程约 15.3 秒，4 个约 23.8 秒；12 个约 13.9 秒，因此默认值采用 12。设为 1 可串行运行。程序用 lxml 的 C 扩展解析 HTML，并并行核对映射证据；迁移到 Go/Dart 需要复刻 HTML 结构对齐、映射校验和报告生成，可能改变统计口径。当前先用已有基准支持的并行度设置加速，同时保留成熟的 Python 实现。

比较原始文档与中文站的相同结构单元。单元包含正文段落、标题、列表项、表格单元、直接正文及成员摘要，嵌套结构只计一次；支持 `--scope body` 排除正文外的成员摘要。页面范围同样来自可达页面清单，首页不计入。

- **已映射（mapped）**：单元全部原文英文词均被现有翻译映射覆盖，且对应中文文本在中文站对齐单元中实际存在。
- **部分覆盖（partial）**：部分原文词有上述证据，或者单元已改变并含中文但没有可核对的完整映射。后者不凭猜测增加映射词数。
- **未覆盖（uncovered）**：没有已验证的映射词，且未检测到对齐单元的中文改动。结构无法对齐时，目标文本记为 null，整页不授予已验证覆盖，并单独标记异常。

加权覆盖率 = 已验证映射覆盖的原文英文词数 / 原文英文词总数。部分覆盖只累计映射实际覆盖的词；重叠映射不重复计数。目录汇总使用词数求和，不取页面百分比平均值。来源包括正文映射、摘要映射与片段映射，并核对共享文字替换后的目标文本；过期、未应用或无法匹配的映射不计覆盖。

词按英文字母序列计数，内部撇号或连字符保留。排除代码块、行内代码、脚本、样式、网址、可识别的 camelCase/PascalCase/下划线/点号/API 大写标识符，以及仅含一个标识符的链接文字。排除规则是启发式：个别正常缩写可能被排除，未标记的 API 名称也可能保留。纯代码、纯名称或无英文词的单元不计入三类数量。

英文残留候选是清理后的目标句子中仍含至少 4 个普通英文词的句子。仅列为候选，不自动判定漏译；引用、产品名和中英混合句需要人工核查。JSONL 包含页面路径、单元编号、分类、原文、译文、词数与候选句子。编号对应结构单元，从 0 起，**不是进度清单中的段落编号**。

该指标衡量有实际目标文本证据的映射覆盖程度，不认证翻译质量或整段翻译完整性；同样不把“有中文”直接算成整段完成。尚未录入映射的实际翻译、结构变化和跨单元片段可能导致保守低估。报告是一轮读取的结果，运行期间应避免同时修改翻译文件。

## 字符构成统计

程序仅使用 Python 标准库，不修改原始文档和中文站。

```powershell
# 中文站：统计全部可达 API 页面的正文与成员摘要
python -X utf8 .translation/text_language_stats.py --json .translation/language-stats/site.json

# 指定库并导出无 HTML 标签的纯文本
python -X utf8 .translation/text_language_stats.py --page widgets/ --text-dir .translation/language-stats/text

# 原始英文文档；可重复指定 --page
python -X utf8 .translation/text_language_stats.py --source original --page widgets/WidgetState.html
```

页面范围来自 `.translation/reachable-pages.json`，不依赖仅包含未完成页面的进度清单。支持大小写冲突页面的现有路径映射。指定页面使用相对于 `flutter/` 的路径；库路径以 `/` 结尾。

`--scope body` 选择 `section.desc.markdown` 完整正文，`--scope prose`（默认）另包含 `dd` 成员摘要，`--scope page` 选择全页文本。首页不在 API 页面统计内。正文范围包括列表和表格，因而不等同于进度工具的 p/h2–h6 段落数量。

使用 HTMLParser 去除标签、注释并解码 HTML 实体，默认排除 script/style/template/noscript 与 code/pre 内容。`--include-code` 可包含代码。嵌套摘要只计一次。纯文本保留段落换行，折叠其余空白。

中文数量按 Unicode 汉字字符计数（含扩展区及兼容汉字），英文数量按 ASCII A–Z/a–z 字母计数。分母为两者之和；数字、标点、空白和其他文字不参与占比。没有中英文字的页面占比为 null。总占比由总字符数计算，不取各页面百分比平均值。

这些数值衡量文本字符构成，不能直接视为翻译完成率：保留的 API 名称、链接文字等仍可能含英文字母；汉字也无法单凭字符区间区分中文和日文。

JSON 包含统计口径、汇总与逐页数据；缺失文件会报错，避免静默漏算。纯文本导出以映射后的页面路径保存为 `.txt`。
