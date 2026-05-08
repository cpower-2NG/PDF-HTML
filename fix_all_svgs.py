import re

with open('generated-html/sz-hk-hub-proposal/03-slides.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Slide 2: Pain Points
html = html.replace('<rect x="104" y="86" width="72" height="22"', '<rect x="90" y="86" width="105" height="22"')
html = html.replace('<text x="140" y="100" text-anchor="middle" font-size="12" fill="#ff8fab">Fragmented Policy</text>', '<text x="142" y="100" text-anchor="middle" font-size="10" fill="#ff8fab">Fragmented Policy</text>')

html = html.replace('<rect x="184" y="86" width="72" height="22"', '<rect x="200" y="86" width="105" height="22"')
html = html.replace('<text x="220" y="100" text-anchor="middle" font-size="12" fill="#ff8fab">Unclear Compliance</text>', '<text x="252" y="100" text-anchor="middle" font-size="10" fill="#ff8fab">Unclear Compliance</text>')

html = html.replace('<rect x="104" y="130" width="72" height="22"', '<rect x="90" y="130" width="105" height="22"')
html = html.replace('<text x="140" y="144" text-anchor="middle" font-size="12" fill="#f08080">Information Lag</text>', '<text x="142" y="144" text-anchor="middle" font-size="10" fill="#f08080">Information Lag</text>')

html = html.replace('<rect x="184" y="130" width="72" height="22"', '<rect x="200" y="130" width="105" height="22"')
html = html.replace('<text x="220" y="144" text-anchor="middle" font-size="12" fill="#f08080">Data Disconnect</text>', '<text x="252" y="144" text-anchor="middle" font-size="10" fill="#f08080">Data Disconnect</text>')

html = html.replace('<text x="180" y="62" text-anchor="middle" font-size="12" fill="#ff1493">⚠ Info Silos</text>', '<text x="180" y="62" text-anchor="middle" font-size="12" fill="#ff1493">⚠ Info Silos</text>')

# Slide 5: Core Functions
html = html.replace('<rect x="6" y="28" width="96" height="70"', '<rect x="10" y="28" width="110" height="70"')
html = html.replace('<text x="54" y="52"', '<text x="65" y="52"')
html = html.replace('<text x="54" y="70"', '<text x="65" y="70"')
html = html.replace('<text x="54" y="84"', '<text x="65" y="84"')

html = html.replace('<rect x="258" y="28" width="96" height="70"', '<rect x="240" y="28" width="110" height="70"')
html = html.replace('<text x="306" y="52"', '<text x="295" y="52"')
html = html.replace('<text x="306" y="70"', '<text x="295" y="70"')
html = html.replace('<text x="306" y="84"', '<text x="295" y="84"')

# Slide 6: Architecture
html = html.replace('<rect x="36" y="84" width="64"', '<rect x="36" y="84" width="68"')
html = html.replace('<rect x="108" y="84" width="64"', '<rect x="110" y="84" width="65"')
html = html.replace('<rect x="180" y="84" width="64"', '<rect x="180" y="84" width="65"')
html = html.replace('<text x="68" y="115" text-anchor="middle" font-size="12" fill="#b080a0">Decompose</text>', '<text x="70" y="115" text-anchor="middle" font-size="10" fill="#b080a0">Decompose</text>')
html = html.replace('<text x="140" y="115" text-anchor="middle" font-size="12" fill="#b080a0">Audit·Check</text>', '<text x="142" y="115" text-anchor="middle" font-size="10" fill="#b080a0">Audit·Check</text>')

# Slide 7: Agent Workflow
html = html.replace('<text x="180" y="78" text-anchor="middle" font-size="13" fill="#b080a0">Intent → Subtasks → Dependencies</text>', '<text x="180" y="78" text-anchor="middle" font-size="11" fill="#b080a0">Intent → Subtasks → Dependencies</text>')
html = html.replace('<text x="180" y="192" text-anchor="middle" font-size="13" fill="#6aa88a">Anti-Hallucination → Compliance → Trace</text>', '<text x="180" y="192" text-anchor="middle" font-size="11" fill="#6aa88a">Guards → Compliance → Evidence</text>')

# Slide 8: RAG
html = html.replace('<text x="147" y="46" text-anchor="middle" font-size="13" fill="#7a5a90">Clean / Chunk / Dedupe</text>', '<text x="147" y="46" text-anchor="middle" font-size="11" fill="#7a5a90">Clean / Chunk / Dedupe</text>')
html = html.replace('<text x="128" y="97" font-size="12" fill="#6b6b80">Query → Vector Recall → Rerank → Context Assembly</text>', '<text x="128" y="97" font-size="10" fill="#6b6b80">Query → Vector Recall → Rerank → Assembly</text>')

# Slide 9: MCP Pipeline
html = html.replace('<rect x="210" y="72" width="160"', '<rect x="210" y="72" width="150"')
html = html.replace('<rect x="400" y="40" width="200"', '<rect x="390" y="40" width="230"')
html = html.replace('<text x="325" y="132" font-size="14" fill="#6b6b80">Pipeline</text>', '<text x="325" y="145" font-size="14" fill="#6b6b80">Pipeline</text>')


with open('generated-html/sz-hk-hub-proposal/03-slides.html', 'w', encoding='utf-8') as f:
    f.write(html)
