import re

with open('index.html', 'r') as f:
    html = f.read()

# Remove old tags
for old in ['data-16d.js', 'data-16e.js']:
    html = re.sub(r'\s*<script src="js/' + old + '"></script>', '', html)

# Ensure a, b, c, d exist
for fname in ['data-16a.js', 'data-16b.js', 'data-16c.js', 'data-16d.js']:
    tag = '<script src="js/' + fname + '"></script>'
    if tag not in html:
        pos = html.find('<script src="js/script.js"')
        if pos != -1:
            html = html[:pos] + '    ' + tag + '\n    ' + html[pos:]
            print(fname + ' added')
    else:
        print(fname + ' already present')

with open('index.html', 'w') as f:
    f.write(html)

print('Done')

