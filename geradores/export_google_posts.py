#!/usr/bin/env python3
"""
Exporta os 10 posts do Google Meu Negócio em 1080×1080px.
Roda DEPOIS de gen_google_posts.py gerar o HTML.
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

INPUT  = Path("/home/user/Meu-espa-o/previews/nucvision-googleposts.html")
OUT    = Path("/home/user/Meu-espa-o/output/google-posts")
TOTAL  = 10
VW = VH = 420
SCALE  = 1080 / 420

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROME)
        page = await browser.new_page(
            viewport={"width": VW, "height": VH},
            device_scale_factor=SCALE,
        )
        await page.set_content(INPUT.read_text(encoding="utf-8"), wait_until="networkidle")
        await page.wait_for_timeout(3500)

        # Strip navigation chrome, normalize container
        await page.evaluate(f"""() => {{
            const nav = document.querySelector('.post-nav');
            if (nav) nav.style.display = 'none';
            const frame = document.querySelector('.post-frame');
            frame.style.cssText = 'width:{VW}px;height:{VH}px;border-radius:0;box-shadow:none;overflow:hidden;margin:0;';
            const vp = document.querySelector('.carousel-viewport');
            vp.style.cssText = 'width:{VW}px;height:{VH}px;overflow:hidden;cursor:default;';
            document.body.style.cssText = 'padding:0;margin:0;display:block;overflow:hidden;background:#000;';
        }}""")
        await page.wait_for_timeout(400)

        for i in range(TOTAL):
            await page.evaluate(f"""(idx) => {{
                const t = document.querySelector('.carousel-track');
                t.style.transition = 'none';
                t.style.transform = 'translateX(' + (-idx * {VW}) + 'px)';
            }}""", i)
            await page.wait_for_timeout(350)
            out = OUT / f"gmn_post_{i + 1:02d}.png"
            await page.screenshot(
                path=str(out),
                clip={"x": 0, "y": 0, "width": VW, "height": VH},
            )
            print(f"  {i + 1:02d}/{TOTAL} → {out.name}")

        await browser.close()
        print("✓ Exportação concluída.")

asyncio.run(run())
