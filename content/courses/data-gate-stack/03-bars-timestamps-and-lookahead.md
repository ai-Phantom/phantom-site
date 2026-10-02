---
{
  "title": "Bars, Timestamps and Lookahead Through Stale Stamps",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Yahoo's daily bar for SPY on 2025-03-07 carries the Unix timestamp for 14:30 UTC; the bar for 2025-03-10 carries 13:30 UTC. Why?", "opts": ["The exchange opened an hour early on the 10th", "Daylight saving began on 2025-03-09, so 09:30 New York moved from UTC-5 to UTC-4; the stamp is the session open in exchange time", "A vendor error", "The 10th was a half day"], "correct": 1, "explain": "The stamp is 09:30 America/New_York on both days. Convert to exchange time before taking the date; a UTC hour is not a session."},
    {"q": "An ASX 200 daily bar carries the timestamp 2025-03-03 23:00 UTC. Normalising it to a date in UTC files the bar under:", "opts": ["2025-03-04, the correct session", "2025-03-03, the previous calendar day, because 10:00 Sydney is 23:00 UTC the day before", "2025-03-05", "It depends on the vendor"], "correct": 1, "explain": "Sydney is UTC+11 in March. Every ASX bar lands on the wrong date if the code normalises in UTC, and every join against a US series is off by a day."},
    {"q": "A scanner ran once per session over every bar of the session, stamped each signal with whichever bar qualified, and graded outcomes forward from that stamp. The average gap between the stamp and the time the row was written was 305 minutes. A reversion setup printed +0.498 R. On a clean re-run it printed −0.447 R. What happened?", "opts": ["The market regime changed between runs", "Scanning backward from the session end returned the most recent bar still qualifying, which after a bounce is the bar at the bottom of the move; the grade began from a low the scanner chose because it could already see the rebound", "The clean run used fewer tickers", "The stop was too tight"], "correct": 1, "explain": "The scanner picked the bottom because the rebound had already printed. Momentum setups scanned forward and were penalised by the same mechanism in the other direction, and the gap between two artefacts was reported as an edge."},
    {"q": "Which one-line query would have caught that bug on the first day?", "opts": ["SELECT AVG(created_at - triggered_at)", "SELECT COUNT(*) WHERE r > 0", "SELECT MAX(close)", "SELECT AVG(volume)"], "correct": 0, "explain": "Anything larger than one bar interval between when a signal was stamped and when it was written is lookahead. The fix is to bound emission to the just-closed bar, and to fix the scan cadence rather than widen the guard."},
    {"q": "A detector refuses to fire on the last bar of a session by reading bars[i+1:] to see whether a next bar exists. Is that lookahead?", "opts": ["No, it only checks existence", "No, session ends are public", "Yes; deciding at bar i using anything at i+1 or later is lookahead however innocent the purpose; express the rule against the clock instead", "Only for intraday data"], "correct": 2, "explain": "The rule 'no entry at or after 15:55' is something a detector genuinely knows at the time. 'Is there a next bar' is not. The trade-definition gate P0 failed six of six cells on exactly this and was right."}
  ],
  "task": "For any signal table you keep, compute the average gap between the bar a signal was stamped with and the time the row was written; anything over one bar interval is a defect to fix before the next lesson."
}
---

## A bar is a summary with a timestamp

A daily bar is four prices, a count and a stamp. The prices tell you what traded; the stamp tells you when the bar belongs. Both can be wrong in ways a rule cannot see, and the stamp is the more dangerous of the two, because a wrong stamp does not look wrong. It looks like a slightly earlier signal.

## What the timestamp means

Vendors stamp a daily bar with the session open in the exchange's local time and ship it as Unix seconds in UTC. SPY's bar for 2025-03-07 carries 14:30:00 UTC and the bar for 2025-03-10 carries 13:30:00 UTC. Nothing changed at the exchange; both are 09:30 America/New_York. Daylight saving began on 2025-03-09, so the offset moved from UTC−5 to UTC−4. Convert to the exchange's zone before taking the date, and treat the zone name (`exchangeTimezoneName` in Yahoo's response) as part of the data.

For a US instrument the mistake of normalising in UTC costs nothing, because 13:30 and 14:30 UTC fall on the same calendar day as 09:30 New York. For an exchange east of the date line it costs a day. The ASX 200 bar Yahoo returns for the Sydney session of 2025-03-04 carries 2025-03-03 23:00:00 UTC, which is 10:00 AEDT on the 4th. Normalise in UTC and every Australian bar files under the previous day; join that against SPY and the two series are misaligned by one session for the whole history. The research notes (Phantom Traders, 2026, internal) record a foreign-market replication that failed a data gate for an unrelated reason, a loader that fabricated open, high and low from the close and manufactured 4,508 flat bars. The point is the same: a series you did not build has conventions you have not read.

The 13-week T-bill series used as cash in later lessons is stamped in America/Chicago, not New York. Its date column is right; its Unix stamps are an hour off SPY's. A join on the Unix stamp finds nothing; a join on the exchange-local date finds everything.

## Session close versus last print

An intraday session is many bars and the last one can be fake. Some feeds emit a row at the bell with the timestamp 16:00:00, no volume and the last quoted price, before the closing auction prints. Lesson 1 showed what happens when a rule takes that row as the session close: 20% of the trades exited on it, the median correction to the auction print was 7 basis points, and a 98th-percentile result died. The gate is D4: every session must end on a bar that actually traded.

D4 is an intraday question. A daily bar is its own session, so on daily data the rule degenerates into "no bar anywhere has zero volume", which is a statement about the vendor's bookkeeping, not about prices. One vendor carries no volume for 30 to 57% of some foreign index histories and still reports every close correctly. The notes record that changing D4 to skip on daily, by name, moved exactly one verdict in 55 series, and that a first draft of the comment claimed it changed nothing. Measuring is what caught it. The dangerous daily case, a delisted name padded forward, is zero volume and no range, which is D3 and still runs.

## Lookahead through a stale stamp

The most expensive bug class in the notes is not a price defect. It is a signal stamped with a bar earlier than the one it could have been acted on, and an outcome graded forward from that stamp over price that had already printed by the time the row existed.

The mechanism, dated 2026-08-26. A scanner ran once per session and handed each detector every bar of the session. A detector stamped `triggered_at` with whichever bar qualified, and the resolver graded the path forward from that stamp. The average gap between the stamp and the row's creation was 305 minutes, roughly half a session, which is exactly what uniform selection across a session produces.

| setup | signals | average lag | stale (>6 min) | printed hit rate |
|---|---|---|---|---|
| RSI and band extreme (reversion) | 187 | 305 min | 183 of 187 | 56.1%, reported as an edge |
| opening-range break | 539 | 539 min | 538 of 539 | 23.4% |
| Donchian break | 693 | 266 min | 679 of 693 | 18.8% |

It survived review because the bias had opposite signs. Recurring setups scanned backward from the session end and returned the most recent bar still qualifying. After a bounce, the bars still qualifying are the ones at the bottom of the excursion, so the scanner picked the local low because it could already see the rebound. Momentum setups scanned forward and took the session's first breakout, which skews false. One artefact flattered reversion, the other punished breakouts, and the gap between the two was reported as a discovery. The permutation null was methodologically sound and gave the wrong answer anyway, because it compared contaminated real alerts against a clean null. The 100th percentile was measuring the lookahead.

The clean replication, 61,205 signals over ten quarters with emission bound to the just-closed bar: the reversion setup went from +0.498 R to −0.447 R, zero of ten eras and zero of 37 tickers positive. The breakout went to −0.061 R, one era of ten, indistinguishable from random.

Five checks, in the order they are cheap. Compute the average of `created_at − triggered_at`; anything beyond one bar interval is a bug. Bound emission to the just-closed bar. If the scan cadence is slower than the bar interval, fix the cadence, never the guard. Guard every detector; one had its own forward loop, bypassed the shared helper, and was still leaking a 170-minute-stale bar after the fix, caught only by a regression test. Flag contaminated history rather than deleting it, and never aggregate it with clean rows.

A cousin of the same bug hides in session rules. A detector that refuses to fire on the last bar by reading `bars[i+1:]` to see whether a next bar exists is deciding at bar i with information from i+1. The trade-definition gate P0 failed six of six cells on it, and was right. Express session rules against the clock: no entry at or after 15:55 is something a detector genuinely knows at the time.

## Worked example

The mechanism reproduces on daily SPY bars with a scanner that runs once a week. Data: Yahoo Finance SPY daily bars, 2010-01-04 to 2025-12-31, fetched 2026-09-30, closes used raw since no dividend falls inside a three-day hold often enough to matter here. The signal is RSI(2) below 10 at the close (Wilder smoothing, alpha 1/2). The outcome is the close three sessions after the graded bar divided by the graded bar's close, minus one.

The weekly scanner runs on every fifth session, looks back over the five bars of that week, and, like the backward-scanning detector above, stamps the signal with the most recent bar in the window whose RSI(2) was below 10. The stale grade measures forward from the stamped bar. The honest grade measures forward from the bar the scan actually ran on, which is the first close at which the scan's output could have been traded.

Over the window, 230 weekly scans found a signal. Stale grade: mean +1.3060% per signal, 73.5% positive. Honest grade: mean +0.3317%, 61.3% positive. The stale figure is 1.3060 / 0.3317 = 3.94 times the honest one on the same 230 rows. The mean lag between the stamped bar and the scan bar was 1.63 sessions, and the lag was greater than zero on 154 of the 230 scans.

Decomposed by lag, the two grades agree exactly on the 76 rows where the stamped bar was the scan bar itself, and disagree on every other row. At lag 1 the stale grade is +0.7253% and the honest grade is −0.2080%. At lag 3, stale +1.9135%, honest −0.4047%. The bounce that follows an RSI(2) low is concentrated in the first session or two; a stale stamp collects it, and the honest trade, entered after it has printed, gets what is left, which on average is nothing.

For comparison, a daily scan that acts at the signal bar's own close, the honest version of the same rule with no lag, produced 387 signals at +0.4795% and 58.1% positive. That is the real effect. The 1.3060% is not a stronger version of it; it is the same effect plus price that had already happened.

The lesson generalises: the check that finds this is not a better null, a holdout or a bigger sample. It is the lag column. Print it before anything else.

## Table

The weekly-scanner sample broken down by how many sessions the stamped bar preceded the scan.

| lag (sessions) | scans | stale grade, mean | honest grade, mean |
|---|---|---|---|
| 0 | 76 | +0.9366% | +0.9366% |
| 1 | 40 | +0.7253% | −0.2080% |
| 2 | 42 | +1.7286% | +0.9527% |
| 3 | 37 | +1.9135% | −0.4047% |
| 4 | 35 | +1.6223% | −0.3318% |
| all | 230 | +1.3060% | +0.3317% |

The lag-0 rows are the only ones where the two grades can agree, and they do, exactly. The whole gap sits in the rows where the scanner stamped a bar it could not have traded.

## Sources

- NYSE, Holidays and Trading Hours (session times used to interpret bar timestamps): https://www.nyse.com/markets/hours-calendars
- IANA Time Zone Database (the America/New_York, America/Chicago and Australia/Sydney rules applied above): https://www.iana.org/time-zones
- Harvey, C. R., Liu, Y. (2015). "Backtesting." Journal of Portfolio Management 42(1). https://doi.org/10.3905/jpm.2015.42.1.013
