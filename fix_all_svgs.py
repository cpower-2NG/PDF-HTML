import re

with open('generated-html/sz-hk-hub-proposal/03-slides.html', 'r', encoding='utf-8') as f:
    text = f.read()

# SVG 1
text = text.replace('⚠ 信息孤岛', '⚠ Info Silos')
text = text.replace('⚠ 实时缺失', '⚠ No Real-time')
text = text.replace('>香港</text>', '>Hong Kong</text>')
text = text.replace('>深圳</text>', '>Shenzhen</text>')
text = text.replace('政策碎片化', 'Fragmented Policy')
text = text.replace('合规模糊', 'Unclear Compliance')
text = text.replace('信息滞后', 'Information Lag')
text = text.replace('数据断联', 'Data Disconnect')
text = text.replace('缺一个「跨境专业决策中枢」', 'Missing Domain-Specific Agent')

# SVG 2
text = text.replace('通用 LLM', 'General LLM')
text = text.replace('✗ 易产生幻觉', '✗ Hallucination')
text = text.replace('✗ 合规风险高', '✗ High Risk')
text = text.replace('✗ 信息不实时', '✗ Stale Info')
text = text.replace('✗ 不可追溯', '✗ Untraceable')
text = text.replace('专业 Agent', 'Domain Agent')
text = text.replace('✓ 可验证检索', '✓ Verified RAG')
text = text.replace('✓ 合规护栏', '✓ Safety Guardrails')
text = text.replace('✓ 实时工具', '✓ Real-time MCP')
text = text.replace('✓ 可追溯', '✓ Traceable Output')

# SVG 5 (Slide 7 - Agent Workflow)
text = text.replace('👤 用户查询', '👤 User Query')
text = text.replace('Planner · 任务拆解 &amp; 步骤规划', 'Planner: Decompose &amp; Plan')
text = text.replace('意图识别 → 子任务分解 → 依赖排序', 'Intent → Subtasks → Dependencies')
text = text.replace('RAG 检索', 'RAG Search')
text = text.replace('知识库查询', 'Knowledge Base')
text = text.replace('MCP 工具', 'MCP Tools')
text = text.replace('实时数据调用', 'Real-time API')
text = text.replace('LLM 推理', 'LLM Core')
text = text.replace('逻辑推理', 'Reasoning')
text = text.replace('Verifier · 合规审查 &amp; 逻辑校验', 'Verifier: Audit &amp; Validate')
text = text.replace('幻觉检测 → 合规检查 → 依据溯源', 'Anti-Hallucination → Compliance → Trace')
text = text.replace('反馈修正', 'Fallback/Retry')
text = text.replace('✅ 可执行方案输出', '✅ Final Executable Plan')

# SVG 6 (Slide 8 - RAG)
text = text.replace('📥 数据采集', '📥 Data Collection')
text = text.replace('爬虫 / API / PDF', 'Crawler / API / PDF')
text = text.replace('🔧 处理', '🔧 Processing')
text = text.replace('清洗 / 切分 / 去重', 'Clean / Chunk / Dedupe')
text = text.replace('向量化处理', 'Embedding')
text = text.replace('>向量库</text>', '>Vector DB</text>')
text = text.replace('🔍 检索阶段：', '🔍 Retrieval Stage:')
text = text.replace('Query → 向量召回 → 重排序 → 上下文组装', 'Query → Vector Recall → Rerank → Context Assembly')
text = text.replace('📊 评估指标：Hit Rate / MRR', '📊 Metrics: Hit Rate / MRR')

# Layout and font-size check
text = text.replace('font-size="7"', 'font-size="9"')
text = text.replace('font-size="8"', 'font-size="10"')
text = text.replace('font-size="9"', 'font-size="11"')
text = text.replace('font-size="10"', 'font-size="12"')
text = text.replace('font-size="11"', 'font-size="13"')

with open('generated-html/sz-hk-hub-proposal/03-slides.html', 'w', encoding='utf-8') as f:
    f.write(text)
