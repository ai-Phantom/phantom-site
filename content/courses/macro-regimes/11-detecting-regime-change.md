---
{
  "title": "Detecting Regime Change: How Late You Are, Why Filters Lag, and Switching vs Buy-and-Hold",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "In the 2020 decline, SPY peaked on 2020-02-19 and crossed below its 200-day SMA on 2020-02-27, six sessions later, by which point it was already 12.1% off the peak. In 2008 the cross came 22 sessions after the peak at -6.0%. Why was the faster decline detected later in percentage terms?", "opts": ["The 2020 data was wrong", "Because the VIX was higher in 2008", "Because the filter uses 250 days", "Because a moving-average filter detects distance, not time: a slow decline reaches the average after a small loss, a fast one after a large loss, and the 200-day was about 12% below the 2020 peak"], "correct": 3, "explain": "The lag of a trend filter is measured in price, not sessions. Whatever the speed of the decline, the filter fires when price reaches the average, and the average sits wherever the last 200 sessions put it."},
    {"q": "After the 2020-03-23 low, SPY re-crossed above its 200-day on 2020-05-26, by which point it had risen 34.1% from the low and was 11.1% below the peak. What did a switching rule earn from the round trip?", "opts": ["It avoided the whole decline", "It captured the rebound", "Almost nothing: it exited at -12.1% from the peak and re-entered at -11.1%, so being out of the market covered a net move of +1.1% in SPY, and the rule paid two switches for it", "It lost 33.7%"], "correct": 2, "explain": "The rule was out for the worst 21.6 points of the fall and also for the first 34 points of the recovery. In a V-shaped decline the two cancel. Only in a long decline does the exit pay."},
    {"q": "The four declines studied (2008, 2020, 2022, 2025) gave the 200-day switching rule these results while out of the market: SPY moved -34.8%, +1.1%, -5.8% and +4.3%. What is the pattern?", "opts": ["The rule earns a great deal in a long decline (2008), roughly nothing in a V (2020), a little in a grinding decline (2022), and pays in a short correction (2025); the distribution of outcomes is the distribution of decline shapes", "The rule always wins", "The rule always loses", "The rule works only in even years"], "correct": 0, "explain": "One of four episodes produced nearly all of the benefit. That is the same structure as the 107-trade record in lesson 7: a few long trades pay for many short ones."},
    {"q": "The VIX crossed 25 on 2020-02-24 when SPY was 4.7% off its peak, three sessions before the 200-day cross at -12.1%. Does this make the VIX the better detector?", "opts": ["Yes, it is always faster", "It was faster in that episode, but the VIX also crossed 25 on many days that were not followed by a regime change (204 crossings from 2005 to 2026); a faster detector with more false alarms is a different trade-off, not a free improvement", "No, the VIX is a lagging indicator", "They are the same signal"], "correct": 1, "explain": "Detection speed and false-alarm rate move together. Every threshold you lower to catch the next crash earlier catches more non-crashes too."},
    {"q": "Why does the lesson say that regime change is only knowable in retrospect?", "opts": ["Because NBER dates recessions after the fact", "Because a persistent state and a short flicker look identical on the day they begin; persistence is established by the state lasting, and by then the filter has already fired late. The best you can do is choose the lag you will accept", "Because the data is revised", "Because markets are random"], "correct": 1, "explain": "The 2019 three-day 2s10s inversion and the 2022 two-day one looked the same as the first days of the 2022-2024 inversion. Nothing at the time distinguished them."}
  ],
  "task": "For the most recent time SPY crossed below its 200-day SMA, write down the date, how far it was from the prior peak on that day, and what SPY did between that cross and the next re-cross."
}
---

## Lag is the price of a definition

Every regime variable in this course is a function of past data: a 200-session average, a 21-session realised volatility, a spread that has to stay negative for weeks to count, a VIX that rises only after prices have started to move. That is not a defect to be engineered away; it is what makes the variable observable. A regime you could identify on its first day would be a forecast, and the point of a regime variable is that it is a measurement.

The consequence is that you are always late, and the useful question is how late. This lesson measures it for the 200-day filter and the VIX threshold on the four largest SPY declines since 2007, in sessions and in the percentage of the decline that had already happened when the filter fired, and then in the percentage of the recovery that had already happened when it re-entered.

## How late, in the four declines

In 2008, SPY's total-return peak was 2007-10-09 and the trough 2009-03-09, a 517-day, -55.2% decline. The 200-day cross came on 2007-11-08, 22 sessions after the peak, at -6.0%. The VIX crossed 25 on 2007-11-07 at -5.5% and 30 on 2007-11-12 at -8.2%. The re-cross above the 200-day came on 2009-05-29, 57 sessions after the trough, with SPY 36.8% above the low and still 38.7% below the peak. Between the cross and the re-cross SPY moved -34.8%: the switching rule avoided most of the decline.

In 2020, the peak was 2020-02-19 and the trough 2020-03-23, 33 days, -33.7%. The 200-day cross came six sessions after the peak, on 2020-02-27, but by then SPY was already 12.1% down, because the fall was so fast that the price reached the average in a week. The VIX crossed 25 on 2020-02-24 at -4.7% and 30 on 2020-02-27 at -12.1%. The re-cross came on 2020-05-26, 44 sessions after the trough, with SPY 34.1% above the low and 11.1% below the peak. Between cross and re-cross SPY moved +1.1%: the rule was out for the worst of the fall and the first third of the rebound, and the two cancelled.

In 2022, the peak was 2022-01-03 and the trough 2022-10-12, 282 days, -24.5%. The cross came on 2022-01-21, 13 sessions after the peak, at -8.3%. The VIX crossed 25 on 2022-01-20 at -6.5% and 30 on 2022-01-25 at -9.1%. The re-cross came on 2022-11-30, 34 sessions after the trough, at +14.3% from the low and -13.7% from the peak. Between cross and re-cross SPY moved -5.8%: a modest saving from a grinding decline that spent most of the year oscillating around the average.

In 2025, the peak was 2025-02-19 and the trough 2025-04-08, 48 days, -18.8%. The cross came on 2025-03-10 at -8.5%, the VIX crossed 25 the same day and 30 on 2025-04-03 at -12.2%. The re-cross came on 2025-05-12, 23 sessions after the trough, at +17.4% from the low and -4.6% from the peak. Between cross and re-cross SPY moved +4.3%: the rule paid to be out.

## Why the lag is in price, not time

The 2020 case shows the essential property. The filter fired six sessions after the peak, faster than in any other episode, and it was the latest in percentage terms, because a trend filter detects distance from an average, not elapsed time. The average sits wherever the last 200 sessions left it, about 12% below the February 2020 peak. However fast or slow the decline, the filter fires when price reaches that level. A slow decline reaches it after a small loss; a fast one after a large loss. The VIX threshold is faster in a fast decline (three sessions ahead of the 200-day in 2020) because volatility responds to the speed of the move, but it is also the noisier input: from 2005 to 2026 the VIX crossed 25 in one direction or the other 204 times, against 134 crossings of the 200-day, and those crossings drove most of lesson 9's 320 state changes. A faster detector with more false alarms is a different trade-off, not a better detector.

## Switching versus buy-and-hold

The four episodes give the switching rule these results while it was out: -34.8%, +1.1%, -5.8%, +4.3%. One episode produced essentially the whole benefit. That is the same shape as lesson 7's full record, where 19 trades of more than 100 sessions produced +426.7% and 60 trades of five sessions or fewer produced -78.5%, and it leads to the same conclusion: a switching rule is a bet that the next decline will be long. Since 1993, one in four of the large ones has been.

Buy-and-hold makes the opposite bet and has been paid for it in three of the four episodes. Its cost is the fourth, and whether you can carry the fourth is the question lesson 10 asked. Neither is right; they are different exposures to the shape of the next decline, and the honest position is to know which one you are holding.

## What you can and cannot detect

Regime change is knowable only in retrospect. On 2019-08-27 the 2s10s inverted for three sessions; on 2022-04-01 for two; on 2022-07-06 for what became 539. Nothing on the first day distinguished them. On 2020-02-24 the VIX crossed 25; it had also done so on dozens of days in 2018 and 2019 that were followed by nothing. Persistence is established by the state persisting, and by the time it has, the filter has fired late.

The operational conclusion is to choose your lag deliberately. A longer average or a higher threshold fires later and flickers less; a shorter one fires earlier and pays more whipsaws. There is no setting that is early and quiet. What you can do is refuse the binary: a sizing policy that moves exposure gradually as the state deepens (lesson 10) pays a smaller price for each false alarm and captures a larger share of each true one than a switch does, and the capstone asks you to write one.

## Worked example

Data: SPY adjusted close and `^VIX` close from the Yahoo Finance chart API, current session dropped; the 200-session SMA is computed on the adjusted close. Peak and trough dates are the sessions with the highest adjusted close before the decline and the lowest during it. "Sessions after peak" counts trading days. Drawdown at a signal is the adjusted close on the signal day divided by the peak close, minus one. "Out of market" return is the adjusted close on the re-cross day divided by the adjusted close on the cross day, minus one.

2008: peak 2007-10-09, trough 2009-03-09 (-55.2%, 517 days). Cross 2007-11-08 (22 sessions, -6.0%). VIX above 25 on 2007-11-07 (-5.5%); above 30 on 2007-11-12 (-8.2%). Re-cross 2009-05-29 (57 sessions after trough, +36.8% from trough, -38.7% from peak). VIX first below 25 after the trough: 2009-07-17. New total-return high: 2012-08-16. Out-of-market move: -34.8%.

2020: peak 2020-02-19, trough 2020-03-23 (-33.7%, 33 days). Cross 2020-02-27 (6 sessions, -12.1%). VIX above 25 on 2020-02-24 (-4.7%); above 30 on 2020-02-27 (-12.1%). Re-cross 2020-05-26 (44 sessions, +34.1%, -11.1%). VIX below 25: 2020-06-05. New high: 2020-08-10. Out-of-market move: +1.1%.

2022: peak 2022-01-03, trough 2022-10-12 (-24.5%, 282 days). Cross 2022-01-21 (13 sessions, -8.3%). VIX above 25 on 2022-01-20 (-6.5%); above 30 on 2022-01-25 (-9.1%). Re-cross 2022-11-30 (34 sessions, +14.3%, -13.7%). VIX below 25: 2022-11-04. New high: 2023-12-13. Out-of-market move: -5.8%.

2025: peak 2025-02-19, trough 2025-04-08 (-18.8%, 48 days). Cross 2025-03-10 (13 sessions, -8.5%). VIX above 25 on 2025-03-10 (-8.5%); above 30 on 2025-04-03 (-12.2%). Re-cross 2025-05-12 (23 sessions, +17.4%, -4.6%). VIX below 25: 2025-04-25. New high: 2025-06-26. Out-of-market move: +4.3%.

A check on one figure: in 2020 the cross came at -12.1% and the re-cross at -11.1% from the same peak, so the out-of-market move is (1 - 0.111) / (1 - 0.121) - 1 = 0.889 / 0.879 - 1 = +1.1%.

## Table

| Decline | Peak to trough | 200-day cross: sessions after peak, drawdown then | VIX > 25: drawdown then | Re-cross: sessions after trough, gain from low, vs peak | SPY move while out |
|---|---|---|---|---|---|
| 2008 | 2007-10-09 to 2009-03-09, -55.2% | 22, -6.0% | -5.5% | 57, +36.8%, -38.7% | -34.8% |
| 2020 | 2020-02-19 to 2020-03-23, -33.7% | 6, -12.1% | -4.7% | 44, +34.1%, -11.1% | +1.1% |
| 2022 | 2022-01-03 to 2022-10-12, -24.5% | 13, -8.3% | -6.5% | 34, +14.3%, -13.7% | -5.8% |
| 2025 | 2025-02-19 to 2025-04-08, -18.8% | 13, -8.5% | -8.5% | 23, +17.4%, -4.6% | +4.3% |

Read the last column against the second. The rule's benefit is a function of the length of the decline: 517 days paid -34.8%, 282 days paid -5.8%, and the two declines under 50 days cost money. The middle columns show the fixed costs: the rule is 6 to 12 percent late on the way down and 14 to 37 percent late on the way up, in every episode, regardless of what it earned.

## Sources

- Yahoo Finance historical data for SPY and ^VIX: https://finance.yahoo.com/quote/SPY/history/ and https://finance.yahoo.com/quote/%5EVIX/history/
- National Bureau of Economic Research, Business Cycle Dating: https://www.nber.org/research/business-cycle-dating
- Zakamulin, V. (2014), "The Real-Life Performance of Market Timing with Moving Average and Time-Series Momentum Rules", Journal of Asset Management 15(4), https://doi.org/10.1057/jam.2014.25
- Hamilton, J. D. (1989), "A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle", Econometrica 57(2), https://doi.org/10.2307/1912559
