---
name: premium-lp
description: >-
  Build a premium, dark, cinematic single-file landing page in the "GPS" house
  style — WebGL smoke background, a GPS route/progress line with an arrow head,
  kinetic typography, scroll-reveals, focal-point photos and per-public variants.
  Use when the user asks to build an infoproduct / offer landing page "in our
  style", "like the GPS one", a new LP for cold paid traffic, or hands over page
  copy and wants it turned into a finished premium LP. Not for generic docs,
  dashboards or utilitarian pages.
---

# Premium LP — the "GPS" house style

A reusable system for building **self-contained, single-file** landing pages that
feel like a cinematic GPS/navigation interface: black→green palette, living WebGL
background, a route line that tracks scroll with an arrow head, kinetic headlines,
and photos framed with intent. Born from the *Programa GPS* project; generalized
here so the next project only needs **content in, finished LP out**.

## What you produce
- **One file**: `index.html` — vanilla HTML/CSS/JS, **no framework, no build, no npm**.
  Only external resource is the Google Fonts `<link>`. Everything else is inline.
- Optional **per-public variants** (P2, P3…) generated from P1 by a copy-swap
  script so all pages stay byte-identical in design.

## How to use this skill (workflow)
1. **Read all four references first** — they are the actual system, not summaries:
   - `references/design-tokens.css` — palette, fonts, type scale, resets (copy verbatim).
   - `references/patterns.md` — every signature effect with its code (shader, route+arrow, kinetic, reveals, focal images, cursor trail, chip vertentes, virada scan, 3D book, tilt, magnetic).
   - `references/blueprint.md` — section order for cold traffic, the copy/voice method, guardrail discipline, and the build+verify+optimize workflow.
   - `references/example-full.html` — a **complete, working** LP built with this system. Clone it as the base and swap content; it is faster and safer than assembling from scratch.
2. **Start from `example-full.html`.** Copy it to the new project's `index.html`.
   Replace the copy block-by-block (see blueprint), keep the CSS/JS/motion intact.
3. **Adapt tokens only if the brand demands it** — change the accent in
   `:root` (`--green*` / `--cyan*`) and, if needed, the display font. Keep the
   dark neutral (`--ink*`) unless told otherwise. Never flatten the motion system
   to "simplify".
4. **Generate variants** with a copy-swap script (see blueprint → per-public).
5. **Verify visually** with headless Chromium and **optimize images** before delivery
   (blueprint → build/verify). Ship previews as self-contained files.

## Design DNA (the non-negotiables that make it read as "ours")
- **Palette**: near-black neutrals with a green→cyan accent and a single amber
  "destination" accent. Neutrals are green-biased, never flat grey. (tokens file)
- **Type pairing**: `Anton` (condensed display, UPPERCASE headlines) + `Bricolage
  Grotesque` (body) + `JetBrains Mono` (HUD/labels, letter-spaced, uppercase).
- **Layered depth**: fixed living background (WebGL shader, 2D fallback) → full-page
  SVG route (z1) → content (z2). Decorative giant "ghost" wordmark for depth.
- **Motion is meaning, not decoration**: the route line *is* a progress bar with an
  arrow that sits at your reading line; branches carry "energy" into titles as you
  reach them; one block (the reframe/"virada") gets a **distinct** signature reveal;
  the cursor leaves a subtle digital trail. Everything else stays quiet.
- **HUD vocabulary**: mono labels, corner brackets, coordinate/"signal" ticks,
  connector lines (vertentes) from floating chips to the subject — used sparingly.
- **Accessibility built in**: `prefers-reduced-motion` gates the heavy motion,
  focus-visible states, `role="img"`+`aria-label` on background-image "photos",
  semantic headings, `text-wrap:balance`.

## Guardrails discipline (adapt per project, always enforce)
Every project carries a small set of **inviolable copy rules** from the client
brief (claims you must never make, credentials that must stay separate, a tone to
respect). Treat them like tests: capture them up front, and check the finished copy
against them before shipping. See blueprint → "Voice & guardrails as a method".

## Golden rules
- **Don't rebuild from scratch** when adapting — clone the example and edit surgically.
- **Reorder/adjust content; don't silently delete blocks.**
- **Tailor the whole page per public**, not just the hero — the offer bullets and FAQ
  must speak to the same reader as the headline (the #1 conversion leak we fixed).
- **Never fabricate** proof/testimonials/numbers — use a clearly-commented placeholder.
- **Keep checkout links, pixels, tracking and forms untouched** when editing content.
- **Verify before claiming done**: screenshot the real render; motion effects need a
  real browser (they won't show in a static headless frame).
