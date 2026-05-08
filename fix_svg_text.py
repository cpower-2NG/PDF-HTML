with open('generated-html/sz-hk-hub-proposal/03-slides.html', 'r', encoding='utf-8') as f:
    html = f.read()

# SVG texts Slide 5 (Core Functions / Module Overview)
html = html.replace('决策引擎', 'Decision Engine')

# Slide 6 Architecture
html = html.replace('01 Interactive Layer', '01 Interactive Layer') # Already Eng
html = html.replace('Web UI', 'Web UI')
html = html.replace('API', 'API')
html = html.replace('Chat', 'Chat')

# Replace SVG Chinese
html = html.replace('<text x="212" y="115" text-anchor="middle" font-size="12" fill="#b080a0">Tool Route</text>', '<text x="212" y="115" text-anchor="middle" font-size="12" fill="#b080a0">Tool Route</text>') 

# Let's actually look for `<text ...>Chinese</text>` and do replacements
html = html.replace('>$GPT-4 / DeepSeek</text>', '>GPT-4 / DeepSeek</text>')
html = html.replace('>Embedding</text>', '>Embedding</text>')

html = html.replace('01 用户交互层</text>', '01 Interactive Layer</text>')
html = html.replace('02 Agent 编排层</text>', '02 Agent Orchestration</text>')
html = html.replace('拆解</text>', 'Decompose</text>')
html = html.replace('反思·审计</text>', 'Audit·Check</text>')
html = html.replace('工具路由</text>', 'Tool Route</text>')
html = html.replace('核心推理</text>', 'Reasoning Core</text>')

html = html.replace('05 数据源</text>', '05 Data Sources</text>')
html = html.replace('香港政府</text>', 'HK Govt</text>')
html = html.replace('银行合规</text>', 'Bank Rules</text>')
html = html.replace('港铁时刻</text>', 'MTR Data</text>')
html = html.replace('文旅活动</text>', 'Events</text>')

# Slide 7 Agent flow
html = html.replace('👤 User Query', '👤 User Query')

# Slide 8 RAG
html = html.replace('📊 指标：Hit Rate / MRR</text>', '📊 Metrics: Hit Rate / MRR</text>')

# Just write a function to map Chinese strings to English
svg_translates = {
    '港深双城痛点示意': 'SZ-HK Pain Points Overview',
    '信息孤岛': 'Info Silos',
    '缺乏实时': 'No Real-time',
    '香港': 'Hong Kong',
    '深圳': 'Shenzhen',
    '政策碎片化': 'Fragmented Policy',
    '合规易违规': 'Unclear Compliance',
    '信息滞后': 'Information Lag',
    '数据不互通': 'Data Disconnect',
    '缺一个“垂直领域决策 Agent”': 'Missing Domain-Specific Agent',
    '通用模型 → 专业决策助手': 'General LLM → Domain Assistant',
    '通用大模型': 'General LLM',
    '容易幻觉': 'Hallucination',
    '无法验证': 'Untraceable',
    '领域 Agent': 'Domain Agent',
    '可信 RAG': 'Verified RAG',
    '安全护栏': 'Safety Guardrails',
    '调用工具': 'Tools',
    '输出可查': 'Traceable',
    '功能模块总览': 'Module Overview',
    '决策引擎': 'Decision Engine',
    '跨境金融': 'Finance',
    '开户指南': 'Account Guide',
    '合规提醒': 'Compliance Alerts',
    '文旅活动': 'Events',
    '海报解析': 'Poster Parsing',
    '日程冲突': 'Conflict Detection',
    '实时支持': 'Real-time Support',
    '汇率 / 人流 / 时间表': 'FX / Flow / MTR / Routing',
    '数据采集': 'Data Collection',
    '处理清洗': 'Processing',
    '检索阶段：': 'Retrieval Stage:',
    'Query → 向量召回 → Rerank → 上下文组装': 'Query → Vector Recall → Rerank → Context Assembly',
    '多 Agent 协作流程 · 从用户查询到可执行方案': 'Multi-Agent Workflow: From Query to Plan',
    '查询入口': 'User Query',
    '意图识别 → 任务拆分 → 依赖树': 'Intent → Subtasks → Dependencies',
    'RAG 检索': 'RAG Search',
    '知识库': 'Knowledge Base',
    '实时 API': 'Real-time API',
    '安全校验 → 兜底策略 → 证据透出': 'Anti-Hallucination → Compliance → Trace',
    '失败重试': 'Fallback/Retry',
    '✅ 最终可执行方案': '✅ Final Executable Plan',
    '03 RAG 知识层': '03 RAG Knowledge',
    '04 MCP 工具层': '04 MCP Tools',
    '全栈技术架构 · LLM 应用技术栈总览': 'Full-Stack Architecture Overview'
}

for k, v in svg_translates.items():
    html = html.replace(f'>{k}<', f'>{v}<')
    html = html.replace(f'"{k}"', f'"{v}"')

with open('generated-html/sz-hk-hub-proposal/03-slides.html', 'w', encoding='utf-8') as f:
    f.write(html)
