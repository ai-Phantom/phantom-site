---
{
  "title": "Basis and Cash-and-Carry: Spot vs Perp vs Dated Futures",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "At 07:28 UTC on 2026-09-24 the Deribit index was 84,256.40 and BTC-30OCT26 marked at 84,719.61 with 36 days to expiry. The annualised basis was", "opts": ["0.55%", "5.57%", "55.7%", "1.34%"], "correct": 1, "explain": "463.21 divided by 84,256.40 is 0.5498% for 36 days; times 365 over 36 gives 5.57% simple annualised."},
    {"q": "The cash-and-carry trade is", "opts": ["Long the future, short spot", "Long spot, short the future or perp, held until the basis is captured", "Long both", "Long the perp, short the future"], "correct": 1, "explain": "You own the coin and sell it forward at a premium. Price risk cancels; you keep the premium, and on a perp you keep the funding."},
    {"q": "The 13-week Treasury bill yielded 4.028% on 2026-09-23. A carry trade grossing 5.57% annualised therefore earns, before fees and venue risk", "opts": ["5.57% above cash", "About 1.5% above cash", "Nothing above cash", "Negative carry"], "correct": 1, "explain": "5.57 minus 4.03 is about 1.5 points. Carry must be compared to the risk-free rate, not to zero, because the capital could simply sit in bills."},
    {"q": "When does a perp-based carry trade lose money even though spot and perp are perfectly hedged?", "opts": ["Never", "When funding turns negative for long enough that the short leg pays more than it collected, as in November 2022 at minus 0.25% per 8 hours", "When BTC rises", "When BTC falls"], "correct": 1, "explain": "The short perp receives funding only while it is positive. In a panic the perp trades at a discount and the short pays; the hedge protects price, not carry."},
    {"q": "Why does a dated-future carry have a known return while a perp carry does not?", "opts": ["Futures have no fees", "The future's basis is fixed when you sell it and is captured in full at expiry; perp funding is reset every period", "Perps cannot be shorted", "Futures settle in cash"], "correct": 1, "explain": "Selling the October future locked in $463.21 of basis on 1 BTC. A perp short's income depends on every future funding print."}
  ],
  "task": "Pull the current index, perpetual mark and the next three dated-future marks for BTC from any venue's public API and compute the simple annualised basis for each tenor."
}
---

## Basis

Basis is the difference between a derivative's price and the spot price of the thing it references. For a dated future it is future minus index; for a perpetual it is the premium that funding is computed on. Quoted as an annualised percentage, basis is the market's price for holding the coin forward: what a buyer will pay above spot to own BTC in October rather than today.

Basis exists because holding spot has a cost (capital tied up that could earn interest) and a benefit (you can lend it, or you simply want it). In a market where demand for leveraged long exposure exceeds the supply of coins to lend against it, the future trades above spot, the curve slopes up (contango), and someone who owns coins can be paid to sell them forward. That is cash-and-carry.

## The legs

Buy 1 BTC on a spot venue. Sell 1 BTC of a dated future, or 1 BTC of the perpetual, on a derivatives venue. Price risk is now hedged: if BTC rises $5,000 the spot leg gains it and the short loses it. What is left is the basis you sold, captured in full at the future's expiry when it settles to the index, or, on the perp, the stream of funding payments to the short for as long as they stay positive.

## Chart

![The cash-and-carry legs at the Deribit snapshot of 2026-09-24 07:28 UTC: buy 1 BTC at the 84,256.40 index, sell BTC-30OCT26 at the 84,719.61 mark to lock $463.21 of basis over 36 days (5.57% annualised), hold to expiry when the future cash-settles to the index, sell the spot, and compare the result to the 4.03% 13-week T-bill. Notes on each box give the numbers; fees and venue risk are the subject of the worked example and the capstone.](figures/cash-and-carry-legs.svg)

## Worked example

All prices come from Deribit's public book-summary and ticker endpoints at 2026-09-24 07:28 UTC, when the btc_usd index was 84,256.40. Expiries are at 08:00 UTC on the stated dates, so the October contract had 36.0 days to run.

**Step 1: the term structure.**

- BTC-PERPETUAL: mark 84,268.18. Premium 11.78, or 0.014%.
- BTC-30OCT26 (36 days): mark 84,719.61. Basis 84,719.61 − 84,256.40 = $463.21 = 0.5498%.
- BTC-27NOV26 (64 days): mark 85,079.43. Basis $823.03 = 0.9768%.
- BTC-25DEC26 (92 days): mark 85,388.59. Basis $1,132.19 = 1.3437%.
- BTC-26MAR27 (183 days): mark 86,466.99. Basis $2,210.59 = 2.6236%.
- BTC-25JUN27 (274 days): mark 87,614.92. Basis $3,358.52 = 3.9861%.

**Step 2: annualise.** Simple annualised basis = basis % × 365 ÷ days.

- October: 0.5498% × 365 ÷ 36 = 5.57%.
- November: 0.9768% × 365 ÷ 64 = 5.57%.
- December: 1.3437% × 365 ÷ 92 = 5.33%.
- March: 2.6236% × 365 ÷ 183 = 5.23%.
- June: 3.9861% × 365 ÷ 274 = 5.31%.

A flat curve at roughly 5.2 to 5.6% annualised. The perp, by comparison, was paying its shorts 0.004549% per 8 hours, 4.98% annualised on that print and 4.55% realised over the previous 30 days (lesson 6).

**Step 3: compare to cash.** Yahoo's ^IRX series, the 13-week Treasury bill discount rate, closed at 4.028% on 2026-09-23. The carry trade ties up $84,256.40 of capital for 36 days. That capital in bills would earn 84,256.40 × 0.04028 × 36 ÷ 365 = $334.74. The October basis is $463.21. Gross excess over cash: 463.21 − 334.74 = $128.47 on $84,256, or 1.5 points annualised. That is the whole prize before fees, and it is the number a carry trade must be judged against, because the alternative to the trade is not zero, it is the bill.

**Step 4: fees.** Use Kraken's published Tier 5 maker rate of 0.15% for the spot legs and Deribit's API-reported taker rate of 0.035% for the future.

- Spot buy: 84,256.40 × 0.0015 = $126.38. Spot sell at the end: another $126.38 (assume unchanged price). Total $252.77.
- Future sell: 84,719.61 × 0.00035 = $29.65. Cash settlement at expiry has no closing trade.
- Net carry: 463.21 − 252.77 − 29.65 = $180.79 over 36 days, 2.18% annualised.
- Versus the bill's $334.74: the trade underperforms cash by $153.95.

At Kraken's Tier 1 taker rate of 0.80% the spot legs cost $1,348.10 and the trade loses $914.54 outright. At Tier 12 (0.00% maker) the spot legs are free and net carry is $433.56, beating the bill by $98.82. The basis is the same for everyone; whether carry pays is decided almost entirely by which fee tier you are on.

**Step 5: the perp version.** Sell the perpetual instead of the October future. Over the previous 30 days the short would have collected 0.374% of notional (lesson 6): 84,268.18 × 0.00374 = $315.16. Fees: spot legs $252.77 as above, perp open and close at 0.035% each, 84,268.18 × 0.00035 × 2 = $58.99. Net: 315.16 − 252.77 − 58.99 = $3.40 for a month, 0.05% annualised, against $278.95 the bill would have paid over 30 days. And unlike the future, that $315.16 was not known in advance.

## When carry collapses

Three ways.

Funding turns negative. In November 2022 BitMEX's XBTUSD funding averaged −0.0171% per 8 hours and printed −0.2514% on 2022-11-11. A short perp in a carry trade was paying, not receiving, 275% annualised at the worst print. The spot leg was fine; the carry was gone and reversed.

The curve inverts. When the future trades below the index (backwardation), a new carry trade earns negative basis. An existing one, sold at a premium, still captures its locked basis at expiry, which is the dated future's structural advantage over the perp.

The venue fails. The two legs sit at two counterparties. Lesson 3 showed what happens to a balance on a failing venue: your short future's margin and profit become a petition-date dollar claim while your spot, if held elsewhere, stays a coin. A hedge across venues is a hedge against price, not against either venue.

One more failure that is not a collapse but feels like one: BTC rallies hard. The short leg loses in dollars every day the price rises and requires margin; the spot leg's gain is on a different venue and cannot be posted automatically. Lesson 8 computes the liquidation price of a 3x short, and the capstone requires an exit plan for exactly this.

## What the curve is telling you

Basis at 5.5% with bills at 4.0% says the market is paying about 1.5% a year for leveraged long BTC exposure, which is modest. In April 2021 the equivalent perp funding was over 300% annualised; the curve was screaming. A flat, low basis is a market that is not crowded on either side, which is a fact about positioning, not a prediction about price. Watch it the way an equity trader watches the put-call ratio: as a thermometer, never as a signal on its own.

## Future or perp: choosing the short leg

The dated future gives certainty: the basis is locked when you sell and paid in full at expiry, and there is no closing fee because it cash-settles. Its costs are a fixed horizon and a curve that may offer less than the perp is currently paying. The perp gives flexibility: no expiry, close whenever the funding stops paying, and in a euphoric month it can pay several times the curve. Its cost is that every 8-hour print is a new decision, and the income can reverse without notice. A carry trader who cannot watch the funding print at every timestamp belongs in the future; one who can, and who has margin ready on the derivatives venue, can use the perp and roll into the future when the curve pays more.

## Sources

- Deribit API, public/get_book_summary_by_currency and public/ticker, BTC futures (marks quoted above, 2026-09-24 07:28 UTC): https://docs.deribit.com/
- Yahoo Finance chart API, ^IRX (13-week Treasury bill), daily: https://query1.finance.yahoo.com/v8/finance/chart/%5EIRX?range=1mo&interval=1d
- Kraken, "Fee Schedule" (spot tiers used in the fee calculation): https://www.kraken.com/features/fee-schedule
- BitMEX REST API, GET /funding, XBTUSD, November 2022 prints: https://www.bitmex.com/api/explorer/
