---
{
  "title": "Capstone: Three Reports, Implied vs Realised",
  "duration": "45 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The capstone asks for the implied move 'the day before' the report. Which expiry's straddle is the right one?", "opts": ["The nearest monthly", "The first expiry after the report", "The last expiry before the report", "Any expiry, they are all the same"], "correct": 1, "explain": "Only an expiry that contains the event carries the event's variance. The last expiry before the report gives the baseline, which you may also record to strip the event out as in lesson 2."},
    {"q": "If you cannot source a dated option quote for a report, the capstone requires you to:", "opts": ["Skip that report", "Use a clearly labelled representative chain, state its assumptions, and keep the stock prices real", "Estimate from memory", "Use the current chain and pretend it is dated"], "correct": 1, "explain": "A representative chain is acceptable when it is labelled as such and its assumptions (straddle as a percentage of spot, post-event vol) are written down. Passing off a representative figure as a dated quote is the one thing the rubric fails outright."},
    {"q": "For the IV-before and IV-after comparison, which two observations should be paired?", "opts": ["The same expiry's ATM implied vol at the close before the report and at the close after", "Two different expiries", "The VIX and the stock's IV", "The bid IV and the ask IV"], "correct": 0, "explain": "The crush is the drop in a given option's implied vol once the event passes. Comparing different expiries mixes the term structure into the measurement."},
    {"q": "Three reports give straddle returns of −40%, +25% and −35%. What should the write-up conclude?", "opts": ["Straddles lose on this name", "The sample is too small to distinguish the mean from zero; report the mean, the dispersion, and the number of events a conclusion would require", "Buy the next one because it is due", "Sell strangles"], "correct": 1, "explain": "Three observations cannot establish a sign. The rubric's highest-weighted criterion is whether you say what the sample cannot show, with the arithmetic from lesson 11."},
    {"q": "Which of these belongs in the 'what the sample cannot tell you' section for a short strangle that won all three times?", "opts": ["That it is a reliable strategy", "That its loss distribution is unbounded and unobserved in the sample, so hit rate says nothing, and the honest measure is worst-case size", "That it should be scaled up", "Nothing; three wins is enough"], "correct": 1, "explain": "The absence of a tail loss in three draws is uninformative about the tail. The rubric awards points for stating this and computing the loss at a two-implied-move gap."}
  ],
  "task": "Submit the capstone: three reports, the four measurements for each, both structures' P&L, the gap-sized position for each, and the write-up, with every source URL and every representative assumption stated."
}
---

## The exercise

Choose **three real earnings reports** from the last four quarters (a report dated between late September 2025 and late September 2026) in three different companies, or in one company if you prefer, but not the four NVIDIA reports already worked in the course. For each report you will gather four measurements, price two option structures, size a position, and then write what the three-report sample can and cannot tell you. The write-up is graded by the rubric at the end.

Everything must be sourced. Stock prices come from a public daily-bar source you name (the Yahoo Finance chart API used throughout the course is acceptable: `https://query1.finance.yahoo.com/v8/finance/chart/<TICKER>?period1=<unix>&period2=<unix>&interval=1d`, with the row count verified and stated). Earnings dates come from the company's press release or 8-K. Option quotes come from a dated source if you have one (a broker's historical chain, a saved screenshot with a visible timestamp, or a data vendor); if you do not, you use a **clearly labelled representative chain** with its assumptions written out, exactly as lessons 4 and 5 did.

## The four measurements per report

1. **The implied move the day before.** Spot at the close before the report; the ATM straddle of the first expiry after the report, at that close; straddle divided by spot. If you also record the ATM straddle of the last expiry before the report you can strip the baseline as in lesson 2 and report the one-standard-deviation event move alongside the straddle figure. State the expiry dates.
2. **The realised move.** Close before to close after, as a signed percentage; the open after as a gap percentage; and the ratio gap / close-to-close.
3. **Implied vol before.** The ATM implied vol of the first-after expiry at the close before the report.
4. **Implied vol after.** The same expiry's ATM implied vol at the close of the reaction day. If representative, state the post-event baseline vol you assumed and why (the name's ordinary IV from a current chain is a reasonable anchor).

## The two structures per report

Price both on your dated or representative chain, and compute P&L at the reaction-day close and at expiry:

- **Long ATM straddle**, first expiry after the report. Cost, value at the reaction-day close (intrinsic plus residual time value at the post-event vol), value at expiry, P&L in points and as a percentage of cost.
- **Short strangle**, strikes at the listed strikes nearest one implied move either side of spot, same expiry. Credit, whether either strike was breached intraday on the reaction day (from the daily high and low), value at expiry, P&L.

Then the **gap-sized position** from lesson 10: for a stated account size and risk budget, the number of shares that survives a two-implied-move gap, and what that position would have made or lost at the actual open.

## Worked example

One report, in the format the submission should follow, using the course's representative chain so the arithmetic is visible. Substitute your own three reports; do not reuse this one.

**Report:** NVIDIA, Q4 FY2026, released after the close on Wednesday, February 25, 2026 (company press release). Daily bars: Yahoo Finance chart API, 496 rows, 2024-10-01 to 2026-09-23.

**Measurement 1, implied move.** Close before, 195.56. First expiry after: Friday, February 27, 2026. Representative straddle at 7.0% of spot (not a dated quote): 0.07 × 195.56 = **13.69** at the 195 strike. Implied move **7.0%**.

**Measurement 2, realised move.** Close after (February 26): 184.89. Realised = 184.89 / 195.56 − 1 = **−5.46%**. Open after: 194.27; gap = 194.27 / 195.56 − 1 = **−0.66%**. Ratio gap / move = −0.66 / −5.46 = **0.12**: almost the entire reaction happened inside the regular session, not at the open. Friday close (expiry): 177.19.

**Measurement 3, IV before.** Representative: straddle 7.0% over two trading days implies σ = (0.07 / 0.8) / √(2/365) = 0.0875 / 0.0740 = **118%** annualised.

**Measurement 4, IV after.** Representative baseline **40%**, chosen above the roughly 31% ordinary NVDA vol visible in the Cboe snapshot of September 2026 to be conservative.

**Long 195 straddle.** Cost 13.69. Thursday close: intrinsic |184.89 − 195| = 10.11; the 195 call is 5.2% OTM with one day left at 40% vol, worth roughly 0.05; value ≈ 10.16; P&L 10.16 − 13.69 = **−3.53 (−25.8%)**. Friday expiry: |177.19 − 195| = 17.81; P&L 17.81 − 13.69 = **+4.12 (+30.1%)**. Note the sign change between the two dates.

**Short 177.5P / 212.5C strangle.** Strikes 9.2% below and 8.7% above. Representative credit 1.4% × 195.56 = **2.74**. Reaction-day low 184.32, high 194.29: neither strike breached Thursday. Friday close 177.19: the 177.5 put finishes 0.31 in the money; P&L = 2.74 − 0.31 = **+2.43**, and the Friday low was 176.38, 1.12 through the strike intraday.

**Gap-sized position.** $50,000 account, 1% budget = $500, gap assumption 14%. Shares = 500 / (195.56 × 0.14) = 500 / 27.38 = **18**. At the actual open of 194.27 a long position lost 18 × 1.29 = $23; at the Thursday close, 18 × 10.67 = $192; at the Friday close, 18 × 18.37 = $331. All inside the budget.

**Sources for this row:** NVIDIA press release of February 25, 2026; Yahoo Finance chart API; representative chain assumptions as stated.

## Table

Submission template, one row per report, followed by the write-up.

| Field | Report 1 | Report 2 | Report 3 |
|---|---|---|---|
| Company, quarter, date, time, source URL | | | |
| Close before / open after / close after / expiry close | | | |
| First-after expiry; straddle price; source or "representative: …" | | | |
| Implied move (straddle / spot); event σ if computed | | | |
| Realised move; gap; gap / move ratio | | | |
| IV before; IV after; source or assumption | | | |
| Straddle: cost, value at reaction close, value at expiry, P&L, % | | | |
| Strangle: strikes, credit, breached intraday?, P&L at expiry | | | |
| Gap-sized shares at stated budget; P&L at actual open | | | |

## The write-up

Four hundred to eight hundred words, in this order:

1. **What the three reports show.** Mean absolute realised move against mean implied; how many of three came in under implied; the mean and dispersion of the straddle returns at expiry; the strangle's outcomes.
2. **What the sample can tell you.** The direction of the implied-realised gap in these three cases; whether the reaction-day close or the expiry mattered more for the straddle; where the gap / move ratio fell.
3. **What the sample cannot tell you.** The lesson 11 arithmetic: the t-statistic of the straddle mean, and the number of events needed to establish an edge of the size you observed. For the strangle, a statement that its loss distribution is unobserved and the loss it would take at a two-implied-move gap, in points and as a multiple of the credit.
4. **What you would record next time.** One paragraph on which measurement was hardest to source and how the journal from lesson 11 would capture it before the next report.

No claim that any structure "works." The rubric penalises it.

## Rubric

| Criterion | What earns full marks | Points |
|---|---|---|
| Sourcing and labelling | Every date from a company release or 8-K; every price from a named public source with row count; every option figure either dated with its source or explicitly marked representative with assumptions written out. Any representative figure presented as a dated quote scores zero on this criterion. | 25 |
| Measurements | All four measurements for all three reports, with every calculation shown (implied move, realised move, gap ratio, IV before and after), arithmetic correct to the stated precision. | 20 |
| Structure pricing and P&L | Straddle and strangle priced consistently with the stated chain; P&L at the reaction-day close and at expiry; intraday strike breaches checked against the daily high and low; gap-sized position computed and evaluated at the actual open. | 20 |
| Statistical honesty | The write-up computes the t-statistic and the required sample size, states that three events cannot establish a sign, and treats the strangle's unbounded loss by worst-case size rather than hit rate. | 25 |
| Clarity and process | Write-up within length, in the four-part order, in plain second person; identifies what was hardest to source and how the journal would capture it next time. | 10 |
| **Total** | | **100** |

A submission below 60 is returned for revision. A submission that loses all 25 points on sourcing is returned regardless of the other scores.

## Sources

- Yahoo Finance chart API (daily bars used throughout the course): https://query1.finance.yahoo.com/v8/finance/chart/NVDA?period1=1727740800&period2=1790467200&interval=1d
- NVIDIA, "NVIDIA Announces Financial Results for Fourth Quarter and Fiscal 2026," February 25, 2026: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
- Dubinsky, A., Johannes, M., Kaeck, A., and Seeger, N. J. (2019). "Option Pricing of Earnings Announcement Risks." Review of Financial Studies 32(2), 646–687. https://doi.org/10.1093/rfs/hhy060
- Cboe delayed option quotes (public feed), for the post-event baseline vol anchor: https://cdn.cboe.com/api/global/delayed_quotes/options/NVDA.json
