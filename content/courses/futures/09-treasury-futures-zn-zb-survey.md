---
{
  "title": "Rates Survey: 10-Year Note (ZN) and T-Bond (ZB) Futures",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "ZN is quoted at 105-02 (105 and 2/32). What is the dollar value of one contract at that price?", "opts": ["$10,506.25", "$105,062.50", "$1,050,625", "$105.06"], "correct": 1, "explain": "105 + 2/32 = 105.0625% of $100,000 face = $105,062.50. One full point is $1,000."},
    {"q": "What is the minimum tick and its value on ZN, and on ZB?", "opts": ["1/32 = $31.25 on both", "ZN: half of 1/32 = $15.625; ZB: 1/32 = $31.25", "ZN: 1/64 = $31.25; ZB: 1/32 = $15.625", "0.01 = $10 on both"], "correct": 1, "explain": "ZN ticks in halves of a 32nd ($15.625); ZB ticks in full 32nds ($31.25). Both have $100,000 face and $1,000 per point."},
    {"q": "Yields rise. What happens to ZN and ZB prices?", "opts": ["Both rise", "Both fall, ZB by more per basis point", "ZN rises, ZB falls", "Nothing until delivery"], "correct": 1, "explain": "Bond prices move inversely to yields. ZB's deliverable basket has 15 to 25 years of maturity, so it has far more duration than ZN's 6.5 to 10 years."},
    {"q": "Why must a retail long exit ZN before the first notice day rather than the last trading day?", "opts": ["Because the contract is cash-settled on first notice", "Because from first notice day a short can assign delivery of $100,000 face of actual notes to a long", "Because margin doubles", "Because volume disappears"], "correct": 1, "explain": "Treasury futures are physically delivered; delivery can be initiated by shorts from the first notice day, which for the Dec contract falls at the end of November, weeks before the last trading day."},
    {"q": "Between 2026-09-18 and 2026-09-23 the 10-year yield rose 11.6 bp and ZN fell about 1.05 points. Roughly what was one ZN contract's sensitivity per basis point over that window?", "opts": ["About $9", "About $90", "About $900", "About $9,000"], "correct": 1, "explain": "1.05 points x $1,000 = $1,050, divided by 11.6 bp = about $90 per bp for that move; the precise DV01 depends on the cheapest-to-deliver note."}
  ],
  "task": "Find the first notice day and last trading day for the December 2026 ZN contract on the CME calendar and note how many weeks apart they are."
}
---

## What the contracts are

The CBOT Treasury complex is the deepest interest-rate futures market in the world, and it is where the price of money is discovered for everyone from mortgage lenders to the pension fund in Lesson 1. This lesson surveys the two most traded: the 10-Year U.S. Treasury Note future (product code ZN) and the U.S. Treasury Bond future (ZB). Both trade on CME Globex and clear through CME Clearing.

Each contract's unit is **$100,000 face value** of U.S. Treasury securities. Prices are quoted as a percentage of par in points and fractions of a 32nd, an old convention that trips people up. A quote of 105-02 means 105 and 2/32 = 105.0625% of face. One full point is $1,000 per contract. ZN's minimum tick is one half of a 32nd, 0.015625 points, worth $15.625; ZB's minimum tick is a full 32nd, 0.03125 points, worth $31.25.

Contract months are the quarterly cycle, March, June, September and December. Trading hours are Sunday to Friday 6:00 p.m. to 5:00 p.m. ET with a 60-minute daily break.

## Delivery, and why first notice day is the date that matters

Unlike ES, Treasury futures are **physically delivered**. A short who holds to delivery must deliver $100,000 face of an eligible Treasury; a long who holds must pay for and receive it, through the Federal Reserve's book-entry system. Eligible securities for ZN are notes with between 6.5 and 10 years remaining to maturity; for ZB, bonds with at least 15 and less than 25 years. Each eligible issue has a **conversion factor** that normalises it to a 6% notional coupon, and the short chooses which to deliver, which is always the **cheapest-to-deliver** (CTD). The CTD is the security the futures contract actually tracks, and it changes as yields move.

Delivery can be initiated by the short from the **first notice day**, which for these contracts is the last business day of the month before the delivery month; for December 2026 that is late November. The **last trading day** is the seventh business day before the last business day of the delivery month, in the third week of December. A retail long must be out before first notice, not before last trade; otherwise they can be assigned $105,000 of notes to pay for. Brokers enforce this with a forced liquidation date, as with crude.

## Price, yield and duration

Bond prices move inversely to yields. The sensitivity of a contract's dollar value to a one-basis-point move in yield is its **DV01**, and it depends on the CTD's duration. ZB, with a 15-to-25-year basket, has roughly twice to three times the DV01 of ZN. Neither number is fixed; the exchange does not publish a multiplier per basis point because there isn't one. You estimate it from the CTD or, more crudely, from recent price and yield moves, as the worked example does.

## What moves them

- **The FOMC**: eight scheduled decisions a year, plus the minutes three weeks later. The front end reacts to the funds rate; ZN and ZB react to the path and to the statement's tone.
- **Inflation and employment data**: CPI, PCE, the monthly jobs report, all at 8:30 a.m. ET, in a thinner book than the U.S. open.
- **Treasury supply**: the quarterly refunding announcement and the 3-, 10- and 30-year auctions at 1:00 p.m. ET. A weak 30-year auction moves ZB in seconds.
- **Term premium and fiscal news**: deficits, ratings actions, foreign demand. These move the long end more than the short end, so ZB relative to ZN.
- **Risk-off flows**: on equity selloffs Treasuries often rally, so ZN is a common hedge against ES. On 2025-10-10, ES's worst day of the year (-2.71%), ZN rose 0.58% and ZB 1.23%, their best days of the year. The relationship is not reliable enough to count on; the 2026-09-23 session had ES down 0.76% and ZN down 0.91%.

## Worked example

Prices from Yahoo Finance daily bars for ZN=F, ZB=F, ^TNX (10-year yield) and ^TYX (30-year yield), pulled 2026-09-24; spec values from the CME pages. Yahoo rounds the 32nds to two decimals, so the fractions below are reconstructed to the nearest tick.

Contract values on 2026-09-24. ZNZ26 last traded 105.0625 = 105-02: value 1.050625 x $100,000 = $105,062.50. ZBZ26 last traded 105.75 = 105-24: value $105,750.00. The 10-year yield was 5.114% and the 30-year 5.401% on 2026-09-23.

The year's move. ZN's high close was 114.375 (114-12) on 2026-03-02 and its low 104.875 (104-28) on 2026-09-23: a fall of 9.5 points, $9,500 per contract, as the 10-year yield rose from the low fours toward 5.1%. ZB fell from a high of 119.59375 (119-19) on 2025-10-22 to 105.625 (105-20) on 2026-09-24: 13.96875 points, $13,968.75 per contract. Same direction, half again as large, which is the duration difference.

Worst days. ZN's worst daily change in the year was 2026-09-23: 106.00 to 105.03125 (105-01), a fall of 0.96875 points = 31/32 = 62 ZN ticks. Loss per contract: 62 x $15.625 = $968.75, or 0.96875 x $1,000 = $968.75. ZB's worst was 2026-05-15: 112.46875 (112-15) to 110.625 (110-20), a fall of 1.84375 points = 59/32 = 59 ZB ticks. Loss: 59 x $31.25 = $1,843.75.

An empirical DV01. Between 2026-09-18 and 2026-09-23 the 10-year yield moved from 4.998% to 5.114%, +11.6 basis points, while ZN moved from about 106.08 to 105.03, -1.05 points, or -$1,050 per contract. Ratio: $1,050 / 11.6 = about $90 per basis point. For ZB over the same window: 30-year yield 5.331% to 5.401%, +7.0 bp; price 107.56 to 105.88, -1.68 points = -$1,680; about $240 per basis point. These are rough, because the futures track the CTD rather than the on-the-run benchmark, but the ratio of roughly 2.7 to 1 between ZB and ZN is the duration story in one number.

Margin and leverage. A broker republication at 110% of CME's figures showed $2,062 for ZN and $4,070 for ZB in September 2026, implying exchange maintenance of about $1,875 and $3,700. Against contract values of $105,062.50 and $105,750.00 those are 1.8% and 3.5% of notional, leverage of roughly 56x and 29x. The leverage is higher than ES because the daily volatility is lower, and the worst-day losses above, $968.75 and $1,843.75, are each about half of the respective maintenance margin. Verify the live figures on the CME margins pages before trading.

## Table

| Row from the spec page | 10-Year T-Note (ZN) | T-Bond (ZB) |
|---|---|---|
| Contract unit | $100,000 face value | $100,000 face value |
| Deliverable grade | 6.5 to 10 years remaining | 15 to less than 25 years remaining |
| Price quotation | Points and halves of 1/32 of par | Points and 1/32 of par |
| Minimum tick | 0.015625 (half a 32nd) | 0.03125 (one 32nd) |
| Tick value | $15.625 | $31.25 |
| Value of one point | $1,000 | $1,000 |
| Contract months | Mar, Jun, Sep, Dec | Mar, Jun, Sep, Dec |
| First notice day | Last business day of month before delivery month | Same |
| Last trading day | 7th business day before last business day of delivery month | Same |
| Settlement | Physical delivery via Fed book-entry | Same |
| Value at 2026-09-24 last trade | $105,062.50 (105-02) | $105,750.00 (105-24) |
| Approx. exchange maintenance margin | About $1,875 (derived, Sept 2026; verify) | About $3,700 (derived; verify) |
| Worst day, year to 2026-09-24 | -$968.75 (2026-09-23) | -$1,843.75 (2026-05-15) |
| Empirical $ per bp, 09-18 to 09-23 | About $90 | About $240 |

## Sources

- CME Group, 10-Year T-Note futures contract specifications — https://www.cmegroup.com/markets/interest-rates/us-treasury/10-year-us-treasury-note.contractSpecs.html
- CME Group, U.S. Treasury Bond futures contract specifications — https://www.cmegroup.com/markets/interest-rates/us-treasury/30-year-us-treasury-bond.contractSpecs.html
- CME Group, 10-Year T-Note margins — https://www.cmegroup.com/markets/interest-rates/us-treasury/10-year-us-treasury-note.margins.html
- U.S. Department of the Treasury, Daily Treasury Par Yield Curve Rates — https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202609
