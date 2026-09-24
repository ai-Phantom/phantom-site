---
{
  "title": "The Opening and Closing Auctions: Imbalances and the Day's Biggest Print",
  "duration": "17 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "On Nasdaq, when does the Net Order Imbalance Indicator for the close begin to publish, and how often does it update after 15:55?", "opts": ["15:30, every minute", "15:50, every second after 15:55", "15:55, every 10 seconds", "16:00, once"], "correct": 1, "explain": "Nasdaq's closing cross FAQ: NOII starts at 15:50, every 10 seconds until 15:55, then every second until 16:00."},
    {"q": "In the 60-session SPY sample, what share of the day's volume traded in the 15:30–16:00 slot?", "opts": ["7.3%", "14.3%", "21.4%", "35.7%"], "correct": 2, "explain": "7.94 million of 37.21 million shares = 21.4%, the largest slot; 09:30 was second at 14.3%."},
    {"q": "The representative on-close book has 1,540,000 MOC buys and 1,300,000 MOC sells. What is the imbalance before limit-on-close orders are considered?", "opts": ["240,000 shares to buy", "240,000 shares to sell", "2,840,000 shares paired", "Zero"], "correct": 0, "explain": "1,540,000 − 1,300,000 = 240,000 more shares to buy than to sell at any price; that is a buy imbalance."},
    {"q": "Why do index funds and many institutions concentrate trading in the closing auction?", "opts": ["Fees are lower after 15:50", "Their benchmarks are priced at the official close, so trading in the auction eliminates tracking error against it", "The SEC requires it", "Spreads are always tightest at 16:00"], "correct": 1, "explain": "An index fund that trades at the closing price by construction matches its benchmark. That is the mechanical reason the close is the deepest liquidity event of the day."},
    {"q": "Bogousslavsky and Muravyev found the closing price matched the pre-close bid or ask in what share of cases?", "opts": ["About 10%", "About 33%", "About 68%", "Nearly 100%"], "correct": 2, "explain": "68%. Despite enormous volume, the auction usually clears inside or at the last continuous quote, which is evidence that closing volume is mostly uninformed benchmark flow."}
  ],
  "task": "Tomorrow at 15:50 Eastern, watch the published closing imbalance on one S&P 500 stock and note whether the last ten minutes moved toward or away from the imbalance side."
}
---

## Why auctions exist

Continuous trading is good at matching small orders quickly and bad at two things: finding a price after a gap in trading, and absorbing very large, uninformed volume without moving. The opening and closing auctions solve both. Instead of matching orders one at a time, the exchange collects orders for a period, publishes what it is holding, and then executes everything at a single clearing price. That single price is the official open or the official close, and it is the price index funds, mutual funds, options settlements and most performance benchmarks use.

This lesson walks through the mechanics as the exchanges publish them, measures how much volume the auctions attract on real data, and works one representative imbalance to show how the clearing price is found.

## The opening auction

On NYSE, order entry for the opening auction begins at 06:30 Eastern, and from 08:00 the exchange disseminates imbalance and paired-off information every second for each security whenever it changes. At 09:30 the Designated Market Maker opens each stock; securities that can open within 10% of the reference price are opened algorithmically, and anything outside that band is opened manually by the DMM. Nasdaq runs a comparable opening cross with its own imbalance feed.

The opening auction resolves overnight information: earnings, macro data, futures moves. Its volume is large but its price is often the day's least stable, because the auction has to absorb everything that happened since 16:00 with the shallowest information about how the day's trading will go.

## The closing auction

The close is where the money is. On NYSE, market-on-close (MOC) and limit-on-close (LOC) orders can be entered, modified or cancelled until 15:50. At 15:50 the exchange publishes the MOC/LOC significant imbalance, and after that only offsetting orders on the contra side are accepted, up to 16:00. From 15:50 until the stock closes, an informational imbalance publication is disseminated every second whenever it changes, including paired quantity, unpaired quantity, total imbalance, the closing-only interest price and the continuous-book clearing price.

Nasdaq's version: MOC, LOC and imbalance-only (IO) orders are accepted before 15:50; from 15:50 the Net Order Imbalance Indicator (NOII) publishes every ten seconds; at 15:55 MOC entry stops and the NOII goes to every second; LOC entry stops at 15:58 (with LOCs entered between 15:55 and 15:58 repriced if more aggressive than the 15:50 or 15:55 reference prices); IO orders can be entered until 16:00; and at 16:00 the cross executes at the single price that maximises the number of shares matched, the Nasdaq Official Closing Price. Nasdaq's own FAQ states that almost 10% of its average daily volume occurs in the closing auction.

The point of publishing the imbalance is to invite the other side. If 240,000 more shares want to buy at the close than sell, that number is broadcast so that anyone willing to sell can enter offsetting orders and dampen the price move. This is why, in the last ten minutes, you often see a stock drift toward the imbalance side and then partly revert: the drift is the market pricing in the known imbalance, and the reversion is offsetting liquidity arriving.

## How big the close is

Bogousslavsky and Muravyev, using consolidated tape data, found that closing auctions rose from 3.1% of daily volume in 2010 to 7.5% in 2018, driven by the growth of indexing and ETFs. They also found that the closing price matched the pre-close bid or ask in 68% of cases, and that price impact in the auction was lower than during continuous trading: enormous volume, mostly uninformed, clearing at low cost.

To see this on current data, the figure below uses SPY 5-minute bars from Yahoo Finance's chart API for the 60 regular sessions from 2026-06-30 to 2026-09-23 (pulled 2026-09-24), summed into half-hour slots and averaged across sessions. The chart provider folds the 16:00 closing print into the final 15:55 bar, which is why that bar averages 3.62 million shares against a median 5-minute bar of 0.33 million for the whole sample: the closing print is about eleven times a normal bar on its own.

## Worked example

Two calculations: the real volume profile, then a representative closing imbalance.

Average volume per half-hour slot, millions of shares, SPY, 60 sessions: 09:30 5.32, 10:00 3.12, 10:30 2.58, 11:00 2.53, 11:30 1.98, 12:00 1.92, 12:30 1.69, 13:00 1.78, 13:30 1.48, 14:00 1.88, 14:30 2.26, 15:00 2.71, 15:30 7.94.

Total = 5.32 + 3.12 + 2.58 + 2.53 + 1.98 + 1.92 + 1.69 + 1.78 + 1.48 + 1.88 + 2.26 + 2.71 + 7.94 = 37.21 million.

- Last half hour: 7.94 / 37.21 = 21.4% of the day.
- First half hour: 5.32 / 37.21 = 14.3%.
- Together: 13.26 / 37.21 = 35.7% of volume in one sixth of the session.
- Quietest slot, 13:30: 1.48 / 37.21 = 4.0%. Busiest to quietest: 7.94 / 1.48 = 5.4×.

Now the representative imbalance. This on-close book is invented for the lesson; it is not a real feed. A $52 stock at 15:50 has these closing orders:

- MOC buy: 1,540,000 shares. MOC sell: 1,300,000 shares.
- LOC buy: 200,000 at 52.00 or better; 150,000 at 51.95 or better.
- LOC sell: 180,000 at 52.05 or better; 260,000 at 52.10 or better.
- Continuous book at 15:50: bid 52.02, ask 52.04.

Step 1, the raw MOC imbalance: 1,540,000 − 1,300,000 = 240,000 shares to buy. That is what the 15:50 publication broadcasts as the significant imbalance.

Step 2, find the price that matches the most shares. Test candidate prices:

- At 52.05: buys willing = 1,540,000 MOC + 0 LOC (both buy LOCs are below 52.05) = 1,540,000. Sells willing = 1,300,000 MOC + 180,000 (52.05 LOC) = 1,480,000. Matched = min = 1,480,000; residual 60,000 to buy.
- At 52.10: buys = 1,540,000. Sells = 1,300,000 + 180,000 + 260,000 = 1,740,000. Matched = 1,540,000; residual 200,000 to sell.
- At 52.04 (the continuous ask): buys = 1,540,000. Sells = 1,300,000. Matched = 1,300,000; residual 240,000 to buy.

52.10 matches the most shares (1,540,000), so the auction clears there, one to two ticks above the 15:50 quote, with 200,000 shares of LOC sells left unexecuted. Exchanges also break ties by minimising the residual imbalance and by proximity to the reference price, but the ordering here is unambiguous. Paired volume of 1,540,000 shares at $52.10 is a single $80.3 million print at 16:00.

Notice the sequence: a published 240,000-share buy imbalance at 15:50 drew in 440,000 shares of LOC selling, and the price moved eight cents (15 basis points) to clear it. If those LOC sellers had not appeared, the auction would have had to walk further up. The imbalance feed's job is to make them appear.

## Chart

![SPY average volume per half-hour slot over 60 sessions, 2026-06-30 to 2026-09-23. The 15:30 slot (7.94M, 21.4% of the day) and 09:30 slot (5.32M, 14.3%) are highlighted; the 13:30 slot is the trough at 1.48M. Source: Yahoo Finance chart API, 5-minute bars, regular hours.](figures/spy-volume-by-half-hour-with-auctions.svg)

The two highlighted bars are the auction windows. The close is larger than the open in an index ETF because benchmark flow is scheduled at 16:00 and nowhere else.

## What this means for you

The closing auction is the deepest, cheapest liquidity of the day for a large, uninformed order, which is why institutions use it and why an individual with a large position to exit in a thin stock should consider an MOC rather than a 15:45 market order. It is also predictable in a narrow sense: the imbalance is public from 15:50, and the direction of the last ten minutes' drift is correlated with it. What it is not is a free signal. The imbalance is public to everyone at once, offsetting liquidity is paid to show up, and Bogousslavsky and Muravyev's 68% figure says the auction mostly clears at prices the continuous market had already found. Treat the auction as a place to execute, and the imbalance as context for the last ten minutes, not as a trade on its own.

## Sources

- Nasdaq, "Nasdaq Closing Cross" FAQ (NOII timing, MOC/LOC/IO cutoffs, NOCP determination): https://www.nasdaqtrader.com/content/productsservices/Trading/ClosingCrossfaq.pdf
- NYSE, "NYSE Opening and Closing Auctions" fact sheet (imbalance publication, 15:50 cutoff, DMM opening): https://www.nyse.com/publicdocs/nyse/NYSE_Auctions_Closing_Process_Fact_Sheet.pdf
- Vincent Bogousslavsky and Dmitriy Muravyev, "Who Trades at the Close? Implications for Price Discovery and Liquidity", Journal of Financial Markets 66, 2023: https://ssrn.com/abstract=3485840
- Yahoo Finance, SPY historical data (the chart API used here serves the same bars): https://finance.yahoo.com/quote/SPY/history/
