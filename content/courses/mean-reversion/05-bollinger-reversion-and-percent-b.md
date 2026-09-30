---
{
  "title": "Bollinger Reversion and %B, Tested Honestly",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "On 2025-04-03 SPY closed at 536.70 with a 20-day average of 562.64 and a 20-day standard deviation of 8.68. %B was:", "opts": ["−0.247", "+0.25", "0", "−2.0"], "correct": 0, "explain": "Lower band = 562.64 − 2 × 8.68 = 545.27; band width = 4 × 8.68 = 34.72; %B = (536.70 − 545.27) / 34.72 = −0.247. Below zero means the close was outside the lower band."},
    {"q": "On 2025-04-09 SPY rose 10.5% in one day to 548.62, yet the open Bollinger trade did not exit. Why?", "opts": ["Because the exit rule was never coded", "Because the bands had widened so much (20-day s.d. 23.01) that 548.62 was still only %B = +0.454, just under the 0.5 exit", "Because the trade had already been stopped out", "Because %B cannot exceed 0.5 in April"], "correct": 1, "explain": "The exit is defined relative to the bands, and the bands are defined by recent volatility. After a crash, the same price level maps to a lower %B. The trade ran to its ten-day limit and lost 1.94%."},
    {"q": "Shorting SPY when it closed above the upper band (%B > 1) and covering at the middle band, 2015 to 2026, produced:", "opts": ["+58.6%", "−13.7% with a 45.5% win rate", "+100%", "No trades"], "correct": 1, "explain": "The short side lost on SPY, QQQ (−27.9%) and IWM (−4.7%). Closing above the upper band in an uptrending index is not a reason to sell it, which is the momentum-horizon point from lesson 1."},
    {"q": "The same long rule earned +58.6% on SPY, +35.3% on QQQ and +2.9% on IWM. The most defensible conclusion is:", "opts": ["The rule works on large-caps only", "IWM's data is wrong", "QQQ should use 3 standard deviations", "One rule, three closely related ETFs, three very different results: the edge, if it exists, is small relative to sampling noise, and IWM's −29.8% drawdown shows what the same entry does when the reversion does not arrive"], "correct": 3, "explain": "The spread of outcomes across three highly correlated instruments is the best evidence you have of how uncertain the rule's expected return is."},
    {"q": "Exiting Bollinger longs at the upper band instead of the middle band raised SPY's total from +58.6% to +100.0% but:", "opts": ["Lowered the win rate to 40%", "Doubled the average holding period to 18 days, raised the worst trade to −22.25% and the drawdown to −22.2%, so the extra return came from holding through 2020 with no stop", "Reduced the trade count to zero", "Had no effect on risk"], "correct": 1, "explain": "The upper-band exit is a trend-following exit bolted onto a reversion entry. Its extra return is mostly one recovery, and its risk is a −22% single trade."}
  ],
  "task": "Compute the 20-day Bollinger Bands and %B for an ETF you follow for the last 30 sessions, and mark any close with %B below 0 or above 1."
}
---

Bollinger Bands are a moving average with a volatility envelope: a 20-day simple average plus and minus two 20-day standard deviations. John Bollinger's %B indicator locates the close inside that envelope on a scale where 0 is the lower band and 1 is the upper band. The reversion trade is obvious enough that everyone tries it: buy below the lower band, sell at the middle. This lesson tests exactly that on three index ETFs and reports what happened, including the two places it does not work.

## The construction

For each day, with n = 20 and k = 2:

middle = SMA₂₀(close)
σ = standard deviation of the last 20 closes (population form, dividing by 20, as Bollinger specifies)
upper = middle + 2σ; lower = middle − 2σ
%B = (close − lower) / (upper − lower) = (close − lower) / (4σ)

%B below 0 means the close is outside the lower band; above 1, outside the upper. Bandwidth, (upper − lower) / middle, measures how wide the envelope is and matters for the exit, as the worked example shows.

## The rule

Long only, on SPY, QQQ and IWM separately:

1. Buy at the close when %B < 0.
2. Sell at the first close with %B > 0.5 (back above the middle band), or after ten trading days if that has not happened.
3. Cost 0.01% per side.

The ten-day limit is there because a %B exit can wait indefinitely if the bands keep moving away from the price. Variants below drop the limit, add a 200-day filter, and test the short side.

## Worked example

Data: Yahoo Finance daily closes (`interval=1d`), pulled 2026-09-24; tests run from 2015-10-19 so that the 200-day filter variant has the same start as the others.

**April 2025 on SPY.** On 2025-04-03 SPY closed at 536.70 after the tariff announcement. The 20 closes ending that day average 562.64, with a population standard deviation of 8.68:

lower = 562.64 − 2 × 8.68 = **545.27**; upper = 562.64 + 17.36 = 580.00
%B = (536.70 − 545.27) / (4 × 8.68) = −8.57 / 34.72 = **−0.247**

Below zero, so buy at 536.70. What followed:

- 04-04: close 505.28. The 20-day average has dropped to 559.11 and σ has jumped to 14.78; lower band 529.54; %B = (505.28 − 529.54) / 59.12 = **−0.410**. Deeper below the band.
- 04-07: close 504.38; σ = 18.98; %B = −0.184.
- 04-08: close 496.48; σ = 23.03; %B = −0.117.
- 04-09: close **548.62**, up 10.5% on the day, the largest one-day gain since 2008. Middle 552.81, σ 23.01, lower 506.78, upper 598.84. %B = (548.62 − 506.78) / 92.06 = **+0.454**.

Not above 0.5. The bands had widened so far in four sessions (σ from 8.68 to 23.01) that a close 12 points above the entry price still sat below the middle band. The trade continued:

- 04-10: 524.58, %B +0.218. 04-11: 533.94, +0.332. 04-14: 539.12, +0.400. 04-15: 537.61, +0.396. 04-16: 525.66, +0.292.
- 04-17: close 526.41, %B +0.319. Ten trading days since entry. Exit at 526.41.

Return: 526.41 / 536.70 − 1 = −1.92%, minus 0.02% = **−1.94%**. The market bottomed the day after entry and rallied 10.5% inside the holding period, and the trade lost, because the exit was defined in units that the crash had inflated. Had the rule held two more sessions, 04-23 printed %B = +0.486 and 04-24 printed +0.640 at 546.69, a +1.84% exit. That is not an argument for a twelve-day limit; it is an illustration that the outcome of a band-based exit depends on the volatility regime at least as much as on the price.

**February 2025.** The other 2025 SPY loser: entered 02-25 at 594.24, never reached the middle band, exited on the ten-day limit 03-11 at 555.92: **−6.47%**. Two consecutive trades in the spring cost 8.4% and the year's two winners (10-10 to 10-15, +1.84%; 11-18 to 11-25, +2.24%) recovered half of it.

**All trades.** SPY, 2015-10-19 to 2026-09-23: 57 trades, 70.2% winners, average +0.854%, average winner +2.43%, average loser −2.85%, total **+58.6%**, worst trade −7.77%, maximum drawdown −13.9%, average hold 6.9 days, in the market 14% of days. QQQ: 49 trades, 61.2%, +0.693%, total +35.3%, drawdown −15.5%. IWM: 60 trades, 60.0%, +0.160%, total **+2.9%**, worst trade −14.02%, drawdown **−29.8%**.

## Table

| ETF, variant (2015-10-19 to 2026-09-23) | Trades | Win | Avg trade | Total | Max DD | Worst trade |
|---|---|---|---|---|---|---|
| SPY long %B<0, exit %B>0.5 or 10 d | 57 | 70.2% | +0.854% | +58.6% | −13.9% | −7.77% |
| SPY same, plus close > 200-day SMA | 39 | 74.4% | +0.733% | +31.0% | −14.5% | −7.77% |
| SPY long, exit %B>1.0 or 20 d | 46 | 76.1% | +1.658% | +100.0% | −22.2% | −22.25% |
| SPY short %B>1, cover %B<0.5 or 10 d | 66 | 45.5% | −0.207% | −13.7% | −20.5% | −4.87% |
| QQQ long, base | 49 | 61.2% | +0.693% | +35.3% | −15.5% | −7.73% |
| QQQ long, 200-day filter | 32 | 59.4% | −0.070% | −4.2% | −13.8% | −7.73% |
| QQQ short, base | 66 | 45.5% | −0.465% | −27.9% | −27.5% | −5.12% |
| IWM long, base | 60 | 60.0% | +0.160% | +2.9% | −29.8% | −14.02% |
| IWM long, 200-day filter | 33 | 69.7% | +1.321% | +51.9% | −9.3% | −6.85% |
| IWM short, base | 68 | 50.0% | −0.020% | −4.7% | −21.5% | −7.66% |
| Buy and hold: SPY +277.5%, QQQ +581.6%, IWM +143.8% | | | | | | |

Source: Yahoo Finance daily closes, computed by the course. Totals are compounded trade returns after 0.01% per side.

## What the table says

Three findings, none of them flattering to the folklore.

The long side is positive on all three ETFs but the size varies from +58.6% to +2.9% on instruments whose daily returns are 80% to 95% correlated. That range is your uncertainty. If you had tested only SPY you would believe in a +0.85% per-trade edge; if only IWM, in +0.16% with a −30% drawdown. Neither number is "the" edge. The rule buys a two-sigma dip; whether the dip is the start of a crash is the thing the rule cannot see, and IWM's trades of 2020-02-25 (−14.02%), 2020-03-11 (−12.66%) and 2018-12-07 (−10.89%) show what that costs.

The short side loses everywhere. Closing above the upper band in an index that spent most of eleven years rising is not overbought; it is trending. The best of the three shorts, IWM, lost 4.7%. The trend filter helps the shorts less than it helps the longs because the filter's own logic (only short below the 200-day) puts you short in bear markets, where upper-band closes are the sharpest rallies.

The 200-day filter is not a free improvement. It roughly halves SPY's total, turns QQQ's small profit into a small loss, and rescues IWM (from +2.9% to +51.9%, drawdown from −29.8% to −9.3%). Its value is in the tail, and the tail shows up in the instrument that has the most of it. Lesson 4 found the same thing with RSI(2): filters trade average return for a shorter list of ways to be badly hurt.

The "exit at the upper band" row is a warning. Doubling SPY's total to +100% looks like an improvement until you read across: eighteen-day average hold, a single trade at −22.25% (entered 2020-02-25, held through the March collapse with no stop) and a −22.2% drawdown. You have converted a reversion trade into an unprotected trend trade. Lesson 10 is about why every reversion rule needs a stop that is not the reversion target.

## Sources

- Bollinger, J. (2001). *Bollinger on Bollinger Bands*. McGraw-Hill, New York. ISBN 0-07-137368-3. https://www.worldcat.org/isbn/0071373683
- Lento, C., Gradojevic, N. and Wright, C. S. (2007). Investment information content in Bollinger Bands? *Applied Financial Economics Letters*, 3(4), 263–267. https://doi.org/10.1080/17446540701206576
- Lo, A. W. and MacKinlay, A. C. (1990). When are contrarian profits due to stock market overreaction? *Review of Financial Studies*, 3(2), 175–205. https://doi.org/10.1093/rfs/3.2.175
- Yahoo Finance historical data: https://finance.yahoo.com/quote/IWM/history/
