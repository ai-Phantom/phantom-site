---
{
  "title": "Intrinsic and Time Value",
  "duration": "14 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "XYZ is 100.00. The 95 call trades at 7.15. Its time value is:", "opts": ["7.15", "5.00", "2.15", "0.00"], "correct": 2, "explain": "Intrinsic = 100 - 95 = 5.00. Time value = premium - intrinsic = 7.15 - 5.00 = 2.15."},
    {"q": "Which option has the most time value in absolute dollars on a given expiration?", "opts": ["The deepest ITM call", "The ATM option", "The farthest OTM put", "They are all equal"], "correct": 1, "explain": "Time value peaks at the money, where the outcome is most uncertain, and shrinks toward zero both deep ITM (the option behaves like stock) and far OTM (little chance of finishing ITM)."},
    {"q": "An option's time value at expiration is always:", "opts": ["Equal to the premium paid", "Zero", "Equal to intrinsic value", "Negative"], "correct": 1, "explain": "With no time left there is no uncertainty to pay for; an expiring option is worth exactly its intrinsic value, which may be zero."},
    {"q": "XYZ is 100.00, the 105 put trades at 6.64 and the 95 call at 7.15. Both are 5.00 ITM. Why is the put's time value (1.64) lower than the call's (2.15)?", "opts": ["Interest: the call holder keeps cash earning 4% while the put holder forgoes it, which put-call parity prices in", "Puts are always cheaper", "The put is closer to expiration", "The put has a lower strike"], "correct": 0, "explain": "With a positive rate and no dividend, a call's value includes the benefit of delaying payment of the strike, while a put's is reduced by delaying receipt. The same effect shows in the ATM pair: 100 call 4.16 versus 100 put 3.67."},
    {"q": "A put has strike 110 and the stock is at 100. Intrinsic value is:", "opts": ["0", "Cannot be known without the premium", "-10", "10"], "correct": 3, "explain": "Put intrinsic = max(strike - stock, 0) = max(110 - 100, 0) = 10. It does not depend on the premium."}
  ],
  "task": "On a real chain, take one expiration and compute intrinsic and time value for the ATM call, one ITM call and one OTM call; confirm time value peaks at the money."
}
---


## Two parts to every premium

Every option price you see on the chain is the sum of two pieces. **Intrinsic value** is what the option would be worth if it were exercised this instant. **Time value**, also called extrinsic value, is everything else: what the market is paying for the possibility that the option becomes more valuable before it expires.

Premium = intrinsic value + time value

Intrinsic value is arithmetic. Time value is a price, set by supply and demand, that reflects how much can still happen. The split matters because the two pieces behave completely differently as the stock moves and as the calendar advances, and every Greek in the next four lessons is a description of how one of them changes.

## Computing intrinsic value

For a call: intrinsic = max(stock price - strike, 0).
For a put: intrinsic = max(strike - stock price, 0).

The max(..., 0) is the whole point of an option. A call with strike 105 on a stock at 100 is not worth negative five; it is worth zero on exercise, because you would simply not exercise. Intrinsic value is never negative and never depends on the premium, the volatility, or the time left.

An ITM option has positive intrinsic value. ATM and OTM options have zero intrinsic value, so their entire premium is time value.

## Computing time value

Time value = premium - intrinsic value.

Time value is rarely negative for an American option, because if a call were quoted below its intrinsic value you could buy it, exercise it, and sell the shares for an instant profit; arbitrageurs keep that from lasting more than seconds. You will occasionally see a deep ITM option with a bid slightly below intrinsic when the spread is wide; that is a stale or defensive quote, not a free lunch, and it is a signal that the contract is illiquid.

Time value depends on four things you can read directly from the chain and the calendar:

1. **Time to expiration.** More days, more time value, other things equal. Lesson 5 shows the shape of the relationship; it is not linear.
2. **Distance from the money.** Time value is largest at the money and falls off in both directions.
3. **Implied volatility.** Higher expected movement, higher time value. Lesson 6.
4. **Interest rates and dividends.** Small for short-dated options, but they explain why calls and puts at the same strike carry different time value. Lesson 8.

## Why time value peaks at the money

Think about what the buyer is paying for. A deep ITM call, say the 85 strike on a $100 stock, is almost certain to be exercised. It behaves like owning the stock with 85 dollars borrowed; there is little optionality left to pay for, so its time value is small. A far OTM call, say the 115 strike, is unlikely to finish ITM, so the market pays little for the chance. At the money, the outcome is close to a coin flip and the option's payoff has the greatest sensitivity to the next few weeks of news, so the market pays the most for the uncertainty.

The practical consequence, which you will see again in Lesson 5, is that ATM options carry the most time value and therefore lose the most dollars per day to decay. OTM options carry less time value in dollars but often more as a percentage of premium, because they have no intrinsic floor.

## Time value and moneyness on the put side

Everything above applies to puts with the direction flipped. The 105 put on a $100 stock is 5.00 ITM; the 95 put is 5.00 OTM. Time value peaks at the 100 strike. One subtlety: with positive interest rates and no dividend, an ITM put has less time value than an ITM call the same distance from the money, because a put holder who exercises early receives cash now, and delaying that is a cost, whereas a call holder who delays paying the strike keeps earning interest on the cash. This is the reason deep ITM American puts are sometimes exercised early and deep ITM calls on non-dividend stocks essentially never are.

## Worked example

Use the XYZ chain from Lesson 2: XYZ at $100.00 on 22 September 2026, November 6 expiration, 45 DTE, representative mids from a 28% IV model.

**The 95 call, mid 7.15.**
- Intrinsic = max(100.00 - 95, 0) = **5.00**
- Time value = 7.15 - 5.00 = **2.15**
- Share of premium that is time value: 2.15 / 7.15 = 30%

**The 100 call, mid 4.16.**
- Intrinsic = max(100.00 - 100, 0) = **0.00**
- Time value = 4.16 - 0 = **4.16**
- Share of premium that is time value: 100%

**The 105 call, mid 2.16.**
- Intrinsic = max(100.00 - 105, 0) = **0.00**
- Time value = **2.16**, 100% of premium

**The 110 call, mid 1.00.**
- Intrinsic **0.00**; time value **1.00**, 100% of premium

**The 105 put, mid 6.64.**
- Intrinsic = max(105 - 100.00, 0) = **5.00**
- Time value = 6.64 - 5.00 = **1.64**

**The 100 put, mid 3.67.**
- Intrinsic **0.00**; time value **3.67**

**The 95 put, mid 1.69.**
- Intrinsic **0.00**; time value **1.69**

Now read the pattern. Time value across the calls runs 0.16 (85 strike: 15.58 - 15.00), 1.05 (90: 11.05 - 10.00), 2.15 (95), 4.16 (100), 2.16 (105), 1.00 (110), 0.41 (115). It rises to a peak at the ATM strike and falls symmetrically enough on either side that the 95 and 105 calls carry almost the same time value, 2.15 versus 2.16, even though one costs 7.15 and the other 2.16.

Compare across the strike pair: the 95 call and the 105 put are each 5.00 ITM, but the call carries 2.15 of time value and the put only 1.64. The 0.51 gap is not a mispricing. It is interest at 4% on the strike for 45 days, roughly 100 x (1 - e^(-0.04 x 45/365)) = 0.49, plus a small volatility asymmetry. Lesson 8 derives it from put-call parity; for now, notice that time value is not just "time".

Finally, what you paid for. If you bought the 100 call at the 4.24 ask, all 4.24 is time value, and time value goes to zero at expiration. For the trade to break even at expiration, intrinsic value must grow to 4.24, so XYZ must be at 104.24. Every dollar of time value you buy is a dollar the stock must earn back for you.

## Table

Intrinsic and time value across the XYZ November chain, stock at 100.00, 45 DTE.

| Strike | Call mid | Call intrinsic | Call time value | Put mid | Put intrinsic | Put time value |
|---|---|---|---|---|---|---|
| 85 | 15.58 | 15.00 | 0.58 | 0.16 | 0.00 | 0.16 |
| 90 | 11.05 | 10.00 | 1.05 | 0.61 | 0.00 | 0.61 |
| 95 | 7.15 | 5.00 | 2.15 | 1.69 | 0.00 | 1.69 |
| 100 | 4.16 | 0.00 | 4.16 | 3.67 | 0.00 | 3.67 |
| 105 | 2.16 | 0.00 | 2.16 | 6.64 | 5.00 | 1.64 |
| 110 | 1.00 | 0.00 | 1.00 | 10.46 | 10.00 | 0.46 |
| 115 | 0.41 | 0.00 | 0.41 | 14.84 | 15.00 | -0.16 |

The 115 put shows a *negative* time value of -0.16 because the model chain is European-style, and a European put can be worth less than its intrinsic value when interest rates are positive (you cannot exercise today to collect the 15.00). A listed American put can never trade below intrinsic for long: at that price a holder would exercise, which is exactly the early-exercise situation Lesson 11 covers. On a live chain the 115 put bid would sit at or just above 15.00.

## How traders use the split

Three habits follow from this lesson. First, when you buy an option, know how much of the price is time value, because that is the part that evaporates. Second, when you sell an option, time value is the only thing you are being paid for; a short ITM option's intrinsic component is simply stock exposure. Third, when you compare two strikes, compare time value, not premium: the 95 call at 7.15 and the 105 call at 2.16 are paying almost identical amounts for uncertainty, and differ mainly in how much stock exposure is bundled in.

## Sources

- Options Clearing Corporation, *Characteristics and Risks of Standardized Options*, chapter on option pricing components: https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document
- Cboe Global Markets, Options Institute, intrinsic and extrinsic value: https://www.cboe.com/education/
- FINRA, options basics for investors: https://www.finra.org/investors/investing/investment-products/options
