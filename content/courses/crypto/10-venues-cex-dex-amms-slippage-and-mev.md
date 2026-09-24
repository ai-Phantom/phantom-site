---
{
  "title": "The Venues: Centralised Exchanges, DEXs, AMMs, Slippage and MEV",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A constant-product AMM pool holds 1,000 BTC and 84,256,400 USDC. Its quoted price is", "opts": ["$1,000", "$84,256.40 per BTC", "$84.26", "Undefined without an order book"], "correct": 1, "explain": "The marginal price is the ratio of reserves, 84,256,400 divided by 1,000. There is no order book; the curve x times y = k is the book."},
    {"q": "Buying BTC from that pool with $1,000,000 (after a 0.30% fee) returns 11.6945 BTC. The average price paid is", "opts": ["$84,256", "$85,510, about 1.49% above the pool price", "$94,510", "$84,509"], "correct": 1, "explain": "1,000,000 divided by 11.6945 is $85,510. The trade moved the pool's reserves and therefore its price; the buyer paid the average along the curve plus the fee."},
    {"q": "A sandwich attack is", "opts": ["A venue outage", "A searcher placing a buy before your pending swap and a sell after it, profiting from the price impact your trade creates", "A hardware wallet exploit", "A type of stablecoin"], "correct": 1, "explain": "Because pending transactions are visible and their ordering can be bought, your slippage becomes someone else's profit. Daian et al. documented this class of extraction in 2019."},
    {"q": "On a centralised exchange your counterparty risk is the exchange. On a DEX it is", "opts": ["Nobody, ever", "The smart contract's code and the chain it runs on, plus whoever can reorder your transaction", "The SEC", "The pool's largest liquidity provider"], "correct": 1, "explain": "A DEX removes the custodian but adds contract risk, chain risk and ordering risk. It is a different set of risks, not a smaller one."},
    {"q": "Why is a 0.30% pool fee not the full cost of an AMM trade?", "opts": ["It is the full cost", "Price impact from moving along the curve, gas, and any MEV extraction come on top; for a $10,000 trade in the example the all-in cost was 0.313%, for $1M it was 1.49%", "The fee is refunded", "Gas is free"], "correct": 1, "explain": "The fee is fixed; impact scales with trade size relative to the pool's reserves."}
  ],
  "task": "Find one AMM pool for BTC or ETH, note its reserves, and compute by hand the average price you would pay for a trade equal to 1% of the pool's reserves."
}
---

## Two kinds of venue

Everything in lessons 2 to 8 happened on a centralised exchange: a company that holds your assets, runs an order book on its own servers, and settles trades in its database. A decentralised exchange (DEX) replaces all three with a smart contract on a public chain. You keep your keys, the contract holds pooled liquidity, and every trade is a transaction on the ledger that anyone can see before it confirms.

Both are called exchanges. They share almost nothing else. This lesson covers the DEX model at survey depth, the arithmetic of trading against a pool, and the two costs that do not exist on a centralised venue: price impact from a bonding curve and extraction by whoever orders the block.

## Automated market makers

Most DEX volume runs through automated market makers rather than order books. The design that defined the category, Uniswap v2 (Adams, Zinsmeister and Robinson, 2020), keeps a pool of two tokens with reserves x and y and enforces one rule: after any trade, the product x × y must be at least what it was before, minus the fee. The pool's marginal price is y ÷ x. There are no quotes, no makers and no queue; liquidity providers deposit both tokens, earn the fee on every trade, and bear the risk that the pool's ratio drifts away from the outside market.

Uniswap v3 refined this by letting providers concentrate liquidity within price ranges, which makes a pool behave more like an order book near the current price and less like one far from it. The constant-product formula is still the right mental model, and the worked example uses it.

The trade-off against an order book is exact. An order book gives you a known price for a known size until the level is exhausted; a pool gives you a continuous curve where every unit costs more than the last. For a trade that is small relative to the reserves the difference is a few basis points; for a large one it is the whole trade.

## Chart

![Average price paid, as a percentage above the pool's quoted 84,256.40, when buying BTC from a constant-product pool of 1,000 BTC and 84,256,400 USDC with a 0.30% fee, for trade sizes from $10,000 to $10 million, computed in the worked example from x times y = k. The marked point is the $1 million trade: 11.6945 BTC at an average of $85,510.](figures/amm-price-impact.svg)

## Worked example

Set up a pool at the Deribit index of 2026-09-24 07:28 UTC: x = 1,000 BTC and y = 84,256,400 USDC, so the price is 84,256,400 ÷ 1,000 = $84,256.40 and k = x × y = 84,256,400,000. The fee is 0.30% of the input, charged before the swap.

You want to buy BTC with $1,000,000 of USDC.

- Fee: 1,000,000 × 0.003 = $3,000. Effective input Δy = $997,000.
- New USDC reserve: 84,256,400 + 997,000 = 85,253,400.
- New BTC reserve from the invariant: x' = k ÷ y' = 84,256,400,000 ÷ 85,253,400 = 988.3055 BTC.
- BTC received: 1,000 − 988.3055 = 11.6945 BTC.
- Average price: 1,000,000 ÷ 11.6945 = $85,509.93.
- Cost above the quoted price: 85,509.93 ÷ 84,256.40 − 1 = 1.488%, of which 0.30% is the fee and about 1.19% is price impact.
- The pool's new marginal price: 85,253,400 ÷ 988.3055 = $86,262.13, 2.38% above where it started. That is the price the next trader sees, and the gap between it and the outside market is what arbitrageurs will close, at the liquidity providers' expense.

Repeat for other sizes (all-in cost above the quote, fee included): $10,000 buys 0.1183 BTC at 0.313%; $100,000 buys 1.1819 BTC at 0.420%; $500,000 buys 5.8817 BTC at 0.894%; $2 million buys 23.1187 BTC at 2.675%; $5 million buys 55.8597 BTC at 6.235%; $10 million buys 105.809 BTC at 12.169%. A $10 million trade against a pool of $84 million a side pays 12% more than the quote. Compare lesson 2, where Coinbase's book showed 78 BTC of asks within $1,000 (1.2%) of the touch: for that size, at that moment, the order book was the cheaper venue by an order of magnitude. For $10,000, the pool's 0.313% is competitive with an entry-tier taker fee of 0.80% on a centralised venue and worse than a Tier 5 maker at 0.15%.

The slippage tolerance you set on a DEX trade is the maximum you will accept between the price you saw and the price you get. Set it wide and you invite the next section; set it tight and your transaction fails, and you pay the gas anyway.

## MEV

On a public chain every pending transaction sits in a mempool before it is included in a block, and whoever builds the block chooses the order. Daian et al. (2019), in "Flash Boys 2.0", documented bots paying for priority to front-run and back-run DEX trades and named the phenomenon miner extractable value, later maximal extractable value (MEV).

The version that hits a trader directly is the sandwich. A searcher sees your $1 million buy pending, inserts a buy ahead of it (pushing the pool price up), lets your trade execute at the worse price, then sells immediately after, capturing the impact your trade created, within your slippage tolerance. Your 1.49% cost can become 3% with no change in the pool's rules, and the extra is not a fee anyone disclosed. Mitigations exist, including private transaction relays and tighter slippage, and are venue- and chain-specific; the survey-level point is that on a DEX the ordering of trades is for sale and you are not the buyer.

## Centralised and decentralised, side by side

| | Centralised exchange | Decentralised exchange (AMM) |
|---|---|---|
| Custody | Exchange holds keys; your balance is an IOU (lesson 1) | You hold keys; contract holds pooled liquidity |
| Price formation | Order book, price-time priority | Bonding curve; price = ratio of reserves |
| Cost of a small trade | Maker/taker fee (0.00% to 0.80% by tier), tiny spread | Pool fee (typically 0.05% to 1.00%) plus gas |
| Cost of a large trade | Walks the book; depth visible in advance | Price impact from the curve, computable from reserves |
| Hidden cost | Venue insolvency, withdrawal halts | MEV extraction, contract exploits, chain congestion |
| Trading hours | 24/7, venue can halt | 24/7, chain can congest but not halt trading |
| Counterparty | The company | The code, the chain, and the block builder |
| Recourse | Terms of service, bankruptcy court | None |

## Where this leaves you

For BTC and ETH in size, the centralised order book is usually cheaper to trade and the DEX is safer to hold. That is the same split as lesson 1: trade where the liquidity is, keep the balance where the keys are yours. The DEX earns its place for assets that no centralised venue lists, for traders who will not accept a custodian at any price, and for anyone who wants to see, in the contract's reserves, exactly what liquidity exists rather than trusting a venue's depth chart.

## Sources

- Hayden Adams, Noah Zinsmeister, Dan Robinson, "Uniswap v2 Core", March 2020: https://app.uniswap.org/whitepaper.pdf
- Hayden Adams et al., "Uniswap v3 Core", March 2021: https://uniswap.org/whitepaper-v3.pdf
- Philip Daian et al., "Flash Boys 2.0: Frontrunning, Transaction Reordering, and Consensus Instability in Decentralized Exchanges", arXiv:1904.05234, 2019: https://arxiv.org/abs/1904.05234
- Deribit API, public/get_index_price, btc_usd (the 84,256.40 pool price): https://docs.deribit.com/
