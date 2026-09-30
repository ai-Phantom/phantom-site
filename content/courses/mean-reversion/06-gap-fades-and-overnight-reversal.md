---
{
  "title": "Gap Fades and Overnight Reversal",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "From 2015-01-02 to 2026-09-23 SPY rose 273.8%. Splitting every day into the overnight move (prior close to open) and the intraday move (open to close), the overnight part compounded to:", "opts": ["+66.8%", "+124.1%", "+273.8%", "−10%"], "correct": 1, "explain": "Overnight returns compounded to +124.1% and intraday returns to +66.8% (in log terms 0.807 + 0.511 = 1.318, the total). Most of the index's gain accrued while the market was closed."},
    {"q": "On the 144 days when SPY opened more than 1% below the prior close, the average open-to-close return was +0.110%, but the close was back at or above the prior close only:", "opts": ["91% of the time", "52.8% of the time", "13.2% of the time", "Never"], "correct": 2, "explain": "'Gaps get filled' is folklore. A 1%+ gap down filled the same day 13.2% of the time. The fade trade profits from a partial bounce, not from a fill, and only 52.8% of those bounces were positive at all."},
    {"q": "Fading gaps up (shorting at the open after a 1%+ gap higher) over the same period:", "opts": ["Was the better trade", "Lost about 0.14% per trade before costs, because gap-up days kept rising into the close on average", "Broke even", "Filled 13% of the time"], "correct": 1, "explain": "The average open-to-close return on 1%+ gap-up days was +0.138%, and 91.1% of them closed above the prior close. Upside gaps in an uptrending index continued; the asymmetry from lesson 1 again."},
    {"q": "Net of 10 basis points per side, which is a plausible all-in cost for a market order in the first minute of trading, the 1%+ gap-down fade earned:", "opts": ["+0.070% per trade", "+0.010% per trade", "−0.090% per trade", "+0.110% per trade"], "correct": 2, "explain": "+0.110% gross minus 0.20% round trip is −0.090%. At 5 bp per side it is +0.010%; at 2 bp it is +0.070%. The entire result lives inside the cost assumption, which is why the execution at the open matters more than the signal."},
    {"q": "Berkman, Koch, Tuttle and Zhang (2012) found that the opening price systematically:", "opts": ["Understates value in all stocks", "Is inflated by retail attention-driven buying, especially in stocks with high overnight returns, so that buying at the open carries a hidden cost", "Equals the prior close", "Is set by the SEC"], "correct": 1, "explain": "Their title is 'Paying attention: overnight returns and the hidden cost of buying at the open'. The opening auction absorbs a burst of demand that tends to reverse intraday, which is a reason to avoid market orders at 9:30 for any strategy, not just gap fades."}
  ],
  "task": "For the last 40 SPY sessions, list every day the open was more than 0.5% away from the prior close and record the open-to-close return that followed."
}
---

A gap is the difference between today's open and yesterday's close. Fading it means betting the gap partly closes during the session. The folklore says "gaps get filled"; the data says something more specific and less generous. This lesson decomposes SPY's return into overnight and intraday parts, tests gap fades in both directions with real costs, and explains why the opening print is the worst place in the day to be executing a market order.

## Overnight versus intraday

The daily close-to-close return is the product of two pieces: close-to-open (overnight, when the exchange is shut and news accumulates) and open-to-close (intraday, when it is open). In logs they add. Lou, Polk and Skouras (2019) showed that these two pieces behave like different assets: overnight returns carry most of the premium in many stocks and factors, intraday returns carry most of the reversal, and the two are negatively related across firms. Cooper, Cliff and Gulen (2008) found on U.S. index data that essentially all of the equity premium since 1993 accrued overnight.

The SPY numbers for 2015-01-02 to 2026-09-23 (Yahoo Finance daily open and close, `interval=1d`, pulled 2026-09-24; 2,947 sessions) reproduce that: total log return 1.3184 (+273.8%), of which the sum of overnight log returns is 0.8070 (**+124.1%** compounded) and the sum of intraday log returns is 0.5114 (**+66.8%**). Sixty-one percent of the log gain came while the market was closed. The intraday piece is where the reversal lives, because the open is where the overnight flow gets absorbed.

## Worked example

Define gap = open / prior close − 1 and the fade return as close / open − 1 for a gap down (you buy the open, sell the close) or open / close − 1 for a gap up (you short the open, cover the close).

**Two April 2025 sessions.** On 2025-04-04, SPY had closed at 536.70 the day before. It opened at 523.67, a gap of 523.67 / 536.70 − 1 = **−2.43%**. It closed at 505.28: open-to-close 505.28 / 523.67 − 1 = **−3.51%**. The fade lost 3.5% in one session.

On 2025-04-07 the prior close was 505.28 and the open 489.19: gap **−3.18%**. Close 504.38: open-to-close 504.38 / 489.19 − 1 = **+3.11%**. The fade made 3.1%, and the close was still 0.18% below the prior close, so the gap was not filled.

Two consecutive sessions, two gaps of similar size, outcomes of −3.5% and +3.1%. That is the distribution you are trading.

**All gap-down sessions, 2015 to 2026.**

- Gap below −0.5% (388 sessions): average gap −1.09%; average open-to-close **+0.041%**; positive 52.1% of the time; close at or above prior close (gap filled) 18.0%.
- Gap below −1% (144 sessions): average gap −1.77%; open-to-close **+0.110%**, median +0.089%; positive 52.8%; filled **13.2%**.
- Gap below −2% (30 sessions): average gap −3.48%; open-to-close **+0.030%**, median −0.207%; positive 43.3%; filled 10.0%.

The −1% bucket by year: 2018 (7 sessions) +1.460% average, 2020 (28) **−0.258%**, 2022 (33) +0.057%, 2025 (18) +0.203%, 2026 to date (8) +0.327%. Excluding 2020 the average is +0.199% on 116 sessions with a 54.3% hit rate; since 2023 it is +0.243% on 40 sessions at 60.0%. The year with the most gaps was the year the fade lost.

**Gap-up sessions.** Gap above +1% (123 sessions): average gap +1.65%; open-to-close **+0.138%** (so a short loses 0.138% before costs); the close stayed above the prior close 91.1% of the time. Gap above +2% (24): open-to-close −0.125%, the one bucket where the short side made anything, on 24 events.

**Costs.** The gap-down fade below −1%, 144 trades, gross +0.110% per trade:

- at 2 bp per side (a limit order that gets filled a little after the open): 0.110 − 0.04 = **+0.070%**, total +10.1% over eleven years
- at 5 bp per side: **+0.010%**, total +1.5%
- at 10 bp per side (a market order into the opening print): **−0.090%**, total −12.9%

The gross number is the same in all three rows. The trade is profitable or not depending entirely on how you get into it.

## Table

| SPY, 2015-01-02 to 2026-09-23 | Sessions | Avg gap | Avg open-to-close | Open-to-close > 0 | Closed at/above prior close |
|---|---|---|---|---|---|
| All sessions | 2,947 | +0.03% | +0.021% | 53.5% | 54.6% |
| Gap < −0.5% | 388 | −1.09% | +0.041% | 52.1% | 18.0% |
| Gap < −1% | 144 | −1.77% | +0.110% | 52.8% | 13.2% |
| Gap < −2% | 30 | −3.48% | +0.030% | 43.3% | 10.0% |
| Gap > +0.5% | 464 | +0.94% | +0.087% | 61.2% | 85.8% |
| Gap > +1% | 123 | +1.65% | +0.138% | 62.6% | 91.1% |
| Gap > +2% | 24 | +3.04% | −0.125% | 54.2% | 91.7% |

Source: Yahoo Finance daily open and close, computed by the course.

## Why the open is the expensive place

Three things happen at 9:30 that do not happen at 15:59. The opening print is set by an auction that matches all the orders queued overnight, so it reflects a burst of demand or supply that has not yet met the day's liquidity. Berkman, Koch, Tuttle and Zhang (2012) show that this burst is systematically biased upward in stocks that attracted attention overnight, so that opening prices tend to be high and drift down: buying at the open is paying a premium you cannot see on the tape. Second, quoted spreads in the first minutes are wider than at any other time of day; for SPY the difference is small in cents but large relative to the 0.1% you are trying to capture. Third, the official "open" in a daily bar is the auction print, and a market order sent at 9:30:00 executes in the continuous session after it, at a price that on a gap-down morning is moving fast.

That is why the table's gross +0.110% should not be read as a strategy. A trader who can place a limit order a few cents below the auction price and accept that it sometimes does not fill is trading a different, better rule than one who sends a market order, and the difference between them is the entire edge.

The overnight/intraday split gives one more reason to be careful. If SPY's return accrues mostly overnight, then a strategy that is flat overnight and long intraday, which is what a gap fade is, has given up the part of the day where the drift lives. It is a bet on the intraday reversal alone, and the intraday reversal, on average, is +0.02% a session.

## What to keep

The gap-down fade on SPY is a real but tiny reversal, larger after moderate gaps than after extreme ones, negative in the year with the most gaps, and dependent on execution to within a few basis points. The gap-up fade is not a reversal at all. The decomposition of returns into overnight and intraday halves is the more durable lesson: a large part of what looks like reversal in daily data is the open absorbing the night's flow, and it is at the open that the cost of trading is highest. Any reversion rule that enters at the open has to be tested with opening-auction costs, not closing-auction costs.

## Sources

- Lou, D., Polk, C. and Skouras, S. (2019). A tug of war: overnight versus intraday expected returns. *Journal of Financial Economics*, 134(1), 192–213. https://doi.org/10.1016/j.jfineco.2019.03.011
- Berkman, H., Koch, P. D., Tuttle, L. and Zhang, Y. J. (2012). Paying attention: overnight returns and the hidden cost of buying at the open. *Journal of Financial and Quantitative Analysis*, 47(4), 715–741. https://doi.org/10.1017/S0022109012000270
- Cooper, M. J., Cliff, M. T. and Gulen, H. (2008). Return differences between trading and non-trading hours: like night and day. SSRN Working Paper 1004081. https://doi.org/10.2139/ssrn.1004081
- Yahoo Finance, SPY historical data: https://finance.yahoo.com/quote/SPY/history/
