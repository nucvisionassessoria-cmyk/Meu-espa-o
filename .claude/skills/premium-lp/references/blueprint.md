# LP blueprint — structure, copy method, build workflow

## Section order — cold paid traffic, no VSL
When there is **no sales video**, structure/authority/proof carry the trust, so
authority appears early and the offer precedes the FAQ. Target order:

1. **Hero** — headline (the reader's pain, as a provocation/question) + specific
   promise + primary CTA + real photo of the authority (gaze toward the button).
   *(Leave a commented `<!-- SLOT VSL -->` in the hero if a video may come later.)*
2. **Compact authority/media strip** — logos/outlets + institutions ("why trust
   this person") right under the fold. Anchored in real media/institutions, never
   follower counts.
3. **Problem** — the vacuum + the noisy "bad solutions" market, tied to real stakes,
   **without selling fear**.
4. **Reframe ("virada")** — the signature pivot: the real cost isn't the fine, it's
   X. Own block, gets the §8 scan reveal. Reader feels relief + a new lens.
5. **What the product delivers** — a decision tool / "x-ray", concrete "what you'll
   see and decide" bullets. Never "an index of a book", never promise compliance.
6. **Technical proof** — real competence via correct domain truth (no jargon, no
   normative errors). A single wrong technical claim destroys the whole page.
7. **Deep authority** — full bio, credentials kept **separate**, real reach.
8. **Social proof** — media clippings + testimonials (placeholder if none — never fabricate).
9. **Offer + guarantee** — low-risk price with a tangible anchor + risk-reversal guarantee + clear CTA.
10. **FAQ** — breaks the real remaining objections; reinforces what you do NOT promise.
11. **Final CTA** — a firm invitation in solution tone; no fear, no fake urgency.

Adjust to the product. The recurring mistakes to fix: authority appearing too late;
the reframe and technical proof buried instead of being explicit blocks; offer after
the FAQ instead of before.

## Voice & guardrails as a method
Copy is design material. For each project:
1. **Capture the brief's inviolable rules up front** and treat them as tests, e.g.:
   *solution not fear · no guaranteed-compliance claim · keep credential A and B
   separate · anchor authority in media/institutions not followers · don't invent
   proof · don't touch the offer terms.* (These specifics change per client — always
   ask for / extract them.)
2. **Write in the authority's voice**: second person, clean and professional, provoke
   by question, technical truth stated naturally, solution over fear.
3. **Before shipping, re-read the finished copy against the rules** and grep for
   violations.

### Per-public variants — tailor the WHOLE page, not just the hero
The biggest conversion leak: a page whose hero is tailored to public B/C but whose
**offer bullets and FAQ still speak to public A**. When you make P2/P3 from P1, swap
not only the top (hero, problem, reframe, product headline) but also the **offer
bullet framing, the final-CTA subline, and the persona-specific FAQ questions** so the
whole journey addresses the same reader. (P1 keeps the original as the control.)

### Per-public generation script (keeps design identical)
Generate variants from P1 by string replacement so CSS/JS/structure stay byte-identical:
```js
// mklp.js — run from the LP folder
const fs=require('fs'); const base=fs.readFileSync('index.html','utf8');
function build(reps,out){ let s=base;
  s=s.split("url('assets/").join("url('../assets/");     // subfolder asset paths
  let miss=0; reps.forEach(r=>{ if(s.indexOf(r[0])<0){miss++;console.log('MISS:',r[0].slice(0,50));} s=s.split(r[0]).join(r[1]); });
  fs.writeFileSync(out,s); console.log(out,miss?miss+' MISSED':'all swaps OK'); }
const P2=[ ['<old exact string>','<new string>'], /* title, meta, kick, hero l1/l2, sub, problem cards, reframe, product headline, offer bullet, CTA subline, FAQ items… */ ];
build(P2,'p2/index.html');
```
Each swap's first string must match P1 **exactly**. After editing P1's design, just
re-run to re-sync all variants. Watch for `MISS` (a stale swap string).

## Build → verify → optimize workflow
- **Headless render** (this env): `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`
  with `--headless=new --no-sandbox --allow-file-access-from-files --use-gl=angle
  --use-angle=swiftshader --enable-unsafe-swiftshader --run-all-compositor-stages-before-draw
  --window-size=W,H --screenshot=out.png file://.../index.html`. Wrap in `timeout 55`.
- **Image optimisation** (no imagemagick/PIL needed): load each photo in a headless
  page, draw to a canvas capped at ~1600px, `canvas.toDataURL('image/jpeg',0.82)`,
  `--dump-dom` to extract the data URIs, then base64-decode over the files. Cut a
  ~19MB photo set to <1MB. (ffmpeg in this env can't decode JPEG; canvas can.)
- **Self-contained previews to share**: embed each photo as a compressed `data:` URI
  in place of its `url('…')`, keep the Google-Fonts `<link>`; deliver the single HTML
  file. Opened in a real browser it shows fonts + WebGL + motion.
- **Pre-launch checklist** before driving traffic: install Meta Pixel / GA4 (a slot
  that activates when IDs are filled), OG tags + favicon per public, real e-book/OG
  image, test the checkout, confirm mobile.

## Gotchas learned (save yourself the debugging)
- **Headless clamps the CSS viewport to ~500px min** — you can't screenshot a true
  390px phone here; probe `document.body.scrollWidth` vs `clientWidth` to detect
  real overflow, and trust `overflow-x:hidden` on `html`+`body` to clip decorative layers.
- **`--virtual-time-budget` does NOT advance CSS transitions/animations** — to audit
  final states, inject an override forcing `.rv{opacity:1!important;translate:none!important}`,
  `.kin .ltr>i{opacity:1!important}`, and for the virada `.big{clip-path:none!important}`.
- **Scroll-dependent and pointer-dependent effects won't show in a static frame** —
  verify their code and confirm no JS errors (`--enable-logging=stderr`), then trust
  the real browser.
- **HTML comments can't contain `--`** — use en-dashes in commented scaffolds.
- **Reveal uses `translate`, tilt/parallax uses `transform`** — keep them separate.
- Motion tuned in this house style is always-on for core storytelling; only the
  heavy per-letter/aura/scanner motion is gated by `prefers-reduced-motion`.
