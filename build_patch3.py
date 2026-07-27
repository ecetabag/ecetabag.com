SRC = "/sessions/peaceful-great-bardeen/mnt/outputs/index_22.html"

with open(SRC, "r", encoding="utf-8") as f:
    html = f.read()

with open("/sessions/peaceful-great-bardeen/mnt/outputs/poster_display_b64.txt") as f:
    display_b64 = f.read().strip()
with open("/sessions/peaceful-great-bardeen/mnt/outputs/poster_download_b64.txt") as f:
    download_b64 = f.read().strip()

# ---- 1. add "Published at" paragraph right after the Introduction paragraph ----
OLD_INTRO_END = '<h2>Introduction</h2><p>Block-based programming languages guide all new learners through an informative process of understanding the fundamentals of coding before starting text-based languages. Throughout various summits and competitions which encourage block-based coding through peer learning in collaborative workspaces, learners exhibited exciting learning behavior.</p>"+'
assert html.count(OLD_INTRO_END) == 1, f"count={html.count(OLD_INTRO_END)}"
NEW_INTRO_END = OLD_INTRO_END + '\n"<p style=\\"color:var(--ink3);font-style:italic\\">Published at: <a href=\\"https://cs.wellesley.edu/~blocks-and-beyond/2019\\" target=\\"_blank\\" rel=\\"noopener\\" style=\\"color:var(--ink);border-bottom:1px solid var(--border2)\\">cs.wellesley.edu/~blocks-and-beyond/2019</a> \u2014 Blocks &amp; Beyond Workshop, 2019.</p>"+'
html = html.replace(OLD_INTRO_END, NEW_INTRO_END, 1)

# ---- 2. define BLOCKCODING_POSTER / BLOCKCODING_POSTER_DL right before "const modal=document.getElementById('paper-modal');" ----
ANCHOR = "  const modal=document.getElementById('paper-modal');\n"
assert html.count(ANCHOR) == 1, f"count={html.count(ANCHOR)}"
const_imgs = (
    '  const BLOCKCODING_POSTER="data:image/jpeg;base64,' + display_b64 + '";\n'
    '  const BLOCKCODING_POSTER_DL="' + download_b64 + '";\n'
)
html = html.replace(ANCHOR, const_imgs + ANCHOR, 1)

# ---- 3. update the #blockcoding-card click handler to show poster + actions ----
OLD_HANDLER = """  document.addEventListener('click',(ev)=>{
    const card=ev.target.closest('#blockcoding-card');
    if(!card)return;
    document.getElementById('pm-venue').textContent='Paper';
    document.getElementById('pm-title').textContent='The Benefits of Learning Block-Based Coding Languages';
    document.getElementById('pm-body').innerHTML=BLOCKCODING_HTML;
    const poster=document.getElementById('pm-poster');
    poster.style.display='none';poster.src='';poster.alt='';
    const actions=document.getElementById('pm-actions');
    actions.innerHTML='';
    modal.classList.add('open');document.body.style.overflow='hidden';
  });
"""
assert html.count(OLD_HANDLER) == 1, f"count={html.count(OLD_HANDLER)}"

NEW_HANDLER = """  document.addEventListener('click',(ev)=>{
    const card=ev.target.closest('#blockcoding-card');
    if(!card)return;
    document.getElementById('pm-venue').textContent='Paper \\u00b7 2019';
    document.getElementById('pm-title').textContent='The Benefits of Learning Block-Based Coding Languages';
    document.getElementById('pm-body').innerHTML=BLOCKCODING_HTML;
    const poster=document.getElementById('pm-poster');
    poster.src=BLOCKCODING_POSTER;poster.alt='Teaching Students Block-Based Programming in Utilising the Coding Summit and Rapid Prototyping - poster';poster.style.display='block';
    const actions=document.getElementById('pm-actions');
    actions.innerHTML='';
    const openBtn=document.createElement('a');
    openBtn.className='pm-btn primary';openBtn.href='https://cs.wellesley.edu/~blocks-and-beyond/2019';openBtn.target='_blank';openBtn.rel='noopener';
    openBtn.innerHTML='<i class="ti ti-external-link"></i> View Publication';
    const posterBtn=document.createElement('button');
    posterBtn.className='pm-btn';posterBtn.innerHTML='<i class="ti ti-photo"></i> Download Poster';
    posterBtn.addEventListener('click',()=>dl(BLOCKCODING_POSTER_DL,'Block-Based-Coding-Poster.jpg','image/jpeg'));
    actions.appendChild(openBtn);actions.appendChild(posterBtn);
    modal.classList.add('open');document.body.style.overflow='hidden';
  });
"""
html = html.replace(OLD_HANDLER, NEW_HANDLER, 1)

with open(SRC, "w", encoding="utf-8") as f:
    f.write(html)

print("OK, wrote", len(html), "chars")
