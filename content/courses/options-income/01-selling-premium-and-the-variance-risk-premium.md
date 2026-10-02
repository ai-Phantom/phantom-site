---
{
  "title": "Selling Premium and the Variance Risk Premium",
  "duration": "16 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "The variance risk premium is best described as:", "opts": ["The extra premium a market maker charges for wide bid/ask spreads", "The tendency of index options to expire worthless more often than not", "The gap between the volatility implied by option prices and the volatility the underlying subsequently realises, which has on average been positive for the S&P 500", "The dividend yield an option seller forgoes by holding cash instead of stock"], "correct": 2, "explain": "Carr and Wu (2009) and Bakshi and Kapadia (2003) measure the premium as the difference between implied (or synthetic variance-swap) variance and realised variance; on the S&P 500 it has averaged positive, meaning options were on average priced for more movement than occurred."},
    {"q": "On the model chain (XYZ 100, 45 DTE, 28% IV) the 100 straddle is worth 7.83 and a one-standard-deviation 45-day move is 9.83. What does that comparison tell you?", "opts": ["The straddle seller loses whenever the stock moves more than 7.83 in either direction, which is less than one standard deviation", "The straddle is mispriced because the premium should equal one standard deviation", "The straddle seller profits on any move smaller than one standard deviation", "The straddle seller has a 68% probability of profit"], "correct": 0, "explain": "The straddle seller's break-evens sit at 92.17 and 107.83, inside the one-sigma band. A short straddle is a bet that the realised move is smaller than roughly 0.8 standard deviations, which is why the average profit is modest and the tail loss is not."},
    {"q": "Why is selling premium not the same as collecting income?", "opts": ["Because the premium is taxed as ordinary income", "Because option premium is paid in shares rather than cash", "Because the broker holds the premium until expiration", "Because the credit is compensation for a contingent liability whose expected cost, at fair prices, equals the credit"], "correct": 3, "explain": "At a fair price the expected payout on the option equals the premium received. The seller's edge, if any, is only the amount by which the price exceeds the fair value, which is the variance risk premium, not the whole credit."},
    {"q": "The Cboe BXM factsheet (June 20, 1986 to August 31, 2026) reports a maximum drawdown of -35.8% for BXM versus -50.9% for the S&P 500. What is the correct reading?", "opts": ["Covered calls eliminate drawdowns", "Covered calls reduced the worst drawdown but did not remove the equity tail; the seller still lost roughly a third", "The BXM index is uncorrelated with the S&P 500", "The premium collected fully offset the 2008 decline"], "correct": 1, "explain": "The monthly premium cushions declines but a systematic call writer is still long the market. BXM fell 17.5% in October 1987 against 21.5% for the S&P 500 (Hewitt EnnisKnupp, 2012): a smaller loss, not a hedge."},
    {"q": "Which statement about the tail you are paid for is accurate?", "opts": ["Index puts are cheap because crashes are rare", "The premium seller is short the jump: the average profit is small and frequent, the loss is large and infrequent, and the two are linked by the same price", "Diversifying across many underlyings removes the tail risk of short premium", "A short put has the same tail as a short call"], "correct": 1, "explain": "Bondarenko (2014) and Carr and Wu (2009) both frame the premium as compensation for bearing jump and variance risk. Because most short-premium positions are short the same market factor, diversifying across tickers does not diversify away the crash."}
  ],
  "task": "Download the Cboe PUT and BXM factsheets, write down each index's annualised return, volatility and maximum drawdown next to the S&P 500's, and note the date range each figure covers."
}
---

## Where this course starts

You finished Options Trading Complete, so delta, theta, vega, gamma, vertical spreads and expiration mechanics are assumed here; if a Greek feels rusty, go back to that course before continuing. This course is about the other side of the ticket: being the writer rather than the holder, consistently, as a plan.

Every worked example in the twelve lessons and the capstone uses the same model chain, so numbers tie out from lesson to lesson: **XYZ at $100.00, November 6, 2026 expiration (45 days), 28% implied volatility, 4% risk-free rate, no dividend.** Today is September 22, 2026. Mids are Black-Scholes model values, the same chain the previous course priced. When a lesson needs a second expiration or a later date, it says so and derives the new prices from the same model.

## What you actually sell

When you write an option you sell a contingent liability. The buyer pays you today; in return you promise to deliver a payoff at expiration that depends on where the stock lands. At a fair price the premium equals the expected value of that payoff, discounted. That sentence is the whole lesson: a fairly priced short option has an expected profit of zero, before costs, and a negative expected profit after the bid/ask toll and commissions.

So why does anyone do it? Because index options, and to a lesser extent stock options, have not been priced fairly on average. They have been priced for more movement than subsequently occurred. The difference between the variance implied by option prices and the variance the underlying then realised is the **variance risk premium**. Carr and Wu (2009) built synthetic variance swaps from S&P 500 option prices from 1996 to 2003 and found the average payoff to the variance buyer was strongly negative, meaning the seller was paid. Bakshi and Kapadia (2003) reached the same conclusion from a different direction: delta-hedged long option positions on the index lost money on average, so the hedged seller earned it. Bondarenko (2014) found S&P 500 futures puts from 1987 to 2000 were expensive by any of the models he tried.

That is the case for selling premium in one paragraph, and notice what it is not. It is not "options expire worthless most of the time." An option struck two standard deviations away will expire worthless most of the time and still be fairly priced, because the rare loss is large. The premium seller's edge is only the amount by which the price exceeds fair value, and on the model chain that amount is zero by construction, because the chain was built with a single volatility. The edge, when it exists, is the gap between 28% implied and whatever XYZ actually does over the next 45 days.

## The shape of the trade

Take the simplest short-premium position: sell the 100 straddle, the 100 call at 4.16 and the 100 put at 3.67, for 7.83. You keep all 7.83 only if XYZ closes exactly at 100 on November 6. You keep something if it closes between 92.17 and 107.83. Beyond either break-even you lose a dollar per dollar of further movement, without limit on the upside and down to zero on the downside.

Now compare that to what the chain says is a normal move. One standard deviation over 45 days at 28% volatility is 100 x 0.28 x sqrt(45/365) = 9.83 dollars. The straddle's break-evens are 7.83 away, about 0.8 standard deviations. So the seller wins on the small moves, which are common, and loses on the large ones, which are not, and the premium is set so that at 28% realised volatility those two outcomes net to zero.

Every structure in this course, covered call, cash-secured put, credit spread, iron condor, is a version of that shape with the loss capped, moved, or financed differently. The economics do not change: frequent small gains, infrequent large losses, priced to break even at the implied volatility. The premium seller is paid for two things, variance risk (movement in general) and jump risk (sudden, large, usually downward movement). Those are exactly the events that hurt everything else in a portfolio at the same time, which is why the compensation exists and why it is not free.

## The evidence, with dates

The cleanest long records are Cboe's strategy benchmarks. The Cboe S&P 500 BuyWrite Index (BXM) holds the S&P 500 and writes a one-month at-the-money call each third Friday; its history begins June 20, 1986. The Cboe S&P 500 PutWrite Index (PUT) sells a one-month at-the-money SPX put collateralised by Treasury bills; Cboe's current factsheet series begins January 3, 2007, and the Wilshire study extends the back-tested history to June 30, 1986.

From the Cboe factsheets dated August 31, 2026: BXM returned 8.6% a year from June 20, 1986 with 10.7% annualised volatility and a maximum drawdown of -35.8%, against 11.2%, 15.2% and -50.9% for the S&P 500 total return index. PUT returned 7.1% a year from January 3, 2007 with 10.7% volatility and a -32.7% maximum drawdown, against 11.0%, 15.4% and -50.9%. Wilshire Analytics (2016), covering June 30, 1986 to June 30, 2016, reported PUT at 10.32% annualised with 9.91% standard deviation against 8.77% and 15.39% for the S&P 500. Hewitt EnnisKnupp (2012), covering June 30, 1986 to January 31, 2012, found BXM and the S&P 500 both at 9.2% annualised, with BXM's standard deviation 11.4% against 15.9%.

Read those four results together and the picture is consistent: premium selling on the index delivered lower volatility and smaller drawdowns, roughly equal returns through 2012 or 2016, and lower returns over windows that include the 2009 to 2026 bull market, when capped upside cost more than the premium paid. Whether the risk-adjusted improvement survives your costs and your discipline is what the rest of this course is about. None of these figures is a forecast.

## The tail you are paid for

Look at the drawdowns again. BXM's worst peak-to-trough loss was 35.8% of capital. In October 1987 the S&P 500 fell 21.5% in the month and BXM fell 17.5% (Hewitt EnnisKnupp, 2012). The VIX closed at a record 82.69 on March 16, 2020. Those are the events the premium compensates you for, and they arrive after long stretches of the strategy looking effortless.

Two properties of the tail matter for planning. First, it is correlated: short premium on twenty stocks is one position on market variance, because in a crash every implied volatility rises together. Second, it is skewed: BXM's monthly returns had a skew of -1.55 against -0.78 for the S&P 500 (Hewitt EnnisKnupp, 2012), the fingerprint of a strategy that collects small amounts often and gives back a large amount rarely. Sizing rules in Lesson 10 exist because of this shape.

## Worked example

The variance risk premium in dollars, on the model chain.

Sell the November 100 straddle for the chain mid: 4.16 + 3.67 = 7.83 per share, $783 per straddle.

Fair value depends on the volatility XYZ actually realises. An at-the-money straddle is close to linear in volatility, roughly 0.8 x S x sigma x sqrt(T). Check: 0.8 x 100 x 0.28 x sqrt(45/365) = 0.8 x 100 x 0.28 x 0.3511 = 7.86, within three cents of the model's 7.83.

Suppose XYZ realises 24% over the 45 days instead of 28%. Fair value at 24%: 0.8 x 100 x 0.24 x 0.3511 = 6.74. The seller's edge was 7.83 - 6.74 = 1.09 per share, $109 per straddle, or 14% of the credit. That is the variance risk premium on this trade: four volatility points, worth about a dollar.

Suppose instead XYZ realises 40%. Fair value: 0.8 x 100 x 0.40 x 0.3511 = 11.24. The seller's expected loss was 11.24 - 7.83 = 3.41 per share, $341. Twelve volatility points against you cost three times what four points in your favour earned. That asymmetry is not a property of this chain; it is what a short-variance payoff looks like.

Break-evens at expiry: 100 - 7.83 = 92.17 and 100 + 7.83 = 107.83. One-sigma move: 9.83. Ratio: 7.83 / 9.83 = 0.80 standard deviations, as above.

## Table

What the model chain pays, and the move each position must survive. Break-evens and the one-sigma move are at expiry, 45 days, 28% IV.

| Position | Credit (per share) | Credit as % of spot | Break-even(s) | Distance to break-even | One-sigma move |
|---|---|---|---|---|---|
| Short 100 straddle | 7.83 | 7.8% | 92.17 / 107.83 | 7.83 (0.80 sigma) | 9.83 |
| Short 95 put | 1.69 | 1.7% | 93.31 | 6.69 (0.68 sigma) | 9.83 |
| Short 105 call (covered) | 2.16 | 2.2% | 97.84 on the stock | 2.16 cushion | 9.83 |
| 95/90 bull put spread | 1.08 | 1.1% | 93.92 | 6.08 (0.62 sigma) | 9.83 |
| 90/85 + 110/115 iron condor | 1.04 | 1.0% | 88.96 / 111.04 | 11.04 (1.12 sigma) | 9.83 |

Every one of these will be built, priced and managed in the lessons that follow; keep the table, because the arithmetic does not change.

## Sources

- Carr, P. and Wu, L. (2009), "Variance Risk Premiums", *Review of Financial Studies* 22(3): https://doi.org/10.1093/rfs/hhn038
- Bakshi, G. and Kapadia, N. (2003), "Delta-Hedged Gains and the Negative Market Volatility Risk Premium", *Review of Financial Studies* 16(2): https://doi.org/10.1093/rfs/hhg002
- Bondarenko, O. (2014), "Why Are Put Options So Expensive?", *Quarterly Journal of Finance* 4(3): https://doi.org/10.1142/S2010139214500153
- Cboe Global Indices, BXM and PUT index factsheets and dashboards: https://www.cboe.com/us/indices/dashboard/bxm/ and https://www.cboe.com/us/indices/dashboard/put/
