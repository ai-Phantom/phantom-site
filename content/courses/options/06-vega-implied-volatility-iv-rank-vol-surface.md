---
{
  "title": "Vega, Implied Volatility, IV Rank, Vol Surface",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The XYZ 100 call is 4.16 with vega 0.139. Implied volatility rises from 28% to 32% with nothing else changing. The call is now worth about:", "opts": ["4.30", "4.72", "3.60", "5.55"], "correct": 1, "explain": "Vega is the change per one-point move in IV: 4 points x 0.139 = 0.56, so 4.16 + 0.56 = 4.72. The full model gives 4.72."},
    {"q": "Implied volatility is best described as:", "opts": ["The stock's realised volatility over the past 30 days", "The expected return of the stock", "The VIX", "The volatility input that makes a pricing model reproduce the option's market price"], "correct": 3, "explain": "IV is backed out of the market price: it is the sigma at which the model price equals the quoted price. It is a price for uncertainty, not a measurement of past movement."},
    {"q": "XYZ's 30-day IV has ranged from 16% to 44% over the past year and is 28% today. IV rank is:", "opts": ["28%", "63.6%", "42.9%", "12%"], "correct": 2, "explain": "IV rank = (current - low) / (high - low) = (28 - 16) / (44 - 16) = 12 / 28 = 42.9%."},
    {"q": "On most equity chains, OTM puts trade at higher implied volatility than OTM calls the same distance from the money. This pattern is called:", "opts": ["Contango", "Skew (or smile)", "Term structure", "Put-call parity"], "correct": 1, "explain": "Volatility skew describes IV varying by strike within one expiration; the downside-put premium reflects demand for crash protection and the tendency of stocks to fall faster than they rise."},
    {"q": "Which position has the most vega risk per contract?", "opts": ["An ATM call at 7 DTE (vega 0.055)", "An ATM call at 45 DTE (vega 0.139)", "An ATM call at 90 DTE (vega 0.196)", "A far OTM call at 45 DTE (vega 0.058)"], "correct": 2, "explain": "Vega grows with time to expiration because a change in expected volatility has more time to matter. Longer-dated ATM options are the most volatility-sensitive."}
  ],
  "task": "Find the IV rank or IV percentile field on your broker's platform for three different stocks and write down which one is highest, along with each stock's next earnings date."
}
---


## The input you cannot see

Every other input to an option's price is public: the stock price, the strike, the days to expiration, the interest rate, the dividend. The one thing the market has to guess is how much the stock is going to move. **Implied volatility (IV)** is that guess, expressed as an annualised standard deviation, and it is the number the market backs out of the option price rather than puts in. If the XYZ 100 call trades at 4.16 with 45 DTE and a 4% rate, the volatility that makes a standard model produce 4.16 is 28%. That is what "IV 28%" on the chain means.

Two consequences. First, IV is a price, not a forecast, and like any price it can be high or low relative to what actually happens. Second, because IV is backed out of the market price, saying "the option is expensive" and saying "IV is high" are the same sentence. Vega is how you turn one into the other.

## Vega

Vega is the change in an option's value for a one-percentage-point change in implied volatility, everything else fixed. The XYZ 100 call has vega 0.139: if IV rises from 28% to 29%, the call rises about 0.139 to 4.30; per contract, $13.90. Vega is positive for every long option, call or put, and negative for every short option. A long call is long volatility as well as long the stock.

Vega is largest at the money and grows with time to expiration. On the XYZ chain, the ATM call's vega is 0.196 at 90 DTE, 0.139 at 45 DTE and 0.055 at 7 DTE; the 115 call at 45 DTE has vega 0.058. A long-dated ATM option is mostly a volatility bet; a short-dated OTM option is mostly a direction bet. If you buy a 90 DTE call because you expect a move and IV then falls five points, vega alone costs you about 1.00 of the 6.02 you paid, before the stock has done anything.

## Reading IV: what is high?

A 28% IV means nothing on its own. It is high for a utility and low for a biotech. Two tools put it in context.

**IV rank** compares today's IV to its own range over the past year: (current - 52-week low) / (52-week high - 52-week low). It runs from 0% at the year's low to 100% at the year's high. **IV percentile** asks a different question: what fraction of days in the past year had IV below today's level. Rank can be distorted by a single spike (one crash day sets a high that makes every other day look low); percentile is more robust to that but says nothing about how far above typical the current reading is. Most platforms show one or both; use them together.

The reason to care is that IV tends to revert toward its typical level. When IV rank is very high, long options are paying a rich price for uncertainty, and the odds favour that price falling; when IV rank is very low, options are cheap in volatility terms and the odds favour a rise. That is a statement about the tendency of a price, not a guarantee, and it says nothing about direction. Its practical use is in choosing between debit and credit structures (Lesson 10), not in predicting the stock.

## Realised versus implied

**Realised (historical) volatility** is what the stock actually did: the annualised standard deviation of its daily returns over some window. Comparing implied to realised tells you whether the market is pricing more or less movement than has recently occurred. Over long samples, index IV has on average exceeded subsequent realised volatility, a gap known as the volatility risk premium, which is the structural reason option sellers can be compensated for their risk. It is an average with a fat left tail, not a promise, and the same literature that documents it documents the periods where it inverted violently.

## The volatility surface

IV is not one number per stock. It varies by strike and by expiration, and the full map is the **volatility surface**.

**Skew (or smile)** is the variation across strikes at one expiration. On equity and index chains, OTM puts almost always trade at higher IV than ATM options, and OTM calls at lower IV, so the plot slopes down from left to right. Two explanations dominate: demand for downside protection from long stock holders, and the tendency of markets to fall faster than they rise, which makes a lognormal model underprice crash risk. Skew is why the 95 put on a real chain will show a higher IV than the 105 call, and why a put credit spread collects proportionately more than a call credit spread the same distance OTM.

**Term structure** is the variation across expirations at one strike. In quiet markets, longer-dated IV is usually higher than short-dated (upward sloping), because more time leaves more room for something to happen. Ahead of a known event such as earnings, the expiration that contains the event carries much higher IV than the ones around it, and after the event that premium collapses, which traders call **IV crush**. In a stressed market, short-dated IV can exceed long-dated (inverted), signalling that the market expects the turmoil to fade.

The VIX index is the most quoted point on any surface: Cboe's measure of 30-day expected volatility on the S&P 500, computed from a strip of SPX option prices rather than from a single option or a model. When a card or a headline says "VIX 18", it is quoting 30-day SPX implied volatility of 18% annualised.

## Worked example

XYZ at 100.00, 22 September 2026, representative chain at a flat 28% IV, 4% rate. In this lesson we let IV move.

**Vega on the 100 call (45 DTE, 4.16, vega 0.139).**
- IV 28% to 32% (+4 points): estimated 4.16 + 4 x 0.139 = **4.72**. Full model value at 32%: 4.72.
- IV 28% to 24% (-4 points): estimated 4.16 - 0.56 = **3.60**. Full model: 3.60.
- IV 28% to 20% (-8 points): estimated 4.16 - 1.11 = 3.05. Full model: **3.05**.

Per contract, the swing from 24% to 32% IV is 4.72 - 3.60 = 1.12, or $112, on a $416 option, with the stock not moving a cent.

**Vega on the 110 call (45 DTE, 1.00, vega 0.096).** IV to 32%: estimated 1.00 + 4 x 0.096 = 1.38; full model 1.40. That is a 40% change in the option's price for a four-point change in IV: cheap OTM options are proportionally the most IV-sensitive.

**IV rank.** Suppose XYZ's 30-day IV over the past 52 weeks ranged from 16% (low) to 44% (high, set during a market sell-off in the spring). Today's 28%: IV rank = (28 - 16) / (44 - 16) = 12 / 28 = **42.9%**. Suppose also that on 61% of trading days in the past year IV was below 28%: IV percentile = **61%**. Read together: IV is in the middle of its range but above its typical day, moderately elevated.

**An earnings expiration.** Suppose XYZ reports on 20 October and the October 23 expiration (31 DTE) prices at 45% IV while November 6 (45 DTE) sits at 28%. The ATM straddle in the October 23 expiration at 45% IV is worth about 10.27; at 28% it would be worth about 6.40. The 3.87 difference, about 39% of the straddle's value, is the event premium. If the stock does nothing on the report and IV drops to 28% the next morning, a long straddle loses that 3.87 in a single session; a 3.00 move in the stock does not come close to covering it. This is IV crush, and it is why "buy options before earnings because a big move is coming" fails as a plan: the big move is already in the price.

## Table

Representative XYZ volatility surface on 22 September 2026, IV in percent. Skew runs across each row (puts richer than calls); term structure runs down each column; the October 23 column carries the earnings premium. Illustrative shape, not a live quote.

| Expiration | DTE | 90P | 95P | 100 (ATM) | 105C | 110C |
|---|---|---|---|---|---|---|
| Oct 9 | 17 | 36 | 31 | 27 | 25 | 24 |
| Oct 23 (earnings) | 31 | 52 | 48 | 45 | 43 | 42 |
| Nov 6 | 45 | 35 | 31 | 28 | 26 | 25 |
| Dec 18 | 87 | 34 | 31 | 29 | 27 | 26 |

Note how the Nov 6 row is the flat 28% chain used in every other lesson only at the ATM strike; a live chain would show the skew in the outer columns, which is why real OTM put prices run a little above the model mids in Lesson 2.

## Vega in decisions

Before any long option trade, check three things: the option's vega relative to its price (how much of your P&L is a volatility bet), where IV sits in its own range (IV rank and percentile), and whether an event sits inside the expiration (term structure). A long call bought at IV rank 90 into earnings is a volatility short in disguise. Before any short option trade, check the same three things in reverse and add a fourth: what happens to the position if IV doubles overnight, because that is the scenario short vega does not survive without a defined-risk structure. Lesson 10 supplies the structures.

## Sources

- Cboe Global Markets, *The Cboe Volatility Index (VIX) White Paper*: https://cdn.cboe.com/resources/vix/vixwhite.pdf
- Cboe Global Markets, Options Institute, implied volatility, skew and term structure: https://www.cboe.com/education/
- Black, F. and Scholes, M. (1973), "The Pricing of Options and Corporate Liabilities", *Journal of Political Economy* 81(3): https://www.jstor.org/stable/1831029
- Bakshi, G. and Kapadia, N. (2003), "Delta-Hedged Gains and the Negative Market Volatility Risk Premium", *Review of Financial Studies* 16(2): https://doi.org/10.1093/rfs/hhg002
