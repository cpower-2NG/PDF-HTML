# 生成的 HTML

这个目录用于存放按主题归档的演示文稿输出。

## 目录约定
- 每个主题使用独立子目录。
- 固定流程：先摘要，再大纲，确认后再生成正式 HTML。

推荐结构：
- generated-html/<topic>/01-summary.md
- generated-html/<topic>/02-outline.md
- generated-html/<topic>/03-slides.html
- generated-html/<topic>/assets/

当前主题：
- generated-html/shenzhen-low-altitude-economy-xijinping-thought/01-summary.md
- generated-html/shenzhen-low-altitude-economy-xijinping-thought/02-outline.md
- generated-html/shenzhen-low-altitude-economy-xijinping-thought/03-slides-draft.html

## 在线预览与归档（GitHub Pages）
- 仓库首页为 index.html。
- 工作流文件：.github/workflows/deploy-pages.yml。
- 每次推送到 main 分支后自动发布。

## 本地到发布的最短流程
1. 修改摘要或大纲。
2. 生成或更新 03-slides.html。
3. 提交并推送到 main。
4. 打开 GitHub Pages 地址查看在线效果。
