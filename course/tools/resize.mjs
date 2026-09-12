// Downsample an image using the headless browser that is already installed.
// No Pillow, no ImageMagick, no ffmpeg needed.
//
//   node training/tools/resize.mjs <in> <out.jpg> [maxWidth=1200] [quality=0.82]
//
// Used to keep course artwork small before it is embedded in a Claude Design
// canvas (the whole page is republished on every save, so bytes matter).

import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { readFileSync, writeFileSync } from 'node:fs';
import { extname, basename } from 'node:path';

const [input, output, maxWidthArg, qualityArg] = process.argv.slice(2);
if (!input || !output) {
  console.error('usage: node resize.mjs <in> <out.jpg> [maxWidth=1200] [quality=0.82]');
  process.exit(2);
}
const maxWidth = Number(maxWidthArg ?? 1200);
const quality = Number(qualityArg ?? 0.82);

const mime = { '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp' }[
  extname(input).toLowerCase()
] ?? 'image/jpeg';
const dataUrl = `data:${mime};base64,${readFileSync(input).toString('base64')}`;

const browser = await chromium.launch();
const page = await browser.newPage();
const result = await page.evaluate(
  async ({ dataUrl, maxWidth, quality }) => {
    const img = new Image();
    img.src = dataUrl;
    await img.decode();
    const scale = Math.min(1, maxWidth / img.naturalWidth);
    const w = Math.round(img.naturalWidth * scale);
    const h = Math.round(img.naturalHeight * scale);
    const canvas = document.createElement('canvas');
    canvas.width = w;
    canvas.height = h;
    const ctx = canvas.getContext('2d');
    ctx.imageSmoothingEnabled = true;
    ctx.imageSmoothingQuality = 'high';
    ctx.drawImage(img, 0, 0, w, h);
    return {
      from: [img.naturalWidth, img.naturalHeight],
      to: [w, h],
      out: canvas.toDataURL('image/jpeg', quality),
    };
  },
  { dataUrl, maxWidth, quality },
);
await browser.close();

const bytes = Buffer.from(result.out.split(',')[1], 'base64');
writeFileSync(output, bytes);
const before = readFileSync(input).length;
console.log(
  `${basename(input)} ${result.from.join('x')} ${(before / 1024).toFixed(0)} KB` +
    `  ->  ${basename(output)} ${result.to.join('x')} ${(bytes.length / 1024).toFixed(0)} KB`,
);
