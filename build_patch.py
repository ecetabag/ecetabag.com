import sys

SRC = "/sessions/peaceful-great-bardeen/mnt/uploads/index_22.html"
DST = "/sessions/peaceful-great-bardeen/mnt/outputs/index_22.html"

with open(SRC, "r", encoding="utf-8") as f:
    html = f.read()

# ---- 1. Card markup: add id + cursor + "Read more" line ----
OLD_CARD = '<div class="paper-card"><span class="paper-venue">Paper</span><div class="paper-title">The Benefits of Learning Block-Based Coding Languages</div><div class="paper-desc">How Scratch-style programming and peer learning foster deeper coding comprehension in early learners.</div></div>'
NEW_CARD = '<div class="paper-card" id="blockcoding-card" style="cursor:pointer"><span class="paper-venue">Paper</span><div class="paper-title">The Benefits of Learning Block-Based Coding Languages</div><div class="paper-desc">How Scratch-style programming and peer learning foster deeper coding comprehension in early learners.</div><div class="paper-desc" style="margin-top:8px;color:var(--ink);font-weight:500">Read more →</div></div>'

assert html.count(OLD_CARD) == 1, f"OLD_CARD count = {html.count(OLD_CARD)}"
html = html.replace(OLD_CARD, NEW_CARD, 1)

# ---- 2. BLOCKCODING_HTML const, inserted right after `if(!modal)return;` ----
BODY_HTML = '''"<h2>Introduction</h2><p>Block-based programming languages guide all new learners through an informative process of understanding the fundamentals of coding before starting text-based languages. Throughout various summits and competitions which encourage block-based coding through peer learning in collaborative workspaces, learners exhibited exciting learning behavior.</p>"+
"<h2>Coding Summit from Students\u2019 Perspective</h2><p>Every year, as the HISAR CS Team, we host a 2-day-long Coding Summit, aiming to encourage and teach students the fundamentals of computer programming through various coding languages, including 4 block-based languages. Our annual summit helps enrich over 300 students\u2019 current information about coding and creative problem-solving. We welcome everyone to this event, where the teachers and students swap roles. The participants\u2019 ages range from a 5-year-old boy to a 60-year-old adult - they all have different levels of understanding and experience of programming. During the courses, the booklets that are created for each class by the Hisar CS students are used.</p>"+
"<h2>Technovation</h2><p>Most girls do not receive enough guidance when it comes to programming. By giving girls a platform to express their opinions on global issues, Technovation encourages girls to code and find creative solutions by using a block-based coding language, MIT App Inventor. In this competition, participants are expected to solve crucial world problems, which can require complex coding skills.</p>"+
"<h2>Rapid Prototyping</h2><p>Block-based platforms can be very useful in prototyping as they do not require advanced knowledge and experience. Users can learn the functions of the blocks by reading the phrases on them and start to build a prototype in a day as it brings down the barriers of accessing technology and understanding it. According to Technovation\u2019s data, participants are able to produce complex applications in a very short time. One of the example projects from Technovation is a game called Mole Mash, where the player tries to tap on the moles before they disappear. In this project, the students use variables, timer, loops, components, and etc.</p>"+
"<h2>Learning From Our Peers</h2><p>The instructors of the Coding Summit consist of high school students that are passionate about the coding language that they are teaching. They are proficient in their involved language and have written a starter guide \u201cbooklet\u201d based on their lesson content, which is distributed to participants after the lessons. Peer learning is effectively practiced in the Coding Summit, ensuring direct interaction between the instructor and participants. Since the instructors and participants are close in terms of age, their similar minds result in greater understanding in the participants. Participants may feel more comfortable and open when interacting with a fellow student. Peer learning in the classroom environment can also reinforce the instructors' own learning.</p>"+
"<h2>The Courses</h2><p>The essential courses we provide for our participants are Scratch, MIT App Inventor, Microbit, Lego EV3, Dash &amp; Dot, Python, Java, Fusion, NLP, Swift, and Arduino. As seen throughout the years, the majority of the children and beginners prefer and get redirected to the block-based languages. The reason is that it is more enjoyable and introductory - especially for children and they can develop emotional resilience, patience, and persistence through experimentation which is provided more with block-based programming.</p>"+
"<h2>Collecting Feedback</h2><p>The most important thing for us is collecting feedback from the participants. We want them to be honest and encourage us to give us positive feedback and point out opportunities for improvement for next year. Thankfully, in the previous years, almost everyone were inspired and many commented that we \u201copened a new path\u201d for them.</p>"+
"<h2>Hisar Coding Summit at ACS</h2><p>This year HisarCS students organized the 2nd ICSI Summit in ASC Athens, Greece. The students from ASC, AFS Thessaloniki and Hisar School gave various workshops. Four of the twelve workshops were given by our students. The organization has achieved a great success. With 4 workshops: Scratch, Arduino, Python and Fusion, we introduced 400 students to our field. Again, the booklets that were used during the sessions were made by the HisarCS students. We got to know a different culture and had the opportunity organize an inspiring organization with our peers from different cultures and geographies.</p>"+
"<h2>Conclusion</h2><p>Block-based programming languages were observed to prepare students to learn text-based programming languages in events such as the summits and Technovation. These events not only introduced young people to block-based programming but also helped their logical skills and motivated them to pursue their interests. Block-based programming\u2019s benefit in rapid prototyping was found to be noteworthy, as most of the participants had already coded their own program by the time the event had ended.</p>"+
"<h2>References</h2><ol style=\\"padding-left:1.2rem;color:var(--ink3);font-size:14px;line-height:1.7\\">"+
"<li>Impact of Visual Aids in Enhancing the Learning Process: Case Research: District Der, Ghazi Khan. Ghulam Shabiralyani. Khuram Shahzad Hasan. Naqvi Hamad. Nadeem Iqbal. G.C University Faisalabad. Punjab Pakistan. Journal of Education and Practice. ISSN 2222-1735 (Paper) ISSN 2222-288X (Online) Vol.6. No.19, 2015.</li>"+
"<li>Ha, Katherine (2005) - Getting the Picture: Using Visual Learning Techniques to Foster Higher Order Thinking Skills and Encourage Connections in the Secondary Classroom; Language Arts Journal of Michigan: Vol. 21: Iss. 2, Article 10. Available at: <a href=\\"https://doi.org/10.9707/2168-149X.1198\\" target=\\"_blank\\" rel=\\"noopener\\">https://doi.org/10.9707/2168-149X.1198</a>.</li>"+
"<li>Examples of Algorithmic Thinking in Programming Education, Juraj Hromkovi\u010d, Tobias Kohn, Dennis Komm, Giovanni Serafini. Department of Computer Science, ETH Zurich, Universit\u00e4tstrasse 6, 8092 Zurich, Switzerland.</li>"+
"<li>Robotics and Engineering for Middle and High School Students to Develop Computational Thinking, Shuchi Grover, Stanford University. Annual Meeting of the American Educational Research Association New Orleans, April 7-11, 2011.</li>"+
"<li>Williams, R. (2009). Visual Learning Theory. <a href=\\"http://www.aweoregon.org/research_theory.html\\" target=\\"_blank\\" rel=\\"noopener\\">http://www.aweoregon.org/research_theory.html</a>.</li>"+
"<li>Anatomy of the Brain. Tonya Hines. CMI. Mayfield Clinic, Cincinnati, Ohio. Mayfield Brain &amp; Spine, April 2018.</li>"+
"<li>M. Young, The Technical Writer's Handbook. Mill Valley, CA: University Science, 1989.</li>"+
"<li>Dewan, Pauline. Words Versus Pictures: Leveraging the Research on Visual Communication. The Canadian Journal of Library and Information Practice and Research. 2015. pdewan@wlu.ca.</li>"+
"<li>Raiyn, Jamal. \\"The Role of Visual learning in Improving Students' High-Order Thinking Skills.\\" Journal of Education and Practice. Computer Science Department. Al Qasemi Academic College for Education. Baqa El Gharbia, Israel. 2016, <a href=\\"https://files.eric.ed.gov/fulltext/EJ1112894.pdf\\" target=\\"_blank\\" rel=\\"noopener\\">files.eric.ed.gov/fulltext/EJ1112894.pdf</a>.</li>"+
"<li>Lai, A., Yang, S. (2011) The learning effect of visualized programming learning on 6th graders' problem-solving.</li>"+
"</ol>"'''

INSERT_AFTER = "  if(!modal)return;\n"
assert html.count(INSERT_AFTER) == 1, f"INSERT_AFTER count = {html.count(INSERT_AFTER)}"
const_block = "  const BLOCKCODING_HTML=\n" + BODY_HTML + ";\n"
html = html.replace(INSERT_AFTER, INSERT_AFTER + const_block, 1)

# ---- 3. New click listener for #blockcoding-card, inserted right before back.addEventListener ----
OLD_BACK_LINE = "  back.addEventListener('click',()=>{modal.classList.remove('open');document.body.style.overflow='';});"
assert html.count(OLD_BACK_LINE) == 1, f"OLD_BACK_LINE count = {html.count(OLD_BACK_LINE)}"

NEW_LISTENER = '''  document.addEventListener('click',(ev)=>{
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
'''

html = html.replace(OLD_BACK_LINE, NEW_LISTENER + OLD_BACK_LINE, 1)

# ---- 4. small CSS additions so h2/ol inside the paper modal body match site style ----
OLD_CSS = "#pm-body p{margin-bottom:1.1rem;line-height:1.7}"
assert html.count(OLD_CSS) == 1, f"OLD_CSS count = {html.count(OLD_CSS)}"
NEW_CSS = OLD_CSS + "\n#pm-body h2{font-family:var(--serif);font-size:22px;font-weight:300;color:var(--ink);margin:2rem 0 .75rem;letter-spacing:-.01em}\n#pm-body ol{margin:0 0 1rem 0}\n#pm-body li{margin-bottom:.6rem}\n#pm-body a{color:var(--ink);border-bottom:1px solid var(--border2)}"
html = html.replace(OLD_CSS, NEW_CSS, 1)

with open(DST, "w", encoding="utf-8") as f:
    f.write(html)

print("OK, wrote", len(html), "chars to", DST)
