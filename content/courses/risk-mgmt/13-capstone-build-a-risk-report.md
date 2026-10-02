---
{
  "title": "Capstone: Build a Risk Report for a Ten-Position Book",
  "duration": "90 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The capstone book holds $100,012 of TLT among $810,527 of longs. When computing beta-adjusted net exposure, TLT's weight is multiplied by", "opts": ["1.0, because it is an ETF", "The average beta of the equity positions", "Zero, because bonds have no beta", "Its own regression beta to SPY over the stated window, whatever sign and size that turns out to be"], "correct": 3, "explain": "Beta is measured, not assumed. Over the year to 2026-09-23 TLT's beta to SPY was small and positive; in other windows it has been negative. The report uses the number the data gives and states the window."},
    {"q": "For the historical VaR, the book's daily return series must be built by", "opts": ["Multiplying each position's daily return by its fixed 2026-09-23 weight and summing across the ten positions for each of the 251 days, then reading the 5th percentile", "Averaging each position's VaR", "Taking SPY's returns times the book's beta", "Using only the long positions"], "correct": 0, "explain": "Historical VaR is the quantile of the book's own simulated P&L. Fixed weights are a simplification the capstone accepts; the alternative, rebalancing daily to the weights, is a refinement, not the method."},
    {"q": "The correlation-shock stress in the capstone replaces the last-year correlation matrix with the one from 2020-02-20 to 2020-04-30 while keeping current vols. TSLA and META, the two shorts, did not both exist as public companies in 2008 but did in 2020. Why does the capstone specify the 2020 window?", "opts": ["Because 2020 was worse than 2008", "Because correlations were lower in 2020", "Because every one of the ten tickers has daily data in that window, so the matrix is complete; a window in which a position lacks data would require an assumption for its correlations, which must then be stated", "Because 2008 data is unavailable"], "correct": 2, "explain": "A stress matrix with a missing row is not a stress test; it is a stress test plus a guess. When a position lacks crisis history, the report says so and uses a proxy or the flat-0.8 bound for that row, explicitly."},
    {"q": "An action rule in the capstone must have", "opts": ["A description of market conditions", "A number that can be read from the report, a comparison, and an action that is specific enough to execute at the next close without further decision", "A reference to a lesson", "A confidence level"], "correct": 1, "explain": "'Reduce risk if things get volatile' is not a rule. 'If SPY 20-day vol prints above its one-year figure, cut gross to 100% at that close' is. The rubric awards points for the second kind only."},
    {"q": "The rubric gives the most points to the exposures and VaR section and the least to presentation. Why?", "opts": ["Because the report's value is in numbers that are correct, sourced and reproducible; a beautiful report with the wrong gross is worse than a plain one with the right gross, since every downstream number inherits the error", "Presentation does not matter", "Because VaR is hard", "Because graders prefer tables"], "correct": 0, "explain": "The capstone is graded the way a risk desk is judged: on whether the numbers can be trusted and whether they lead to actions. Format is scored because a report that cannot be read at 6 a.m. will not be read, but it is scored last."}
  ],
  "task": "Submit the report, the data pull log and the calculation file, then re-run the daily page one week later and note what moved."
}
---

## The exercise

Build the complete risk report for the book below, as of the 2026-09-23 close, in the format of lesson 12's daily page with the weekly addendum. Everything must be computed from data you pull yourself, with the source, the dates and the row counts recorded. The book is different from the course specimen so that nothing can be copied; the methods are identical.

Deliver three things: the report (one page daily, one page weekly), the calculation file (spreadsheet or script) that produced every number, and a log of the data pull (source URL pattern, tickers, date range, rows returned per ticker, any gaps and how you treated them).

## The book

Equity $1,000,000. Prices are Yahoo Finance closes on 2026-09-23. Share counts are whole shares; weights are shares × price ÷ equity. Long market value $810,527; short market value $180,335.

## Table

| Position | Side | Shares | Price 2026-09-23 | Market value | Weight |
|---|---|---|---|---|---|
| AAPL | Long | 386 | $337.02 | $130,090 | 13.0% |
| GOOGL | Long | 355 | $337.83 | $119,930 | 12.0% |
| LLY | Long | 87 | $1,150.99 | $100,136 | 10.0% |
| CAT | Long | 111 | $812.02 | $90,134 | 9.0% |
| V | Long | 277 | $361.52 | $100,141 | 10.0% |
| WMT | Long | 814 | $110.53 | $89,971 | 9.0% |
| HD | Long | 270 | $296.72 | $80,114 | 8.0% |
| TLT | Long | 1,243 | $80.46 | $100,012 | 10.0% |
| TSLA | Short | −263 | $380.12 | −$99,972 | −10.0% |
| META | Short | −108 | $744.10 | −$80,363 | −8.0% |

Source: Yahoo Finance daily closes, pulled 2026-09-24.

Sector labels to use: AAPL and GOOGL technology/communication; LLY health care; CAT industrials; V financials; WMT consumer staples; HD consumer discretionary; TLT long Treasuries; TSLA consumer discretionary (short); META communication (short).

Data: Yahoo Finance daily adjusted closes via the chart endpoint, `https://query1.finance.yahoo.com/v8/finance/chart/<TICKER>?period1=<unix>&period2=<unix>&interval=1d`, with explicit unix timestamps. Pull from 2019-01-01 to 2026-09-24 for all ten tickers plus SPY, QQQ and BIL. Record the row count per ticker. Where a ticker lacks a trading day that SPY has, carry the prior close forward and note it. Note that at the time this course was written, several of these tickers lacked the 2026-09-22 row on Yahoo; if your pull has the same gap, treat it as stated.

Window for betas, vols, correlations and VaR: the 251 trading days from 2025-09-24 to 2026-09-23. Crisis window for the stress: 2020-02-20 to 2020-04-30.

## Required content

**Section A: exposures.** Gross, net, long and short as percent of equity. Beta of each position to SPY on the one-year window (OLS slope of daily returns) and on a three-year window (2023-09-25 to 2026-09-23). Beta-adjusted net on both windows, with the per-position products shown. Net exposure by sector. Beta of each position to QQQ on the one-year window and the net QQQ-beta-weighted exposure as the growth-factor check.

**Section B: volatility and VaR.** One-year annualised vol of each position and of SPY. The book's daily return series with fixed weights; its daily standard deviation; annualised vol. Parametric one-day 95% and 99% VaR and 95% ES in dollars, with the formulas and the z-values shown. Historical one-day 95% VaR from the sorted series, showing the two observations that bracket the 5% cut and the interpolation; historical 95% ES as the mean of the tail; the five worst days with dates. State which is the primary figure and why the two methods differ by the amount they do. Count the in-sample breaches of the parametric cut.

**Section C: correlation and stress.** The 10×10 correlation matrix for the one-year window and for the crisis window. Average pairwise correlation among the eight longs in each. Correlation of each short with the weighted long basket in each. Portfolio σ and 95% VaR recomputed with (i) crisis correlations and current vols, (ii) all off-diagonal correlations set to 0.8 and current vols, (iii) crisis correlations and crisis vols. The stress-to-base ratio for each. The replay: the book's return with current weights from 2020-02-19 to 2020-03-23, with each position's return over the window shown.

**Section D: concentration.** Herfindahl effective N on gross weights. Each position's share of portfolio variance on the one-year matrix, summing to 100%, ranked. The same on the crisis matrix. Diversification ratio on both. The largest position's loss on a 30% and a 50% gap as percent of equity. A statement of which limits from lesson 6 the book passes and fails, with the numbers.

**Section E: funding and operations.** Reg T initial and FINRA-minimum maintenance requirements. Portfolio-margin requirement as the −15% index shock on the net long. A gap of −8% longs / +4% shorts: loss, equity after, requirement after, excess under each regime. The same at 3x gross. Days to close each position at 10% of 30-day ADV at $1M and at $50M scale. Cash balance implied by the positions. Kill-switch thresholds at 2× and 3× the historical VaR.

**Section F: three action rules.** Each stated as a number readable from the report, a comparison, and an action executable at the next close. One must concern volatility, one concentration or exposure, one drawdown or funding. For each, state the date on which it would last have fired if the book had been held with these weights through 2025, using the data you pulled.

## Rubric

| Criterion | What earns full marks | Points |
|---|---|---|
| A. Exposures and betas | Gross, net, beta-adjusted net on two windows with per-position products; sector and QQQ-factor exposure; all from shares × price; betas stated with window and method | 20 |
| B. VaR and ES, both methods | Book return series built correctly; parametric and historical 95% VaR and ES with every step shown; bracketing observations and interpolation shown; worst five days dated; primary method chosen with a reason; in-sample breach count | 25 |
| C. Correlation stress and replay | Both matrices complete; three stress cases with σ and VaR; stress-to-base ratios; 2020 replay with per-position returns; correct treatment of any missing data, stated | 20 |
| D. Concentration | Effective N; variance shares on both matrices summing to 100%; diversification ratios; gap losses; explicit pass/fail against each lesson-6 limit | 10 |
| E. Funding and operations | Reg T, maintenance and portfolio-margin figures; gap scenario at 1x and 3x with call or no call; ADV liquidity at two scales; cash; kill-switch thresholds | 10 |
| F. Action rules and presentation | Three rules each with number, comparison and executable action, and the date each last fired in 2025; daily and weekly pages in lesson 12's format, limits beside values, data log complete and reproducible | 15 |

Total 100. A report scores zero on any section whose numbers cannot be reproduced from the submitted calculation file and data log, regardless of whether they are correct. A report with a gross or net figure wrong by more than 0.5 points of equity loses half of section A and all sections that inherit the error.

## Checks before you submit

Recompute gross and net by hand from the ten lines above; they should match your file to the dollar. Confirm the book return series has 251 rows and that its standard deviation, annualised, is of the same order as the weighted position vols divided by a diversification ratio between 2 and 4. Confirm the parametric and historical 95% VaR agree to within about 30% on a calm year; if they do not, look for a data error before looking for a fat tail. Confirm the variance shares sum to 100.0%. Confirm the crisis matrix has no missing entries. Confirm every action rule can be executed by someone who has only the report in front of them.

Then run the daily page again one week later with the same shares. What moved, and by how much, is the first live observation of your framework working.

## Sources

- Basel Committee on Banking Supervision (2019). "Minimum capital requirements for market risk." BCBS d457. https://www.bis.org/bcbs/publ/d457.htm
- FINRA Rule 4210, Margin Requirements. https://www.finra.org/rules-guidance/rulebooks/finra-rules/4210
- Yahoo Finance historical data for the capstone tickers. https://finance.yahoo.com/quote/AAPL/history/
