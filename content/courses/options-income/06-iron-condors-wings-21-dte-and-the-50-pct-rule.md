---
{
  "title": "Iron Condors: Wings, 21 DTE and the 50% Rule",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The chain's condor is short the 90 put (0.61) and 110 call (1.00), long the 85 put (0.16) and 115 call (0.41). Credit and maximum loss per share?", "opts": ["1.61 and 3.39", "1.04 and 3.96", "1.04 and 8.96", "2.18 and 2.82"], "correct": 1, "explain": "Credit = (0.61 - 0.16) + (1.00 - 0.41) = 0.45 + 0.59 = 1.04. Only one wing can be breached at expiry, so max loss = 5.00 - 1.04 = 3.96."},
    {"q": "Why is the buying-power reduction on the condor $396 and not $792?", "opts": ["Brokers discount condors by 50%", "Because XYZ cannot finish below 90 and above 110 at the same time, so only one 5-wide spread can lose", "Because the long wings are free", "Because the put side is cash-secured"], "correct": 1, "explain": "The two spreads share the same expiry and the losses are mutually exclusive, so exchanges and FINRA require margin on one side only: width minus total credit."},
    {"q": "With XYZ unchanged at 100 on October 16 (21 DTE) the condor marks at about 0.36. What fraction of the maximum profit has been earned in the first 24 of 45 days?", "opts": ["36%", "50%", "65%", "24%"], "correct": 2, "explain": "1.04 - 0.36 = 0.68 earned, 0.68 / 1.04 = 65%. The remaining 0.36 must be earned over the last 21 days while gamma rises, which is the argument for managing early."},
    {"q": "The 50% profit target on the chain's condor means closing when the four legs can be bought back for:", "opts": ["0.52", "0.50", "1.04", "0.26"], "correct": 0, "explain": "Half the 1.04 credit is 0.52 profit, so you buy the condor back at 1.04 - 0.52 = 0.52."},
    {"q": "Which statement about the evidence for '50% and 21 DTE' is accurate?", "opts": ["It is established in the peer-reviewed literature", "Cboe's CNDR index proves it", "It comes from broker-published backtests and from the gamma-theta arithmetic; a trader should test it on their own fills rather than assume it", "It applies to every short-premium structure equally"], "correct": 2, "explain": "The rules are widely used and the theta-versus-gamma logic behind them is sound, but the published support is broker research, not refereed studies. The Cboe CNDR index, by contrast, holds to expiration with no adjustments, which makes it a benchmark for the unmanaged version only."}
  ],
  "task": "Pull the Cboe CNDR index history from the Cboe dashboard, note its base date and methodology, and write two sentences on how a held-to-expiry benchmark differs from a condor managed at 21 DTE."
}
---

## Four legs, one bet

An iron condor is the bull put spread and the bear call spread from Lesson 5, sold together in the same expiration with both short strikes out of the money. On the chain: sell the November 90 put at 0.61 and buy the 85 put at 0.16 (put side credit 0.45); sell the 110 call at 1.00 and buy the 115 call at 0.41 (call side credit 0.59). Total credit 1.04 per share, $104 per condor. Both wings are 5 wide.

The position profits if XYZ finishes between the two break-evens, 90 - 1.04 = 88.96 and 110 + 1.04 = 111.04, a range of 22 points, plus or minus 11% from today's price, or about 1.1 standard deviations each way at 28% volatility over 45 days. From the model, the probability of finishing inside that range is 74%. The maximum loss is the width of one wing minus the whole credit, 5.00 - 1.04 = 3.96, because the stock cannot finish below 90 and above 110 at once. So the buying-power reduction is $396 per condor, not $792, and the return on capital if it expires worthless is 104 / 396 = 26%.

The Greeks at entry, from the chain: net delta is -0.12 (put) - 0.19 (call) with signs for the short legs, roughly +0.12 - 0.19 = -0.07 per share, a small short bias because the flat-volatility model prices the call side richer; net theta about +0.03 per day; net vega negative; net gamma negative and small, growing as expiration approaches. The condor is a pure short-variance position: it wants the stock to stay put and implied volatility to fall.

## Wing width and the short strikes

Two decisions define the condor: where the short strikes go and how wide the wings are.

The short strikes set the probability of profit and the credit, in opposite directions, exactly as in Lesson 5. The 90/110 shorts are near 12- and 19-delta on the model chain. Move to 95/105 and the credit rises to (1.69 - 0.61) + (2.16 - 1.00) = 2.24 with POP dropping to about 47%; move to 85/115 and the credit falls below 0.40 for POP around 90%. Cboe's S&P 500 Iron Condor Index (CNDR) uses shorts at 20-delta and wings at 5-delta, monthly, and that is a sensible default: far enough out that the position is a volatility bet rather than a direction bet, close enough that the credit survives the bid/ask.

Wing width sets the maximum loss and the buying power. A 5-wide wing on the chain caps the loss at 3.96; a 10-wide wing (buy the 80 put at 0.03 and the 120 call at 0.15 instead) would collect 1.43 but risk 8.57, and require $857 per condor. Wider wings collect more credit per condor and less per dollar of risk; on this chain the 5-wide earns 26% on capital and the 10-wide 17%. Narrow wings behave like a smaller number of wide ones, but the cost of the long options is a larger share of the credit. Choose the width by the max-loss budget (Lesson 10) and the size by the width, not the other way round.

Notice a real-market wrinkle the model hides. Index and stock chains have skew: puts at the same distance trade at higher implied volatility than calls. On a real chain the 90 put would bring in more than 0.61 and the 110 call less than 1.00, so a delta-balanced condor sits with its put strike further from the stock than its call strike in price terms. The model's flat 28% is why the call side here pays more. Build real condors by delta, not by equal distance.

## Managing at 21 DTE

You know from the previous course that theta and gamma both accelerate into expiration, and that an option's gamma is concentrated near its strike in the last three weeks. That is the argument for the 21-DTE rule: close or roll the condor when 21 days remain, whatever it is worth, rather than holding for the last of the premium.

The chain gives the arithmetic. On October 16, 21 days before expiry, with XYZ still at 100 and IV still 28%, the four legs mark at 0.15 (90 put), 0.01 (85 put), 0.27 (110 call) and 0.05 (115 call). The condor is worth 0.36. You have earned 1.04 - 0.36 = 0.68, 65% of the maximum, in 24 of the 45 days. The remaining 0.36 is what you are paid to hold through the period when a 5% move puts a short strike in play and the P&L swings fastest. At 103 on the same date the condor marks 0.54 (profit 0.50, 48%); at 97 it marks 0.41 (profit 0.63, 61%). At 92 with IV up to 34%, a plausible pair, it marks 1.41 and the position is under water by 0.37 with 21 days of rising gamma ahead.

The 50% profit rule is the other half: close whenever the condor can be bought back for half the credit, 0.52 here, regardless of the calendar. On an unchanged stock the model reaches 0.52 around day 18 of 45, so the rule typically fires before 21 DTE and the two rules together mean you rarely hold a condor into its final three weeks.

## What the evidence is, and is not

Be clear about where these rules come from. The gamma-theta logic is textbook and you can verify it on any chain. The specific numbers, 50% and 21 days, come from backtests published by brokers, tastytrade's research in particular, which are not peer-reviewed and are run on their own fills and methodology. They are a reasonable starting point, not a finding. Test them on your own record.

The peer-reviewed literature and Cboe's benchmark say something different and complementary. CNDR, base date June 20, 1986, launched August 3, 2015, sells the 20-delta SPX put and call and buys the 5-delta wings monthly, holds every position to expiration with no adjustments, and keeps a Treasury bill account of ten times the maximum loss. It is the unmanaged version of this lesson. Its history is the honest answer to "what does a mechanical condor earn"; your management rules are a claim that you can do better than that, and the burden of proof is on the rules.

## Worked example

November iron condor on the chain, per condor, commissions excluded.

Legs at mid: sell 90 put 0.61, buy 85 put 0.16, sell 110 call 1.00, buy 115 call 0.41.

Credit: (0.61 - 0.16) + (1.00 - 0.41) = 0.45 + 0.59 = 1.04 ($104).
Maximum loss: 5.00 - 1.04 = 3.96 ($396). Buying-power reduction: $396.
Break-evens: 90 - 1.04 = 88.96; 110 + 1.04 = 111.04. POP from the model: 74%.
Return on capital if expired worthless: 104 / 396 = 26.3%.

At market fills, half the bid/ask on each leg (0.03, 0.02, 0.04, 0.03): credit 1.04 - 0.12 = 0.92 ($92), maximum loss 4.08. The toll is 12% of the credit.

October 16 (21 DTE), XYZ 100, IV 28%: marks 0.15 - 0.01 + 0.27 - 0.05 = 0.36. Profit if closed: 1.04 - 0.36 = 0.68 ($68), 65% of maximum, in 24 days. Return on the $396: 17.2%.

50% target: buy back at 1.04 / 2 = 0.52, profit $52. Reached, on an unchanged stock, about day 18.

October 16, XYZ 92, IV 34%: marks 1.98 - 0.60 + 0.04 - 0.01 = 1.41. Loss if closed: 1.04 - 1.41 = -0.37 ($37). The alternative is to hold 21 days with the short 90 put 2 points away: the maximum loss is still $396 and the probability of touching 88.96 from 92 in three weeks is not small.

Expiry outcomes, held: XYZ 106, all legs expire, +$104. XYZ 97, +$104. XYZ 84, put side fully in the money, 1.04 - 5.00 = -$396.

## Chart

![Iron condor on the model chain: short November 90 put at 0.61 and 110 call at 1.00, long 85 put at 0.16 and 115 call at 0.41; payoff per share at expiry, credit 1.04, break-evens 88.96 and 111.04, maximum loss 3.96 beyond either wing. Source: the lesson's worked example.](figures/iron-condor-payoff.svg)

The flat top is 22 points wide; the two cliffs are 5 points each. Almost all of the position's time is spent on the top and almost all of its losses happen on the cliffs.

## Sources

- Cboe Global Indices, S&P 500 Iron Condor Index (CNDR) methodology: https://cdn.cboe.com/api/global/us_indices/governance/CNDR_Methodology.pdf
- Cboe Global Markets, Margin Manual (iron condor requirement on one side): https://www.cboe.com/us/options/strategy_based_margin/
- Options Clearing Corporation, *Characteristics and Risks of Standardized Options*: https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document
