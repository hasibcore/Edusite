import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('@media (max-width: 1000px) { .container { grid-template-columns: 1fr; } .sidebar { display: none; } }', '''
@media (max-width: 1000px) { 
  .container { grid-template-columns: 1fr; } 
  .sidebar { position: relative; max-height: none; top: 0; padding: 10px; margin-bottom: 20px; }
  #sscMenu, #hscMenu { display: flex; flex-direction: row; overflow-x: auto; gap: 10px; padding-bottom: 10px; }
  .subject-btn { width: auto; white-space: nowrap; flex: 0 0 auto; margin-bottom: 0; }
  .hero h1 { font-size: 2rem; }
  .hero p { font-size: 1rem; }
}
''')

html = html.replace('<link rel="stylesheet" href="style.css">', f'<style>\n{css}\n</style>')

logo_html = '<span style="font-size:2.2rem">🌅</span> <span>Godhuli</span>'
html = re.sub(r'<img src="logo.jpg"[^>]+>', logo_html, html)

html = html.replace('width=device-width, initial-scale=1.0', 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no')

with open('Universal_App.html', 'w', encoding='utf-8') as f:
    f.write(html)
