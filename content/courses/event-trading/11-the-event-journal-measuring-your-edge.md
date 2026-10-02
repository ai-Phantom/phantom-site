---
{
  "title": "The Event Journal: Measuring Your Edge",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Which three columns must be filled in before the event, not after?", "opts": ["Realised move, P&L, notes", "Implied move, your expected move, and your thesis", "Volume, high, low", "Commission, slippage, tax"], "correct": 1, "explain": "Anything written after the outcome is known is contaminated by it. The implied move, your own expectation and your reason are the only columns that measure your judgement, and they only do so if they are timestamped before the print."},
    {"q": "Four representative NVDA straddles returned −53%, +30%, −54% and −49% of premium. The mean is −31.5% and the standard deviation about 41%. What is the t-statistic of the mean?", "opts": ["About −0.8", "About −1.5", "About −3.1", "About −6.0"], "correct": 1, "explain": "t = mean / (sd / sqrt(n)) = −31.5 / (41.1 / 2) = −31.5 / 20.6 = −1.53. Not distinguishable from zero at conventional thresholds; four observations cannot establish that the straddle loses."},
    {"q": "To detect an average edge of 10% of premium per event with a per-event standard deviation of 41%, at roughly a t of 2, you need about how many events?", "opts": ["4", "16", "67", "500"], "correct": 2, "explain": "n = (2 x 41 / 10)^2 = 8.2^2 = 67. At eight reports a year in one name, that is over eight years; across ten names it is under one. This is why the journal must span many names and why a single name's record proves nothing."},
    {"q": "Why can the journal not compute an honest t-statistic for the short strangle after four full-credit wins?", "opts": ["Because the credit was too small", "Because the sample contains no loss, so its standard deviation understates the strategy's true dispersion, which is dominated by the rare unbounded loss", "Because strangles are not journalled", "Because four is an even number"], "correct": 1, "explain": "A strategy with unbounded loss has a distribution whose variance is set by the tail. If the tail has not occurred in your sample, your sample variance is wrong, and any t computed from it is meaningless."},
    {"q": "The ratio 'gap / close-to-close move' in the journal is meant to capture:", "opts": ["The commission rate", "How much of the reaction was already in the open, so that a day trader knows whether there was anything left to trade", "The implied volatility", "The consensus"], "correct": 1, "explain": "A ratio near 1 means the open was the whole move; well below 1 means the session continued it; negative means the open reversed. NVDA's four reports gave −1.61, 0.12, 0.30 and 0.72."}
  ],
  "task": "Set up the journal with the columns in this lesson and back-fill it with the last four events you actually traded, using your broker statements for the fills, not your memory."
}
---

## The only evidence that applies to you

Every study cited in this course is an average over thousands of events, in a sample that ended before you started trading, executed at institutional costs. Whether *you* have an edge in event trading is a question none of them can answer. The event journal is the instrument that can, and it works only if it is designed so that its answer cannot be argued with afterward.

The journal has three jobs. It records what the market expected and what you expected, before the outcome. It records what happened, in several separately measured pieces, after. And it lets you compute, from a large enough sample, whether the difference between your expectation and the market's was worth anything.

## The columns

One row per event per position. The row is opened before the print and closed after expiry or exit.

**Filled before the event, timestamped:**

- Date and time of the event, and the source it was confirmed from.
- Name, event type (earnings, FOMC, CPI, NFP, index, other).
- Spot at the time of entry.
- Implied move: ATM straddle of the first expiry after the event divided by spot, with the expiry date.
- Your expected move, as a number, and its sign if you have a directional view.
- Thesis, one sentence.
- For macro prints: the consensus, by survey name, and the regime in one line from the latest FOMC statement.
- Structure, strikes, expiry, size, entry price, and the gap-sized share or contract count from lesson 10.
- Exit plan: what you do at the open, at 15 minutes, at the close of the reaction day, at expiry.

**Filled after:**

- Realised move, close before to close after, and the gap (open after over close before).
- The ratio gap / close-to-close, which tells you how much of the move was in the open.
- For earnings: the surprise against guidance (lesson 3), separately from the reaction.
- Position value at the reaction-day close and at expiry or exit; P&L in dollars and as a percentage of premium or of the risk budget.
- Fills, commissions and the bid-ask paid, from the broker statement.
- Did you follow the exit plan? Yes or no, and if no, why, in one line.

That last column is the one most people leave out and the one that explains most of the variance in retail event trading.

## Worked example

Back-fill the journal with the four representative NVDA straddles from lesson 5. Stock prices are real (Yahoo Finance daily bars); the straddle costs are the labelled representative 7.0% of spot, held to the Friday expiry. Returns are P&L divided by premium paid.

- **2025-11-19.** Implied 7.0%. Realised −3.15%. Gap +5.06%; ratio 5.06 / −3.15 = **−1.61** (the open reversed). Straddle return **−53.1%**.
- **2026-02-25.** Implied 7.0%. Realised −5.46%. Gap −0.66%; ratio **0.12**. Straddle return **+30.1%**.
- **2026-05-20.** Implied 7.0%. Realised −1.77%. Gap −0.53%; ratio **0.30**. Straddle return **−54.2%**.
- **2026-08-26.** Implied 7.0%. Realised +8.74%. Gap +6.30%; ratio **0.72**. Straddle return **−48.6%**.

**Implied versus realised.** Mean |realised| = (3.15 + 5.46 + 1.77 + 8.74) / 4 = 4.78%. Ratio to implied: 4.78 / 7.0 = **0.68**. Three of four under implied.

**Mean return.** (−53.1 + 30.1 − 54.2 − 48.6) / 4 = −125.8 / 4 = **−31.5%** of premium per event.

**Standard deviation.** Deviations from the mean: −21.6, +61.6, −22.7, −17.1. Squares: 466.6, 3794.6, 515.3, 292.4; sum 5068.9; divide by n − 1 = 3: 1689.6; square root: **41.1%**.

**t-statistic of the mean.** t = mean / (sd / √n) = −31.5 / (41.1 / 2) = −31.5 / 20.55 = **−1.53**. A t of 1.53 with three degrees of freedom is nowhere near a conventional threshold. The four losses in a row *feel* like evidence; the arithmetic says they are consistent with a strategy whose true mean is zero, or positive.

**How many events would it take?** To establish an average edge of size m with per-event standard deviation s at a t of about 2, you need n ≈ (2s / m)². For m = 10% of premium and s = 41%: n ≈ (82 / 10)² = 8.2² = **67 events**. For m = 20%: (82 / 20)² = 4.1² = **17 events**. One name reports four times a year, so 67 events is seventeen years in one name, or under two years across ten names. The journal has to span many names, and the question it can answer in the first year is only whether your edge is *large*.

**The strangle's row.** Returns on credit: +100%, +88.7%, +100%, +100%. Mean +97%, standard deviation 5.6%, t = 97 / (5.6 / 2) = **34.6**. That number is meaningless. The strangle's true standard deviation is set by the loss it takes when the stock gaps through a strike by 10%, which did not occur in four draws. The journal must flag any short-unbounded structure and refuse to compute a t for it until the sample contains at least one of its tail losses, and the honest way to evaluate it in the meantime is by worst-case size (lesson 10), not by hit rate.

## Table

| Event | Implied | Realised | Gap | Gap / move | Surprise vs guidance | Straddle return | Followed plan? |
|---|---|---|---|---|---|---|---|
| 2025-11-19 | 7.0% | −3.15% | +5.06% | −1.61 | (not computed) | −53.1% | (back-fill) |
| 2026-02-25 | 7.0% | −5.46% | −0.66% | 0.12 | +4.8% | +30.1% | (back-fill) |
| 2026-05-20 | 7.0% | −1.77% | −0.53% | 0.30 | +4.6% | −54.2% | (back-fill) |
| 2026-08-26 | 7.0% | +8.74% | +6.30% | 0.72 | +5.7% | −48.6% | (back-fill) |
| **Mean** | 7.0% | \|4.78%\| | | | | **−31.5%** (sd 41.1%, t −1.53) | |

## What the journal will show you first

Long before it can measure an edge, the journal will show you three things that matter more:

**Whether your expected move has any relationship to the realised move.** Plot your expected against realised across all rows. If the cloud has no slope, your event judgement is noise and the structures you chose to express it were the whole trade. Most traders find this within twenty rows, and it is the most useful thing the journal ever tells them.

**Whether you follow your exit plan.** Count the "no" answers. If the P&L of the rows where you deviated is worse than the rows where you did not, which it usually is, the edge you need is not in the market.

**What costs are doing.** Sum the bid-ask and commissions column and compare it to gross P&L. In lesson 2's example, costs were up to a fifth of the seller's gross edge on a single straddle. Over a year of weekly options the comparison is often the difference between a strategy that works on paper and one that does not in the account.

## Reading the two columns that matter most

The **gap / move ratio** distribution tells you whether there is anything for a day trader to do after an event in your names. NVDA's four rows gave −1.61, 0.12, 0.30, 0.72: one reversal, one where the open was essentially flat and the session did the whole move, two in between. If, after forty rows, most ratios are near 1, the reaction is in the open and your intraday process is fighting for scraps. If many are negative, the open is systematically wrong and a fade has something to work with. Four rows say nothing; forty might.

The **surprise versus reaction** pair tells you which of the two you are actually responding to. In the three NVDA rows with a computed surprise, all three surprises were positive and the reactions were −5.46%, −1.77% and +8.74%. A trader whose thesis column says "beat expected" and whose expected-move column says "+5%" has, on this record, been right about the surprise every time and right about the reaction once. That is the kind of thing you cannot see without the columns being separate.

## Sources

- Chung, S. G., and Louis, H. (2017). "Earnings announcements and option returns." Journal of Empirical Finance 40, 220–235. https://doi.org/10.1016/j.jempfin.2016.07.010 (the conditioning variables, prior realised volatility relative to implied, that a journal can test)
- Chordia, T., Goyal, A., Sadka, G., Sadka, R., and Shivakumar, L. (2009). "Liquidity and the Post-Earnings-Announcement Drift." Financial Analysts Journal 65(4), 18–32. https://doi.org/10.2469/faj.v65.n4.3 (why the costs column decides)
- NVIDIA press releases for the four reports: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2026; https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026; https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027; https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
