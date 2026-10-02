---
{
  "title": "Benchmarks the Stack Must Include: Cash and Buy-and-Hold",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A swing rule on one stock cleared nine promotion gates: 185 out-of-sample trades, 65% wins, Sharpe 1.24, max drawdown 2.5%, 99.7th percentile against random entry. Buy-and-hold over the same window returned +1,524% against the rule's equivalent of +236% on the same notional. What was missing from the nine gates?", "opts": ["A comparison against holding the asset; the rule captured 15% of buy-and-hold and its flattering Sharpe and drawdown came from sitting in cash 90% of the time", "A longer window", "A smaller stop", "A second stock"], "correct": 0, "explain": "The signal was real, about $23,000 of timing alpha at the 99.7th percentile. It was also a worse way to own the stock than owning the stock. Nothing in the stack asked."},
    {"q": "The RSI(2) rule on SPY 2010-2025 sits at the 95th percentile against random entry, returned +119% against SPY's +702%, and has a Sharpe versus cash of 0.37 against SPY's 0.76. It was in the market about 20% of sessions. Which reading is right?", "opts": ["It passes: the percentile is what matters", "It should be levered five times to match exposure", "The timing has some information and the rule is a worse way to own SPY than owning SPY; it fails the buy-and-hold gate at 0.49x the asset's Sharpe", "It beats cash, so it passes"], "correct": 2, "explain": "The random-entry and buy-and-hold checks answer different questions and both are needed. Leverage is a separate decision with its own costs and is not the benchmark's job."},
    {"q": "Why does the cash gate charge the T-bill rate over the holding period of each trade rather than annualising?", "opts": ["Annualising is harder to compute", "Because T-bills pay quarterly", "It does not matter", "Because a three-session hold forgoes 3/252 of the annual rate, about 0.045% at 3.75%; annualising first overcharges the trade by roughly 84 times"], "correct": 3, "explain": "The rule's return per trade is compared with what the same capital would have earned in bills for the same days. 3.751% x 3/252 = 0.0447%."},
    {"q": "One rule cleared the buy-and-hold Sharpe check at 1.09x and was rejected only by the random-entry check at the 51st percentile. Another cleared random entry at the 99.7th percentile and captured 15% of buy-and-hold. What follows?", "opts": ["Use whichever check is stricter", "The two checks are independent; build both, because each one alone would have promoted a rule the other rejects", "Random entry is sufficient", "Buy-and-hold is sufficient"], "correct": 1, "explain": "The first rule's whole return was exposure to a rising market; the second's timing was real but its exposure was not. Neither check sees what the other does."},
    {"q": "A stack introduced the cash and benchmark gates without a default risk-free rate: absent an explicit rate, both skip by name. Why refuse a default?", "opts": ["No reliable rate exists", "Rates change too often", "A hardcoded rate would silently re-verdict every study already run; a by-name skip keeps old verdicts unchanged and makes the missing input visible", "Defaults are bad style"], "correct": 2, "explain": "A missing input must be a reported skip, never a silent pass or a silent change. The same rule governs a missing second data source in D6."}
  ],
  "task": "Compute, for your rule's window, the growth of one dollar for the rule, for buy-and-hold in the same instrument and for 13-week T-bills, and write all three on one line above your equity curve."
}
---

## Nine gates and no standing bar

The research notes (Phantom Traders, 2026, internal) record the first strategy to clear all nine of an earlier promotion stack, dated 2026-08-19: a swing-momentum rule on one large technology stock, daily bars. It had 185 out-of-sample trades, a 65.4% win rate, a profit factor of 2.22, an annualised Sharpe of 1.24, a maximum drawdown of 2.5%, no degradation between search and holdout, and a parameter plateau with full neighbour support. The data was verified clean through all four of the stock's splits. Against a random-entry null matched on count, hold length and size, its $37,218 sat at the 99.7th percentile (random median $14,203, 95th percentile $27,363). The signal was real; it carried about $23,000 of timing alpha.

Buy-and-hold over the same window returned +1,524%, or $239,965 on matched notional against the rule's $37,218. The rule captured 15% of simply owning the stock. Its flattering Sharpe and its 2.5% drawdown came largely from sitting in cash about 90% of the time. No gate in the stack compared the rule against holding the asset.

Two gates were added the same day and a third followed: versus buy-and-hold over the same window, versus cash over each trade's hold, and the random-entry null already in place. Applied to the five pairs that had been promoted, three became one:

| pair | percentile vs random | Sharpe vs buy-and-hold | capture of buy-and-hold | verdict |
|---|---|---|---|---|
| AAPL | 99.5th | 2.46x | 17% | promote |
| QQQ | 51.1st | 1.09x | 13% | reject: a coin flip |
| SPY | 88.1st | 1.67x | 9% | reject |
| NVDA | 16.6th | 0.77x | 0% | reject: worse than random |
| TSLA | 52.3rd | 0.47x | 8% | reject |

The QQQ row is the instructive one. It had cleared all nine original gates at the 51st percentile of random entry, which is to say its entire profit was exposure to a rising index. It also passed the buy-and-hold Sharpe check at 1.09x and was caught only by the random-entry check. The two checks are independent, and each one alone would have promoted a rule the other rejects. Build both.

## The cash gate

A rule that is flat most of the time is competing with T-bills for the days it is flat and with the asset for the days it is long. The cash gate, G2 in the stack, asks whether each trade earned more than the same capital would have earned in bills over the same days. The rate is charged over the hold, not over a year: a three-session hold at 3.751% forgoes 3.751% × 3 / 252 = 0.0447%. Annualising the trade's return first and comparing that with 3.751% would overcharge it by a factor of about 84, and would reject every short-hold rule that has ever existed.

The benchmark gate, G7, compares Sharpe ratios computed against cash on both sides, which is what makes a rule that is flat 85% of the time comparable to an asset that never is. On the rule's side, the days out of the market earn the bill rate and contribute zero excess return; on the asset's side, every day contributes. The rule's lower volatility from sitting in cash is therefore not a virtue the ratio rewards; it is a smaller numerator and a smaller denominator together, and the ratio says whether the timing bought anything.

The stack has no default rate. Absent an explicit annual rate and a bars-per-year figure, both gates skip by name and say so, like the null without a null. A hardcoded default would have silently re-verdicted every study already run. The notes record that the arithmetic for these two gates had been hand-written three times in four days and was wrong three times on the way; one tested implementation is the point.

## What the two gates catch

Turn-of-month on SPY passed nine gates and then scored 0.43 against cash and 0.38 against SPY on the Sharpe comparison, which is why it was sized at half. An RSI(2) book passed on seven of sixteen names and then scored 1.04 on the names it had been developed on and 0.03 on names it had never seen. Both times the stack said pass and these two gates changed the conclusion. Their placement matters: between the geometry gate and the null, because all three are questions about tradeability, and a rule that cannot beat T-bills has no business consuming a null.

## Worked example

RSI(2) mean reversion on SPY daily bars from Yahoo Finance, 2010-01-04 to 2025-12-31, fetched 2026-09-30, dividend-adjusted. Enter at the close when RSI(2) is below 10; exit at the first close above the 5-day simple moving average; one position at a time; 5 bps per side. Cash is the 13-week T-bill discount yield (Yahoo ^IRX), divided by 252 for a daily rate and earned on every day the rule is out of the market. Buy-and-hold is SPY's adjusted close.

The rule: 173 trades, mean net +0.3456% per trade, 71.1% winners, mean hold 3.57 sessions, in the market on about 20% of sessions. Against a random-entry null matched on the 173 holds and charged the same 10 bps, the null mean is +0.0986% and the rule sits at the 95.0th percentile, exactly on the bar.

Growth of one dollar from 2010-01-04 to 2025-12-31: the rule 2.188 (+118.8%), SPY buy-and-hold 8.020 (+702.0%), T-bills 1.245 (+24.5%). Compound annual growth over 15.97 years: the rule 5.02%, SPY 13.93%, bills 1.38%. Capture: 118.8 / 702.0 = 17%.

Sharpe versus cash, daily excess returns annualised by the square root of 252: the rule 0.37, SPY 0.76. The ratio is 0.37 / 0.76 = 0.49x, against a gate of 1.0x. Maximum drawdown: the rule −29.9% (it bought the dips of March 2020 and rode the last of them down), SPY −33.7%. The rule's drawdown is not much smaller than the asset's, because a dip-buying rule is by construction long during dips; what it gave up was the 80% of sessions in which SPY compounded without it.

The cash gate per trade: the mean bill yield over the window was 1.37%, so a 3.57-session hold forgoes 1.37% × 3.57 / 252 = 0.0194%. The rule's +0.3456% net per trade clears that by 0.326 percentage points; G2 passes. The benchmark gate: 0.49x of the asset's Sharpe against cash; G7 fails. The random-entry gate: 95.0th percentile; G3 passes on the bar, though Lesson 5's rule about seeds applies and Lesson 8 will show what the per-era view says.

The verdict on this rule, written the way the stack writes it: the timing has some information (95th), the trade beats bills (+0.33 points per trade), and the rule is a worse way to own SPY than owning SPY (0.49x). Rejected at G7.

![Line chart of the growth of one dollar at month-ends from January 2010 to December 2025 for three series: the RSI(2) rule on SPY at 5 bps per side, ending at 2.19; SPY buy-and-hold, ending at 8.02; and 13-week T-bills, ending at 1.24. Source: Yahoo Finance SPY and ^IRX daily data, fetched 2026-09-30.](figures/rsi2-vs-buy-and-hold-and-cash.svg)

## Table

The three benchmarks, what each one controls for, and what it would have missed on its own.

| Benchmark | Controls for | Passes | Would miss |
|---|---|---|---|
| Random entry, matched on count, hold, direction, filter | Drift over the time held; the timing question | The AAPL swing rule (99.7th); RSI(2) on SPY (95th) | AAPL's 15% capture: real timing inside a bad exposure |
| Cash over the hold (G2) | Whether the trade beat bills for its own days | RSI(2) on SPY by 0.33 points per trade | A rule with timing that beats bills and still trails the asset |
| Buy-and-hold, Sharpe vs cash on both sides (G7) | Whether the exposure was worth having at all | AAPL swing rule at 2.46x | QQQ swing rule at 1.09x, whose timing was a coin flip |

Every rule in this course is scored against all three, and the verdict line prints all three numbers. A rule that passes one and fails another has told you exactly what it is, which is more than a rule that only ever met one bar.

## Sources

- Sharpe, W. F. (1994). "The Sharpe Ratio." Journal of Portfolio Management 21(1). https://doi.org/10.3905/jpm.1994.409501
- Fama, E. F., French, K. R. (2010). "Luck versus Skill in the Cross-Section of Mutual Fund Returns." Journal of Finance 65(5). https://doi.org/10.1111/j.1540-6261.2010.01598.x
- Yahoo Finance, 13-week Treasury bill yield, ^IRX (the cash series): https://finance.yahoo.com/quote/%5EIRX/
- Yahoo Finance, SPY historical data: https://finance.yahoo.com/quote/SPY/history/
