# Signature patterns & code

Every system below is in `example-full.html` and works together in **one rAF loop**.
Copy them as a set. Key convention: **reveals animate the CSS `translate` property;
tilt/parallax animate `transform`** — independent properties compose without fighting.

---

## 0. Layering
```
.bg{position:fixed;inset:0;z-index:0;overflow:hidden}   /* WebGL canvas #gl + 2D fallback #amb + grid + veil + scan + cursor-glow */
#trail{position:fixed;inset:0;z-index:6;pointer-events:none;mix-blend-mode:screen}  /* cursor trail canvas */
#routeSvg{position:absolute;inset:0;z-index:1;pointer-events:none;overflow:visible}  /* full-page route */
.wrap,.nav,.hero,.section,footer{position:relative;z-index:2}                        /* content */
.topbar{position:fixed;top:0;height:2px;z-index:50;transform:scaleX(0);transform-origin:left}  /* thin top progress */
```

## 1. Living background — WebGL fbm "smoke" (+ 2D fallback)
A raw GLSL fragment shader (no libs): value-noise `fbm` with domain warping = fluid
smoke, cursor-reactive (`u_mouse`), scroll-reactive (`u_scroll`), dark ink→green
palette + a small mouse light. If WebGL is missing, a 2D canvas draws slow green
glows + drifting particles + a faint grid.
- Palette in shader: `ink=vec3(0.026,0.039,0.033)`, `gdeep=vec3(0.030,0.20,0.12)`, `grn=vec3(0.09,0.53,0.30)`.
- **Mouse light** (keep small): `float ml=exp(-dot(p-m,p-m)*6.5); col+=vec3(0.10,0.46,0.28)*ml*0.34;`
  (the `*6.5` sets the radius — smaller number = bigger glow).
- Render at reduced resolution for perf: `q=min(dpr,1.5)*0.8`.
- When WebGL is active, hide the DOM `.cursor-glow` (that's the fallback light).
- The full VS/FS strings are in the example; copy verbatim, only tweak palette/`ml`.

## 2. The route — a progress bar that navigates (the signature)
A full-page SVG spanning the document: a faint dashed **base** path + a bright
**live** path drawn with `stroke-dashoffset`, **branches** to section titles, an
amber **destination** node at the offer, and an **arrow head** that sits at your
reading line.

Build (on load + resize): compute a left gutter X, collect anchors from
`#heroTitle, .sec-h, .final h2`, draw a mostly-vertical path that meanders slightly
then curves into the offer card centre. Branches only when there is a desktop
gutter and the title is left-aligned in the left third.

Drive it every frame from scroll — **arrow at viewport middle** (this is what makes
it feel right; do NOT use a look-ahead, it makes the line "run ahead"):
```js
if(mainLen>0){
  var targetY=y+innerHeight*0.5;                 // arrow rides your reading line
  var frac=clamp((targetY-mainStartY)/Math.max(1,(mainEndY-mainStartY)),0,1);
  var lenAt=frac*mainLen;
  rLive.style.strokeDashoffset=mainLen*(1-frac); // fill line to here
  var pt=rLive.getPointAtLength(lenAt);
  var pt2=rLive.getPointAtLength(Math.min(mainLen,lenAt+1.4));
  var ang=Math.atan2(pt2.y-pt.y,pt2.x-pt.x)*180/Math.PI-90;   // orient the arrow along the path
  rHead.setAttribute('transform','translate('+pt.x.toFixed(1)+' '+pt.y.toFixed(1)+') rotate('+ang.toFixed(1)+')');
  rHead.setAttribute('opacity', y>24?1:0);
  for(var ai=0;ai<anchors.length;ai++){var a=anchors[ai];
    if(!a.lit && pt.y>=a.y-2){a.lit=true;a.el.classList.add('energized');   // energy reaches the title
      if(a.bpath)a.bpath.classList.add('on'); if(a.bnode)a.bnode.classList.add('on');}}
  if(destNode) destNode.classList.toggle('on', frac>=0.985);
}
```
Arrow head element: `<path id="routeHead" d="M -6.5 -6 L 6.5 -6 L 0 7.5 Z"/>` (points
down at 0°, rotated to the tangent). Title glow: `.energized{animation:enrg 1.3s ease forwards}`.

## 3. Kinetic typography
Split target headings into per-letter `<i>` grouped into `.word` spans (so words
never break mid-word), then reveal letters with opacity/translate/blur.
- Targets: `#heroTitle, .sec-h, .final h2, .offer-top h2`.
- CSS: `.kin .ltr>i{display:inline-block;opacity:0;translate:0 .55em;filter:blur(6px);transition:...}`
  `.kin.in .ltr>i{opacity:1;translate:0 0;filter:blur(0)}` (stagger per-letter via delay).
- `.word{display:inline-block;white-space:nowrap}` prevents the "PRE/CISA" bug.

## 4. Reveal system
`.rv` = fade/translate/blur up; `.rv.rvx`/`.rvr` = slide from left/right. An
IntersectionObserver adds `.in` (staggered by sibling index). **Failsafe**: a
double-rAF after load reveals anything already in the initial viewport so the fold
is never stuck hidden.
```js
var revIO=new IntersectionObserver(function(es){es.forEach(function(e){
  if(!e.isIntersecting)return;var el=e.target;/*stagger*/ el.classList.add('in');revIO.unobserve(el);});
},{threshold:.16,rootMargin:'0px 0px -8% 0px'});
document.querySelectorAll('.rv,.turn,.kin').forEach(function(el){revIO.observe(el);});
requestAnimationFrame(function(){requestAnimationFrame(function(){
  document.querySelectorAll('.rv,.kin').forEach(function(el){var r=el.getBoundingClientRect();
    if(r.top<innerHeight*0.94&&r.bottom>0){el.classList.add('in');revIO.unobserve(el);}});});});
```
Do NOT add a global timeout that reveals everything — it kills the scroll choreography.

## 5. Focal-point photos (background-image, not <img>)
Photos are CSS backgrounds via a `--pimg` (cards) or `--photo` (hero/authority)
custom property on a container with `aspect-ratio` + `background-size:cover`.
**Per-image focal map** (a small CSS block = the "imageFocalPoints"): give each slot
a slug class and set `background-position` per image AND per breakpoint. Analyse each
photo first (where is the face/body, one person or two).
```css
#heroPhoto{background-position:16% center}      /* subject sits left in a 3:2 photo cropped to 4:5 */
.auth-photo{background-position:64% center}
.gitem.gf-sbt{background-position:22% center}    /* two people close together: keep both */
.pcard .ph.pf-globo{background-position:center 42%}  /* 16:10 crops vertically -> bias to faces */
@media(max-width:600px){#heroPhoto{background-position:19% center}}   /* mobile favours the face */
```
- **Two people at opposite edges** (impossible to portrait-crop): use *contain over a
  blurred copy of itself* — `.gcontain` has a `.gbg`(blurred cover) + `.gfg`(sharp contain).
- **Placeholders**: filename/label placeholders are hidden by default and shown ONLY
  on real load failure (`img.onerror -> el.classList.add('no-img')`). The loader regex
  accepts `assets/…`, `../assets/…` and `data:image…`:
  `/url\(['"]?((?:\.\.\/)?assets[^'")]+|data:image[^'")]+)['"]?\)/`.

## 6. Cursor digital trail (breadcrumb)
A fixed `#trail` canvas (blend `screen`, `pointer-events:none`, desktop + non-reduced
only). Each frame push the pointer position (when moved > ~5px, cap ~20 points),
draw fading cyan segments + green square "nodes"; when idle, shift the oldest so the
trail shrinks to nothing. Pair with the small shader mouse light (§1).

## 7. Chip "vertentes" (connect floating HUD chips to the subject)
Floating mono chips around the hero photo get a connector so they don't look loose —
pure pseudo-elements so they float WITH the chip (absolute, so they don't join flex flow):
```css
.chipfloat::after{content:"";position:absolute;top:50%;height:1px;width:38px}
.chipfloat::before{content:"";position:absolute;top:50%;width:5px;height:5px;border-radius:50%;
  background:var(--cyan);box-shadow:0 0 9px rgba(53,198,244,.95)}
.chipfloat.f1::after,.chipfloat.f3::after{left:100%;background:linear-gradient(90deg,rgba(53,198,244,.8),transparent)}
.chipfloat.f2::after{right:100%;background:linear-gradient(270deg,rgba(53,198,244,.8),transparent)}
.chipfloat.f1::before,.chipfloat.f3::before{left:calc(100% + 34px)}
.chipfloat.f2::before{right:calc(100% + 34px)}
```

## 8. The "virada"/reframe block — ONE distinct signature reveal
The single pivot block gets an effect used nowhere else: the headline is **drawn by
a signal** — a bright green→cyan scanner sweeps left→right while a clip-path reveals
the text in sync.
```css
.turn .big-wrap{position:relative;display:inline-block}
.turn .big{clip-path:inset(0 100% 0 -5%);transition:clip-path 1.15s cubic-bezier(.62,0,.2,1) .08s}
.turn.in .big{clip-path:inset(0 -5% 0 -5%)}
.turn .scan-line{position:absolute;top:-8%;bottom:-8%;left:-3%;width:3px;opacity:0;
  background:linear-gradient(180deg,transparent,var(--green) 28%,var(--cyan) 72%,transparent);
  box-shadow:0 0 24px 5px rgba(var(--green-rgb),.7),0 0 46px 12px rgba(53,198,244,.22)}
.turn.in .scan-line{animation:turnScan 1.25s cubic-bezier(.62,0,.2,1) .08s forwards}
@keyframes turnScan{0%{left:-3%;opacity:0}10%{opacity:1}90%{opacity:1}100%{left:103%;opacity:0}}
@media (prefers-reduced-motion:reduce){.turn .big{clip-path:none}.turn .scan-line{display:none}}
```
Triggered by the section's `.in` (the IO already adds it to `.turn`).

## 9. Supporting interactions (desktop, `pointer:fine`, non-reduced)
- **3D book** (offer/e-book): 6-face CSS box (`preserve-3d`), faces centred with
  `top/left:50% + negative margins`, `spin360` rotateY animation, cream page edges.
- **Tilt 3D**: on `.tilt`, pointermove → `transform:perspective(900px) rotateX/Y(...)`
  (skip an element while its parallax uses transform — tilt has priority).
- **Magnetic buttons**: `.magnetic` translate toward the pointer, spring back on leave.
- **Gallery**: horizontal drag-scroll carousel with snap + edge fade.

## Perf & a11y notes
- One `requestAnimationFrame` loop drives background, route, parallax, trail.
- Gate tilt/magnetic/parallax/trail behind `matchMedia('(pointer:fine)')` + not-reduced.
- Core storytelling (reveals, kinetic, shader, route) runs regardless of reduced-motion
  in this house style (client wanted it always alive) — but reduce heavy per-letter
  motion and disable the scanner/aura spins under `prefers-reduced-motion`.
