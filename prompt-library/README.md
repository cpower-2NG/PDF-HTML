# Prompt 模板库

这个目录专门放“内容要求 / 生成任务”的文档，方便持续归档和扩展。

## 目录用途
- 这里放的是可复用的 prompt 模板，而不是最终生成出来的 HTML。
- 如果某个主题会反复使用，就把模板单独拆成一个 `.md` 文件放进来。
- 如果只是一次性任务，也可以继续放在 `.github/prompts/` 里做成可直接触发的 prompt。

## 推荐结构
- `templates/`：按用途分类的模板文件
- `README.md`：目录说明和入口索引

## 命名建议
- `*-outline.md`：只生成大纲
- `*-content-rich.md`：内容充实版
- `*-html.md`：HTML 生成版
- `*-pptx-safe.md`：PPTX 转换友好版
- `*-gap-fill.md`：补充内容缺口版

## 写法原则
- 主题要具体
- 受众要明确
- 核心结论要提前写出
- 必须覆盖的内容要列出来
- 页数、风格、输出目标要明确
- 要求先大纲，再正文，再 HTML
- 明确强调内容充实，而不是只做版式

## 模板索引
- [内容充实版](./templates/content-rich.md)
- [HTML 生成版](./templates/html-deck.md)
- [PPTX 稳定版](./templates/pptx-safe.md)
- [只生成大纲](./templates/outline.md)
- [补全内容缺口](./templates/gap-fill.md)
