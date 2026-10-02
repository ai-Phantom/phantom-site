---
{
  "title": "Trend Regimes: The 200-Day SMA as a Regime Filter, Tested Honestly on SPY",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "From 1993-11-15 to 2026-09-29, holding SPY only when the prior close was above its 200-day SMA (T-bills otherwise) returned 9.15% a year against 10.88% for buy-and-hold, with a maximum drawdown of -22.1% against -55.2%. Which statement is correct?", "opts": ["The filter beat buy-and-hold", "The filter is worthless because it returned less", "The filter doubled returns", "The filter lost 1.7 points of annual return and cut the worst drawdown by more than half; whether that trade is worth it depends on what the drawdown costs you, not on the return alone"], "correct": 3, "explain": "The filter is a drawdown-reduction tool that pays for itself in return. It lost to buy-and-hold in 1994-2007 and in 2014-2026 and beat it in 2008-2013. Its Sharpe-type ratio was higher (0.55 against 0.45) because volatility fell more than return."},
    {"q": "SPY's annualised return on sessions BELOW the 200-day was +9.48%, nearly as high as the +11.30% on sessions above. Why does the filter still reduce risk?", "opts": ["Because the below-line sessions carried 29.9% annualised volatility and a -51.7% drawdown against 13.8% and -27.5% above the line: the below state has similar mean and more than double the dispersion", "It does not; the numbers show the filter is pointless", "Because the below-line return is negative once costs are included", "Because T-bills yield more than 9%"], "correct": 0, "explain": "The below-line state contains both the crashes and the violent rebounds. Its mean is not the problem; its width is. A regime filter is a tool for managing dispersion, and this one does that."},
    {"q": "Of the 107 long trades the filter generated, 60 lasted five sessions or fewer and every one of them lost, for a combined -78.5%. The 19 trades that lasted more than 100 sessions all won, for +426.7%. What does this tell you about the strategy's return distribution?", "opts": ["It is a coin flip", "The whipsaws can be filtered out", "The whole return comes from a handful of long trades and the cost of finding them is dozens of small whipsaw losses; you cannot keep the winners without paying for the losers", "Most trades win"], "correct": 2, "explain": "The 60 immediate losers are the price of being in position when a trend starts. Filtering them out after the fact is the look-ahead error; any rule that avoids them in advance will also miss some of the 19."},
    {"q": "Adding a cost of 5 basis points per switch reduced the filter's annual return from 9.15% to 8.79%. Why is the cost so large for a strategy that trades so rarely?", "opts": ["The cost model is wrong", "214 switches over 33 years is about 6.5 a year, and 214 times 5 basis points is 10.7 percentage points of cumulative return, about a third of a point a year; the whipsaws drive the count", "The strategy trades every day", "Costs are always negligible"], "correct": 1, "explain": "The trade count is what the whipsaws cost you a second time. At 10 basis points the return falls to 8.44% and the drawdown widens to -25.0%."},
    {"q": "The filter's return over 2014-2026 was 10.69% a year against 13.71% for buy-and-hold. The largest reason is:", "opts": ["The period contained sharp declines with fast recoveries (December 2018, March 2020, spring 2025), in which the filter exited after the fall and re-entered after the rise: 64 switches in twelve years", "The 200-day stopped working", "The filter was never in the market", "T-bill yields were high"], "correct": 0, "explain": "A trailing average is late by construction. In a V-shaped decline it sells near the low and buys back higher. Lesson 11 measures exactly how late, in sessions and in percent."}
  ],
  "task": "Compute SPY's 200-session simple moving average from the adjusted closes for the latest session and record whether the close is above or below it, and by what percentage."
}
---

## The simplest regime variable

The 200-day simple moving average is the average of the last 200 daily closes. It has been used as a trend definition for at least seventy years, it can be computed by hand, and it embodies one idea: a market above its long average is in an up-trend state and one below it is in a down-trend state. Its virtue is that it has no parameters to fit beyond the 200, and that number is so widely used that changing it looks like data mining. Its vice is that it is late by construction: it is an average of the past 200 sessions, so it cannot turn until price has moved far enough for long enough to drag it.

This lesson tests it the way you would test any rule. State observed at the close of day t; return earned on day t+1; T-bills when out. No optimisation, no look-ahead, costs added afterwards, and the result reported in full, including where the rule lost to buy-and-hold, which is most of the time.

## What the filter does to the distribution

Read the worked example's first four lines together. Sessions above the 200-day returned 11.30% annualised with 13.8% volatility and a worst drawdown of -27.5%. Sessions below it returned 9.48% annualised with 29.9% volatility and a worst drawdown of -51.7%. The mean return is not very different between the two states; the width of the distribution is more than doubled below the line.

That is the whole result and it is worth stating plainly. The 200-day is not a return filter. Below-line sessions are where the crashes live, but they are also where the rebounds live, and the rebounds are large enough that the below-line mean is positive and close to the above-line mean. What the line separates is dispersion. If you are indifferent to dispersion, the filter costs you 1.7 points of return a year. If a -55% drawdown would end your trading, the filter converts it into -22% for that price.

## Whipsaws are the cost, not a bug

The filter switched sides 214 times between 1993-11-15 and 2026-09-29, an average of 6.5 switches a year, producing 107 round-trip long trades. Sixty of those trades lasted five sessions or fewer and every one of them lost, for a combined -78.5% in summed simple returns. Eighteen lasted six to twenty sessions; one won. Ten lasted 21 to 100 sessions; five won. Nineteen lasted more than 100 sessions; all nineteen won, for a combined +426.7%. The best single trade ran from 1996-07-31 to 1998-08-27 for +68.3%.

The structure is the structure of every trend rule: a long tail of small immediate losses that pay for a short list of large wins. You cannot have the nineteen without the sixty, because on the day each of the sixty was opened it was indistinguishable from the day each of the nineteen was opened. Any refinement that removes whipsaws (a percentage band around the line, a confirmation delay) removes some of the good entries too and delays the rest; it changes the trade-off, it does not abolish it.

Costs make the whipsaws bite twice. At 5 basis points per switch (a generous assumption for SPY), 214 switches cost 10.7 percentage points of cumulative return and the annualised figure falls from 9.15% to 8.79%; at 10 basis points it is 8.44%, and the maximum drawdown widens to -25.0% because the costs land inside the drawdowns.

## By sub-period

The filter's relative performance depends on what kind of decline the period contained. In 1994-2007 (119 switches) it returned 8.13% against 10.42% for buy-and-hold, with a -22.1% drawdown against -47.5%: the 2000-2002 bear was slow enough for the filter to catch, but the 1990s bull was choppy enough to whipsaw it repeatedly. In 2008-2013 (31 switches) it returned 8.35% against 6.24%, with -20.5% against -52.3%: the one period in which it beat buy-and-hold on both counts, because the 2008 decline was long and the line got out early. In 2014-2026 (64 switches) it returned 10.69% against 13.71%, with -18.1% against -33.7%: three V-shaped declines (December 2018, March 2020, spring 2025) each cost it an exit near the low and a re-entry well above it.

The honest summary is that a 200-day filter on SPY has been a way to trade about 1.7 points of annual return for roughly half the drawdown and two thirds of the volatility, with the trade-off worst in fast recoveries and best in slow bear markets. Whether that is a good deal is a question about you, not about the rule.

## Worked example

Data: SPY daily bars from the Yahoo Finance chart API (8,475 rows, 1993-01-29 to 2026-09-30, current session dropped), dividend-adjusted close for returns and for the average; `^IRX` (13-week T-bill discount rate, Yahoo, 9,223 rows from 1990-01-02) for the cash return, applied as the prior session's rate divided by 100 divided by 252 per day, floored at zero.

The 200-session SMA on day t is the mean of adjusted closes on days t-199 through t. The first session with a full window is 1993-11-15. The signal on day t is the close on day t-1 compared with the SMA on day t-1; if the close is above, the strategy earns SPY's return on day t, otherwise the T-bill return. That is 8,253 return days from 1993-11-16 to 2026-09-29.

Annualised return is the compounded growth raised to 252 over the number of days, minus one. Annualised volatility is the standard deviation of daily returns times sqrt(252). Maximum drawdown is the largest peak-to-trough fall in the compounded equity.

Sessions above the line: 6,381 (77.3%), annualised +11.30%, volatility 13.80%, drawdown -27.5%. Below: 1,872 (22.7%), +9.48%, 29.93%, -51.7%. Strategy: +9.15%, 12.14%, -22.1%. Buy-and-hold: +10.88%, 18.72%, -55.2%. T-bills: +2.49%, 0.13%, 0.0%.

Excess return over T-bills divided by volatility: strategy (9.15 - 2.49) / 12.14 = 0.55; buy-and-hold (10.88 - 2.49) / 18.72 = 0.45.

Switch count: 214 sign changes of the signal. Round-trip long trades: 107, entered on the session after the signal turns positive and exited on the session after it turns negative, return measured on adjusted closes. By length: 5 sessions or fewer, 60 trades, 0 winners, mean -1.31%, sum -78.5%; 6 to 20 sessions, 18 trades, 1 winner, mean -1.24%, sum -22.2%; 21 to 100 sessions, 10 trades, 5 winners, mean -0.57%, sum -5.7%; more than 100 sessions, 19 trades, 19 winners, mean +22.46%, sum +426.7%. Sum of all 107 trades: +320.2%.

Costs: subtracting 5 basis points from the strategy's return on each switch day gives +8.79% annualised, -23.6% drawdown; 10 basis points gives +8.44%, -25.0%.

## Chart

![SPY's unadjusted close and its 200-session SMA on the last session of each month, January 2015 to September 2026, Yahoo Finance daily data; the annotated points mark the late-2018, February-to-April 2020, 2022 and March-to-April 2025 periods in which month-end closes sat below the line.](figures/spy-200-day.svg)

The chart is at monthly resolution, which hides the whipsaws (a session that closes a few cents below the line and back above the next day does not show) but makes the regime episodes since 2015 visible: two short (late 2015 to early 2016, and late 2018 to early 2019), one violent and short (2020), one long (2022, with month-end closes below the line in nine of twelve months), one short (spring 2025), and a single month-end below in March 2026. The filter's return in each of those is a function of the episode's shape: it earns in the long ones and pays in the short ones.

## Sources

- Yahoo Finance historical data for SPY and ^IRX: https://finance.yahoo.com/quote/SPY/history/ and https://finance.yahoo.com/quote/%5EIRX/history/
- Faber, M. T. (2007), "A Quantitative Approach to Tactical Asset Allocation", Journal of Wealth Management 9(4); SSRN: https://ssrn.com/abstract=962461
- Brock, W., Lakonishok, J. and LeBaron, B. (1992), "Simple Technical Trading Rules and the Stochastic Properties of Stock Returns", Journal of Finance 47(5), https://doi.org/10.1111/j.1540-6261.1992.tb04681.x
- Moskowitz, T. J., Ooi, Y. H. and Pedersen, L. H. (2012), "Time Series Momentum", Journal of Financial Economics 104(2), https://doi.org/10.1016/j.jfineco.2011.11.003
