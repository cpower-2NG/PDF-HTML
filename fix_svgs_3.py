with open('generated-html/sz-hk-hub-proposal/03-slides.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's fix the specific line mapping. Previous script missed it if strings changed in memory or file
html = html.replace('<rect x="90" y="86" width="105" height="22"', '<rect x="80" y="86" width="112" height="22"')
html = html.replace('<rect x="200" y="86" width="105" height="22"', '<rect x="208" y="86" width="112" height="22"')

html = html.replace('<rect x="90" y="130" width="105" height="22"', '<rect x="80" y="130" width="112" height="22"')
html = html.replace('<rect x="200" y="130" width="105" height="22"', '<rect x="208" y="130" width="112" height="22"')

html = html.replace('<text x="142" y="100" text-anchor="middle" font-size="10" fill="#ff8fab">Fragmented Policy</text>', '<text x="136" y="100" text-anchor="middle" font-size="10" fill="#ff8fab">Fragmented Policy</text>')
html = html.replace('<text x="252" y="100" text-anchor="middle" font-size="10" fill="#ff8fab">Unclear Compliance</text>', '<text x="264" y="100" text-anchor="middle" font-size="10" fill="#ff8fab">Unclear Compliance</text>')
html = html.replace('<text x="142" y="144" text-anchor="middle" font-size="10" fill="#f08080">Information Lag</text>', '<text x="136" y="144" text-anchor="middle" font-size="10" fill="#f08080">Information Lag</text>')
html = html.replace('<text x="252" y="144" text-anchor="middle" font-size="10" fill="#f08080">Data Disconnect</text>', '<text x="264" y="144" text-anchor="middle" font-size="10" fill="#f08080">Data Disconnect</text>')

html = html.replace('<rect x="400" y="152" width="320" height="90" rx="10" fill="#eef4ff" stroke="#0057ff" stroke-width="2"/>', '<rect x="360" y="152" width="350" height="90" rx="10" fill="#eef4ff" stroke="#0057ff" stroke-width="2"/>')
html = html.replace('<text x="560" y="188" text-anchor="middle" font-size="20" fill="#0057ff"', '<text x="535" y="188" text-anchor="middle" font-size="20" fill="#0057ff"')
html = html.replace('<text x="560" y="214" text-anchor="middle" font-size="15" fill="#49617d">FX', '<text x="535" y="214" text-anchor="middle" font-size="15" fill="#49617d">FX')
html = html.replace('<text x="560" y="220" text-anchor="middle" font-size="14" fill="#49617d">FX', '<text x="535" y="220" text-anchor="middle" font-size="14" fill="#49617d">FX')


with open('generated-html/sz-hk-hub-proposal/03-slides.html', 'w', encoding='utf-8') as f:
    f.write(html)
