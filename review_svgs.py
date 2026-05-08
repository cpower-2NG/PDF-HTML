import re

with open('generated-html/sz-hk-hub-proposal/03-slides.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract all SVG text elements
svgs = re.findall(r'<svg.*?</svg>', text, flags=re.DOTALL)
for i, svg in enumerate(svgs):
    print(f"--- SVG {i+1} ---")
    texts = re.findall(r'<text[^>]*>([^<]+)</text>', svg)
    for t in texts:
        if re.search(r'[\u4e00-\u9fa5]', t):
            print(f"Chinese text found: {t}")
