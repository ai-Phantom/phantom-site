---
{
  "title": "What Risk Is to a Portfolio",
  "duration": "16 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "Between 2021-02-12 and 2026-09-23, ARKK's annualised volatility was 46.1% and its maximum drawdown was 80.9%. Which statement about those two numbers is correct?", "opts": ["Volatility describes the typical day; the drawdown describes the path, and a path can destroy capital that the volatility number never hinted at", "They measure the same thing on different scales", "The drawdown is a rounding error of the volatility", "A higher volatility always produces a smaller drawdown"], "correct": 0, "explain": "Volatility is a statement about the dispersion of daily returns. The drawdown is a statement about the sequence of them. ARKK's 46% vol implies a typical day of about 2.9%, which says nothing about 1,377 of 1,409 sessions being spent more than 20% below the high."},
    {"q": "Which of these is NOT one of the three questions a risk framework has to answer?", "opts": ["How much can this book lose?", "How fast can it lose it?", "Will the book and the trader still be here afterwards?", "What is the book's expected return next quarter?"], "correct": 3, "explain": "Expected return is the job of the strategy, not the risk framework. The framework exists to bound size, speed and survivability of loss so that whatever return the strategy has can actually be collected."},
    {"q": "SPY in 2020 had realised volatility of 33.5% and finished the year up 18.3%. SPY in 2022 had volatility of 24.3% and finished down 18.2%. What does that comparison show?", "opts": ["Higher volatility guarantees a loss", "Volatility and the sign of the year's outcome are different things; 2020 was a fast round trip, 2022 a slow grind", "The 2022 number must be a data error", "Volatility is only meaningful in bear markets"], "correct": 1, "explain": "2020 spent 62 sessions more than 10% below its high and recovered within the year. 2022 spent 180 sessions there and did not. The calmer year was the one that lost money, because what matters to a book is the path, not the dispersion."},
    {"q": "TLT lost 34.1% over the same 2021 to 2026 window with only 15.5% annualised volatility. The main lesson for a portfolio manager is that", "opts": ["low-volatility assets cannot lose money", "Treasury ETFs should never be held", "a slow, persistent, one-directional move can do more permanent damage than a violent one, and daily volatility does not measure it", "volatility should be measured monthly instead"], "correct": 2, "explain": "TLT's typical day was small. It simply had far more down days than up days for three years, and spent 1,114 of 1,409 sessions more than 20% below its high. That is path risk, and it is invisible in a daily standard deviation."},
    {"q": "Why does an Expert-level risk framework treat loss of capital, volatility and path as three separate quantities rather than one?", "opts": ["Because regulators require three reports", "Because each one is bounded by a different tool: position size and stops bound loss, vol targeting bounds volatility, and drawdown rules bound the path", "Because volatility is always the largest of the three", "Because they are measured in different currencies"], "correct": 1, "explain": "Each risk has its own control. If you only measure one of the three, the other two run unmanaged, and the unmanaged one is the one that ends careers."}
  ],
  "task": "For your own book, write down the largest loss you would accept over one day, one month and one year, in dollars, and pin it where you trade."
}
---

## The word does three jobs

"Risk" in a portfolio conversation is usually doing three separate jobs at once, and most disagreements about it are really disagreements about which job is meant.

The first meaning is **loss of capital**: money that is gone and will not come back without new money being made. The second is **volatility**: how widely the book's daily value swings around its trend. The third is **path**: the specific sequence of gains and losses the book travels, including how deep it goes below its previous high and how long it stays there.

You already know the arithmetic of a single drawdown from *Building Your First Portfolio*. This course starts from the observation that the three quantities are only loosely related, that each has its own instrument, and that a risk framework which measures only one of them leaves the other two running unsupervised. That is why the syllabus has separate lessons on exposure, volatility, Value at Risk, correlation, concentration and drawdown control: each is the control for a different one of the three.

## Loss of capital

Loss of capital is the only one of the three that is irreversible, and so it is the one the framework exists to bound. It comes in two forms. Realised loss is a closed trade that lost money. Unrealised loss is an open position marked below cost, which is not yet permanent but becomes permanent the moment you are forced to close it, whether by a margin call, by a risk rule, or by your own inability to sit through it.

The distinction matters because the tools differ. Realised loss is bounded by position size and by the stop, if there is one. Unrealised loss is bounded by the same two things plus one more: the funding that lets you hold the position through the mark. A position that would have recovered but was liquidated by the broker at the low is a realised loss caused by a funding failure, not by a bad idea. Lesson 10 is about that.

## Volatility

Volatility is the standard deviation of returns, usually daily returns scaled to a year by multiplying by the square root of 252. It measures dispersion, not direction. A book that goes up 1% every day and a book that goes down 1% every day have the same volatility, zero, and completely different fates.

Volatility is nonetheless the most useful of the three for day-to-day control, for two reasons. It is the one that can be measured from a short window, so it can be re-estimated every day. And it is the one that clusters: a high-vol day tends to be followed by high-vol days, so today's estimate carries information about tomorrow. Lesson 3 shows the evidence and builds a vol-targeting rule on it.

What volatility cannot do is tell you how much you can lose. That takes a distributional assumption or a historical sample, and lesson 4 shows what happens when either is wrong.

## Path

Path is the shape of the equity curve. Two books with identical total return and identical volatility can have different paths, and the path is what determines whether you were margin-called, whether your rules cut exposure at the bottom, and whether you were still trading when the recovery came.

Path risk has its own measures: maximum drawdown, time under water, and the number of sessions spent below some threshold. It has its own control, the drawdown rule, which lesson 7 tests against real crashes. And it is the one most often ignored, because on any single day the path is invisible. You only see it looking back.

## The three questions

A risk framework, whatever its size, has to answer three questions every day, in writing:

1. **How much can this book lose?** In dollars, at a stated confidence, over a stated horizon, and also in the case the confidence is wrong.
2. **How fast can it lose it?** A 20% loss over two years and a 20% loss over two weeks are different events. The first is survivable with patience; the second may trigger calls, rules and panic before patience can be applied.
3. **Will the book and the trader still be here afterwards?** Capital, funding, broker access, and the psychological ability to re-enter after the loss.

Every later lesson feeds one of these three. Exposure and VaR feed the first. Volatility and correlation feed the second. Drawdown control, leverage and operational risk feed the third. The risk report in lesson 12 is simply the three answers, dated.

## Worked example

To make the three quantities concrete, take five liquid ETFs over a single window: 2021-02-12, the day ARKK set its all-time high, to 2026-09-23. Daily adjusted closes from Yahoo Finance, 1,409 trading days. Volatility is the standard deviation of daily returns times the square root of 252. Maximum drawdown is the largest fall from a running high. "Sessions more than 20% under water" counts days where the close was more than 20% below the prior peak.

**SPY**: total return +111.1%. Annualised volatility 16.7%. Maximum drawdown −24.5% (low on 2022-10-12). Worst single day −5.9% (2025-04-04). Sessions more than 20% below the high: 37 of 1,409.

**QQQ**: +127.8%. Volatility 22.5%. Maximum drawdown −35.1% (2022-11-03). Worst day −6.2% (2025-04-04). Sessions under −20%: 245.

**ARKK**: −41.7%. Volatility 46.1%. Maximum drawdown −80.9% (2022-12-28). Worst day −10.1% (2022-05-11). Sessions under −20%: 1,377 of 1,409, meaning the fund spent 98% of the window more than a fifth below its high.

**GLD**: +130.2%. Volatility 18.3%. Maximum drawdown −26.4% (2026-07-16). Worst day −10.3% (2026-01-30). Sessions under −20%: 56.

**TLT**: −34.1%. Volatility 15.5%. Maximum drawdown −43.7% (2023-10-19). Worst day −3.4% (2022-03-02). Sessions under −20%: 1,114.

Now read the three risks off the table. Loss of capital: ARKK and TLT lost it; the other three made money. Volatility: ARKK was the wildest, TLT the calmest. Path: ARKK and TLT both spent most of the window deep under water, despite having the highest and the lowest volatility in the set.

The pair that teaches the most is TLT against GLD. Similar volatility, 15.5% versus 18.3%. Similar worst drawdown order of magnitude, −43.7% versus −26.4%. Opposite outcomes, −34.1% versus +130.2%. The daily standard deviation of TLT was small; it simply had a persistently negative drift for three years and never recovered. Nothing in a volatility number would have told you that a "low-risk" bond ETF was the one that would lose a third of your capital.

The second pair is SPY in two different years. Calendar 2020: volatility 33.5%, maximum drawdown −33.7%, total return +18.3%, 62 sessions spent more than 10% below the high. Calendar 2022: volatility 24.3%, maximum drawdown −24.5%, total return −18.2%, 180 sessions spent more than 10% below the high. The year with lower volatility and a shallower drawdown was the one that lost money, because the path was a grind rather than a round trip.

## Table

| Instrument, 2021-02-12 to 2026-09-23 | Total return | Ann. vol | Max drawdown | Worst day | Sessions >20% under water |
|---|---|---|---|---|---|
| SPY | +111.1% | 16.7% | −24.5% | −5.9% | 37 / 1,409 |
| QQQ | +127.8% | 22.5% | −35.1% | −6.2% | 245 / 1,409 |
| ARKK | −41.7% | 46.1% | −80.9% | −10.1% | 1,377 / 1,409 |
| GLD | +130.2% | 18.3% | −26.4% | −10.3% | 56 / 1,409 |
| TLT | −34.1% | 15.5% | −43.7% | −3.4% | 1,114 / 1,409 |

Source: Yahoo Finance daily adjusted closes, pulled 2026-09-24. Volatility is the sample standard deviation of daily returns × √252.

## What this means for the rest of the course

The three risks need three instruments, and the instruments are not interchangeable.

Loss of capital is bounded by exposure limits (lesson 2), concentration caps (lesson 6) and the funding structure (lesson 10). Volatility is bounded by vol targeting (lesson 3) and monitored by VaR (lesson 4), with the caveat that both assume correlations that lesson 5 shows to be unstable. Path is bounded by drawdown rules (lesson 7) and, at the extreme, by tail hedges (lesson 9).

The gate stack in lesson 8 sits in front of all of it: nothing gets into the book that has not shown, on data it was not fitted to, that it adds return without adding a risk the rest of the book already carries. And lesson 11 covers the risks that no statistic captures, because they come from the broker, the code and the keyboard rather than from the market.

The framework is written down, and the numbers in it are computed rather than felt. That is the single distinction between a book that has a risk framework and a book that has a trader who says he is careful. By the capstone you will have built one for a stated ten-position book: exposures, beta, two flavours of VaR, a correlation stress, concentration checks, and three rules that say what happens when a number crosses a line.

## Sources

- Markowitz, H. (1952). "Portfolio Selection." *Journal of Finance* 7(1). https://doi.org/10.1111/j.1540-6261.1952.tb01525.x
- Artzner, P., Delbaen, F., Eber, J.-M. and Heath, D. (1999). "Coherent Measures of Risk." *Mathematical Finance* 9(3). https://doi.org/10.1111/1467-9965.00068
- Yahoo Finance historical data, SPY, QQQ, ARKK, GLD, TLT. https://finance.yahoo.com/quote/ARKK/history/
