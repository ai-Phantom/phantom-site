// Safe build pass for Phantom Traders.
// Source of truth is src/index.html. This minifies it IN PLACE (inline CSS via
// clean-css, inline JS via terser) and writes the served file to ./index.html.
// Behavior is preserved: terser runs with mangle:false so global functions called
// by inline onclick="..." handlers are never renamed.
import { minify } from 'html-minifier-terser';
import { readFile, writeFile } from 'node:fs/promises';

const SRC = new URL('./src/index.html', import.meta.url);
const OUT = new URL('./index.html', import.meta.url);

const src = await readFile(SRC, 'utf8');

const out = await minify(src, {
  collapseWhitespace: true,
  conservativeCollapse: true,   // keep a single space where text relied on it
  removeComments: true,
  minifyCSS: true,
  minifyJS: {
    compress: { drop_console: false },
    mangle: false,              // never rename identifiers — global fns stay callable from onclick
    format: { comments: false },
  },
  keepClosingSlash: true,
  caseSensitive: true,
  // safety: leave attribute quoting + boolean attrs + URLs untouched
  removeAttributeQuotes: false,
  removeEmptyAttributes: false,
  decodeEntities: false,
});

await writeFile(OUT, out);
const pct = (100 * (1 - out.length / src.length)).toFixed(1);
console.log(`built index.html: ${src.length} -> ${out.length} bytes (${pct}% smaller)`);
