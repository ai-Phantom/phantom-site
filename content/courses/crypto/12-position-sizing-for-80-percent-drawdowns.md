---
{
  "title": "Risk: Sizing for 80% Drawdowns and a Plan That Survives a Venue Failure",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "BTC's close-to-close drawdown from 2021-11-08 to 2022-11-21 was 76.6%. The gain required to recover it is", "opts": ["76.6%", "153%", "327%", "400%"], "correct": 2, "explain": "1 divided by (1 minus 0.766) minus 1 is 3.27, a 327% gain. From an 80% drawdown it is 400%."},
    {"q": "If your rule is that a full 80% drawdown of your crypto may cost at most 10% of net worth, the crypto allocation is at most", "opts": ["10%", "12.5%", "20%", "80%"], "correct": 1, "explain": "Allocation times 0.8 equals 0.10, so allocation is 12.5%. The drawdown is the sizing input; the expected return does not enter."},
    {"q": "Why does the lesson size for the drawdown rather than for daily volatility?", "opts": ["Volatility is irrelevant", "Because the realised 2021 to 2022 drawdown was 76.6% while daily volatility of 64% would suggest a much smaller typical loss; drawdown is the loss you must actually survive", "Drawdown is easier to compute", "Regulators require it"], "correct": 1, "explain": "Daily sigma sets stops and leverage; the cycle drawdown sets the allocation. The two are different questions."},
    {"q": "A plan that survives a venue failure requires, at minimum", "opts": ["Using the largest venue", "A cap on the share of crypto held at any one venue, self-custody of the idle balance, and a written procedure for what happens to hedged positions if one leg's venue halts withdrawals", "Buying insurance from the venue", "Trading only stablecoins"], "correct": 1, "explain": "Lesson 3 showed that failures are not detectable in advance. The plan must limit the loss structurally and specify the actions for the open positions."},
    {"q": "The 1 BTC cash-and-carry of lesson 7 with its short leg at 3x: if the derivatives venue halts, what is your exposure?", "opts": ["None, it is hedged", "You are now unhedged long 1 BTC in spot with a frozen claim on the short's margin and P&L; the hedge is gone the moment the venue is", "Only the spot leg is at risk", "The venue will close the short for you"], "correct": 1, "explain": "The hedge is two claims on two counterparties. Losing one leaves you with the other's full price exposure plus a bankruptcy claim."}
  ],
  "task": "Write your crypto risk plan on one page: maximum allocation from the 80% rule, per-venue cap, self-custody threshold, and the exact steps you take on each open position if a venue halts withdrawals."
}
---

## The loss you are sizing for

Everything in this course has pointed at one number, and it is not the daily volatility. It is what the asset has actually done to a buyer at the top. BTC's peak close was $67,566.83 on 2021-11-08 and its trough close $15,787.28 on 2022-11-21: a fall of 76.6% in 378 days. ETH fell 79.4% from its 2021-11-08 close of $4,812.09 to $993.64 on 2022-06-18. The Nasdaq-100 ETF fell 35.6% over the same cycle and the S&P 500 ETF 25.4%. The 2021 to 2022 episode was not the first: the 2017 to 2018 drawdown was larger, and the 2013 to 2015 one larger still.

An 80% drawdown is therefore not a tail scenario for this asset class. It is the base case for a buyer at a cycle high, and any sizing rule that does not start there is a sizing rule for a different asset.

## Chart

![BTC-USD weekly candles from the week of 2021-11-01 to the week of 2022-11-28, built from Yahoo Finance daily bars aggregated Monday to Sunday. Marked: the peak close of $67,567 (2021-11-08) and the trough close of $15,787 (2022-11-21), a 76.6% close-to-close drawdown spanning the Luna collapse (May 2022), the Three Arrows and Celsius failures (June 2022) and the FTX bankruptcy (November 2022).](figures/btc-2021-2022-drawdown-weekly.svg)

The chart's shape matters as much as its depth. There was no single crash. The drawdown arrived as a series of 20 to 35% legs, each followed by a rally that looked like a bottom, over a year in which funding turned negative, venues failed, and every level that had held before broke. A stop-loss would have taken you out; a plan to buy the dip would have been executed four times, each time at a higher price than the eventual low.

## Worked example

The arithmetic of recovery first. A drawdown of d requires a gain of 1 ÷ (1 − d) − 1 to return to the starting value.

- 76.6%: 1 ÷ 0.234 − 1 = 3.27, a 327% gain. BTC did this: from the $15,787 trough to the 2025-10-06 close of $124,753 is a 690% rise, but it took 34 months and passed through another 32.5% drawdown to the 2026-09-24 close of $84,242.
- 80%: 1 ÷ 0.2 − 1 = 4.00, a 400% gain.
- For comparison, 25.4% (SPY, 2022): 1 ÷ 0.746 − 1 = 34%.

Now size an allocation for it. Take an investor with $250,000 of liquid net worth who decides that a full 80% drawdown of the crypto allocation may cost at most 10% of net worth, $25,000.

- Allocation A satisfies A × 0.80 = 25,000, so A = $31,250, or 12.5% of net worth.
- At the 2026-09-24 close of $84,242 that is 0.371 BTC, or a BTC-and-ETH mix of the same dollar value (they are one bet: correlation 0.80 to 0.91 every year, lesson 9).
- Cross-check against daily risk: 31,250 × 2.45% daily sigma = $766 per day, 0.31% of net worth. Comfortable. The drawdown constraint binds; the volatility constraint does not. That is typical for this asset class and it is why the drawdown, not the sigma, sets the allocation.
- Leverage: none. A 3x position on the same $31,250 is $93,750 of exposure, and lesson 8 puts its liquidation 32.8% below entry, inside the first leg of the 2022 drawdown. Leverage does not fit inside a budget built for an 80% fall; if you use it for a hedged trade like the capstone's carry, it is sized separately as a margin buffer, not as directional exposure.

Then split the allocation by custody, applying lesson 3:

- Working capital on venues: only what open orders need. Say 20% of the allocation, $6,250, and no more than $6,250 on any single venue.
- Self-custody: the remaining $25,000 in a wallet whose seed you have restored from paper.
- Maximum loss from one venue failure: $6,250, 2.5% of net worth, and that is the total loss case, not the FTX case where a fiat claim eventually paid more than 100% of petition-date value.

Combine the two rules: the worst simultaneous outcome is an 80% drawdown plus a total loss of one venue balance, 25,000 + 6,250 × 0.2 (the venue balance's remaining 20% after the drawdown) = $26,250, 10.5% of net worth. Written down in advance, that number is survivable. Discovered after the fact, at 03:00 on a Sunday, it is the reason people leave the market.

## A plan for the day a venue halts

The custody split limits the loss. The plan says what you do. It has to be written before the event because, as lesson 3 showed, the event is not announced.

For unhedged spot on the halted venue: nothing can be done; the balance is now a claim. Record the date, the balance and the last price. Do not send more funds to "help" a withdrawal.

For a hedged position with one leg on the halted venue, using the capstone's carry as the case: you are long 1 BTC spot elsewhere and short 1 BTC on the halted venue at 3x. The short's margin ($28,089) and any profit are frozen. You are now unhedged long 1 BTC of price risk. The plan must say which of three things you do, and it must say it now:

1. Re-hedge: open a new 1 BTC short on a second venue, posting fresh margin, and accept that you are now paying to hold a hedge whose original leg may or may not come back.
2. Unwind: sell the 1 BTC spot, going flat on price, and carry the frozen claim as a fixed-dollar receivable whose value now depends on the bankruptcy, not the market.
3. Hold: keep the spot and treat the frozen short as if it did not exist, meaning you are now simply long BTC at the current price with an 80% drawdown possible.

Any of the three can be right. Not having chosen is always wrong. The capstone asks you to choose and to state the trigger.

For the venue you are still using: the plan should also say what happens if it halts next. The 2022 sequence was Celsius, Voyager, Three Arrows, then FTX and BlockFi within five months. Reduce per-venue caps when the sector is under stress, and do it by rule, not by news.

## What the rule is not

It is not a forecast. Sizing for an 80% drawdown does not mean expecting one. It means that if one arrives, the result is a bad year rather than a changed life, and that you are still solvent and still in the market when the recovery, which historically has been as violent as the fall, begins. BTC's calendar returns after the trough were +154% in 2023 and +112% in 2024; the investor who had sized to survive 2022 collected those, and the one who had not was reading about them.

## Sources

- Yahoo Finance chart API, BTC-USD daily bars, 5-year range (peak, trough, weekly aggregation): https://query1.finance.yahoo.com/v8/finance/chart/BTC-USD?range=5y&interval=1d
- Yahoo Finance chart API, ETH-USD daily bars, 5-year range: https://query1.finance.yahoo.com/v8/finance/chart/ETH-USD?range=5y&interval=1d
- John J. Ray III, written testimony before the House Committee on Financial Services, 2022-12-13 (what a venue failure looks like from the inside): https://docs.house.gov/meetings/BA/BA00/20221213/115246/HHRG-117-BA00-Wstate-RayJ-20221213.pdf
- Coinbase Global, Inc., Form 10-K for fiscal 2022, risk factor on customers as unsecured creditors: https://www.sec.gov/Archives/edgar/data/1679788/000167978823000031/coin-20221231.htm
