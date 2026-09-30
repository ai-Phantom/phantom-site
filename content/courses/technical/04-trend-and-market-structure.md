---
{
  "title": "Trend, Higher Highs and Lower Lows, and Market Structure",
  "duration": "14 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Using the definition in this lesson, an uptrend exists when:", "opts": ["Price is above its 200-day moving average", "The most recent swing high is above the prior swing high and the most recent swing low is above the prior swing low", "The stock has gone up for three days in a row", "Analysts are bullish"], "correct": 1, "explain": "Market structure defines trend by the sequence of swing points. Moving averages are a different (and lagging) definition covered in Lesson 6."},
    {"q": "In the worked example, SPY's first higher low of the 2022–23 turn was:", "opts": ["17 Jun 2022 at 362.17", "13 Oct 2022 at 348.11", "22 Dec 2022 at 374.77", "24 Jan 2022 at 420.76"], "correct": 2, "explain": "The 22 December low of 374.77 was the first swing low above the prior swing low (348.11 on 13 October)."},
    {"q": "The 10-bar swing-point algorithm has a built-in delay of:", "opts": ["Zero bars", "10 bars, because a swing cannot be confirmed until 10 bars have printed after it", "1 bar", "200 bars"], "correct": 1, "explain": "A pivot is defined by the bars on both sides, so it is only known 10 bars after the fact. Every structural definition of trend lags by construction."},
    {"q": "Moskowitz, Ooi and Pedersen (2012) found that time-series momentum (past 12-month return predicting the next month) held across:", "opts": ["Only US stocks", "58 futures markets across equities, bonds, currencies and commodities", "Only cryptocurrencies", "No markets at all"], "correct": 1, "explain": "Time-series momentum is one of the most broadly replicated findings supporting trend persistence, though at monthly rather than daily horizons."},
    {"q": "From the 4 January 2022 high (479.98) to the 13 October 2022 low (348.11), SPY fell about:", "opts": ["12%", "19%", "27%", "35%"], "correct": 2, "explain": "(348.11 − 479.98) / 479.98 = −27.5%."}
  ],
  "task": "Apply the 10-bar swing algorithm to one year of daily data on a ticker you follow, list every swing high and low with its date and price, and label the sequence as HH/HL or LH/LL."
}
---

Trend is the most-used and least-defined word in trading. This lesson gives you one precise definition based on swing points, an algorithm for finding them, and the evidence on whether trends persist at all. You will also see the built-in delay of every structural definition, which is the price you pay for objectivity.

## Defining trend by structure

Price moves in swings: it advances, pulls back, advances again. The turning points are swing highs and swing lows. Market structure is simply the sequence of those points.

- **Uptrend**: each swing high is above the previous swing high (a higher high, HH) and each swing low is above the previous swing low (a higher low, HL).
- **Downtrend**: lower highs (LH) and lower lows (LL).
- **Range**: swings overlap without a consistent sequence.

A trend changes when the sequence breaks. In a downtrend, the first higher low is a warning; the first higher high is the change. In an uptrend, the first lower high is the warning and the first lower low is the change. This gives you an objective, if lagging, definition that anyone can reproduce.

## An algorithm for swing points

A swing high is a bar whose high is the highest of the N bars before it and the N bars after it. A swing low is the mirror. N controls how large a swing has to be to count. N = 10 on daily bars captures moves that last a few weeks; N = 3 captures every wiggle; N = 20 captures only multi-month turns.

Two consequences of this definition:

1. **It lags by N bars.** You cannot know that 13 October 2022 was a swing low until 27 October, because the algorithm needs ten bars after it to confirm nothing lower printed. Any structural signal you act on is at least N bars old.
2. **It is parameter-dependent.** With N = 5 you will see more swings and more "trend changes"; with N = 20 you will see fewer. Neither is right. Choose N to match the holding period you intend and keep it fixed.

You can implement this in a spreadsheet: for each row, check whether the high equals the maximum of the highs from N rows above to N rows below.

## Does trend persist?

Two kinds of evidence say yes, with important caveats.

**Cross-sectional momentum.** Jegadeesh and Titman (1993) sorted US stocks by their prior 3 to 12 month returns and found that past winners outperformed past losers by roughly 1% per month over the following 3 to 12 months. This result has been replicated across decades and countries and is a core anomaly in asset pricing.

**Time-series momentum.** Moskowitz, Ooi and Pedersen (2012) showed that a single asset's own past 12-month return predicts its next-month return across 58 futures contracts in equities, bonds, currencies and commodities.

The caveats: these effects operate at horizons of months, not days. At daily horizons, as you saw in Lesson 1, SPY shows slight reversal, not persistence. Momentum strategies also suffer severe drawdowns when trends reverse abruptly (the 2009 rebound is the standard example). And the effects are measured across portfolios of many assets; on a single ticker, the noise around the tendency is large.

So structural trend-following on one stock is not "proven". What the literature supports is that persistence is real at intermediate horizons, and that a rule which aligns with it has a base rate on its side. That is worth something, and it is less than most trend traders assume.

## Worked example

SPY, November 2021 to February 2023, swing points found with N = 10 on daily bars. Source: Yahoo Finance historical daily data, unadjusted highs and lows.

Swing highs (H) and swing lows (L), in order:

1. H 22 Nov 2021: 473.54
2. L 3 Dec 2021: 448.92
3. L 20 Dec 2021: 451.14 (higher low)
4. H 4 Jan 2022: **479.98** (higher high; the bull-market top)
5. L 24 Jan 2022: 420.76 (lower low than 451.14: **first LL**)
6. L 24 Feb 2022: 410.64 (LL)
7. H 29 Mar 2022: 462.07 (lower high than 479.98: **first LH**, confirming the downtrend)
8. L 20 May 2022: 380.54 (LL)
9. H 2 Jun 2022: 417.44 (LH)
10. L 17 Jun 2022: 362.17 (LL)
11. H 28 Jun 2022: 393.16 (LH)
12. L 14 Jul 2022: 371.04 (**higher low**: a warning, not a change)
13. H 16 Aug 2022: 431.73 (**higher high** than 393.16, but still below 462.07)
14. L 13 Oct 2022: **348.11** (LL; the bear-market low)
15. H 13 Dec 2022: 410.49 (LH relative to 431.73)
16. L 22 Dec 2022: 374.77 (**higher low** than 348.11)
17. H 2 Feb 2023: 418.31 (**higher high** than 410.49: structure turns up)

Some arithmetic on the sequence:

- Peak to trough: (348.11 − 479.98) / 479.98 = **−27.5%**.
- Each leg down, high to next low: 479.98 → 420.76 is −12.3%; 462.07 → 380.54 is −17.6%; 417.44 → 362.17 is −13.2%; 431.73 → 348.11 is −19.4%.
- Each bounce, low to next high: 410.64 → 462.07 is +12.5%; 380.54 → 417.44 is +9.7%; 362.17 → 431.73 is +19.2%; 348.11 → 410.49 is +17.9%.
- The July–August sequence (HL at 371.04, HH at 431.73) looked like a trend change at the time. It was followed by the largest leg down of the year. The higher high at 431.73 was still below the March high of 462.07, which under the strict definition means the larger downtrend structure (LH from 479.98 to 462.07) was intact.
- The confirmed turn came at the 2 February 2023 high of 418.31: higher high above 410.49, following a higher low at 374.77 above 348.11. The algorithm confirmed that high on 16 February 2023 (the tenth bar after it), by which time SPY closed at 408.28. The confirmation arrived (408.28 − 348.11) / 348.11 = **17.3%** above the October low.

That last number is the honest cost of structural trend definition. A trader waiting for confirmed HH and HL missed the first 17% of the move. In exchange, they avoided buying the failed turn in August 2022, which under the same rules never confirmed as a trend change because 431.73 stayed below 462.07.

## Chart

Described chart: a daily line of SPY closes from 1 November 2021 to 28 February 2023, with the seventeen swing points above marked as dots and labelled H1 to H8 and L1 to L9. Connect the swing highs with one line and the swing lows with another. From January to October 2022 both lines slope down (LH and LL). Between 14 July and 16 August the low line ticks up and the high line ticks up, but the high line's new point (431.73) sits visibly below its March point (462.07). From 22 December 2022 to 2 February 2023 both lines slope up for the first time since 2021. Shade the region between the two lines to show the swing envelope narrowing from about 60 points in the spring to about 35 points in the winter.

## Using structure

Structure gives you three things a moving average does not: an exact price that defines the trend (the last swing low in an uptrend), an exact price that invalidates it (a close below that low), and a scale for what counts as a pullback (the size of the previous swing). Use the last swing as the location for your stop; use the average swing size to judge whether a target is realistic.

Do not use structure to predict. Use it to classify. When you know what the sequence is, you know which of your rules apply.

## Sources

- Jegadeesh, N., & Titman, S. (1993). "Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency." *Journal of Finance*, 48(1). https://doi.org/10.1111/j.1540-6261.1993.tb04702.x
- Moskowitz, T. J., Ooi, Y. H., & Pedersen, L. H. (2012). "Time series momentum." *Journal of Financial Economics*, 104(2). https://doi.org/10.1016/j.jfineco.2011.11.003
- Lo, A. W., Mamaysky, H., & Wang, J. (2000). "Foundations of Technical Analysis." *Journal of Finance*, 55(4). https://www.nber.org/papers/w7613
- Yahoo Finance. SPY historical prices. https://finance.yahoo.com/quote/SPY/history/
