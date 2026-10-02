---
{
  "title": "Perpetual Swaps: No Expiry, Funding, Mark vs Index, Liquidation",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "What keeps a perpetual swap's price near spot if the contract never expires?", "opts": ["The exchange sets the price", "Periodic funding payments between longs and shorts, in the direction that pushes the premium back toward zero", "Arbitrageurs delivering coins at expiry", "Nothing; perps drift freely"], "correct": 1, "explain": "With no delivery there is no convergence at expiry. Funding is the substitute: when the perp trades above the index, longs pay shorts, which makes being long expensive and pulls the premium down."},
    {"q": "At 07:28 UTC on 2026-09-24 Deribit's BTC-PERPETUAL mark was 84,268.18 and its index 84,256.40. The premium was", "opts": ["0.14%", "0.014%", "1.4%", "Negative"], "correct": 1, "explain": "(84,268.18 minus 84,256.40) divided by 84,256.40 is 0.00014, or 0.014%, about $11.78 on an $84,000 contract. Small premiums produce small funding rates."},
    {"q": "Why do exchanges liquidate on the mark price rather than the last traded price?", "opts": ["Mark price is always higher", "Last price can be pushed by a single trade in a thin book; the mark is anchored to the external index plus a smoothed basis", "It is a regulatory requirement", "Mark price updates less often"], "correct": 1, "explain": "A liquidation engine keyed to last price could be triggered by one manipulated print. Anchoring to the index across several spot venues makes that attack expensive."},
    {"q": "Deribit's BTC index is built from", "opts": ["Deribit's own perpetual price", "A composite of prices from several external spot exchanges, with outliers handled by rule", "The CME futures settlement", "Yahoo Finance"], "correct": 1, "explain": "The index documentation describes a basket of spot venues and the rule for excluding outliers. The whole point is that no single venue, including Deribit, controls the number that liquidations key off."},
    {"q": "A funding rate of 0.01% per 8 hours, the floor many venues default to when premium is near zero, annualises to roughly", "opts": ["0.01%", "3.65%", "10.95%", "36.5%"], "correct": 2, "explain": "Three payments a day for 365 days is 1,095 periods. 0.01% times 1,095 is 10.95% per year, paid by longs to shorts even when the perp trades exactly at the index."}
  ],
  "task": "Open a perpetual contract's page on any derivatives venue and write down, side by side, its last price, mark price, index price and the next funding rate with its countdown."
}
---

## A future with no delivery date

A dated future settles on a known day at a known reference price, and that certainty is what pins its price to spot: as expiry approaches, any gap between the future and the index is an arbitrage that closes. A perpetual swap removes the expiry. It is a linear or inverse contract on BTC (or ETH, or anything the venue lists) that you can hold forever, margined in a stablecoin or in the coin itself, with leverage set by the venue's margin table.

Remove the expiry and you remove the anchor. Something else has to make the perpetual's price track spot, and that something is funding.

## Funding

Every eight hours on most venues (Deribit accrues it continuously and reports an 8-hour equivalent), holders of open positions exchange a payment proportional to the contract's premium over the index. If the perpetual trades above the index, longs pay shorts; below, shorts pay longs. The venue keeps none of it. The payment is a percentage of position notional, charged to the account at the funding timestamp; if you are flat at that instant you pay and receive nothing.

The formula the industry inherited from BitMEX's perpetual contract guide is: funding rate = premium index + clamp(interest rate − premium index, −0.05%, +0.05%), where the premium index is the time-weighted average premium of the perpetual over the index during the period and the interest rate term reflects the borrowing cost differential between the two currencies, historically fixed at 0.01% per 8 hours. The clamp means that when the premium is close to zero, funding sits at the interest floor of 0.01%; when the premium is large, funding tracks it. Venues differ in their averaging window, their cap on the absolute rate, and whether they pay every eight, four or one hour, and the documentation for each is the only reliable source of its rules.

The economic effect is simple. Funding is a rent that the crowded side of the market pays to the other side. In a euphoric market longs pay a lot; in a panic shorts pay a lot. Lesson 6 prices that rent with real numbers, and lesson 7 shows how a hedged position can collect it.

## Mark price versus index price versus last price

A perpetual has three prices, and confusing them is how people get liquidated on a trade that was right.

The index is the spot reference: a composite of prices from several external exchanges, computed by rule. Deribit's index documentation describes the basket of venues and how outliers are excluded. The index is what funding is measured against and what the venue means by "spot".

The mark price is the index plus a smoothed estimate of the perpetual's fair basis, typically derived from the current funding rate over the time to the next payment. Liquidations and unrealised P&L are computed on the mark. On 2026-09-24 at 07:28 UTC Deribit's ticker endpoint reported BTC-PERPETUAL mark 84,268.18 against an index of 84,256.40.

The last price is whatever the most recent trade printed. It can be pushed by a single large order in a thin book, at 04:00 on a Sunday, to a level the index never visited. If liquidations keyed off the last price, that print would be an attack vector; anchoring them to the mark makes the attack require moving several spot venues at once.

The consequence for you: the price at which your position is liquidated is not the price on the chart. It is the mark, and the mark can differ from last by tens of dollars in calm conditions and hundreds in stress.

## Liquidation

Because you post only a fraction of notional as margin, the venue must close your position before your losses exceed the margin. Each contract has an initial margin (the minimum to open) and a maintenance margin (the minimum to keep). BitMEX's instrument endpoint for XBTUSD reports initMargin 0.01 and maintMargin 0.005: 1% to open, so 100x leverage, and 0.5% to hold. When your margin balance, marked to the mark price, falls to the maintenance level, the liquidation engine takes over the position and closes it, keeping whatever margin remains and paying the excess, if any, into an insurance fund. If the fund cannot cover a loss, venues socialise the shortfall across profitable traders through auto-deleveraging. Lesson 8 works through the arithmetic; the point here is that liquidation is an ordinary mechanism that fires at a price you can compute in advance, and most people never compute it.

## Worked example

Use Deribit's public ticker for BTC-PERPETUAL on 2026-09-24 at 07:28:07 UTC. The response reported mark price 84,268.18, index price 84,256.40, best bid 84,269.00, best ask 84,269.50, last price 84,269.00, funding_8h 0.00004549 and open interest 876,123,210 USD.

Step 1, the premium. Mark minus index: 84,268.18 − 84,256.40 = $11.78. As a fraction of the index: 11.78 ÷ 84,256.40 = 0.000140 = 0.014%.

Step 2, the funding rate. The reported 8-hour rate is 0.00004549, i.e. 0.004549% per 8 hours. That is below the 0.01% floor that a BitMEX-style formula would produce with a small positive premium, which tells you Deribit's method differs (it accrues continuously with a different interest assumption); read each venue's page rather than assuming.

Step 3, what a position pays. A long of 1 BTC notional, $84,268.18 at the mark, pays 84,268.18 × 0.00004549 = $3.83 per 8-hour period to the shorts. Per day: 3.83 × 3 = $11.50. If this rate persisted for a year: 0.00004549 × 3 × 365 = 0.0498, or 4.98% of notional, paid by longs to shorts.

Step 4, the size of the market. Open interest of $876 million on this one contract at one venue, at a mark of $84,268, is 876,123,210 ÷ 84,268.18 = 10,397 BTC of long positions matched by 10,397 BTC of shorts. Every 8 hours 10,397 × 84,268.18 × 0.00004549 = $39,861 moves from longs to shorts on this contract alone.

Step 5, the spread. Bid 84,269.00, ask 84,269.50: $0.50 wide, 0.0006% of price, on a contract with a $0.50 tick. The perpetual is the most liquid BTC instrument in the world; that liquidity is why it, not spot, is where price is discovered.

## Table

| Feature | Spot | Dated future (e.g. BTC-30OCT26) | Perpetual swap |
|---|---|---|---|
| What you hold | The coin (or an exchange IOU for it) | A contract settling at index on 2026-10-30 08:00 UTC | A contract with no expiry |
| Price anchor | It is the price | Convergence to index at expiry | Funding payments every 8 hours |
| Leverage | 1x unless borrowed | Set by margin table; Deribit lists maker 0.015%, taker 0.035% fees via its API | Same margin table; BitMEX XBTUSD shows 1% initial, 0.5% maintenance |
| Carrying cost | Custody only | Basis paid up front in the price | Funding paid or received continuously |
| Liquidation | None | On mark price | On mark price |
| Price on 2026-09-24 07:28 UTC | Index 84,256.40 | Mark 84,719.61 | Mark 84,268.18 |

## The three prices, one more time

Chart shows last. Funding is computed on the premium of the perp over the index. Liquidation fires on mark. If you take one thing from this lesson, take that sentence, and go and find all three numbers on the venue you use before you place a leveraged order.

## Sources

- BitMEX, "Perpetual Contracts Guide" (funding formula, premium index, interest rate clamp): https://www.bitmex.com/app/perpetualContractsGuide
- Deribit Knowledge Base, "Deribit Perpetual" (continuous funding, mark price): https://www.deribit.com/kb/deribit-perpetual
- Deribit Knowledge Base, "Deribit Index" (index composition and outlier rules): https://www.deribit.com/kb/deribit-index
- Deribit API documentation, public/ticker and public/get_instruments (values quoted above pulled 2026-09-24 07:28 UTC): https://docs.deribit.com/
