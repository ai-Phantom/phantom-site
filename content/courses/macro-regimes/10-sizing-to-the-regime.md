---
{
  "title": "Sizing to the Regime: Vol Targeting, Exposure Caps in High-Vol States, and the Cost of Being Wrong",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A 15% volatility target with exposure capped at 1.0 (no leverage), on SPY from 2000 to 2026 with 5 basis points per unit of turnover, returned 7.56% a year at 13.3% volatility with a -43.6% drawdown, against 8.27%, 19.3% and -55.2% for buy-and-hold. What did the rule buy and what did it cost?", "opts": ["It beat buy-and-hold", "It cut volatility by a third and the drawdown by a fifth, at a cost of 0.7 points of annual return; its return per unit of risk (0.42 against 0.33) was higher", "It did nothing", "It doubled the drawdown"], "correct": 1, "explain": "Vol targeting is a risk-shaping tool. It rarely beats buy-and-hold in raw return on an asset with a positive drift; it makes the ride smoother and the worst case smaller."},
    {"q": "Why does the vol-targeted rule still have a -43.6% drawdown if it cuts exposure when volatility rises?", "opts": ["Because the exposure is set from trailing realised volatility, which is low on the day a crash starts; the rule cuts after the first losses, not before, so it takes most of the initial fall and then misses part of the rebound", "The rule is broken", "Because SPY fell 43.6% in one day", "Because leverage was used"], "correct": 0, "explain": "The minimum exposure of 0.16 was reached on 2008-10-28, three weeks into the worst of the crash. A trailing filter is always late; sizing reduces the damage from the second half of a decline, not the first."},
    {"q": "A rule that goes to zero exposure whenever the VIX closed above 30 returned 5.01% a year with a -56.9% drawdown, worse than buy-and-hold on both counts. Why?", "opts": ["The VIX is a bad indicator", "The costs were too high", "The rule should have used 25", "SPY's cumulative return on the 622 sessions following a VIX close above 30 was +114.7%: the exits happened after the losses and the re-entries after the rebounds, so the rule sold low and bought high 5.6 times a year"], "correct": 3, "explain": "A binary exit on an acute-stress reading is the worst-performing rule in the lesson. Halving exposure above 30 instead gave 6.84% and -49.8%: still worse than buy-and-hold in return, better in drawdown, and much better than the full exit."},
    {"q": "Vol targeting with a 1.5x cap returned 8.33% against 7.56% for the 1.0x cap, with 15.4% volatility against 13.3% and 6.3x annual turnover against 2.6x. Which is the honest way to describe the leveraged version?", "opts": ["Leverage is free return", "It should always be used", "It recovers buy-and-hold's return at lower volatility, but the extra 0.8 points cost 2.4x the turnover and require a margin facility, a financing rate above T-bills, and the acceptance that a gap down on a leveraged day is a larger loss than the model shows", "It is riskier than buy-and-hold"], "correct": 2, "explain": "The backtest charges 5 basis points per unit of turnover and assumes financing at the T-bill rate. Neither holds for a retail account. The 1.5x line is a ceiling on what the idea can do, not a forecast."},
    {"q": "The cost of being wrong in this lesson refers to:", "opts": ["The return foregone when a regime rule reduces exposure and the feared decline does not come, or comes and reverses before the rule re-enters: in 2020, halving exposure above VIX 30 from 2020-02-27 to 2020-05-08 gave up half of the +31.2% rebound from the March 23 low", "Losses from bad trades", "Commissions", "The cost of computing the VIX"], "correct": 0, "explain": "Every regime rule is insurance. The premium is paid in the episodes where the rule is wrong, and those episodes are the majority. The decision is whether the insurance is worth its premium, and the lesson gives you the numbers to decide."}
  ],
  "task": "Compute the exposure a 15% volatility target would set today from SPY's trailing 21-session realised volatility (15% divided by realised, capped at 1.0) and write it down."
}
---

## The principle

The previous lessons established one fact above all others: the states differ far more in the width of their return distributions than in their location. S4's SPY volatility is 3.4 times S1's; its mean is not reliably different in a way you could trade. A sizing rule that responds to width therefore has something to work with, and one that responds to location does not.

Sizing to width means holding a position whose expected dollar volatility is roughly constant across regimes. In a 12% volatility state you hold a full position; in a 40% state you hold a third of one. The bet is not that you know which way the market goes; it is that a loss of a given size in dollars should have the same probability tomorrow as it had last month. The mechanism is called volatility targeting, and the empirical support for it is the clustering result of lesson 6: tomorrow's magnitude is forecastable from today's, so a position sized on today's magnitude is a position sized on a forecast that works.

## Vol targeting, mechanically

Choose a target annualised volatility, say 15%. Each day, estimate realised volatility from the trailing 21 sessions. Set exposure equal to the target divided by the estimate, capped at some maximum (1.0 if you do not use leverage). Hold the rest in T-bills. Rebalance daily or when the exposure changes by more than some band.

The worked example runs it on SPY from 2000 to 2026 with a 5-basis-point cost per unit of turnover. Target 15%, cap 1.0: 7.56% a year, 13.3% volatility, -43.6% drawdown, 2.6x annual turnover, against buy-and-hold's 8.27%, 19.3% and -55.2%. The rule gave up 0.7 points of return for a third less volatility and a fifth less drawdown. Return per unit of risk (excess return over T-bills divided by volatility) rose from 0.33 to 0.42. Target 10%, cap 1.0: 6.44%, 10.3%, -31.4%, ratio 0.44. Target 15%, cap 1.5: 8.33%, 15.4%, -45.8%, ratio 0.42, at 6.3x turnover.

Two features of these results are general. First, vol targeting on an asset with positive drift does not beat buy-and-hold in raw return unless it is allowed to lever, and the levered version's extra return depends on financing at the T-bill rate and on a cost model that does not include margin calls. Second, the drawdown is still large, because the rule sizes on trailing volatility, which is low on the day a crash begins. The minimum exposure in the sample, 0.16, was reached on 2008-10-28, three weeks into the worst of the decline. The rule takes most of the first leg and then reduces exposure for the rest.

## Exposure caps in high-vol states

A cruder alternative is a cap tied to the state: full exposure in calm, a fixed fraction in stress. The worked example tries three. Halve exposure when the VIX closed above 30: 6.84%, 15.8%, -49.8%. Halve it above 25: 6.66%, 14.3%, -45.4%. Go to zero above 30: 5.01%, 14.4%, -56.9%, a drawdown worse than buy-and-hold.

The last result is the one to remember. SPY's cumulative return over the 622 sessions that followed a VIX close above 30 was +114.7%, at 42% annualised volatility. A binary exit at 30 sells after the losses, sits out the rebound, buys back after it, and does so 5.6 times a year on average. It has the worst return and the worst drawdown of any rule in the lesson. Halving instead of exiting is not a compromise; it is the difference between a rule that reduces damage and one that manufactures it.

## The cost of being wrong

Every regime rule is insurance against a decline continuing. The premium is what it gives up when the decline reverses before the rule re-enters, and reversals are the common case. In 2020 the VIX first closed above 30 on 2020-02-27 (at 39.2, with SPY already 12% off its high) and first closed below 30 on 2020-05-08. SPY's return between those dates was -1.1%; from the 2020-03-23 low to 2020-05-08 it was +31.2%. A rule that halved exposure above 30 was half-exposed for the whole rebound and gave up roughly 15 points of it. In 2025 the VIX crossed 30 on 2025-04-03 and was back below on 2025-04-17, ten sessions; SPY moved -1.9% between the two dates and the rule paid two switches for nothing.

The insurance is worth its premium only if the tail it protects against is one you cannot survive. If a -55% drawdown would end your trading, the 15% target's -43.6% or the 10% target's -31.4% is the price of staying in the game and the 0.7 to 1.8 points of annual return is the premium. If you could sit through -55% without changing behaviour, the premium buys you nothing but a smoother chart.

## Writing a policy

A sizing policy is a table: for each state, a target volatility or an exposure cap, a maximum, and a rule for moving between them. The capstone asks you to write one. The principles this lesson supports: size on the width of the state's distribution, not its mean; prefer continuous adjustment (vol targeting) to binary switches; use the state as a cap on the vol-targeted exposure rather than as a signal of its own; and write down, before you run it, what the policy will cost in the episodes where it is wrong, because those will be most of them.

## Worked example

Data: SPY adjusted close and `^VIX` close from the Yahoo Finance chart API, `^IRX` for the T-bill rate, current session dropped, aligned on common dates; test window 2000-01-03 to 2026-09-29, 6,719 return days.

Realised volatility on day t: the sample standard deviation of the 21 daily returns ending on t, times sqrt(252). Exposure for day t+1 under a vol target V with cap C: min(C, V / realised(t)). Exposure under a VIX cap: 1.0 if VIX(t) is at or below the threshold, otherwise the stated fraction. Strategy return on day t+1: exposure times SPY's return plus (1 - exposure) times the T-bill daily rate (prior session's `^IRX` divided by 100 and by 252, floored at zero), minus 5 basis points times the absolute change in exposure from the prior day. Annualised return, volatility and drawdown as in lesson 7. The ratio is annualised return minus the mean T-bill rate, divided by annualised volatility. Turnover is the sum of absolute exposure changes per year.

Results (annualised return, volatility, drawdown, ratio, turnover per year): buy-and-hold +8.27%, 19.26%, -55.2%, 0.33, 0. Vol target 10%, cap 1.0: +6.44%, 10.27%, -31.4%, 0.44, 4.2x. Vol target 10%, cap 1.5: +6.30%, 10.98%, -31.4%, 0.40, 7.1x. Vol target 15%, cap 1.0: +7.56%, 13.33%, -43.6%, 0.42, 2.6x. Vol target 15%, cap 1.5: +8.33%, 15.41%, -45.8%, 0.42, 6.3x. VIX above 30 to 50% exposure: +6.84%, 15.77%, -49.8%, 0.31, 2.8x. VIX above 30 to 0%: +5.01%, 14.43%, -56.9%, 0.21, 5.6x. VIX above 25 to 50%: +6.66%, 14.26%, -45.4%, 0.33, 5.1x.

The 15% target with cap 1.0 held a mean exposure of 0.87 and was at the cap on 57% of days; its minimum exposure was 0.16 on 2008-10-28, when trailing realised volatility was 94.5%, the sample maximum. The sample minimum of realised volatility was 3.4% on 2017-10-11, when the uncapped exposure would have been 4.4x.

Cost of being wrong, 2020: exposure under the VIX-30 half rule was 0.5 from the session after 2020-02-27 to the session after 2020-05-08. SPY's return 2020-02-27 to 2020-05-08: -1.1%. SPY's return 2020-03-23 to 2020-05-08: +31.2%. The half-exposed rule captured about half of the latter.

## Table

| Rule (SPY, 2000-01-03 to 2026-09-29, 5 bp per unit turnover) | Ann. return | Ann. vol | Max drawdown | (Return - T-bill) / vol | Turnover / yr |
|---|---|---|---|---|---|
| Buy and hold | +8.27% | 19.26% | -55.2% | 0.33 | 0.0x |
| Vol target 10%, cap 1.0 | +6.44% | 10.27% | -31.4% | 0.44 | 4.2x |
| Vol target 10%, cap 1.5 | +6.30% | 10.98% | -31.4% | 0.40 | 7.1x |
| Vol target 15%, cap 1.0 | +7.56% | 13.33% | -43.6% | 0.42 | 2.6x |
| Vol target 15%, cap 1.5 | +8.33% | 15.41% | -45.8% | 0.42 | 6.3x |
| VIX > 30: exposure 0.5 | +6.84% | 15.77% | -49.8% | 0.31 | 2.8x |
| VIX > 30: exposure 0.0 | +5.01% | 14.43% | -56.9% | 0.21 | 5.6x |
| VIX > 25: exposure 0.5 | +6.66% | 14.26% | -45.4% | 0.33 | 5.1x |

No rule in the table beats buy-and-hold on raw return without leverage. Every vol-targeting rule beats it on return per unit of risk; the binary VIX rules match it at best (0.33 for the halve-above-25 rule) and the full exit does worse on every measure. Split the sample and the picture is less tidy. In 2000-2012 buy-and-hold returned 1.60% a year with a -55.2% drawdown, and the 10% vol target returned 2.41% with -31.4%: sizing won on return too, because that period held two bear markets. In 2013-2026 buy-and-hold returned 14.97% (ratio 0.79), the 15% vol target 13.17% (0.90), and the halve-above-25 rule 13.21% (0.86), so in the second half the cruder rule nearly matched vol targeting while the full exit at 30 still trailed (0.71). The robust result is the last one: reducing beats exiting in both halves. Continuous beats binary in the full sample and the first half, by a smaller margin in the second.

## Sources

- Moreira, A. and Muir, T. (2017), "Volatility-Managed Portfolios", Journal of Finance 72(4), https://doi.org/10.1111/jofi.12513
- Harvey, C. R., Hoyle, E., Korgaonkar, R., Rattray, S., Sargaison, M. and van Hemert, O. (2018), "The Impact of Volatility Targeting", Journal of Portfolio Management 45(1); SSRN: https://ssrn.com/abstract=3175538
- Cboe, VIX Index methodology: https://www.cboe.com/tradable_products/vix/vix_index_methodology/
- Yahoo Finance historical data for SPY, ^VIX and ^IRX: https://finance.yahoo.com/quote/SPY/history/
