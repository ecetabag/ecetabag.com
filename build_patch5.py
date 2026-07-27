SRC = "/sessions/peaceful-great-bardeen/mnt/outputs/index_22.html"

with open(SRC, "r", encoding="utf-8") as f:
    html = f.read()

# ---- 1. CSS additions, right after `.proj-impact i{font-size:12px}` ----
OLD_CSS = ".proj-impact i{font-size:12px}"
assert html.count(OLD_CSS) == 1, f"count={html.count(OLD_CSS)}"
NEW_CSS = OLD_CSS + """
.proj-card{gap:0}
.proj-front{display:flex;flex-direction:column;gap:8px}
.proj-visual{width:40px;height:40px;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:2px}
.proj-visual i{font-size:20px}
.proj-stat{font-family:var(--mono);font-size:26px;font-weight:400;color:var(--ink);letter-spacing:-.02em;line-height:1;margin-top:6px}
.proj-stat-label{display:block;font-family:var(--sans);font-size:11px;font-weight:300;color:var(--ink3);margin-top:4px}
.proj-hint{font-size:10px;color:var(--ink3);display:flex;align-items:center;gap:4px;margin-top:6px;transition:opacity .2s var(--ease)}
.proj-hint i{font-size:12px}
.proj-detail{max-height:0;opacity:0;overflow:hidden;margin-top:0;transition:max-height .35s var(--ease),opacity .25s var(--ease),margin-top .35s var(--ease)}
.proj-card:hover .proj-detail,.proj-card.expanded .proj-detail{max-height:320px;opacity:1;margin-top:10px}
.proj-card:hover .proj-hint,.proj-card.expanded .proj-hint{opacity:0}
.proj-detail .proj-desc{margin-bottom:8px}"""
html = html.replace(OLD_CSS, NEW_CSS, 1)

# ---- 2. restructure the whole projects-grid block ----
OLD_GRID = '''<div class="projects-grid reveal">
  <div class="proj-card">
    <span class="proj-tag tag-eng"><i class="ti ti-code"></i>Engineering</span>
    <div class="proj-title">Full-stack recruiting platform</div>
    <div class="proj-desc">Parses resumes (PDF/DOCX), extracts GPA, athletics, leadership, and sales signals, scores candidates using a weighted ranking model, and presents results in an interactive web dashboard for recruiter review.</div>
    <div class="proj-impact"><i class="ti ti-arrow-up-right"></i>Automated evaluation for 200+ applicants, cutting manual screening time</div>
  </div>
  <div class="proj-card">
    <span class="proj-tag tag-fin"><i class="ti ti-receipt"></i>Finance</span>
    <div class="proj-title">Stripe billing reconciliation &amp; ARR audit</div>
    <div class="proj-desc">Audited and cleaned 160+ historical Stripe purchases, matching payments against contractual fee schedules (valuations, rush fees) to verify ARR and one-time charges and correct reporting discrepancies.</div>
    <div class="proj-impact"><i class="ti ti-arrow-up-right"></i>Improved accuracy of ARR reporting across 900+ transactions</div>
  </div>
  <div class="proj-card">
    <span class="proj-tag tag-ops"><i class="ti ti-building"></i>Operations</span>
    <div class="proj-title">SF office search &amp; expansion planning</div>
    <div class="proj-desc">Led office search efforts across San Francisco, evaluating spaces against cost efficiency, team capacity, and long-term operational scalability to support company growth.</div>
    <div class="proj-impact"><i class="ti ti-arrow-up-right"></i>Drove end-to-end expansion planning for a scaling startup</div>
  </div>
  <div class="proj-card">
    <span class="proj-tag tag-ops"><i class="ti ti-gavel"></i>Regulatory</span>
    <div class="proj-title">Government onboarding &amp; regulatory filings</div>
    <div class="proj-desc">Supported legal and operational onboarding through regulatory filings, registrations, and government verification procedures for a trust company operating in a compliance-heavy environment.</div>
    <div class="proj-impact"><i class="ti ti-arrow-up-right"></i>End-to-end regulatory process management</div>
  </div>
  <div class="proj-card">
    <span class="proj-tag tag-ops"><i class="ti ti-truck-delivery"></i>Automation</span>
    <div class="proj-title">Vendor &amp; catering automation (DoorDash)</div>
    <div class="proj-desc">Designed and implemented automated workflows for company-wide meal delivery coordination and bulk procurement, significantly reducing manual administrative overhead and optimizing team logistics.</div>
    <div class="proj-impact"><i class="ti ti-arrow-up-right"></i>Eliminated manual coordination for recurring vendor orders</div>
  </div>
  <div class="proj-card">
    <span class="proj-tag tag-ai"><i class="ti ti-robot"></i>AI &amp; Automation</span>
    <div class="proj-title">Slack lunch bot &amp; AI tooling suite</div>
    <div class="proj-desc">Engineered a lunch automation system using Google Apps Script, Slack webhooks, and Google Sheets. Built an Azure trend-monitoring bot (saving 12+ hrs/week), a 63-tool AI catalog, and AI Slack bots driving ~30% engagement lift.</div>
    <div class="proj-impact"><i class="ti ti-arrow-up-right"></i>~25% reduction in task completion time across internal workflows</div>
  </div>
  <div class="proj-card">
    <span class="proj-tag tag-eng"><i class="ti ti-users"></i>EdTech</span>
    <div class="proj-title">PEAR — peer tutoring matching platform</div>
    <div class="proj-desc">Founded a P2P tutoring platform serving 300+ students with 52 mentors. Developed a JavaScript-based weighted bipartite matching algorithm cutting manual effort by 70%, coordinating 100+ sessions/month.</div>
    <div class="proj-impact"><i class="ti ti-arrow-up-right"></i>85% of participants improved academic outcomes</div>
  </div>
  <div class="proj-card">
    <span class="proj-tag tag-ai"><i class="ti ti-book-2"></i>AI</span>
    <div class="proj-title">AI prompt library &amp; model training</div>
    <div class="proj-desc">Built an AI Prompt Library to train models for specific internal workflows, and created an Azure Industry Trend Monitoring Bot automating real-time market tracking for the team.</div>
    <div class="proj-impact"><i class="ti ti-arrow-up-right"></i>~25% reduction in task completion time; 12+ hrs/week saved</div>
  </div>
</div>'''

assert html.count(OLD_GRID) == 1, f"count={html.count(OLD_GRID)}"

def card(tag_class, icon, tag_label, title, stat, stat_label, desc, impact):
    stat_html = f'<div class="proj-stat">{stat}<span class="proj-stat-label">{stat_label}</span></div>' if stat else ''
    return f'''  <div class="proj-card">
    <div class="proj-front">
      <div class="proj-visual {tag_class}"><i class="ti {icon}"></i></div>
      <span class="proj-tag {tag_class}"><i class="ti {icon}"></i>{tag_label}</span>
      <div class="proj-title">{title}</div>
      {stat_html}
      <div class="proj-hint"><i class="ti ti-plus"></i>Details</div>
    </div>
    <div class="proj-detail">
      <div class="proj-desc">{desc}</div>
      <div class="proj-impact"><i class="ti ti-arrow-up-right"></i>{impact}</div>
    </div>
  </div>'''

cards = [
    card("tag-eng","ti-code","Engineering","Full-stack recruiting platform","200+","applicants evaluated",
         "Parses resumes (PDF/DOCX), extracts GPA, athletics, leadership, and sales signals, scores candidates using a weighted ranking model, and presents results in an interactive web dashboard for recruiter review.",
         "Automated evaluation for 200+ applicants, cutting manual screening time"),
    card("tag-fin","ti-receipt","Finance","Stripe billing reconciliation &amp; ARR audit","900+","transactions reconciled",
         "Audited and cleaned 160+ historical Stripe purchases, matching payments against contractual fee schedules (valuations, rush fees) to verify ARR and one-time charges and correct reporting discrepancies.",
         "Improved accuracy of ARR reporting across 900+ transactions"),
    card("tag-ops","ti-building","Operations","SF office search &amp; expansion planning", None, None,
         "Led office search efforts across San Francisco, evaluating spaces against cost efficiency, team capacity, and long-term operational scalability to support company growth.",
         "Drove end-to-end expansion planning for a scaling startup"),
    card("tag-ops","ti-gavel","Regulatory","Government onboarding &amp; regulatory filings", None, None,
         "Supported legal and operational onboarding through regulatory filings, registrations, and government verification procedures for a trust company operating in a compliance-heavy environment.",
         "End-to-end regulatory process management"),
    card("tag-ops","ti-truck-delivery","Automation","Vendor &amp; catering automation (DoorDash)", None, None,
         "Designed and implemented automated workflows for company-wide meal delivery coordination and bulk procurement, significantly reducing manual administrative overhead and optimizing team logistics.",
         "Eliminated manual coordination for recurring vendor orders"),
    card("tag-ai","ti-robot","AI &amp; Automation","Slack lunch bot &amp; AI tooling suite","~25%","faster task completion",
         "Engineered a lunch automation system using Google Apps Script, Slack webhooks, and Google Sheets. Built an Azure trend-monitoring bot (saving 12+ hrs/week), a 63-tool AI catalog, and AI Slack bots driving ~30% engagement lift.",
         "~25% reduction in task completion time across internal workflows"),
    card("tag-eng","ti-users","EdTech","PEAR &mdash; peer tutoring matching platform","85%","improved academic outcomes",
         "Founded a P2P tutoring platform serving 300+ students with 52 mentors. Developed a JavaScript-based weighted bipartite matching algorithm cutting manual effort by 70%, coordinating 100+ sessions/month.",
         "85% of participants improved academic outcomes"),
    card("tag-ai","ti-book-2","AI","AI prompt library &amp; model training","~25%","faster task completion",
         "Built an AI Prompt Library to train models for specific internal workflows, and created an Azure Industry Trend Monitoring Bot automating real-time market tracking for the team.",
         "~25% reduction in task completion time; 12+ hrs/week saved"),
]

NEW_GRID = '<div class="projects-grid reveal">\n' + '\n'.join(cards) + '\n</div>'
html = html.replace(OLD_GRID, NEW_GRID, 1)

# ---- 3. click-to-toggle JS for touch devices (hover-only wouldn't work there) ----
OLD_SAFETY = "// safety: ensure all reveal sections become visible/clickable\nsetTimeout(function(){document.querySelectorAll('.reveal:not(.visible)').forEach(function(el){el.classList.add('visible');});},1500);"
assert html.count(OLD_SAFETY) == 1, f"count={html.count(OLD_SAFETY)}"
NEW_SAFETY = OLD_SAFETY + """

// project cards: tap/click toggles the detail reveal (hover handles desktop already)
document.querySelectorAll('.proj-card').forEach(function(el){
  el.addEventListener('click',function(){ el.classList.toggle('expanded'); });
});"""
html = html.replace(OLD_SAFETY, NEW_SAFETY, 1)

with open(SRC, "w", encoding="utf-8") as f:
    f.write(html)

print("OK, wrote", len(html), "chars")
