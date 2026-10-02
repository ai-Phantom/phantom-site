// Build the blog from content/blog/<slug>.md.
//
// Each post is a Markdown file with a JSON frontmatter object between `---`
// lines: title, cat (bots | indicators | education), tag, emoji, excerpt, date
// (YYYY-MM-DD), read, status. Posts whose status is not "published" are left
// out. Figures live in content/blog/figures/ and are referenced from a post as
// ![Caption](figures/name.svg).
//
// The page carries a small index of every post (no bodies) between the
// BLOG:BEGIN / BLOG:END markers in src/index.html; each body is written to
// posts/<slug>.json and fetched when the post is opened.
import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { marked } from 'marked';

const CATEGORY_ORDER = { bots: 0, indicators: 1, education: 2 };

function rendererForBlog() {
  const r = new marked.Renderer();
  r.image = function ({ href, text }) {
    const src = href.startsWith('figures/') ? `content/blog/${href}` : href;
    const caption = text ? `<figcaption>${text}</figcaption>` : '';
    return `<figure class="course-fig"><img src="${src}" alt="${(text || '').replace(/"/g, '&quot;')}" loading="lazy">${caption}</figure>`;
  };
  return r;
}

function parsePost(text, file) {
  const match = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
  if (!match) throw new Error(`${file}: missing frontmatter`);
  let meta;
  try { meta = JSON.parse(match[1]); } catch (e) { throw new Error(`${file}: frontmatter is not valid JSON — ${e.message}`); }
  for (const key of ['title', 'cat', 'excerpt', 'date']) {
    if (!meta[key]) throw new Error(`${file}: frontmatter needs "${key}"`);
  }
  return { meta, body: match[2] };
}

function displayDate(isoDate) {
  const d = new Date(`${isoDate}T12:00:00Z`);
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric', timeZone: 'UTC' });
}

export async function buildBlog(contentDir) {
  let files = [];
  try { files = (await readdir(contentDir)).filter(f => f.endsWith('.md')).sort(); } catch { return { index: [], bodies: {} }; }
  const posts = [];
  for (const file of files) {
    const { meta, body } = parsePost(await readFile(join(contentDir, file), 'utf8'), `blog/${file}`);
    if ((meta.status || 'published') !== 'published') continue;
    const id = file.replace(/\.md$/, '');
    posts.push({
      id,
      cat: meta.cat,
      tag: meta.tag || meta.cat,
      emoji: meta.emoji || '📊',
      title: meta.title,
      excerpt: meta.excerpt,
      isoDate: meta.date,
      date: displayDate(meta.date),
      read: (meta.read || '6 min').replace(/\s*read$/i, ''),
      content: marked.parse(body.trim(), { renderer: rendererForBlog() }),
    });
  }
  posts.sort((a, b) => (CATEGORY_ORDER[a.cat] ?? 9) - (CATEGORY_ORDER[b.cat] ?? 9) || b.isoDate.localeCompare(a.isoDate) || a.title.localeCompare(b.title));
  const index = posts.map(({ content, isoDate, ...rest }) => rest);
  const bodies = Object.fromEntries(posts.map(p => [p.id, { id: p.id, content: p.content }]));
  return { index, bodies };
}

export function injectBlog(html, index) {
  const begin = html.indexOf('/*BLOG:BEGIN*/');
  const end = html.indexOf('/*BLOG:END*/');
  if (begin < 0 || end < 0 || end < begin) throw new Error('src/index.html: BLOG:BEGIN / BLOG:END markers not found');
  const js = 'const BLOG_POSTS = ' + JSON.stringify(index).replace(/<\//g, '<\\/') + ';';
  return html.slice(0, begin) + '/*BLOG:BEGIN*/' + js + html.slice(end);
}
