---
{
  "title": "Energy Survey: WTI Crude Oil (CL), Its Specs and What Moves It",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "CL moves from $92.41 to $92.53. What is the change in value of one contract?", "opts": ["$12", "$120", "$1,200", "$12,000"], "correct": 1, "explain": "$0.12 per barrel x 1,000 barrels = $120. Each $0.01 tick is $10; a $1.00 move is $1,000."},
    {"q": "How is the CL contract settled at expiration?", "opts": ["Cash against a published index", "Physical delivery of 1,000 barrels at Cushing, Oklahoma", "Conversion into the next month", "Delivery of an ETF"], "correct": 1, "explain": "CL is physically delivered. A retail account cannot make or take delivery, so brokers force positions out before the last trading day."},
    {"q": "On 2026-04-08 the front CL contract fell from $112.95 to $94.41. Per contract that was a loss of:", "opts": ["$1,854", "$18,540", "$185,400", "$18.54"], "correct": 1, "explain": "$18.54 per barrel x 1,000 barrels = $18,540 in one day, roughly twice the exchange maintenance margin at the time."},
    {"q": "Which scheduled release most often moves CL during U.S. hours?", "opts": ["The Wednesday 10:30 a.m. ET EIA Weekly Petroleum Status Report", "The monthly jobs report", "The FOMC decision", "The CME settlement"], "correct": 0, "explain": "The EIA inventory report (Wednesday 10:30 a.m. ET, a day later after Monday holidays) is the single most reliable weekly volatility event in crude; the API estimate the prior evening previews it."},
    {"q": "Why did the May 2020 CL contract settle at negative $37.63 on 2020-04-20?", "opts": ["A data error", "Holders of the expiring physical-delivery contract had nowhere to store oil and paid to be rid of it", "OPEC set the price", "The exchange closed"], "correct": 1, "explain": "With Cushing storage effectively full, longs in a contract expiring the next day could not take delivery and had to pay buyers to take the obligation. Cash-settled index futures cannot do this; physical ones can."}
  ],
  "task": "Look up the last trading day of the front CL contract on the CME calendar and your broker's earlier liquidation date, and write both down before you place any energy trade."
}
---

## What the contract is

The NYMEX Light Sweet Crude Oil future, product code CL, is the benchmark for West Texas Intermediate (WTI) crude, and it is the most actively traded physical commodity future in the world. Unlike ES it is not a promise about a number; it is a promise about barrels. The contract unit is 1,000 U.S. barrels (42,000 gallons). Price is quoted in dollars and cents per barrel, the minimum tick is $0.01 per barrel, and the tick value is therefore $0.01 x 1,000 = $10.00. A one-dollar move is $1,000 per contract.

Contract months are listed monthly, out many years, which is why the term structure in Lesson 5 had a point for every month. Trading hours are Sunday to Friday 6:00 p.m. to 5:00 p.m. ET with a 60-minute break, the same clock as ES. There is a Micro WTI contract (MCL) at 100 barrels with a $0.01 tick worth $1.00, for sizing.

The expiration is the part that makes crude different. Trading in a CL contract terminates three business days before the 25th calendar day of the month preceding the contract month; if the 25th is not a business day, four business days before it. For the November 2026 contract (CLX26) the reference is 2026-10-25, a Sunday, so termination falls on Tuesday 2026-10-20. After that the contract goes to **physical delivery** at Cushing, Oklahoma, the pipeline hub whose storage tanks set the physical price of WTI.

## Delivery means what it says

A retail account cannot take or make delivery of 1,000 barrels of crude. Every futures broker therefore sets a liquidation date for physically delivered contracts that is earlier than the exchange's last trading day, often several days earlier, and will close your position at market if you are still in it. That is not a courtesy you can decline. Treat the broker's date, not CME's, as the contract's real end.

The reason this matters more than an inconvenience is 2020-04-20. The May 2020 CL contract, expiring the next day, settled at negative $37.63 per barrel. Storage at Cushing was effectively full, longs could not take delivery, and they paid buyers to assume the obligation. A long one contract lost roughly $55 per barrel, $55,000 per contract, in a single session, on a position whose margin had been a few thousand dollars. CME had enabled negative pricing in its systems days earlier and the market used it. Cash-settled index futures cannot go negative; physically delivered ones can, and the further you are from the front month the less likely it is to happen to you.

## Margin and leverage

CME's maintenance margin for CL is set by SPAN on a volatility that is structurally higher than equities. A broker republication at 110% of the CME figure showed $10,869 in September 2026, implying an exchange maintenance requirement of roughly $9,900 per contract; take that as an approximate, undated figure and check the CME margins page for the live one. Against a notional of $92,410 (Nov 2026 at $92.41) that is about 10.7% of notional, or roughly 9x leverage, lower leverage than ES because the exchange expects bigger daily moves. It does.

## What moves it

Crude has more scheduled catalysts than any index future:

- **EIA Weekly Petroleum Status Report**, Wednesdays at 10:30 a.m. ET (Thursday after a Monday holiday): U.S. crude, gasoline and distillate inventories. The most reliable weekly volatility event in the contract.
- **API inventory estimate**, Tuesdays at 4:30 p.m. ET, the industry's preview of the EIA number.
- **OPEC+ meetings** and production-quota announcements, which reset the supply side for months.
- **Geopolitics** affecting supply routes and producing regions; the reaction is fastest in the overnight session, when the book is thin.
- **The dollar**: crude is priced in dollars, so a stronger dollar tends to lower the price in dollar terms.
- **Refinery runs, maintenance seasons, hurricanes** in the Gulf of Mexico, and Strategic Petroleum Reserve releases.
- **The curve itself**: a steep backwardation signals tight inventories and rewards longs who roll; a contango signals glut.

The year to 2026-09-24 illustrates the scale. The front contract ranged from $54.98 (2025-12-16) to $119.48 (2026-03-09), a 117% rise in under three months followed by a slide back to the low $90s. Month-end closes went $57.42 (December 2025), $65.21 (January), $67.02 (February), $101.38 (March), $105.07 (April), $87.36 (May), $69.50 (June), $84.67 (July), $85.76 (August). No index future moved like that.

## Worked example

Figures from the Yahoo Finance CL=F daily series (pulled 2026-09-24) and the CME spec page. A trader is long one CL at the 2026-04-07 close of $112.95. The next session, 2026-04-08, the contract closed at $94.41.

Daily change: $94.41 - $112.95 = -$18.54 per barrel.

Variation margin: -$18.54 x 1,000 barrels = -$18,540.00, debited that evening.

Against the approximate exchange maintenance margin of $9,900, the one-day loss was 1.87 times the entire performance bond. Any account holding the position with margin near the minimum ended the day in deficit: a $15,000 account long one contract was at -$3,540 before the broker could act, assuming a fill at the close. The intraday path was worse; the day's range extended below the close.

Now the same year's worst gap. On 2026-03-10 the contract opened 9.52% below the 2026-03-09 close of $119.48: an open around $108.10, a gap of about $11.38 per barrel, or $11,380 per contract, between one session's settlement and the next session's first trade. No stop order could have filled inside that gap, because there was no trade inside it.

Tick arithmetic for sizing: at $92.41 a 1% move is $0.92, 92 ticks, $924 per CL contract or $92.40 per MCL. A 2% adverse open (the capstone scenario applied to crude) is $1,848 per CL. The 2026-04-08 move was 16.4%, eight of those.

Finally the term structure from Lesson 5, as a roll matter. On 2026-09-24 the Nov/Dec spread was $92.41 - $89.47 = $2.94. A long rolling from November to December sells at $92.41 and buys at $89.47, collecting $2,940 per contract of backwardation, which the December contract will hand back as it converges to whatever spot is on its own expiry. As with ES, the spread is carry, not profit; here the carry runs in the long's favour because inventories are tight.

## Table

| Row from the spec page | WTI Crude Oil (CL) | Micro WTI (MCL) |
|---|---|---|
| Contract unit | 1,000 barrels | 100 barrels |
| Price quotation | $ per barrel | $ per barrel |
| Minimum tick | $0.01 | $0.01 |
| Tick value | $10.00 | $1.00 |
| Value of a $1.00 move | $1,000 | $100 |
| Contract months | Monthly | Monthly |
| Termination | 3 business days before the 25th of the prior month (4 if the 25th is not a business day); CLX26: 2026-10-20 | Same reference; MCL terminates one day earlier |
| Settlement | Physical delivery, Cushing OK | Cash, to the CL settlement |
| Notional at $92.41 (2026-09-24) | $92,410 | $9,241 |
| Approx. exchange maintenance margin | About $9,900 (derived from a broker republication at 110%, Sept 2026; verify) | About one-tenth |
| Worst day in year to 2026-09-24 | -16.41% on 2026-04-08 = -$18,540 | -$1,854 |
| Trading hours (ET) | Sun 6 p.m. to Fri 5 p.m., 60-min daily break | Same |

## Sources

- CME Group, WTI Crude Oil futures contract specifications — https://www.cmegroup.com/markets/energy/crude-oil/light-sweet-crude.contractSpecs.html
- CME Group, WTI Crude Oil margins — https://www.cmegroup.com/markets/energy/crude-oil/light-sweet-crude.margins.html
- U.S. Energy Information Administration, Weekly Petroleum Status Report — https://www.eia.gov/petroleum/supply/weekly/
- CFTC, "Basics of Futures Trading" — https://www.cftc.gov/LearnAndProtect/EducationCenter/FuturesMarketBasics/index.htm
