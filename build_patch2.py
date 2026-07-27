SRC = "/sessions/peaceful-great-bardeen/mnt/outputs/index_22.html"

with open(SRC, "r", encoding="utf-8") as f:
    html = f.read()

OLD = '.article-content{font-size:16px;color:var(--ink2);line-height:1.85}\n.article-content p{margin-bottom:1.25rem}\n.article-content h2{font-family:var(--serif);font-size:22px;font-weight:300;color:var(--ink);margin:2rem 0 .75rem;letter-spacing:-.01em}\n.article-content blockquote{border-left:3px solid var(--border);padding-left:1.25rem;color:var(--ink3);margin:1.5rem 0;font-style:italic}'

assert html.count(OLD) == 1, f"OLD count = {html.count(OLD)}"

NEW = '.article-content{font-size:14px;color:var(--ink);line-height:1.6}\n.article-content p{margin-bottom:1.1rem;line-height:1.7}\n.article-content h2{font-family:var(--serif);font-size:22px;font-weight:300;color:var(--ink);margin:2rem 0 .75rem;letter-spacing:-.01em}\n.article-content blockquote{border-left:3px solid var(--border);padding-left:1.25rem;color:var(--ink3);margin:1.5rem 0;font-style:italic}\n.article-content ol{margin:0 0 1rem 0}\n.article-content li{margin-bottom:.6rem}\n.article-content a{color:var(--ink);border-bottom:1px solid var(--border2)}'

html = html.replace(OLD, NEW, 1)

with open(SRC, "w", encoding="utf-8") as f:
    f.write(html)

print("OK, wrote", len(html), "chars")
