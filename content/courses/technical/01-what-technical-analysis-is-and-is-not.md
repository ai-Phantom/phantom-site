---
{
  "title": "What Technical Analysis Is (and Is Not)",
  "duration": "14 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "Technical analysis, stated precisely, is:", "opts": ["A method for predicting the exact future price of a security", "The study of past price and volume to make conditional statements about future price behaviour", "The analysis of a company's earnings and balance sheet", "A way of removing risk from trading"], "correct": 1, "explain": "Technical analysis works only with market-generated data (price, volume, and derived series) and produces probabilistic, not exact, statements."},
    {"q": "Which finding is the most common in the academic literature on simple technical rules since about 1990?", "opts": ["Rules that worked in early samples tend to work less or not at all in later, out-of-sample data", "Every published rule has been confirmed on new data", "Technical rules only work on cryptocurrencies", "Academic studies have never examined technical rules"], "correct": 0, "explain": "Park and Irwin (2007) and Sullivan, Timmermann and White (1999) both document that early evidence of profitability weakens sharply once later data and data-snooping corrections are applied."},
    {"q": "In the worked example, the day-after-a-down-day average return on SPY was larger than the day-after-an-up-day return. What is the correct reading of that result?", "opts": ["A guaranteed profitable strategy", "A small, in-sample statistical tendency that has not yet been tested for costs, stability or out-of-sample validity", "Proof that markets are inefficient", "Evidence that up days are dangerous"], "correct": 1, "explain": "A single in-sample conditional average is a hypothesis, not an edge. The rest of the course is about what it takes to move from one to the other."},
    {"q": "Which of these is NOT a claim technical analysis can support?", "opts": ["Prices sometimes trend for longer than a random walk would suggest", "Round-number and prior-high levels attract orders", "Chart patterns determine a company's intrinsic value", "Volume carries information beyond price"], "correct": 2, "explain": "Intrinsic value is a fundamental-analysis concept. Charts describe what buyers and sellers did, not what a business is worth."},
    {"q": "What does 'data snooping' mean in the context of testing trading rules?", "opts": ["Downloading data without permission", "Testing many rules on the same data and reporting only the one that worked, which inflates the apparent edge", "Looking at a chart before the market opens", "Using data from a competitor"], "correct": 1, "explain": "If you try 1,000 rules on the same history, some will look excellent by chance. White (2000) and Sullivan et al. (1999) built formal tests for this."}
  ],
  "task": "Download ten years of daily SPY data from Yahoo Finance or Nasdaq, open it in a spreadsheet, and reproduce the four conditional averages in the worked example before starting Lesson 2."
}
---

Technical analysis is the study of market-generated data, mostly price and volume, to make conditional statements about what price is more or less likely to do next. That is the whole definition. It is not forecasting in the sense of naming a future price, and it is not a description of what a business is worth. It is closer to a set of measurement habits applied to a noisy time series.

This lesson sets the terms for the rest of the course. You will learn what the discipline actually claims, what the academic evidence says about those claims, and how to tell the difference between a pattern and an edge. Every later lesson assumes you have internalised that distinction.

## What it is

Every bar on a chart is a compressed record of transactions. The open, high, low, close and volume of a day are facts: they happened, they were reported by the exchange, and they cannot be revised. Technical analysis takes those facts and asks three kinds of question:

1. **Descriptive.** Where is price relative to where it has been? Is it above or below a recent range, a moving average, a prior high? These questions have exact answers and no forecasting content at all.
2. **Conditional.** Given that price is in a particular state, what has it tended to do next, historically? This is where indicators, patterns and rules live. The answer is always a distribution, never a single number.
3. **Operational.** Given a conditional tendency, where do you enter, where do you exit if wrong, where do you exit if right, and how much do you risk? This is the part that turns an observation into a trade.

Most of what is sold as technical analysis skips from the descriptive layer to the operational layer and never checks the conditional one. A chart with a trend line and an arrow is a description plus an opinion. This course insists on the middle step.

## What it is not

It is not fundamental analysis. Earnings, revenue, margins, balance sheets and management quality are inputs to a valuation. A chart contains none of them directly. It may contain the market's reaction to them, and that reaction is real information, but the chart cannot tell you whether a company is cheap.

It is not prediction. A support level is not a floor. A moving-average crossover is not a signal that price will rise. Each is a statement of the form "in the past, when X was true, Y followed more often than the base rate." The base rate matters as much as the pattern, and you will compute it in every worked example in this course.

It is not a way of removing risk. If you carry a position, you carry risk. Technical tools may help you size and locate that risk; they do not eliminate it.

## The case for it

Three strands of evidence give technical analysis a legitimate footing.

**Order clustering.** Osler (2000, 2003) used actual customer order books at a large currency dealer and showed that stop-loss and take-profit orders cluster at round numbers and at prior highs and lows. When orders cluster, price reacts at those levels more often than chance. This is a mechanism, not a mystical property of the chart, and it is the best-supported explanation for why support and resistance can exist at all. You will meet it again in Lesson 3.

**Momentum and trend persistence.** Jegadeesh and Titman (1993) documented that stocks which outperformed over the prior 3 to 12 months tended to continue outperforming for the next 3 to 12 months. Moskowitz, Ooi and Pedersen (2012) found the same "time-series momentum" in 58 futures markets. These are among the most replicated results in empirical finance and they are, at heart, technical: they use nothing but past price.

**Non-random patterns in the data.** Lo, Mamaysky and Wang (2000) applied a smoothing algorithm to decades of US stock data and found that several classic chart patterns (head-and-shoulders, double tops and bottoms) occur more often than they would in a random series, and that the distribution of returns after them differs from the unconditional distribution. Note the careful wording: different, not necessarily profitable.

## The case against it

**The original evidence has faded.** Brock, Lakonishok and LeBaron (1992) reported that simple moving-average and trading-range breakout rules earned meaningful returns on the Dow Jones Industrial Average from 1897 to 1986. Sullivan, Timmermann and White (1999) re-examined those rules with a bootstrap that corrects for the fact that thousands of rules had been tried on the same data, and found that the best rule's performance in the original sample survived the correction, but the same rules earned nothing out of sample from 1987 to 1996. Park and Irwin (2007), surveying 95 modern studies, found that a majority reported positive results, but that most of those had problems with data snooping, transaction costs, or the risk adjustment, and that results were consistently weaker in stock markets than in currencies or futures.

**Weak-form efficiency.** Fama (1970) framed the efficient markets hypothesis. Its weak form says that past prices are already reflected in current prices, so no rule based on them alone can earn a risk-adjusted excess return. The evidence above shows the weak form is not exactly true, but it is close enough to true that any edge from price alone is small, unstable, and fragile to costs.

**Indicators are late by construction.** Every moving average, oscillator and band is a function of past prices. It cannot contain information that the last price does not already contain. What it can do is filter noise and enforce discipline. That is a real but modest benefit.

## Worked example

Take the simplest possible technical claim: "yesterday's direction tells you something about today's." Here is what ten years of SPY data say. Source: Yahoo Finance historical daily data for SPY, unadjusted closes, 26 September 2016 to 23 September 2026 (2,512 closes, 2,511 daily returns).

Define an up day as a close higher than the prior close.

- Number of days: 2,511
- Up days: 1,382, so the unconditional probability of an up day is 1,382 / 2,511 = **55.0%**
- Days following an up day: 1,382. Of those, 54.4% were up.
- Days following a down day: 1,129. Of those, 55.8% were up.
- Average return on the day after an up day: **+0.031%**
- Average return on the day after a down day: **+0.089%**
- Lag-1 autocorrelation of daily returns: **−0.13**

The arithmetic for the last item: autocorrelation is the correlation between today's return and yesterday's return across all 2,510 pairs. A value of −0.13 means a small tendency for a positive day to be followed by a slightly weaker day and a negative day by a slightly stronger one.

Now read it honestly. The difference between +0.031% and +0.089% per day is 0.058 percentage points. That is real in this sample and it agrees with a well-documented short-term reversal effect. But it is one comparison on one instrument with no cost model, no risk adjustment and no out-of-sample check. If you had tested twenty such one-day rules, you would expect one of them to look about this good by luck. That is the difference between a pattern and an edge, and this course will not let you forget it.

## Table

| Claim | Best evidence for | Best evidence against | Verdict for a beginner |
|---|---|---|---|
| Prices trend more than a random walk | Jegadeesh & Titman (1993); Moskowitz et al. (2012) | Effect is at 3–12 month horizons, not days | Real, but slow and crash-prone |
| Support and resistance levels matter | Osler (2000, 2003) order-book data | Effect is strongest in FX and intraday | Real mechanism, modest edge |
| Simple indicator rules beat buy-and-hold | Brock et al. (1992) | Sullivan et al. (1999); Park & Irwin (2007) | Faded after publication |
| Chart patterns predict direction | Lo et al. (2000): patterns are non-random | Same paper: no claim of profitability | Informative, not a strategy |
| Volume adds information beyond price | Karpoff (1987) survey | Effect is about volatility, not direction | Real, but read it carefully |

## How to use this course

Each lesson gives you one tool, one worked example with real numbers you can reproduce, one table or chart, and the primary sources. You will not be told that any tool "works". You will be shown how to measure whether it worked on a given sample and what the sample cannot tell you. By the capstone you will run that measurement yourself on twenty setups.

Two habits to start now. First, always compute the base rate before you compute the conditional rate. Second, write down what you expect to find before you look at the data. If you cannot say what result would make you abandon the idea, you are not testing it.

## Sources

- Fama, E. F. (1970). "Efficient Capital Markets: A Review of Theory and Empirical Work." *Journal of Finance*, 25(2). https://www.jstor.org/stable/2325486
- Brock, W., Lakonishok, J., & LeBaron, B. (1992). "Simple Technical Trading Rules and the Stochastic Properties of Stock Returns." *Journal of Finance*, 47(5). https://www.jstor.org/stable/2328994
- Sullivan, R., Timmermann, A., & White, H. (1999). "Data-Snooping, Technical Trading Rule Performance, and the Bootstrap." *Journal of Finance*, 54(5). https://doi.org/10.1111/0022-1082.00163
- Park, C.-H., & Irwin, S. H. (2007). "What Do We Know About the Profitability of Technical Analysis?" *Journal of Economic Surveys*, 21(4). https://doi.org/10.1111/j.1467-6419.2007.00519.x
