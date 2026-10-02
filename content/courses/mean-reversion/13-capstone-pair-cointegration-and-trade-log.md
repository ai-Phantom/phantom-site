---
{
  "title": "Capstone: Test a Pair, Build the Z-Score, Log a Year of Trades",
  "duration": "60 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "On the capstone's formation window (2023-09-22 to 2025-09-22) the GDX-on-GLD regression gives β = 1.2150 and a Dickey-Fuller t of −1.01. Before logging a single trade, what have you established?", "opts": ["That the pair is cointegrated", "That the pair is not cointegrated at any conventional level (5% value −3.34), so every trade that follows is a test of what a 2σ/0σ rule does to a spread with no established mean", "That β should be 1.0", "That GDX is overvalued"], "correct": 1, "explain": "The test result is the first finding of the capstone and it frames every later one. The trade log is still worth building, because seeing the consequence is the exercise."},
    {"q": "On 2025-09-23, the first trading day, GLD closed at 346.46 and GDX at 74.23. With α = −3.0057, β = 1.2150 and σ = 0.06245, the z-score is about:", "opts": ["+3.3, already outside the +2 band on day one", "−3.3", "0", "+1.0"], "correct": 0, "explain": "s = ln(74.23) + 3.0057 − 1.2150 × ln(346.46) = 4.3072 + 3.0057 − 7.1050 = +0.2079; z = 0.2079 / 0.06245 = +3.33. The formation window ended with the spread already far outside the band, so the rule shorts the spread on the first day."},
    {"q": "The 2σ/0σ rule with no stop enters short the spread on 2025-09-23 and, because z never crosses zero (minimum +1.05 on 2026-03-19, maximum +5.06 on 2026-09-08), is still open on 2026-09-23 with:", "opts": ["A profit of $1,882", "A net loss of about $1,048 on a $10,000 GDX leg, having been marked as low as −$1,436", "A net loss of $59", "Zero P&L"], "correct": 1, "explain": "GDX rose 26.0% and GLD 13.4%; short $10,000 GDX against long $12,150 GLD gives gross −$976, less $22.15 transaction cost and $49.80 borrow: −$1,048. Miners re-rated against gold for the entire year."},
    {"q": "The same year with a rolling 60-day z-score instead produced five trades and +$1,882 net. The correct conclusion is:", "opts": ["Rolling z-scores are the right method", "Rolling statistics redefined the mean as wherever the spread had recently been; the profit is real for that year but it is a different bet (that the spread oscillates around its recent level) and it says nothing about the formation-window relation the test rejected", "The static version had a bug", "Both methods are equivalent"], "correct": 1, "explain": "The two rules trade different hypotheses. Reporting one as the result of the capstone without the other, or without the cointegration test, would be selection."},
    {"q": "A submission that reproduces every number in the answer key but writes 'the pair works' as its conclusion, versus one that differs by $30 from the key and concludes that a one-year sample of a spread that failed its test cannot tell you whether the rule has an edge:", "opts": ["The first scores higher because it matched", "The second scores higher: the rubric weights the interpretation of what the sample can and cannot show, and reproducibility of method over matching a key", "They tie", "Neither passes"], "correct": 1, "explain": "The capstone's point is to show that you can run the full procedure and read its output honestly. Matching numbers is necessary; drawing the conclusion the numbers support is the harder skill."}
  ],
  "task": "Submit the capstone: the cointegration test, the z-score series, the full trade log with costs under both the base rule and the stop rule, and the one-page write-up."
}
---

This capstone asks you to do, on one ETF pair with public data, everything lessons 7 through 11 built: estimate a hedge ratio on a stated window, test the spread for cointegration, construct the z-score series, log every trade a 2σ-entry, 0σ-exit rule would have taken over the twelve months to 2026-09-23 with costs, and then write what that year can and cannot tell you. An answer key for the GLD/GDX pair is given so you can check your method. The grade is for the method and the reading, not for matching the key.

## The exercise

**Pair.** Choose one: GLD/GDX (the answer key), KO/PEP, or SPY/IWM. Do not use XLE/XOP, which the lessons worked. If you choose KO/PEP or SPY/IWM, all the same steps apply and you will report your own numbers; the lesson 7 table gives you the hedge ratio and test statistic to check against.

**Data.** Daily closes from Yahoo Finance's chart API: `https://query1.finance.yahoo.com/v8/finance/chart/GDX?period1=1695340800&period2=1790208000&interval=1d`, and the same for the other ticker. Use explicit `period1`/`period2` unix timestamps and `interval=1d`; confirm the response's `dataGranularity` is `1d` and that you have about 750 rows (the `range=max` shortcut silently returns monthly bars). Record the date you pulled the data. Use unadjusted closes for the log-price regression and for all trade prices; note any ex-dividend dates inside a trade if you want to reconcile to the cent.

**Part 1: Formation and test (lesson 7).** Formation window 2023-09-22 to 2025-09-22, common trading days only (501 for GLD/GDX). Regress ln(Y) on ln(X) with a constant; report α, β and the standard error of β. Compute the residual series s_t, its mean (should be zero to rounding) and its standard deviation σ. Run the Dickey-Fuller regression Δs_t = a + γ·s_{t−1} + b·Δs_{t−1} + u_t and report γ, its standard error and t-statistic. Compare with −3.90 / −3.34 / −3.04 and state the verdict. Also report the daily-return correlation of the two ETFs, so the contrast with the test is on the page.

**Part 2: Half-life (lesson 9).** From the same regression, λ = −γ and half-life = ln(2)/λ. Report both, and state whether the t-statistic justifies quoting the half-life at all.

**Part 3: Z-score series (lesson 8).** For every trading day from 2025-09-23 to 2026-09-23 compute s_t = ln(Y_t) − α − β·ln(X_t) and z_t = s_t / σ. Report z on the first day, the minimum and maximum with their dates, and the last day. Plot it or tabulate it at month starts.

**Part 4: Trade log, base rule.** Enter short the spread when z > +2 (short Y, long β dollars of X per dollar of Y), long the spread when z < −2; exit when z crosses 0; one position at a time. Y leg $10,000. Costs: 0.05% per side on every leg, 0.5% per year borrow on the short leg prorated by trading days / 252. For every trade record: entry date, exit date (or "open at end"), side, z in, z out, days held, all four prices, gross P&L, transaction cost, borrow, net P&L, and the worst mark-to-market during the trade. Total the year.

**Part 5: Trade log, stop rule (lesson 10).** Repeat with a stop at |z| = 4, a 60-day time stop, and a re-arm condition (no new entry after a stop until |z| is back inside 2). Same columns. Total the year.

**Part 6: Write-up, one page.** What did the test say, and did the year behave as a spread with that test result should? What was the largest mark-to-market loss and how would it have been sized under lesson 11's 1%-of-account rule? What can a single year of a single pair tell you about the rule, and what can it not? If you also ran a rolling-60 z-score, report it alongside, not instead.

## Worked example

The answer key for GLD (X) and GDX (Y). Data pulled 2026-09-24.

**Part 1.** n = 501. α = **−3.0057**, β = **1.2150** (s.e. 0.0148). Residual σ = **0.06245**. Dickey-Fuller: γ = −0.01191, t = **−1.25** with no lags, **−1.01** with one lag. Not cointegrated at 10%, 5% or 1%. Daily-return correlation **0.803**. On the last formation day, 2025-09-22 (GLD 345.05, GDX 74.33), s = ln(74.33) + 3.0057 − 1.2150 × ln(345.05) = **+0.2141**, z = **+3.43**: the window ends with the spread already 3.4 standard deviations above its own mean.

**Part 2.** λ = 0.0119; half-life = 0.6931 / 0.0119 = **58 days**. With t = −1.25, the slope is not distinguishable from zero and the half-life should be reported as "not established".

**Part 3.** 2025-09-23: GLD 346.46, GDX 74.23. s = 4.3072 + 3.0057 − 1.2150 × 5.8478 = 4.3072 + 3.0057 − 7.1050 = **+0.2079**; z = **+3.33** (the full-precision log records 3.32). Minimum **+1.05** on 2026-03-19; maximum **+5.06** on 2026-09-08; last day 2026-09-23 **+4.58**. The spread never entered the −2 to +2 band from above zero's far side; it never crossed zero at all.

**Part 4.** One trade. Short spread from 2025-09-23: short $10,000 GDX (134.7 shares at 74.23), long $12,150 GLD (35.1 shares at 346.46). Open at end, 2026-09-23: GDX 93.56 (+26.04%), GLD 392.88 (+13.40%).

Gross = −10,000 × 0.2604 + 12,150 × 0.1340 = −2,604 + 1,628 = **−$976**
Transaction cost = 2 × $22,150 × 0.0005 = **$22.15**
Borrow = $10,000 × 0.005 × 251/252 = **$49.80**
Net = **−$1,048**. Worst mark **−$1,436**; 251 trading days.

**Part 5.** Four trades, all short the spread, all losers but one: 2025-09-23 to 2025-12-17, time stop, **+$256**; 2025-12-18 to 2026-01-20, z-stop at 4.01, **−$845**; 2026-03-23 to 2026-06-17, time stop, **−$616**; 2026-06-18 to 2026-08-19, z-stop at 4.21, **−$988**. Net **−$2,193**, worst single mark −$957. The stop rule lost twice as much as the no-stop rule this year, because the spread kept ratcheting up through the entry band and the re-arm let the rule back in three more times.

**Rolling-60 comparison** (report alongside, not instead): five trades, four winners, net **+$1,882**, last trade open at −$607.

## Table

| Rule (GDX vs 1.2150 × GLD, 2025-09-23 to 2026-09-23) | Trades | Winners | Worst mark | Gross | Costs | Net |
|---|---|---|---|---|---|---|
| Formation z, ±2 / 0, no stop | 1 (open at end) | 0 | −$1,436 | −$976 | $71.95 | −$1,048 |
| Formation z, ±2 / 0, stop 4σ, time 60 d, re-arm | 4 | 1 | −$957 | −$2,068 | $124.72 | −$2,193 |
| Rolling-60 z, ±2 / 0, no stop | 5 (last open) | 4 | −$932 | +$2,008 | $126.08 | +$1,882 |

$10,000 GDX leg, $12,150 GLD leg; 0.05% per side, 0.5% annual borrow. Source: Yahoo Finance daily closes, computed by the course.

## What the sample can and cannot tell you

It can tell you that this pair, on this window, failed its test, and that the year behaved accordingly: the spread started outside the band and finished further outside it. It can tell you the size of the marks a $10,000 leg produced, −$1,436 at worst, which under a 1%-of-account rule with a 4σ stop (2 × 0.06245 = 12.5% of the leg) implies a $4,000 leg on a $50,000 account. It can show you that the stop rule and the no-stop rule lost different amounts for reasons specific to the path, and that the rolling version made money on a different hypothesis.

It cannot tell you the rule's expected value. One year is one draw of a spread whose long-run behaviour the test could not establish; a year in which gold miners re-rated against gold by 26 points is one regime. It cannot tell you that the stop is wrong because it lost more this year, or that rolling bands are right because they won. And it cannot tell you anything about a pair that passes the test, because you did not trade one. The next step, if you want to trade pairs, is to find a spread with a t-statistic beyond −3.34 on a stated window and run this same exercise on it.

## Rubric

| Criterion | What earns full marks | Points |
|---|---|---|
| Formation and test (Parts 1-2) | α, β, σ, γ with standard error and t, verdict against the stated critical values, return correlation reported; half-life reported with the caveat its t-statistic requires; data pull date and row count recorded | 20 |
| Z-score series (Part 3) | First, minimum, maximum and last values with dates, computed from the Part 1 statistics; one hand calculation shown in full | 10 |
| Base trade log (Part 4) | Every trade with all listed columns; gross, costs and net reconcile arithmetically; worst mark stated; matches the key within rounding or the difference is explained | 25 |
| Stop-rule trade log (Part 5) | Same standard; stop, time stop and re-arm applied correctly (no re-entry the day after a stop); totals reconcile | 20 |
| Interpretation (Part 6) | States what the test result implies for the year, sizes the worst mark under the 1% rule, and distinguishes what one year of one pair shows from what it does not; any rolling-z result reported alongside, not instead | 20 |
| Reproducibility | A reader with the same data source can recompute every number from what is written | 5 |
| **Total** | | **100** |

A submission that reports the rolling-z profit as the result, or that omits the cointegration test, cannot score above 55 regardless of the quality of its trade log.

## Sources

- Engle, R. F. and Granger, C. W. J. (1987). Co-integration and error correction: representation, estimation, and testing. *Econometrica*, 55(2), 251–276. https://doi.org/10.2307/1913236
- Gatev, E., Goetzmann, W. N. and Rouwenhorst, K. G. (2006). Pairs trading: performance of a relative-value arbitrage rule. *Review of Financial Studies*, 19(3), 797–827. https://doi.org/10.1093/rfs/hhj020
- MacKinnon, J. G. (2010). Critical values for cointegration tests. Queen's Economics Department Working Paper 1227. https://www.econ.queensu.ca/sites/econ.queensu.ca/files/wpaper/qed_wp_1227.pdf
- Yahoo Finance historical data: GLD https://finance.yahoo.com/quote/GLD/history/ and GDX https://finance.yahoo.com/quote/GDX/history/
