---
{
  "title": "Drawdown Control: Rules and What They Cost",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "SPY fell 55.2% from 2007-10-09 to 2009-03-09 and did not regain the peak until 2012-08-16, 1,256 days after the low. The gain required from the low was", "opts": ["55.2%", "82.3%", "123.2%", "155.2%"], "correct": 2, "explain": "1 ÷ (1 − 0.552) − 1 = 1.232. A 55% loss needs a 123% gain. The asymmetry is the whole reason drawdown control exists: the recovery cost grows faster than the loss."},
    {"q": "The tested rule cut SPY exposure to 50% at a 10% drawdown from the 252-day peak and to zero at 20%. In 2020 it went flat on 03-12, seven sessions before the low, and returned +1.8% for the year against +17.2% for buy-and-hold. What went wrong?", "opts": ["The rule was too slow to cut", "The 252-day peak was wrong", "Buy-and-hold is always better", "The crash was faster than the rule's thresholds could track, so it cut at the bottom and re-entered late; a rule tuned to slow bears is whipsawed by fast crashes"], "correct": 3, "explain": "From the 02-19 high to −20% took 16 sessions; from −20% to the low took 7 more. The rule sold most of its exposure inside the worst three weeks and bought it back in May at prices 20% higher than where it sold."},
    {"q": "The same rule in 2008-2009 returned −7.1% against −19.4% for buy-and-hold, with a −14.2% worst drawdown against −51.9%. Why did it work there and not in 2020?", "opts": ["2008 was a slow bear: the −20% trigger fired on 2008-07-14, two months before Lehman, so the rule was flat through the worst of it; the cost was seven whipsaws in early 2008 and a late re-entry in August 2009", "Luck", "The thresholds were different", "Volatility was lower in 2008"], "correct": 0, "explain": "A drawdown rule is a trend-following overlay. It pays when the fall is long enough for the trigger to fire well before the bottom, and costs money when the fall and the recovery both happen inside the trigger's reaction time."},
    {"q": "Across 2018, 2020, 2022-23 and 2025 the rule trailed buy-and-hold every time, by 1.2 to 15.5 points, while cutting the worst drawdown by about 3 to 14 points. What is the honest description of what a drawdown rule buys?", "opts": ["Higher returns", "A shallower worst case, paid for with lower average returns in the years the market recovers on its own, which is most years", "Nothing", "Protection only in 2008"], "correct": 1, "explain": "The rule is insurance. In four of five test windows it cost a premium and paid a partial claim on the drawdown; in one it paid out fully. Whether that is worth it depends on the funding and psychology constraints of lesson 1's third question, not on the average."},
    {"q": "Which design change most reduces whipsaw in a drawdown rule?", "opts": ["Tighter thresholds", "Using a 20-day peak instead of 252-day", "Measuring drawdown weekly", "A re-entry condition with hysteresis, for example a new 50-day high, so exposure is not restored the day after it is cut; and thresholds measured against the book's own vol so a 10% move in a 40%-vol regime is not treated like a 10% move in a 12%-vol regime"], "correct": 3, "explain": "The tested rule already used a 50-day-high re-entry and still whipsawed six times in 2022. Scaling the trigger by realised vol, so it fires at a fixed number of daily standard deviations rather than a fixed percentage, is the standard fix, and lesson 3's estimate is the input."}
  ],
  "task": "Write your book's drawdown rule as three thresholds, three actions and one re-entry condition, then find the date in 2020 on which each would have fired."
}
---

## The arithmetic, at the book level

You know that a loss of L requires a gain of L ÷ (1 − L) to recover. At the book level the same arithmetic has a second term: time. A drawdown is a depth and a duration, and the duration is where books die, because funding, investors and nerves all have clocks.

SPY, Yahoo adjusted closes: from the 2007-10-09 peak to the 2009-03-09 low, −55.2%, requiring +123.2% to recover, which took until 2012-08-16, 1,256 days after the low. From 2020-02-19 to 2020-03-23, −33.7%, requiring +50.9%, recovered 2020-08-10 after 140 days. From 2022-01-03 to 2022-10-12, −24.5%, requiring +32.4%, recovered 2023-12-13 after 427 days. From 2025-02-19 to 2025-04-08, −18.8%, requiring +23.1%, recovered 2025-06-26 after 79 days.

Four drawdowns, four very different shapes. The deepest took three and a half years to recover; the fastest to fall recovered in under five months. A drawdown rule has to work on both, and the worked example shows that it does not.

## What a drawdown rule is

A drawdown rule cuts gross exposure as the book falls from its peak and restores it on some recovery condition. Its logic is that of a trailing stop applied to the whole book: it does not know why the book is falling, only that it is, and it acts on the fact.

One more property matters: a drawdown rule is symmetric in a way a stop on a single position is not. It cuts the whole book, including the positions that are working, because it does not know which ones are the problem. That is a feature when the problem is the regime and a cost when the problem is one name, which lesson 6's concentration limits should already have caught.

Three design decisions. The **reference peak**: the all-time high, or a rolling one, typically 252 days, so that a book with a long-ago peak is not permanently in drawdown. The **thresholds and actions**: a ladder such as 50% gross at −10%, zero at −20%. The **re-entry condition**: what has to happen before exposure goes back up. This last one is the most neglected and the most important, because a rule that restores exposure the day the drawdown shrinks below the threshold will oscillate across it.

The rule tested below: reference peak is the rolling 252-day high of SPY's adjusted close; at a drawdown of 10% or worse, exposure goes to 50%; at 20% or worse, to zero; exposure is restored to 100% only when the close makes a new 50-day high. Evaluated daily at the close, acted on at the same close, no costs, no slippage. Applied to SPY, not to the course book, so that the result is about the rule rather than about the book.

## Worked example

**2020.** SPY closed at its high on 02-19. The rule cut to 50% on 02-27 at $270.51, a 12.1% drawdown (the fall had already blown through the 10% line in a day). It went to zero on 03-12 at $225.60, −26.7%. The low was 03-23. The rule re-entered on 05-20 at $271.57, 20% above the exit, then cut again the next day on a −12.3% print, restored on 05-27, cut on 06-11, and finally restored for good on 07-15. Seven transitions. Calendar-year result: **+1.8% versus +17.2% for buy-and-hold**; worst drawdown −20.0% versus −33.7%.

**2022-2023.** Cut to 50% on 2022-02-22 at −10.1%. Flat on 06-13 at −21.3%. Restored 08-10, cut 08-11, restored 08-12, cut 08-17, flat again 09-21 at −20.1%, restored 11-22, cut 11-23, restored 2023-02-01, cut 02-06, restored for good 04-18. Twelve transitions. Two-year result: **−4.6% versus +2.7%**; worst drawdown −21.7% versus −24.5%.

**2008-2009.** Seven whipsaws between January and May 2008 as SPY oscillated around −10%. Flat on 2008-07-14 at $88.06, −20.4%, two months before Lehman. Stayed flat through the low (03-09-2009, −55% from peak) and did not re-enter until 2009-08-13, at $74.85, by which time SPY had rallied 34% from the low. More whipsaw in August and September 2009, fully restored 10-09. Two-year result: **−7.1% versus −19.4%**; worst drawdown **−14.2% versus −51.9%**.

**2025.** Cut to 50% on 03-13 at −10.0%; restored 05-13 on a new 50-day high. Two transitions. Result: +14.6% versus +18.0%; worst drawdown −14.4% versus −18.8%.

**2018.** Cut 02-08, restored 06-01, cut 12-14. Result: −6.4% versus −5.3%; drawdown −15.2% versus −19.3%.

The pattern: the rule reduced the worst drawdown in every window, by 2.8 to 37.7 points. It trailed buy-and-hold on return in every window except 2008-09, by 1.2 to 15.5 points. The one window where it paid was the one where the fall was slow enough for the −20% trigger to fire two months before the worst of it and the recovery slow enough that late re-entry still caught most of it.

**Too late** is 2020: cutting inside the last week of a three-week crash, then re-entering after the rebound. The cost was 15.5 points of return for 13.7 points of drawdown reduction. **Too early** is early 2008 and mid-2022: cutting at −10% repeatedly in a choppy market, paying the round trip each time. Each whipsaw costs the difference between the exit and the higher re-entry; in 2022 the rule sold at $353 and bought back at $397 in the June to August loop alone.

## Chart

![The drawdown de-risking rule as a flow: mark NAV against its 252-day peak; drawdown under 10% keeps full gross; 10% to 20% halves gross; over 20% goes to zero; exposure is restored only on a new 50-day high. Notes carry the tested dates on SPY: cut 2020-02-27 at −12.1%, flat 2020-03-12 at −26.7% seven sessions before the low, back in 2020-05-20; the rule returned +1.8% in 2020 against +17.2% for buy-and-hold. Source: Yahoo Finance SPY adjusted closes.](figures/drawdown-derisking-rule-flow.svg)

## Making the rule better

The tested rule is deliberately plain. Three changes address the failures the example exposed.

**Scale the thresholds by volatility.** A 10% fall is two weeks of ordinary noise when realised vol is 40% and a genuine regime signal when it is 12%. Set the trigger at, say, 2.5 daily standard deviations of the book's current EWMA vol accumulated over the drawdown window, rather than at a fixed percentage. In March 2020 that would have fired earlier relative to the crash and not fired at all on the −12% May print.

**Cut on the vol signal, not only the drawdown.** Lesson 3 showed the 20-day and EWMA estimates rising from 13% to 25% between 02-19 and 02-28 2020. A rule that halves gross when fast vol crosses twice its slow estimate would have de-risked on roughly 02-25, five sessions and about 8% before the drawdown rule did.

**Re-enter in steps.** Instead of zero to 100% on one signal, restore a third at each of three conditions: a new 20-day high, a new 50-day high, fast vol back below slow. The whipsaw cost is then a third of the size.

None of this makes the rule free. In four of the five windows the market recovered on its own and the rule was a premium paid. The rule is bought for the fifth window, and for the two constraints VaR cannot see: the margin call that arrives at −25% and the trader who cannot sit at −30%. Lesson 10 and lesson 1's third question decide whether you need it.

## Sources

- Grossman, S. J. and Zhou, Z. (1993). "Optimal Investment Strategies for Controlling Drawdowns." *Mathematical Finance* 3(3). https://doi.org/10.1111/j.1467-9965.1993.tb00044.x
- Moreira, A. and Muir, T. (2017). "Volatility-Managed Portfolios." *Journal of Finance* 72(4). https://doi.org/10.1111/jofi.12513
- Yahoo Finance historical data, SPY. https://finance.yahoo.com/quote/SPY/history/
