---
{
  "title": "Level 2, the Tape, and What Order Flow Can and Cannot Tell You",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Level 2 data shows:", "opts": ["Every trade that has occurred", "Displayed limit orders at prices away from the best bid and offer, by venue or aggregated", "Hidden and iceberg orders", "The intentions of institutional traders"], "correct": 1, "explain": "The book shows displayed resting orders only. Hidden orders, reserve size and orders held at brokers or in dark pools are not in it."},
    {"q": "Time and sales (the tape) shows:", "opts": ["Resting orders", "Executed trades with price, size and time", "Only trades above 10,000 shares", "Quotes from a single exchange"], "correct": 1, "explain": "The tape is the record of executions, consolidated across venues under Regulation NMS."},
    {"q": "At the open, SPY traded about 7,300 shares per second in the 60-session sample. How long does 2,000 shares of displayed size last at that rate if it all trades?", "opts": ["About 0.3 seconds", "About 3 seconds", "About 30 seconds", "About 5 minutes"], "correct": 0, "explain": "2,000 / 7,333 = 0.27 seconds. At the 12:30 rate of 1,150 per second it is 1.7 seconds. Displayed size is not a wall."},
    {"q": "Cont, Kukanov and Stoikov found that order-flow imbalance explains short-horizon price changes. What horizon?", "opts": ["Days", "Hours", "Seconds to minutes, with the effect decaying as the horizon lengthens", "Weeks"], "correct": 2, "explain": "The relation is strongest at very short horizons and is a statement about contemporaneous price impact, not about forecasting the next hour."},
    {"q": "Why can a large displayed bid disappear without trading?", "opts": ["It cannot; displayed orders are binding until filled", "Limit orders can be cancelled at any time, and a large share of displayed orders are cancelled rather than executed", "The exchange removes it after 10 seconds", "Only market makers can cancel"], "correct": 1, "explain": "Displayed liquidity is an option to trade held by the poster, who can withdraw it; O'Hara documents cancellation rates far above execution rates."}
  ],
  "task": "Watch the SPY tape for the 09:30 to 09:35 bar on one session and count how many seconds a single displayed level survives before it is either traded through or pulled."
}
---

## What the two screens are

Level 1 is the best bid and best offer with their displayed sizes. Level 2 is the book beneath: displayed limit orders at prices away from the inside, either per venue (Nasdaq TotalView, NYSE OpenBook and their equivalents) or aggregated across venues by your data vendor. The tape, or time and sales, is the stream of executed trades: price, size, time and often the venue. Under Regulation NMS, quotes and trades from every US venue are consolidated, so the tape you see is the whole market's prints, and the top of book you see is the national best bid and offer.

This lesson explains what those screens contain and, more importantly, what they do not. Order-flow trading is a discipline of its own with its own course in this catalog; here the goal is to stop you from reading the book as if it were a list of intentions.

## What the book contains

Displayed limit orders. That is the whole list. It does not contain hidden orders (fully non-displayed limit orders that most venues allow), the non-displayed part of reserve or iceberg orders, orders resting at wholesalers who internalise retail flow, or anything in a dark pool. It does not contain the stop orders that brokers hold until triggered, and it does not contain the large institutional order that an algorithm is slicing into 200-share children. Nasdaq's own documentation describes TotalView as displaying every displayed quote and order at every price level; the word "displayed" is doing a lot of work.

A displayed order is also an option, not a commitment. Its owner can cancel it at any time, and most do. O'Hara's survey of high-frequency microstructure reports order-to-trade ratios in US equities where the large majority of submitted orders are cancelled rather than executed. Large size on the bid is therefore evidence that someone wants you to see large size on the bid, and it is at least as consistent with spoofing (illegal, but it happens) or with a market maker's quoting model as with a buyer who will hold the level.

## What the tape contains

Executions. Each print is a trade that happened, with its size and whether it went off at the bid, the offer or in between. Aggregating prints by whether they lifted the offer or hit the bid gives you order-flow imbalance, which is the one thing on these screens with a solid academic result behind it. Cont, Kukanov and Stoikov showed that the net imbalance between buy-initiated and sell-initiated volume explains a large share of contemporaneous price changes over horizons of seconds to minutes, with a roughly linear price impact that scales inversely with the depth of the book.

Read that result carefully. It says that when more people are hitting offers than bids, price is going up at the same time. It does not say that seeing imbalance now tells you where price will be in twenty minutes. The relation weakens quickly as the horizon lengthens, and by the time the imbalance is visible to a human reading a scrolling window, the price impact it explains has mostly already happened.

## Worked example

Flow rates from the 60-session SPY sample (2026-06-30 to 2026-09-23, 5-minute bars, Yahoo Finance chart API):

Average 09:30 bar volume: 2,199,978 shares. Per second: 2,199,978 / 300 = 7,333.
Average 12:30 bar volume: 345,189 shares. Per second: 345,189 / 300 = 1,151.
Average 15:55 bar volume: 3,623,024 shares. Per second: 3,623,024 / 300 = 12,077.

Suppose the book shows 2,000 shares at the best bid. If flow were all one-sided at the average rate, that level would be exhausted in 2,000 / 7,333 = 0.27 seconds at the open, 2,000 / 1,151 = 1.7 seconds at 12:30, and 2,000 / 12,077 = 0.17 seconds in the last bar. Flow is not one-sided, so real levels last longer, but the scale is right: displayed size at the inside in SPY is a fraction of a second of flow. It cannot "hold" anything.

Now the tape on a session you already know, 2026-07-01, where the 15-minute opening-range breakout of lesson 3 triggered at 09:55:

- 09:30 bar: 2,388,004 shares, range 745.18 to 742.50, closed at 742.63 (down $2.37 from the open).
- 09:35 bar: 912,760 shares, closed 743.07.
- 09:40 bar: 1,153,801 shares, closed 743.21.
- 09:45 bar: 913,819 shares, closed 743.69.

The opening bar was heavy and down; the next three were lighter and up. A tape reader at 09:46 would have seen selling exhausted on the open and buyers stepping in on lighter volume, which is a reasonable narrative for a long. It is also a narrative that fits after the fact. The bar-based rule needed no narrative: it waited for a 5-minute close above 745.18, got it at 09:55, and entered at 745.34. The tape could have helped that trader enter a bar or two earlier, around 743.70 to 744.75, for an extra dollar of profit. It could equally have talked a trader into a long on 2026-07-02, when the same rule entered at 750.42 on a similar-looking tape and was stopped for a $3.34 loss at 10:40.

## Table

What the screens can and cannot tell you, with the reason.

| Question | Book (Level 2) | Tape (time and sales) | Why |
|---|---|---|---|
| Is there displayed liquidity at this price right now? | Yes | No | The book is a snapshot of displayed resting orders |
| Will that liquidity still be there when my order arrives? | No | No | Orders are cancellable; most displayed orders are cancelled |
| Did buyers or sellers initiate recent trades? | No | Yes | Prints marked at bid or offer give initiator side |
| Is price about to move in the next few seconds? | Weakly | Weakly | Order-flow imbalance explains contemporaneous moves; the signal decays fast |
| Where will price be in an hour? | No | No | No documented predictive power at that horizon |
| Is an institution accumulating? | No | Rarely | Institutional orders are sliced and often hidden or routed off-exchange |
| What are the stops above the range? | No | No | Stops are held at brokers, not displayed |

## What it can do for an opening-range or VWAP trader

Two modest uses. First, fill management: if you are entering with a limit order, the book tells you whether there is displayed size ahead of you and the tape tells you how fast it is going. Second, disconfirmation: if your breakout bar closed above the range on a tape that shows almost every print at the bid, the closing price was set by a thin last trade rather than by buyers, and skipping the trade is defensible. Neither use turns the screens into a signal. Both fit inside a rule that was defined before the session, which is the standard every lesson in this course holds to.

What the screens will do to you if you let them is generate a new reason every thirty seconds. The trader who has a written entry, stop and target and then watches Level 2 tends to move the stop because "there's a big bid," or exit early because "sellers are hitting," and neither action is one you can test afterward because neither was a rule. The order-flow course in this catalog spends its time on defining those observations precisely enough to test. Until you have done that, treat the book and tape as execution tools.

## Data you need and data you do not

Consolidated Level 1 and the tape are cheap and, for a 5-minute-bar strategy, sufficient. Full-depth books from each exchange are sold separately by the venues (Nasdaq TotalView is the best-known) and are priced for professionals. Nothing in this course requires depth data. If you buy it, buy it to study execution, and keep a log of the decisions it changed and whether they were better; that log is the only thing that will tell you whether it paid for itself.

## Sources

- Rama Cont, Arseniy Kukanov and Sasha Stoikov, "The Price Impact of Order Book Events," Journal of Financial Econometrics 12(1), 2014: https://doi.org/10.1093/jjfinec/nbt003
- Maureen O'Hara, "High Frequency Market Microstructure," Journal of Financial Economics 116(2), 2015: https://doi.org/10.1016/j.jfineco.2015.01.003
- Nasdaq, TotalView data product documentation: https://www.nasdaq.com/solutions/nasdaq-totalview
- U.S. Securities and Exchange Commission, Regulation NMS, Release No. 34-51808 (consolidated quotes and trades, order protection): https://www.sec.gov/rules/final/34-51808.pdf
