<!DOCTYPE html>
<html lang="en" data-os="mac" data-writer="markdown" data-data="sample">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Build Your Executive Assistant Agent — Setup Guide</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{
  --navy:#1E2761;
  --navy-dk:#10143A;
  --navy-deep:#0B0E2B;
  --ink:#171B2E;
  --muted:#5B6584;
  --muted-soft:#8890AC;
  --paper:#FBFCFE;
  --card:#F3F6FC;
  --card-hover:#EAF0FA;
  --line:#E1E6F2;
  --line-strong:#C9D2E8;
  --teal:#00A896;
  --teal-dk:#017C72;
  --teal-tint:#DFF5F1;
  --alert:#B8452E;
  --alert-tint:#FBEAE5;
  --amber:#B7791F;
  --amber-tint:#FCF3DF;
  --code-bg:#10142B;
  --code-text:#D3E3FF;
  --code-accent:#7DEFE2;
  --code-dim:#7783A8;
  --radius:14px;
  --radius-sm:9px;
  --shadow:0 10px 30px -12px rgba(16,20,58,.18);
  --shadow-sm:0 2px 10px -4px rgba(16,20,58,.12);
}

*{box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{
  margin:0;
  background:var(--paper);
  color:var(--ink);
  font-family:'Inter',system-ui,sans-serif;
  font-size:16px;
  line-height:1.55;
  -webkit-font-smoothing:antialiased;
}
h1,h2,h3,h4{
  font-family:'Fraunces',Georgia,serif;
  color:var(--navy);
  margin:0 0 .4em;
  line-height:1.12;
}
p{margin:0 0 1em;}
a{color:var(--teal-dk);}
code{font-family:'IBM Plex Mono',Consolas,monospace;}
::selection{background:var(--teal-tint);color:var(--navy-dk);}
@media (prefers-reduced-motion: reduce){
  html{scroll-behavior:auto;}
  *{animation-duration:.001ms !important; transition-duration:.001ms !important;}
}

/* ---------- layout shell ---------- */
.wrap{max-width:1180px;margin:0 auto;padding:0 28px;}

/* ---------- sticky top bar ---------- */
.topbar{
  position:sticky;top:0;z-index:40;
  background:rgba(251,252,254,.92);
  backdrop-filter:blur(10px);
  border-bottom:1px solid var(--line);
}
.topbar-inner{
  max-width:1180px;margin:0 auto;padding:12px 28px;
  display:flex;align-items:center;gap:18px;
}
.topbar-title{
  font-family:'Fraunces',serif;font-weight:600;font-size:16px;color:var(--navy);
  white-space:nowrap;
}
.topbar-title span{color:var(--teal-dk);}
.progress-track{
  flex:1;height:6px;background:var(--line);border-radius:99px;overflow:hidden;
  min-width:80px;
}
.progress-fill{
  height:100%;background:linear-gradient(90deg,var(--teal-dk),var(--teal));
  width:0%;transition:width .35s ease;border-radius:99px;
}
.progress-label{font-size:12.5px;color:var(--muted);white-space:nowrap;font-variant-numeric:tabular-nums;}
.chip-row{display:flex;gap:6px;}
.chip{
  font-size:11.5px;font-weight:600;color:var(--navy);background:var(--card);
  border:1px solid var(--line);padding:4px 9px;border-radius:99px;
  cursor:pointer;white-space:nowrap;transition:background .15s,border-color .15s;
}
.chip:hover{background:var(--card-hover);border-color:var(--line-strong);}
@media (max-width:760px){ .chip-row{display:none;} .topbar-title{font-size:14px;} }

/* ---------- hero ---------- */
.hero{
  background:
    radial-gradient(760px 420px at 88% -12%, rgba(0,168,150,.35), transparent 60%),
    radial-gradient(600px 360px at 8% 110%, rgba(122,150,255,.14), transparent 60%),
    linear-gradient(180deg,var(--navy-deep),var(--navy-dk) 70%);
  color:#fff;
  padding:64px 0 54px;
  position:relative;
  overflow:hidden;
}
.hero-eyebrow{
  font-size:12.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
  color:var(--code-accent);margin-bottom:14px;display:flex;align-items:center;gap:10px;
}
.hero-eyebrow::before{content:"";width:22px;height:1px;background:var(--code-accent);display:inline-block;}
.hero h1{
  color:#fff;font-size:clamp(32px,4.6vw,52px);font-weight:600;max-width:16ch;margin-bottom:.3em;
}
.hero-sub{
  color:#BFC9EE;font-size:18px;max-width:56ch;margin-bottom:28px;
}
.hero-meta{display:flex;flex-wrap:wrap;gap:28px;margin-bottom:8px;}
.hero-meta-item{display:flex;flex-direction:column;gap:2px;}
.hero-meta-item .num{font-family:'Fraunces',serif;font-size:26px;color:#fff;font-weight:600;}
.hero-meta-item .lbl{font-size:12.5px;color:#9AA6D4;text-transform:uppercase;letter-spacing:.06em;}
.hero-cta{
  margin-top:30px;display:inline-flex;align-items:center;gap:10px;
  background:var(--teal);color:#08201C;font-weight:700;font-size:14.5px;
  padding:12px 20px;border-radius:99px;text-decoration:none;
  box-shadow:0 8px 22px -8px rgba(0,168,150,.7);
  transition:transform .15s ease, box-shadow .15s ease;
}
.hero-cta:hover{transform:translateY(-1px);box-shadow:0 12px 26px -8px rgba(0,168,150,.85);}
.hero-cta svg{width:15px;height:15px;}

/* ---------- config panel ---------- */
.config{
  background:#fff;
  border:1px solid var(--line);
  border-radius:var(--radius);
  box-shadow:var(--shadow);
  margin-top:-38px;
  position:relative;
  z-index:5;
  padding:30px 32px 26px;
}
.config-head{display:flex;align-items:baseline;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:6px;}
.config-head h2{font-size:22px;margin-bottom:0;}
.config-head p{color:var(--muted);font-size:14.5px;margin:0;}
.config-note{
  font-size:13px;color:var(--teal-dk);background:var(--teal-tint);
  padding:3px 10px;border-radius:99px;font-weight:600;
}
.decision-grid{
  display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:22px;
}
@media (max-width:900px){.decision-grid{grid-template-columns:1fr;}}
.decision{border-top:1px solid var(--line);padding-top:16px;}
.decision-label{
  font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;
  color:var(--navy);margin-bottom:3px;
}
.decision-hint{font-size:13px;color:var(--muted);margin-bottom:12px;}
.opt-group{display:flex;flex-direction:column;gap:8px;}
.opt{
  display:flex;align-items:center;gap:10px;
  border:1.5px solid var(--line);border-radius:10px;padding:10px 12px;
  cursor:pointer;background:var(--paper);transition:border-color .15s,background .15s;
  font-size:14px;
}
.opt:hover{border-color:var(--line-strong);}
.opt input{accent-color:var(--teal-dk);width:15px;height:15px;flex:none;}
.opt .opt-text strong{display:block;font-size:14px;color:var(--ink);}
.opt .opt-text small{display:block;color:var(--muted-soft);font-size:12px;margin-top:1px;}
.opt.selected{border-color:var(--teal);background:var(--teal-tint);}
.opt.selected .opt-text strong{color:var(--teal-dk);}
.opt.disabled{opacity:.42;cursor:not-allowed;}
.opt.disabled:hover{border-color:var(--line);}

/* ---------- main layout ---------- */
.layout{display:grid;grid-template-columns:230px 1fr;gap:44px;padding:44px 0 20px;align-items:start;}
@media (max-width:900px){.layout{grid-template-columns:1fr;}}

/* rail */
.rail{position:sticky;top:70px;align-self:start;}
@media (max-width:900px){.rail{display:none;}}
.rail-title{font-size:11.5px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-soft);margin-bottom:14px;padding-left:26px;}
.rail-list{list-style:none;margin:0;padding:0;position:relative;}
.rail-list::before{
  content:"";position:absolute;left:9px;top:6px;bottom:6px;width:2px;background:var(--line);
}
.rail-item{position:relative;padding:0 0 0 26px;margin-bottom:2px;}
.rail-link{
  display:block;padding:7px 0;font-size:13.5px;color:var(--muted);text-decoration:none;
  border-radius:6px;transition:color .15s;
}
.rail-link:hover{color:var(--navy);}
.rail-dot{
  position:absolute;left:2px;top:11px;width:16px;height:16px;border-radius:50%;
  background:#fff;border:2px solid var(--line-strong);transition:all .2s;
}
.rail-item.active .rail-link{color:var(--navy);font-weight:600;}
.rail-item.active .rail-dot{border-color:var(--navy);box-shadow:0 0 0 3px rgba(30,39,97,.12);}
.rail-item.done .rail-dot{background:var(--teal);border-color:var(--teal);}
.rail-item.done .rail-dot::after{
  content:"";position:absolute;left:4px;top:1.5px;width:4px;height:8px;
  border-right:2px solid #fff;border-bottom:2px solid #fff;transform:rotate(40deg);
}

/* mobile jump */
.mobile-jump{display:none;margin:0 0 30px;}
@media (max-width:900px){.mobile-jump{display:block;}}
.mobile-jump select{
  width:100%;padding:12px 14px;border-radius:10px;border:1.5px solid var(--line-strong);
  font-family:'Inter';font-size:14.5px;color:var(--navy);background:#fff;
}

/* content */
.content{min-width:0;}
.lead-block{margin-bottom:36px;}
.lead-block h2{font-size:22px;margin-bottom:10px;}
.lead-block p{color:var(--muted);font-size:15px;max-width:66ch;}

/* step card */
.step{
  scroll-margin-top:80px;
  background:#fff;border:1px solid var(--line);border-radius:var(--radius);
  padding:30px 32px 28px;margin-bottom:26px;box-shadow:var(--shadow-sm);
}
.step-top{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;margin-bottom:14px;}
.step-heading{display:flex;align-items:baseline;gap:14px;}
.step-num{
  font-family:'Fraunces',serif;font-weight:600;font-size:15px;color:var(--teal-dk);
  background:var(--teal-tint);width:34px;height:34px;border-radius:9px;
  display:flex;align-items:center;justify-content:center;flex:none;
}
.step-title-wrap h3{font-size:21px;margin-bottom:2px;}
.step-meta{display:flex;gap:10px;align-items:center;flex-wrap:wrap;}
.step-time{font-size:12.5px;color:var(--muted-soft);}
.badge{
  font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;
  padding:3px 8px;border-radius:6px;background:var(--card);color:var(--navy);
  border:1px solid var(--line);
}
.badge.adapts{background:#EFF1FF;color:#3C46A6;border-color:#DADCFF;}
.step-check{display:flex;align-items:center;gap:7px;cursor:pointer;flex:none;user-select:none;}
.step-check input{width:18px;height:18px;accent-color:var(--teal-dk);cursor:pointer;}
.step-check span{font-size:12.5px;color:var(--muted);font-weight:600;}
.step-body p{color:var(--ink);font-size:15px;}
.step-body p.muted{color:var(--muted);font-size:14px;}

/* code block */
.code{
  background:var(--code-bg);border-radius:10px;margin:14px 0 16px;overflow:hidden;
  box-shadow:0 6px 18px -8px rgba(9,12,35,.5);
}
.code-head{
  display:flex;align-items:center;justify-content:space-between;
  padding:8px 14px;border-bottom:1px solid rgba(255,255,255,.08);
}
.code-lang{font-size:11px;color:var(--code-dim);text-transform:uppercase;letter-spacing:.07em;font-weight:600;}
.copy-btn{
  font-family:'Inter';font-size:11.5px;font-weight:600;color:var(--code-accent);
  background:rgba(125,239,226,.1);border:1px solid rgba(125,239,226,.25);
  border-radius:6px;padding:4px 9px;cursor:pointer;transition:background .15s;
}
.copy-btn:hover{background:rgba(125,239,226,.2);}
.copy-btn.copied{color:#fff;background:var(--teal-dk);border-color:var(--teal-dk);}
.code pre{
  margin:0;padding:15px 16px 17px;overflow-x:auto;
  font-family:'IBM Plex Mono',Consolas,monospace;font-size:13px;line-height:1.62;color:var(--code-text);
}
.code pre .c{color:var(--code-dim);}
.code pre .s{color:var(--code-accent);}

/* branch panels */
.branch{display:none;}
.branch.is-visible{display:block;}
.branch-note{
  font-size:13.5px;color:var(--muted);background:var(--card);border:1px dashed var(--line-strong);
  border-radius:9px;padding:12px 14px;margin:14px 0;
}

/* callouts */
.callout{
  display:flex;gap:11px;border-radius:10px;padding:13px 15px;margin:14px 0;font-size:14px;
}
.callout .ic{flex:none;width:19px;height:19px;margin-top:1px;}
.callout.hint{background:var(--teal-tint);border:1px solid #BFE9E1;}
.callout.hint .ic{color:var(--teal-dk);}
.callout.hint strong{color:var(--teal-dk);}
.callout p{margin:0;color:#0E4842;}
.callout p strong{color:var(--teal-dk);}

.trouble{margin:18px 0 4px;}
.trouble-title{
  display:flex;align-items:center;gap:8px;font-size:12.5px;font-weight:700;text-transform:uppercase;
  letter-spacing:.05em;color:var(--alert);margin-bottom:10px;
}
.trouble-title .ic{width:15px;height:15px;}
.trouble-list{border:1px solid var(--alert-tint);border-radius:10px;overflow:hidden;}
.trouble-row{
  display:grid;grid-template-columns:1fr 1.3fr;gap:14px;padding:11px 15px;
  border-top:1px solid var(--alert-tint);background:#fff;
}
.trouble-row:first-child{border-top:none;}
.trouble-row:nth-child(odd){background:var(--alert-tint);}
.trouble-sym{font-family:'IBM Plex Mono';font-size:12.5px;color:#7A2E1D;display:flex;align-items:flex-start;gap:6px;}
.trouble-fix{font-size:13.5px;color:var(--ink);display:flex;align-items:flex-start;gap:6px;}
@media (max-width:600px){.trouble-row{grid-template-columns:1fr;}}

/* option tabs inside a step (for writer/data branches shown as sub-tabs) */
.subtabs{display:flex;gap:6px;flex-wrap:wrap;margin:4px 0 4px;}
.subtab{
  font-size:12.5px;font-weight:600;padding:6px 11px;border-radius:99px;
  background:var(--card);color:var(--muted);border:1px solid var(--line);
}
.subtab.active{background:var(--navy);color:#fff;border-color:var(--navy);}

/* decision recap ribbon inside step */
.recap{
  display:inline-flex;align-items:center;gap:7px;font-size:12px;color:var(--muted);
  background:var(--card);border:1px solid var(--line);padding:4px 10px;border-radius:8px;margin-bottom:14px;
}
.recap b{color:var(--navy);}

/* checklist grid (take-home) */
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:6px;}
@media (max-width:600px){.grid2{grid-template-columns:1fr;}}
.item-card{
  display:flex;gap:11px;align-items:flex-start;background:var(--card);border:1px solid var(--line);
  border-radius:10px;padding:12px 14px;
}
.item-card input{margin-top:3px;width:16px;height:16px;accent-color:var(--teal-dk);flex:none;}
.item-card span{font-size:14px;color:var(--ink);}

/* success ladder */
.ladder{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:6px;}
@media (max-width:760px){.ladder{grid-template-columns:1fr 1fr;}}
.rung{border-radius:11px;padding:16px 15px;color:#fff;}
.rung h4{color:#fff;font-size:13px;text-transform:uppercase;letter-spacing:.05em;margin-bottom:8px;font-family:'Inter';font-weight:700;}
.rung p{font-size:13px;color:rgba(255,255,255,.92);margin:0;}
.rung.r1{background:#B7C0E6;color:#20264D;}
.rung.r1 h4,.rung.r1 p{color:#20264D;}
.rung.r2{background:#6FBFB4;}
.rung.r3{background:#1E9E8E;}
.rung.r4{background:var(--navy);}

/* footer */
.footer{background:var(--navy-dk);color:#C9D0EF;padding:56px 0 40px;margin-top:20px;}
.footer h2{color:#fff;font-size:24px;}
.footer .wrap{display:grid;grid-template-columns:1.1fr 1fr;gap:50px;}
@media (max-width:760px){.footer .wrap{grid-template-columns:1fr;}}
.footer-links{list-style:none;margin:14px 0 0;padding:0;}
.footer-links li{padding:9px 0;border-top:1px solid rgba(255,255,255,.1);font-size:14px;}
.footer-links li:first-child{border-top:none;}
.footer-links a{color:#DDE3FF;text-decoration:none;}
.footer-links a:hover{color:var(--teal);}
.footer-links .k{color:#8B95C4;margin-right:8px;}
.closing{
  border:1px solid rgba(125,239,226,.25);background:rgba(125,239,226,.06);
  border-radius:10px;padding:16px 18px;font-size:14px;color:#D9F2ED;font-style:italic;margin-top:22px;
}
.foot-tiny{margin-top:34px;font-size:12.5px;color:#6C76A6;}

/* small icons via inline svg currentColor - defined per use */
svg{display:inline-block;vertical-align:middle;}
</style>
</head>
<body>

<!-- ============ STICKY TOP BAR ============ -->
<div class="topbar">
  <div class="topbar-inner">
    <div class="topbar-title">EA Agent <span>· Setup Guide</span></div>
    <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>
    <div class="progress-label" id="progressLabel">0 / 12 steps</div>
    <div class="chip-row">
      <button class="chip" id="chipOs" onclick="scrollToConfig()">macOS/Linux</button>
      <button class="chip" id="chipWriter" onclick="scrollToConfig()">Markdown</button>
      <button class="chip" id="chipData" onclick="scrollToConfig()">Sample data</button>
    </div>
  </div>
</div>

<!-- ============ HERO ============ -->
<header class="hero">
  <div class="wrap">
    <div class="hero-eyebrow">Self-service setup guide</div>
    <h1>Build Your Executive Assistant Agent</h1>
    <p class="hero-sub">A step-by-step build path for the morning agent that reads your world, thinks once, and writes where you work. Pick your stack once — every step below adapts to it.</p>
    <div class="hero-meta">
      <div class="hero-meta-item"><span class="num">12</span><span class="lbl">Build steps</span></div>
      <div class="hero-meta-item"><span class="num">~75</span><span class="lbl">Minutes, guided</span></div>
      <div class="hero-meta-item"><span class="num">3</span><span class="lbl">Decisions that branch the build</span></div>
      <div class="hero-meta-item"><span class="num">0</span><span class="lbl">Required beyond a terminal</span></div>
    </div>
    <a class="hero-cta" href="#config">
      Configure your build
      <svg viewBox="0 0 20 20" fill="none"><path d="M4 10h12M11 5l5 5-5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </a>
  </div>
</header>

<!-- ============ CONFIG / DECISION PANEL ============ -->
<div class="wrap">
  <section class="config" id="config">
    <div class="config-head">
      <div>
        <h2>Configure your build</h2>
        <p>Three choices. Every step below — commands, code, troubleshooting — updates to match.</p>
      </div>
      <div class="config-note">Change these anytime</div>
    </div>

    <div class="decision-grid">

      <div class="decision">
        <div class="decision-label">Operating system</div>
        <div class="decision-hint">Sets your shell commands and scheduling steps.</div>
        <div class="opt-group" data-group="os">
          <label class="opt selected" data-value="mac">
            <input type="radio" name="os" value="mac" checked>
            <span class="opt-text"><strong>macOS / Linux</strong><small>venv, cron or launchd</small></span>
          </label>
          <label class="opt" data-value="windows">
            <input type="radio" name="os" value="windows">
            <span class="opt-text"><strong>Windows</strong><small>venv, Task Scheduler</small></span>
          </label>
        </div>
      </div>

      <div class="decision">
        <div class="decision-label">Task destination</div>
        <div class="decision-hint">Where finished tasks get written.</div>
        <div class="opt-group" data-group="writer">
          <label class="opt selected" data-value="markdown">
            <input type="radio" name="writer" value="markdown" checked>
            <span class="opt-text"><strong>Markdown checklist</strong><small>Default — nothing to install</small></span>
          </label>
          <label class="opt" data-value="todoist">
            <input type="radio" name="writer" value="todoist">
            <span class="opt-text"><strong>Todoist</strong><small>Cross-platform, API token</small></span>
          </label>
          <label class="opt" data-value="google_tasks">
            <input type="radio" name="writer" value="google_tasks">
            <span class="opt-text"><strong>Google Tasks</strong><small>Cross-platform, reuses OAuth</small></span>
          </label>
          <label class="opt" data-value="apple_reminders" id="optAppleReminders">
            <input type="radio" name="writer" value="apple_reminders">
            <span class="opt-text"><strong>Apple Reminders</strong><small>Requires macOS</small></span>
          </label>
        </div>
      </div>

      <div class="decision">
        <div class="decision-label">Data source</div>
        <div class="decision-hint">Start on sample data, connect real accounts later.</div>
        <div class="opt-group" data-group="data">
          <label class="opt selected" data-value="sample">
            <input type="radio" name="data" value="sample" checked>
            <span class="opt-text"><strong>Sample data</strong><small>Fastest path — no OAuth</small></span>
          </label>
          <label class="opt" data-value="live">
            <input type="radio" name="data" value="live">
            <span class="opt-text"><strong>Live Gmail + Calendar</strong><small>Needs Google Cloud OAuth</small></span>
          </label>
        </div>
      </div>

    </div>
  </section>
</div>

<!-- ============ MAIN LAYOUT ============ -->
<div class="wrap">
  <div class="layout">

    <!-- RAIL -->
    <nav class="rail" aria-label="Step navigation">
      <div class="rail-title">Build path</div>
      <ul class="rail-list" id="railList">
        <!-- populated identically to steps below, hand-authored for reliability -->
        <li class="rail-item" data-step="1"><a class="rail-link" href="#step-1"><span class="rail-dot"></span>Prerequisites</a></li>
        <li class="rail-item" data-step="2"><a class="rail-link" href="#step-2"><span class="rail-dot"></span>Starter repo</a></li>
        <li class="rail-item" data-step="3"><a class="rail-link" href="#step-3"><span class="rail-dot"></span>API key</a></li>
        <li class="rail-item" data-step="4"><a class="rail-link" href="#step-4"><span class="rail-dot"></span>First brief</a></li>
        <li class="rail-item" data-step="5"><a class="rail-link" href="#step-5"><span class="rail-dot"></span>EA contract</a></li>
        <li class="rail-item" data-step="6"><a class="rail-link" href="#step-6"><span class="rail-dot"></span>System prompt</a></li>
        <li class="rail-item" data-step="7"><a class="rail-link" href="#step-7"><span class="rail-dot"></span>Data source</a></li>
        <li class="rail-item" data-step="8"><a class="rail-link" href="#step-8"><span class="rail-dot"></span>Task destination</a></li>
        <li class="rail-item" data-step="9"><a class="rail-link" href="#step-9"><span class="rail-dot"></span>Schedule it</a></li>
        <li class="rail-item" data-step="10"><a class="rail-link" href="#step-10"><span class="rail-dot"></span>Level up</a></li>
        <li class="rail-item" data-step="11"><a class="rail-link" href="#step-11"><span class="rail-dot"></span>Ship checklist</a></li>
        <li class="rail-item" data-step="12"><a class="rail-link" href="#step-12"><span class="rail-dot"></span>Take-home</a></li>
      </ul>
    </nav>

    <!-- CONTENT -->
    <main class="content">

      <div class="mobile-jump">
        <select id="mobileJump" onchange="if(this.value) location.hash=this.value;">
          <option value="">Jump to a step…</option>
          <option value="#step-1">1 · Prerequisites</option>
          <option value="#step-2">2 · Starter repo</option>
          <option value="#step-3">3 · API key</option>
          <option value="#step-4">4 · First brief</option>
          <option value="#step-5">5 · EA contract</option>
          <option value="#step-6">6 · System prompt</option>
          <option value="#step-7">7 · Data source</option>
          <option value="#step-8">8 · Task destination</option>
          <option value="#step-9">9 · Schedule it</option>
          <option value="#step-10">10 · Level up</option>
          <option value="#step-11">11 · Ship checklist</option>
          <option value="#step-12">12 · Take-home</option>
        </select>
      </div>

      <div class="lead-block">
        <h2>You're not building a chatbot</h2>
        <p>You're building a ritual: an agent that runs before you open your laptop, reads your world, synthesizes one integrated day, and writes brief + tasks where you already work. Follow the steps in order the first time through — after that, jump around freely.</p>
      </div>

      <!-- STEP 1 -->
      <section class="step" id="step-1">
        <div class="step-top">
          <div class="step-heading">
            <div class="step-num">1</div>
            <div class="step-title-wrap">
              <h3>Check prerequisites</h3>
              <div class="step-meta"><span class="step-time">~2 min</span></div>
            </div>
          </div>
          <label class="step-check"><input type="checkbox" data-step-check="1"><span>Done</span></label>
        </div>
        <div class="step-body">
          <p>You need Python 3.10+ (3.12 recommended) and an Anthropic API key. Nothing else — no Google account required to get your first brief running.</p>
          <div class="code">
            <div class="code-head"><span class="code-lang">terminal</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
            <pre>python3 --version<span class="c">  # need 3.10 or newer, 3.12 recommended</span></pre>
          </div>
          <div class="callout hint">
            <svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M10 2a5 5 0 0 0-3 9v2h6v-2a5 5 0 0 0-3-9Z" stroke="currentColor" stroke-width="1.5"/><path d="M8 17h4M9 19h2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <p><strong>Hint —</strong> get a key at <a href="https://console.anthropic.com" target="_blank" rel="noopener">console.anthropic.com</a> before step 3, so it's ready when you need it.</p>
          </div>
        </div>
      </section>

      <!-- STEP 2 -->
      <section class="step" id="step-2">
        <div class="step-top">
          <div class="step-heading">
            <div class="step-num">2</div>
            <div class="step-title-wrap">
              <h3>Get the starter repo running</h3>
              <div class="step-meta"><span class="step-time">~3 min</span><span class="badge adapts">Adapts to OS</span></div>
            </div>
          </div>
          <label class="step-check"><input type="checkbox" data-step-check="2"><span>Done</span></label>
        </div>
        <div class="step-body">
          <p>Create an isolated environment and install the workshop package in editable mode.</p>

          <div class="branch" data-req-os="mac">
            <div class="code">
              <div class="code-head"><span class="code-lang">terminal · macOS / Linux</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
              <pre>cd starter
python3.12 -m venv .venv && source .venv/bin/activate
pip install -e .</pre>
            </div>
          </div>
          <div class="branch" data-req-os="windows">
            <div class="code">
              <div class="code-head"><span class="code-lang">powershell · Windows</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
              <pre>cd starter
python3.12 -m venv .venv
.venv\Scripts\activate
pip install -e .</pre>
            </div>
          </div>

          <div class="trouble">
            <div class="trouble-title">
              <svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M10 3 2 17h16L10 3Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M10 8.5v3.2M10 14.2h.01" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
              Common snags
            </div>
            <div class="trouble-list">
              <div class="trouble-row">
                <div class="trouble-sym">error: externally-managed-environment</div>
                <div class="trouble-fix">Your venv isn't active. Re-run the activate line — your prompt should show <code>(.venv)</code> before you install.</div>
              </div>
              <div class="trouble-row">
                <div class="trouble-sym">python3.12: command not found</div>
                <div class="trouble-fix">Use whatever Python 3.10+ you have: <code>python3 -m venv .venv</code> works the same way.</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- STEP 3 -->
      <section class="step" id="step-3">
        <div class="step-top">
          <div class="step-heading">
            <div class="step-num">3</div>
            <div class="step-title-wrap">
              <h3>Add your Anthropic API key</h3>
              <div class="step-meta"><span class="step-time">~1 min</span></div>
            </div>
          </div>
          <label class="step-check"><input type="checkbox" data-step-check="3"><span>Done</span></label>
        </div>
        <div class="step-body">
          <p>Copy the example env file and drop in your key. This file is already gitignored — it never leaves your machine.</p>
          <div class="branch" data-req-os="mac">
            <div class="code">
              <div class="code-head"><span class="code-lang">terminal · macOS / Linux</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
              <pre>cp .env.example .env
<span class="c"># open .env and set:</span>
ANTHROPIC_API_KEY=sk-ant-...</pre>
            </div>
          </div>
          <div class="branch" data-req-os="windows">
            <div class="code">
              <div class="code-head"><span class="code-lang">powershell · Windows</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
              <pre>copy .env.example .env
<span class="c"># open .env and set:</span>
ANTHROPIC_API_KEY=sk-ant-...</pre>
            </div>
          </div>
          <div class="trouble">
            <div class="trouble-title">
              <svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M10 3 2 17h16L10 3Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M10 8.5v3.2M10 14.2h.01" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
              Common snags
            </div>
            <div class="trouble-list">
              <div class="trouble-row">
                <div class="trouble-sym">ANTHROPIC_API_KEY not set</div>
                <div class="trouble-fix">Confirm the key is in <code>.env</code> in the <code>starter/</code> folder, with no quotes around it.</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- STEP 4 -->
      <section class="step" id="step-4">
        <div class="step-top">
          <div class="step-heading">
            <div class="step-num">4</div>
            <div class="step-title-wrap">
              <h3>Run your first brief</h3>
              <div class="step-meta"><span class="step-time">~2 min</span></div>
            </div>
          </div>
          <label class="step-check"><input type="checkbox" data-step-check="4"><span>Done</span></label>
        </div>
        <div class="step-body">
          <p>This is the 5-minute win — bundled sample data, no Google setup required.</p>
          <div class="code">
            <div class="code-head"><span class="code-lang">terminal</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
            <pre>ea-workshop --sample
<span class="c"># or preview only, without writing a file:</span>
ea-workshop --sample --dry-run</pre>
          </div>
          <div class="callout hint">
            <svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M10 2a5 5 0 0 0-3 9v2h6v-2a5 5 0 0 0-3-9Z" stroke="currentColor" stroke-width="1.5"/><path d="M8 17h4M9 19h2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <p><strong>Opens —</strong> <code>output/Daily Brief — YYYY-MM-DD.md</code>. If it reads like something you'd actually want to open at 7am, you're on track.</p>
          </div>
          <div class="trouble">
            <div class="trouble-title">
              <svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M10 3 2 17h16L10 3Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M10 8.5v3.2M10 14.2h.01" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
              Common snags
            </div>
            <div class="trouble-list">
              <div class="trouble-row">
                <div class="trouble-sym">command not found: ea-workshop</div>
                <div class="trouble-fix">Your venv isn't active, or step 2's install didn't finish. Re-activate, then re-run <code>pip install -e .</code></div>
              </div>
              <div class="trouble-row">
                <div class="trouble-sym">Model not found / 404</div>
                <div class="trouble-fix">Add <code>ANTHROPIC_MODEL=claude-sonnet-4-6</code> to <code>.env</code>.</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- STEP 5 -->
      <section class="step" id="step-5">
        <div class="step-top">
          <div class="step-heading">
            <div class="step-num">5</div>
            <div class="step-title-wrap">
              <h3>Write your EA contract</h3>
              <div class="step-meta"><span class="step-time">~5 min</span></div>
            </div>
          </div>
          <label class="step-check"><input type="checkbox" data-step-check="5"><span>Done</span></label>
        </div>
        <div class="step-body">
          <p>Before touching prompts, decide what your agent is actually for. Open <code>config.yaml</code> and fill in: the roles you juggle, your never-do rules, and where output should land.</p>
          <div class="code">
            <div class="code-head"><span class="code-lang">config.yaml</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
            <pre>prompt_rules:
  - <span class="s">"I juggle Work and Personal — tag everything."</span>
  - <span class="s">"No work content on weekends."</span>
  - <span class="s">"Always include a movement challenge."</span>
  - <span class="s">"Cap new tasks at 5 per day."</span></pre>
          </div>
          <div class="callout hint">
            <svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M10 2a5 5 0 0 0-3 9v2h6v-2a5 5 0 0 0-3-9Z" stroke="currentColor" stroke-width="1.5"/><path d="M8 17h4M9 19h2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <p><strong>Hint —</strong> generic agents are useless; opinionated agents are invaluable. Vague rules like "be helpful" do nothing — specific caps and never-dos do everything.</p>
          </div>
        </div>
      </section>

      <!-- STEP 6 -->
      <section class="step" id="step-6">
        <div class="step-top">
          <div class="step-heading">
            <div class="step-num">6</div>
            <div class="step-title-wrap">
              <h3>Tune the system prompt</h3>
              <div class="step-meta"><span class="step-time">~10 min</span></div>
            </div>
          </div>
          <label class="step-check"><input type="checkbox" data-step-check="6"><span>Done</span></label>
        </div>
        <div class="step-body">
          <p>Code is plumbing — the system prompt and JSON schema in <code>src/ea_workshop/synthesizer.py</code> are the EA's brain. This is the part worth spending your time on.</p>
          <div class="code">
            <div class="code-head"><span class="code-lang">synthesizer.py — system prompt</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
            <pre>You are an exceptional executive assistant preparing a
focused morning daily brief.

Voice: warm, clear, concise — like a trusted EA who
protects attention. Synthesize; never dump raw lists.

Brief rules:
- focus_today: MAX 3 items
- work_plan: ONE paragraph with time blocks + effort estimate
- wellness: 2-3 practical nudges
- movement_challenge: 3-5 micro-movements (<span class="c">&lt;=30 min each</span>)

Task rules:
- urgency: critical | today | this_week | whenever
- Max 2 tasks at critical/today
- NEVER duplicate existing_reminders

Respond with valid JSON only.</pre>
          </div>
          <div class="callout hint">
            <svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M10 2a5 5 0 0 0-3 9v2h6v-2a5 5 0 0 0-3-9Z" stroke="currentColor" stroke-width="1.5"/><path d="M8 17h4M9 19h2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <p><strong>Hint —</strong> after any prompt change, re-run <code>ea-workshop --sample --dry-run</code>. That's your fastest feedback loop — no file writes, output straight to terminal.</p>
          </div>
          <div class="trouble">
            <div class="trouble-title">
              <svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M10 3 2 17h16L10 3Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M10 8.5v3.2M10 14.2h.01" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
              Common snags
            </div>
            <div class="trouble-list">
              <div class="trouble-row">
                <div class="trouble-sym">Brief comes back as prose, not JSON</div>
                <div class="trouble-fix">Check you kept the "Respond with valid JSON only" line — it's easy to trim by accident while editing.</div>
              </div>
              <div class="trouble-row">
                <div class="trouble-sym">Everything is marked urgent</div>
                <div class="trouble-fix">Tighten the cap: "max 2 today, most = this_week" as an explicit rule, not a suggestion.</div>
              </div>
              <div class="trouble-row">
                <div class="trouble-sym">Brief is too long to skim</div>
                <div class="trouble-fix">Lower the bullet caps per section rather than asking the model to "be concise" — caps are enforceable, adjectives aren't.</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- STEP 7 : DATA SOURCE (branches on data) -->
      <section class="step" id="step-7">
        <div class="step-top">
          <div class="step-heading">
            <div class="step-num">7</div>
            <div class="step-title-wrap">
              <h3>Connect your data source</h3>
              <div class="step-meta"><span class="step-time">~8 min</span><span class="badge adapts">Adapts to data source</span></div>
            </div>
          </div>
          <label class="step-check"><input type="checkbox" data-step-check="7"><span>Done</span></label>
        </div>
        <div class="step-body">

          <div class="branch" data-req-data="sample">
            <div class="recap">You chose: <b>Sample data</b> — this step needs nothing further.</div>
            <p>The starter ships with bundled sample email, calendar, and meeting data, so there's nothing to connect right now. Everything from step 4 onward already runs on it.</p>
            <div class="callout hint">
              <svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M10 2a5 5 0 0 0-3 9v2h6v-2a5 5 0 0 0-3-9Z" stroke="currentColor" stroke-width="1.5"/><path d="M8 17h4M9 19h2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
              <p><strong>Hint —</strong> switch the "Data source" choice above to <em>Live Gmail + Calendar</em> whenever you're ready — this card will turn into the OAuth walkthrough.</p>
            </div>
          </div>

          <div class="branch" data-req-data="live">
            <div class="recap">You chose: <b>Live Gmail + Calendar</b> — set up Google OAuth below.</div>
            <p>You'll need a Google Cloud project with the Gmail and Calendar APIs enabled, and desktop OAuth credentials.</p>
            <div class="code">
              <div class="code-head"><span class="code-lang">setup</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
              <pre><span class="c"># 1. Create a Google Cloud project
# 2. Enable the Gmail API and Calendar API
# 3. Create Desktop OAuth credentials, save as:</span>
credentials/google_credentials.json
<span class="c"># 4. Run the auth flow:</span>
python scripts/setup_google_auth.py</pre>
            </div>
            <div class="trouble">
              <div class="trouble-title">
                <svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M10 3 2 17h16L10 3Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M10 8.5v3.2M10 14.2h.01" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
                Common snags
              </div>
              <div class="trouble-list">
                <div class="trouble-row">
                  <div class="trouble-sym">OAuth flow times out</div>
                  <div class="trouble-fix">Don't lose momentum — flip back to <em>Sample data</em> above and finish OAuth after the session.</div>
                </div>
                <div class="trouble-row">
                  <div class="trouble-sym">redirect_uri_mismatch</div>
                  <div class="trouble-fix">Your OAuth consent screen's authorized redirect URI doesn't match what the script requests — re-check the Desktop app credential type.</div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </section>

      <!-- STEP 8 : TASK DESTINATION (branches on writer) -->
      <section class="step" id="step-8">
        <div class="step-top">
          <div class="step-heading">
            <div class="step-num">8</div>
            <div class="step-title-wrap">
              <h3>Pick your task destination</h3>
              <div class="step-meta"><span class="step-time">~5 min</span><span class="badge adapts">Adapts to task destination</span></div>
            </div>
          </div>
          <label class="step-check"><input type="checkbox" data-step-check="8"><span>Done</span></label>
        </div>
        <div class="step-body">
          <p>The starter ships one working writer: markdown. It's a genuinely complete, successful workshop outcome on its own. Todoist, Google Tasks, and Apple Reminders are real stretch goals — each is a small file you write, following the pattern already in the codebase, not a setting you flip.</p>

          <div class="branch" data-req-writer="markdown">
            <div class="recap">You chose: <b>Markdown checklist</b> — already done. <span class="badge" style="margin-left:4px;">Ready now</span></div>
            <p>This is the starter's default writer, already wired up in <code>run.py</code>. Tasks land in the same Daily Brief markdown file as a checklist — nothing to install, nothing to write.</p>
          </div>

          <div class="branch" data-req-writer="todoist">
            <div class="recap">You chose: <b>Todoist</b> <span class="badge" style="margin-left:4px;">You'll write this</span></div>
            <p class="muted">Honest status: the starter only ships the markdown writer. Todoist isn't a config toggle — it's a short stretch-goal file you add yourself. Here's the whole thing:</p>
            <div class="code">
              <div class="code-head"><span class="code-lang">src/ea_workshop/writers/todoist.py</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
              <pre>pip install requests   <span class="c"># add to pyproject.toml dependencies too</span>

<span class="c"># add TODOIST_API_TOKEN to .env, then:</span>
import os
import requests

def create_tasks(tasks: list) -> list[str]:
    token = os.environ["TODOIST_API_TOKEN"]
    created = []
    for task in tasks:
        resp = requests.post(
            "https://api.todoist.com/rest/v2/tasks",
            headers={"Authorization": f"Bearer {token}"},
            json={"content": task.title, "description": task.notes},
            timeout=30,
        )
        resp.raise_for_status()
        created.append(task.title)
    return created</pre>
            </div>
            <div class="branch-note">Call <code>create_tasks(result.tasks)</code> from <code>run.py</code> right after <code>synthesize()</code>. Dedupe matters more here than markdown — LLMs rephrase task titles daily, so step 10's dedupe layer is worth adding at the same time, not later.</div>
          </div>

          <div class="branch" data-req-writer="google_tasks">
            <div class="recap">You chose: <b>Google Tasks</b> <span class="badge" style="margin-left:4px;">You'll write this</span></div>
            <p class="muted">Same honest status as Todoist — this is a stretch goal, not a flip-a-switch option. It reuses the OAuth credentials from step 7.</p>
            <div class="code">
              <div class="code-head"><span class="code-lang">setup</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
              <pre><span class="c"># 1. Add the Tasks scope in collectors/google_live.py:</span>
SCOPES = [
    ...,
    "https://www.googleapis.com/auth/tasks",
]
<span class="c"># 2. Delete credentials/google_token.json and re-run:</span>
python scripts/setup_google_auth.py
<span class="c"># 3. Write writers/google_tasks.py using the same
#    `build("tasks", "v1", credentials=creds)` pattern
#    google_live.py already uses for Gmail/Calendar</span></pre>
            </div>
            <div class="branch-note" data-req-data="sample">Needs the OAuth credentials from step 7. Switch "Data source" to <em>Live Gmail + Calendar</em> first.</div>
          </div>

          <div class="branch" data-req-writer="apple_reminders">
            <div class="recap">You chose: <b>Apple Reminders</b> <span class="badge" style="margin-left:4px;">You'll write this</span></div>
            <div class="branch" data-req-os="mac">
              <p class="muted">Stretch goal, macOS only. Install the extra, then write the writer using EventKit.</p>
              <div class="code">
                <div class="code-head"><span class="code-lang">terminal · macOS</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
                <pre>pip install -e ".[apple]"
<span class="c"># then write src/ea_workshop/writers/reminders.py using
# EventKit.EKEventStore — create one EKReminder per task,
# set its list/title/notes, and save via the store.
# First run prompts for access —</span>
<span class="c"># approve in System Settings → Privacy &amp; Security → Reminders</span></pre>
              </div>
            </div>
            <div class="branch-note" data-req-os="windows">Apple Reminders needs macOS. Switch the OS toggle above to <em>macOS / Linux</em>, or pick Todoist / Google Tasks instead — both work everywhere.</div>
          </div>

          <div class="callout hint">
            <svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M10 2a5 5 0 0 0-3 9v2h6v-2a5 5 0 0 0-3-9Z" stroke="currentColor" stroke-width="1.5"/><path d="M8 17h4M9 19h2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <p><strong>Hint —</strong> not on Apple? Markdown, Todoist, and Google Tasks all work identically on Mac, Linux, and Windows.</p>
          </div>
        </div>
      </section>

      <!-- STEP 9 : SCHEDULE (branches on os) -->
      <section class="step" id="step-9">
        <div class="step-top">
          <div class="step-heading">
            <div class="step-num">9</div>
            <div class="step-title-wrap">
              <h3>Schedule the daily run</h3>
              <div class="step-meta"><span class="step-time">~4 min</span><span class="badge adapts">Adapts to OS</span></div>
            </div>
          </div>
          <label class="step-check"><input type="checkbox" data-step-check="9"><span>Done</span></label>
        </div>
        <div class="step-body">
          <p>This is what turns a script into an agent — it runs before you open your laptop, without you thinking about it.</p>

          <div class="branch" data-req-os="mac">
            <div class="code">
              <div class="code-head"><span class="code-lang">crontab -e</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
              <pre>0 7 * * * cd ~/starter && .venv/bin/ea-workshop >> ~/ea-brief.log 2>&1</pre>
            </div>
            <div class="branch-note">Prefer launchd? It catches up on wake if your laptop was asleep at 7am — cron just skips the run. Full plist template in <code>FINISH-ON-YOUR-OWN.md</code>, Step 5.</div>
          </div>

          <div class="branch" data-req-os="windows">
            <div class="code">
              <div class="code-head"><span class="code-lang">Task Scheduler</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
              <pre><span class="c"># Task Scheduler → Create Task → Trigger: daily, 7:00 AM
# Action: run this program/script</span>
python -m ea_workshop.run</pre>
            </div>
          </div>

          <div class="trouble">
            <div class="trouble-title">
              <svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M10 3 2 17h16L10 3Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M10 8.5v3.2M10 14.2h.01" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
              Common snags
            </div>
            <div class="trouble-list">
              <div class="trouble-row">
                <div class="trouble-sym">Cron job never runs</div>
                <div class="trouble-fix">Use absolute paths for everything — cron doesn't load your shell profile. Test the exact command by pasting it directly into a fresh terminal first.</div>
              </div>
              <div class="trouble-row">
                <div class="trouble-sym">Task Scheduler task doesn't fire</div>
                <div class="trouble-fix">Check "Run whether user is logged on or not," and point the action at your venv's <code>python.exe</code> directly rather than the bare command.</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- STEP 10 : LEVEL UP (optional, tabs not gated) -->
      <section class="step" id="step-10">
        <div class="step-top">
          <div class="step-heading">
            <div class="step-num">10</div>
            <div class="step-title-wrap">
              <h3>Level up (optional)</h3>
              <div class="step-meta"><span class="step-time">~15 min</span><span class="badge">Advanced</span></div>
            </div>
          </div>
          <label class="step-check"><input type="checkbox" data-step-check="10"><span>Done</span></label>
        </div>
        <div class="step-body">

          <h4 style="font-size:16px;margin-bottom:6px;">Dedupe — stop duplicate tasks</h4>
          <p class="muted">LLMs rephrase the same task daily: "Reply to James" becomes "Re-engage James Marsden" becomes a duplicate reminder. Three layers, in order of effort:</p>
          <div class="grid2">
            <div class="item-card"><input type="checkbox"><span>Pass open tasks into the prompt as context</span></div>
            <div class="item-card"><input type="checkbox"><span>Scan the todo app before creating anything new</span></div>
            <div class="item-card"><input type="checkbox"><span>Add fuzzy title matching as a final safety net</span></div>
          </div>
          <div class="callout hint" style="margin-top:16px;">
            <svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M10 2a5 5 0 0 0-3 9v2h6v-2a5 5 0 0 0-3-9Z" stroke="currentColor" stroke-width="1.5"/><path d="M8 17h4M9 19h2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <p><strong>Hint —</strong> layer 1 alone removes most duplicates. Only add layers 2–3 once you've felt the problem firsthand.</p>
          </div>

          <h4 style="font-size:16px;margin:26px 0 6px;">Weekend mode — defense in depth</h4>
          <p class="muted">Filter work sources in code, and swap in a different system prompt — don't rely on prompt wording alone to keep Saturday quiet.</p>
          <div class="grid2">
            <div class="item-card"><input type="checkbox"><span>Saturday: personal life, rest, movement — work sources filtered out in code</span></div>
            <div class="item-card"><input type="checkbox"><span>Sunday: adds a soft "week ahead" — deliberately not a work plan</span></div>
          </div>
        </div>
      </section>

      <!-- STEP 11 : SUCCESS LADDER -->
      <section class="step" id="step-11">
        <div class="step-top">
          <div class="step-heading">
            <div class="step-num">11</div>
            <div class="step-title-wrap">
              <h3>Know when you're done</h3>
              <div class="step-meta"><span class="step-time">~1 min</span></div>
            </div>
          </div>
          <label class="step-check"><input type="checkbox" data-step-check="11"><span>Done</span></label>
        </div>
        <div class="step-body">
          <p class="muted">There's no single finish line — pick the rung that matches your time today.</p>
          <div class="ladder">
            <div class="rung r1"><h4>Minimum</h4><p><code>--sample</code> produces a brief you'd actually read.</p></div>
            <div class="rung r2"><h4>Good</h4><p>Live Gmail + Calendar → markdown brief.</p></div>
            <div class="rung r3"><h4>Stretch</h4><p>Scheduled run + task writer + custom rules.</p></div>
            <div class="rung r4"><h4>Hero</h4><p>Full build with dedupe + weekend mode.</p></div>
          </div>
        </div>
      </section>

      <!-- STEP 12 : TAKE HOME -->
      <section class="step" id="step-12">
        <div class="step-top">
          <div class="step-heading">
            <div class="step-num">12</div>
            <div class="step-title-wrap">
              <h3>Take-home menu</h3>
              <div class="step-meta"><span class="step-time">Pick one</span></div>
            </div>
          </div>
          <label class="step-check"><input type="checkbox" data-step-check="12"><span>Done</span></label>
        </div>
        <div class="step-body">
          <p class="muted">Didn't finish live? Any one of these is a good next session.</p>
          <div class="grid2">
            <div class="item-card"><input type="checkbox"><span>Custom roles in config.yaml</span></div>
            <div class="item-card"><input type="checkbox"><span>Weekend personal mode</span></div>
            <div class="item-card"><input type="checkbox"><span>Wellness + movement sections</span></div>
            <div class="item-card"><input type="checkbox"><span>Todoist / Google Tasks writer</span></div>
            <div class="item-card"><input type="checkbox"><span>Multi-inbox Gmail</span></div>
            <div class="item-card"><input type="checkbox"><span>Meeting notes integration</span></div>
            <div class="item-card"><input type="checkbox"><span>Dedupe layer</span></div>
          </div>
        </div>
      </section>

    </main>
  </div>
</div>

<!-- ============ FOOTER ============ -->
<footer class="footer">
  <div class="wrap">
    <div>
      <h2>The API keys are commodity.<br>The prompts and rules are yours.</h2>
      <div class="closing">Questions? Re-run <code>--sample --dry-run</code> after any prompt change — that's your fastest feedback loop.</div>
    </div>
    <div>
      <h2 style="font-size:16px;text-transform:uppercase;letter-spacing:.06em;">Resources</h2>
      <ul class="footer-links">
        <li><span class="k">Workshop repo</span><a href="https://github.com/lindakinning/daily-briefing-agent" target="_blank" rel="noopener">github.com/lindakinning/daily-briefing-agent</a></li>
        <li><span class="k">Finish guide</span><a href="https://github.com/lindakinning/daily-briefing-agent/blob/main/starter/FINISH-ON-YOUR-OWN.md" target="_blank" rel="noopener">starter/FINISH-ON-YOUR-OWN.md</a></li>
        <li><span class="k">Anthropic API</span><a href="https://console.anthropic.com" target="_blank" rel="noopener">console.anthropic.com</a></li>
        <li><span class="k">Google Cloud OAuth</span><a href="https://console.cloud.google.com" target="_blank" rel="noopener">console.cloud.google.com</a></li>
      </ul>
    </div>
    <div class="foot-tiny">Build Your Executive Assistant Agent — Participant self-service guide</div>
  </div>
</footer>

<script>
(function(){
  var TOTAL_STEPS = 12;
  var html = document.documentElement;

  // ---------- decision handling ----------
  function setDecision(group, value){
    html.setAttribute('data-' + group, value);
    document.querySelectorAll('.opt-group[data-group="'+group+'"] .opt').forEach(function(opt){
      opt.classList.toggle('selected', opt.getAttribute('data-value') === value);
    });
    updateBranches();
    updateChips();
    updateAppleRemindersAvailability();
  }

  document.querySelectorAll('.opt-group').forEach(function(group){
    var name = group.getAttribute('data-group');
    group.querySelectorAll('input[type=radio]').forEach(function(input){
      input.addEventListener('change', function(){
        if(input.disabled) return;
        setDecision(name, input.value);
      });
    });
  });

  function updateAppleRemindersAvailability(){
    var os = html.getAttribute('data-os');
    var wrap = document.getElementById('optAppleReminders');
    var input = wrap.querySelector('input');
    if(os === 'windows'){
      wrap.classList.add('disabled');
      if(input.checked){
        input.checked = false;
        document.querySelector('.opt-group[data-group="writer"] input[value="markdown"]').checked = true;
        setDecision('writer','markdown');
      }
      input.disabled = true;
    } else {
      wrap.classList.remove('disabled');
      input.disabled = false;
    }
  }

  function updateBranches(){
    var os = html.getAttribute('data-os');
    var writer = html.getAttribute('data-writer');
    var data = html.getAttribute('data-data');
    document.querySelectorAll('.branch').forEach(function(el){
      var reqOs = el.getAttribute('data-req-os');
      var reqWriter = el.getAttribute('data-req-writer');
      var reqData = el.getAttribute('data-req-data');
      var visible = true;
      if(reqOs && reqOs !== os) visible = false;
      if(reqWriter && reqWriter !== writer) visible = false;
      if(reqData && reqData !== data) visible = false;
      el.classList.toggle('is-visible', visible);
    });
  }

  function updateChips(){
    var labels = {
      os:{mac:'macOS/Linux', windows:'Windows'},
      writer:{markdown:'Markdown', todoist:'Todoist', google_tasks:'Google Tasks', apple_reminders:'Apple Reminders'},
      data:{sample:'Sample data', live:'Live Gmail+Cal'}
    };
    document.getElementById('chipOs').textContent = labels.os[html.getAttribute('data-os')];
    document.getElementById('chipWriter').textContent = labels.writer[html.getAttribute('data-writer')];
    document.getElementById('chipData').textContent = labels.data[html.getAttribute('data-data')];
  }

  window.scrollToConfig = function(){
    document.getElementById('config').scrollIntoView({behavior:'smooth', block:'center'});
  };

  // ---------- progress ----------
  function updateProgress(){
    var checked = document.querySelectorAll('[data-step-check]:checked').length;
    var pct = Math.round((checked/TOTAL_STEPS)*100);
    document.getElementById('progressFill').style.width = pct + '%';
    document.getElementById('progressLabel').textContent = checked + ' / ' + TOTAL_STEPS + ' steps';
    document.querySelectorAll('[data-step-check]').forEach(function(cb){
      var stepNum = cb.getAttribute('data-step-check');
      var railItem = document.querySelector('.rail-item[data-step="'+stepNum+'"]');
      if(railItem) railItem.classList.toggle('done', cb.checked);
    });
  }
  document.querySelectorAll('[data-step-check]').forEach(function(cb){
    cb.addEventListener('change', updateProgress);
  });

  // ---------- copy buttons ----------
  window.copyCode = function(btn){
    var pre = btn.closest('.code').querySelector('pre');
    var text = pre.innerText;
    var done = function(){
      var original = btn.textContent;
      btn.textContent = 'Copied';
      btn.classList.add('copied');
      setTimeout(function(){ btn.textContent = original; btn.classList.remove('copied'); }, 1400);
    };
    if(navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(text).then(done).catch(done);
    } else {
      done();
    }
  };

  // ---------- scrollspy ----------
  var railItems = document.querySelectorAll('.rail-item');
  var steps = document.querySelectorAll('.step');
  if('IntersectionObserver' in window){
    var obs = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        var id = entry.target.id;
        var num = id.split('-')[1];
        var railItem = document.querySelector('.rail-item[data-step="'+num+'"]');
        if(!railItem) return;
        if(entry.isIntersecting){
          railItems.forEach(function(ri){ ri.classList.remove('active'); });
          railItem.classList.add('active');
        }
      });
    }, {rootMargin:'-15% 0px -70% 0px', threshold:0});
    steps.forEach(function(s){ obs.observe(s); });
  }

  // ---------- init ----------
  updateBranches();
  updateChips();
  updateProgress();
  updateAppleRemindersAvailability();
})();
</script>
</body>
</html>
