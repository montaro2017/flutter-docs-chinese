# 本地 Google 字体资源

`../google-fonts.css` 汇总 API 文档站点使用的字体样式，字体文件保存在本目录。页面通过 `static-assets/google-fonts.css` 引用本地副本，无需请求 Google Fonts 服务。

包含字体：Roboto、Roboto Mono、Open Sans、Google Sans、Material Icons、Material Symbols Outlined。CSS 和 WOFF2 文件于 2026-11-10 从以下 Google Fonts CSS API 地址获取：

- https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap
- https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0
- https://fonts.googleapis.com/css?family=Roboto:500,400italic,300,400,100i
- https://fonts.googleapis.com/css?family=Google+Sans:500,400italic,300,400,100i
- https://fonts.googleapis.com/css?family=Open+Sans:500,400italic,300,400,100i
- https://fonts.googleapis.com/icon?family=Material+Icons|Material+Icons+Outlined|Material+Icons+Sharp|Material+Icons+Round

上游许可证副本位于 `licenses/`。
