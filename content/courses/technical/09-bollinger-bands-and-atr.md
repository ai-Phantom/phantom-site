---
{
  "title": "Bollinger Bands and ATR: Volatility, Not Direction",
  "duration": "14 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Standard Bollinger Bands are drawn at:", "opts": ["The 20-day SMA plus and minus 2 population standard deviations of the last 20 closes", "The 50-day SMA plus and minus 5%", "The highest high and lowest low of 20 days", "The 200-day SMA plus and minus one ATR"], "correct": 0, "explain": "Bollinger's specification is a 20-period SMA and a 2-standard-deviation envelope, with the population (divide-by-n) standard deviation."},
    {"q": "On 13 October 2022 the 20 SPY closes summed to 7,393.90 and the sum of squared deviations from their mean was 1,786.61. The population standard deviation was:", "opts": ["9.45", "9.70", "89.33", "369.70"], "correct": 0, "explain": "Variance = 1,786.61 / 20 = 89.33; standard deviation = √89.33 = 9.45. (Dividing by 19 gives 9.70, the sample version, which is not Bollinger's specification.)"},
    {"q": "True range for a bar is:", "opts": ["High minus low only", "The largest of: high − low, |high − prior close|, |low − prior close|", "Close minus open", "The 14-day average range"], "correct": 1, "explain": "True range includes any gap from the prior close, so a bar that gaps has a true range larger than its own high-to-low range."},
    {"q": "Over ten years, what share of SPY daily closes fell outside the 2-standard-deviation bands?", "opts": ["About 4.6%, as a normal distribution predicts", "About 10.9% (6.05% above, 4.86% below)", "Zero", "About 50%"], "correct": 1, "explain": "Closes are outside the bands more than twice as often as a normal distribution would suggest, because returns have fat tails and the bands are computed from the same 20 closes they enclose."},
    {"q": "Which use of ATR is supported by what it measures?", "opts": ["Predicting the direction of the next move", "Sizing a stop so that it sits outside normal daily noise, and sizing a position so that a stop-out risks a fixed fraction of capital", "Identifying oversold conditions", "Replacing volume"], "correct": 1, "explain": "ATR is a pure magnitude measure. Its defensible uses are all about scaling: stops, targets and position sizes in units of typical movement."}
  ],
  "task": "Compute 20-day Bollinger Bands and 14-day ATR on your ticker, then express the distance from your usual stop placement as a multiple of ATR for the last five trades you took or would have taken."
}
---

Bollinger Bands and Average True Range are both volatility measures. Neither contains any information about direction, and most of the ways they are misused come from treating them as if they did. This lesson gives you the arithmetic for each, a check of the most common band rule on ten years of SPY, and the uses that follow from what the tools actually measure.

## Bollinger Bands

John Bollinger's construction, as he specifies it: a 20-period simple moving average of the close (the middle band), plus an upper band two standard deviations above it and a lower band two standard deviations below. The standard deviation is the **population** version (divide the sum of squared deviations by n, not n − 1), computed over the same 20 closes as the average.

Two derived numbers are more useful than the bands themselves:

- **Bandwidth** = (Upper − Lower) / Middle. A scale-free measure of how volatile the last 20 days have been. Bollinger's "squeeze" is a bandwidth at a multi-month low.
- **%B** = (Close − Lower) / (Upper − Lower). Where the close sits relative to the bands: 0 at the lower band, 1 at the upper, 0.5 at the middle. Values below 0 or above 1 mean the close is outside the bands.

The mistake to avoid is the one Bollinger himself warns against: a close above the upper band is not a sell signal and a close below the lower band is not a buy signal. Bands measure the last 20 days' dispersion. A strong trend produces a series of closes at or beyond the band, because the band is a lagging function of the closes that produced it.

## Average True Range

Wilder's true range for a bar is the largest of three distances: high − low, |high − prior close|, and |low − prior close|. The second and third terms capture gaps: a bar that opens far from the prior close has moved further than its own high-to-low range shows. ATR(14) is the average of the last 14 true ranges. Wilder used his own smoothing (k = 1/14); many platforms use a simple 14-day average, and the two differ by a few percent. Know which one your platform shows.

ATR is expressed in price units. Divide by the close to get a percentage, which is comparable across tickers and across time.

## What the evidence says

Lento, Gradojevic and Wright (2007) tested Bollinger Band trading rules on several equity indexes and found that the conventional contrarian rule (buy at the lower band, sell at the upper) did not generate profits after costs, and that a trend-following rule (buy on a break above the upper band) did better on some series, which is the opposite of how most retail traders use the bands. Leung and Chong (2003) compared Bollinger Bands with fixed-percentage moving-average envelopes and found no clear advantage to the statistical construction. Neither tool has a strong academic record as a directional signal; both have a clear logical basis as a measure of how much price has been moving.

## Worked example

SPY, 13 October 2022, from Yahoo Finance historical daily data. The 20 closes ending that day (23 September to 13 October): 385.56, 388.55, 384.09, 377.39, 374.22, 367.95, 364.31, 363.38, 370.53, 362.79, 357.18, 366.61, 377.97, 377.09, 373.20, 362.79, 360.02, 357.74, 356.56, 365.97.

**Middle band.** Sum = 7,393.90. SMA(20) = 7,393.90 / 20 = **369.70**.

**Standard deviation.** Sum of squared deviations from 369.695 = 1,786.61. Variance = 1,786.61 / 20 = 89.33. Standard deviation = √89.33 = **9.45**. (The sample version, dividing by 19, gives 9.70; that is not the Bollinger specification, and platforms that use it draw bands about 2.6% wider.)

**Bands.** Upper = 369.70 + 2 × 9.45 = **388.60**. Lower = 369.70 − 2 × 9.45 = **350.79**. Bandwidth = (388.60 − 350.79) / 369.70 = **10.2%**. %B for the close of 365.97 = (365.97 − 350.79) / (388.60 − 350.79) = 15.18 / 37.81 = **0.40**.

The day's low of 348.11 was below the lower band (350.79) by 2.68 points; the close was back inside at %B 0.40. That is the shape of a failed breakdown expressed in band terms.

**True range and ATR.** Prior close (12 October) 356.56; high 367.51; low 348.11. The three candidates: high − low = 19.40; |high − prior close| = 10.95; |low − prior close| = 8.45. True range = **19.40**. The 14 true ranges ending 13 October were 7.18, 9.53, 9.70, 10.83, 8.87, 11.37, 11.43, 8.51, 6.04, 12.35, 6.54, 7.32, 3.52 and 19.40; their simple average is 132.59 / 14 = **9.47**. Wilder-smoothed ATR(14) on the same day was 8.96. As a percentage of the close: 9.47 / 365.97 = **2.6%**. A stop placed 1 ATR below a 365.97 entry would sit near 356.50; 2 ATR, near 347.00.

For scale: on 19 February 2020, the pre-crash high, bandwidth was 6.0% and ATR(14) was 0.86% of the close. On 16 March 2020 bandwidth was 36.6% and ATR was 5.7% of the close. On 23 September 2026, the last day in the sample, bandwidth was 2.8% and ATR was 0.88%. The same 1-ATR stop is 4.7 times further away in dollars (13.75 against 2.90) in March 2020 than in February 2020, and 6.7 times further as a share of price. That is what ATR is for.

**The contrarian band rule, checked.** Over the full ten years (2,512 days), closes were above the upper band on 6.05% of days and below the lower band on 4.86%. A normal distribution predicts 2.3% each. Forward 5-day return after a close below the lower band: +0.96% (122 cases, 71.3% positive) against a base rate of +0.28%. After a close above the upper band: +0.14% (152 cases, 61.2% positive). The lower-band figure looks like the RSI(2) result from Lesson 7, and for the same reason: it identifies sharp short-term declines on an index with mild short-term reversal. The upper-band figure is below the base rate but still positive, so "sell at the upper band" would have been a way to exit a rising market early. Bandwidth at a six-month low (45 days) was followed by an average absolute 20-day move of 3.88% against a baseline of 3.44%: the squeeze does precede slightly larger moves, in either direction.

## Table

| Measure | Formula | 19 Feb 2020 | 16 Mar 2020 | 13 Oct 2022 | 23 Sep 2026 |
|---|---|---|---|---|---|
| Close | | 338.34 | 239.85 | 365.97 | 767.81 |
| SMA(20) | Σ close / 20 | 331.38 | 300.11 | 369.70 | 765.28 |
| Std dev (pop.) | √(Σ(c − mean)² / 20) | 4.98 | 27.47 | 9.45 | 5.41 |
| Upper band | SMA + 2σ | 341.35 | 355.04 | 388.60 | 776.10 |
| Lower band | SMA − 2σ | 321.41 | 245.18 | 350.79 | 754.46 |
| Bandwidth | (U − L) / SMA | 6.0% | 36.6% | 10.2% | 2.8% |
| ATR(14), Wilder | | 2.90 | 13.75 | 8.96 | 6.76 |
| ATR as % of close | ATR / close | 0.86% | 5.73% | 2.45% | 0.88% |

## Using volatility measures

**Stops in ATR units.** A stop closer than about 1 ATR is inside normal daily noise and will be hit by randomness. Decide the multiple, then place the stop, then size the position so that the stop-out loses a fixed fraction of your capital. That ordering is the single most useful thing in this course for account survival.

**Targets in ATR units.** A target of 3 ATR in 3 days on an instrument that averages 1 ATR of movement per day is not a plan.

**Bandwidth as a regime label.** Low bandwidth says the recent past was quiet; it does not say which way the next move will be. Use it to widen your expectations, not to pick a direction.

**Never trade the bands alone.** The evidence is against the contrarian rule and the trend rule is just a breakout rule with extra steps. Bands describe dispersion; use them for that.

## Sources

- Bollinger, J. "Bollinger Bands: Introduction and rules." https://www.bollingerbands.com/bollinger-bands
- Lento, C., Gradojevic, N., & Wright, C. S. (2007). "Investment information content in Bollinger Bands?" *Applied Financial Economics Letters*, 3(4). https://doi.org/10.1080/17446540701206576
- Leung, J. M.-J., & Chong, T. T.-L. (2003). "An empirical comparison of moving average envelopes and Bollinger Bands." *Applied Economics Letters*, 10(6). https://doi.org/10.1080/1350485032000056959
- Yahoo Finance. SPY historical prices. https://finance.yahoo.com/quote/SPY/history/
