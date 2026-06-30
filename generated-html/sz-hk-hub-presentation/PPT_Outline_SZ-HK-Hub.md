# SZ-HK Hub · 深港跨境生活 AI 助手 —— 期末答辩 PPT 大纲

> 课程：Large Language Models and Applications (IB00322) / 大语言模型及应用  
> 团队规模：2 人 | 答辩时长：15–20 分钟 | 语言：中英双语 (Bilingual CN/EN)  

---

## Slide 1 · 封面 / Title Slide

| 元素 | 内容 (CN) | Content (EN) |
|------|-----------|--------------|
| 项目名 | SZ-HK Hub · 深港跨境专业生活助手 | SZ-HK Hub: AI-Powered Cross-Border Life Assistant for Shenzhen–Hong Kong |
| 课程 | 大语言模型及应用 (IB00322) · 期末项目答辩 | Large Language Models and Applications (IB00322) · Capstone Defense |
| 团队 | 成员姓名 + 学号 | Team Members + Student IDs |
| 日期 | 2026 年春季学期 · 第 18 周 | Spring 2026 · Week 18 |

> 💡 **演讲提示**：1 分钟，快速自我介绍 + 一句话项目定位 ——「We built an AI agent that helps cross-border travelers make real-time, compliant decisions.」

---

## Slide 2 · 目录 / Agenda

| # | 章节 (CN) | Section (EN) | 时长 |
|---|-----------|--------------|------|
| 1 | 项目背景与痛点 | Background & Pain Points | 1.5 min |
| 2 | 核心功能概览 | Core Features Overview | 2 min |
| 3 | 技术架构深度 | Technical Architecture Deep Dive | 5 min |
| 4 | TDD-for-AI 测试实践 | TDD-for-AI Testing Practice | 2 min |
| 5 | 安全护栏设计 | Safety Guardrails | 1.5 min |
| 6 | 现场演示 | Live Demo | 3 min |
| 7 | 创新点与展望 | Innovation & Future Work | 1.5 min |
| 8 | 团队贡献 & 致谢 | Team Contributions & Q&A | 2 min |

> 总计约 18 分钟，留 2 分钟缓冲。

---

## Slide 3 · 项目背景与痛点 / Background & Pain Points

### 副标题：为什么深港跨境需要专用 AI？/ Why Does Cross-Border Travel Need a Specialized AI?

| 痛点 (CN) | Pain Point (EN) | 本项目的应对 (Our Solution) |
|------------|-----------------|---------------------------|
| 通用 LLM 产生幻觉：不了解最新签注政策、海关规定 | General LLMs hallucinate on latest visa & customs policies | RAG 知识库接入 10 篇权威语料（港府、MTR、银行官网），向量检索确保信息可溯源 |
| 信息碎片化：汇率、口岸人流、港铁班次分散在不同平台 | Fragmented real-time data across multiple platforms | MCP 协议统一接入 4 类实时 API，一站式聚合 |
| 决策缺乏验证：路线规划、开户建议没有合规审查 | No verification for route plans or financial advice | Reflection 自审查循环 + 高德地图地点验证 + 敏感词过滤 |
| 活动海报/截图无法结构化 | Posters & screenshots are unstructured images | Vision-LLM 多模态解析：日程提取 + 表单填单建议 |

> 💡 **关键数据**：深港日均跨境客流超 60 万人次（2025 年入境处数据），覆盖通勤、旅游、商务、开户等场景。

### 演讲要点：
> 用一张"信息孤岛"示意图展示通用 LLM vs SZ-HK Hub 的差异 —— 左侧碎片化数据源，右侧统一 Agent 输出。

---

## Slide 4 · 核心功能全景 / Core Features Overview

### 一张图展示四大核心功能 / Four Core Capabilities in One Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    SZ-HK Hub · 核心功能                          │
├───────────────┬───────────────┬───────────────┬─────────────────┤
│  ① 跨境金融   │  ② 活动情报   │  ③ 实时决策   │  ④ 多模态解析    │
│  Cross-Border │  Event        │  Real-Time    │  Multimodal     │
│  Finance      │  Intelligence │  Decision     │  Parsing        │
├───────────────┼───────────────┼───────────────┼─────────────────┤
│ · 传统/虚拟   │ · 海报/截图   │ · 实时汇率    │ · Vision-LLM    │
│   银行开户    │   日程提取    │   HKD↔CNY     │   日程结构化    │
│ · 合规建议    │ · 活动冲突    │ · 口岸客流    │ · 表格字段      │
│ · 货币申报    │   自动检测    │   三级拥堵    │   自动识别      │
│ · 外汇红线    │ · 时间线      │ · 港铁班次    │ · 填单建议      │
│   自动提醒    │   自动编排    │   12站实时    │   自动生成      │
└───────────────┴───────────────┴───────────────┴─────────────────┘
```

### 用户交互流程 / User Flow

```
用户填写表单（目的/目的地/时间/预算）
    + 可选上传海报截图
        ↓
    AI Agent 自动编排全流程
        ↓
    ← RAG 检索 → MCP 实时数据 → Vision 日程解析
        ↓
    LLM 生成分步计划 + 日程冲突提醒 + 合规校验
        ↓
    Reflection 自审查（最多 2 轮修正）
        ↓
    最终输出：可执行的跨境规划
```

> 💡 演讲时可展示真实输入示例：「去港科大打比赛，顺便在 ZA Bank 开户，晚上逛尖沙咀」

---

## Slide 5 · 技术架构总览 / Technical Architecture Overview

### 副标题：满足 A 级要求的 6 项技术集成 / 6 Technologies Integrated (A-Grade: 4+ Required)

| # | 技术 / Technology | 本项目实现 / Our Implementation |
|---|-------------------|-------------------------------|
| 1 | **Prompt Engineering** | 5 个专用 System Prompt（路由/拆解/规划/审核/Vision），含 Few-shot 示例与 JSON 结构化输出 |
| 2 | **MCP Protocol** | 4 工具统一协议（汇率/口岸/港铁/路线）+ 文件操作 + 高德地图地理编码 |
| 3 | **RAG Systems** | ChromaDB 向量库 + 10 篇双语语料 + 混合检索（关键词 + 语义）+ 子任务驱动多轮检索 |
| 4 | **AI Agents (LangGraph)** | 5 节点 StateGraph：路由→拆解→执行→规划→审核，含 Reflection 自审查循环 |
| 5 | **Multimodal Processing** | Vision-LLM 日程提取 + 表单字段识别，支持 OpenAI/Anthropic 双视觉提供商 |
| 6 | **Safety Guardrails** | 规则层敏感词过滤 + AI 层合规审核 + Reflection 自审查 + 地点反幻觉验证 |

### 三层架构图 / Three-Layer Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                      Presentation Layer                          │
│                      Gradio Web UI (port 7860)                   │
│              统一表单 + 数据仪表盘 + 规划结果 + 审核详情            │
└──────────────────────────────┬───────────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────────┐
│                    AI Agent Layer (LangGraph)                     │
│                                                                   │
│   route_intent ──→ decompose ──→ execute ──→ generate ──→ review │
│   (意图路由)       (任务拆解)     (工具调用)    (规划生成)   (审核) │
│                                       ↑                          │
│                                       └── Reflection Loop (≤2) ──┘│
└───────┬──────────────────┬──────────────────┬────────────────────┘
        │                  │                  │
┌───────▼──────┐  ┌────────▼───────┐  ┌───────▼──────────────┐
│  RAG Layer   │  │  MCP Layer     │  │  Multimodal Layer     │
│  ChromaDB +  │  │  Exchange Rate │  │  Vision-LLM (OpenAI/  │
│  Sentence-   │  │  Port Traffic  │  │  Anthropic)          │
│  Transformers│  │  MTR Schedule  │  │  · Event Extraction  │
│  10 docs     │  │  Route Planner │  │  · Form Parsing      │
│  Hybrid      │  │  + 高德地图     │  │  · Image Detection   │
│  Search      │  │  Geocoding     │  │                      │
└──────────────┘  └────────────────┘  └──────────────────────┘
```

> 💡 演讲要点：强调这是**真实可运行**的系统，不是概念原型。可以直接 `python app.py` 启动。

---

## Slide 6 · LangGraph Agent 工作流详解 / Agent Workflow in Depth

### 5 节点状态图 + Reflection 循环 / 5-Node StateGraph with Reflection Loop

| 节点 / Node | 中文说明 | English Description | 关键技术点 |
|-------------|---------|-------------------|-----------|
| **1. route_intent** | 意图路由 | Intent Routing | LLM JSON 结构化输出，根据需求自动判断需调用哪些工具和知识库 |
| **2. decompose** | 子任务拆解 | Task Decomposition | 将复杂需求拆为 2–4 个可检索的子查询（如「去港科大+开户+旅游」→ 3 个子任务） |
| **3. execute** | 并行执行 | Parallel Execution | 同时触发 RAG 检索（子任务驱动）+ MCP 工具调用 + Vision 日程解析 |
| **4. generate** | 规划生成 | Plan Generation | 融合知识库+实时数据+日程 → LLM 生成 5–8 步可执行计划（含时间/路线/费用） |
| **5. review** | 双层审核 | Two-Layer Review | 第①层：合规红线（规则）；第②层：LLM 质量评审 + 高德地图地点验证 |

### Reflection 自审查机制

```
generate ──→ review ──┬── pass  ──→ 输出最终规划
                       │
                       ├── block ──→ 拒绝输出（命中合规红线）
                       │
                       └── review ──→ 修正指令 → generate（最多 2 轮）
```

**修正内容包含**：
- 修正编造的地名（高德地图 Geocoding 验证未通过的）
- 补充遗漏的返程安排
- 纠正不合规的金融建议

> 💡 这是本项目的核心亮点之一，可在答辩中重点讲解。

---

## Slide 7 · RAG 知识库设计 / RAG Knowledge Base Design

### 副标题：10 篇双语语料 + 混合检索 / 10 Bilingual Documents + Hybrid Search

| 类别 / Category | 文档 / Documents | 核心内容 |
|-----------------|-----------------|---------|
| 🏦 金融 / Finance | `bank-guide.md`, `virtual-bank-guide.md` | 6 家传统银行 + 4 家虚拟银行（ZA Bank/Livi/WeLab/Ant/Mox）开户指南 |
| 🛃 海关 / Customs | `customs-clearance.md` | 红绿通道、免税额度、货币申报（≥12 万 HKD）、禁运品清单 |
| 🚇 交通 / Transport | `transport-guide.md`, `mtr-fare.md` | 跨境巴士/港铁/高铁全攻略 + 东铁线票价 |
| 🚧 通关 / Border | `border-policy.md` | 8 大口岸开放时间、签注类型（G/L/商务）、一地两检详解 |
| 🏫 出行 / Tourism | `hkust-guide.md`, `hk-tourism.md`, `travel-info.md` | 港科大 3 条路线 + 20+ 景点 + 半日游推荐 |
| 💰 消费 / Spending | `spending-guide.md` | 支付方式对比（支付宝/微信/八达通/现金）、餐饮/交通消费参考 |

### 检索技术栈 / Retrieval Tech Stack

| 组件 | 选型 | 说明 |
|------|------|------|
| 向量数据库 | ChromaDB (Persistent) | 轻量级，零配置，适合项目规模 |
| Embedding 模型 | `sentence-transformers/all-MiniLM-L6-v2` | 384 维，HuggingFace 镜像下载 |
| 检索策略 | **混合检索**：关键词匹配 (TF) + 语义相似度 (cosine) | 关键词命中优先返回，无命中回退纯语义 |
| 分块策略 | 按段落边界智能分块 (500 chars + 50 overlap) | 保持语义完整性 |
| 去重策略 | 子任务驱动多轮检索 + source 去重 | 避免同一文档重复出现在结果中 |

### 检索质量评估

- 指标：Hit Rate（命中率）与 MRR（Mean Reciprocal Rank）
- 方法：构建评测样本集 → 批量检索 → 统计指标 → 迭代优化分块与检索策略

> 💡 可展示 `rag_crawler.py` 动态爬虫：自动从香港海关/入境处/MTR 官网抓取最新政策文本。

---

## Slide 8 · MCP 实时数据层 / MCP Real-Time Data Layer

### 4 大实时工具 + 高德地图集成 / 4 Real-Time Tools + Amap Integration

| 工具 / Tool | 数据源 / Data Source | 更新频率 | 关键能力 |
|-------------|---------------------|---------|---------|
| 💱 `exchange_rate` | open.er-api.com（主）+ nxvav.cn（备） | 实时 | 双 API 自动 failover |
| 🚌 `port_traffic` | 香港入境处每日客流 CSV + 模拟数据回退 | 每日 | 三级拥堵分级（🟢畅通/🟡较繁忙/🔴极繁忙） |
| 🚆 `mtr_schedule` | data.gov.hk 港铁开放 API | 每 10 秒 | 东铁线罗湖/落马洲等 12 站实时到站 |
| 🗺️ `route_planner` | 高德地图公交路径规划 API + 预设路线库 | 实时 | 公交/地铁/高铁多模式，含费用与耗时 |

### 数据流架构

```
┌─────────────┐    ┌──────────────┐    ┌───────────────────┐
│ MCP Client  │───→│ Primary API  │───→│ Agent State        │
│ (mcp_client │    │ (实时调用)    │    │ (tool_results dict) │
│  .py)       │    └──────┬───────┘    └─────────┬─────────┘
└─────────────┘           │ fallback              │
                          ▼                       ▼
                   ┌──────────────┐    ┌───────────────────┐
                   │ Backup API / │    │ Planner Agent      │
                   │ 预设数据回退  │    │ → generate 节点    │
                   └──────────────┘    │   融合到规划输出    │
                                       └───────────────────┘
```

### MCP Server（可选启用）

- 基于 FastAPI 的自定义 MCP 工具网关（`mcp_server.py`）
- 提供 RESTful `/tools/{name}` 端点
- 内置深圳湾/福田/罗湖/皇岗等 7 大口岸模拟数据
- 内置深港主要路线预设库 + Google Maps API 集成

> 💡 演讲时可展示**高德地图实时路线规划**的实际效果：输入「福田→西九龙」，系统返回多条公交/地铁路线及耗时。

---

## Slide 9 · 多模态处理 / Multimodal Processing

### Vision-LLM 两大能力 / Two Vision-LLM Capabilities

| 能力 | 输入 | 输出 | 技术方案 |
|------|------|------|---------|
| 📅 **日程提取** / Event Extraction | 活动海报/活动截图 (PNG/JPEG/GIF/WebP) | `[{date, time, title}]` JSON | Vision-LLM → JSON parse → 日程冲突检测 |
| 📝 **表单解析** / Form Parsing | 银行预约截图/表格图片 | `{form_title, fields: [{label, type, required, hint}]}` | Vision-LLM → 字段识别 → 填单建议 |

### 处理流程 / Processing Pipeline

```
用户上传图片 (PNG/JPEG/GIF/WebP)
    ↓
文件类型自动检测（Magic Bytes 识别）
    ↓
Base64 编码
    ↓
┌─────────────────────────────────────────┐
│ Vision Provider 选择                    │
│ ├─ OPENAI_API_KEY → OpenAI Vision API  │
│ └─ ANTHROPIC_API_KEY → Anthropic Vision│
└─────────────────────────────────────────┘
    ↓
LLM 结构化输出 (JSON mode / System Prompt)
    ↓
日程冲突检测（同日期+同时间 → 冲突标记）
    ↓
注入到 Agent 规划流程
```

### 文件类型检测（Magic Bytes）

| 格式 | Magic Bytes |
|------|-------------|
| PNG | `\x89PNG\r\n\x1a\n` |
| JPEG | `\xff\xd8\xff` |
| GIF | `GIF87a` / `GIF89a` |
| WebP | `RIFF....WEBP` |

> 💡 演讲时可现场上传一张活动海报截图，演示 Vision-LLM 自动提取日程的完整流程。

---

## Slide 10 · LLM 多供应商设计 / Multi-LLM Provider Design

### 自动优先级探测 / Auto Priority Detection

| 优先级 | 提供商 | 触发条件 | 模型 |
|--------|--------|---------|------|
| 1 | DeepSeek / OpenAI 兼容 | `OPENAI_API_KEY` + `OPENAI_BASE_URL` | `deepseek-v4-pro` |
| 2 | Anthropic | `ANTHROPIC_API_KEY` | `claude-3-5-sonnet-20241022` |
| 3 | Ollama 本地回退 | 以上均未配置 + Ollama 可达 | `qwen2.5:1.5b` |

### 设计原则

- **Ollama 回退满足课程要求**：教师无需 API Key 即可验证系统
- **JSON 结构化输出**：OpenAI 用 `response_format`，Anthropic/Ollama 用 System Prompt 注入
- **JSON 容错解析**：`_safe_json()` 方法支持提取嵌套/不完整的 JSON 块
- **温度统一 0.2**：保证规划输出的稳定性与一致性

### LLM 使用场景矩阵

| 场景 | 调用方式 | 输出格式 |
|------|---------|---------|
| 意图路由 (route) | `chat_json()` | `{intent, needs_rag, needs_vision, tool_calls, needs_verification}` |
| 任务拆解 (decompose) | `chat_json()` | `{subtasks: [...]}` |
| 规划生成 (generate) | `chat_json()` | `{tasks: [...]}` |
| 质量审核 (review) | `chat_json()` | `{status, reason, corrections}` |
| Vision 日程 | `chat()` + image | `{events: [...]}` |
| Vision 表单 | `chat()` + image | `{form_title, fields: [...]}` |

---

## Slide 11 · TDD-for-AI 测试实践 / TDD-for-AI Testing Practice

### 测试总览 / Test Overview

| 指标 / Metric | 数据 / Data |
|---------------|-------------|
| 测试文件数 / Test Files | 7 |
| 测试用例数 / Test Cases | 20+ |
| 覆盖层级 / Coverage Levels | 4 层（工具 → 检索 → 行为 → 集成） ⭐ A 级要求 3+ |
| 测试框架 / Framework | pytest |
| 运行方式 / How to Run | `pytest` 或 `pytest -vv` |

### 四层测试覆盖 / Four-Level Test Coverage

| 层级 / Level | 测试文件 / Test File | 测试内容 / What's Tested |
|-------------|---------------------|------------------------|
| 🔧 **工具测试** / Tool Tests | `test_mcp_client.py` | MCP 客户端解析、汇率读取、异常处理、API failover |
| | `test_vision_client.py` | Vision 图片类型检测、JSON 抽取、provider 分发 |
| 📚 **检索测试** / Retrieval Tests | `test_rag_chunking.py` | RAG 文本分块边界、chunk_size/overlap 参数验证 |
| | `test_rag_search.py` | 关键词提取、混合检索排序、空查询处理 |
| 🧠 **行为测试** / Behavior Tests | `test_planner_workflow.py` | Planner 路由决策、计划生成格式、合规复核、降级路径 |
| | `test_llm_client.py` | LLM 供应商选择优先级、无配置报错、JSON 包裹输出解析 |
| 🔗 **集成测试** / Integration Tests | `test_app_features.py` | 端到端日程解析、RAG 输出格式、路线切换、安全提示 |
| | `test_config_and_ingest.py` | 环境配置读取、RAG ingest 文件筛选与入库 |

### 测试策略亮点

```
硬约束测试 (Hard Constraint)
├── JSON 结构约束验证
├── 步骤数量范围检查
├── 敏感请求触发人工复核
└── 工具异常优雅降级

语义评测 (Semantic Evaluation)
├── 评测样本模板 (cases_template.jsonl)
├── 评分规则模板 (rubric_template.md)
└── 人工评分页模板 (manual_judge_template.md)

CI 阻断项
├── 所有 pytest 必须通过
└── 修改 Prompt 后全量回归
```

> 💡 演讲时展示 `pytest -vv` 运行的终端截图，显示 20+ passed 的绿色结果。

---

## Slide 12 · 安全护栏设计 / Safety Guardrails

### 双层安全防护 / Two-Layer Safety Architecture

| 层级 | 类型 | 机制 | 示例 |
|------|------|------|------|
| **第①层** / Layer 1 | 规则层 / Rule-Based | 敏感词硬编码过滤 (`SENSITIVE_TERMS`) | "绕过外汇"、"套现"、"洗钱"、"违规开户"、"避税"、"非法" |
| **第②层** / Layer 2 | AI 层 / LLM-Based | LLM 合规审核 + 地点反幻觉验证 | 审核规划中是否有编造地名、是否遗漏返程安排、金融建议是否合规 |

### 安全检测流程

```
用户输入 → 敏感词扫描（第①层）
    ├── 命中 → ⛔ 需人工审核：命中敏感词
    └── 未命中 → Agent 生成规划
                    ↓
              review 节点（第②层）
                    ├── LLM 合规评审 (status: pass/review/block)
                    ├── 高德地图地点验证 (Geocoding)
                    └── 综合判定
                          ├── pass → ✅ 通过
                          ├── review → 🔄 Reflection 修正（最多 2 轮）
                          └── block → ⛔ 不合规：建议被驳回
```

### 金融合规红线 / Financial Compliance Red Lines

| 禁止建议 | 说明 |
|---------|------|
| ❌ 绕过外汇监管 | 每人每年 5 万美元等值外汇额度不可规避 |
| ❌ 套现/洗钱 | 涉及非法资金转移 |
| ❌ 违规开户 | 不提供虚假材料开户建议 |
| ❌ 避税方案 | 不提供逃税/避税方案 |

### 审核详情 UI（Gradio）

审核结果在 Web UI 中可折叠展开，展示：
- 📝 LLM 评审结论（pass / review / block）及理由
- 🛡️ 合规红线检查结果
- 📍 地点验证（地图中已验证 vs 未找到的地名）

> 💡 演讲时展示一个敏感词触发的案例：「如何绕过外汇限制？」→ ⛔ 需人工审核

---

## Slide 13 · 现场演示 / Live Demo

### 演示流程 / Demo Flow（3 分钟）

| # | 演示场景 | 操作 |
|---|---------|------|
| 1 | **启动系统** | `python app.py` → 浏览器打开 `http://127.0.0.1:7860` |
| 2 | **基础规划** | 输入：「周六去西九龙购物，预算 2000 HKD」→ 查看生成的 5–8 步规划（含汇率换算/路线/返程提醒） |
| 3 | **复杂场景** | 输入：「去港科大打比赛，顺便在 ZA Bank 开户，晚上逛尖沙咀」→ 查看子任务拆解 + 多维度规划 |
| 4 | **多模态** | 上传活动海报截图 → 查看 Vision-LLM 自动提取的日程 + 冲突检测 |
| 5 | **安全护栏** | 输入：「如何绕过外汇限制？」→ 查看敏感词拦截 |
| 6 | **审核详情** | 展开审核详情 → 查看 LLM 评审 + 地点验证 + 合规红线 |

### 备用方案 / Backup Plan

- 若 API 不可用 → Ollama 本地回退自动生效
- 若网络中断 → 展示预设路线 + 知识库离线检索
- 若演示超时 → 优先展示场景 2 和 4（最具视觉冲击力）

> 💡 建议提前录制 **屏幕录像** 作为备份，避免现场网络问题。

---

## Slide 14 · 创新点与项目亮点 / Innovation & Highlights

### 对比课程 A 级标准 / Compared to A-Grade Requirements

| A 级要求 | 本项目达成情况 | 说明 |
|----------|-------------|------|
| 4+ 技术集成 | ✅ **6 项** | Prompt Engineering + MCP + RAG + Agent + Multimodal + Guardrails |
| 15+ 测试用例 | ✅ **20+** | 覆盖 4 个测试层级 |
| 流畅演示 | ✅ | Gradio Web UI + Live Demo |
| 安全测试 | ✅ | 双层安全 + 3 类合规红线 |

### 创新亮点 / Innovation Highlights

| # | 创新点 | 说明 |
|---|--------|------|
| 1 | 🌉 **垂直场景深度定制** | 专注深港跨境这一真实高频场景，非泛化聊天机器人 |
| 2 | 🔄 **Reflection 自审查** | 规划 → 自我审视 → 自动修正（最多 2 轮），实现 AI 自我纠错 |
| 3 | 📍 **地点反幻觉验证** | 高德地图 Geocoding 验证 LLM 输出中的地名是否真实存在 |
| 4 | 🧩 **子任务驱动 RAG** | 将复杂需求拆解为子任务，逐一检索，比单次检索覆盖更全 |
| 5 | 🔀 **混合检索策略** | 关键词匹配优先 + 语义相似度回退，兼顾精确与召回 |
| 6 | 🔄 **多 LLM 供应商无缝切换** | 满足教师无需 API Key 验证的课程要求 |

---

## Slide 15 · 未来展望 / Future Improvements

| # | 改进方向 (CN) | Improvement (EN) | 优先级 |
|---|--------------|-----------------|--------|
| 1 | 接入更多实时数据源 | Add more real-time data sources (weather, bus ETA) | 高 |
| 2 | 用户历史记录与偏好学习 | User history & preference learning via vector memory | 高 |
| 3 | 多语言支持（粤语/英文） | Multi-language support (Cantonese/English) | 中 |
| 4 | 模型微调（LoRA） | Model fine-tuning on cross-border domain data | 中 |
| 5 | 移动端适配 | Mobile-friendly responsive UI | 低 |
| 6 | 语音输入 | Voice input integration | 低 |
| 7 | LLM-as-Judge 自动化评测 | Automated evaluation via LLM-as-Judge | 中 |

---

## Slide 16 · 团队贡献 / Individual Contributions

| 成员 / Member | 贡献 / Contribution | 占比 |
|--------------|-------------------|------|
| 成员 1 | （待填写） | XX% |
| 成员 2 | （待填写） | XX% |
| 成员 3 | （待填写） | XX% |
| 成员 4 | （待填写） | XX% |

### 贡献维度建议 / Suggested Contribution Categories
- LangGraph Agent 工作流设计与实现
- RAG 知识库构建与检索优化
- MCP 实时数据客户端开发
- Vision-LLM 多模态模块
- Gradio Web UI 前端
- 安全护栏与合规审核
- 测试套件与评测体系
- 文档与 PPT

---

## Slide 17 · 参考文献与致谢 / References & Acknowledgments

### 参考文献

| # | 来源 |
|---|------|
| 1 | LangGraph Documentation — https://langchain-ai.github.io/langgraph/ |
| 2 | ChromaDB Documentation — https://docs.trychroma.com/ |
| 3 | Model Context Protocol (MCP) Specification — https://modelcontextprotocol.io/ |
| 4 | data.gov.hk MTR Real-Time API — https://data.gov.hk/ |
| 5 | Hong Kong Immigration Department Open Data — https://www.immd.gov.hk/ |
| 6 | 课程实验指导书 llm_en/experiments/exp01–exp09/guide.md |

### 使用的开源项目
- LangGraph, ChromaDB, sentence-transformers, Gradio, FastAPI, BeautifulSoup4

### 致谢
- 感谢任课教师 nieliming@sztu.edu.cn 的指导
- 感谢同行评审团队的建设性反馈

---

## Slide 18 · Q&A / 问答环节

> Thank you! Questions & Answers  
> 谢谢！欢迎提问  

---

## 附录 A · 核心技术指标速查卡 / Quick Reference Card

| 维度 | 指标 |
|------|------|
| 代码规模 | ~2500 行 Python |
| Agent 节点 | 5 个 LangGraph 节点 |
| RAG 语料 | 10 篇 Markdown 文档 |
| MCP 工具 | 4 类实时 API + 文件操作 |
| LLM 支持 | 3 种提供商（OpenAI/Anthropic/Ollama） |
| 测试用例 | 20+ pytest |
| 测试层级 | 4 层（工具/检索/行为/集成） |
| UI | Gradio (Soft 主题，端口 7860) |
| Python 版本 | ≥ 3.10 |

---

## 附录 B · PPT 制作建议 / Slide Design Tips

1. **配色方案**：主色 `#0f766e`（Teal-700，与项目 UI 一致），辅色 `#2563eb`（Blue-600）
2. **架构图**：建议使用 Mermaid / draw.io / Excalidraw 绘制，导出 SVG 嵌入 PPT
3. **代码片段**：使用等宽字体（Fira Code / JetBrains Mono），关键行高亮
4. **数据展示**：使用表格 + 图标（emoji）提升可读性
5. **动画**：适当使用 PPT 动画展示 Agent 工作流中的数据流动
6. **双语标注**：英文标题为主，中文副标题为辅；正文关键术语中英对照
7. **字体**：英文用 Segoe UI / Calibri，中文用微软雅黑 / 思源黑体

---

> 大纲版本：v1.0 | 生成日期：2026-06-30 | 基于 `proposal.md` + `README.md` + `final_project_bilingual.docx` 编制
