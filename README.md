# PDF_HTML_creator

本仓库用于按主题生成 HTML 演示文稿，并通过 GitHub Pages 做在线归档与预览。

## 演示文稿操作说明

正式版演示文稿（`03-slides.html`）内置全屏翻页交互，无需额外插件。

### 快速开始

打开演示文稿后，页面右下角会出现控制栏：

| 按钮 | 功能 |
|------|------|
| ⛶ | 进入 / 退出全屏演示模式 |
| ◀ ▶ | 上一页 / 下一页 |
| ✕ | 退出演示模式（回到滚动浏览） |

### 键盘快捷键

| 按键 | 功能 |
|------|------|
| `↑` / `←` / `PageUp` | 上一页 |
| `↓` / `→` / `PageDown` | 下一页 |
| `F` | 切换全屏演示模式 |
| `Esc` | 退出全屏演示模式 |

### 鼠标 / 触控

- **全屏模式下**：鼠标滚轮向下 = 下一页，向上 = 上一页。
- **触屏设备**：上下滑动翻页。
- **普通浏览模式**：直接滚动页面查看所有幻灯片，控制栏悬停 3 秒后自动隐藏，移动鼠标可重新显示。

## 发布方式

- 使用 GitHub Pages 自动发布。
- 工作流配置见 `.github/workflows/deploy-pages.yml`。
- 首页入口为 `index.html`。

## 建议工作流

1. 在 `generated-html/<topic>/01-summary.md` 写摘要。
2. 在 `generated-html/<topic>/02-outline.md` 确认大纲。
3. 确认后生成 `generated-html/<topic>/03-slides.html`。
4. 提交并推送到 main 分支。

## 首次启用 GitHub Pages

1. 在 GitHub 仓库 Settings -> Pages。
2. Source 选择 GitHub Actions。
3. 推送 main 分支后等待部署完成。

## 固定调用方式（后续每次发布）

- 首次启用后，无需重复设置。
- 之后只要把修改提交并推送到 `main` 分支，GitHub Pages 会自动重新部署。
- 本仓库已启用本地自动推送钩子：`core.hooksPath=.githooks`。
- 在 `main` 分支每次 `git commit` 后会自动执行 `git push origin main`，从而自动触发 Pages 发布。
- 如需单次跳过自动推送，可使用：`NO_AUTO_PUSH=1 git commit -m "..."`。
- 建议每次发布前执行：
	1. 确认首页 `index.html` 链接指向当前正式稿。
	2. 确认 `generated-html/<topic>/03-slides.html` 无内容截断。
	3. 推送后到 Actions 页面查看部署是否成功。

部署成功后，访问：
- https://<你的用户名>.github.io/<仓库名>/
