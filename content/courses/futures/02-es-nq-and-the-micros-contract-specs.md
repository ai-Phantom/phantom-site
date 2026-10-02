---
{
  "title": "ES, NQ and the Micros: Reading the Contract Specs",
  "duration": "18 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "ES moves from 7,772.50 to 7,775.00. What is the change in value of one contract?", "opts": ["$2.50", "$12.50", "$125.00", "$250.00"], "correct": 2, "explain": "2.50 index points x $50 per point = $125.00. Equivalently, ten ticks of 0.25 at $12.50 each."},
    {"q": "What is the tick value of one Micro E-mini Nasdaq-100 (MNQ) contract?", "opts": ["$0.50", "$1.25", "$5.00", "$12.50"], "correct": 0, "explain": "MNQ has a $2 multiplier and a 0.25 tick: 0.25 x $2 = $0.50. NQ is $5.00, MES $1.25, ES $12.50."},
    {"q": "When does trading in the December 2026 ES contract terminate?", "opts": ["4:00 p.m. ET on 2026-12-31", "9:30 a.m. ET on Friday 2026-12-18, the third Friday", "5:00 p.m. ET on Thursday 2026-12-17", "At the NYSE close on the last business day of December"], "correct": 1, "explain": "Equity index futures stop trading at 9:30 a.m. ET on the third Friday of the contract month and are cash-settled to that morning's Special Opening Quotation. The third Friday of December 2026 is the 18th."},
    {"q": "Ten MES contracts versus one ES contract: which statement is correct?", "opts": ["Ten MES have the same notional as one ES", "Ten MES have half the notional of one ES", "One MES has the same notional as one ES", "MES tracks a different index"], "correct": 0, "explain": "MES is exactly one-tenth of ES ($5 versus $50 per index point) on the same S&P 500 index, so 10 MES = 1 ES in exposure. Commissions per unit of exposure are usually higher on the micro."},
    {"q": "Which contract months does ES list?", "opts": ["Every calendar month", "March, June, September and December", "January, April, July, October", "Only the front month"], "correct": 1, "explain": "ES, NQ and the micros trade on the quarterly cycle: H (Mar), M (Jun), U (Sep), Z (Dec). Nearly all volume sits in the front quarterly contract until the roll."}
  ],
  "task": "Open the CME spec pages for ES and MES side by side and confirm every row in this lesson's table against the live page, noting anything that has changed."
}
---

## Where the numbers live

Every futures contract is defined by a specification page on the listing exchange's website. For the four contracts in this lesson the pages are on cmegroup.com under Markets > Equities. Nothing on a broker's platform, a charting site or a forum overrides that page. When a number in this course and a number on the spec page disagree, the spec page is right and this course is out of date. Read the spec once before you trade a product and again every time the exchange sends a product notice.

The rows that matter for trading are: contract unit (the multiplier), minimum price fluctuation (tick size and its dollar value), trading hours, listed contract months, termination of trading, and settlement method. Position limits and block-trade minimums exist but will not bind a retail account.

## The multiplier

The **contract unit** turns an index level into dollars. For the E-mini S&P 500 (product code ES) it is $50 times the S&P 500 index. For the E-mini Nasdaq-100 (NQ) it is $20 times the Nasdaq-100 index. The Micro E-mini S&P 500 (MES) is $5 times the S&P 500, and the Micro E-mini Nasdaq-100 (MNQ) is $2 times the Nasdaq-100. The micros are exactly one-tenth of the E-minis on the same underlying index, which means one ES and ten MES are the same exposure.

Notional value is simply index level times multiplier. With ESZ26 at 7,772.50 on 2026-09-23 (Yahoo Finance), one ES controlled $388,625.00 of S&P 500 exposure and one MES controlled $38,862.50. NQZ26 closed at 30,764.75 the same day, so one NQ was $615,295.00 and one MNQ $61,529.50. Note that an NQ is about 1.6 times the size of an ES at these levels, and that ratio drifts as the two indices diverge.

## Tick size and tick value

The **minimum price fluctuation** for all four contracts is 0.25 index points. Multiply by the multiplier to get the tick value: ES $12.50, NQ $5.00, MES $1.25, MNQ $0.50. A one-point move is four ticks: $50, $20, $5 and $2 respectively.

Tick value is the unit of every cost you pay. The bid-ask spread in ES during regular hours is almost always one tick, so crossing the spread with a market order costs about $12.50 per contract per side before commission. It is also the unit of slippage, and of the "one more tick" you will be tempted to wait for. Lesson 10 turns these into a cost per round trip.

Calendar spreads (Lesson 6) trade in a finer increment on ES, 0.05 index points or $2.50, because the spread between two months of the same index is far less volatile than the outright.

## Trading hours

ES, NQ and the micros trade on CME Globex from 6:00 p.m. ET Sunday through 5:00 p.m. ET Friday, with a daily maintenance break from 5:00 p.m. to 6:00 p.m. ET (4:00 to 5:00 p.m. CT). The trading day therefore starts the evening before its date: the session labelled Tuesday 2026-09-22 began at 6:00 p.m. ET on Monday the 21st. The daily settlement price is set in the afternoon, around the cash-market close, and Lesson 4 explains what it does to your account.

You can confirm the break from public data. Yahoo Finance five-minute bars for ES=F on 2026-09-22 show a last bar at 4:55 p.m. ET, no bars from 5:00 to 5:55 p.m., and trading resuming at 6:00 p.m. Lesson 7 covers the whole clock, including holidays.

## Listed months and the last trading day

All four contracts trade the quarterly cycle: March (code H), June (M), September (U) and December (Z). ES lists nine quarterly contracts plus three additional December contracts; NQ and the micros list fewer. A contract's full symbol is product code, month code and two-digit year: ESZ26 is December 2026 ES, MNQH27 is March 2027 MNQ.

Trading terminates at 9:30 a.m. ET on the third Friday of the contract month. Using the third-Friday rule, the next four expiries are 2026-12-18, 2027-03-19, 2027-06-18 and 2027-09-17. The last one that already happened as this was written was 2026-09-18. If the third Friday is an exchange holiday the termination moves to the prior business day; check the CME calendar.

Volume does not wait for the last day. Most open interest migrates to the next quarterly contract about a week before expiry, on the roll date (Lesson 6). A retail trader should be out of the expiring month by the Thursday before the third Friday at the latest.

## Settlement

ES and NQ are **cash-settled**. On the third Friday the exchange computes the Special Opening Quotation (SOQ), the index value built from the official opening price of each component stock, and the final settlement is that number. There is no delivery of anything. If you are still long at 9:30 a.m. ET, your broker's clearing firm receives cash equal to (SOQ minus your last settlement price) times the multiplier, positive or negative, and your position simply ceases to exist.

Because the SOQ uses opening prices rather than a single trade, it can land noticeably away from Thursday's close. Yahoo Finance's continuous ES=F series shows this: the 2026-09-18 bar closes at a fractional 7,657.35, and the 2026-06-18 and 2026-03-20 bars at 7,508.43 and 6,594.63, when every real ES trade is a multiple of 0.25. Those fractional closes are expiry-day artefacts of how the data vendor splices the final settlement into the series. Lesson 6 returns to them.

## Worked example

Take the December 2026 contracts at their 2026-09-23 closes from Yahoo Finance: ESZ26 at 7,772.50 and NQZ26 at 30,764.75. A trader wants roughly $80,000 of S&P 500 exposure and roughly $60,000 of Nasdaq-100 exposure. Which contracts fit, and what does one tick and one point cost in each?

S&P 500 side. One ES = 7,772.50 x $50 = $388,625.00, far too large. One MES = 7,772.50 x $5 = $38,862.50. Two MES = $77,725.00, close to the $80,000 target. Tick value for two MES = 2 x 0.25 x $5 = $2.50. One index point on two MES = 2 x $5 = $10.00. A 1% move in the index (77.73 points) is worth 77.73 x $10.00 = $777.25.

Nasdaq-100 side. One NQ = 30,764.75 x $20 = $615,295.00, again too large. One MNQ = 30,764.75 x $2 = $61,529.50, almost exactly the $60,000 target. Tick value = 0.25 x $2 = $0.50. One point = $2.00. A 1% move (307.65 points) is worth 307.65 x $2.00 = $615.30.

Combined exposure = $77,725.00 + $61,529.50 = $139,254.50. A simultaneous 1% adverse move in both indices costs $777.25 + $615.30 = $1,392.55, which is exactly 1% of the combined notional, as it must be. The multiplier changes the dollar scale of the contract; it never changes the percentage risk of the exposure you chose. What it does change is granularity: with MES you can size in $38,862.50 steps, with ES only in $388,625 steps. That is the entire case for the micros in a small account.

## Table

| Row from the spec page | ES | NQ | MES | MNQ |
|---|---|---|---|---|
| Underlying index | S&P 500 | Nasdaq-100 | S&P 500 | Nasdaq-100 |
| Contract unit (multiplier) | $50 x index | $20 x index | $5 x index | $2 x index |
| Minimum tick | 0.25 pts | 0.25 pts | 0.25 pts | 0.25 pts |
| Tick value | $12.50 | $5.00 | $1.25 | $0.50 |
| Value of one index point | $50 | $20 | $5 | $2 |
| Notional at 2026-09-23 close | $388,625.00 | $615,295.00 | $38,862.50 | $61,529.50 |
| Trading hours (ET) | Sun 6 p.m. to Fri 5 p.m.; break 5 to 6 p.m. daily | same | same | same |
| Contract months | Mar, Jun, Sep, Dec | same | same | same |
| Termination | 9:30 a.m. ET, third Friday | same | same | same |
| Settlement | Cash, to the SOQ | Cash, to the SOQ | Cash, to the SOQ | Cash, to the SOQ |

Closes from Yahoo Finance daily bars for ESZ26.CME and NQZ26.CME, 2026-09-23; spec rows from the CME Group pages below.

## Sources

- CME Group, E-mini S&P 500 contract specifications — https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.contractSpecs.html
- CME Group, E-mini Nasdaq-100 contract specifications — https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.contractSpecs.html
- CME Group, Micro E-mini S&P 500 contract specifications — https://www.cmegroup.com/markets/equities/sp/micro-e-mini-sandp-500.contractSpecs.html
- CME Group, Micro E-mini Nasdaq-100 contract specifications — https://www.cmegroup.com/markets/equities/nasdaq/micro-e-mini-nasdaq-100.contractSpecs.html
