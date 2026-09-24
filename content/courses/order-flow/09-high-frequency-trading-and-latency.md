---
{
  "title": "High-Frequency Trading and Latency: What HFTs Do, What They Do Not, and What You Can See",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Aquilina, Budish and O'Neill measured latency-arbitrage races on the London Stock Exchange. How long did the typical race last?", "opts": ["About a second", "About a millisecond", "5 to 10 microseconds", "One minute"], "correct": 2, "explain": "The modal race lasted 5–10 millionths of a second, and races happened about once a minute per FTSE 100 stock."},
    {"q": "Their estimate of the 'latency arbitrage tax' on trading was about:", "opts": ["0.05 basis point", "0.5 basis point", "5 basis points", "50 basis points"], "correct": 1, "explain": "Roughly half a basis point of volume traded, about 17% of the cost of liquidity, on the order of $5 billion a year in global equities."},
    {"q": "Light travels through optical fibre at roughly 200,000 km/s. The one-way time over 56 km of fibre between two New Jersey data centres is about:", "opts": ["2.8 microseconds", "28 microseconds", "280 microseconds", "2.8 milliseconds"], "correct": 2, "explain": "56 / 200,000 = 0.00028 s = 280 microseconds. Direct feeds arriving through a shorter path than the SIP's aggregation are 'faster' by amounts of this size."},
    {"q": "Which of these can an HFT firm actually see?", "opts": ["Your order before it reaches the exchange", "Your broker's internal order queue", "Public book and trade messages from exchange feeds, with microsecond timestamps", "Your account balance"], "correct": 2, "explain": "HFT sees public market data faster and reacts faster. It cannot see orders that have not been published, and in the US it is not permitted to trade ahead of a customer order it handles."},
    {"q": "What did the SEC's 2010 Concept Release identify as the core characteristics of HFT?", "opts": ["Long holding periods and low turnover", "Very high speed, co-location, short holding periods, many orders that are cancelled, and ending the day near flat", "Trading only in options", "Trading only at the close"], "correct": 1, "explain": "The Concept Release's list is still the standard definition: speed, proximity, high order-to-trade ratios, tiny positions, flat by the close."}
  ],
  "task": "Compare the timestamp of one trade in your platform's time and sales against the same trade on a second data source and record the difference in milliseconds."
}
---

## What "high-frequency" means

The SEC's 2010 Concept Release on equity market structure (Release 34-61358) described high-frequency trading by a list of characteristics rather than a definition: very fast, sophisticated systems; co-location of servers next to exchange matching engines; very short holding periods; submission of many orders that are cancelled shortly after; and ending the day close to flat. Firms with those characteristics are the market makers of lessons 4 and 5, the arbitrageurs who keep SPY and ES futures aligned, and a smaller group whose business is winning races.

This lesson separates what those firms do from the folklore about them, using the best public measurements, and then asks the question that matters for you: what of this can you see, and does it change how you should trade?

## What HFTs do

Market making. Most HFT volume is quoting: posting bids and offers on every exchange, hedging in correlated instruments, and collecting spread plus rebate. The queue-position economics of lesson 3 are their economics.

Arbitrage across venues and instruments. When ES futures tick up, every SPY quote on sixteen exchanges is stale for a few microseconds. The firm that updates or trades against those quotes first captures the difference. This is where latency arbitrage lives.

Liquidity detection and short-horizon prediction. Statistical models on the order book and tape predict the next few seconds of price movement, and firms trade on those predictions with tiny positions. This is legal and common; it is the industrial version of lesson 7's delta.

## Measuring the race

Aquilina, Budish and O'Neill (Quarterly Journal of Economics, 2022) used message data from the London Stock Exchange, which unlike ordinary order-book data includes the orders and cancels that failed, so both winners and losers of a race are visible. For FTSE 100 stocks in 2015 they found races occurring about once a minute per stock, the modal race lasting 5–10 microseconds, and races accounting for about 20% of trading volume. Race participation was concentrated: the top six firms accounted for over 80% of race wins and losses. Latency arbitrage accounted for about 33% of the effective spread and 31% of price impact, imposing a tax of roughly 0.5 basis point on trading; they estimated that a market design eliminating races (frequent batch auctions) would cut the cost of liquidity by about 17%, and that the sums at stake were on the order of $5 billion a year in global equities.

Those numbers are the best public quantification of the negative side of HFT. Read them carefully: the "tax" is real, it falls on whoever provides or takes liquidity in a stale quote, and it is small per trade. It is a cost of the market design, not a theft from any particular retail order.

## What HFTs do not do

They do not see your order before the exchange does. An order is private until the matching engine publishes it. An HFT firm that also acts as a wholesaler does see the orders it has bought (lesson 4), and is prohibited from trading ahead of them.

They did not cause the May 6, 2010 flash crash. Kirilenko, Kyle, Samadi and Tuzun (Journal of Finance, 2017), using CFTC audit-trail data that identifies each account, found that HFTs did not trigger the crash, that they initially provided liquidity and then reduced it, and that their behaviour during the event was consistent with their normal inventory management rather than with a change in strategy. The trigger was a large sell algorithm in E-mini futures interacting with a market that was already fragile; a separate spoofing prosecution (lesson 11) later attached to the same day.

They do not hold positions. Ending flat is a defining characteristic. HFT is not a directional participant and cannot be "long" or "short" the market in any way that affects daily returns.

## What you can and cannot see

You see the consolidated tape and the NBBO, usually through your broker's feed, which itself may be delayed by aggregation and by the network between the SIP and you. HFT firms see each exchange's proprietary feed, which is faster than the SIP because it skips consolidation and, physically, because their servers sit in the same building. The gap between "direct feed at the exchange" and "SIP at your broker" is measured in hundreds of microseconds to a few milliseconds. Nothing in that gap is a secret; it is the same public data arriving later.

The IEX speed bump, approved by the SEC in 2016, is a 350-microsecond delay imposed on all incoming messages by 38 miles of coiled fibre, designed so that IEX's own view of the NBBO is never staler than the fastest participant's. It is the market-design response to the race the QJE paper measured, and it has a rulebook, not a black box.

What you cannot see: hidden orders, wholesaler inventory, the losing orders in a race (which never appear in ordinary data), and the intent behind a cancel. The order-to-trade ratio you observe on a Level 2 screen is mostly quote updates against futures moves, not manipulation, though lesson 11 covers the exception.

## Worked example

Two calculations: the physics of latency, and the cost of the race on a retail order.

Physics. The major New Jersey data centres (NYSE in Mahwah, Nasdaq in Carteret, Cboe and others in Secaucus) are 20 to 35 miles apart. Take 35 miles = 56.3 km between Mahwah and Carteret. Light in optical fibre travels at about two thirds of its vacuum speed, roughly 200,000 km/s.

- One-way fibre time = 56.3 / 200,000 = 0.000282 s = 282 microseconds.
- Microwave links through the air run at near vacuum speed, about 300,000 km/s: 56.3 / 300,000 = 188 microseconds, so a microwave path is about 94 microseconds faster than fibre over that distance.
- A round trip (see a quote change at Carteret, send an order to Mahwah) is roughly 2 × 282 = 564 microseconds by fibre.

Now compare to the race: Aquilina et al. found the modal race lasting 5–10 microseconds. A race is decided in the time light takes to travel one to two miles. Nothing running through a retail broker's stack, which involves multiple network hops and typically tens of milliseconds, participates in that contest, and that is the practical point: you are not in the race, so its winner is not taking anything from a decision you made a hundred milliseconds ago.

Cost. Apply the 0.5 basis point latency-arbitrage tax to a retail trade of $10,000: 10,000 × 0.00005 = $0.50. To a $500,000 institutional order: $25. To Cboe's 2025 average daily notional value of $1.1 trillion: 1,100,000,000,000 × 0.00005 = $55 million a day, which over 252 sessions would be $13.9 billion. That is higher than the paper's own estimate of about $5 billion for global equities, because the tax falls only on the volume that trades in stale quotes, not on every dollar, and because the paper's coefficient was measured on 2015 FTSE 100 data; treat the daily figure as an upper bound and the $5 billion as the authors' estimate. Per trade, the number that reaches you is cents.

The comparison that should change your behaviour is with lesson 4: the SEC's estimated competitive shortfall on retail orders was 1.08 basis points, twice the latency-arbitrage tax. If you want to reduce what market structure costs you, the routing of your order matters more than the speed of anyone else's.

## Table

| Claim about HFT | Evidence | Verdict |
|---|---|---|
| HFTs are most of the quoting and much of the volume | SEC 2010 Concept Release; exchange data | True |
| Latency arbitrage is a real cost | Aquilina, Budish and O'Neill: ~0.5 bp, ~20% of volume in races | True, and small per trade |
| HFTs see retail orders before they execute | Orders are private until published; wholesaler flow is bought, not intercepted | False |
| HFTs caused the 2010 flash crash | Kirilenko et al.: no; they did not trigger it | False |
| HFTs "front-run" institutional orders | They predict from public data and react in microseconds; front-running requires knowledge of the order | Misleading: prediction, not front-running |
| Retail can compete on speed | Round-trip fibre ~564 µs versus races of 5–10 µs; retail stacks add milliseconds | False, and irrelevant |

## Sources

- Matteo Aquilina, Eric Budish and Peter O'Neill, "Quantifying the High-Frequency Trading 'Arms Race'", Quarterly Journal of Economics 137(1), 2022: https://doi.org/10.1093/qje/qjab032
- SEC, Concept Release on Equity Market Structure, Release No. 34-61358 (January 14, 2010): https://www.sec.gov/files/rules/concept/2010/34-61358.pdf
- Andrei Kirilenko, Albert Kyle, Mehrdad Samadi and Tugkan Tuzun, "The Flash Crash: High-Frequency Trading in an Electronic Market", Journal of Finance 72(3), 2017: https://doi.org/10.1111/jofi.12498
- SEC, order approving the registration of Investors' Exchange LLC as a national securities exchange (the 350-microsecond access delay), Release No. 34-78101 (June 17, 2016): https://www.sec.gov/files/rules/other/2016/34-78101.pdf
