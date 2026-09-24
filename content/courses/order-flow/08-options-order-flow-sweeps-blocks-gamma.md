---
{
  "title": "Options Order Flow: Sweeps, Blocks, Open Interest, and Dealer Gamma Hedging",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Dealers are net short 40,000 contracts of a call with gamma 0.04 per share. The stock rises $2. To stay delta-neutral they must:", "opts": ["Sell 320,000 shares", "Buy 320,000 shares", "Buy 3,200 shares", "Do nothing"], "correct": 1, "explain": "Delta change = 0.04 × 2 = 0.08 per share; × 40,000 × 100 = 320,000 shares. Short calls lose delta as price rises, so dealers buy to rebalance, in the direction of the move."},
    {"q": "An options 'sweep' on the tape means:", "opts": ["A single large print on one exchange", "An order split across multiple exchanges and executed near-simultaneously, usually via intermarket sweep orders", "A dealer hedge", "An expiring contract"], "correct": 1, "explain": "Sweeps are aggressive orders that take liquidity on several venues at once. They indicate urgency, not necessarily information, and are routinely used by execution algorithms."},
    {"q": "In August 2025, 0DTE contracts were what share of SPX options volume, according to Cboe?", "opts": ["About 20%", "About 40%", "62.4%", "90%"], "correct": 2, "explain": "A record 62.4%, with roughly 2.4 million 0DTE contracts a day and flow split about 53% retail, 47% institutional."},
    {"q": "Open interest in a strike rises by 15,000 contracts overnight after 15,000 traded at the ask. What can you conclude?", "opts": ["A buyer opened 15,000 long calls", "Someone opened a new position of 15,000; whether the aggressor was opening a long or a dealer was opening a short hedge is not identifiable from OI alone", "Dealers are short gamma", "The stock will rise"], "correct": 1, "explain": "OI is net of opens and closes across both sides. It confirms a new position exists; it does not say who holds which side or why."},
    {"q": "Ni, Pearson, Poteshman and White (2021) found that the stock-price effect of options hedging:", "opts": ["Does not exist", "Is pervasive and consistent with dealer delta hedging, with larger effects when dealers' net gamma is larger", "Only occurs at expiration", "Is illegal"], "correct": 1, "explain": "Their result is the primary empirical support for the gamma-feedback mechanism, and it is a description of average effects, not a trading signal."}
  ],
  "task": "Pull the open-interest change for the five nearest strikes in SPY after tomorrow's close and estimate the share equivalent of the delta change if the underlying moves 1%."
}
---

## Why options flow feeds back into stocks

Every options trade has a counterparty, and in listed options that counterparty is usually a market maker who does not want directional exposure. The dealer hedges: buys stock against calls it sold, sells stock against puts it sold. As the stock moves, the option's delta changes, and the dealer's hedge must change with it. Gamma is the rate at which delta changes, and dealers' aggregate gamma position determines whether their hedging pushes with the stock's move or against it. That feedback is the one part of options flow with a mechanical link to the stock, and it is the part this lesson works through in numbers.

The rest of options flow, sweeps, blocks and open-interest changes, is popular with signal services and mostly describes urgency and size rather than information. Both halves are worth knowing; only one has a mechanism.

## The scale of the market

The Options Clearing Corporation cleared 12.2 billion contracts in 2024, up 10.6% on 2023 and a record for the fifth consecutive year. Cboe's Q3 2025 industry review reported market-wide average daily volume of 59 million contracts through September 2025, up 22% on 2024, with single-stock options up 25%, ETF options up 18% and index options up 17% year to date, and retail traders accounting for nearly half of daily volume. Large institutional blocks of 1,000 or more contracts averaged nearly 10 million contracts a day.

Inside that, SPX index options averaged a record 3.8 million contracts a day in Q3 2025, and zero-days-to-expiry contracts were 2.15 million of those, 57%. In August 2025 the 0DTE share hit a record 62.4% (about 2.4 million contracts a day), with flow split roughly 53% retail and 47% institutional. For the full year 2025, 0DTE averaged 2.3 million contracts a day, 59% of SPX volume. Short-dated options have very high gamma near the money, which is why the hedging arithmetic below matters more now than it did in 2019.

## Sweeps, blocks and open interest

A sweep is an order routed to several options exchanges at once, typically with intermarket sweep orders that ignore better-priced quotes elsewhere because the sender is taking all of them. On the tape it appears as a burst of prints at the same strike across venues within milliseconds. What it tells you is that someone wanted a lot of contracts immediately. Execution algorithms sweep routinely, so does anyone hedging a stock position on a deadline, and so does a trader acting on information. The tape does not say which.

A block is a large print negotiated off the screen and reported through a single exchange, often as part of a spread or a stock-tied package. Many blocks are one leg of a multi-leg strategy: a large call print at the ask that looks like a bullish bet is frequently a covered-call overwrite or the long leg of a collar. Classifying a single options print as "bullish" because it traded at the ask is the options equivalent of lesson 6's print 8: it takes the most ambiguous data point and assigns it the least ambiguous label.

Open interest is the number of contracts outstanding, updated once a day after the close. A rise means more positions were opened than closed; it does not say who opened them or on which side. A 15,000-contract rise at a strike after 15,000 traded at the ask is consistent with a customer opening a long and a dealer opening a short hedge, which is the same event described from two chairs. OI is a fact about position size. It is the input to the gamma calculation, and that is its real use.

## Dealer gamma: the mechanism

If customers in aggregate are long calls and puts, dealers are short them, and short options have negative gamma: as the stock rises the dealer's short calls gain delta (become more negative for the dealer), so the dealer must buy stock; as it falls the dealer must sell. The hedge trades in the direction of the move and amplifies it. If customers are net sellers of options (covered calls, cash-secured puts, income strategies), dealers are long gamma and the hedge trades against the move, dampening it. Which regime prevails depends on the balance of positions in the strikes near the current price, which is why the OI table around the money matters.

The empirical record supports the mechanism as an average effect. Ni, Pearson, Poteshman and White (2021) found that stock returns respond to the net gamma position of option market makers in a manner consistent with delta hedging, that the effect is pervasive across stocks, and that it is stronger when net gamma is larger. Barbon and Buraschi document the same channel at the index level and call it gamma fragility. None of these papers claim the effect is large enough, stable enough or forecastable enough to trade; they establish that hedging flow is a real component of intraday price formation.

## Worked example

A representative large-cap trading at $187, average daily volume 8 million shares. From the exchange's open-interest file, dealers are estimated to be net short 40,000 contracts of the 190-strike call expiring this week, with gamma 0.04 per share per $1 move. (The gamma value is typical for a near-the-money weekly; the dealer positioning is an assumption, because OI does not reveal which side dealers hold.)

The stock rises $2.00, from 187 to 189.

- Delta change per share of underlying = gamma × move = 0.04 × 2 = 0.08.
- Contracts × shares per contract = 40,000 × 100 = 4,000,000 shares of notional exposure.
- Change in the position's delta = 0.08 × 4,000,000 = 320,000 shares.
- Dealers are short the calls, so their delta has become more negative by 320,000 shares. To return to neutral they buy 320,000 shares.

Scale it against the day: 320,000 / 8,000,000 = 4.0% of average daily volume, to be bought over whatever window the move took. Using the square-root impact model from lesson 10 with a 1.5% daily volatility, the expected impact of an order that size is 150 × √0.04 = 150 × 0.2 = 30 basis points, or about $0.56 on a $187 stock. The hedge buying is itself an order that moves the price; the move it responds to is amplified by roughly a quarter of its own size in this example. A $2.00 move becomes something closer to $2.50 before the next round of hedging.

Reverse the assumption, dealers net long 40,000 contracts of the same call, and every sign flips: they sell 320,000 shares into the rally and the $2.00 move is dampened toward $1.50. The arithmetic is identical; only the sign of the position differs, and the sign is exactly what the public data does not tell you. This is why gamma-exposure estimates circulate with wide error bars and why a stated "dealers are short gamma" is an inference, not an observation.

Now check the 0DTE scale. Cboe reported 2.4 million 0DTE SPX contracts a day in August 2025. If even 10% of those were near-the-money with gamma 0.05 and a net dealer position of one sign, a 1% move in the S&P 500 (about 65 index points at 6,500) implies a delta change of 0.05 × 65 = 3.25 per contract, times 240,000 contracts, times the $100 multiplier, equals $78 million of notional index exposure per point of delta, or 3.25 × 240,000 × 100 = 78,000,000 index-dollars of hedging. Against a futures market that trades hundreds of billions of dollars a day this is not dominant, but it is not zero either, and it is concentrated into the last hours before expiry.

## Table

| Flow item | What it measures | What it does not tell you | Mechanism for stock price |
|---|---|---|---|
| Sweep | Urgency: liquidity taken on several exchanges at once | Whether the sender is informed, hedging, or an algorithm | Only through the dealer's hedge |
| Block | Size: a negotiated print | Whether it is one leg of a spread or stock-tied package | Only through the dealer's hedge |
| Open-interest change | Net new positions at a strike | Which side dealers hold; the sign of aggregate gamma | Input to the gamma estimate |
| Dealer gamma × move | Shares dealers must trade to stay hedged | Sign of the position (assumed, not observed) | Direct: the hedge is a stock order |

Only the last row has a mechanism, and it depends on an assumption you cannot verify from public data.

## Sources

- The Options Clearing Corporation, historical volume statistics (2024: 12.2 billion contracts cleared): https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics
- Cboe Global Markets, "SPX 0DTE Options Jump to Record 62% Share in August" (2025): https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august
- Cboe Global Markets, "The State of the Options Industry: Quarter Three 2025": https://www.cboe.com/insights/posts/the-state-of-the-options-industry-quarter-three-2025/
- Sophie Ni, Neil Pearson, Allen Poteshman and Joshua White, "Does Option Trading Have a Pervasive Impact on Underlying Stock Prices?", Review of Financial Studies 34(4), 2021: https://doi.org/10.1093/rfs/hhaa082
