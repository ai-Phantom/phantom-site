---
{
  "title": "Moving Averages: SMA, EMA, 20/50/200, and Crossovers",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A 50-day simple moving average on a given day is:", "opts": ["The average of the last 50 closes, including today's", "The average of the next 50 closes", "The median of the last 50 closes", "Today's close weighted by 50"], "correct": 0, "explain": "SMA(50) = sum of the most recent 50 closes divided by 50. On 1 July 2025 the SPY sum was 29,154.89, giving 583.10."},
    {"q": "The smoothing constant for a 20-day EMA is:", "opts": ["1/20 = 0.05", "2/(20+1) = 0.0952", "20/21", "0.5"], "correct": 1, "explain": "EMA uses k = 2/(n+1). For n = 20 that is 0.0952, so each new close gets about 9.5% weight and the prior EMA gets 90.5%."},
    {"q": "Over ten years of SPY, how many 50/200 crossovers ('golden' and 'death' crosses) occurred?", "opts": ["2", "9", "41", "110"], "correct": 1, "explain": "Nine crosses in ten years: five golden, four death. The 20/50 pair crossed 41 times in the same period."},
    {"q": "Of the four death crosses in the sample, how many were followed by a gain in SPY before the next golden cross?", "opts": ["0", "1", "3", "4"], "correct": 2, "explain": "Three of four (Dec 2018, Mar 2020, Apr 2025) saw SPY rise before the 50-day recrossed the 200-day; the fourth (Mar 2022) was a wash at −0.05%."},
    {"q": "Compounding only the golden-cross holding periods gave about +111% versus +215% for buy-and-hold over the same span. The main reason for the gap is:", "opts": ["The rule was in the market during every rally", "The rule was out of the market during rebounds that started before the 50-day could catch up with the 200-day", "Moving averages are always wrong", "Dividends"], "correct": 1, "explain": "The lag that protects you in a long decline also keeps you out for the first weeks or months of a recovery; three of the four out-of-market periods were rallies."}
  ],
  "task": "Compute the 20, 50 and 200-day SMAs on your ticker in a spreadsheet, count every 50/200 cross in the past ten years, and record the return from each cross to the next."
}
---

A moving average is a filter. It replaces a noisy series with a smoother one at the cost of delay. That trade-off, smoothness for lag, is the whole subject; everything else about moving averages follows from it. This lesson covers the two common types, the three conventional lengths, what crossovers are supposed to signal, and what ten years of SPY data say about how often they signal correctly.

## Simple and exponential

The **simple moving average** (SMA) of length n is the arithmetic mean of the last n closes. Every close in the window gets the same weight; a close that drops out of the window has its weight go from 1/n to zero in one step. That causes an SMA to jump when a large old bar leaves the window, which has nothing to do with today's price.

The **exponential moving average** (EMA) fixes that by weighting recent closes more and letting old ones decay gradually:

EMA today = EMA yesterday + k × (Close today − EMA yesterday), where k = 2 / (n + 1).

For n = 20, k = 2/21 = 0.0952. Today's close gets 9.5% of the weight and the prior EMA gets 90.5%. An EMA reacts faster than an SMA of the same length and never jumps when an old bar leaves, because old bars never fully leave.

Neither is better. The EMA is faster, which means more responsive and more false signals. The SMA is slower. Pick one and keep it; the difference between them matters far less than the difference between lengths.

## The 20, 50 and 200

These lengths are conventions, not discoveries. Twenty trading days is roughly a month, fifty a quarter, two hundred most of a year. They matter mostly because so many participants watch them, which is the same order-clustering argument from Lesson 3: if enough funds treat the 200-day as a line in the sand, orders will sit near it.

Three descriptive uses are defensible:

- **Price above or below the 200-day** is a widely used regime filter. Faber (2007) showed that holding an asset class only when its price was above its 10-month (roughly 200-day) SMA produced returns similar to buy-and-hold with materially smaller drawdowns, across equities, bonds, commodities and real estate from 1973 to 2005. Zakamulin (2014) re-examined that class of rule with longer data and found the outperformance was smaller and less consistent than the earlier work implied, though the drawdown reduction persisted.
- **Slope** of a moving average is a cheap trend measure: if the 50-day is rising, the average of the last 50 closes is higher than it was yesterday, which means today's close is above the close that dropped out of the window.
- **Distance from the average**, as a percentage, is a stretch measure. Price 15% above its 200-day is unusual and the unusual tends to revert, slowly.

## Crossovers

A crossover is when a shorter average crosses a longer one. The 50 crossing above the 200 is the "golden cross"; below, the "death cross". The idea is that the shorter average summarises recent price and the longer summarises the regime, so a cross marks a regime change.

The idea is correct as a description and late as a signal, because both averages lag. By the time the 50-day catches the 200-day after a decline, price has usually already fallen a long way; by the time it recrosses, price has usually already risen a long way. Brock, Lakonishok and LeBaron (1992) found that moving-average rules produced positive returns on the Dow from 1897 to 1986; Sullivan, Timmermann and White (1999) found the same rules earned nothing from 1987 to 1996. The ten-year check below is your own out-of-sample look.

## Worked example

SPY, daily closes, 26 September 2016 to 23 September 2026, from Yahoo Finance historical data. First the arithmetic for one day, then the record of every 50/200 cross.

**1 July 2025.** The sum of the 50 closes ending that day was 29,154.89, so SMA(50) = 29,154.89 / 50 = **583.10**. The sum of the 200 closes ending that day was 116,408.31, so SMA(200) = 116,408.31 / 200 = **582.04**. The previous day, SMA(50) was 581.27 and SMA(200) was 581.73. The 50 was below the 200 on 30 June and above it on 1 July: a golden cross. SPY closed at 617.65 that day, which was 617.65 / 582.04 − 1 = **6.1% above** the 200-day SMA at the moment of the "buy" signal, and 24.4% above the 8 April 2025 closing low of 496.48. The EMA(20) that day was 602.94; check: prior EMA 601.39 + 0.0952 × (617.65 − 601.39) = 601.39 + 1.55 = 602.94.

**Every 50/200 cross in the sample.** The table at the end of this lesson lists all nine, with the SPY close at each cross and the return from that close to the close at the next cross. The accounting below uses those rows.

Now the accounting. A rule that holds SPY only between a golden cross and the next death cross compounds the five golden-row returns: 1.0802 × 0.9154 × 1.3264 × 1.2935 × 1.2431 = 2.109, or **+110.9%**. Buy-and-hold from the first golden cross (244.01) to the last close in the sample (767.81) is 767.81 / 244.01 − 1 = **+214.7%**. The gap is the four death-row periods, during which SPY compounded 1.0845 × 1.2015 × 0.9995 × 1.1457 = 1.492, or **+49.2%**, while the rule was in cash.

Three of the four death crosses were followed by gains before the next golden cross. The March 2020 death cross printed on 30 March, six trading days after the 23 March low, and the rule stayed out until 9 July, missing +20.15%. The one death cross that "worked", March 2022, was a wash at −0.05% because the rule re-entered in February 2023 at almost exactly the price it had exited.

What the rule did do: the golden-to-death holding periods never contained the worst of the 2020 or 2022 declines. From the 14 March 2022 death cross the rule was out while SPY went from 417.00 to a 348.11 low, a 16.5% drop it did not experience. That is Faber's and Zakamulin's finding in one instrument: lower drawdown, lower return.

For contrast, the 20/50 pair crossed **41 times** in the same ten years. Trading it long-only from bullish cross to bearish cross gave 20 completed trades, 60% winners, average +3.67%. Faster averages give more signals and more whipsaws; that is the filter trade-off again.

## Table

Every 50/200-day SMA cross on SPY, September 2016 to September 2026. "Return to next cross" is the change in the SPY close from this cross to the next one; for Golden rows that is the return of a long position, for Death rows it is the return the rule sat out.

| Date | Type | Close | SMA 50 | SMA 200 | Return to next cross | Days |
|---|---|---|---|---|---|---|
| 12 Jul 2017 | Golden | 244.01 | 241.58 | 230.20 | +8.02% | 513 |
| 7 Dec 2018 | Death | 263.57 | 275.48 | 275.92 | +8.45% | 115 |
| 1 Apr 2019 | Golden | 285.83 | 275.65 | 275.37 | −8.46% | 364 |
| 30 Mar 2020 | Death | 261.65 | 301.39 | 302.42 | +20.15% | 101 |
| 9 Jul 2020 | Golden | 314.38 | 302.49 | 302.13 | +32.64% | 613 |
| 14 Mar 2022 | Death | 417.00 | 445.23 | 445.62 | −0.05% | 325 |
| 2 Feb 2023 | Golden | 416.78 | 394.35 | 394.25 | +29.35% | 802 |
| 14 Apr 2025 | Death | 539.12 | 573.31 | 573.83 | +14.57% | 78 |
| 1 Jul 2025 | Golden | 617.65 | 583.10 | 582.04 | +24.31% (open) | 449 |

The column to study is "Return to next cross" for the Death rows: three positive, one flat.

## Using averages without over-reading them

Use the 200-day as a regime label, not a signal. "Above" and "below" are conditions you can add to a checklist (Lesson 12); a cross is an event that happens too late to trade on its own.

Use the distance from the average as a stretch gauge and combine it with an oscillator (Lesson 7).

Do not optimise the length. If 47 works better than 50 on your history, that is noise, and Sullivan, Timmermann and White (1999) explain what happens next.

## Sources

- Brock, W., Lakonishok, J., & LeBaron, B. (1992). "Simple Technical Trading Rules and the Stochastic Properties of Stock Returns." *Journal of Finance*, 47(5). https://www.jstor.org/stable/2328994
- Faber, M. T. (2007). "A Quantitative Approach to Tactical Asset Allocation." *Journal of Wealth Management*, 9(4). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461
- Zakamulin, V. (2014). "The real-life performance of market timing with moving average and time-series momentum rules." *Journal of Asset Management*, 15(4). https://doi.org/10.1057/jam.2014.25
- Sullivan, R., Timmermann, A., & White, H. (1999). "Data-Snooping, Technical Trading Rule Performance, and the Bootstrap." *Journal of Finance*, 54(5). https://doi.org/10.1111/0022-1082.00163
