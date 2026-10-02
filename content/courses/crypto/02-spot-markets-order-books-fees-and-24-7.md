---
{
  "title": "Spot Markets: Order Books, Maker-Taker Fees and 24/7 Trading",
  "duration": "17 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "On Kraken's published fee schedule (Tier 1, under $2,500 of 30-day volume), what is the taker fee for spot?", "opts": ["0.10%", "0.40%", "0.80%", "0.035%"], "correct": 2, "explain": "The Tier 1 row reads maker 0.40%, taker 0.80%. A round trip at that tier costs 1.6% of notional before the spread, which is why fee tier matters more than the spread for small accounts."},
    {"q": "At 07:30 UTC on 2026-09-24 Kraken's best bid was 84,397.10 and best ask 84,397.20. What was the spread in basis points?", "opts": ["About 1 bp", "About 0.01 bp", "About 10 bp", "About 100 bp"], "correct": 1, "explain": "0.10 divided by the 84,397.15 midpoint is 0.0000012, or 0.012 bp. The spread was negligible; the fee was 80 bp."},
    {"q": "Which order pays the maker fee?", "opts": ["A market order", "A limit order that rests on the book and is later matched", "Any order over $10,000", "Any order placed at the weekend"], "correct": 1, "explain": "Makers add resting liquidity and pay the lower rate; takers remove it and pay the higher rate. A limit order priced through the book executes immediately and is charged as a taker."},
    {"q": "Over the two years to 2026-09-24, BTC's average absolute daily move was 1.87% on weekdays and 1.07% on weekends. What does that imply for a stop left unattended on Saturday?", "opts": ["Weekends are riskless", "It can be hit; weekend moves are smaller on average but the market never closes and liquidity is thinner", "Stops cannot trigger at weekends", "Weekend fills are always better"], "correct": 1, "explain": "Smaller average moves do not mean no moves; the tails still occur, and with fewer participants a stop can fill further from its trigger."},
    {"q": "Why does an exchange's 30-day volume ranking matter to a trader who never looks at it?", "opts": ["It sets the price of BTC", "It determines the maker and taker rates every one of their fills is charged", "It is only relevant to market makers", "It changes the spread"], "correct": 1, "explain": "Fee tiers are keyed to 30-day volume (or assets on platform). The rate applied to your fills is decided by that ranking, not by the order type alone."}
  ],
  "task": "Open the fee schedule page of any exchange you use, find the exact maker and taker rates your account is charged today, and write them at the top of your trading journal."
}
---

## What a spot market is

A spot market exchanges the asset for cash now, at the price the order book shows. In crypto that means you receive a credit of BTC on the venue (lesson 1) in exchange for a debit of dollars or a dollar stablecoin (lesson 4). Nothing about the matching engine is exotic: bids on one side, asks on the other, price-time priority, partial fills. What is different from equities is who runs it, what it costs, and when it is open.

There is no national best bid and offer. Each exchange runs its own book, sets its own fees, and quotes its own price. On 2026-09-24 at about 07:30 UTC Kraken's best ask for BTC/USD was 84,397.20 and Coinbase Exchange's was 84,412.83, a 15-dollar difference at the same moment. Arbitrageurs keep venues within a few basis points of each other most of the time, but there is no rule that forces it, and in stress the gaps widen.

## Reading the book

Public order-book endpoints let you see the book without an account. At 07:30:05 UTC on 2026-09-24 Kraken's XBT/USD depth endpoint returned:

- Best bid 84,397.10 for 1.232 BTC; best ask 84,397.20 for 8.369 BTC.
- Ten levels of bids summed to 10.863 BTC; ten levels of asks to 8.461 BTC.

At the same moment Coinbase Exchange's level-2 book showed best bid 84,412.82 for 0.147 BTC and best ask 84,412.83 for 0.00006 BTC, with 77.4 BTC of bids and 78.3 BTC of asks resting within $1,000 of the touch. Its 24-hour volume was 7,654.7 BTC and its 30-day volume 188,672 BTC, which at $84,000 is roughly $16 billion a month on one venue.

Two things to notice. The spread at the touch was one cent on Coinbase and ten cents on Kraken: for a liquid pair on a large venue, the quoted spread is not where your cost lives. And the size at the touch is small and changes every second; the depth figures a few levels down tell you what a market order of size will actually pay.

## Maker-taker fees

Every crypto exchange charges a percentage of notional per fill, split by whether you added liquidity (maker: a resting limit order that was later matched) or removed it (taker: a market order, or a limit order priced through the book). Rates step down with your 30-day volume.

Kraken publishes its spot schedule at kraken.com/features/fee-schedule. As read on 2026-09-24, the table starts at Tier 1 (under $2,500 of 30-day volume): maker 0.40%, taker 0.80%. Tier 5 ($50,000+): maker 0.15%, taker 0.30%. Tier 12 ($10 million+): maker 0.00%, taker 0.10%. Other venues use different numbers and different tier boundaries, and some quote a single fee for retail "instant buy" products that is higher still; the page's own note says instant-buy volume does not count toward the tiers. The structure is what matters: the rate you pay is set by your ranking, not by the order.

Compare that to equities, where commission is usually zero and the cost is the spread plus payment for order flow measured in fractions of a cent. A crypto spot trader at an entry tier pays more in explicit fees per round trip than most equity day traders pay in a month.

## Worked example

You want to buy 0.5 BTC on 2026-09-24 at 07:30 UTC using the Kraken book above, and you are at Tier 1.

Market order (taker):

- The best ask has 8.369 BTC available at 84,397.20, so your 0.5 BTC fills in full at the touch.
- Notional: 0.5 × 84,397.20 = $42,198.60.
- Taker fee at 0.80%: 42,198.60 × 0.008 = $337.59.
- All-in cost: $42,536.19, an effective price of $85,072.38 per BTC, 0.80% above the quote.

Limit order at the bid (maker), assuming it fills:

- Price 84,397.10; notional 0.5 × 84,397.10 = $42,198.55.
- Maker fee at 0.40%: 42,198.55 × 0.004 = $168.79.
- All-in cost: $42,367.34, effective price $84,734.68, 0.40% above the quote.

The spread between the two quotes was 84,397.20 − 84,397.10 = $0.10, which is 0.10 ÷ 84,397.15 = 0.000012 = 0.012 basis points. The fee difference between the two orders was $168.80. The spread was irrelevant; the fee choice was 1,700 times larger.

Round trip at Tier 1 taker: 0.80% in and 0.80% out, so BTC must rise 1.6% before the trade is at zero. At Tier 5 maker, 0.15% each way, the hurdle is 0.30%. For an active trader, moving down the tier table is worth more than any indicator in the technical analysis course, and the only ways down are volume, which costs fees, or assets on the platform, which is custody risk.

Repeat the taker calculation at Coinbase's touch of 84,412.83: notional $42,206.42. The venue's fee schedule is behind an account login and differs by product, so the fee line depends on your tier there; the method is the same. Note that a market order for 0.5 BTC would not have filled at the touch, where only 0.00006 BTC was resting, but would have walked a few cents down a book with 78 BTC of asks within $1,000.

## 24/7 and what it does to you

Crypto spot trades every hour of every day. Yahoo Finance's daily BTC-USD series has 1,827 bars in the five years to 2026-09-24; SPY has about 1,255 over the same span. Three consequences follow.

Weekends are real trading days with fewer participants. Over the two years to 2026-09-24 the mean absolute close-to-close move (Yahoo daily bars, close at 00:00 UTC) was 1.87% on weekdays and 1.07% on Saturdays and Sundays. Moves are smaller on average but not absent, and a stop-loss left on the book fills against a thinner book.

There is no opening auction and no close. Equity traders lean on the 09:30 open and 16:00 close for volume; crypto volume clusters around the US equity session and around the 00:00 UTC and 08:00 UTC funding timestamps of the perpetual markets (lesson 5), but there is no bell. A daily bar's open and close are conventions set by whoever draws the chart, and Yahoo's UTC-midnight bars differ from an exchange's own daily candles.

You are never flat by default. An equity day trader is forced flat by the close; a crypto position carries risk through every night and weekend unless you close it deliberately, and margin calls on the perpetual venues arrive at 03:00 on a Sunday as readily as at 10:00 on a Tuesday.

## Table

| Item, 2026-09-24 about 07:30 UTC | Kraken XBT/USD | Coinbase Exchange BTC-USD |
|---|---|---|
| Best bid / best ask | 84,397.10 / 84,397.20 | 84,412.82 / 84,412.83 |
| Quoted spread | $0.10 (0.012 bp) | $0.01 (0.001 bp) |
| Size at best ask | 8.369 BTC | 0.00006 BTC |
| Depth shown | 10 levels: 10.863 BTC bid, 8.461 BTC ask | 77.4 BTC bid, 78.3 BTC ask within $1,000 |
| 24h volume | 3,446 BTC (ticker endpoint) | 7,654.7 BTC (stats endpoint) |
| Entry-tier fees | maker 0.40%, taker 0.80% (published schedule) | schedule requires login; varies by product and tier |

The numbers change every second; the shape does not. Spread tiny, size at the touch tiny, depth adequate a few dollars away, fees enormous relative to all three.

## Sources

- Kraken, "Fee Schedule" (spot maker-taker tiers, read 2026-09-24): https://www.kraken.com/features/fee-schedule
- Kraken REST API documentation, "Get Order Book" (Depth endpoint used above): https://docs.kraken.com/api/docs/rest-api/get-order-book
- Coinbase Exchange API reference, "Get product book" (level-2 book used above): https://docs.cdp.coinbase.com/exchange/reference/exchangerestapi_getproductbook
- Yahoo Finance chart API, BTC-USD daily bars, 5-year range: https://query1.finance.yahoo.com/v8/finance/chart/BTC-USD?range=5y&interval=1d
