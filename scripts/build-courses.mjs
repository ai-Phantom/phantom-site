// Build the COURSES object from content/courses/<id>/{course.json, NN-slug.md}.
//
// Source of truth for every lesson is its Markdown file. Frontmatter is a JSON
// object between `---` lines (title, duration, free, status, quiz, task). The
// body is Markdown; a body that starts with `<` is treated as already-HTML
// (the pre-2026-09 lessons were authored that way). Lessons whose status is
// not "published" are left out of the page entirely, so lesson counts in the
// store always describe what a buyer actually gets.
//
// build.mjs calls buildCourses() and injects the result between the
// COURSES:BEGIN / COURSES:END markers in src/index.html, and replaces every
// {{lessons:<course-id>}} token with the published lesson count.
import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { marked } from 'marked';

marked.setOptions({ gfm: true, breaks: false });

function parseFrontmatter(text, file) {
  const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
  if (!m) throw new Error(`${file}: missing frontmatter`);
  let meta;
  try { meta = JSON.parse(m[1]); } catch (e) { throw new Error(`${file}: frontmatter is not valid JSON — ${e.message}`); }
  return { meta, body: m[2] };
}

function minutes(duration) {
  const m = /(\d+)/.exec(duration || '');
  return m ? Number(m[1]) : 10;
}

function totalDuration(lessons) {
  const mins = lessons.reduce((a, l) => a + minutes(l.duration), 0);
  if (mins < 60) return `${mins} min`;
  const h = mins / 60;
  return `${Number.isInteger(h) ? h : h.toFixed(1)} hrs`;
}

function validateQuiz(quiz, file) {
  if (!quiz) return null;
  const list = Array.isArray(quiz) ? quiz : [quiz];
  list.forEach((q, i) => {
    if (!q.q || !Array.isArray(q.opts) || q.opts.length < 2) throw new Error(`${file}: quiz[${i}] needs q and opts`);
    if (!Number.isInteger(q.correct) || q.correct < 0 || q.correct >= q.opts.length) throw new Error(`${file}: quiz[${i}].correct out of range`);
  });
  return list;
}

export async function buildCourses(contentDir) {
  const courses = {};
  const manifest = {};
  const ids = (await readdir(contentDir, { withFileTypes: true })).filter(d => d.isDirectory()).map(d => d.name).sort();
  for (const id of ids) {
    const dir = join(contentDir, id);
    const meta = JSON.parse(await readFile(join(dir, 'course.json'), 'utf8'));
    const files = (await readdir(dir)).filter(f => /^\d{2}-.*\.md$/.test(f)).sort();
    const lessons = [];
    for (const f of files) {
      const { meta: fm, body } = parseFrontmatter(await readFile(join(dir, f), 'utf8'), `${id}/${f}`);
      if ((fm.status || 'published') !== 'published') continue;
      const trimmed = body.trim();
      const html = trimmed.startsWith('<') ? trimmed : marked.parse(trimmed);
      lessons.push({
        id: lessons.length + 1,
        title: fm.title,
        duration: fm.duration || '10 min',
        free: fm.free === true,
        content: {
          heading: fm.title,
          body: html,
          quiz: validateQuiz(fm.quiz, `${id}/${f}`),
          task: fm.task || null,
        },
      });
    }
    courses[id] = {
      ...meta,
      id,
      lessons: lessons.length,
      duration: totalDuration(lessons),
      lessons_data: lessons,
    };
    manifest[id] = { lessons: lessons.length, duration: courses[id].duration, free: lessons.filter(l => l.free).length };
  }
  return { courses, manifest };
}

// JSON is a valid JS object literal. `</` is escaped so a lesson body can
// never terminate the inline <script> that carries it.
export function coursesToJs(courses) {
  return 'const COURSES = ' + JSON.stringify(courses).replace(/<\//g, '<\\/') + ';';
}

export function injectCourses(html, courses, manifest) {
  const begin = html.indexOf('/*COURSES:BEGIN*/');
  const end = html.indexOf('/*COURSES:END*/');
  if (begin < 0 || end < 0 || end < begin) throw new Error('src/index.html: COURSES:BEGIN / COURSES:END markers not found');
  let out = html.slice(0, begin) + '/*COURSES:BEGIN*/' + coursesToJs(courses) + html.slice(end);
  out = out.replace(/\{\{lessons:([a-z0-9-]+)\}\}/g, (_, id) => {
    if (!manifest[id]) throw new Error(`{{lessons:${id}}}: no such course in content/courses`);
    return String(manifest[id].lessons);
  });
  return out;
}
