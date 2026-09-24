---
{
  "title": "Rebalancing",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A 60/40 portfolio starts at $10,000. Over a year stocks return +25% and bonds −5%. The new stock weight is", "opts": ["60%", "62.5%", "66.4%", "75%"], "correct": 2, "explain": "Stocks: 6,000 × 1.25 = 7,500. Bonds: 4,000 × 0.95 = 3,800. Total 11,300. Stock weight 7,500 ÷ 11,300 = 66.4%, more than 5 points above target."},
    {"q": "Rebalancing's primary purpose, according to Vanguard's research, is", "opts": ["To increase returns", "To keep the portfolio's risk at the level chosen, since drift toward the higher-returning asset raises risk over time", "To generate taxable gains", "To time the market"], "correct": 1, "explain": "Rebalancing usually lowers return slightly versus letting winners run, because the higher-risk asset tends to have the higher expected return. Its job is risk control: an unrebalanced 60/40 from 1926 would have drifted to over 80% stocks."},
    {"q": "Which of these rebalancing moves has no tax cost in a taxable account?", "opts": ["Selling appreciated stock funds to buy bonds", "Directing new contributions and dividends toward the underweight asset", "Selling bonds at a gain", "Any move made in December"], "correct": 1, "explain": "Buying does not realise gains. Using cash flows to top up the underweight asset moves the weights back without triggering capital gains tax."},
    {"q": "Under IRS rules, a gain on shares held one year or less is taxed as", "opts": ["Long-term capital gain at 0%, 15% or 20%", "Ordinary income at your marginal rate", "Not taxed", "A flat 10%"], "correct": 1, "explain": "Short-term gains are taxed as ordinary income. Holding past one year moves the gain to the long-term schedule, which is why rebalancing sales should prefer lots older than a year where possible."},
    {"q": "A threshold rule of 5 percentage points on a 60/40 portfolio means you rebalance when stocks reach", "opts": ["61% or 59%", "65% or 55%", "70% or 50%", "Any change at all"], "correct": 1, "explain": "The band is target ± 5 points. Vanguard found that checking annually or semi-annually and trading only when a 5-point band is breached gave risk control similar to more frequent rebalancing with far fewer transactions."}
  ],
  "task": "Compute your current weights against your targets and note which, if any, are outside a 5-point band."
}
---

## Why weights drift

You set an allocation in lesson 7. Within a year it will be wrong, not because you did anything but because the holdings moved at different rates. Stocks rise 25%, bonds fall 5%, and the 60/40 portfolio you built is now 66/34. Keep going and the drift compounds: Vanguard's research shows that a 60/40 US portfolio left untouched from 1926 would have drifted to over 80% stocks, with the volatility and drawdown of a much more aggressive allocation than the one its owner chose.

Rebalancing is the act of selling what has grown and buying what has shrunk to restore the target weights. It is the maintenance step that keeps the risk budget from lesson 1 in force.

## What rebalancing is for, and what it is not for

It is for risk control. The allocation was set so that the worst plausible year stayed inside your budget. Drift toward the higher-risk asset silently raises that worst year. Rebalancing puts it back.

It is not primarily for return. Because the asset that drifts upward is usually the one with the higher expected return, rebalancing typically gives up a little return relative to letting winners run. Vanguard's rebalancing studies found that over long periods a rebalanced 60/40 had somewhat lower return and substantially lower volatility than an unrebalanced one. There are periods where rebalancing adds return, when assets mean-revert, but you should not count on a "rebalancing bonus." Count on the risk control.

It is also a forced discipline. Rebalancing sells after a rise and buys after a fall, which is the opposite of what your instincts will tell you to do. In March 2009 or March 2020 the rebalancing rule said to sell bonds and buy stocks. The people who followed a written rule did; the people who relied on judgement mostly did not.

## Calendar versus threshold

**Calendar rebalancing** checks and trades on a fixed schedule: every quarter, every six months, every year. It is simple and easy to automate. The cost is that it can trade when the drift is trivial, incurring tax and transaction cost for nothing, and it can miss a large drift that happens between dates.

**Threshold rebalancing** trades only when a weight moves outside a band around its target, such as ±5 percentage points on a 60% allocation. It responds to what the market did rather than to the date. The cost is that you have to monitor, and in a volatile year it can trigger several times.

**Combined.** Vanguard's analysis, covering 1926 to 2009 and updated since, found that checking on a schedule (annually or semi-annually) and trading only when a 5-point band was breached gave risk control close to monthly rebalancing with far fewer trades. That combination, check twice a year, act only outside the band, is the sensible default for a first portfolio.

Bands should scale with the allocation. A ±5-point band on a 60% holding is a relative move of about 8%. The same absolute band on a 5% satellite would let it double before triggering, so satellites get a relative band, typically ±25% of their target weight (a 7% target rebalances at 5.25% or 8.75%), or are governed by their stop and thesis review rather than by rebalancing at all.

## The costs

Every rebalancing trade has three costs, and a plan that ignores them rebalances too often.

**Transaction cost.** Commissions are mostly zero for US-listed ETFs and stocks now, but the bid-ask spread is not. Broad ETFs like VTI and BND trade at spreads of a cent or two; thinly traded funds and small-cap stocks can cost 0.5% or more per round trip.

**Tax, in a taxable account.** Selling an appreciated holding realises a capital gain. Under IRS rules (Topic 409 and Publication 550), gains on lots held more than one year are taxed at 0%, 15% or 20% depending on income; gains on lots held one year or less are taxed as ordinary income at your marginal rate, which for many people is 22% or 24%. In a tax-advantaged account such as an IRA or 401(k), rebalancing is free of this cost entirely, which is a reason to hold the more volatile parts of the allocation there if you have both types of account.

**Time.** Not a dollar cost, but the frequency of checking is also the frequency of temptation. Twice a year is enough.

## Rebalancing without selling

Before selling anything in a taxable account, use the free levers:

1. **New contributions.** Direct every new dollar to whichever asset is most underweight. With regular contributions, this alone keeps a portfolio near target most of the time.
2. **Dividends and interest.** Turn off automatic reinvestment into the paying fund and direct the cash to the underweight asset instead.
3. **The cash reserve.** The 5% T-bill sleeve from lesson 7 exists partly for this: it is the buffer you draw on to buy the underweight asset after a fall.
4. **Losses.** If a holding is below its cost basis, selling it to rebalance realises a loss that offsets gains elsewhere, subject to the wash-sale rule (Publication 550: no repurchase of a substantially identical security within 30 days before or after).

Only when these are exhausted do you sell appreciated holdings, and when you do, sell the lots with the highest cost basis first and the lots older than a year in preference to newer ones.

## Worked example

A 60/40 portfolio in a taxable account starts the year at $10,000: $6,000 in VTI, $4,000 in BND. Over the year VTI returns +25% and BND −5%.

**End-of-year values.**

- VTI: 6,000 × 1.25 = $7,500
- BND: 4,000 × 0.95 = $3,800
- Total: $11,300
- VTI weight: 7,500 ÷ 11,300 = 66.4%
- BND weight: 3,800 ÷ 11,300 = 33.6%

The stock weight is 6.4 points over target, outside a 5-point band. Rebalance.

**Target dollars.**

- VTI target: 0.60 × 11,300 = $6,780
- BND target: 0.40 × 11,300 = $4,520
- Sell VTI: 7,500 − 6,780 = $720
- Buy BND: 4,520 − 3,800 = $720

**Tax on the sale.** The $720 of VTI sold was bought for 720 ÷ 1.25 = $576, so the realised gain is 720 − 576 = $144.

- If the shares were held over a year and your long-term rate is 15%: tax = 144 × 0.15 = $21.60.
- If held under a year and your marginal rate is 24%: tax = 144 × 0.24 = $34.56.

**Alternative with no tax.** Suppose you also planned to contribute $720 this year. Put the whole contribution into BND instead of splitting it:

- VTI: $7,500 (unchanged)
- BND: 3,800 + 720 = $4,520
- Total: $12,020
- VTI weight: 7,500 ÷ 12,020 = 62.4%

Not fully back to 60%, but inside the band, with no sale and no tax. The next contribution finishes the job.

**Transaction cost.** Selling $720 of VTI and buying $720 of BND at spreads of about 0.01% each costs roughly $0.14. Negligible for broad ETFs; the tax was the real cost, and it was avoidable.

## Table

| | Calendar only | Threshold only | Calendar check + threshold act |
|---|---|---|---|
| Rule | Trade to target on fixed dates | Trade when a weight leaves its band | Check on fixed dates; trade only if outside band |
| Monitoring effort | Low | High (continuous) | Low |
| Trades per year (typical) | 1 to 4, regardless of need | 0 to several, depending on volatility | 0 to 2 |
| Risk control | Good, with gaps between dates | Tight | Close to monthly rebalancing in Vanguard's tests |
| Tax and spread cost | Can trade when drift is trivial | Only when needed, but can cluster in volatile years | Lowest of the three |
| Behavioural risk | Low; the date decides | Higher; you are watching constantly | Low |
| Suited to | Automated accounts, 401(k)s | Experienced investors | First portfolios in any account |

## The rule to write down

Check weights on two fixed dates a year. If any core holding is more than 5 points from target, or any satellite more than a quarter of its target away, restore it: first with contributions, dividends and the cash reserve; then, if still outside the band, by selling the highest-basis, longest-held lots of the overweight holding. Do nothing between the dates unless a satellite hits its stop. Lesson 12 puts this sentence into your investment plan.

## Sources

- Vanguard Research (Jaconetti, Kinniry, Zilbering), "Best practices for portfolio rebalancing", 2010: https://www.vanguard.com/pdf/icrpr.pdf
- Internal Revenue Service, Topic No. 409, "Capital Gains and Losses": https://www.irs.gov/taxtopics/tc409
- Internal Revenue Service, Publication 550, "Investment Income and Expenses": https://www.irs.gov/publications/p550
- U.S. Securities and Exchange Commission, Investor.gov, "Rebalancing": https://www.investor.gov/introduction-investing/investing-basics/glossary/rebalancing
