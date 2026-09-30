---
{
  "title": "The Implied Move: Reading the Straddle",
  "duration": "18 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "Spot is 228.56 and the ATM straddle expiring just after an earnings date trades at 26.90. What is the implied move by the straddle convention?", "opts": ["5.9%", "8.2%", "11.8%", "23.5%"], "correct": 2, "explain": "Implied move = straddle price / spot = 26.90 / 228.56 = 0.1177, about 11.8%. That figure covers the whole life of the option, not just the event, which is why lesson 2 also strips out the baseline."},
    {"q": "Why does the course convert straddle prices into variance before subtracting one expiry from another?", "opts": ["Because variance is what brokers quote", "Because variances over non-overlapping periods add, while volatilities and straddle prices do not", "Because it makes the number smaller", "Because Cboe requires it"], "correct": 1, "explain": "Total variance to an expiry is the sum of variance over each sub-period, so the event's contribution is the difference in total variance between an expiry after the event and one before it. Straddle prices scale with the square root of time and cannot be subtracted directly."},
    {"q": "Which statement best summarises the academic record on implied versus realised earnings moves?", "opts": ["Straddles always lose because implied is always too high", "Straddles always win because implied is always too low", "Implied has tended to exceed realised on average, but not uniformly, and the gap varies with regime and with how recent volatility compares to implied", "The literature has not studied it"], "correct": 2, "explain": "Dubinsky et al. (2019) document a premium in option-implied earnings variance; Chung and Louis (2017) find pre-announcement straddle returns that are positive on average, concentrated after low-volatility periods. Both cannot be reduced to one rule."},
    {"q": "For a short-straddle seller, what does 'the stock moved less than implied' mean at expiry?", "opts": ["The trade was profitable, before costs, because the payout owed was smaller than the premium collected", "The trade lost", "The trade broke even exactly", "Nothing; short straddles are not affected by the move"], "correct": 0, "explain": "The seller collects the straddle price and owes |move| at expiry. If |move| is smaller than the premium collected, the difference is the seller's gross profit, before commissions, slippage and the capital tied up in margin."},
    {"q": "The 0.8 factor in 'straddle is about 0.8 of a one-standard-deviation move' comes from:", "opts": ["An exchange rule", "The expected absolute value of a normal variable, sqrt(2/pi) is about 0.80", "Average bid-ask spread", "The delta of the ATM call"], "correct": 1, "explain": "A fairly priced ATM straddle pays E|X| for a normal move X with standard deviation sigma, and E|X| = sigma times sqrt(2/pi), which is 0.798 sigma."}
  ],
  "task": "For one name that reports in the next three weeks, write down spot, the ATM straddle of the first expiry after the report, the ATM straddle of the last expiry before it, and the implied move both ways (straddle/spot and event sigma)."
}
---

## What the straddle price says

The at-the-money straddle is a long call and a long put at the same strike and expiry. At expiry it pays the absolute value of the move away from the strike. Because the market has to price that payout, the straddle's price is the market's estimate of the *expected absolute move* to that expiry, and dividing it by the stock price gives that estimate as a percentage. That percentage is what traders, brokers and financial media call the **implied move** or **expected move**.

Two things follow immediately. The straddle covers the entire life of the option, not just the event. A straddle expiring 58 days out includes 57 ordinary days and one earnings night, and its price bundles them. And the straddle prices an *expected absolute value*, not a standard deviation. For a normally distributed move with standard deviation σ, the expected absolute value is σ times √(2/π) ≈ 0.80σ. So the straddle convention gives you roughly 0.8 of a one-standard-deviation move. If you want the standard deviation, divide by 0.8.

The rest of this lesson does the arithmetic on a real chain, then puts the result next to what the stock actually did on its last four reports, then reads what the academic literature has found when it did the same thing across thousands of reports.

## Isolating the event from the term structure

You saw the term structure in the options course: implied volatility plotted against expiry. Into an earnings date it has a step. Expiries that end before the report carry only ordinary volatility. Expiries that end after it carry ordinary volatility plus the event. The height of the step is the event's contribution.

To extract it you cannot subtract volatilities, because volatility scales with the square root of time. You subtract *variance*, because variance over non-overlapping periods adds. With annualised implied volatility σ and time to expiry T in years, total variance is σ²T. Take an expiry after the event with total variance σ₂²T₂ and assume the baseline volatility of the pre-event expiry, σ₁, would have applied over the whole period T₂ had there been no event. Then:

event variance = σ₂²T₂ − σ₁²T₂ = (σ₂² − σ₁²)T₂

and the one-standard-deviation event move is the square root of that. This is the standard reduced-form decomposition used in Dubinsky, Johannes, Kaeck and Seeger (2019); their estimators are more careful about the baseline, but the logic is the same.

## Worked example

Cboe publishes delayed option quotes. A snapshot of the NVDA chain captured on 2026-09-23 (quotes reflecting the prior session's close) shows spot at 228.56 and, at the strike nearest spot, these ATM quotes (mid of bid and ask):

- October 30, 2026 expiry (37 days): 230 call mid 9.38, 230 put mid 9.45; straddle 18.83; ATM implied vol 31.8% (mean of call and put IV).
- November 20, 2026 expiry (58 days): 230 call mid 13.73, 230 put mid 13.18; straddle 26.91; ATM implied vol 36.5%.

NVIDIA has set its third-quarter fiscal 2027 call for November 17, 2026, so the November 20 expiry is the first expiry that contains the report and the October 30 expiry is the last that does not.

**Step 1, the straddle convention.** November 20: 26.91 / 228.56 = 0.1177, an implied move of **11.8%** over 58 days. October 30: 18.83 / 228.56 = 0.0824, **8.2%** over 37 days. The first number is not "the earnings move"; it is 58 days of NVDA plus one earnings night.

**Step 2, check the 0.8 rule.** A straddle at 0.8σ√T with σ = 0.365 and T = 58/365 = 0.1589 gives 0.8 × 0.365 × 0.3986 = 0.1164, or 11.6% of spot, against the quoted 11.8%. The rule holds to within rounding.

**Step 3, strip the baseline.** Convert to variance. Total variance to November 20: 0.365² × 0.1589 = 0.133225 × 0.1589 = 0.021170. Baseline variance over the same 58 days at the October 30 vol: 0.318² × 0.1589 = 0.101124 × 0.1589 = 0.016069. Event variance: 0.021170 − 0.016069 = 0.005101. One-standard-deviation event move: √0.005101 = **0.0714, about 7.1%**.

**Step 4, convert back to a straddle-style number.** 0.8 × 7.1% = **5.7%**. That is roughly what an ATM straddle expiring the Friday after the report would be expected to cost on the afternoon of November 17, if the baseline vol stayed where it is and nothing else changed. In practice the day-before weekly straddle also carries two or three days of ordinary vol and usually prices a little above this.

**Step 5, put it next to realised.** The last four NVIDIA reports, from the Yahoo Finance daily bars (496 rows, 2024-10-01 to 2026-09-23), close before to close after:

- November 19, 2025: 186.52 → 180.64, **−3.15%**
- February 25, 2026: 195.56 → 184.89, **−5.46%**
- May 20, 2026: 223.47 → 219.51, **−1.77%**
- August 26, 2026: 209.66 → 227.98, **+8.74%**

Mean absolute move: (3.15 + 5.46 + 1.77 + 8.74) / 4 = 19.12 / 4 = **4.78%**. Root-mean-square move, which is the right comparison to a one-sigma figure: √((3.15² + 5.46² + 1.77² + 8.74²) / 4) = √((9.92 + 29.81 + 3.13 + 76.39) / 4) = √(119.25 / 4) = √29.81 = **5.46%**.

Against the 7.1% one-sigma event move implied today, and against the representative 7.0% straddle-style implied move used in the chart below (a round figure in the range NVDA options have priced in recent quarters, not a dated quote), three of the four realised moves were smaller and one was larger. That is exactly the pattern the literature describes: on average the straddle buyer overpays, and occasionally the one large move pays for several small ones.

## Chart

![Representative 7.0% implied move (grey) beside the realised close-to-close absolute move (green) for NVDA's reports of Nov 19 2025, Feb 25 2026, May 20 2026 and Aug 26 2026. Realised moves from Yahoo Finance daily closes; the implied bars are a labelled representative figure, not dated quotes.](figures/nvda-implied-vs-realised-four-reports.svg)

## What the studies found

Dubinsky, Johannes, Kaeck and Seeger (2019) built estimators exactly like the variance subtraction above and applied them to a broad sample of U.S. earnings announcements. Their option-implied earnings-move estimates are strongly informative about the size of the subsequent move, and on average they exceed the realised move: there is a risk premium embedded in the event variance, meaning buyers of event variance pay more than it is worth on average and sellers collect it. They also show the premium is not constant across firms or time.

Chung and Louis (2017) looked at the same question from the straddle buyer's side and found something that appears to contradict it: returns on straddles bought shortly before earnings announcements are positive on average in their sample. The reconciliation is in the conditioning. Their positive returns are concentrated after periods of *low* recent volatility, when option traders appear to under-estimate the coming move, and they find over-estimation after high-volatility periods. Whether the implied move is too high or too low depends on where you are in the volatility cycle.

A 2023 study of weekly options in the Journal of Risk and Financial Management tests a practical version of that rule: straddle returns are materially higher when the stock's *historical* earnings moves are large relative to the *implied* move, and lower when the reverse holds. The trader's takeaway is not "sell earnings straddles" or "buy them"; it is that the ratio of realised-to-implied in the name's own history is the first thing to compute, and that on average the seller has had the edge before costs.

## What "moved less than implied" means to a seller

If you sold the ATM straddle at 5.7% of spot and the stock closed 4.8% away at expiry, you owe 4.8% and keep 0.9%. That is the gross edge. It is small relative to the tail: a 12% move costs the seller 6.3%, seven times the typical win. The seller's business, if it is a business, is collecting many 0.9%s and surviving the 6.3%s. Costs matter at this scale: a two-leg round trip in NVDA weeklies with a 0.05 to 0.10 bid-ask per leg is 0.10 to 0.20 of spot per straddle, up to a fifth of the gross edge in this example.

The buyer's version is the mirror. The buyer needs |move| > straddle cost, and needs it often enough that the winners pay for the losers. On the last four NVDA reports one of four cleared a 7% hurdle. That is not evidence of anything by itself; it is four observations. Lesson 11 tells you how many you need.

## Sources

- Dubinsky, A., Johannes, M., Kaeck, A., and Seeger, N. J. (2019). "Option Pricing of Earnings Announcement Risks." Review of Financial Studies 32(2), 646–687. https://doi.org/10.1093/rfs/hhy060
- Chung, S. G., and Louis, H. (2017). "Earnings announcements and option returns." Journal of Empirical Finance 40, 220–235. https://doi.org/10.1016/j.jempfin.2016.07.010
- "The Efficiency of Weekly Option Prices around Earnings Announcements." Journal of Risk and Financial Management 16(5), 270 (2023). https://doi.org/10.3390/jrfm16050270
- Cboe delayed option quotes (public feed), NVDA snapshot 2026-09-23: https://cdn.cboe.com/api/global/delayed_quotes/options/NVDA.json
