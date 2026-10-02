---
{
  "title": "Building and Testing a Reversion Rule With Walk-Forward Validation",
  "duration": "19 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Over 2019 to 2026 the best of 32 RSI(2) rule variants, chosen with full knowledge of those years, earned +159.0%. The walk-forward procedure, which chose each year's variant using only the three prior years, earned +81.4%. The difference is:", "opts": ["A measure of how much of the in-sample number was selection: about half of it was picking the winner after seeing the race", "A bug in the walk-forward", "Proof the rule does not work", "Due to costs"], "correct": 0, "explain": "The in-sample best is the maximum of 32 noisy numbers, which is biased upward. Walk-forward removes the look-ahead and the number roughly halves. The grid median over the same years was +57.0%, close to the fixed default rule's +59.0%."},
    {"q": "In the walk-forward, the variant chosen for the 2019 test year (threshold 20, fixed 5-day exit, filter on) earned +15.7% on its 2016-2018 training data and −0.4% in 2019. What does that tell you?", "opts": ["The 2019 data was wrong", "The best in-sample variant is often the one that fitted that window's noise; its edge did not carry into the next year, which is exactly what the test exists to reveal", "Threshold 20 is always wrong", "Training on three years is too long"], "correct": 1, "explain": "Annualising the three-year training returns, five of the eight test years fell short of their training figure and three (2021, 2023, 2024) exceeded it. The gap is the overfitting you would otherwise never see."},
    {"q": "The fixed default rule (threshold 10, 5-day SMA exit, filter on) earned +59.0% over the same eight test years with no fitting at all. Compared with the walk-forward's +81.4%:", "opts": ["The default is clearly worse", "The walk-forward's extra return came mostly from switching to a fixed 5-day exit with the filter off from 2021 onward; whether that is skill or a lucky match to a rising market is not knowable from eight years", "The default should be abandoned", "Both should be doubled"], "correct": 1, "explain": "The chosen parameters changed three times across eight years. Adaptation helps when regimes persist for longer than the training window and hurts when they do not; the sample is too short to say which happened here."},
    {"q": "SPY buy-and-hold over the same 2019-2026 period returned +207.2%. The honest comparison with the +81.4% walk-forward result is:", "opts": ["The rule beat the market", "The rule is worthless", "The rule earned less than half of buy-and-hold while in the market roughly one day in six; it is a low-exposure return stream, not a replacement for holding the index", "SPY's return is irrelevant"], "correct": 2, "explain": "A reversion rule with 11 to 17% exposure should not be expected to match a fully-invested index in a bull market. The comparison that matters is return per unit of exposure and drawdown, which lesson 4 gave for the base rule."},
    {"q": "Why should the walk-forward design itself (three-year train, one-year test, choose by total return with at least 10 trades) be fixed before you run it?", "opts": ["Because the computer requires it", "Because every design choice is another parameter; trying several designs and reporting the best re-introduces the selection bias the procedure was meant to remove", "Because one-year tests are illegal", "Because it makes the code faster"], "correct": 1, "explain": "Bailey, Borwein, López de Prado and Zhu (2014) call this backtest overfitting: the more configurations tried, the higher the best in-sample Sharpe ratio, with no change in true expected performance."}
  ],
  "task": "Write down, before running anything, the rule family, the grid, the training length, the test length and the selection criterion you would use to walk-forward test your own reversion rule."
}
---

Every result in this course so far has one weakness in common: the rule was specified after looking at the data. Lesson 4 tested seven RSI(2) variants and reported all seven, which is better than reporting only the best one, but you still saw the table before deciding what you thought. Walk-forward validation is the procedure that takes the decision out of your hands: it picks the rule on data it is allowed to see and scores it on data it is not. This lesson runs the full procedure on the RSI(2) rule over eight test years and shows you how much of the in-sample result was real.

## The problem it solves

Suppose you test 32 variants of a rule on eleven years of data and report the best. Even if all 32 have the same true expected return, the best observed return will be well above the average, because you selected the maximum of 32 noisy draws. Bailey, Borwein, López de Prado and Zhu (2014) show that with enough variants, the best in-sample Sharpe ratio can be made arbitrarily high with no true edge at all. Harvey, Liu and Zhu (2016) apply the same logic to the hundreds of published return predictors and argue that most would not survive a correction for the number of things that were tried.

You cannot un-see the data. What you can do is simulate a trader who had not seen it: at each point in time, choose the rule using only the past, apply it to the next period, record what happened, and move on. The recorded out-of-sample sequence is what that trader would have earned.

## The procedure

1. **Fix the rule family and the grid before starting.** Entry threshold in {5, 10, 15, 20}; exit in {close above 5-day SMA, RSI(2) above 70, fixed 5 days, fixed 3 days}; 200-day filter on or off. 32 combinations. This list does not change once the test begins.
2. **Training window**: the three calendar years before the test year.
3. **Selection**: the combination with the highest compounded net return on the training window, subject to at least 10 trades.
4. **Test window**: the next calendar year, traded with the chosen combination, every trade recorded, no changes.
5. **Roll** forward one year and repeat.
6. **Stitch** the test years into one out-of-sample record and compare it with a fixed benchmark rule and with buy-and-hold.

Every one of those six choices is a parameter. Three years rather than two, total return rather than average trade, ten trades rather than twenty: each could be varied, and trying several and keeping the best would reintroduce the problem. Write the design down, run it once, report it.

## Chart

![The walk-forward loop as run in this lesson: fix the family and grid, train on three years, pick the best combination, test on the untouched next year, roll forward, stitch the test years. Notes give the specific settings and the result: 111 out-of-sample trades, +81.4% against +59.0% for the fixed default rule. Source: computed by the course on Yahoo Finance SPY closes.](figures/walk-forward-process.svg)

## Worked example

Data: Yahoo Finance daily closes for SPY, `interval=1d`, 2015-01-02 to 2026-09-23, pulled 2026-09-24; cost 0.01% per side. Test years 2019 through 2026 (2026 runs to 09-23). The first training window is 2016-01-04 to 2018-12-31.

**Test year 2019.** Training 2016-2018. Best of the 32: threshold 20, fixed 5-day exit, filter on, +15.7% over 43 training trades. Applied to 2019: 12 trades, **−0.4%**. The fixed default (threshold 10, 5-day SMA exit, filter on): 7 trades, +1.7%. SPY: +28.8%.

**2020.** Training 2017-2019. Best: threshold 15, RSI-above-70 exit, filter on, +9.5% in training. Out of sample: 8 trades, **−3.3%**. Default: +2.9%. SPY +16.2%.

**2021.** Training 2018-2020. Best: threshold 20, fixed 5 days, filter off, +13.9%. Out of sample: 16 trades, **+11.0%**. Default: +14.7%. SPY +27.0%.

**2022.** Training 2019-2021. Best: threshold 20, fixed 5 days, filter off, +42.2%. Out of sample: 26 trades, **−5.1%**. Default: 2 trades, −2.9%. SPY −19.5%. The unfiltered rule bought every dip of a bear market.

**2023.** Training 2020-2022. Best: threshold 10, fixed 5 days, filter off, +39.3%. Out of sample: 13 trades, **+14.5%**. Default: +3.5%. SPY +24.3%.

**2024.** Same combination chosen (+38.7% in training). Out of sample: 12 trades, **+24.3%**. Default: +13.4%. SPY +23.3%.

**2025.** Same combination (+44.1%). Out of sample: 12 trades, **+10.7%**. Default: +6.1%. SPY +16.4%.

**2026 to 09-23.** Same combination (+59.5%). Out of sample: 12 trades, **+13.6%**. Default: +9.6%. SPY +12.6%.

**Stitched.** 111 out-of-sample trades, 64% winners, average +0.577%, compounded **+81.4%**. The fixed default over the same eight years: 68 trades, **+59.0%**. SPY: **+207.2%**.

**The number you would have reported otherwise.** Run all 32 combinations on 2019-2026 directly and take the best: threshold 10, fixed 5 days, filter off, 97 trades, **+159.0%**. That is the in-sample result. The walk-forward earned 51% of it. The median of the 32 combinations over 2019-2026 was +57.0%, the worst +15.4% (threshold 5, fixed 3 days, filter on, 36 trades).

## Year by year

| Test year | Training window | Chosen combination | Train return | Out-of-sample | Fixed default | SPY |
|---|---|---|---|---|---|---|
| 2019 | 2016-01-04 to 2018-12-31 | thr 20, fixed 5 d, filter on | +15.7% | −0.4% (12) | +1.7% (7) | +28.8% |
| 2020 | 2017-01-03 to 2019-12-31 | thr 15, RSI > 70, filter on | +9.5% | −3.3% (8) | +2.9% (7) | +16.2% |
| 2021 | 2018-01-02 to 2020-12-31 | thr 20, fixed 5 d, filter off | +13.9% | +11.0% (16) | +14.7% (11) | +27.0% |
| 2022 | 2019-01-02 to 2021-12-31 | thr 20, fixed 5 d, filter off | +42.2% | −5.1% (26) | −2.9% (2) | −19.5% |
| 2023 | 2020-01-02 to 2022-12-30 | thr 10, fixed 5 d, filter off | +39.3% | +14.5% (13) | +3.5% (10) | +24.3% |
| 2024 | 2021-01-04 to 2023-12-29 | thr 10, fixed 5 d, filter off | +38.7% | +24.3% (12) | +13.4% (13) | +23.3% |
| 2025 | 2022-01-03 to 2024-12-31 | thr 10, fixed 5 d, filter off | +44.1% | +10.7% (12) | +6.1% (8) | +16.4% |
| 2026 (to 09-23) | 2023-01-03 to 2025-12-31 | thr 10, fixed 5 d, filter off | +59.5% | +13.6% (12) | +9.6% (10) | +12.6% |
| **Stitched 2019-2026** | | | | **+81.4% (111)** | **+59.0% (68)** | **+207.2%** |

Trade counts in parentheses. In-sample best over 2019-2026 with hindsight: +159.0%. Source: Yahoo Finance daily closes, computed by the course.

## Reading it

Three things stand out. Training returns are three-year totals, so divide by three for a rough annual figure: 3% to 17% per year. Five of the eight test years fell short of their annualised training figure, and the three exceptions (2021, 2023 and 2024) were years the training combination happened to suit. The selection changed three times: the 2019-2020 picks (thresholds 20 and 15, filter on) both lost out of sample; the switch to filter-off in 2021 caught a bull market and then bought every dip of 2022; the settled choice from 2023 on was the one that would have been best in hindsight, but a trader following the procedure did not have it until 2023. And the fixed default, with no fitting at all, did about as well as the grid median, which is the honest baseline for a rule family: most variants of a reasonable rule earn about what the family earns.

The walk-forward's +81.4% against the default's +59.0% is the case for adaptation, and the 2022 row is the case against. Eight years cannot settle it. What the procedure does settle is the size of the in-sample illusion: +159.0% was the number you would have seen, and about half of it was selection.

## What to do with your own rule

Write the design first: family, grid, training length, test length, criterion. Run it once. Report the stitched out-of-sample record next to a fixed default and next to buy-and-hold, with trade counts, and report the in-sample best alongside so the reader can see the gap. If the out-of-sample record is not better than the default, the fitting is not earning its complexity. And if the out-of-sample record is worse than a plain average of the grid, the fitting is choosing noise. Those two comparisons, not the headline return, are the test.

## Sources

- Bailey, D. H., Borwein, J. M., López de Prado, M. and Zhu, Q. J. (2014). Pseudo-mathematics and financial charlatanism: the effects of backtest overfitting on out-of-sample performance. *Notices of the American Mathematical Society*, 61(5), 458–471. https://doi.org/10.1090/noti1105
- Harvey, C. R., Liu, Y. and Zhu, H. (2016). ... and the cross-section of expected returns. *Review of Financial Studies*, 29(1), 5–68. https://doi.org/10.1093/rfs/hhv059
- White, H. (2000). A reality check for data snooping. *Econometrica*, 68(5), 1097–1126. https://doi.org/10.1111/1468-0262.00152
- Yahoo Finance, SPY historical data: https://finance.yahoo.com/quote/SPY/history/
