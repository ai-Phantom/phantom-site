---
{
  "title": "Capstone: A Four-State Regime Table for 2015-2026 and a Sizing Policy",
  "duration": "45 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "In the 2015-2026 reference table, 126 of the 250 sessions in S4 (trend down, VIX above 25) fall in 2022 and 59 in 2020. What does that mean for the S4 row?", "opts": ["S4 is well estimated because it has 250 days", "S4 is irrelevant because it is rare", "The S4 row is mostly two episodes, so its statistics describe 2022 and 2020 more than they describe a repeatable state; a different next S4 episode could look nothing like them", "2022 and 2020 should be removed"], "correct": 2, "explain": "Day counts overstate the information in a state when the days are clustered. The honest unit of evidence for a regime is the number of independent episodes, and S4 has about two large ones in this window."},
    {"q": "GLD returned +52.0% annualised in S3 (trend down, calm) over 2015-2026, but -10.2% in S3 over 2005-2015 in lesson 9's split. How should the capstone treat it?", "opts": ["As an unstable result: a sign flip across halves means the row is a description of one sample, not a property of the state, and it should not drive the sizing policy", "Overweight gold in S3", "As proof that gold is a hedge", "As a data error"], "correct": 0, "explain": "A result that flips sign between non-overlapping periods fails the cheapest robustness test there is. Report it; do not size on it."},
    {"q": "The reference policy (SPY exposure 1.0 in S1, 0.5 in S2 and S3, 0.25 in S4, T-bills otherwise) returned 10.83% a year against 13.74% for buy-and-hold, with -18.0% maximum drawdown against -33.7%. Which description is accurate?", "opts": ["The policy beat buy-and-hold", "The policy gave up 2.9 points of annual return to cut the drawdown nearly in half and volatility by a third; its excess return per unit of volatility was higher (0.75 against 0.67), and it lost to buy-and-hold on raw return", "The policy failed", "The policy and buy-and-hold are equivalent"], "correct": 1, "explain": "A sizing policy is judged on what it was designed to do. This one reduced drawdown and volatility and paid for it in return, which is the trade-off the course has measured throughout."},
    {"q": "Which statement belongs in the 'what the sample cannot tell you' section?", "opts": ["SPY's annualised return in S1 was 11.8%", "That the classifier changed state 164 times", "That the VIX threshold was 25", "Whether S4's +36.0% annualised SPY mean will recur, because it is the average of the 2020 and 2022 crash and rebound days, and the next stressed down-trend may have a different shape"], "correct": 3, "explain": "The other three are facts about the sample. The S4 mean is a fact too, but its use as an expectation is exactly what the sample cannot support."},
    {"q": "Why must the state be read at the close of day t and the return measured on day t+1?", "opts": ["Because a state is only usable if it is known before the return it is used for; same-day attribution credits the policy with information it could not have had", "To make the results look better", "Because Yahoo publishes data with a one-day delay", "Because it reduces the number of states"], "correct": 0, "explain": "This is the look-ahead rule that every lesson has followed. A capstone that breaks it fails criterion 1 of the rubric regardless of its other qualities."}
  ],
  "task": "Submit your state table, your written sizing policy and your limitations section as one document, with the code or spreadsheet that produced the numbers attached."
}
---

## The exercise

You will build a four-state regime table for 2015 through the latest full session, from rules stated in advance, measure how SPY, TLT and GLD behaved in each state, write a sizing policy per state, test it, and write down what the sample can and cannot tell you. Every number must be computed by you from data you name, and every rule must be fixed before you look at the results.

This is the course in one document. Lesson 9 built the classifier on 2005-2026; you are re-running it on the more recent window and deciding what to do with it. Lessons 6, 7 and 10 give you the reasons for each choice; lessons 11 and 12 give you the reasons to be modest about the result.

## Step 1: data

Pull daily bars for SPY, TLT, GLD, `^VIX` and `^IRX` from the Yahoo Finance chart API with explicit Unix timestamps, for example `https://query1.finance.yahoo.com/v8/finance/chart/SPY?period1=631152000&period2=<today>&interval=1d`. Do not use `range=max`; it returns monthly bars. For each series, record the row count, first date and last date, and drop the current session if the market has not closed. Use the adjusted close for the three funds and the close for the two indexes.

Start SPY's history well before 2015 so the 200-session SMA is fully formed on the first day of the test. If any series has gaps, align on the dates all five share and say how many sessions that removes.

## Step 2: the rules, written first

Write these down before computing anything:

Trend axis: up if SPY's adjusted close on day t is above the mean of its last 200 adjusted closes (including day t), else down. Volatility axis: stressed if the VIX close on day t is above 25, else calm. States: S1 up/calm, S2 up/stressed, S3 down/calm, S4 down/stressed. Attribution: the state on day t is assigned the return from the close of day t to the close of day t+1.

You may substitute different thresholds (a VIX of 20 or 30, a 150-day average) if you justify the choice from lessons 6 and 7 before running the numbers. You may not try several and keep the best. If you change your mind after seeing results, say so, and report both.

## Step 3: the state table

For each state and each of SPY, TLT and GLD, compute: the number of sessions and their share of the window; annualised return (compound the state's daily returns, raise the growth factor to 252 over the day count, subtract one); annualised volatility (standard deviation of the state's daily returns times the square root of 252); and maximum drawdown of the within-state compounded curve. Add a row for buy-and-hold over the whole window. Also report the number of state changes and the median run length.

## Step 4: the sizing policy

Write one exposure rule per state for SPY, with the remainder in T-bills (the prior session's `^IRX` divided by 100 and by 252). You may also allocate to TLT or GLD per state, but only if the per-state result you rely on was stable in lesson 9's split halves. Charge 5 basis points per unit of exposure change. Report annualised return, volatility, maximum drawdown, excess return over T-bills divided by volatility, mean exposure and turnover per year, against buy-and-hold over the same days.

Justify each state's exposure in one or two sentences from evidence in this course: the width of the state's distribution (lesson 9), the cost of binary exits (lesson 10), the lag at transitions (lesson 11).

## Step 5: what the sample can and cannot tell you

Write at least four statements of each kind. Can: facts about the sample (counts, per-state statistics, the policy's measured trade-off). Cannot: which per-state results are a few episodes in disguise; which flipped sign against lesson 9's 2005-2015 half; what a state that did not occur in the window (a stressed down-trend with falling real yields and a Fed hiking, for instance) would do; and whether the thresholds you chose are the ones a different sample would favour.

## Worked example

This is the reference computation, so you can check your mechanics before you write your own policy. Data pulled 2026-09-30 from the Yahoo Finance chart API with `period1=631152000` and `period2=1790812800`, current session dropped: SPY 8,474 sessions from 1993-01-29, TLT 6,081 from 2002-07-30, GLD 5,499 from 2004-11-18, `^VIX` 9,255 from 1990-01-02, `^IRX` 9,222 from 1990-01-02, all ending 2026-09-29.

The window runs 2015-01-02 to 2026-09-29: 2,951 return days on the dates SPY, TLT, GLD and VIX share. State counts: S1 2,309 (78.2%), S2 139 (4.7%), S3 253 (8.6%), S4 250 (8.5%). Check: 2,309 + 139 + 253 + 250 = 2,951. State changes: 164; median run 3 sessions; 104 of 165 runs lasted five sessions or fewer.

One cell in full, S4 SPY. The 250 daily returns have a mean of 0.1536% and a standard deviation of 2.5127%. Their compounded growth factor is 1.3567. Annualised return: 1.3567 ^ (252 / 250) - 1 = 36.0%. Annualised volatility: 2.5127% x sqrt(252) = 2.5127% x 15.875 = 39.9%. Within-state maximum drawdown: -25.9%. By calendar year, those 250 sessions were: 2015 14, 2016 11, 2018 10, 2019 1, 2020 59, 2022 126, 2023 2, 2025 18, 2026 9. More than half are 2022 and nearly three quarters are 2020 and 2022 together.

The reference policy: SPY exposure 1.0 in S1, 0.5 in S2, 0.5 in S3, 0.25 in S4, T-bills otherwise, 5 basis points per unit of exposure change. Aligning with `^IRX` removes one session, leaving 2,950 return days. Result: annualised return 10.83%, volatility 11.65%, maximum drawdown -18.0%, mean exposure 0.87, turnover 5.98x a year. Buy-and-hold on the same days: 13.74%, 17.54%, -33.7%. The mean T-bill return over the window was 2.07% a year, so the excess-return ratios are (10.83 - 2.07) / 11.65 = 0.75 for the policy and (13.74 - 2.07) / 17.54 = 0.67 for buy-and-hold.

The reference policy lost 2.9 points of annual return to buy-and-hold. It is not offered as a good policy; it is offered so you can check your engine. Yours should differ, and your justification is what is graded.

## Table

Reference state table, 2015-01-02 to 2026-09-29 (state at close t, return on t+1; annualised return / annualised volatility / within-state maximum drawdown):

| State | Sessions | SPY | TLT | GLD |
|---|---|---|---|---|
| S1 up / calm | 2,309 (78.2%) | +11.8% / 12.0% / -20.6% | +0.5% / 13.1% / -29.4% | +8.7% / 15.8% / -28.5% |
| S2 up / stressed | 139 (4.7%) | +23.6% / 23.8% / -14.9% | -4.7% / 14.5% / -13.2% | +11.8% / 15.3% / -6.5% |
| S3 down / calm | 253 (8.6%) | +6.1% / 20.1% / -11.9% | +11.7% / 14.8% / -9.2% | +52.0% / 14.4% / -7.7% |
| S4 down / stressed | 250 (8.5%) | +36.0% / 39.9% / -25.9% | -25.3% / 25.5% / -29.4% | -3.5% / 22.1% / -20.0% |
| Buy and hold, whole window | 2,951 | +13.7% / 17.5% / -33.7% | -1.4% / 14.8% / -48.4% | +10.9% / 16.3% / -26.4% |

Three warnings that belong in your limitations section if you use this window. S2 is 95 sessions of 2020 out of 139, so it is mostly the post-crash rebound. S3's GLD result (+52.0%) flipped sign against 2005-2015 (-10.2%) and should not drive a gold allocation. S4's TLT result (-25.3%) is dominated by 2022, the one rates-shock bear market in the window; in the 2008 and 2020 growth shocks, TLT rose during the decline (lesson 12).

## Rubric

| # | Criterion | What earns full marks | Points |
|---|---|---|---|
| 1 | Data and rules | Every series named with source, request parameters, row count and date range; rules written before results; state read at close t, return on t+1; no threshold shopping, or any change disclosed with both versions reported | 20 |
| 2 | State table | Counts, shares, annualised return, volatility and drawdown for SPY, TLT and GLD in all four states plus buy-and-hold; one cell's calculation shown in full; numbers reproducible from the attached code | 25 |
| 3 | Sizing policy | An exposure rule for every state, each justified from a specific course result about width, lag or the cost of binary exits; costs charged; results reported against buy-and-hold on the same days, including where the policy lost | 25 |
| 4 | Can and cannot | At least four of each; identifies which states are one or two episodes; flags any per-state result that flipped sign against lesson 9's earlier half; names a state the window never contained | 20 |
| 5 | Presentation | Plain statements, dated numbers, no performance claims beyond the sample, no recommendation to anyone else about what to trade | 10 |

A submission that measures returns on the same day the state was read fails criterion 1 outright and cannot score more than 50 overall, whatever its other qualities.

## Sources

- Yahoo Finance historical data: https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/%5EVIX/history/, https://finance.yahoo.com/quote/%5EIRX/history/
- Cboe, VIX Index methodology: https://www.cboe.com/tradable_products/vix/vix_index_methodology/
- Moreira, A. and Muir, T. (2017), "Volatility-Managed Portfolios", Journal of Finance 72(4), https://doi.org/10.1111/jofi.12513
- Bailey, D. H. and López de Prado, M. (2014), "The Deflated Sharpe Ratio", Journal of Portfolio Management 40(5); SSRN: https://ssrn.com/abstract=2460551
