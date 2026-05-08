with open('generated-html/sz-hk-hub-proposal/03-slides.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's adjust font size and tracking for SVG texts specifically.
# For Slide 2: Pain points overlap
html = html.replace('<rect x="104" y="86" width="72" height="22"', '<rect x="85" y="86" width="95" height="22"')
html = html.replace('<rect x="184" y="86" width="72" height="22"', '<rect x="195" y="86" width="95" height="22"')
html = html.replace('<rect x="104" y="130" width="72" height="22"', '<rect x="85" y="130" width="95" height="22"')
html = html.replace('<rect x="184" y="130" width="72" height="22"', '<rect x="195" y="130" width="95" height="22"')

html = html.replace('<text x="140" y="100" text-anchor="middle" font-size="12" fill="#ff8fab">Fragmented Policy</text>', '<text x="132" y="100" text-anchor="middle" font-size="9" fill="#ff8fab">Fragmented Policy</text>')
html = html.replace('<text x="220" y="100" text-anchor="middle" font-size="12" fill="#ff8fab">Unclear Compliance</text>', '<text x="242" y="100" text-anchor="middle" font-size="9" fill="#ff8fab">Unclear Compliance</text>')
html = html.replace('<text x="140" y="144" text-anchor="middle" font-size="12" fill="#f08080">Information Lag</text>', '<text x="132" y="144" text-anchor="middle" font-size="9" fill="#f08080">Information Lag</text>')
html = html.replace('<text x="220" y="144" text-anchor="middle" font-size="12" fill="#f08080">Data Disconnect</text>', '<text x="242" y="144" text-anchor="middle" font-size="9" fill="#f08080">Data Disconnect</text>')

# Slide 5: Modules 
html = html.replace('<rect x="6" y="28" width="96" height="70"', '<rect x="10" y="28" width="105" height="70"')
html = html.replace('<rect x="258" y="28" width="96" height="70"', '<rect x="245" y="28" width="105" height="70"')

html = html.replace('<text x="54" y="70" text-anchor="middle" font-size="13" fill="#7a5a90">Account Guide</text>', '<text x="62" y="70" text-anchor="middle" font-size="11" fill="#7a5a90">Account Guide</text>')
html = html.replace('<text x="54" y="84" text-anchor="middle" font-size="13" fill="#7a5a90">Compliance Alerts</text>', '<text x="62" y="84" text-anchor="middle" font-size="10" fill="#7a5a90">Compliance Alerts</text>')
html = html.replace('<text x="54" y="52" text-anchor="middle" font-size="12" fill="#ff6b9d" font-weight="700">🏦 Finance</text>', '<text x="62" y="52" text-anchor="middle" font-size="12" fill="#ff6b9d" font-weight="700">🏦 Finance</text>')

html = html.replace('<text x="306" y="70" text-anchor="middle" font-size="13" fill="#6b9d8b">Poster Parsing</text>', '<text x="297" y="70" text-anchor="middle" font-size="11" fill="#6b9d8b">Poster Parsing</text>')
html = html.replace('<text x="306" y="84" text-anchor="middle" font-size="13" fill="#6b9d8b">Conflict Detection</text>', '<text x="297" y="84" text-anchor="middle" font-size="10" fill="#6b9d8b">Conflict Detection</text>')
html = html.replace('<text x="306" y="52" text-anchor="middle" font-size="12" fill="#00c9a7" font-weight="700">🎭 Events</text>', '<text x="297" y="52" text-anchor="middle" font-size="12" fill="#00c9a7" font-weight="700">🎭 Events</text>')

html = html.replace('<text x="180" y="198" text-anchor="middle" font-size="13" fill="#b080a0">FX / Flow / MTR / Routing</text>', '<text x="180" y="198" text-anchor="middle" font-size="11" fill="#b080a0">FX / Flow / MTR / Routing</text>')

# Slide 6: Architecture Layer 3 text overflow
html = html.replace('<text x="95" y="184" text-anchor="middle" font-size="8.5" fill="#6aa88a">Qdrant / Chroma / FAISS</text>', '<text x="95" y="184" text-anchor="middle" font-size="7.5" fill="#6aa88a">Qdrant/Chroma/FAISS</text>')
html = html.replace('<text x="259" y="184" text-anchor="middle" font-size="12" fill="#b89040">Routing / MTR Schedule</text>', '<text x="259" y="184" text-anchor="middle" font-size="10" fill="#b89040">Routing / MTR Schedule</text>')

# Slide 8: Data processing text overflow
html = html.replace('<text x="49" y="46" text-anchor="middle" font-size="13" fill="#6b6b80">Crawler / API / PDF</text>', '<text x="49" y="46" text-anchor="middle" font-size="10" fill="#6b6b80">Crawler / API / PDF</text>')

# Slide 9: Large pipeline SVG overlapping
html = html.replace('<text x="325" y="132" font-size="14" fill="#6b6b80">Pipeline</text>', '<text x="325" y="145" font-size="14" fill="#6b6b80">Pipeline</text>')
html = html.replace('<text x="290" y="124" text-anchor="middle" font-size="14" fill="#8a5c77">Decomposition</text>', '<text x="290" y="128" text-anchor="middle" font-size="13" fill="#8a5c77">Decomposition</text>')
html = html.replace('<text x="500" y="90" text-anchor="middle" font-size="14" fill="#5e8f7e">Vector Search / Evidence</text>', '<text x="500" y="94" text-anchor="middle" font-size="13" fill="#5e8f7e">Vector Search/Evidence</text>')
html = html.replace('<text x="560" y="214" text-anchor="middle" font-size="15" fill="#49617d">FX Rate · Border Flow · MTR</text>', '<text x="560" y="220" text-anchor="middle" font-size="14" fill="#49617d">FX Rate · Border Flow · MTR</text>')

with open('generated-html/sz-hk-hub-proposal/03-slides.html', 'w', encoding='utf-8') as f:
    f.write(html)
