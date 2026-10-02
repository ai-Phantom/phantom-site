---
{"title": "How the Bots Learn Their Weights", "cat": "bots", "tag": "Bots & Signals", "emoji": "📡", "excerpt": "Two separate learners set Phantom's signal weights: a weekly two-year replay of classic signals and a 60-day learner fed by the bots' own paper trades.", "date": "2026-10-02", "read": "6 min", "status": "published"}
---

Every Phantom signal has base points. Before those points count, they are multiplied by a weight. A weight of 1.0 is neutral. Higher means the signal has earned more trust. Lower means less.

Those weights are not typed in by hand. They come from two separate learners. The two learners look at different data, grade different signals and use different formulas.

If you remember one thing from this post, make it this: **the weekly replay does not grade the eight ported TradingView indicators.** Their weights come only from the live learner, or default to 1.0.

## Learner one: the weekly replay

Once a week, on Sunday, a replay runs over two years of daily price bars for the watchlist.

It grades 12 classic signals. These are six signal families, each with a bullish and a bearish version:

- RSI
- Bollinger bands
- MACD
- MACD histogram
- Volume surge
- EMA trend

### The win rule

For each time a signal fired in those two years, the replay asks one question. Did the stock move at least 1% in the signal's direction within 5 days?

If yes, it is a win. If no, it is a loss. That gives each signal a win rate.

Notice what this measures. It is the stock's move, not an option's profit. A stock can move 1% in your favor while an option still loses value to time decay or a falling implied volatility. The replay tells you whether a signal pointed the right way. It does not tell you whether an option trade on it would have paid.

### The weight formula

The win rate is compared to a baseline. The weight is:

**weight = 1 + (win rate − baseline) / 20**

Both rates are in percentage points. The result is clamped between 0.1 and 2.0.

An illustrative example, not a real result. Say the baseline is 50% and a signal wins 58% of the time. Then the weight is 1 + 8 / 20 = 1.4. If it wins only 45% of the time, the weight is 1 + (−5) / 20 = 0.75.

### Guardrails

The replay has rules to avoid trusting noise:

- **Minimum sample.** A signal needs at least 30 occurrences before it gets a weight.
- **Clusters.** Combinations of three or more signals are graded too. They need at least 15 occurrences.
- **Stability.** A weight is marked stable only if the signal beat the baseline in both halves of the two-year window. One lucky year is not enough.

### What it produces

The replay writes three things:

1. An overall weight per signal.
2. Context weights per signal, split by market regime, VIX bucket and time of day.
3. Signal clusters, the combinations that work better together.

Clusters feed the cluster boost in scoring. A combination earns a boost only if its edge is at least 2 percentage points, it has at least 15 samples, and it is stable. The boost is capped at 1.30x and never penalizes.

## Learner two: the live learner

The second learner looks at something different. It reads the bots' **own closed paper trades** from the last 60 days.

Here a win is a paper trade that closed as a win, not a 1% stock move. That makes it closer to what an option trade actually experienced, including entry price, stop and trail.

Its formula is gentler:

**weight = 1 + (win rate − 50) / 40**

An illustrative example: a 60% win rate gives 1 + 10 / 40 = 1.25. A 40% win rate gives 0.75.

### Auto-apply versus human approval

The live learner does not get free rein. If a new weight lands between 0.5 and 1.5, it applies automatically. Anything outside that band is staged for a human to approve or reject.

That keeps one bad stretch of trades from swinging a signal to an extreme on its own.

## Which learner weights which signal

This is the part most people get wrong.

| Signal group | Weekly replay | Live learner |
|---|---|---|
| 12 classic signals (RSI, Bollinger, MACD, MACD histogram, volume surge, EMA trend) | Yes | Yes |
| 8 ported indicators (Gaps, UT Bot, EMA stack, Zero Lag, Trend Reversal Probability, QQE MOD, MACD_X, SMC) | No | Yes |
| Any signal with no learned weight yet | n/a | n/a (it uses 1.0) |

So when you hear "two years of replay data," it applies to the classic signals. The ported indicators like UT Bot or QQE MOD are judged on the bots' own recent paper trades. Until there is enough of that history, they score at their base points.

## How a weight is picked at scan time

When Phantom scores a setup, it looks up each signal's weight in this order:

1. **Context weights.** If weights exist for the current regime, VIX bucket or time of day, Phantom combines them with a geometric mean.
2. **Overall weight.** If there are no context weights, it uses the signal's overall weight.
3. **Default.** If neither exists, the weight is 1.0.

The regimes are uptrend, downtrend, choppy, stretched overbought and stretched oversold. The VIX buckets are low (below 15), normal (15 to 25) and high (above 25). Time of day is open, midday or close.

## Learning can switch things off

Learning is not only about boosting. It also removes signals that do not hold up.

A Donchian channel breakout used to score. Testing showed it was anti-predictive, so it is now off by default. Separately, a signal with measured negative edge can be suppressed at entry.

## The limits, stated plainly

Neither learner is a crystal ball.

- The replay measures stock direction over 5 days, not option profit.
- The live learner uses 60 days of paper trades, which can be a small sample for a rarely firing signal.
- Paper fills are not real fills.
- Two years is one slice of market history.

The weights are a way to lean toward signals with a better record and away from ones with a worse record. They are not a forecast.

## What this means for you

When a signal posts, its score already reflects these weights. A signal with a strong record carries more points. A weak one carries fewer.

But the weights move. A signal that scored well last month may count for less next month. That is the system working, not breaking.

## Sources

- Phantom Traders bot code (October 2026)
- Options Industry Council (OCC), [options education](https://www.optionseducation.org/)

*Educational content, not financial advice. Signals are paper-traded.*
