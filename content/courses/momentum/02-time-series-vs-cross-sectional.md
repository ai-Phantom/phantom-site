---
{
  "title": "Time-Series vs Cross-Sectional Momentum",
  "duration": "16 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "Time-series momentum asks:", "opts": ["Which stocks have done best relative to each other", "Whether an asset's own past return predicts its own future return", "Which sector has the highest dividend", "Whether volume is rising"], "correct": 1, "explain": "Time-series momentum is a signal on one asset against itself, typically the sign of its trailing 12-month return. Cross-sectional momentum compares assets to each other."},
    {"q": "On SPY monthly data from 1994 to 2026, the average next-month return when the trailing 12-month return was positive was about +1.14%, versus about +0.10% when it was negative. The standard deviation of next-month returns in the negative state was:", "opts": ["Lower, about 2%", "About the same", "Higher, about 6.2% versus 3.7%", "Zero"], "correct": 2, "explain": "The negative-trend state had both a lower mean and much higher volatility, which is the pattern that makes a trend filter useful as risk control even when its return edge is modest."},
    {"q": "The SPY long-or-cash rule in the worked example ended with about the same wealth as buy-and-hold (30.4x versus 28.4x) but a maximum drawdown of −19.5% versus −50.8%. This means the rule:", "opts": ["Roughly doubled returns", "Delivered a similar return with far less depth of loss, with the caveat that cash was assumed to earn nothing and no costs were charged", "Lost money", "Only worked in 2008"], "correct": 1, "explain": "The rule's value here is in drawdown, not in return. The assumptions flatter and penalise it in different directions: zero interest on cash hurts it; zero trading costs help it slightly."},
    {"q": "In the same rule, the 12-month signal was still negative at the end of June 2009 (−26.2%), so the rule missed July 2009's +7.5%. This illustrates that:", "opts": ["The rule is broken", "A slow signal exits late and re-enters late; that is the price of not reacting to every wobble", "SPY data is unreliable", "Cash is always better in July"], "correct": 1, "explain": "A 12-month lookback smooths out noise at the cost of lag at turning points. The worked example shows both the avoided January 2009 (−8.2%) and the missed April 2020 (+12.7%)."},
    {"q": "The nine-sector-ETF long/short momentum book in the lesson ended 2000 to 2026 almost flat before costs with a −45% maximum drawdown. The lesson draws which conclusion?", "opts": ["Cross-sectional momentum is a myth", "A cross-section of nine highly correlated sectors is too small and too similar for the ranking to carry much information; the academic result uses thousands of stocks", "Sector ETFs are illegal to short", "The 2009 crash explains the whole result"], "correct": 1, "explain": "With nine assets that share most of their variance, the ranking spread is small. The result is reported as it came out rather than tuned, and its main lesson is about universe size."}
  ],
  "task": "Download SPY monthly closes from Yahoo Finance, compute the trailing 12-month return at the end of each of the last 24 months, and mark which months the signal was negative."
}
---

Momentum comes in two forms that are often confused. Cross-sectional momentum compares assets to each other: rank the universe, buy the top, avoid or short the bottom. Time-series momentum compares an asset to its own past: is this thing above where it was a year ago, yes or no. They are measured differently, they fail differently, and a swing trader uses both, one for picking and one for permission.

## Cross-sectional momentum

This is the Jegadeesh-Titman effect from lesson 1. The signal is relative: a stock that fell 5% ranks in the top decile if everything else fell 20%. The strategy is market-neutral by construction, long winners and short losers, so its return is the spread between the two groups and it does not depend on the market going up. Its weakness is the rotation crash described in lesson 1 and worked in lesson 10.

For a swing trader, cross-sectional momentum is the ranking tool. It answers "which names" and it is the subject of lesson 4.

## Time-series momentum

Moskowitz, Ooi and Pedersen (2012) studied 58 futures and forward contracts across equities, bonds, currencies and commodities from 1985 to 2009 and found that each instrument's own past 12-month excess return predicted its next-month return, with positive results in nearly every contract. The strategy is simple: go long anything that is up over the past year, short anything that is down, size by volatility. Unlike cross-sectional momentum, it is not market-neutral; when everything trends up it is long everything. And its worst periods are different: it suffers in sharp reversals, but it does not suffer the specific long-defensives, short-cyclicals crash of 2009 because it does not hold that structure.

For a swing trader, time-series momentum is the permission tool. It answers "should I be running long swing setups at all", and the answer changes slowly.

## Worked example

Data: SPY monthly closes, adjusted for dividends, built from daily bars pulled from Yahoo Finance's chart API on 2026-09-24 (`https://query1.finance.yahoo.com/v8/finance/chart/SPY?period1=0&period2=<now>&interval=1d`). The first usable signal is at the end of January 1994 and the last evaluated month is August 2026, a sample of 392 months. Adjusted closes are used because a total-return comparison is what matters over three decades of dividends.

The signal at each month end is the trailing 12-month return: this month's adjusted close divided by the adjusted close twelve months earlier, minus one. The rule is: if the signal is positive, hold SPY for the next month; if it is zero or negative, hold cash, assumed to earn nothing.

Four dated instances show how it behaves:

- End of December 2008: adjusted close 65.66 against 103.88 a year earlier, signal = 65.66 / 103.88 − 1 = **−36.8%**. Out. January 2009 returned **−8.21%**, avoided.
- End of June 2009: 67.76 against 91.84, signal = **−26.2%**. Still out. July 2009 returned **+7.46%**, missed. The rule did not turn positive until well after the March low; a 12-month lookback is slow by design.
- End of March 2020: 235.74 against 253.19, signal = **−6.9%**. Out. April 2020 returned **+12.70%**, missed. This is the classic time-series-momentum failure: a fast crash and a faster rebound inside the lookback.
- End of May 2022: 388.78 against 390.33, signal = **−0.4%**. Out by a whisker. June 2022 returned **−8.25%**, avoided.

Over the full 392 months:

| State at month end | Months | Mean next-month return | Std. dev. | Months positive |
|---|---|---|---|---|
| 12-month return > 0 | 322 | +1.14% | 3.72% | 68.6% |
| 12-month return ≤ 0 | 70 | +0.10% | 6.23% | 50.0% |
| All months | 392 | +0.95% | — | — |

The difference in mean is 1.04 points per month in favour of the positive state, and the difference in volatility is larger still: the negative state is 1.7 times as volatile. That second fact is why the rule matters even if you doubt the first. A swing trader who runs the same setups regardless of state is taking the same risk per trade in a tape that moves 6% a month as in one that moves 4%.

Compounding the rule from January 1994 to August 2026: buy-and-hold multiplied the starting equity by **28.4**; long-or-cash multiplied it by **30.4**. The difference in wealth is small and would shrink if cash earned interest for the rule and costs were charged for its 30-odd switches; call it a wash. The difference in the worst peak-to-trough drawdown is not a wash: **−50.8%** for buy-and-hold against **−19.5%** for the rule. The time-series filter did not make you richer here. It made the same wealth reachable without living through a halving of the account.

Now the cross-sectional version at small scale. Take the nine original SPDR sector ETFs (XLB, XLE, XLF, XLI, XLK, XLP, XLU, XLV, XLY), monthly adjusted closes from Yahoo Finance from 1999. Each month, rank on the 12-1 return, go long the top three and short the bottom three, equal weight, rebalance monthly. From February 2000 to September 2026, 321 months, the long-short book finished at **1.045 times** its starting value, before costs, with a maximum drawdown of **−45%**. That is not a typo: over 26 years the crude sector version of the academic strategy earned essentially nothing. Lesson 10 shows where the drawdown happened. The reason it is reported here is that nine sector funds sharing most of their variance are a poor cross-section; the ranking spread among them is small, and the 2009 rotation alone removed a third of the book. The academic result is built on thousands of stocks with real dispersion. Scale of the cross-section is not a detail.

## How to use both

Run the time-series check on the index once a month. It is not a trading signal; it is a dial on how aggressively you run the cross-sectional playbook. A reasonable mapping for a long-only swing trader:

- Index above its level of twelve months ago and above its 200-day average: full size, normal setups.
- One of the two true: half size, breakouts only.
- Neither: no new longs, or paper-trade the setups to keep your eye in.

This is not an optimised rule. It encodes the two things the data support: the positive state has better and calmer returns, and the negative state is where both kinds of momentum have their worst months.

Rank your universe cross-sectionally every week regardless of state. The ranking is information even in a bear tape; it is just not permission.

## Sources

- Moskowitz, T. J., Ooi, Y. H. and Pedersen, L. H. (2012). Time series momentum. *Journal of Financial Economics*, 104(2), 228–250. https://doi.org/10.1016/j.jfineco.2011.11.003
- Asness, C. S., Moskowitz, T. J. and Pedersen, L. H. (2013). Value and momentum everywhere. *Journal of Finance*, 68(3), 929–985. https://doi.org/10.1111/jofi.12021
- Jegadeesh, N. and Titman, S. (1993). Returns to buying winners and selling losers. *Journal of Finance*, 48(1), 65–91. https://doi.org/10.1111/j.1540-6261.1993.tb04702.x
- Yahoo Finance historical data, SPY: https://finance.yahoo.com/quote/SPY/history/
