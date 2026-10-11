"""Generates the animated SVGs for the GitHub profile README.
Change ACCENT / BG here and re-run: python3 build_assets.py
"""
from pathlib import Path

ACCENT = "#00D1FF"
BG = "#030405"
FG = "#EDEFF2"
MUTED = "#6B7280"
LINE = "#1A1D22"
SANS = "Inter, -apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
MONO = "'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

REDUCED = """@media (prefers-reduced-motion: reduce){*{animation:none!important}}"""


def wave(y, amp, phase):
    """A smooth 1200px-wide cubic wave. Same command count for every call so SMIL can morph."""
    pts, step = [], 150
    d = f"M -50 {y + amp * phase[0]:.1f}"
    for i in range(1, 10):
        x = -50 + i * step
        a = phase[i % len(phase)]
        d += f" C {x - step*0.66:.1f} {y + amp*phase[(i-1) % len(phase)]:.1f}, {x - step*0.33:.1f} {y + amp*a:.1f}, {x:.1f} {y + amp*a:.1f}"
    return d


# ---------------------------------------------------------------- hero
def hero():
    w, h = 1200, 460
    waves = ""
    seeds = [
        ([0, .8, -.6, .4, -.9, .7, -.3, .9, -.5, .2], [.6, -.7, .9, -.4, .5, -.8, .7, -.2, .4, -.6]),
        ([.5, -.4, .7, -.8, .3, -.6, .9, -.7, .2, -.4], [-.6, .9, -.3, .6, -.8, .4, -.5, .8, -.7, .5]),
        ([-.3, .6, -.9, .5, -.2, .8, -.6, .3, -.7, .9], [.8, -.5, .4, -.9, .7, -.3, .6, -.4, .9, -.2]),
    ]
    for i, (a, b) in enumerate(seeds):
        y, amp, dur = 362 + i * 22, 22 - i * 4, 14 + i * 5
        op = [0.8, 0.45, 0.25][i]
        waves += f"""
  <path fill="none" stroke="url(#strokeFade)" stroke-width="1.1" opacity="{op}" d="{wave(y, amp, a)}">
    <animate attributeName="d" dur="{dur}s" repeatCount="indefinite" calcMode="spline"
      keySplines="0.45 0 0.55 1;0.45 0 0.55 1"
      values="{wave(y, amp, a)};{wave(y, amp, b)};{wave(y, amp, a)}"/>
  </path>"""

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Afif Alamgir, full-stack and AI engineer">
<defs>
  <clipPath id="frame"><rect width="{w}" height="{h}" rx="20"/></clipPath>
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="70"/></filter>
  <linearGradient id="strokeFade" x1="0" x2="1">
    <stop offset="0" stop-color="{ACCENT}" stop-opacity="0"/>
    <stop offset=".5" stop-color="{ACCENT}"/>
    <stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="shine" gradientUnits="userSpaceOnUse" x1="-600" x2="0" y1="0" y2="0">
    <stop offset="0" stop-color="{FG}"/>
    <stop offset=".45" stop-color="{FG}"/>
    <stop offset=".5" stop-color="{ACCENT}"/>
    <stop offset=".55" stop-color="{FG}"/>
    <stop offset="1" stop-color="{FG}"/>
    <animate attributeName="x1" values="-600;1200" dur="7s" repeatCount="indefinite"/>
    <animate attributeName="x2" values="0;1800" dur="7s" repeatCount="indefinite"/>
  </linearGradient>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0H0V40" fill="none" stroke="{FG}" stroke-opacity=".035"/>
  </pattern>
  <radialGradient id="vignette" cx=".5" cy=".4" r=".75">
    <stop offset=".55" stop-color="{BG}" stop-opacity="0"/><stop offset="1" stop-color="{BG}"/>
  </radialGradient>
</defs>
<style>
  .mono{{font-family:{MONO};font-size:13px;letter-spacing:.08em;fill:{MUTED}}}
  .up{{opacity:0;animation:up 1.1s cubic-bezier(.2,.7,.1,1) forwards}}
  .d1{{animation-delay:.15s}} .d2{{animation-delay:.35s}} .d3{{animation-delay:.6s}} .d4{{animation-delay:.9s}}
  @keyframes up{{from{{opacity:0;transform:translateY(18px)}}to{{opacity:1;transform:none}}}}
  .draw{{stroke-dasharray:1400;stroke-dashoffset:1400;animation:draw 2.6s .5s cubic-bezier(.6,0,.2,1) forwards}}
  @keyframes draw{{to{{stroke-dashoffset:0}}}}
  .dot{{animation:pulse 2.4s ease-in-out infinite}}
  @keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
  .scroll{{animation:drop 2.2s cubic-bezier(.6,0,.4,1) infinite}}
  @keyframes drop{{0%{{transform:translateY(-14px);opacity:0}}40%{{opacity:1}}100%{{transform:translateY(14px);opacity:0}}}}
  {REDUCED}
</style>
<g clip-path="url(#frame)">
  <rect width="{w}" height="{h}" fill="{BG}"/>
  <rect width="{w}" height="{h}" fill="url(#grid)"/>
  <g filter="url(#blur)" opacity=".5">
    <circle r="150" fill="{ACCENT}" opacity=".35">
      <animateMotion dur="24s" repeatCount="indefinite" path="M900 120 C 1050 260, 780 380, 700 220 S 820 40, 900 120"/>
    </circle>
    <circle r="120" fill="#5B5BFF" opacity=".25">
      <animateMotion dur="30s" repeatCount="indefinite" path="M300 360 C 160 260, 420 120, 520 260 S 420 420, 300 360"/>
    </circle>
  </g>
  {waves}
  <rect width="{w}" height="{h}" fill="url(#vignette)"/>

  <!-- top bar, like the site -->
  <g class="up">
    <circle class="dot" cx="62" cy="58" r="3.5" fill="{ACCENT}"/>
    <text class="mono" x="76" y="62">23.81°N 90.41°E</text>
    <text class="mono" x="{w-60}" y="62" text-anchor="end">DHAKA · UTC+6</text>
  </g>
  <line x1="56" x2="{w-56}" y1="86" y2="86" stroke="{LINE}"/>

  <g class="up d1"><text class="mono" x="60" y="170">FULL-STACK &amp; AI ENGINEER</text></g>
  <g class="up d2">
    <text x="56" y="262" font-family="{SANS}" font-size="104" letter-spacing="-4">
      <tspan font-weight="700" fill="url(#shine)">Afif</tspan><tspan dx="22" font-weight="300" fill="none" stroke="{FG}" stroke-width="1.2" class="draw">Alamgir</tspan>
    </text>
  </g>
  <g class="up d3">
    <text x="60" y="318" font-family="{SANS}" font-size="20" fill="{MUTED}">I build SaaS platforms, CRMs and AI pipelines, from the Postgres schema to the interface.</text>
  </g>

  <g class="up d4">
    <text class="mono" x="60" y="{h-46}">AFIFALAMGIR.COM ↗</text>
    <text class="mono" x="{w-86}" y="{h-46}" text-anchor="end">SCROLL</text>
    <line x1="{w-66}" x2="{w-66}" y1="{h-70}" y2="{h-36}" stroke="{LINE}"/>
    <line class="scroll" x1="{w-66}" x2="{w-66}" y1="{h-60}" y2="{h-48}" stroke="{ACCENT}" stroke-width="1.5"/>
  </g>
</g>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="20" fill="none" stroke="{FG}" stroke-opacity=".08"/>
</svg>"""


# ---------------------------------------------------------------- section headers
def section(idx, total, label, title):
    w, h = 1200, 128
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}">
<defs>
  <linearGradient id="pulse" gradientUnits="userSpaceOnUse" x1="-300" x2="0">
    <stop offset="0" stop-color="{ACCENT}" stop-opacity="0"/>
    <stop offset=".85" stop-color="{ACCENT}"/>
    <stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/>
    <animate attributeName="x1" values="-300;1200" dur="5s" repeatCount="indefinite" calcMode="spline" keySplines=".6 0 .3 1"/>
    <animate attributeName="x2" values="0;1500" dur="5s" repeatCount="indefinite" calcMode="spline" keySplines=".6 0 .3 1"/>
  </linearGradient>
</defs>
<style>
  .in{{opacity:0;animation:in 1s cubic-bezier(.2,.7,.1,1) forwards}}
  .t{{animation-delay:.15s}}
  @keyframes in{{from{{opacity:0;transform:translateX(-14px)}}to{{opacity:1;transform:none}}}}
  {REDUCED}
</style>
<rect width="{w}" height="{h}" rx="16" fill="{BG}"/>
<g class="in">
  <text x="40" y="44" font-family="{MONO}" font-size="13" letter-spacing="1.5">
    <tspan fill="{ACCENT}">{idx:02d}</tspan><tspan fill="{MUTED}"> / {total:02d}  ·  {label.upper()}</tspan>
  </text>
</g>
<g class="in t"><text x="38" y="94" font-family="{SANS}" font-size="40" font-weight="600" letter-spacing="-1.5" fill="{FG}">{title}</text></g>
<line x1="40" x2="{w-40}" y1="{h-12}" y2="{h-12}" stroke="{LINE}"/>
<line x1="40" x2="{w-40}" y1="{h-12}" y2="{h-12}" stroke="url(#pulse)" stroke-width="1.5"/>
</svg>"""


# ---------------------------------------------------------------- stack marquee
ROW_A = ["Next.js", "React", "TypeScript", "Node.js", "Express", "Python", "FastAPI", "Django",
         "GraphQL", "Tailwind CSS", "Framer Motion", "GSAP", "Three.js", "Flutter", "Dart"]
ROW_B = ["PostgreSQL", "Supabase", "Redis", "Firebase", "Stripe", "OpenAI", "Anthropic", "Gemini",
         "Ollama", "Vector DBs", "PyTorch", "TensorFlow", "Docker", "AWS", "Vercel"]


def marquee():
    w, h = 1200, 150
    cw, gap = 10.2, 56  # monospace char width at 17px, gap between items

    def row(items, y, dur, reverse):
        x, nodes = 0.0, ""
        for it in items:
            tw = len(it) * cw
            nodes += f'<text x="{x:.1f}" y="{y}" textLength="{tw:.1f}" lengthAdjust="spacingAndGlyphs">{it}</text>'
            nodes += f'<circle cx="{x + tw + gap/2:.1f}" cy="{y-5}" r="2" fill="{ACCENT}" opacity=".7"/>'
            x += tw + gap
        L = x
        frm, to = (f"-{L:.1f} 0", "0 0") if reverse else ("0 0", f"-{L:.1f} 0")
        return f"""<g>
    <animateTransform attributeName="transform" type="translate" from="{frm}" to="{to}" dur="{dur}s" repeatCount="indefinite"/>
    <g>{nodes}</g><g transform="translate({L:.1f} 0)">{nodes}</g><g transform="translate({2*L:.1f} 0)">{nodes}</g>
  </g>"""

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Tech stack: {', '.join(ROW_A + ROW_B)}">
<defs>
  <linearGradient id="edge" x1="0" x2="1">
    <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".12" stop-color="#fff"/>
    <stop offset=".88" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
  </linearGradient>
  <mask id="fade"><rect width="{w}" height="{h}" fill="url(#edge)"/></mask>
</defs>
<rect width="{w}" height="{h}" rx="16" fill="{BG}"/>
<g mask="url(#fade)" font-family="{MONO}" font-size="17">
  <g fill="{FG}">{row(ROW_A, 64, 60, False)}</g>
  <g fill="{MUTED}">{row(ROW_B, 106, 70, True)}</g>
</g>
</svg>"""


# ---------------------------------------------------------------- footer
def footer():
    w, h = 1200, 260
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Send the brief. afifalamgir@gmail.com">
<defs>
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
  <clipPath id="c"><rect width="{w}" height="{h}" rx="20"/></clipPath>
</defs>
<style>
  .caret{{animation:blink 1.1s steps(1) infinite}}
  @keyframes blink{{50%{{opacity:0}}}}
  .arrow{{animation:nudge 2.4s cubic-bezier(.6,0,.3,1) infinite}}
  @keyframes nudge{{0%,100%{{transform:translateX(0)}}50%{{transform:translateX(8px)}}}}
  {REDUCED}
</style>
<g clip-path="url(#c)">
  <rect width="{w}" height="{h}" fill="{BG}"/>
  <circle r="160" fill="{ACCENT}" opacity=".18" filter="url(#blur)">
    <animateMotion dur="20s" repeatCount="indefinite" path="M1000 200 C 1150 80, 820 20, 860 160 S 900 300, 1000 200"/>
  </circle>
  <text x="56" y="70" font-family="{MONO}" font-size="13" letter-spacing="1.5" fill="{MUTED}">CONTACT</text>
  <text x="52" y="150" font-family="{SANS}" font-size="72" font-weight="600" letter-spacing="-3" fill="{FG}">Send the <tspan font-weight="300" font-style="italic" fill="{ACCENT}">brief.</tspan><tspan class="caret" dx="10" font-weight="300" fill="{ACCENT}">_</tspan></text>
  <text x="56" y="212" font-family="{MONO}" font-size="15" fill="{MUTED}">afifalamgir@gmail.com</text>
  <g class="arrow"><text x="{w-56}" y="212" text-anchor="end" font-family="{MONO}" font-size="15" fill="{FG}">START A PROJECT →</text></g>
</g>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="20" fill="none" stroke="{FG}" stroke-opacity=".08"/>
</svg>"""


files = {
    "hero.svg": hero(),
    "stack.svg": marquee(),
    "footer.svg": footer(),
    "s-01-expertise.svg": section(1, 5, "Expertise", "What I build"),
    "s-02-stack.svg": section(2, 5, "Stack", "Tools of the trade"),
    "s-03-research.svg": section(3, 5, "Research · Springer Nature · 2024", "Binarized neural networks"),
    "s-04-writing.svg": section(4, 5, "Blog · latest", "Engineering notes"),
    "s-05-activity.svg": section(5, 5, "Activity", "Commit signal"),
}
for name, svg in files.items():
    (OUT / name).write_text(svg, encoding="utf-8")
    print("wrote", name, len(svg), "bytes")
