---
{
  "title": "Order Types and Time-in-Force",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "You place a market buy order for a thinly traded stock at 9:30:01 a.m. The most likely problem is:", "opts": ["It will be rejected", "It will fill at a price well above the last quote you saw", "It will only fill after the close", "It cannot be cancelled"], "correct": 1, "explain": "A market order takes whatever liquidity is available. At the open, spreads are wide and the book is thin, so the fill can be far from the last print."},
    {"q": "A sell stop order at 400 becomes what kind of order once the stock trades at or below 400?", "opts": ["A limit order at 400", "A market order", "A stop-limit order", "A good-till-cancelled order"], "correct": 1, "explain": "A plain stop order converts to a market order when triggered. It guarantees execution but not price."},
    {"q": "You set a sell stop-limit with stop 400 and limit 398. Overnight news gaps the stock open at 380. What happens?", "opts": ["You are sold at 398", "You are sold at 380", "The order triggers but does not fill, because no one is buying at 398 or above", "The order is cancelled by the exchange"], "correct": 2, "explain": "The stop triggered, creating a limit order at 398. With the market at 380, no buyer will pay 398, so you keep the shares and the loss keeps growing."},
    {"q": "A buy limit order at 418 while the ask is 421.50 is:", "opts": ["Marketable and fills immediately", "Rejected as below the market", "Resting on the book until a seller comes down to 418 or better", "Converted to a stop order"], "correct": 2, "explain": "A buy limit below the ask is not marketable. It rests in the order book and fills only if the price comes to it."},
    {"q": "What does a Day time-in-force mean for an order placed at 2:00 p.m. that does not fill?", "opts": ["It stays open for 24 hours", "It expires at the end of the regular session that day", "It carries over until cancelled", "It expires at the end of extended hours"], "correct": 1, "explain": "Day orders are cancelled at the close of the regular session unless the broker has explicitly extended them to after-hours trading."}
  ],
  "task": "In a paper-trading account, place one limit buy below the market on a stock you follow, note whether it fills by the close, and write down why."
}
---

## Why the order type is a decision, not a setting

Every order tells the market two things: what you want to do, and how badly you want to do it. A market order says "fill me now at any price". A limit order says "fill me only at this price or better, and I will wait". A stop order says "do nothing until the price reaches a trigger, then act". Choosing among them is the first real risk-management decision you make, and it is made before you own a single share.

The wrong choice does not usually blow up an account in one trade. It bleeds it: a few cents of slippage on every entry, a stop that fires on a wick and then watches the stock recover, a stop-limit that never fills through a gap. This lesson lays out each order type, what it guarantees, what it does not, and the time-in-force modifiers that decide how long it lives.

## Market orders

A market order executes immediately against the best available prices in the book. It guarantees execution. It does not guarantee price.

For a large, liquid stock during regular hours, a market order for a few hundred shares will fill at or near the NBBO and often slightly better, because wholesalers compete to give retail orders price improvement. Under those conditions it is the simplest and often the cheapest order.

It goes wrong in three situations:

- **At the open.** Before 9:30 the book is thin and spreads are wide. A market order queued overnight participates in the opening auction and can fill far from the previous close if news broke.
- **In thin stocks.** If the ask shows 200 shares and you send a market buy for 1,000, you take the 200, then the next price level, then the next. Your average fill can be well above the quote you saw.
- **During halts and fast markets.** A market order placed during a trading halt executes when trading resumes, at whatever the reopening price is.

Rule of thumb: use market orders only in liquid names, during regular hours, for sizes well below the displayed size.

## Limit orders

A limit order specifies the worst price you will accept: a maximum for a buy, a minimum for a sell. It guarantees price. It does not guarantee execution.

Two cases:

- **Marketable limit.** A buy limit at or above the ask, or a sell limit at or below the bid. It executes immediately like a market order but with a ceiling on what you will pay. This is the safest default for most trades: you get the immediacy of a market order and protection against a bad print.
- **Resting limit.** A buy limit below the ask or a sell limit above the bid. It sits in the book and fills only if the price comes to you. You avoid paying the spread and may catch a better price, at the cost of possibly not being filled at all. Note that a resting limit tends to fill when the price is moving against you: your buy at 418 fills because sellers are pushing the stock down through 418, and it may keep falling.

Partial fills are normal. If 50 shares are available at your limit and you asked for 100, you get 50 and the rest keeps resting.

## Stop orders

A stop order, often called a stop-loss, is dormant until the stock trades at or through the stop price. Then it becomes a market order. For a long position the stop is placed below the current price and triggers a sale; a buy stop is placed above and is used to enter breakouts or cover shorts.

What it guarantees: once triggered, it will execute. What it does not guarantee: the price. On an overnight gap, a stop at 400 on a stock that opens at 380 sells you at roughly 380, not 400.

Two mechanics you must check with your own broker:

- **Trigger basis.** Some brokers trigger on the last trade, others on the bid or ask. On a volatile day a single odd-lot print far from the market can trigger a last-trade stop.
- **Extended hours.** Most stops do not trigger outside regular hours. A stock can fall through your stop at 5:00 p.m. and you find out at 9:30 the next morning.

## Stop-limit orders

A stop-limit combines the two: at the stop price it becomes a limit order at your limit price rather than a market order. Stop 400, limit 398 means "if it trades at 400, try to sell, but not below 398".

This prevents a bad fill in a fast market. It also creates the single most common trap for beginners: through a gap, the order triggers but cannot fill, and you are left holding a falling stock with no protection at all. If you use stop-limits, set the limit far enough below the stop to absorb ordinary volatility, and understand that a true gap defeats it.

## Trailing stops

A trailing stop moves with the price: a trailing stop of 5 percent on a long position sits 5 percent below the highest price seen since you placed it, and only ratchets up, never down. It is a stop order underneath, with all of the same gap risk. It is useful for locking in gains without watching the screen. It is poor at handling normal noise: a stock that regularly swings 6 percent intraday will stop you out repeatedly with a 5 percent trail.

## Time-in-force

The time-in-force (TIF) decides how long an unfilled order lives.

- **Day.** Expires at the end of the regular session. The default at most brokers.
- **Good-till-cancelled (GTC).** Stays open until it fills or you cancel. Brokers impose a maximum, commonly 60 or 90 days. A forgotten GTC order is a common way to end up owning a stock you no longer wanted.
- **Immediate-or-cancel (IOC).** Fill whatever you can right now, cancel the remainder. Useful for taking displayed size without leaving a footprint.
- **Fill-or-kill (FOK).** Fill the entire quantity immediately or cancel everything. Rarely useful for retail sizes.
- **Extended hours.** A flag, not a TIF, that allows a limit order to work in pre-market or after-hours sessions. Only limit orders are accepted outside regular hours at most brokers.

## Table

What each order type guarantees, and its characteristic failure.

| Order type | Guarantees | Does not guarantee | Characteristic failure |
| --- | --- | --- | --- |
| Market | Execution | Price | Bad fill at the open or in a thin stock |
| Limit (marketable) | Price ceiling or floor, near-immediate fill | Full fill if size exceeds the book | Partial fill |
| Limit (resting) | Price | Execution | Never fills, or fills just as the price runs through you |
| Stop | Execution once triggered | Price | Sold at the gap price, well below the stop |
| Stop-limit | Price once triggered | Execution | Triggers through a gap and never fills |
| Trailing stop | Execution once triggered | Price | Stopped out by normal noise |

## Worked example

Microsoft (MSFT) closed at 421.50 dollars on Tuesday, 31 December 2024. Suppose you want to buy 10 shares over the following days and protect the position. Here are the orders you might place and the arithmetic behind each; the outcomes are hypothetical, the starting price is real.

**Entry.** You place a resting buy limit for 10 shares at 418.00, GTC. That is 0.83 percent below the close. If MSFT dips to 418.00 or lower during the next weeks, you are filled for 4,180.00 dollars. If it rallies from 421.50 without dipping, you never own it. You have decided that missing the trade is acceptable and paying up is not.

**Protection, option A: plain stop.** You set a sell stop at 400.00, about 4.3 percent below your entry. If MSFT trades at 400.00, the order becomes a market sell. In an orderly decline you are out near 400, for a loss of about 180 dollars. If the company reports a bad quarter after the close and opens at 380, you are sold near 380, for a loss of about 380 dollars. The stop capped your loss in the first case; in the second it only capped it at the gap.

**Protection, option B: stop-limit.** Stop 400.00, limit 397.00. In the orderly decline you sell between 400 and 397. In the 380 gap the order triggers, becomes a limit sell at 397, and does not fill. You still own 10 shares now worth 3,800 dollars, and you have no order protecting you.

**Time-in-force check.** If the entry limit was Day instead of GTC, it would have expired at 4:00 p.m. on the day you placed it, and the dip three days later would have passed without a fill.

The lesson is not that one option is right. It is that each guarantee costs something, and you should be able to say which cost you are choosing before you send the order.

## Sources

- SEC Office of Investor Education, "Types of Orders": https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders
- SEC Investor Bulletin, "Stop, Stop-Limit, and Trailing Stop Orders": https://www.sec.gov/resources-investors/investor-alerts-bulletins/stop-stop-limit-trailing-stop-orders
- FINRA, "Understanding Order Types" (investor insights): https://www.finra.org/investors/insights/order-types
- Nasdaq Trader, order types and trading hours: https://www.nasdaqtrader.com/Trader.aspx?id=TradingHours
