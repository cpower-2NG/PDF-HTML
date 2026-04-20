# PDF_HTML_creator

本仓库用于按主题生成 HTML 演示文稿，并通过 GitHub Pages 做在线归档与预览。

## 发布方式
- 使用 GitHub Pages 自动发布。
- 工作流配置见 .github/workflows/deploy-pages.yml。
- 首页入口为 index.html。

## 建议工作流
1. 在 generated-html/<topic>/01-summary.md 写摘要。
2. 在 generated-html/<topic>/02-outline.md 确认大纲。
3. 确认后生成 generated-html/<topic>/03-slides.html。
4. 提交并推送到 main 分支。

## 首次启用 GitHub Pages
1. 在 GitHub 仓库 Settings -> Pages。
2. Source 选择 GitHub Actions。
3. 推送 main 分支后等待部署完成。

部署成功后，访问：
- https://<你的用户名>.github.io/<仓库名>/
