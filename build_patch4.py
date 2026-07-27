SRC = "/sessions/peaceful-great-bardeen/mnt/outputs/index_22.html"

with open(SRC, "r", encoding="utf-8") as f:
    html = f.read()

OLD = '''    <div class="art-meta"><span id="pm-venue"></span></div>
    <h1 class="art-h1" id="pm-title"></h1>
    <div class="art-body" id="pm-body"></div>
    <img class="art-img" id="pm-poster" src="" alt="" style="width:100%;margin-top:1.5rem;border-radius:8px;display:none">
    <div id="pm-actions" style="margin-top:1.5rem;display:flex;gap:10px;flex-wrap:wrap"></div>'''

assert html.count(OLD) == 1, f"count={html.count(OLD)}"

NEW = '''    <div class="art-meta"><span id="pm-venue"></span></div>
    <h1 class="art-h1" id="pm-title"></h1>
    <img class="art-img" id="pm-poster" src="" alt="" style="width:100%;margin-top:1.5rem;border-radius:8px;display:none">
    <div id="pm-actions" style="margin-top:1.5rem;margin-bottom:1.5rem;display:flex;gap:10px;flex-wrap:wrap"></div>
    <div class="art-body" id="pm-body"></div>'''

html = html.replace(OLD, NEW, 1)

with open(SRC, "w", encoding="utf-8") as f:
    f.write(html)

print("OK, wrote", len(html), "chars")
# placeholder marker unused; real edit handled in separate script
