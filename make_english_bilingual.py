import re

with open('generated-html/sz-hk-hub-proposal/03-slides.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace language to en
html = html.replace('<html lang="zh-CN">', '<html lang="en">')
html = html.replace('<title>SZ-HK Hub 开题报告</title>', '<title>SZ-HK Hub Proposal</title>')

# Update font setup to favor English
html = html.replace('font-family: "PingFang SC"', 'font-family: "Inter", "Helvetica Neue", "PingFang SC"')

# Topbar elements
html = html.replace('开题报告</div>', 'Proposal</div>')
html = html.replace('背景与痛点</div>', 'Background & Pain Points</div>')
html = html.replace('目标与定位</div>', 'Goals & Positioning</div>')
html = html.replace('用户画像与场景</div>', 'User Personas & Scenarios</div>')
html = html.replace('核心功能</div>', 'Core Functions</div>')
html = html.replace('技术架构</div>', 'Technical Architecture</div>')
html = html.replace('Agent 工作流</div>', 'Agent Workflow</div>')
html = html.replace('RAG 数据与评估</div>', 'RAG Data & Evaluation</div>')
html = html.replace('MCP Tools层</div>', 'MCP Tools Layer</div>')
html = html.replace('TDD-for-AI</div>', 'TDD for AI</div>')
html = html.replace('当前阶段与迭代方向</div>', 'Current Stage & Micro-iterations</div>')
html = html.replace('总结与展望</div>', 'Conclusion & Outlook</div>')

# Cover
html = html.replace('深港跨境专业生活助手', 'Cross-border Professional Life Assistant<br><span style="font-size:0.6em;color:var(--muted);font-weight:500;">深港跨境专业决策助手</span>')
html = html.replace('面向跨境金融、文旅活动与政策通关的垂直领域智能决策助手。<br><span style="font-size:0.8em;color:var(--muted)">Vertical intelligent decision assistant for finance, events, and border policies.</span>', 'Vertical intelligent decision assistant for finance, events, and border policies.<br><span style="font-size:0.85em;color:var(--muted)">面向跨境金融、文旅活动与政策通关的垂直领域智能决策助手</span>')
html = html.replace('多智能体协作', 'Multi-Agent')
html = html.replace('高级 RAG', 'Advanced RAG')
html = html.replace('实时工具调用', 'Real-time MCP Tools')
html = html.replace('目标：把“能回答”升级为“能决策、可验证、可合规”。', '<b>Goal:</b> Upgrade from "can answer" to "can decide, verify, and comply." (能决策、可验证、可合规)')

html = html.replace('<b>主题词：</b>跨境生活 / 合规决策 / 双城协同', '<b>Keywords:</b> Cross-border / Compliance / Synergy')
html = html.replace('版本 1.0.0', 'Ver 1.0.0')

# Slide 2
html = html.replace('<h2>现实挑战：信息碎片、实时性差、合规风险高<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">Challenges: Fragmented Info, Poor Timeliness, High Compliance Risk</span></h2>', '<h2>Challenges: Fragmented Info, Poor Timeliness, High Compliance Risk<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">现实挑战：信息碎片、实时性差、合规风险高</span></h2>')

# Fix list paragraphs bilingual order (Eng first, then Ch)
def swap_bilingual(match):
    cn = match.group(1)
    en = match.group(2)
    return f'{en}<br><span style="font-size:0.85em;color:var(--muted)">{cn}</span>'

html = re.sub(r'<li>(.*?)<br><span style="font-size:0.85em;color:var\(--muted\)\">(.*?)<\/span><\/li>', swap_bilingual, html)
html = re.sub(r'<p>(.*?)<br><span style="font-size:0.85em;color:var\(--muted\)\">(.*?)<\/span><\/p>', swap_bilingual, html)

html = html.replace('港深双城痛点示意', 'SZ-HK Pain Points Overview')
html = html.replace('问题本质：缺一个“跨境专业决策中枢”。', '<b>Core Issue:</b> Missing a specialized "Cross-Border Decision Hub."')
html = html.replace('讲​述建议：先抛出现实痛点，再强调General LLM 的局限', '<b>Note:</b> Highlight reality pain points first.')

# Slide 3
html = html.replace('<h2>为什么要做“跨境Domain Agent”？<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">Why Build a Domain-Specific Agent?</span></h2>', '<h2>Why Build a Domain-Specific Agent?<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">为什么要构建垂直领域的跨境 Agent？</span></h2>')
html = html.replace('产品定位', 'Product Positioning')
html = html.replace('| Product Positioning', '| 产品定位')
html = html.replace('核心目标', 'Core Goals')
html = html.replace('| Core Goals', '| 核心目标')

html = html.replace('通用模型 → 专业决策助手', 'General LLM → Domain Assistant')
html = html.replace('定位一句话：跨境决策不只是“答案”，而是“可执行方案”。', '<b>Positioning:</b> Cross-border planning is not just "answers", but "executable solutions."')

# Slide 4
html = html.replace('<h2>核心用户与高频跨境场景<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">Target Users & High-Frequency Scenarios</span></h2>', '<h2>Target Users & High-Frequency Scenarios<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">核心用户与高频跨境全覆盖场景</span></h2>')
html = html.replace('跨境金融人群', 'Finance Users')
html = html.replace('| Finance Users', '| 金融客群')
html = html.replace('文旅活动人群', 'Event Goers')
html = html.replace('| Event Goers', '| 演艺活动人群')
html = html.replace('通勤商务人群', 'Commuters')
html = html.replace('| Commuters', '| 通勤商务人群')

html = html.replace('图4.1 跨境金融服务', 'Fig 4.1 Cross-border Finance')
html = html.replace('图4.2 文旅活动', 'Fig 4.2 Events & Arts')
html = html.replace('图4.3 通勤场景', 'Fig 4.3 Daily Commute')
html = html.replace('<h3>典型场景</h3>', '<h3>Typical Scenario</h3>')
html = html.replace('“去西九龙看演唱会并顺便开户”——跨场景需求需要拆解、验证、并行处理。', '"Go to West Kowloon for a concert & open a bank account" — cross-domain routing requires decomposition, verification, and parallel execution.')

# Make SVG texts bilingual where appropriate, or just Eng. For small SVG let's just make it English.
# Slide 5
html = html.replace('<h2>三大能力模块，覆盖跨境决策全链路<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">3 Core Modules: Full-Link Cross-Border Decision Making</span></h2>', '<h2>3 Core Modules: Full-Link Decision Stack<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">三大能力模块，覆盖跨境决策全链路</span></h2>')
html = html.replace('跨境金融导航', 'Finance Guide')
html = html.replace('| Finance Guide', '| 跨境金融导航')
html = html.replace('活动自动化', 'Event Automation')
html = html.replace('| Event Automation', '| 活动冲突检测')
html = html.replace('实时决策支持', 'Real-time Support')
html = html.replace('| Real-time Support', '| 实时决策支持')
html = html.replace('功能模块总览', 'Module Overview')

html = html.replace('架构原则：信息可追溯、流程可回放、建议可审查。', '<b>Architecture Principles:</b> Traceable info, replayable workflow, auditable advice.')

# Slide 6
html = html.replace('<h2>技术架构：多智能体 + RAG + MCP<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">Technical Architecture: Multi-Agent + RAG + MCP Plugins</span></h2>', '<h2>Technical Architecture: Agent + RAG + MCP<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">技术架构组合与插件调度体系</span></h2>')

# Slide 7
html = html.replace('<h2>Agent 工作流机制<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">Agent Workflow: Decompose → Call → Verify</span></h2>', '<h2>Agent Workflow: Decompose → Route → Verify<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">Agent 智能体核心工作流机制</span></h2>')
html = html.replace('协作优势', 'Workflow Advantages')
html = html.replace('| Workflow Advantages', '| 协作优势')

html = html.replace('全栈技术架构 · LLM 应用技术栈总览', 'Full-Stack Architecture Overview')
html = html.replace('多 Agent 协作流程 · 从用户查询到可执行方案', 'Multi-Agent Workflow: From Query to Plan')
html = html.replace('协作机制确保输出“可执行、可审计、可纠错”。', '<b>Mechanism:</b> Ensures outputs are executable, auditable, and self-correcting.')

# Slide 8
html = html.replace('<h2>RAG：合规与知识底座<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">RAG: The Baseline of Trust and Rules</span></h2>', '<h2>RAG: The Baseline of Trust & Compliance<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">RAG 架构：合规与知识可信底座</span></h2>')
html = html.replace('数据源', 'Data Sources')
html = html.replace('| Data Sources', '| 数据源')

# Lists in S8
html = html.replace('<li>香港特区政府政策与通关指南。</li>', '<li>HK Govt Policies & Border Guidelines.<br><span style="font-size:0.85em;color:var(--muted)">香港特区政府政策与通关指南</span></li>')
html = html.replace('<li>ZA Bank 等数字银行开户与合规说明。</li>', '<li>Virtual Banks Setup & Compliance.<br><span style="font-size:0.85em;color:var(--muted)">ZA Bank 等数字银行开户与合规说明</span></li>')
html = html.replace('<li>港铁/MTR 官方时刻与公告。</li>', '<li>MTR Official Schedules & Notices.<br><span style="font-size:0.85em;color:var(--muted)">港铁官方时刻与动态公告</span></li>')
html = html.replace('<li>专业论坛与动态 PDF 资料。</li>', '<li>Professional Forums & Dynamic PDFs.<br><span style="font-size:0.85em;color:var(--muted)">垂直跨境论坛与专业指南文档</span></li>')

html = html.replace('图5 数据源入口截图', 'Fig 5. Data Sources')
html = html.replace('RAG Search链路 · 从数据采集到检索增强', 'RAG Pipeline: From Ingestion to Retrieval')

# Slide 9
html = html.replace('<h2>MCP Tools层：把信息转成行动<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">MCP Tools: Translating Info into Action</span></h2>', '<h2>MCP Tools: Translating Info into Action<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">MCP 工具层：跨域服务的实时调用抽象</span></h2>')
html = html.replace('核心能力', 'Core Capabilities')
html = html.replace('| Core Capabilities', '| 核心能力')
html = html.replace('实时数据流概念', 'Real-Time Data Streaming via MCP')
html = html.replace('图注：用更大的节点和更少的文字展示完整数据流逻辑。', 'Note: End-to-end info flow from Query to Verified Route.')
html = html.replace('输出结果可直接给出“通关时间 + 路线 + 支付方案”。', '<b>Output:</b> Tangible combo of "Clearance Time + Route + Payment Schema."')

# Slide 10
html = html.replace('<h2>测试：保障模型可控性<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">Testing: Guarantee AI Controllability</span></h2>', '<h2>Testing: Guaranteeing Controllability<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">多维联合测试，确保输出安全、可复现</span></h2>')
html = html.replace('检索准确性测试', 'Retrieval QA Test')
html = html.replace('| Retrieval QA Test', '| 检索准确性测试')
html = html.replace('路径轨迹测试', 'Workflow Tracing')
html = html.replace('| Tracing Test', '| 路径轨迹校验')
html = html.replace('Ollama 本地回退', 'Local Fallback')
html = html.replace('| Fallback Test', '| 离线状态回退')
html = html.replace('<b>质量目标：</b>稳定性可量化、可回归、可复现，确保开题后可持续迭代。', '<b>Quality Goal:</b> Stability should be quantifiable, regressive, and reproducible to guarantee iteration safety.')

# Slide 11
html = html.replace('<h2>当前阶段与计划<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">Current Status & Milestones</span></h2>', '<h2>Current Status & Milestones<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">当前验证阶段与下一阶段迭代焦点</span></h2>')
html = html.replace('<h3>已完成探索</h3>', '<h3>Completed Explorations</h3>')
html = html.replace('<li>项目定位与用户场景确认。</li>', '<li>Validated product positioning & core user stories.</li>')
html = html.replace('<li>技术选型：Agent + RAG + MCP 架构方案。</li>', '<li>Architected the Multi-Agent + RAG + MCP design.</li>')
html = html.replace('<li>跨境合规与数据源初步调研。</li>', '<li>Surveyed compliance bounds and primary APIs.</li>')

html = html.replace('<h3>当前焦点</h3>', '<h3>Current Focus</h3>')
html = html.replace('<li>搭建最小可用原型，走通 Planner → Tools → Verifier 闭环。</li>', '<li>Build MVP loop: Planner → Tools → Verifier.</li>')
html = html.replace('<li>优先接入 2-3 个核心数据源（港府政策 + 港铁 + 汇率）。</li>', '<li>Integrate 2-3 core tools (HK Govt, MTR, FX).</li>')
html = html.replace('<li>建立基础测试框架，保障检索与行为可测。</li>', '<li>Setup baseline evaluation framework for outputs.</li>')

html = html.replace('迭代原则', 'Iteration Principles')
html = html.replace('<li>从窄场景切入，逐步扩展覆盖范围。</li>', '<li>Start from narrow scenarios, scale gradually.<br><span style="font-size:0.85em;color:var(--muted)">从窄场景切入，逐步扩展</span></li>')
html = html.replace('<li>每轮迭代产出可验证 Demo，避免过度设计。</li>', '<li>Output verifiable demos per sprint.<br><span style="font-size:0.85em;color:var(--muted)">产出可验证 Demo，避免过度设计</span></li>')
html = html.replace('<li>测试先行，功能后补。</li>', '<li>Test-driven design priority.<br><span style="font-size:0.85em;color:var(--muted)">测试先行，体验后置补充</span></li>')

html = html.replace('方向比速度重要——先跑通，再跑快。', '<b>Mindset:</b> Direction over raw speed — complete the loop before optimizing it.')

# Slide 12
html = html.replace('<h2>跨境决策助手<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">Conclusion: Decision Ready</span></h2>', '<h2>Conclusion: Decision Ready<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">总结：重塑跨境智能决策流程</span></h2>')
html = html.replace('项目核心主张', 'Core Value Proposition')
html = html.replace('<li>面向深港跨境高净值生活场景的垂直 AI 助手。</li>', '<li>Vertical AI assistant for SZ-HK cross-border scenarios.</li>')
html = html.replace('<li>多智能体协作 + 高级 RAG + MCP 实时工具的差异化架构。</li>', '<li>Differentiated stack: Multi-Agent + RAG + Real-time MCP.</li>')
html = html.replace('<li>合规可验证、信息可追溯、输出可执行。</li>', '<li>Compliant, traceable info, and actionable execution plans.</li>')

html = html.replace('需要支持的方向', 'Asks & Support Resources')
html = html.replace('<li>数据源对接授权与合规咨询。</li>', '<li>Data source API authorizations & compliance consulting.</li>')
html = html.replace('<li>MCP Tools开发与实时接口方案。</li>', '<li>Rapid integration interfaces for MCP tools.</li>')
html = html.replace('<li>测试环境与算力资源。</li>', '<li>Testing environments and computational quotas.</li>')

html = html.replace('<b>总结：</b>General LLM 难以覆盖跨境实时政策与合规要求——<b>SZ-HK Hub</b> 以多智能体 + RAG + MCP 构建专业决策闭环，让跨境生活更准确、更实时、更合规。', '<b>Summary:</b> General LLMs struggle with real-time border policies globally — <b>SZ-HK Hub</b> provides a closed-loop reliable decision engine using Multi-Agents + RAG + MCP, ensuring cross-border flow is accurate and seamless.')
html = html.replace('<b>请求：</b>请支持开题与资源协同', '<b>Request:</b> Looking forward to feedback & resources.')
html = html.replace('谢谢 · 期待反馈', 'Thank You')


with open('generated-html/sz-hk-hub-proposal/03-slides-en.html', 'w', encoding='utf-8') as f:
    f.write(html)
