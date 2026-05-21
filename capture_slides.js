const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');

const CHROMIUM_PATH = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

async function captureSlides(htmlFile, outFiles) {
  const browser = await chromium.launch({
    executablePath: CHROMIUM_PATH,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 420 * outFiles.length + 200, height: 700 });

  const url = 'file://' + path.resolve(htmlFile);
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForTimeout(2000);

  await page.evaluate(() => {
    const vp = document.querySelector('.carousel-viewport');
    if (vp) vp.style.overflow = 'visible';
  });

  const slides = await page.$$('.slide');
  console.log(`Found ${slides.length} slides in ${htmlFile}`);

  for (let i = 0; i < Math.min(slides.length, outFiles.length); i++) {
    await slides[i].screenshot({ path: outFiles[i] });
    console.log(`  → ${path.basename(outFiles[i])}`);
  }

  await browser.close();
}

const BASE = '/home/user/Meu-espa-o';
const JOBS = process.argv[2];

const jobs = {
  editorial: {
    html: `${BASE}/nucvision-editorial.html`,
    files: Array.from({length:7}, (_,i) => `${BASE}/editorial_slide_${i+1}.png`)
  },
  slide: {
    html: `${BASE}/nucvision-editorial.html`,
    files: Array.from({length:7}, (_,i) => `${BASE}/slide_0${i+1}.png`)
  }
};

const job = jobs[JOBS] || jobs.editorial;

(async () => {
  await captureSlides(job.html, job.files);
})().catch(console.error);
