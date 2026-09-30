---
{
  "title": "Rolling: Expiry, the Roll Date, Roll Cost and Continuous Charts",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "You are long ESZ26 on 2026-12-10 and want to stay long into 2027. What is the cleanest way to roll?", "opts": ["Sell ESZ26 at market, wait, buy ESH27 later", "Do nothing; the exchange rolls you", "Sell the ESZ26/ESH27 calendar spread as one order, which sells Dec and buys Mar simultaneously", "Buy ESH27 and let ESZ26 expire into it"], "correct": 2, "explain": "The calendar spread is a single instrument on Globex with its own book and a 0.05 tick. One fill, no leg risk. Letting Dec expire cash-settles it; it does not convert into March."},
    {"q": "With ESZ26 at 7,772.50 and ESH27 at 7,833.55, a long who rolls pays 61.05 points more for March. What is that 61.05 mostly?", "opts": ["A fee charged by CME", "The cost of carry (r - q) for one quarter, which the March contract will give back as it converges", "Slippage", "The expected rise in the S&P"], "correct": 1, "explain": "The spread is carry. March will converge toward spot by March, so the 61 is not a loss at the moment of the roll; the true friction is commissions plus the spread's bid-ask."},
    {"q": "On the CME equity index roll convention, when does most volume move from the expiring December contract to March?", "opts": ["On the third Friday itself", "The Thursday eight days before expiry (2026-12-10 for the Dec 2026 roll)", "The first business day of December", "The Monday after expiry"], "correct": 1, "explain": "Volume and open interest migrate on the Thursday of the week before expiration week. Trading the expiring month after that means thinner books."},
    {"q": "A back-adjusted continuous ES chart shows prices from 2018 that are lower than the contracts actually traded then. Why?", "opts": ["Data error", "Every roll's spread has been subtracted from all earlier prices so that there are no jumps at the splices", "The index was rebased", "Dividends have been removed"], "correct": 1, "explain": "Back-adjustment removes roll gaps by shifting the whole prior history by each spread. It preserves point changes but destroys historical levels; unadjusted charts do the reverse."},
    {"q": "Yahoo Finance's ES=F series shows a close of 7,657.35 on 2026-09-18. Why should you distrust that bar?", "opts": ["ES only trades in 0.25 increments, so a fractional close is a vendor splice or settlement artefact on expiry day", "The market was closed", "It is a March contract price", "Volume was zero"], "correct": 0, "explain": "A real ES print is a multiple of 0.25. The fractional expiry-day closes (also 2026-06-18 and 2026-03-20) are the vendor merging the final settlement or SOQ into the continuous series."}
  ],
  "task": "Put the Dec 2026 roll date (Thursday 2026-12-10) and the expiry (Friday 2026-12-18, 9:30 a.m. ET) in your calendar, and write down which day your broker starts liquidating expiring equity index positions."
}
---

## Contracts end; positions do not have to

A futures contract has a last trading day. If you want exposure beyond it, you must move your position to a later contract before it expires. That transaction is the **roll**, and for a retail trader in ES it happens four times a year. It is mechanical but not free, and the way it is recorded on charts has confused more backtests than any other feature of futures.

## The expiry, restated

ES, NQ and the micros stop trading at 9:30 a.m. ET on the third Friday of the contract month and cash-settle to the Special Opening Quotation. For December 2026 that is Friday 2026-12-18. If you hold ESZ26 into that morning you do not "get" March; you receive or pay the difference between your last settlement and the SOQ, and you are flat. If you want to stay long, you have to buy March yourself.

Most brokers do not let a retail account reach that point. They set a cut-off, often the close of the Thursday before expiry or earlier, after which they liquidate expiring positions at market. That liquidation is at their timing, not yours. Know the date.

## The roll date

CME's equity index roll convention is that liquidity moves from the expiring quarterly to the next one on the Thursday eight days before expiration, the Thursday of the week *before* expiration week. For the December 2026 roll that is Thursday 2026-12-10. On that day, the March contract typically becomes the front month by volume; by the following Monday the December book is noticeably thinner and by Thursday 2026-12-17 it is a shadow. The pattern is visible in the previous roll: in the Yahoo Finance ES=F daily series, the bars for 2026-09-15, 09-16 and 09-17 show volumes of 943,078, 487,789 and 285,399 as the September contract emptied out, against 1.3 to 2.1 million on ordinary days that month.

The practical rule: roll on or just after the roll date, while both months are liquid. Rolling a week early means paying carry on a spread that still has a wide book; rolling on expiry morning means trading a dead contract.

## How to roll

Do not sell December and then buy March as two separate orders. Between the two fills the market can move, and you carry leg risk. Globex lists the **calendar spread** ESZ26-ESH27 as its own instrument with its own order book and a tick of 0.05 index points ($2.50). Selling the spread sells December and buys March at a single net price in one fill; buying it does the reverse. A long who wants to stay long sells the Dec/Mar spread. A short buys it.

The spread's price is the March premium over December, and from Lesson 5 you know what it should be: roughly the carry, r - q, for one quarter.

## Roll cost, separated into its parts

Traders say "the roll cost me 61 points." Be precise about what was paid.

**Carry.** The March contract is priced above December by the fair-value premium. A long pays that premium when rolling. But March will converge toward spot over the next quarter, so the premium is returned through the daily marks as time passes, provided rates and dividends behave. It is the cost of financing the leverage for one more quarter, and you offset it by earning the bill rate on the cash you did not spend. It is a cost relative to holding SPY, not a loss at the moment of the roll.

**Friction.** Two commissions (one per leg; brokers usually charge the spread as two contracts) plus the bid-ask on the spread, typically one spread tick of $2.50 on ES, plus any slippage if you use a market order in a thin moment. This is the part you lose outright, and it is small: a few dollars per contract, four times a year.

**Mistiming.** If you roll after the cut-off and get liquidated, or roll on expiry morning in a thin book, the cost can be several outright ticks per leg. This is the only part that scales badly, and it is entirely avoidable.

## Worked example

All figures dated. ESZ26 closed at 7,772.50 on 2026-09-23 (Yahoo Finance). From Lesson 5, with the 13-week bill at 4.14% (Treasury, 2026-09-23) and a trailing SPY dividend yield of 0.99%, the fair December-to-March premium for the 91 days between 2026-12-18 and 2027-03-19 is 7,772.50 x 0.0315 x 91/365 = 61.04 points, so a fair spread quote is 61.05 (tick 0.05).

A trader is long one ES and rolls on Thursday 2026-12-10 by selling the ESZ26-ESH27 calendar spread at 61.05, assuming the same premium. Commission assumed at $2.50 per contract per side (use your own).

Carry component: 61.05 points x $50 = $3,052.50. This is the amount by which the March entry price exceeds the December exit price. It is recovered as March converges: if the S&P is unchanged on 2027-03-19, March settles at spot and the trader has "lost" 61.05 points on the March leg, exactly the carry. Over the same quarter the $27,526 of margin plus the rest of the notional that the trader did not have to spend, about $388,625 in total, could have earned 4.14% x 91/365 = 1.032%, or $4,010.75, against dividends forgone of 0.99% x 91/365 x $388,625 = $959.30. Net of everything the futures holder is $4,010.75 - $959.30 - $3,052.50 = -$1.05 versus the stock holder: zero, to within rounding, which is the no-arbitrage condition doing its job.

Friction component: commissions 2 x $2.50 = $5.00; one spread tick of bid-ask, 0.05 x $50 = $2.50; total $7.50 per roll, $30.00 per year for a permanent one-contract long. For ten MES the commissions are ten times larger, $50.00 per roll, since each micro is its own contract.

Mistiming component, for comparison: rolling with two market orders on expiry morning and losing one outright tick on each leg costs 2 x $12.50 = $25.00, more than three times the friction of a proper spread order.

Annual carry for a permanent long: four rolls x roughly 61 points = about 244 points, 3.15% of the index, which equals r - q. That is the price of holding $388,625 of exposure with $27,526 of collateral.

![Flow diagram of the December 2026 ES roll in five steps: the expiring ESZ26 contract (last trade 9:30 a.m. ET on 2026-12-18), the roll date on Thursday 2026-12-10, selling the Dec/Mar calendar spread as one order with a 0.05 tick, the spread as carry (about 61 points at r 4.14% and q 0.99%) plus friction, and the splice on continuous charts. Dates from the CME third-Friday rule; carry from this lesson's worked example.](figures/quarterly-roll.svg)

## Table

| Continuous-contract method | What it does at each roll | Historical levels | Point changes | Use it for |
|---|---|---|---|---|
| Unadjusted (splice) | Switches series to the new front month; leaves a gap equal to the spread | Correct | Wrong across the splice (a 61-point phantom jump in contango) | Reading actual traded prices |
| Back-adjusted (difference) | Subtracts each spread from all earlier prices | Wrong; can go negative in commodities | Correct | Backtesting point-based systems |
| Ratio-adjusted | Multiplies earlier prices by the roll ratio | Wrong | Percent changes correct | Backtesting percent-based systems |
| Vendor blend (e.g. Yahoo ES=F) | Undocumented splice; expiry-day bars may carry the settlement or SOQ | Mostly correct, with artefacts | Fractional closes 7,657.35 (2026-09-18), 7,508.43 (2026-06-18), 6,594.63 (2026-03-20) | Quick looks only |

The three fractional closes are from the Yahoo Finance ES=F daily series pulled 2026-09-24. A real ES trade is always a multiple of 0.25.

## Sources

- CME Group, E-mini S&P 500 contract specifications — https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.contractSpecs.html
- CME Group, Equity index products page (roll and listing information) — https://www.cmegroup.com/markets/equities/micro-emini-equity.html
- U.S. Department of the Treasury, Daily Treasury Bill Rates — https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_bill_rates&field_tdr_date_value_month=202609
