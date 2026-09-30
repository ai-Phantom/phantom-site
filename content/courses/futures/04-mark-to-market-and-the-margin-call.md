---
{
  "title": "Mark-to-Market, Daily Settlement and the Margin Call",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "You are long one ES bought at 7,613.25. The daily settlement is 7,571.75. What happens to your account that evening?", "opts": ["Nothing until you close the trade", "$2,075 is debited as variation margin", "$2,075 is held as unrealised loss but no cash moves", "Your broker lends you $2,075"], "correct": 1, "explain": "(7,571.75 - 7,613.25) x $50 = -$2,075. Futures losses are settled in cash every day; the money leaves your account whether or not you close."},
    {"q": "Which statement about variation margin is correct?", "opts": ["It is a one-time deposit when you open the trade", "It is the daily cash transfer equal to the change in settlement value", "It is charged only when you receive a margin call", "It is interest on the performance bond"], "correct": 1, "explain": "Variation margin is the daily pay-and-collect. The performance bond (initial/maintenance) is separate collateral held against future variation."},
    {"q": "A $30,000 account long one ES (maintenance $25,024, initial $27,526) closes the day with equity of $19,362.50. What is the margin call?", "opts": ["$5,661.50, to restore maintenance", "$8,163.50, to restore initial", "$10,637.50, to restore the starting balance", "None, because equity is positive"], "correct": 1, "explain": "A margin call restores the initial level: $27,526 - $19,362.50 = $8,163.50. Restoring only to maintenance is not enough."},
    {"q": "Why can a futures loss exceed the money in your account?", "opts": ["Because brokers add hidden fees", "Because daily settlement is only an estimate", "Because you are obligated on the full notional, and a gap can move price past any liquidation level before a trade can be done", "It cannot; losses are capped at the margin posted"], "correct": 2, "explain": "The bond is collateral, not a limit. If the market gaps through your liquidation point, the loss on the full contract is yours and the broker will pursue the deficit."},
    {"q": "With the account in the question above, at what ES settlement price would equity first fall below maintenance?", "opts": ["7,613.25 - 99.52 = 7,513.75", "7,613.25 - 50.00 = 7,563.25", "7,613.25 - 212.75 = 7,400.50", "7,613.25 - 550.52 = 7,062.75"], "correct": 0, "explain": "Cushion above maintenance = $30,000 - $25,024 = $4,976; divided by $50 per point = 99.52 points. Any settlement below about 7,513.75 triggers the call."}
  ],
  "task": "Find your broker's written margin-call policy (deadline to meet a call, whether it liquidates automatically, and at what level) and paste the relevant sentences into your trading notes."
}
---

## Futures profit and loss is cash, every day

In a stock account an open position can sit with an unrealised loss for years and no money moves. Futures do not work that way. Every business day the exchange publishes a **daily settlement price** for each contract, the clearinghouse revalues every open position at that price, and the difference from the previous settlement is transferred in cash between the losing and winning accounts. This is **mark-to-market**, and the cash that moves is called **variation margin**.

The consequence is that you never hold an unrealised futures loss overnight. If the settlement went against you by 40 points on one ES, $2,000 left your account that evening. If you close the trade the next day at a better price, the money comes back through the same channel. Your broker's screen may still show an "open P&L" for convenience, but the cash has already moved.

Daily settlement is the mechanism that lets the clearinghouse guarantee every trade with a bond of only 7% of notional. It never allows a loss to accumulate beyond one day's move before it is collected. The performance bond covers that one day; variation margin collects everything else as it happens.

## Settlement price versus last trade

The settlement is not necessarily the last traded price of the session. For ES the exchange derives it from trading around the cash-market close, typically a volume-weighted price over a short window at 3:00 p.m. CT (4:00 p.m. ET), with the procedure published on the CME settlement-procedures page for equity index products. Trading continues until 5:00 p.m. ET, so the session's final tick and the settlement usually differ by a few ticks. Your daily variation margin is computed against the settlement, not against your platform's last print, which is why the debit can be a little larger or smaller than you expected.

## Initial, maintenance, and the call

Recall the two levels from Lesson 3. You need **initial margin** to open. Once open, your account equity, meaning cash plus or minus the running variation, may fall as low as **maintenance margin** without consequence. The moment settlement takes equity below maintenance, the broker issues a **margin call**: a demand to deposit enough to bring equity back up to the *initial* level, not merely back to maintenance.

That asymmetry is deliberate. Restoring to initial rebuilds a cushion of 10% of maintenance above the trigger, so that a normal day does not produce another call tomorrow. It also means a call is always larger than the amount by which you breached.

Brokers differ on what happens next, and their agreement governs. Common terms: the call must be met by a deadline (often before the next session, sometimes within hours); if it is not, the broker may liquidate enough of the position to bring the account into compliance; and many brokers reserve the right to liquidate immediately, without a call, if equity falls below some fraction of maintenance intraday. Read your agreement. The margin call you imagine, a phone call and a day to wire money, is the courteous version and increasingly rare.

## What a margin call looks like in practice

The notice itself is undramatic: an email or platform banner stating the account's equity, the requirement, the shortfall and the deadline, sometimes with the words "margin deficiency" rather than "call." What makes it consequential is what sits behind it. Until the deficiency is cured you cannot add positions, and most brokers will not let you replace a liquidated contract even after a favourable move. If the deadline passes, the liquidation is done at market, at the broker's chosen moment, and the fill is recorded in your account like any other trade, with the slippage of whatever hour they chose. Wiring funds takes hours; a same-day call issued at 5:30 p.m. ET may need to be met before the 6:00 p.m. reopen. The only comfortable way to receive a margin call is to have arranged never to receive one, by sizing so that the maintenance level is far below any move you expect to survive.

## Deficit: the part nobody plans for

A performance bond is collateral, not a ceiling on your loss. If the market gaps past the point where liquidation would have saved you, the loss on the full contract is still yours. A $30,000 account long one ES through a 10% overnight gap (777 points, $38,862.50) ends the day at negative $8,862.50, and the broker will pursue the debit balance. This is what the CFTC means by "can be required to pay more than they invested initially." It is rare in ES; it is not rare in crude oil, which is why Lesson 8 exists.

## Worked example

Use the real ES daily closes of early June 2026 from Yahoo Finance's ES=F series, standing in for settlements. A trader with a $30,000 account buys one ES at the 2026-06-01 close of 7,613.25. The CME initial margin is $27,526 and maintenance $25,024 (CME margins page figure, republished 2026-08-18), so the account qualifies to open with $2,474 to spare. Multiplier $50.

First, the margin-call trigger. Cushion above maintenance = $30,000 - $25,024 = $4,976. In points: $4,976 / $50 = 99.52. The account breaches maintenance at any settlement below 7,613.25 - 99.52 = 7,513.73, in practice a settlement of 7,513.50 or lower.

Now mark to market each day. Equity = $30,000 + (settlement - 7,613.25) x $50.

- 2026-06-02, close 7,623.75: +10.50 pts, +$525.00, equity $30,525.00. Variation credit.
- 2026-06-03, close 7,571.75: -52.00 pts from the prior settlement, -$2,600.00 that day; equity $27,925.00. Above initial, no action.
- 2026-06-04, close 7,601.00: +29.25 pts, +$1,462.50; equity $29,387.50.
- 2026-06-05, close 7,400.50: -200.50 pts, -$10,025.00 in one session (a -2.64% day, the second worst of the year); equity $19,362.50. That is $5,661.50 below maintenance. Margin call = $27,526 - $19,362.50 = $8,163.50, due per the broker's deadline. Note the trigger price of 7,513.73 was blown through by 113 points; the intraday low was 7,359.00, at which equity had touched $17,287.50.
- If the call is met, the account holds $27,526 of equity with the position still open. 2026-06-08, close 7,416.00: +15.50 pts, +$775.00; equity $28,301.00.
- 2026-06-09, close 7,392.75: -23.25 pts, -$1,162.50; equity $27,138.50. Below initial but above maintenance, no call.
- 2026-06-10, close 7,278.50: -114.25 pts, -$5,712.50; equity $21,426.00. Second call: $27,526 - $21,426.00 = $6,100.00.

Without the first deposit the account would have stood at $13,262.50 on 06-10, 47% of maintenance, and the broker would have liquidated days earlier. Total deposits demanded across seven sessions: $14,263.50, against an initial account of $30,000, on a position that at no point exceeded the exchange's own margin definition of "one contract".

![Line chart of account equity for a $30,000 account long one ES from the 2026-06-01 close of 7,613.25, marked to each daily close through 2026-06-10, with dashed lines at the $27,526 initial and $25,024 maintenance margins; the 2026-06-05 settlement of 7,400.50 takes equity to $19,362.50. Prices from Yahoo Finance ES=F; margins from the CME Group E-mini S&P 500 margins page as republished 2026-08-18.](figures/margin-call-path.svg)

## Table

| Date (2026) | Settlement proxy | Points vs prior | Variation | Equity before deposits | Status |
|---|---|---|---|---|---|
| 06-01 | 7,613.25 | entry | — | $30,000.00 | opened; initial $27,526 met |
| 06-02 | 7,623.75 | +10.50 | +$525.00 | $30,525.00 | ok |
| 06-03 | 7,571.75 | -52.00 | -$2,600.00 | $27,925.00 | ok |
| 06-04 | 7,601.00 | +29.25 | +$1,462.50 | $29,387.50 | ok |
| 06-05 | 7,400.50 | -200.50 | -$10,025.00 | $19,362.50 | call $8,163.50 |
| 06-08 | 7,416.00 | +15.50 | +$775.00 | $20,137.50 | (if unmet: liquidation) |
| 06-09 | 7,392.75 | -23.25 | -$1,162.50 | $18,975.00 | |
| 06-10 | 7,278.50 | -114.25 | -$5,712.50 | $13,262.50 | 47% of maintenance |

Closes from Yahoo Finance ES=F daily bars pulled 2026-09-30; they stand in for CME settlements, which differ by a few ticks.

## Sources

- CME Group, Performance Bonds/Margins FAQ — https://www.cmegroup.com/solutions/risk-management/performance-bonds-margins/faq-performance-bonds-margins.html
- CME Group, E-mini S&P 500 margins — https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.margins.html
- CFTC, "Basics of Futures Trading" — https://www.cftc.gov/LearnAndProtect/EducationCenter/FuturesMarketBasics/index.htm
