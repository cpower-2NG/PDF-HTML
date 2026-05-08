import re

with open('generated-html/sz-hk-hub-proposal/03-slides.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Helper for H2 titles
def bi_h2(zh, en):
    return f'<h2>{zh}<br><span style="font-size:0.65em;font-weight:400;color:var(--muted);margin-top:4px;display:block;">{en}</span></h2>'

def bi_h3(zh, en):
    return f'<h3>{zh}<span style="font-size:0.7em;font-weight:400;color:var(--muted);margin-left:8px;">| {en}</span></h3>'

def bi_p(zh, en):
    return f'<p>{zh}<br><span style="font-size:0.85em;color:var(--muted)">{en}</span></p>'

def bi_li(zh, en):
    return f'<li>{zh}<br><span style="font-size:0.85em;color:var(--muted)">{en}</span></li>'


# Cover Slide
text = text.replace('<h1>SZ-HK Hub</h1>\n            <h2>深港跨境专业生活助手</h2>\n            <p class="lead">面向跨境金融、文旅活动与政策通关的垂直领域智能决策助手。</p>',
                    '''<h1>SZ-HK Hub</h1>
            <h2 style="border:none;padding-left:0;">深港跨境专业生活助手<br><span style="font-size:0.6em;color:var(--muted)">Cross-border Professional Life Assistant</span></h2>
            <p class="lead">面向跨境金融、文旅活动与政策通关的垂直领域智能决策助手。<br><span style="font-size:0.8em;color:var(--muted)">Vertical intelligent decision assistant for finance, events, and border policies.</span></p>''')

# Slide 2
text = text.replace('<h2>双城生活的现实挑战：信息碎片、实时性差、合规风险高</h2>', bi_h2('现实挑战：信息碎片、实时性差、合规风险高', 'Challenges: Fragmented Info, Poor Timeliness, High Compliance Risk'))
text = text.replace('<li>政策、口岸、金融服务更新频繁，用户难以持续跟踪。</li>', bi_li('政策、口岸、金融服务更新频繁，用户难以持续跟踪。', 'Frequent policy updates make tracking difficult.'))
text = text.replace('<li>实时数据（汇率、人流、班次）缺失导致决策失误。</li>', bi_li('实时数据（汇率、人流、班次）缺失导致决策失误。', 'Lack of real-time data leads to poor decisions.'))
text = text.replace('<li>跨境金融合规边界模糊，通用 LLM 容易产生幻觉。</li>', bi_li('跨境金融合规边界模糊，通用 LLM 容易产生幻觉。', 'LLM hallucination on obscure cross-border compliance.'))
text = text.replace('<li>跨域信息分散在政府、银行、交通与活动平台。</li>', bi_li('跨域信息分散在政府、银行、交通与活动平台。', 'Information is scattered across isolated platforms.'))

# Slide 3
text = text.replace('<h2>为什么要做“跨境专业 Agent”</h2>', bi_h2('为什么要做“跨境专业 Agent”？', 'Why Build a Domain-Specific Agent?'))
text = text.replace('<h3>产品定位</h3>', bi_h3('产品定位', 'Product Positioning'))
text = text.replace('<p>面向跨境高净值生活与决策的垂直领域助手，聚焦“金融合规 + 出行路径 + 活动安排”。</p>', bi_p('面向跨境决策的垂直领域助手，聚焦“金融合规 + 出行 + 活动”。', 'Vertical assistant focused on financial compliance, travel routing, and event planning.'))
text = text.replace('<h3>核心目标</h3>', bi_h3('核心目标', 'Core Goals'))
text = text.replace('<li>准确：基于权威数据源，减少幻觉。</li>', bi_li('准确：基于权威数据源，减少幻觉。', 'Accuracy: Authoritative sources reduce hallucinations.'))
text = text.replace('<li>实时：接入动态数据与实时工具。</li>', bi_li('实时：接入动态数据与实时工具。', 'Real-time: Plug into dynamic tools and data.'))
text = text.replace('<li>合规：提供风险提示与边界提醒。</li>', bi_li('合规：提供风险提示与边界提醒。', 'Compliance: Output clear risk and boundary alerts.'))
text = text.replace('<li>可验证：输出依据可追溯。</li>', bi_li('可验证：输出依据可追溯。', 'Verifiable: Traceable output evidence.'))

# Slide 4
text = text.replace('<h2>三类核心用户，覆盖高频跨境场景</h2>', bi_h2('核心用户与高频跨境场景', 'Target Users & High-Frequency Scenarios'))
text = text.replace('<h3>跨境金融用户</h3>', bi_h3('跨境金融人群', 'Finance Users'))
text = text.replace('<p>关注开户流程、合规限制、支付渠道与资产配置。</p>', bi_p('关注开户流程、合规限制与资产配置。', 'Focus on account opening & regulations.'))
text = text.replace('<h3>文旅活动人群</h3>', bi_h3('文旅活动人群', 'Event Goers'))
text = text.replace('<p>需要快速获取活动信息、排期冲突检测与路线规划。</p>', bi_p('需要快速获取活动信息与路线规划。', 'Require quick event info & conflict detection.'))
text = text.replace('<h3>通勤商务人群</h3>', bi_h3('通勤商务人群', 'Commuters'))
text = text.replace('<p>高频过关、重视通关效率与最优路径决策。</p>', bi_p('高频过关、重视通关效率与最优决策。', 'Value routing efficiency & border flow.'))

# Slide 5
text = text.replace('<h2>三大能力模块，覆盖跨境决策全链路</h2>', bi_h2('三大能力模块，覆盖跨境决策全链路', '3 Core Modules: Full-Link Cross-Border Decision Making'))
text = text.replace('<h3>跨境金融导航</h3>', bi_h3('跨境金融导航', 'Finance Guide'))
text = text.replace('<p>基于最新 RAG 知识库输出开户指南与合规建议。</p>', bi_p('基于最新 RAG 知识库输出开户指南与合规建议。', 'Provide account setup guides & compliance alerts using RAG.'))
text = text.replace('<h3>活动/情报自动化</h3>', bi_h3('活动自动化', 'Event Automation'))
text = text.replace('<p>自动解析海报与官网信息，完成日程冲突检测。</p>', bi_p('自动解析海报与官网信息，完成日程冲突检测。', 'Parse posters/websites automatically for conflict detection.'))
text = text.replace('<h3>实时决策支持</h3>', bi_h3('实时决策支持', 'Real-time Support'))
text = text.replace('<p>接入汇率、口岸人流、港铁班次，推荐最优路径。</p>', bi_p('接入汇率、口岸人流、港铁班次，推荐最优路径。', 'Fetch real-time FX, border flow, and MRT schedules for routing.'))

# Slide 5 SVG Text translated to English for cleaner look & space
s5_svg_old = '''<circle cx="180" cy="120" r="40" fill="rgba(0,87,255,0.08)" stroke="rgba(0,87,255,0.3)" stroke-width="1.5"/>
            <circle cx="180" cy="120" r="28" fill="rgba(0,87,255,0.05)" stroke="rgba(0,87,255,0.15)" stroke-width="0.8"/>
            <text x="180" y="118" text-anchor="middle" font-size="11" fill="#0057ff" font-weight="700">SZ-HK Hub</text>
            <text x="180" y="134" text-anchor="middle" font-size="8" fill="#6b6b80">核心决策引擎</text>
            <!-- 三个模块向外辐射 -->
            <!-- 金融 -->
            <rect x="6" y="28" width="96" height="70" rx="10" fill="rgba(255,20,147,0.06)" stroke="rgba(255,20,147,0.25)" stroke-width="1"/>
            <text x="54" y="52" text-anchor="middle" font-size="10" fill="#ff6b9d" font-weight="700">🏦 跨境金融</text>
            <text x="54" y="70" text-anchor="middle" font-size="7" fill="#7a5a90">开户导航</text>
            <text x="54" y="84" text-anchor="middle" font-size="7" fill="#7a5a90">合规提示</text>
            <line x1="102" y1="70" x2="140" y2="106" stroke="rgba(255,20,147,0.2)" stroke-width="1"/>
            <!-- 文旅 -->
            <rect x="258" y="28" width="96" height="70" rx="10" fill="rgba(0,201,167,0.06)" stroke="rgba(0,201,167,0.25)" stroke-width="1"/>
            <text x="306" y="52" text-anchor="middle" font-size="10" fill="#00c9a7" font-weight="700">🎭 文旅活动</text>
            <text x="306" y="70" text-anchor="middle" font-size="7" fill="#6b9d8b">海报解析</text>
            <text x="306" y="84" text-anchor="middle" font-size="7" fill="#6b9d8b">冲突检测</text>
            <line x1="258" y1="70" x2="220" y2="106" stroke="rgba(0,201,167,0.2)" stroke-width="1"/>
            <!-- 实时 -->
            <rect x="100" y="162" width="160" height="52" rx="10" fill="rgba(255,20,147,0.06)" stroke="rgba(255,20,147,0.25)" stroke-width="1"/>
            <text x="180" y="186" text-anchor="middle" font-size="10" fill="#ff1493" font-weight="700">🚇 实时决策支持</text>
            <text x="180" y="204" text-anchor="middle" font-size="7" fill="#b080a0">汇率 / 口岸人流 / 港铁 / 路径规划</text>
            <line x1="180" y1="160" x2="180" y2="162" stroke="rgba(255,20,147,0.2)" stroke-width="1"/>'''
s5_svg_new = '''<circle cx="180" cy="120" r="40" fill="rgba(0,87,255,0.08)" stroke="rgba(0,87,255,0.3)" stroke-width="1.5"/>
            <circle cx="180" cy="120" r="28" fill="rgba(0,87,255,0.05)" stroke="rgba(0,87,255,0.15)" stroke-width="0.8"/>
            <text x="180" y="118" text-anchor="middle" font-size="11" fill="#0057ff" font-weight="700">SZ-HK Hub</text>
            <text x="180" y="134" text-anchor="middle" font-size="8" fill="#6b6b80">Decision Engine</text>
            <!-- 金融 -->
            <rect x="6" y="28" width="96" height="70" rx="10" fill="rgba(255,20,147,0.06)" stroke="rgba(255,20,147,0.25)" stroke-width="1"/>
            <text x="54" y="52" text-anchor="middle" font-size="10" fill="#ff6b9d" font-weight="700">🏦 Finance</text>
            <text x="54" y="70" text-anchor="middle" font-size="7" fill="#7a5a90">Account Guide</text>
            <text x="54" y="84" text-anchor="middle" font-size="7" fill="#7a5a90">Compliance Alerts</text>
            <line x1="102" y1="70" x2="140" y2="106" stroke="rgba(255,20,147,0.2)" stroke-width="1"/>
            <!-- 文旅 -->
            <rect x="258" y="28" width="96" height="70" rx="10" fill="rgba(0,201,167,0.06)" stroke="rgba(0,201,167,0.25)" stroke-width="1"/>
            <text x="306" y="52" text-anchor="middle" font-size="10" fill="#00c9a7" font-weight="700">🎭 Events</text>
            <text x="306" y="70" text-anchor="middle" font-size="7" fill="#6b9d8b">Poster Parsing</text>
            <text x="306" y="84" text-anchor="middle" font-size="7" fill="#6b9d8b">Conflict Detection</text>
            <line x1="258" y1="70" x2="220" y2="106" stroke="rgba(0,201,167,0.2)" stroke-width="1"/>
            <!-- 实时 -->
            <rect x="100" y="162" width="160" height="52" rx="10" fill="rgba(255,20,147,0.06)" stroke="rgba(255,20,147,0.25)" stroke-width="1"/>
            <text x="180" y="180" text-anchor="middle" font-size="10" fill="#ff1493" font-weight="700">🚇 Real-time Support</text>
            <text x="180" y="198" text-anchor="middle" font-size="7" fill="#b080a0">FX / Flow / MTR / Routing</text>
            <line x1="180" y1="160" x2="180" y2="162" stroke="rgba(255,20,147,0.2)" stroke-width="1"/>'''
text = text.replace(s5_svg_old, s5_svg_new)

# Slide 6
text = text.replace('<h2>多智能体 + 高级 RAG + MCP 实时工具的组合架构</h2>', bi_h2('技术架构：多智能体 + RAG + MCP', 'Technical Architecture: Multi-Agent + RAG + MCP Plugins'))
text = text.replace('<li>Planner Agent：任务拆解、步骤规划。</li>', bi_li('Planner Agent：任务拆解、步骤规划。', 'Task decomposition and planning.'))
text = text.replace('<li>Verifier Agent：反思审查、合规校验。</li>', bi_li('Verifier Agent：反思审查、合规校验。', 'Self-reflection and compliance auditing.'))
text = text.replace('<li>高级 RAG：动态数据源与检索评估。</li>', bi_li('高级 RAG：动态数据源与检索评估。', 'Advanced RAG with dynamic source evaluation.'))
text = text.replace('<li>MCP Server：封装实时汇率、口岸人流、路径规划。</li>', bi_li('MCP Server：封装核心实时小工具。', 'Encapsulated real-time tools via MCP protocols.'))
text = text.replace('<li>Safety Guardrails：敏感词与合规红线。</li>', bi_li('Safety Guardrails：敏感词与合规红线。', 'Safety guardrails for sensitive info.'))

# Slide 7
text = text.replace('<h2>任务拆解 → 工具调用 → 自我审查的协作机制</h2>', bi_h2('Agent 工作流机制', 'Agent Workflow: Decompose → Call → Verify'))
text = text.replace('<h3>协作优势</h3>', bi_h3('协作优势', 'Workflow Advantages'))
text = text.replace('<li>复杂跨境任务可拆解为并行子任务。</li>', bi_li('复杂任务可拆解为并行子任务。', 'Decompose complex needs into parallel queries.'))
text = text.replace('<li>工具调用带来实时数据，减少“拍脑袋”。</li>', bi_li('实时工具调用，减少模型幻觉。', 'Real-time tools replace pure LLM hallucination.'))
text = text.replace('<li>Verifier 负责合规与逻辑自检。</li>', bi_li('独立 Verifier 负责合规自检。', 'Stand-alone Verifier for safety verification.'))
text = text.replace('<li>输出包含依据来源，便于复核。</li>', bi_li('输出包含依据来源，便于用户复核。', 'Evidence-backed outputs build trust.'))

# Slide 9
text = text.replace('<h2>实时决策工具箱：把信息转成行动</h2>', bi_h2('MCP 工具层：把信息转成行动', 'MCP Tools: Translating Info into Action'))
text = text.replace('<h3>接入能力</h3>', bi_h3('核心能力', 'Core Capabilities'))
text = text.replace('<li>实时汇率转换与支付建议。</li>', bi_li('实时汇率转换与支付建议。', 'Real-time FX & Payment advice.'))
text = text.replace('<li>口岸人流量与排队预测。</li>', bi_li('口岸人流量与排队预测。', 'Border crossing flow & queue prediction.'))
text = text.replace('<li>Google Maps 路径规划。</li>', bi_li('Google Maps 路径规划。', 'Transit & pedestrian route planning.'))
text = text.replace('<li>港铁班次与末班车提醒。</li>', bi_li('港铁班次与末班车提醒。', 'MTR schedules and last-train alerts.'))

svg9_old = '''<rect x="370" y="132" width="300" height="90" rx="10" fill="#eef4ff" stroke="#0057ff" stroke-width="2"/>
                  <text x="520" y="162" text-anchor="middle" font-size="18" fill="#0057ff" font-weight="700">MCP 工具层</text>
                  <text x="520" y="188" text-anchor="middle" font-size="13" fill="#49617d">汇率 · 口岸人流 · 路径规划 · 班次</text>

                  <rect x="700" y="72" width="150" height="72" rx="10" fill="#fff0f8" stroke="#ff1493" stroke-width="2"/>
                  <text x="775" y="102" text-anchor="middle" font-size="18" fill="#ff1493" font-weight="700">Verifier</text>
                  <text x="775" y="124" text-anchor="middle" font-size="12" fill="#8a5c77">审查与纠错</text>

                  <rect x="700" y="172" width="150" height="68" rx="10" fill="#fff6e8" stroke="#ff8a00" stroke-width="2"/>
                  <text x="775" y="202" text-anchor="middle" font-size="18" fill="#ff8a00" font-weight="700">输出方案</text>
                  <text x="775" y="224" text-anchor="middle" font-size="12" fill="#8c6b3f">时间 / 路线 / 支付建议</text>

                  <line x1="160" y1="108" x2="195" y2="108" stroke="#0057ff" stroke-width="4" marker-end="url(#arrow-big)"/>
                  <line x1="335" y1="108" x2="370" y2="75" stroke="#0057ff" stroke-width="4" marker-end="url(#arrow-big)"/>
                  <line x1="455" y1="110" x2="455" y2="132" stroke="#00c9a7" stroke-width="4" marker-end="url(#arrow-big)"/>
                  <line x1="670" y1="177" x2="700" y2="108" stroke="#ff1493" stroke-width="4" marker-end="url(#arrow-big)"/>
                  <line x1="775" y1="144" x2="775" y2="172" stroke="#ff8a00" stroke-width="4" marker-end="url(#arrow-big)"/>'''

svg9_new = '''<rect x="370" y="152" width="300" height="90" rx="10" fill="#eef4ff" stroke="#0057ff" stroke-width="2"/>
                  <text x="520" y="188" text-anchor="middle" font-size="20" fill="#0057ff" font-weight="700">MCP Plugins</text>
                  <text x="520" y="214" text-anchor="middle" font-size="15" fill="#49617d">FX Rate · Border Flow · MTR</text>

                  <rect x="700" y="72" width="150" height="72" rx="10" fill="#fff0f8" stroke="#ff1493" stroke-width="2"/>
                  <text x="775" y="102" text-anchor="middle" font-size="18" fill="#ff1493" font-weight="700">Verifier</text>
                  <text x="775" y="124" text-anchor="middle" font-size="12" fill="#8a5c77">Audit & Correct</text>

                  <rect x="700" y="182" width="150" height="68" rx="10" fill="#fff6e8" stroke="#ff8a00" stroke-width="2"/>
                  <text x="775" y="212" text-anchor="middle" font-size="18" fill="#ff8a00" font-weight="700">Final Output</text>
                  <text x="775" y="234" text-anchor="middle" font-size="12" fill="#8c6b3f">Route / Time / Payment</text>

                  <line x1="160" y1="108" x2="195" y2="108" stroke="#0057ff" stroke-width="4" marker-end="url(#arrow-big)"/>
                  <line x1="335" y1="108" x2="370" y2="75" stroke="#0057ff" stroke-width="4" marker-end="url(#arrow-big)"/>
                  <line x1="455" y1="110" x2="455" y2="148" stroke="#00c9a7" stroke-width="4" marker-end="url(#arrow-big)"/>
                  <line x1="670" y1="197" x2="695" y2="108" stroke="#0057ff" stroke-width="4" marker-end="url(#arrow-big)"/>
                  <line x1="775" y1="144" x2="775" y2="178" stroke="#ff8a00" stroke-width="4" marker-end="url(#arrow-big)"/>'''
text = text.replace(svg9_old, svg9_new)
text = text.replace('<text x="265" y="102" text-anchor="middle" font-size="18" fill="#ff1493" font-weight="700">Planner</text>\n                  <text x="265" y="124" text-anchor="middle" font-size="12" fill="#8a5c77">拆解任务与路径</text>',
                    '<text x="265" y="102" text-anchor="middle" font-size="18" fill="#ff1493" font-weight="700">Planner</text>\n                  <text x="265" y="124" text-anchor="middle" font-size="12" fill="#8a5c77">Decomposition</text>')
text = text.replace('<text x="90" y="102" text-anchor="middle" font-size="18" fill="#0057ff" font-weight="700">用户查询</text>\n                  <text x="90" y="124" text-anchor="middle" font-size="12" fill="#55708d">跨境金融 / 出行 / 活动</text>',
                    '<text x="90" y="102" text-anchor="middle" font-size="18" fill="#0057ff" font-weight="700">User Query</text>\n                  <text x="90" y="124" text-anchor="middle" font-size="12" fill="#55708d">Finance / Travel / Events</text>')
text = text.replace('<text x="455" y="68" text-anchor="middle" font-size="18" fill="#00a88c" font-weight="700">RAG</text>\n                  <text x="455" y="90" text-anchor="middle" font-size="12" fill="#5e8f7e">检索 / 向量库 / 证据</text>',
                    '<text x="455" y="68" text-anchor="middle" font-size="18" fill="#00a88c" font-weight="700">RAG DB</text>\n                  <text x="455" y="90" text-anchor="middle" font-size="12" fill="#5e8f7e">Vector Search / Evidence</text>')

# Write back
with open('generated-html/sz-hk-hub-proposal/03-slides.html', 'w', encoding='utf-8') as f:
    f.write(text)

