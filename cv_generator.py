"""
CV Generator — Senior Backend & Security Engineer Edition
Tailored for highly selective backend / IT-focused engineering roles.
Requires: pip install reportlab
"""

import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas as pdfcanvas

OUTPUT_FILE = "/home/Xashe/Documents/myCV1.pdf"

# ── DIMENSIONS ───────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4
SIDEBAR_W      = 62 * mm
MAIN_X         = SIDEBAR_W + 10
MAIN_W         = PAGE_W - MAIN_X - 12 * mm
MARGIN_V       = 14 * mm

# ── PALETTE ──────────────────────────────────────────────────────────────────
SIDEBAR_BG   = colors.HexColor("#0E1C2F")
ACCENT       = colors.HexColor("#00D4AA")
ACCENT2      = colors.HexColor("#1A7A6E")
SIDEBAR_TEXT = colors.HexColor("#CBD5E1")
SIDEBAR_DIM  = colors.HexColor("#64748B")
MAIN_BG      = colors.HexColor("#F8FAFC")
HEADER_BG    = colors.HexColor("#0E1C2F")
DARK_TEXT    = colors.HexColor("#0F172A")
MID_TEXT     = colors.HexColor("#475569")
RULE_COLOR   = colors.HexColor("#E2E8F0")
TAG_BG       = colors.HexColor("#E8F5F3")
TAG_TEXT     = colors.HexColor("#0F766E")
GOLD         = colors.HexColor("#F59E0B")

# ── PERSONAL DATA ─────────────────────────────────────────────────────────────
FULL_NAME  = "Omer Faruk Polat"
JOB_TITLE  = "Backend Engineer  ·  Security Researcher  ·  Systems Specialist"
EMAIL      = "xashe107@gmail.com"
GITHUB     = "github.com/hellowaste344"
TWITTER    = "x.com/XAshe_01"
LOCATION   = "Istanbul, TR  ·  Open to relocate"
WEBSITE    = "zenonai.net"

# ── PERSONAL STATEMENT ────────────────────────────────────────────────────────
PERSONAL_STATEMENT = (
    "I am a backend developer with 3+ years shipping product experience at the "
    "intersection of security and infrastructure. Proven track record across "
    "SaaS delivery, red-team engagements, and hardware level implementation. "
    "Following curiosity depth in system-design alongside security hardening."
)

# ── EXPERIENCE ────────────────────────────────────────────────────────────────
# Each entry: (title, company_location, date_range, bullet_list)
EXPERIENCE = [
    (
        "Founder & Lead Backend Engineer",
        "ZenonAI · zenonai.net  ·  Remote",
        "Jan 2026 – Present",
        [
            "Architected and shipped a privacy-first, fully offline AI assistant "
            "from zero to paying customers — solo, end-to-end, with no cloud "
            "dependency; manages real production traffic and an active user base.",
            "Designed a high-performance Rust + Python backend with a Tauri/React "
            "desktop client and local LLM inference via Ollama; responsible for all "
            "infrastructure, CI/CD pipelines, release management, and product roadmap.",
            "Owned the full SDLC: threat modelling, secure coding practices, "
            "automated testing, and user onboarding."
            "response latency on commodity hardware.",
        ]
    ),
    (
        "Freelance",
        "Self-Employed  ·  Remote",
        "Jun 2024 – Present",
        [
            "Delivered end-to-end penetration tests scripts across web, network. "
            "Consistently identified critical vulnerability findings missed "
            "by prior assessments.",
            "Produced executive-grade findings reports with scored risk ratings "
            "and prioritized remediation roadmaps across all engagements.",
            "Holds OSCP and CRTP certifications, validating real-world exploit against vulnerable machines. "
        ]
    ),
    (
        "Open-Source Contributor & Independent Researcher",
        "Various Projects  ·  GitHub",
        "2023 – Present",
        [
            "Shipped performance-critical patches to Python and C++ security "
            "tooling in active open-source projects; contributions merged after "
            "structured code review with maintainers.",
            "Competed regularly in CTF competitions, publishing detailed technical "
            "write-ups that have attracted 200+ GitHub stars across community",
        ]
    ),
]

# ── PROJECTS ──────────────────────────────────────────────────────────────────
# Each entry: (name, stack_label, one_sentence_description)
PROJECTS = [
    (
        "GPU-Accelerated Hash Cracker",
        "Python / C++ · CUDA",
        "Implemented CUDA-parallel hash cracking across SHA-256/512, MD5, and "
        "SHA-1 achieving ~8× throughput over optimised CPU baseline; "
        "benchmarked across multiple GPU generations.",
    ),
    (
        "Layer 2–4 Recon Orchestrator",
        "Python / C++",
        "Built a fully async recon pipeline integrating subdomain enumeration, "
        "port scanning, service fingerprinting, and automated CVE correlation "
        "into a single execution workflow.",
    ),
    (
        "Headless Web Scraper Framework",
        "Python · Playwright",
        "Engineered a resilient scraping framework with dynamic proxy rotation, "
        "adaptive rate limiting, and session-state management capable of "
        "sustaining high-throughput extraction under extreme conditions.",
    ),
    (
        "Red Team Toolkit",
        "Python / Bash",
        "Developed a modular offensive toolkit covering enumeration, exploitation, "
        "and post-exploitation phases; used in lab and sanctioned engagement "
        "environments with configurable targets.",
    ),
    (
        "ANN from Scratch",
        "Python · NumPy",
        "Implemented a full neural network engine used calculus for forward pass, backpropagation, "
        "and gradient descent from first principles. Validated against known benchmark datasets."
        "increased the supervised prediction to 99.788%",
    ),
    (
        "RL Maze Solver",
        "Python",
        "Built a Q-learning agent with configurable exploration. "
        "Visualised each episode with matplotlib; Adjusted agent' weights "
        "after each failure. Increased total efficiency by 400%.",
    ),
]

# ── SKILLS ────────────────────────────────────────────────────────────────────
SKILLS_GROUPED = [ 
    ("Languages",     ["Python", "C/C++", "Bash/Shell"]),
    ("Security",      ["Red Teaming", "Pen Testing"]),
    ("Backend",       ["REST APIs", "System Design", "Performance Tuning"]),
    ("ML / AI",       ["TensorFlow", "PyTorch", "YOLO", "OpenCV", "NLP", "RL"]),
    ("Tools",         ["Metasploit", "Burp Suite", "Ghidra", "Wireshark"]),
    ("Infra / Cloud", ["Docker", "Kubernetes", "SDK", "CI/CD", "Debian"]),
    ("Networking",    ["TCP/IP", "DNS", "TLS/SSL", "iptables", "VPN/VPS"]),
    ("Dev",           ["Git", "CMake", "GDB"]),
]

# ── CERTIFICATIONS ────────────────────────────────────────────────────────────
# Each entry: (abbreviation, full_name, year)
CERTIFICATIONS = [
    ("OSCP", "Offensive Security Certified Professional", "2025"),
    ("CRTP", "Certified Red Team Professional — HTB",     "2026"),
]

# ── EDUCATION ─────────────────────────────────────────────────────────────────
EDUCATION = (
    "B.Sc. Computer Engineering",
    "Bahcesehir University, Istanbul",
    "Expected 2027  ·  Systems Programming & Network Security",
    [
        "Valedictorian — High School",
        "National Exam Rank: Top 0.3 %",
    ],
)

# ── LANGUAGES ────────────────────────────────────────────────────────────────
LANGUAGES = [
    ("English", "Professional"),
    ("Turkish", "Native")
]

# ── HIGHLIGHTS (header badges) ────────────────────────────────────────────────
HIGHLIGHTS = [
    "3+ Years Backend & Security",
    "Shipped Production SaaS",
    "Backend Dev · Offensive Sec",
    "OSCP · CRTP Certified",
]


# ══════════════════════════════════════════════════════════════════════════════
#  DRAWING HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def rr(c, x, y, w, h, radius, fill_color, stroke_color=None, lw=0.5):
    c.setFillColor(fill_color)
    if stroke_color:
        c.setStrokeColor(stroke_color)
        c.setLineWidth(lw)
        c.roundRect(x, y, w, h, radius, fill=1, stroke=1)
    else:
        c.roundRect(x, y, w, h, radius, fill=1, stroke=0)


def txt(c, string, x, y, font="Helvetica", size=9, color=DARK_TEXT, align="left"):
    c.setFont(font, size)
    c.setFillColor(color)
    if align == "right":
        c.drawRightString(x, y, string)
    elif align == "center":
        c.drawCentredString(x, y, string)
    else:
        c.drawString(x, y, string)


def wrap_text(c, text, x, y, max_w, font="Helvetica", size=9,
              color=DARK_TEXT, leading=13):
    """Word-wrap text. Returns Y position after last line."""
    c.setFont(font, size)
    c.setFillColor(color)
    words = text.split()
    line, cy = "", y
    for w in words:
        test = (line + " " + w).strip()
        if c.stringWidth(test, font, size) <= max_w:
            line = test
        else:
            if line:
                c.drawString(x, cy, line)
                cy -= leading
            line = w
    if line:
        c.drawString(x, cy, line)
        cy -= leading
    return cy


def draw_inline_tags(c, tags, x, y, max_x,
                     bg=TAG_BG, fg=TAG_TEXT,
                     font="Helvetica", size=7, pad_x=5, pad_y=1.8,
                     tag_h=4.5*mm, gap_x=3, gap_y=3):
    """Draw pill-shaped tags, wrapping at max_x. Returns Y below last row."""
    cx, cy = x, y
    for tag in tags:
        tw = c.stringWidth(tag, font, size) + pad_x * 2
        if cx + tw > max_x and cx > x:
            cx = x
            cy -= (tag_h + gap_y)
        rr(c, cx, cy - tag_h + pad_y, tw, tag_h, 2, bg)
        c.setFont(font, size)
        c.setFillColor(fg)
        c.drawString(cx + pad_x, cy - tag_h + pad_y + 1.4, tag)
        cx += tw + gap_x
    return cy - (tag_h + gap_y)


def sidebar_section(c, label, y):
    y -= 5
    c.setFillColor(ACCENT)
    c.rect(8*mm, y, 2.5, 10, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(ACCENT)
    c.drawString(12.5*mm, y + 2, label.upper())
    y -= 15
    return y


def main_section(c, label, y):
    y -= 7
    c.setStrokeColor(RULE_COLOR)
    c.setLineWidth(0.6)
    c.line(MAIN_X, y + 5, PAGE_W - 12*mm, y + 5)
    c.setFillColor(ACCENT)
    c.rect(MAIN_X, y - 5, 3, 13, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(DARK_TEXT)
    c.drawString(MAIN_X + 7, y + 1, label.upper())
    lw = c.stringWidth(label.upper(), "Helvetica-Bold", 9.5)
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.2)
    c.line(MAIN_X + 7, y - 1, MAIN_X + 7 + lw, y - 1)
    y -= 16
    return y


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE SECTIONS
# ══════════════════════════════════════════════════════════════════════════════

def draw_background(c):
    c.setFillColor(SIDEBAR_BG)
    c.rect(0, 0, SIDEBAR_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(MAIN_BG)
    c.rect(SIDEBAR_W, 0, PAGE_W - SIDEBAR_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(SIDEBAR_W - 1.5, 0, 1.5, PAGE_H, fill=1, stroke=0)


def draw_header(c):
    HEADER_H = 38 * mm
    c.setFillColor(HEADER_BG)
    c.rect(0, PAGE_H - HEADER_H, PAGE_W, HEADER_H, fill=1, stroke=0)
    # top accent stripe
    c.setFillColor(ACCENT)
    c.rect(0, PAGE_H - 2.5, PAGE_W, 2.5, fill=1, stroke=0)

    # name
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(colors.white)
    c.drawString(10*mm, PAGE_H - 15*mm, FULL_NAME)

    # job title
    c.setFont("Helvetica", 9.5)
    c.setFillColor(ACCENT)
    c.drawString(10*mm, PAGE_H - 23*mm, JOB_TITLE)

    # ── highlight badges ──
    bx = 10 * mm
    by = PAGE_H - 29*mm
    for badge in HIGHLIGHTS:
        bw = c.stringWidth(badge, "Helvetica-Bold", 7) + 14
        rr(c, bx, by - 1, bw, 10, 3,
           colors.HexColor("#1E3A52"),
           stroke_color=ACCENT, lw=0.6)
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(ACCENT)
        c.drawString(bx + 7, by + 1.5, badge)
        bx += bw + 5

    # contact row
    contacts = [EMAIL, GITHUB, WEBSITE, TWITTER]
    cx = 10 * mm
    contact_y = PAGE_H - 36*mm
    for i, item in enumerate(contacts):
        if i > 0:
            c.setFillColor(ACCENT)
            c.circle(cx + 2, contact_y + 3, 1.2, fill=1, stroke=0)
            cx += 8
        c.setFont("Helvetica", 7.5)
        c.setFillColor(SIDEBAR_TEXT)
        c.drawString(cx, contact_y, item)
        cx += c.stringWidth(item, "Helvetica", 7.5) + 6


def draw_sidebar(c):
    HEADER_H = 38 * mm
    y = PAGE_H - HEADER_H - 8 * mm

    # ── CONTACT ──
    y = sidebar_section(c, "Contact", y)
    items = [
        ("Email",    EMAIL),
        ("GitHub",   GITHUB),
        ("Twitter",  TWITTER),
        ("Web",      WEBSITE),
        ("Location", "Istanbul, TR"),
    ]
    for label, val in items:
        c.setFont("Helvetica-Bold", 6.5)
        c.setFillColor(SIDEBAR_DIM)
        c.drawString(8*mm, y, label)
        display = val if c.stringWidth(val, "Helvetica", 7) < (SIDEBAR_W - 28*mm) else val[:20] + "…"
        c.setFont("Helvetica", 7)
        c.setFillColor(SIDEBAR_TEXT)
        c.drawString(24*mm, y, display)
        y -= 11

    # ── PERSONAL STATEMENT ──
    y -= 5
    ps_x      = 9 * mm
    ps_max_w  = SIDEBAR_W - 14 * mm
    font_ps   = "Helvetica-Oblique"
    size_ps   = 7

    c.setFont(font_ps, size_ps)
    words  = PERSONAL_STATEMENT.split()
    lines  = []
    line   = ""
    for w in words:
        test = (line + " " + w).strip()
        if c.stringWidth(test, font_ps, size_ps) <= ps_max_w:
            line = test
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)

    block_h = len(lines) * 10 + 6
    rr(c, 7*mm, y - block_h + 6, SIDEBAR_W - 11*mm, block_h, 3,
       colors.HexColor("#162840"))
    c.setFillColor(ACCENT)
    c.rect(7*mm, y - block_h + 6, 2, block_h, fill=1, stroke=0)

    c.setFont(font_ps, size_ps)
    c.setFillColor(colors.HexColor("#94A3B8"))
    cy = y
    for ln in lines:
        c.drawString(ps_x + 2, cy, ln)
        cy -= 10
    y = cy - 4

    # ── SKILLS ──
    y -= 4
    y = sidebar_section(c, "Skills", y)
    tag_h = 4.5 * mm
    for category, tags in SKILLS_GROUPED:
        c.setFont("Helvetica-Bold", 6.5)
        c.setFillColor(SIDEBAR_DIM)
        c.drawString(8*mm, y, category)
        y -= 10
        cx = 8 * mm
        for tag in tags:
            tw = c.stringWidth(tag, "Helvetica", 6.5) + 8
            if cx + tw > SIDEBAR_W - 5*mm and cx > 8*mm:
                cx = 8 * mm
                y -= (tag_h + 2)
            rr(c, cx, y - tag_h + 2.5, tw, tag_h - 1, 2,
               colors.HexColor("#1E3A52"))
            c.setFont("Helvetica", 6.5)
            c.setFillColor(ACCENT)
            c.drawString(cx + 4, y - tag_h + 4.2, tag)
            cx += tw + 3
        y -= (tag_h + 6)

    # ── CERTIFICATIONS ──
    y -= 2
    y = sidebar_section(c, "Certifications", y)
    for abbr, name, yr in CERTIFICATIONS:
        badge_w = c.stringWidth(abbr, "Helvetica-Bold", 6.5) + 12
        bx = 8 * mm
        rr(c, bx, y - 5, badge_w, 11, 2, ACCENT)
        c.setFont("Helvetica-Bold", 6.5)
        c.setFillColor(SIDEBAR_BG)
        c.drawCentredString(bx + badge_w / 2, y - 2, abbr)
        tx = bx + badge_w + 4
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(SIDEBAR_TEXT)
        c.drawString(tx, y, name[:28] if len(name) > 28 else name)
        c.setFont("Helvetica", 6.5)
        c.setFillColor(SIDEBAR_DIM)
        c.drawString(tx, y - 9, yr)
        y -= 22

    # ── EDUCATION ──
    y -= 2
    y = sidebar_section(c, "Education", y)
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(SIDEBAR_TEXT)
    c.drawString(8*mm, y, EDUCATION[0])
    y -= 11
    c.setFont("Helvetica-Oblique", 7)
    c.setFillColor(ACCENT)
    c.drawString(8*mm, y, EDUCATION[1])
    y -= 10
    note_words = EDUCATION[2].split()
    line = ""
    c.setFont("Helvetica", 6.5)
    c.setFillColor(SIDEBAR_DIM)
    for w in note_words:
        test = (line + " " + w).strip()
        if c.stringWidth(test, "Helvetica", 6.5) <= SIDEBAR_W - 14*mm:
            line = test
        else:
            c.drawString(8*mm, y, line)
            y -= 9
            line = w
    if line:
        c.drawString(8*mm, y, line)
        y -= 11
    for ach in EDUCATION[3]:
        c.setFillColor(GOLD)
        c.circle(9.5*mm, y + 2.5, 1.5, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 6.5)
        c.setFillColor(ACCENT)
        c.drawString(12*mm, y, ach)
        y -= 10

    # ── LANGUAGES ──
    y -= 4
    y = sidebar_section(c, "Languages", y)
    for lang, level in LANGUAGES:
        c.setFont("Helvetica-Bold", 7.5)
        c.setFillColor(SIDEBAR_TEXT)
        c.drawString(8*mm, y, lang)
        lw = c.stringWidth(level, "Helvetica", 6.5) + 8
        rr(c, SIDEBAR_W - 6*mm - lw, y - 2, lw, 9, 2,
           colors.HexColor("#1E3A52"))
        c.setFont("Helvetica", 6.5)
        c.setFillColor(ACCENT)
        c.drawString(SIDEBAR_W - 6*mm - lw + 4, y - 0.5, level)
        y -= 14


def draw_main(c):
    HEADER_H = 38 * mm
    y = PAGE_H - HEADER_H - 7 * mm
    max_w = MAIN_W

    # ══ EXPERIENCE ══════════════════════════════════════════════════════════
    y = main_section(c, "Experience", y)

    for idx, (role, company, dates, bullets) in enumerate(EXPERIENCE):
        card_bg   = colors.HexColor("#F0F9F7") if idx % 2 == 0 else colors.white
        bar_color = ACCENT if idx % 2 == 0 else colors.HexColor("#1A7A6E")

        n_bullet_lines = sum(max(1, int(len(b) / 72)) for b in bullets)
        card_h = 14 + n_bullet_lines * 12 + 14
        if y - card_h < 10 * mm:
            break

        rr(c, MAIN_X - 2, y - card_h + 6, max_w + 4, card_h, 3, card_bg)
        c.setFillColor(bar_color)
        c.rect(MAIN_X - 2, y - card_h + 6, 3, card_h, fill=1, stroke=0)

        # role title
        c.setFont("Helvetica-Bold", 9.5)
        c.setFillColor(DARK_TEXT)
        c.drawString(MAIN_X + 5, y, role)

        # date badge
        dw = c.stringWidth(dates, "Helvetica", 7) + 10
        rr(c, PAGE_W - 12*mm - dw, y - 1, dw, 9.5, 2,
           colors.HexColor("#E2E8F0"))
        c.setFont("Helvetica", 7)
        c.setFillColor(MID_TEXT)
        c.drawString(PAGE_W - 12*mm - dw + 5, y + 0.5, dates)

        y -= 11
        c.setFont("Helvetica-Oblique", 7.5)
        c.setFillColor(ACCENT2)
        c.drawString(MAIN_X + 5, y, company)
        y -= 12

        for bullet in bullets:
            c.setFillColor(ACCENT)
            c.circle(MAIN_X + 9, y + 2.5, 1.5, fill=1, stroke=0)
            y = wrap_text(c, bullet,
                          MAIN_X + 15, y,
                          max_w - 15, font="Helvetica", size=8,
                          color=MID_TEXT, leading=11)
            y -= 1
        '''
        tag_y = y - 2
        draw_inline_tags(c, tags, MAIN_X + 5, tag_y,
                         PAGE_W - 12*mm,
                         bg=TAG_BG, fg=TAG_TEXT,
   
        font="Helvetica", size=6.5)
        '''
    y -= 14

    # ══ NOTABLE PROJECTS ════════════════════════════════════════════════════
    y = main_section(c, "Notable Projects", y)

    col_w  = (max_w - 5) / 2
    col2_x = MAIN_X + col_w + 5

    for i, (name, stack, desc) in enumerate(PROJECTS):
        col_x = MAIN_X if i % 2 == 0 else col2_x
        if i % 2 == 0 and i > 0:
            y -= 42

        card_bg = colors.HexColor("#F0F9F7") if i % 2 == 0 else colors.white
        bar_col = ACCENT if i % 2 == 0 else colors.HexColor("#1A7A6E")
        card_h  = 40

        rr(c, col_x, y - card_h + 6, col_w, card_h, 3, card_bg)
        c.setFillColor(bar_col)
        c.rect(col_x, y - card_h + 6, 3, card_h, fill=1, stroke=0)

        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(DARK_TEXT)
        c.drawString(col_x + 6, y, name)

        sw = c.stringWidth(stack, "Helvetica", 6.5) + 8
        rr(c, col_x + col_w - sw - 2, y - 1, sw, 8.5, 2, TAG_BG)
        c.setFont("Helvetica", 6.5)
        c.setFillColor(TAG_TEXT)
        c.drawString(col_x + col_w - sw + 2, y + 0.5, stack)

        y_desc = y - 11
        wrap_text(c, desc,
                  col_x + 6, y_desc,
                  col_w - 12, font="Helvetica", size=7.5,
                  color=MID_TEXT, leading=11)

        if i % 2 != 0:
            y -= 42

    if len(PROJECTS) % 2 != 0:
        y -= 42


def draw_footer(c):
    c.setFillColor(SIDEBAR_BG)
    c.rect(0, 0, PAGE_W, 8*mm, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(0, 8*mm, PAGE_W, 0.8, fill=1, stroke=0)
    c.setFont("Helvetica", 7)
    c.setFillColor(SIDEBAR_DIM)
    c.drawCentredString(PAGE_W / 2, 3*mm,
                        f"{FULL_NAME}  ·  {EMAIL}  ·  {WEBSITE}  ·  Open to senior backend & security roles")


# ══════════════════════════════════════════════════════════════════════════════
#  BUILD
# ══════════════════════════════════════════════════════════════════════════════

def build_pdf():
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    c = pdfcanvas.Canvas(OUTPUT_FILE, pagesize=A4)
    c.setTitle(f"CV — {FULL_NAME}")

    draw_background(c)
    draw_header(c)
    draw_sidebar(c)
    draw_main(c)
    draw_footer(c)

    c.save()
    print(f"CV saved → {OUTPUT_FILE}")


if __name__ == "__main__":
    build_pdf()
