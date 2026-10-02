---
{
  "title": "ATR-Based Sizing for Volatile Names",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The true range for a day is:", "opts": ["High minus low only", "The largest of: high minus low, high minus prior close, and prior close minus low", "Close minus open", "The 14-day average of closes"], "correct": 1, "explain": "True range includes the gap from the prior close so that a day which opens far from yesterday's close registers its full movement."},
    {"q": "On 2025-06-25 NVDA's true range was 6.55 and the prior day's 14-day ATR was 3.83. Using Wilder's smoothing, the new ATR is:", "opts": ["6.55", "(3.83 × 13 + 6.55) / 14 = 4.02", "3.83", "(3.83 + 6.55) / 2 = 5.19"], "correct": 1, "explain": "Wilder's ATR keeps 13/14 of yesterday's value and adds 1/14 of today's true range, so one big day moves it a little rather than a lot."},
    {"q": "With 1% risk and a stop 2 ATRs below entry, a stock whose ATR is 4% of its price gets a position equal to what share of the account?", "opts": ["50%", "12.5%", "4%", "100%"], "correct": 1, "explain": "Position value = risk fraction / (stop multiple × ATR fraction) = 1% / (2 × 4%) = 12.5%. On 2026-03-31 AVGO, with an ATR of 4.19%, worked out to 11.8% after rounding down to whole shares."},
    {"q": "On the same date JNJ had an ATR of 1.64% of price. Its ATR-sized position came to 30.3% of the account, versus 11.8% for AVGO. This means:", "opts": ["JNJ is the better trade", "The rule puts about 2.6 times as many dollars into the calm stock so that both positions carry the same expected daily movement in dollars", "The rule is broken and needs a cap", "AVGO should be bought with options instead"], "correct": 1, "explain": "ATR sizing equalises dollar volatility across positions. A separate concentration cap is still sensible, but the disparity itself is the rule working."},
    {"q": "Portfolio heat is:", "opts": ["The account's temperature", "The sum of the open risk (entry minus stop, times shares) across all positions, expressed as a share of equity", "The number of positions", "The largest single position"], "correct": 1, "explain": "If five positions each risk 1%, the book's heat is 5%. Capping heat limits what a simultaneous failure of every open trade can cost."}
  ],
  "task": "Compute the 14-day ATR by hand for one stock on your list using the last 15 daily bars from Yahoo Finance, and express it as a percentage of the current close."
}
---

Two stocks with the same dollar position are not the same bet. A $10,000 position in a stock that moves 4% a day carries about twice the daily swing of a $10,000 position in one that moves 2%. The Average True Range is the standard way to measure that, and sizing by it is the standard way to make every position in the book carry roughly the same risk. Lesson 6 gave you the technical stop; this lesson gives you the volatility check on it and the arithmetic that turns both into a share count.

## The Average True Range

The true range for one session is the largest of three distances: today's high minus today's low, today's high minus yesterday's close, and yesterday's close minus today's low. The second and third terms exist so that a gap counts. A stock that closes at 100, opens at 108 and drifts to 109 has a high-minus-low of 1 and a true range of 9.

The Average True Range is the 14-day average of true ranges. J. Welles Wilder, who introduced it in 1978, used a smoothing that keeps 13/14 of yesterday's ATR and adds 1/14 of today's true range. That makes the ATR slow to jump on one big day and slow to decay after it, which is what you want from a number that decides position size.

What matters most for sizing is the ATR as a fraction of price. A $700 stock with a $26 ATR and a $96 stock with a $2.80 ATR are moving 3.7% and 2.9% a day respectively; the dollar figures tell you nothing until you divide.

## Sizing by ATR

The rule has three inputs: the account risk per trade (this course uses 1%), the stop distance in ATRs (2 is the default), and the ATR itself.

shares = (account × 1%) / (2 × ATR)

Because 2 × ATR is the stop distance, this is the same formula as lesson 6 with the technical stop replaced by a volatility stop. Multiply both sides by the price and divide by the account:

position value as a share of the account = 1% / (2 × ATR%)

A stock with an ATR of 2% of price gets 1% / 4% = 25% of the account. A stock at 4% gets 12.5%. A stock at 1% gets 50%, and that is where you add a concentration cap, because no single name should be half the book regardless of how calm it looks today. A cap of 20 to 25% of equity per position is common. The chart below shows the curve and where two real stocks fall on it.

The academic literature uses the same idea at the portfolio level. Moskowitz, Ooi and Pedersen (2012) scale every position in their time-series momentum portfolio by the inverse of its ex-ante volatility so that each contributes equally to risk. Barroso and Santa-Clara (2015) show that scaling the cross-sectional momentum strategy by its own recent realised volatility roughly doubles its Sharpe ratio and removes most of the crash risk, because the crashes happen when volatility is already high and the scaling has already cut exposure. You are doing the same thing one stock at a time.

## Worked example

Data: Yahoo Finance daily bars via the chart API, pulled 2026-09-24. The account is $50,000, risk per trade 1% ($500), stop 2 ATRs.

**Computing the ATR.** NVDA on 2025-06-25: high 154.45, low 149.26, prior close 147.90. The three candidates are 154.45 − 149.26 = 5.19, 154.45 − 147.90 = 6.55, and 149.26 − 147.90 = 1.36. True range = **6.55**. The 14-day ATR at the close of 2025-06-24 was 3.83. Wilder's update: (3.83 × 13 + 6.55) / 14 = (49.79 + 6.55) / 14 = 56.34 / 14 = **4.02**. One breakout day with a true range of 6.55 lifted the ATR by 0.19. The sizing in lesson 6 used that 4.02: stop = 155.98 − 2 × 4.02 = 147.94, shares = 500 / 8.04 = 62.

**Sizing the universe.** On 2026-03-31, the ranking date from lesson 4, here is every stock's close, 14-day ATR, ATR as a share of price, 2-ATR stop distance, the share count from $500 / (2 × ATR) rounded down, and the position that implies:

| Ticker | Close | ATR | ATR % | 2 × ATR | Shares | Position | % of $50k |
|---|---|---|---|---|---|---|---|
| AVGO | 309.51 | 12.96 | 4.19% | 25.91 | 19 | $5,881 | 11.8% |
| TSLA | 371.75 | 13.92 | 3.74% | 27.84 | 17 | $6,320 | 12.6% |
| CAT | 708.46 | 26.10 | 3.68% | 52.19 | 9 | $6,376 | 12.8% |
| META | 572.13 | 20.98 | 3.67% | 41.95 | 11 | $6,293 | 12.6% |
| NVDA | 174.40 | 5.84 | 3.35% | 11.67 | 42 | $7,325 | 14.6% |
| UNH | 270.59 | 8.29 | 3.06% | 16.58 | 30 | $8,118 | 16.2% |
| LLY | 919.77 | 27.22 | 2.96% | 54.45 | 9 | $8,278 | 16.6% |
| NFLX | 96.15 | 2.80 | 2.91% | 5.60 | 89 | $8,557 | 17.1% |
| AMZN | 208.27 | 5.96 | 2.86% | 11.92 | 41 | $8,539 | 17.1% |
| GOOGL | 287.56 | 8.13 | 2.83% | 16.26 | 30 | $8,627 | 17.3% |
| HD | 328.89 | 8.96 | 2.72% | 17.92 | 27 | $8,880 | 17.8% |
| XOM | 169.66 | 4.58 | 2.70% | 9.15 | 54 | $9,162 | 18.3% |
| JPM | 294.16 | 7.41 | 2.52% | 14.81 | 33 | $9,707 | 19.4% |
| MSFT | 370.17 | 9.12 | 2.46% | 18.24 | 27 | $9,995 | 20.0% |
| AAPL | 253.79 | 5.83 | 2.30% | 11.65 | 42 | $10,659 | 21.3% |
| WMT | 124.28 | 2.74 | 2.20% | 5.47 | 91 | $11,309 | 22.6% |
| V | 302.24 | 6.56 | 2.17% | 13.13 | 38 | $11,485 | 23.0% |
| PG | 144.44 | 2.83 | 1.96% | 5.66 | 88 | $12,711 | 25.4% |
| COST | 996.43 | 17.94 | 1.80% | 35.88 | 13 | $12,954 | 25.9% |
| JNJ | 244.44 | 4.02 | 1.64% | 8.04 | 62 | $15,155 | 30.3% |

Read the two ends. AVGO: 500 / 25.91 = 19.3, so 19 shares, 19 × 309.51 = $5,881. JNJ: 500 / 8.04 = 62.2, so 62 shares, 62 × 244.44 = $15,155. The rule puts 2.6 times as many dollars into JNJ as into AVGO, and the point is that both positions are expected to move about the same number of dollars on a typical day: 19 × 12.96 = $246 for AVGO, 62 × 4.02 = $249 for JNJ. Equal dollar volatility is the whole idea. With a 25% concentration cap, JNJ, COST and PG would be trimmed to $12,500, and their dollar risk would fall below $500 as a consequence; the cap is a deliberate under-risking of calm names in exchange for not owning a third of the book in one ticker.

Note the rounding. Whole shares rounded down mean the realised risk is slightly under $500 every time; on CAT it is 9 × 52.19 = $470. Rounding up would breach the risk limit on every trade by a little. Down is the only defensible direction.

## Chart

![Position value as a share of the account against ATR as a share of price, for 1% risk and a stop 2 ATRs below entry. JNJ (ATR 1.64% on 2026-03-31) and AVGO (4.19%) are marked; the curve is 1% divided by twice the ATR percentage. Source: ATRs computed from Yahoo Finance daily bars.](figures/atr-sizing-curve.svg)

## When the ATR stop and the technical stop disagree

Lesson 6 chose the stop from the chart. This lesson chose it from volatility. When they agree, as on the NVDA breakout, you are done. When they disagree, the rule is: use the wider of the two for placement and size to it. A technical level inside one ATR of the entry will be hit by noise; a 2-ATR stop that sits above the breakout level is not defending anything the chart cares about. Taking the wider one costs you shares and buys you a stop that is both technically meaningful and outside the daily range.

## Portfolio heat

Sizing one trade is not sizing a book. Add up the open risk across every position, entry minus stop times shares, and divide by equity. That number is the portfolio's heat: what you lose if every stop is hit tomorrow at its price. Five positions at 1% is 5% heat. Set a maximum, 5 or 6% is typical for a swing account, and stop opening trades when you reach it, however good the next setup looks. The heat cap is what makes a run of losers survivable, and runs of losers are normal: a system that wins 44% of the time, as the one in lesson 12 does, will produce five consecutive losses about one time in eighteen, five-trade sequences.

## Sources

- Moskowitz, T. J., Ooi, Y. H. and Pedersen, L. H. (2012). Time series momentum. *Journal of Financial Economics*, 104(2), 228–250. https://doi.org/10.1016/j.jfineco.2011.11.003
- Barroso, P. and Santa-Clara, P. (2015). Momentum has its moments. *Journal of Financial Economics*, 116(1), 111–120. https://doi.org/10.1016/j.jfineco.2014.11.010
- Yahoo Finance historical data, NVDA: https://finance.yahoo.com/quote/NVDA/history/
