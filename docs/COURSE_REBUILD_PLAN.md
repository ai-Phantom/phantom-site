# Course rebuild plan — Phantom Traders education catalog

Written 2026-09-23 from an inventory of the deployed `index.html` (`const COURSES`,
`const STORE_ITEMS`) and the Phantom Traders Stripe catalog. Status: **Phase 1 built 2026-09-23** (pipeline + Beginner bundle); phases 2–5 await the catalog decisions in the plan package.

## What exists today

Course content is inline in `index.html`: `COURSES[<id>].lessons_data[]` holds each lesson as
`{title, duration, free, content:{heading, body:'<html>'}, quiz}`. Ebooks are Google-Drive PDFs
listed in `STORE_ITEMS[].downloads`. Purchases land in Supabase `course_purchases`
(`user_id, course_id, price_paid, stripe_payment_intent, purchased_at`).

| course id | sold as | price | advertised | actually built | body text | free lessons |
|---|---|---:|---|---|---:|---:|
| foundations | Stock Market Foundations | $9 | 8 lessons / 1.5 h | 6 lessons, 6 quizzes | 5.4k chars (~900 words) | 3 |
| technical | Technical Analysis Complete | $9 | 12 / 2 h | 6, 6 | 11.6k | 5 |
| portfolio-build | Building Your First Portfolio | $9 | 6 / — | **0 — no content** | — | — |
| momentum | Momentum & Swing Trading | $29 | 15 / 3 h | 2, 2 | 4.8k | 2 |
| options | Options Trading Complete | $29 | 18 / 3.5 h | 4, 4 | 6.5k | 4 |
| tax-course | Tax Strategy for Traders | $19 | — | **0 — no content** | — | — |
| risk-mgmt | Portfolio Risk Management | $39 | — | **0 — no content** | — | — |
| algo | Algorithmic Trading Intro | $39 | 14 / 3 h | 1, 1 | 2.3k | 1 |
| institutional | Institutional Portfolio Management | $39 | 16 / 3 h | 1, 1 | 2.4k | 1 |

Bundles resell these (Beginner $20 = foundations+technical+portfolio-build; Intermediate $60;
Expert $100). The five Mastery "PDF + Course" products ($25 each, $100 for all five) are
100-page PDFs and are the only education products with real depth.

Three of nine sold courses have no content at all; the other six carry 1–6 lessons against 8–18
advertised, at roughly 400–500 words per lesson. Every lesson that exists is marked free for
most courses, so the paywall gates nothing.

## Target shape (per course)

- **12–16 lessons**, each 1,200–2,000 words of instruction plus one worked example with real
  numbers, one chart or table, a 5-question quiz with explanations, and a one-line "do this
  before the next lesson" task.
- A **capstone**: one end-to-end exercise (e.g. build and stress a 5-position portfolio; price a
  vertical spread three ways) with a rubric.
- **Free preview = lessons 1–2 only.** Everything else behind `course_purchases`.
- **Source of truth moves out of `index.html`**: one Markdown file per lesson under
  `content/courses/<course-id>/NN-slug.md` with frontmatter (title, duration, free, quiz), built
  into the page (or served from Supabase) by a script. The 64 KB inline `COURSES` block is why
  nobody has touched these since March.
- Each lesson cites its sources (CBOE/OCC for options mechanics, IRS pubs for the tax course,
  exchange docs for market structure) — the current bodies assert without citing.

## Build order (highest revenue-per-effort first)

1. **foundations, technical, portfolio-build** — the Beginner bundle. Beginner content is the
   funnel; portfolio-build currently sells with zero content.
2. **options** — highest-value intermediate topic and the one that pairs with the live signal
   channels (`#day-trades`, `#leaps`); should teach the exact vocabulary the bot embeds use
   (delta, DTE, spread cost, the 22-gate checklist).
3. **momentum** — pairs with the scanner; reuse the measured facts from the research notes
   (ORB, RSI(2), turn-of-month) as worked examples instead of generic textbook claims.
4. **risk-mgmt, tax-course** — tax must be reviewed by a CPA before sale; risk-mgmt can reuse
   the gate-stack material (P3 overlap, position caps) which is already written up.
5. **algo, institutional** — lowest volume; rebuild last or fold into one "Systematic Trading"
   course and archive the other.

## Tie-ins that must be updated together

- `STORE_ITEMS` lesson counts/durations and `COURSES.lessons` must be generated from the same
  manifest, never hand-typed (today they disagree on every course).
- Stripe product descriptions (Product catalog) should carry the same lesson count.
- `#education-portal` in Discord links to the site; add one pinned message per course launch.
- `course_purchases` needs a `bundle_id`/entitlement expansion so a bundle purchase unlocks its
  member courses (today the site checks `course_id` only).

## Not in scope

Pricing changes (decided separately), the Mastery PDFs (keep), video production.


## 2026-09-23 — what was built (Phase 1)

- **Pipeline.** `content/courses/<id>/course.json` + `NN-slug.md` (JSON frontmatter: title, duration, free,
  status, quiz[], task; Markdown body). `scripts/build-courses.mjs` renders it; `build.mjs` injects the
  result between `/*COURSES:BEGIN*/ … /*COURSES:END*/` in `src/index.html` and fills every
  `{{lessons:<id>}}` token in `STORE_ITEMS` from the same manifest. Lessons with `status: "stub"` are left
  out of the page (93 of the 133 titles were stubs).
- **Gating.** Every non-free lesson locks unless `ptOwnsCourse(id)`: `course_purchases` rows for the
  signed-in user (RLS: select own) loaded on auth change into `PT_OWNED`, bundles expanded by
  `BUNDLE_COURSES`. A locked lesson renders the paywall, not the body.
- **Purchases.** Backend PR #29: the Stripe webhook now writes one `course_purchases` row per unlocked
  course (bundles expanded, all line items, idempotent). The table had been empty forever.
- **Content.** Foundations, Technical Analysis, Building Your First Portfolio rewritten: 13 files each
  (12 lessons + capstone), lessons 1–2 free, 1,250–1,820 words per lesson, one worked example with dated
  real numbers, one table, a 5-question quiz with explanations, a task, 2–4 primary sources.
- **Quizzes** may be an array; `answerQuiz` shows the explanation after answering.
- **Full catalog map** (20 courses, 4 tracks) and the phased build order live in the plan package:
  https://claude.ai/artifact/QKtUCQcmQUnseeQ7mC2Bky

### Known follow-ups

- Page weight: the built `index.html` grew from ~780 KB to ~1.2 MB with three full courses inline.
  With all twenty it would pass 3 MB. Before Phase 3, emit one `courses/<id>.json` per course and fetch
  it in `openCourse()` instead of inlining.
- The capstone files carry their single table under `## Rubric`, not `## Table` (by design).
- Tax Strategy stays off the store until a CPA has reviewed it.
