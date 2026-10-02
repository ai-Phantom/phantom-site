---
{
  "title": "Replication on a Fresh, Pre-Registered Universe",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "An internal-bar-strength rule passed on 6 of 38 development names against a measured noise maximum of 2. On a fresh, pre-registered cross-sector universe it passed 1 of 34 against a noise range of 0 to 1. At a 5% false-positive rate, 1 or more passes out of 34 happens by chance:", "opts": ["About 5% of the time", "About 83% of the time, so the fresh result is exactly what no edge looks like", "Never", "About 50% of the time"], "correct": 1, "explain": "1 - 0.95^34 = 0.825. Six of 38 by chance is about 1%, which is why the development result cleared the floor; the fresh universe is where it died."},
    {"q": "The same rule was first replicated on 15 semiconductor names, 12 of which were positive with equally large nulls. Why did the notes redo the test on 34 cross-sector names?", "opts": ["Semiconductors have bad data", "The sample was too large", "The rule is sector-specific", "Fifteen names from one high-drift sector is a narrow test dressed as a broad one; the rule made money there and so did random entry"], "correct": 3, "explain": "How a test fails matters. Positive returns with positive nulls of the same size say the sector rose, not that the signal worked."},
    {"q": "A 52-week-high rule first reported 0 of 4 on a fresh universe. On inspection, sixty-day holds with non-overlapping stepping had starved the locked window below the 25-trade floor. Re-powered, it read 1 of 17. What was the first result?", "opts": ["A failed test, not a failed strategy; a tiny denominator is a broken test, never a result", "A valid negative", "A pass", "Inconclusive but usable"], "correct": 0, "explain": "Check that the test actually ran before filing its verdict. A zero from a starved test would have been archived as a negative and never revisited."},
    {"q": "Before a confirmatory run on two metals ETFs, the criterion was fixed as both above the 95th percentile. One died at the geometry gate and the other reached the 76th. The generating result had arrived on the 19th test of the rule with an effective sample near two. What does the pre-registration buy?", "opts": ["A second chance with a looser bar", "Nothing; the result speaks for itself", "A miss that ends the line; without the fixed criterion the 76th would have been read as encouraging and the search would have continued", "A larger sample"], "correct": 2, "explain": "A criterion written before the run is the only thing that makes a miss final. Written after, every miss is a near miss."},
    {"q": "RSI(2) developed on SPY, then pre-registered on six ETFs with a 95th-percentile-and-positive criterion: QQQ 98th and XLF 99.7th pass, IWM, TLT, EFA and GLD do not. QQQ and XLF have daily-return correlations of 0.93 and 0.87 with SPY. The honest verdict is:", "opts": ["Replicated on 2 of 6, well above the 0.3 expected by chance", "The rule works on anything", "The two passes are close to the same bet as the development instrument, so the count overstates the number of independent confirmations; the rule replicates inside US equity beta and not outside it", "The four failures disprove the rule"], "correct": 2, "explain": "Two of six against a 3.3% chance of two or more is real, and the effective number of independent looks among the equity ETFs is close to one. Both statements go in the ledger."}
  ],
  "task": "Write down, before running anything, a fresh universe of at least twenty names your rule has never touched, the exact criterion for a pass, and the number of passes chance would give; then run it once."
}
---

## The gate that kills what passes the other two

By the time a rule reaches this lesson it has beaten its matched null and it is positive after measured cost. The research notes (Phantom Traders, 2026, internal) record two rules that did both and then died on replication, and the record of their deaths is the reason this gate exists.

An internal-bar-strength rule passed on 6 of 38 names in the development universe, against a measured noise maximum of 2 passes. An inside-day rule passed on 8 of 41, against a measured false-positive rate of 1.3. Both cleared the noise floor. The internal-bar-strength rule was then run on a fresh, pre-registered universe: 2 of 15 semiconductor names (noise 0 to 3), and after that test was recognised as too narrow, 1 of 34 cross-sector names (noise 0 to 1). Dead. The inside-day rule had passed on 6 of 10 hand-picked names that clustered in mega-cap technology and 4 of 30 untouched ones; stated as a hypothesis and tested on 15 fresh large-cap names, it passed 1, where chance gives 0.75. Found by looking, killed by pre-registering.

The gate is three-deep. First, beats its matched null and is positive after cost. Second, above the measured false-positive rate of the fitting procedure: re-run the identical pipeline on a random signal and count, never assume the rate. The notes guessed about 2.5% once and measured 1.3 in 41. Third, replicates on a fresh, broad, pre-registered universe. The third is the one that kills things that pass the first two.

## Why development universes pass

A rule that was found by looking at a set of names has already been selected for looking good on those names. The pass count on the development universe is the maximum over a search, and the noise floor it is compared to was measured on a single random signal that was not searched. A rule can clear that floor honestly and still be nothing more than the best of several hundred things tried on the same data. The only test that does not share the selection is a set of names the search never touched, chosen before the result was known.

The RSI(2) book in the notes is the fullest example. Seven of sixteen names in the live book passed every gate. A parameter surface then found that a threshold of 5 passed 10 of 13 against the live threshold's 7 of 13. Both were pre-registered as candidates for a fresh universe of eleven names never in the book. Result: 0 of 11 at either threshold. Three died at the data gates (a two-source disagreement, an 83% seam under a re-used ticker, 202 padded bars), six at the geometry gate, two at the null. At portfolio level the same shape: 1.18 Sharpe against cash on the sixteen in-book names, 0.05 on the eight fresh names that passed the data gates, 0.02 on all eleven. The surface's 10 of 13 had been the in-sample side of a sweep. The conclusion the notes record is a rule fitted to a universe, not an effect, with the selection unrepeatable (a measured selection premium of −0.04 Sharpe), and the instruction that nothing there should be sized.

## Test-design traps

Three were hit while doing this and each would have been filed as a result.

A narrow "broad" test proves nothing. The first fresh universe was pre-registered as "works broadly on liquid US equities" and tested on 15 semiconductor and software names, one high-drift sector. It had to be redone across 34 cross-sector names.

How it fails matters. On the semiconductors, 12 of 15 were positive (+0.31% to +1.66% per trade) with equally large nulls. The rule made money on high-drift names, and so did random entry. A pass count that ignores the null is a drift count.

Check the test actually ran. A 52-week-high rule first reported 0 of 4 on its fresh universe. Sixty-day holds with non-overlapping stepping had starved the locked window below the 25-trade floor. Re-powered, it read 1 of 17, a valid negative. A tiny denominator is a broken test, never a result.

## Pre-registration makes a miss final

A confirmatory run on two metals ETFs had its criterion fixed before the run: both above the 95th percentile. One died at the geometry gate; the other, the only one to reach the null, landed at the 76th, inside the 40th-to-80th band the notes had predicted and far below the 98th and 88th that had generated the lead. Formally inconclusive, substantively not supported. The generating result had an effective sample near two and had arrived on the nineteenth test of the rule; that prior earned this outcome. A gold ETF was excluded from the confirmatory set deliberately because it holds the same metal as the ETF that generated the lead and would have confirmed by construction. The criterion was fixed in advance precisely so that a miss ends the line.

## Worked example

The RSI(2) rule from Lessons 7 and 8 was developed on SPY. Before running anything else, the replication was written down: six exchange-traded funds the rule had never been run on, chosen for breadth across asset classes (QQQ, IWM, EFA, TLT, GLD, XLF); the identical rule and cost (RSI(2) below 10 at the close, exit at the first close above the 5-day average, 5 bps per side); the window 2010-01-04 to 2025-12-31; the criterion, at or above the 95th percentile against a matched random-entry null of 2,000 draws and net positive per trade. Data from Yahoo Finance, fetched 2026-09-30, dividend-adjusted.

Chance first. At a 5% false-positive rate, the expected number of passes in six is 6 × 0.05 = 0.3. The probability of two or more is 1 − 0.95^6 − 6 × 0.05 × 0.95^5 = 1 − 0.7351 − 0.2321 = 0.0328, about 3.3%.

| ETF | trades | net per trade | win rate | null mean | percentile | buy-and-hold | pass |
|---|---|---|---|---|---|---|---|
| QQQ | 177 | +0.5366% | 67.8% | +0.1738% | 98.2 | +1,423% | yes |
| XLF | 189 | +0.5557% | 73.0% | +0.0881% | 99.7 | +509% | yes |
| IWM | 180 | +0.2449% | 68.9% | +0.0863% | 78.5 | +378% | no |
| TLT | 182 | +0.0604% | 63.2% | −0.0394% | 77.0 | +54% | no |
| EFA | 170 | −0.0441% | 62.9% | +0.0299% | 32.4 | +173% | no |
| GLD | 173 | −0.0080% | 64.7% | +0.0701% | 31.6 | +261% | no |

Two of six pass, against a 3.3% chance of two or more. That is a real replication by the criterion as written.

Then the concentration check that Lesson 10 formalises. The daily-return correlation with SPY over the window is 0.93 for QQQ and 0.87 for XLF; the two passes are the two instruments that most resemble the development instrument. EFA, at 0.86, is nearly as correlated and failed, which is the one piece of evidence against reading the passes as pure SPY beta. TLT and GLD, at −0.30 and +0.05, are the genuinely independent looks, and both failed; TLT's null is negative and its rule is slightly positive, which is Lesson 6's information-not-profit shape at +0.06% per trade. Among the five equity ETFs including SPY, the mean pairwise correlation is 0.824, which makes them about 1.16 independent looks.

The ledger entry, written both ways because both are true: replicated on 2 of 6 pre-registered instruments (chance 3.3%); the two are within US equity beta and count for about one independent confirmation; no replication outside equities. What that buys is a narrower hypothesis for the next fresh universe, US equity ETFs and sector funds the rule has not touched, with the criterion again written first.

## Table

Every replication in this lesson, with what chance would have given and what was found.

| Rule | Development result | Fresh universe | Chance | Found | Verdict |
|---|---|---|---|---|---|
| Internal bar strength | 6 of 38, noise max 2 | 34 cross-sector names | 1+ passes 82.5% of the time | 1 of 34 | dead |
| Inside-day / NR7 | 6 of 10 hand-picked, 4 of 30 | 15 fresh large-caps | 0.75 expected | 1 of 15 | dead |
| RSI(2) threshold 5 and 10 | 7 of 16 in book; 10 of 13 on the surface | 11 names never in the book | 0.55 expected | 0 of 11 | fitted to a universe |
| Inside-day, metals | 98th and 88th on two ETFs | PPLT and PALL, both above 95 required | n/a, two names | G1 and 76th | line closed |
| RSI(2) on SPY (this course) | 95th on SPY | 6 ETFs, 95th and positive | 2+ passes 3.3% | 2 of 6, both US equity | replicates inside equity beta only |

The rows that say dead are the rule's fresh-universe count sitting inside what chance gives. The last row is a pass with a qualifier, and the qualifier is the finding.

## Sources

- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., Mellor, D. T. (2018). "The preregistration revolution." Proceedings of the National Academy of Sciences 115(11). https://doi.org/10.1073/pnas.1708274114
- McLean, R. D., Pontiff, J. (2016). "Does Academic Research Destroy Stock Return Predictability?" Journal of Finance 71(1). https://doi.org/10.1111/jofi.12365
- Harvey, C. R., Liu, Y., Zhu, H. (2016). "... and the Cross-Section of Expected Returns." Review of Financial Studies 29(1). https://doi.org/10.1093/rfs/hhv059
- Yahoo Finance, QQQ historical data (the other five ETFs are on the same site): https://finance.yahoo.com/quote/QQQ/history/
