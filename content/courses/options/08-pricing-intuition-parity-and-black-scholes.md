---
{
  "title": "Pricing Intuition: Parity and Black-Scholes",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Put-call parity for European options on a non-dividend stock states:", "opts": ["C + P = S", "C = P", "C - P = S - K e^(-rT)", "C - P = K - S"], "correct": 2, "explain": "A long call plus a short put at the same strike and expiry replicates a forward purchase of the stock at K, so their price difference equals the stock minus the present value of the strike."},
    {"q": "XYZ is 100.00, the 100 put is 3.67, and K e^(-rT) is 99.51 (45 DTE, 4%). Parity implies the 100 call is worth:", "opts": ["3.67", "3.18", "4.16", "4.65"], "correct": 2, "explain": "C = P + S - K e^(-rT) = 3.67 + 100.00 - 99.51 = 4.16, matching the chain mid."},
    {"q": "Which Black-Scholes input has NO effect on a European call's price?", "opts": ["The interest rate", "The expected return of the stock", "The volatility", "The time to expiration"], "correct": 1, "explain": "The model prices by replication, so the stock's drift drops out; only the current price, strike, time, volatility, rate and dividends matter."},
    {"q": "Holding everything else fixed, a higher interest rate makes:", "opts": ["Calls more expensive and puts cheaper", "Calls cheaper and puts more expensive", "Both cheaper", "Both more expensive"], "correct": 0, "explain": "A call lets you defer paying the strike, worth more when cash earns more; a put defers receiving it, worth less. In the course's chain, the 100 call is 3.92 at r = 0 and 4.16 at r = 4%."},
    {"q": "A stock will pay a 0.50 dividend before expiration. Compared with no dividend, the parity relation becomes:", "opts": ["C - P = S - K e^(-rT), unchanged", "C - P = S - PV(D) - K e^(-rT)", "C - P = S + PV(D) - K e^(-rT)", "C + P = S - PV(D)"], "correct": 1, "explain": "The call holder does not receive the dividend and the put holder is not harmed by the ex-dividend drop, so the stock's effective price for parity is reduced by the present value of the dividend."}
  ],
  "task": "On a real chain, pick the ATM strike at 30 to 60 DTE and check put-call parity: compute C - P and compare it with S - K e^(-rT) using the current Treasury bill rate; note any dividend before expiration."
}
---


## Prices are constrained before they are modelled

You do not need calculus to understand what an option should cost. Two ideas do most of the work. The first is a no-arbitrage relationship, put-call parity, which ties calls, puts and the stock together so tightly that if you know any two you know the third. The second is a description of what the fair price depends on, which is what the Black-Scholes model formalises. This lesson gives you both as intuition; the capstone has you use both as tools.

## Put-call parity

Consider two portfolios built at the same strike K and expiration T. Portfolio A: one long call plus cash equal to the present value of K, that is K e^(-rT), earning the risk-free rate r. Portfolio B: one long put plus one share of stock.

At expiration, if the stock S is above K, the call in A is worth S - K and the cash has grown to K, total S; in B the put is worthless and the share is worth S, total S. If the stock is below K, the call in A is worthless and the cash is K, total K; in B the put is worth K - S and the share S, total K. The two portfolios pay the same in every state of the world, so they must cost the same today, or someone would buy the cheap one, sell the dear one and lock in a riskless profit:

C + K e^(-rT) = P + S, usually written **C - P = S - K e^(-rT)**.

For a stock paying a known dividend D before expiration, the share in Portfolio B collects it and the call does not, so the relation becomes C - P = S - PV(D) - K e^(-rT). The relation is exact for European options and holds closely for American options when early exercise is unlikely, which for calls on non-dividend stocks is always.

Three things follow. **Synthetics:** long call plus short put equals long stock (financed); long put plus long stock equals long call; short call plus long stock equals short put. Every position has a synthetic twin, which is why a covered call and a cash-secured put at the same strike have the same payoff. **Consistency:** on a liquid chain, calls and puts at the same strike must imply the same volatility, and a violation is a data error or a stale quote, not an opportunity. **The rate effect:** the difference between an ATM call and an ATM put is not zero; it is S - K e^(-rT), which is positive when rates are positive, and explains why the XYZ 100 call is 4.16 while the 100 put is 3.67.

## What determines a fair price

The Black-Scholes model (Black and Scholes 1973, extended by Merton the same year) assumes the stock's returns are lognormally distributed with constant volatility, that you can trade continuously without cost, and that you can borrow and lend at a constant rate. Under those assumptions an option can be replicated exactly by a continuously rebalanced position in the stock and cash, so its price is the cost of that replication. The formula takes six inputs and returns a price. You never need to compute it by hand; you need to know what each input does.

**Stock price S.** Higher S raises calls and lowers puts. The sensitivity is delta.

**Strike K.** Higher K lowers calls and raises puts. This is just moneyness.

**Time to expiration T.** More time raises both calls and puts, because more can happen; the sensitivity is theta, and the relationship is roughly square-root for ATM options.

**Volatility sigma.** More expected movement raises both calls and puts, because the option's payoff is one-sided: the buyer gets the upside of a big move and is protected from the downside. The sensitivity is vega. This is the only input that is not observable; the market's value for it is implied volatility.

**Risk-free rate r.** Higher rates raise calls and lower puts, by the parity logic above. The sensitivity is rho, small for short-dated options and the reason it is rarely quoted on cards: on the 45 DTE 100 call, moving r from 0% to 4% changes the price from 3.92 to 4.16.

**Dividends q or D.** Expected dividends lower calls and raise puts, because the stock is expected to drop by the dividend on the ex-date and the option holder does not collect it. This is also the only reason it can be rational to exercise a call early: to capture the dividend (Lesson 11).

The input that is *missing* is the most instructive. The stock's expected return does not appear. A bull and a bear who agree on volatility agree on the option's price, because the price is set by what it costs to hedge, not by what anyone thinks the stock will do. That is why "I'm bullish, so calls are cheap" is not a pricing argument.

## Where the model breaks and why that is useful

Real returns have fatter tails than a lognormal distribution and volatility is not constant. The market knows this and prices it in as the skew and term structure you saw in Lesson 6. So the model is best understood as a translation device: it turns prices into implied volatilities and back, in a common language every desk uses, and the shape of the resulting surface is where the market's disagreements with the model live. When you read "IV 28%" you are reading a Black-Scholes number; when you read "the 90 puts are at 35 vol", you are reading the market's correction to it.

The model's replication argument also gives you the one-step binomial tree you will build in the capstone: assume the stock can only go up to S x u or down to S x d over the period, find the probability p that makes the stock's expected growth equal the risk-free rate, and price the option as the discounted p-weighted payoff. One step is crude; many steps converge to the Black-Scholes price. The capstone shows both.

## Worked example

XYZ at 100.00 on 22 September 2026, November 6 expiration, 45 DTE, r = 4%, no dividend. Representative chain mids from Lesson 2.

**Parity at the 100 strike.**
- K e^(-rT) = 100 x e^(-0.04 x 45/365) = 100 x e^(-0.004932) = 100 x 0.99508 = **99.508**.
- S - K e^(-rT) = 100.00 - 99.508 = **0.492**.
- Chain: C - P = 4.16 - 3.67 = **0.49**. Parity holds to the cent.

**Parity at the 95 strike.**
- K e^(-rT) = 95 x 0.99508 = 94.533. S - K e^(-rT) = 5.467.
- Chain: 7.15 - 1.69 = 5.46. Holds.

**Parity at the 105 strike.**
- K e^(-rT) = 105 x 0.99508 = 104.483. S - K e^(-rT) = -4.483.
- Chain: 2.16 - 6.64 = -4.48. Holds.

**Recovering a missing call from the put.** Suppose the 100 call quote were unavailable. C = P + S - K e^(-rT) = 3.67 + 100.00 - 99.508 = **4.162**. This is the technique the capstone uses to price a spread from the put side of the chain.

**The rate effect.** At r = 0, K e^(-rT) = 100 and parity gives C - P = 0; the model call is 3.92 and put 3.92. At r = 4% the call is 4.16 and the put 3.67. A four-point rate change moved the call 0.24 and the put 0.25, in opposite directions, with nothing else changing.

**A dividend.** Suppose XYZ will pay 0.50 on 12 October, 20 days out. PV(D) = 0.50 x e^(-0.04 x 20/365) = 0.499. Parity: C - P = 100.00 - 0.499 - 99.508 = **-0.007**. The call and put are now worth almost exactly the same; the model gives C = 3.90, P = 3.90. Half a dollar of dividend removed the entire rate advantage of the call.

**The expected move.** A one-standard-deviation move over 45 days is S x sigma x sqrt(T) = 100 x 0.28 x sqrt(45/365) = 100 x 0.28 x 0.3511 = **9.83**. The ATM straddle (4.16 + 3.67 = 7.83) is close to 0.8 x 9.83 = 7.87, the standard rule of thumb that the straddle prices about 0.8 of a one-sigma move. Turned around, you can read the expected move straight off a chain: straddle / 0.8, or roughly straddle x 1.25.

## Table

How each pricing input moves the XYZ 100 call and 100 put (45 DTE, base case S = 100, IV 28%, r = 4%, no dividend), one input changed at a time.

| Input change | 100 call | 100 put | Greek |
|---|---|---|---|
| Base case | 4.16 | 3.67 | |
| S 100 to 102 | 5.32 | 2.83 | delta (and gamma) |
| T 45 to 21 DTE | 2.79 | 2.56 | theta |
| IV 28% to 32% | 4.72 | 4.23 | vega |
| r 4% to 0% | 3.92 | 3.92 | rho |
| Dividend 0.50 in 20 days | 3.90 | 3.90 | (dividend) |

## Using this without the calculus

You now have two independent ways to check any price on a chain. Parity tells you whether the call and put at a strike are consistent with each other and the stock; if they are not, the quote you are looking at is stale or the contract has a dividend or adjustment you missed. The input list tells you what has to be true for the option to gain: the stock must move by more than theta and any IV drop will cost you, and you can size each effect with the Greeks from Lessons 4 to 7. The capstone asks you to do exactly this for a two-leg spread.

## Sources

- Black, F. and Scholes, M. (1973), "The Pricing of Options and Corporate Liabilities", *Journal of Political Economy* 81(3): https://www.jstor.org/stable/1831029
- Merton, R. C. (1973), "Theory of Rational Option Pricing", *Bell Journal of Economics and Management Science* 4(1): https://www.jstor.org/stable/3003143
- Stoll, H. R. (1969), "The Relationship Between Put and Call Option Prices", *Journal of Finance* 24(5): https://doi.org/10.1111/j.1540-6261.1969.tb01694.x
- Cox, J. C., Ross, S. A. and Rubinstein, M. (1979), "Option Pricing: A Simplified Approach", *Journal of Financial Economics* 7(3): https://doi.org/10.1016/0304-405X(79)90015-1
