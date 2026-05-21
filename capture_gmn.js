const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');

const CHROMIUM_PATH = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const BASE = '/home/user/Meu-espa-o';

(async () => {
  const browser = await chromium.launch({
    executablePath: CHROMIUM_PATH,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 420 * 10 + 200, height: 600 });

  const url = 'file://' + path.resolve(`${BASE}/nucvision-googleposts.html`);
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForTimeout(2000);

  await page.evaluate(() => {
    const vp = document.querySelector('.carousel-viewport');
    if (vp) vp.style.overflow = 'visible';
  });

  const slides = await page.$$('.slide');
  console.log(`Found ${slides.length} slides`);

  for (let i = 0; i < slides.length; i++) {
    const num = String(i + 1).padStart(2, '0');
    const outFile = `${BASE}/gmn_post_${num}.png`;
    await slides[i].screenshot({ path: outFile });
    console.log(`  → gmn_post_${num}.png`);
  }

  await browser.close();
})().catch(console.error);
