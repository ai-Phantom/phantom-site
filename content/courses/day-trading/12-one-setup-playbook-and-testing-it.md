---
{
  "title": "Building a One-Setup Playbook and Testing It",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Over the first 30 sessions, 11 of the 12 opening-range variants were profitable. Over the second 30 sessions:", "opts": ["All 12 were profitable", "3 of 12 were profitable and the average variant lost $6.48 per share", "6 of 12 were profitable", "None traded"], "correct": 1, "explain": "The in-sample mean was +$11.46 per share; out of sample it was −$6.48. The rule family did well in July and badly in August and September."},
    {"q": "The best in-sample variant (OR15, 1R, opposite edge: +$21.33) did what out of sample?", "opts": ["+$21.33 again", "−$6.33", "+$2.93", "+$15.00"], "correct": 1, "explain": "Picking the winner of the first half and trading it forward lost money. That is what Bailey et al. call backtest overfitting, compounded here by a change in the market's behaviour."},
    {"q": "Which variant was best out of sample?", "opts": ["OR15 / 1R / opposite edge", "OR30 / 2R / midpoint", "OR5 / 2R / opposite edge, at +$2.93", "OR15 / 2R / midpoint"], "correct": 2, "explain": "The best out-of-sample result was small and was not the best in-sample variant; no in-sample ranking predicted it."},
    {"q": "Harvey, Liu and Zhu's recommendation for strategies discovered by searching many variants is to:", "opts": ["Use the usual t-statistic threshold of 2", "Demand a higher hurdle, around t = 3, because multiple testing inflates false discoveries", "Ignore statistics", "Only test one variant ever"], "correct": 1, "explain": "The more variants you try, the more likely the best one is a fluke; the evidence bar must rise with the number of trials."},
    {"q": "A one-setup playbook is preferable for a beginner because:", "opts": ["One setup always works", "It produces a clean sample for one hypothesis; multiple setups traded at once mix their statistics and make every one of them untestable", "It is cheaper", "Brokers require it"], "correct": 1, "explain": "Expectancy is per setup. Thirty sessions of one rule is evidence; thirty sessions of three rules is ten trades each."}
  ],
  "task": "Write your one-page playbook using the template in this lesson, with every number filled in, and date it."
}
---

## One setup, written down

A playbook is a page that another person could trade from. It names the instrument, the setup, the exact entry, stop, target and time exit, the sizing rule, the daily limit, and the conditions under which you do nothing. If any of those requires judgement in the moment, the page is not finished. The reason for the discipline is not aesthetic. It is that only a fully specified rule produces a sample you can compute expectancy on, and only expectancy with an error bar tells you whether to keep going.

This lesson gives you the template, fills it in with the reference rule, and then shows you, on real data, what happens when you choose a rule by picking the best of several backtests.

## The template

Instrument: SPY, regular session, 5-minute bars, session VWAP shown.

Setup: 15-minute opening range (09:30 to 09:44 inclusive; the first three bars).

Entry: the first 5-minute bar after 09:45 that closes above the range high (long) or below the range low (short). Enter at the next bar's open with a bracket order. First signal only; if none by 11:30, no trade.

Stop: the opposite edge of the range, stop-market.

Target: entry plus (entry minus stop) for a long; symmetric for a short. Limit order.

Time exit: 15:55 bar close if neither is hit.

Size: (account × 0.5%) / (entry − stop), rounded down.

Daily limit: one trade. If, in breach, a second trade is taken and lost, close the platform.

Do nothing when: the range is wider than the 14-day ATR (the 1R target would be a full day's move), the session is a scheduled half day, or you have not written the range high and low down before 09:46.

Journal: the fourteen fields of lesson 10, filled before 16:30.

Every line above is a choice. The 11:30 cutoff is a hypothesis from lesson 3's entry-time split (six trades after 10:30, one winner), and the ATR filter would not have triggered in the 60-session sample (the widest range, $4.09 on 2026-07-23, was 59% of the $6.96 14-day ATR measured at the end of the sample). They are written in because a playbook is allowed to contain hypotheses, provided they are stated before the data that will test them arrive.

## Worked example

The 60 sessions from 2026-06-30 to 2026-09-23 split into a first half (30 sessions, 2026-06-30 to 2026-08-11) and a second half (30 sessions, 2026-08-12 to 2026-09-23). Run each of lesson 3's twelve variants on the first half, pick the best, and see what it did on the second half; costs are $0.02 per share round trip throughout.

First half, net $ per share: OR5/1R/opp +10.40; OR5/1R/mid +1.45; OR5/2R/opp +15.68; OR5/2R/mid +15.54; OR15/1R/opp +21.33; OR15/1R/mid +11.27; OR15/2R/opp +8.64; OR15/2R/mid +20.67; OR30/1R/opp +10.89; OR30/1R/mid +13.95; OR30/2R/opp −4.88; OR30/2R/mid +12.55.

Sum = 10.40 + 1.45 + 15.68 + 15.54 + 21.33 + 11.27 + 8.64 + 20.67 + 10.89 + 13.95 − 4.88 + 12.55 = 137.49. Mean = 137.49 / 12 = +$11.46 per share. Eleven of twelve positive.

The winner is OR15/1R/opposite edge at +$21.33 with a 63% win rate. That is, as it happens, the reference rule, chosen for this course before the split was run, on the grounds in lesson 3.

Second half, the same twelve: OR5/1R/opp +2.47; OR5/1R/mid −5.73; OR5/2R/opp +2.93; OR5/2R/mid −2.61; OR15/1R/opp −6.33; OR15/1R/mid −3.94; OR15/2R/opp −9.70; OR15/2R/mid −1.09; OR30/1R/opp −12.73; OR30/1R/mid −11.00; OR30/2R/opp −17.53; OR30/2R/mid −12.54.

Sum = 2.47 − 5.73 + 2.93 − 2.61 − 6.33 − 3.94 − 9.70 − 1.09 − 12.73 − 11.00 − 17.53 − 12.54 = −77.80. Mean = −77.80 / 12 = −$6.48 per share. Three of twelve positive, none by more than $2.93.

The in-sample winner, traded forward: −$6.33 per share, 53% win rate. The out-of-sample winner, OR5/2R/opp at +$2.93, ranked third in sample. The in-sample loser, OR30/2R/opp, was also the out-of-sample loser, which is the one piece of rank order that survived.

Two things happened at once here and it is worth separating them. One is the selection effect: the best of twelve noisy results is biased upward, so it was always going to look worse on new data. Bailey, Borwein, López de Prado and Zhu show that with enough variants the expected out-of-sample performance of the best in-sample one can be negative even when none of them has any edge. The other is a change in the market: every variant did worse in the second half, including ones you would never have picked, so the family of opening-range breakouts as a whole found August and September less hospitable than July. Lesson 3's monthly figures for the reference rule said the same: +$12.50 in July, −$0.78 in August, +$1.01 in September.

You cannot tell from 60 sessions how much of the reversal is each cause. What you can tell is that neither the in-sample ranking nor the in-sample level predicted the second half, and that a trader who funded the +$21.33 rule on 2026-08-12 lost money for six weeks while doing everything right.

## Chart

![Net $ per share for the twelve opening-range variants over the out-of-sample half, 30 sessions from 2026-08-12 to 2026-09-23, after $0.02 per share cost. Nine of twelve are negative; the best is OR5/2R/opposite edge at +$2.93. Source: Yahoo Finance chart API, SPY 5-minute bars.](figures/or-variants-out-of-sample.svg)

## The rules for testing a playbook

Specify before you look. Every number on the page is written before the test runs. Changes after seeing results are allowed, but they restart the count.

Split the data. Choose the rule on one half, evaluate it on the other, and report the second number. If you have only 60 sessions, that is 30 and 30, and you already know from the example above how little 30 proves; it is still the honest figure.

Count your trials. If you tried twelve variants, the best one's t-statistic has to be judged against twelve draws, not one. Harvey, Liu and Zhu argue that, for strategies found by searching, the usual hurdle of t = 2 should be raised toward 3. The reference rule's full-sample t was 1.31 in R (lesson 1). Against twelve trials it is nowhere.

Prefer the rule with a reason. The reference rule was chosen for a mechanism (overnight information resolves in the first quarter hour; the range is the market's first value estimate; the opposite edge is where the thesis is falsified), not because it topped a table. A rule chosen for a mechanism can be wrong, but it cannot be a coincidence, and coincidences are what the splitting produces.

Trade it forward. The only test that cannot be overfit is the one on sessions that had not happened when the rule was written. That is the capstone.

## Table

The twelve variants, first half versus second half, net $ per share after costs.

| Variant (range / target / stop) | First 30 sessions | Win rate | Second 30 sessions | Win rate |
|---|---|---|---|---|
| 5 / 1R / opposite | +10.40 | 60% | +2.47 | 60% |
| 5 / 1R / midpoint | +1.45 | 53% | −5.73 | 43% |
| 5 / 2R / opposite | +15.68 | 47% | +2.93 | 53% |
| 5 / 2R / midpoint | +15.54 | 50% | −2.61 | 37% |
| 15 / 1R / opposite (reference) | +21.33 | 63% | −6.33 | 53% |
| 15 / 1R / midpoint | +11.27 | 60% | −3.94 | 47% |
| 15 / 2R / opposite | +8.64 | 47% | −9.70 | 43% |
| 15 / 2R / midpoint | +20.67 | 50% | −1.09 | 40% |
| 30 / 1R / opposite | +10.89 | 57% | −12.73 | 43% |
| 30 / 1R / midpoint | +13.95 | 63% | −11.00 | 43% |
| 30 / 2R / opposite | −4.88 | 47% | −17.53 | 37% |
| 30 / 2R / midpoint | +12.55 | 50% | −12.54 | 30% |
| Mean of twelve | +11.46 | | −6.48 | |

## What to put on your page

Use the reference rule or a variant of it, with one change at most, and write down why the change should work before you test it. Then log the next 30 sessions as the capstone specifies. If you want to test a second idea (a VWAP filter, an entry-time cutoff, a break-even stop), do it on the same 30 sessions in the journal as a "what if" column, not as a second live rule. One live rule, one sample, one number with an error bar. Everything else in this course exists to make that number honest.

## Sources

- David Bailey, Jonathan Borwein, Marcos López de Prado and Qiji Zhu, "Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance," Notices of the AMS 61(5), 2014: https://www.ams.org/notices/201405/rnoti-p458.pdf
- Campbell Harvey, Yan Liu and Heqing Zhu, "... and the Cross-Section of Expected Returns," Review of Financial Studies 29(1), 2016: https://doi.org/10.1093/rfs/hhv059
- Yahoo Finance chart API, SPY 5-minute bars, 2026-06-30 to 2026-09-23, pulled 2026-09-24: https://finance.yahoo.com/quote/SPY/history/
