---
{
  "title": "Value at Risk and Expected Shortfall",
  "duration": "20 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The book's daily standard deviation is 0.606% on $1,000,000. Its parametric one-day 95% VaR is", "opts": ["$9,972", "$6,062", "$14,103", "$60,620"], "correct": 0, "explain": "1.645 × 0.00606 × 1,000,000 = $9,972. The 99% figure uses 2.326 and is $14,103. Both assume the daily return is normally distributed with zero mean."},
    {"q": "Historical 95% VaR from 251 daily observations means", "opts": ["The average loss", "The worst day in the sample", "The loss at the 5th percentile of the observed distribution, about the 12th or 13th worst day; here −$9,646 and −$9,140, interpolated to −$9,044", "The parametric VaR with a fatter tail"], "correct": 2, "explain": "0.05 × 251 = 12.55, so the cut falls between the 12th and 13th worst days. Historical VaR makes no distributional assumption; it just reads the sample. It cannot see anything worse than the sample contains."},
    {"q": "Expected shortfall at 95% is", "opts": ["The 95th percentile gain", "The average loss on the days beyond the VaR cut; for the book, the mean of the twelve worst days, −$11,924", "VaR times two", "The same as historical VaR"], "correct": 1, "explain": "VaR says how bad the threshold is; ES says how bad it is on average once you are past it. Basel moved the trading-book standard from 99% VaR to 97.5% ES in 2019 precisely because VaR ignores the shape of the tail."},
    {"q": "A 99% one-day VaR estimated for SPY on 2020-02-19 from the prior 250 days was 1.75% (parametric). Over the next 29 sessions, how many days breached it, against an expectation of 0.29?", "opts": ["1", "3", "29", "13"], "correct": 3, "explain": "Thirteen breaches including −7.81%, −9.57% and −10.94%. The estimate was built from a year with 0.75% daily standard deviation and the regime changed in a week. The failure is not in the arithmetic; it is in the assumption that the next month resembles the last year."},
    {"q": "Across 2005 to 2026, a rolling 99% parametric VaR on SPY was breached on 2.55% of days and a rolling 99% historical VaR on 1.56%, against 1% expected. The lesson is", "opts": ["Both understate the tail because the tail is fatter than normal and clusters; historical does better because it sees the fat tail in its own window, but only once the window contains one", "Historical VaR is exact", "Parametric VaR should use 95%", "SPY is unusually risky"], "correct": 0, "explain": "The normal distribution underweights three- and four-sigma days; a historical window fixes that only after such days are in the window. Both are worst exactly when you need them, at the start of a new regime. That is why VaR is reported alongside a stress test, not instead of one."}
  ],
  "task": "Compute your book's one-day 95% VaR both ways and its 95% ES from the last 251 days, then check how many days in the sample breached the parametric number."
}
---

## What VaR is and is not

Value at Risk is a loss threshold: the amount you would expect to lose no more than, on a stated fraction of days, over a stated horizon. A one-day 95% VaR of $10,000 says that on 95 days in 100 the loss should be smaller than $10,000, and on 5 days in 100 it may be larger. VaR says nothing about how much larger.

That silence is the reason the Basel Committee replaced 99% VaR with 97.5% expected shortfall as the trading-book standard in its 2019 market-risk framework. Expected shortfall is the average loss on the days past the threshold. Two books with identical VaR can have very different ES, and it is the one with the worse ES that ends up in the newspaper.

Both numbers are only as good as the return distribution they are read from, and there are two ways to get that distribution.

## Parametric VaR

Assume daily returns are normal with mean zero and standard deviation σ. Then VaR at confidence c is z_c × σ × NAV, where z is the standard normal quantile: 1.645 at 95%, 2.326 at 99%. Expected shortfall under the same assumption is σ × φ(z) ÷ (1 − c) × NAV, where φ is the normal density; at 95% the multiplier is 2.063.

For a portfolio, σ is computed from the covariance matrix of the positions: σ² = wᵀΣw, with w the weight vector. That is the same σ as the standard deviation of the historical portfolio return series if the weights were constant, and the worked example uses that shortcut. The parametric approach is fast, smooth and needs only σ. Its weakness is the assumption: equity returns have fatter tails than the normal, so the 99% number in particular is too small, and the assumption is at its worst just after a regime change, when σ is still the old regime's.

## Historical VaR

Take the last N daily returns of the current book, sort them, and read off the (1 − c) quantile. With N = 251 at 95%, the cut is between the 12th and 13th worst day. ES is the mean of the days beyond it.

No distribution is assumed, so fat tails are handled correctly as long as the window contains them. That is the catch. A window that contains a crash reports a large VaR for a year afterwards; a window that does not contains no information about crashes at all. The March 2020 example below is exactly this: the prior year was calm, so both methods agreed on a small number, and both were wrong by the same amount.

## When both fail

VaR is a forecast conditional on the recent past resembling the near future. The famous failures were not arithmetic errors; they were regime changes.

**2008.** Estimate SPY's one-day 99% VaR on 2008-08-29 from the prior 250 days: daily σ = 1.246%, parametric VaR = 2.326 × 1.246% = 2.90%; historical 99% VaR = 2.73%. Expected breaches over the next 85 sessions to year-end: 0.85. Actual: 22 for each method, including −7.84% (09-29), −9.84% (10-15), −8.86% (12-01). Twenty-two one-in-a-hundred days in four months.

**March 2020.** Estimate on 2020-02-19: daily σ = 0.751%, parametric 99% VaR 1.75%, historical 2.54%. Expected breaches over the next 29 sessions: 0.29. Actual: 13 for each, including −7.81% (03-09), −9.57% (03-12), −10.94% (03-16). At 95%, the parametric VaR was 1.24% and was breached on 15 of 29 days against 1.45 expected.

**The long run.** Rolling the estimate forward daily from 2005 through 2026-09-23, using each day's prior 250 returns: the 99% parametric VaR was breached on 146 of 5,716 days, 2.55%, two and a half times the nominal rate. The 99% historical VaR was breached on 89 days, 1.56%. Historical does better because its window eventually contains the fat tail; it is still wrong by half.

The practical rule: VaR is the everyday number, sized to the everyday regime. The stress test in lesson 5 is the number for the other regime, and the report carries both.

## Worked example

The course book from lesson 2. Daily return of the book = Σ wᵢ rᵢ over the ten positions, with the 2026-09-23 weights held fixed, on Yahoo adjusted closes for the 251 trading days 2025-09-24 to 2026-09-23. NAV $1,000,000.

Standard deviation of the series: **0.6062% per day** (annualised 9.6%). Mean +0.047% per day, small enough to set to zero.

**Parametric.** 95% VaR = 1.645 × 0.006062 × 1,000,000 = **$9,972**. 99% VaR = 2.326 × 0.006062 × 1,000,000 = **$14,103**. 95% ES = 2.063 × 0.006062 × 1,000,000 = **$12,504**.

**Historical.** Sort the 251 daily P&Ls. The five worst: 2026-06-17 −$14,842; 2025-11-18 −$14,126; 2026-05-26 −$13,397; 2026-02-05 −$13,176; 2026-04-30 −$12,723. The cut for 95% is at 0.05 × 251 = 12.55 observations: the 12th worst day lost $9,646 and the 13th lost $9,140. Linear interpolation gives **historical 95% VaR = $9,044**. The 99% cut at 2.51 observations interpolates to **$13,287**.

**Expected shortfall.** Mean of the twelve worst days = **$11,924**. So on the roughly one day in twenty that the book loses more than $9,000, it loses on average $11,900, and the worst such day in the window cost $14,842.

**Comparing.** Parametric 95% ($9,972) exceeds historical ($9,044) by 10%, which says the last year's tail was slightly thinner than normal at the 5% point. Parametric 99% ($14,103) exceeds historical ($13,287) by 6%. Parametric ES ($12,504) exceeds historical ES ($11,924) by 5%. Everything agrees to within about 10%, which is what you expect from a calm year. It is also what the 2020-02-19 estimate looked like: the two methods agreeing is not evidence that either is right, only that the window is homogeneous.

**Sanity check.** The parametric 95% cut, −$9,972 (−1.00%), was breached on 9 of the 251 days in its own sample: the nine days in the two histogram bins below −1.00%. Expected: 12.55. Slightly conservative within its own data, which is the minimum a VaR should manage and not much more.

## Chart

![Histogram of the book's 251 daily returns from 2025-09-24 to 2026-09-23 in 0.25% bins, from −1.50% to +2.50%. The three bins at or below −1.00% are shaded as the tail; the historical 95% VaR cut is −0.90% (−$9,044), the parametric cut −1.00% (−$9,972), and expected shortfall −$11,924. Weights fixed at the 2026-09-23 book; Yahoo Finance adjusted closes.](figures/book-daily-pnl-distribution.svg)

## Reporting VaR so that it is useful

Report it in dollars, at one confidence and one horizon, using one method as primary and the other as a check. The course standard is one-day 95%, historical primary, parametric secondary, ES alongside. Ninety-five percent is a number you will breach a dozen times a year, which means you can tell within a quarter whether the model is calibrated; 99% takes four years to falsify.

Count the breaches. If a 95% VaR is breached more than about four times in a rolling quarter, the regime has moved and the window is stale; the correct response is to shorten the window or switch the vol input to the EWMA estimate from lesson 3, not to wait for the annual average to catch up.

And write next to the number what it does not cover. It does not cover a correlation collapse (lesson 5). It does not cover a gap through the level at which you would have de-risked (lesson 7). It does not cover a broker who will not let you trade (lesson 11). Those go in the same report, as words, under the number.

## Sources

- Basel Committee on Banking Supervision (2019). "Minimum capital requirements for market risk." BCBS d457. https://www.bis.org/bcbs/publ/d457.htm
- Basel Committee on Banking Supervision (2011). "Messages from the academic literature on risk measurement for the trading book." Working Paper 19. https://www.bis.org/publ/bcbs_wp19.htm
- Artzner, P., Delbaen, F., Eber, J.-M. and Heath, D. (1999). "Coherent Measures of Risk." *Mathematical Finance* 9(3). https://doi.org/10.1111/1467-9965.00068
- Yahoo Finance historical data, SPY. https://finance.yahoo.com/quote/SPY/history/
