---
{
  "title": "Funding-Rate Arithmetic: From 8-Hour Prints to Annualised Cost",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "BitMEX's XBTUSD funding print at 20:00 UTC on 2021-04-10 was 0.2997% per 8 hours. Annualised simply, that is", "opts": ["3.3%", "32.8%", "328%", "0.9%"], "correct": 2, "explain": "0.2997% times 3 periods a day times 365 days is 328.2% per year. Longs were paying shorts nearly the whole position each year at that rate."},
    {"q": "Over the 30 days to 2026-09-24 08:00 UTC, Deribit's hourly funding on BTC-PERPETUAL summed to 0.374% of notional. On a $84,268 long that is", "opts": ["$3.74", "$31.52", "$315.16", "$3,151.60"], "correct": 2, "explain": "84,268 times 0.00374 is $315.16 paid by the long over the month, about 4.55% annualised."},
    {"q": "The 2022-11-11 funding print of minus 0.2514% per 8 hours means", "opts": ["Longs paid shorts 0.2514%", "Shorts paid longs 0.2514% of notional, because the perp traded below the index during the FTX collapse", "Nobody paid", "The exchange charged a fee"], "correct": 1, "explain": "Negative funding flows from shorts to longs. In a panic the perp trades at a discount and the crowded short side pays."},
    {"q": "Why is 'funding times 1,095' only an approximation of the annual cost?", "opts": ["There are 1,096 periods", "Funding is not constant: it varies every period, and the chart shows it moving between minus 0.0027% and 0.0189% in ninety days", "Funding is paid once a year", "It ignores the spread"], "correct": 1, "explain": "Annualising a single print assumes it persists. The realised cost is the sum of the actual prints, which is why the lesson also sums 30 days of hourly rates."},
    {"q": "Two venues reported different mean 8-hour rates over the same 33 days: 0.00417% and 0.00614%. This tells you", "opts": ["One venue is lying", "Funding is venue-specific, set by each book's own premium and formula, so a hedge across venues is not riskless", "They must be averaged", "The lower one is always cheaper"], "correct": 1, "explain": "Each perpetual has its own premium and its own rule. The rate you pay is the one on the venue where your position sits."}
  ],
  "task": "Pull thirty days of funding history for one perpetual from its venue's public API, sum the prints, and convert the total to a dollar cost on the position size you actually trade."
}
---

## Why the arithmetic matters

Funding is the only cost of a perpetual that does not appear in the fee schedule, and it is usually the largest. A trader who checks the fee page and sees 0.035% taker fees concludes that holding a perp is cheap. The same trader, long through a euphoric month, discovers that funding took several per cent of the position. This lesson does the arithmetic from real prints so that you never again read a funding rate without immediately knowing what it costs per day and per year.

Three conventions to fix first. Funding is quoted as a percentage of position notional per period. Most venues pay every 8 hours, so there are 3 periods a day and 1,095 a year; Deribit accrues hourly and reports an 8-hour equivalent, so its history is 24 rows a day. "Annualised" in this course means the simple product rate × periods per year, with no compounding, because funding is paid in cash, not reinvested.

## The four numbers behind every print

- Notional: contract quantity × mark price, in dollars.
- Rate: the 8-hour funding rate, signed. Positive means longs pay shorts.
- Payment per period: notional × rate.
- Annualised: rate × 1,095.

That is the whole toolkit. Everything below is applying it to numbers pulled from the venues' own history endpoints on 2026-09-24.

## Chart

![Deribit BTC-PERPETUAL 8-hour funding rate, daily average of the hourly interest_8h field, 2026-06-26 to 2026-09-24, from the public get_funding_rate_history endpoint. The dashed lines mark zero and the 0.01% interest floor used by BitMEX-style formulas; the marked point is 2026-09-21 at 0.0189%, the ninety-day high, equivalent to 20.7% annualised.](figures/deribit-btc-funding-90d.svg)

The ninety days in the chart are a quiet period. The daily average sat between −0.0027% (2026-09-05) and 0.0189% (2026-09-21), mostly positive and mostly below the 0.01% floor. The fourteen-month history behind it ran from a high of 0.0663% per 8 hours (2025-10-11 04:00 UTC, five days after BTC's cycle high close of $124,753) to a low of −0.0287% (2026-06-04). The monthly means tell the story of the cycle: 0.0087% in October 2025 near the top, 0.0001% in November, −0.0013% in February 2026, then a slow return to 0.004% by the summer.

## Worked example

Take a $50,000 long position in a BTC perpetual, and apply four real prints.

**Print 1: a euphoric top.** BitMEX's funding history endpoint for XBTUSD reports a rate of 0.002997 (0.2997%) at 2021-04-10 20:00 UTC, the highest print in April and May 2021, four days before BTC's then all-time high.

- Payment per period: 50,000 × 0.002997 = $149.85.
- Per day: 149.85 × 3 = $449.55.
- Annualised rate: 0.002997 × 1,095 = 3.282 = 328.2%.
- Annualised cost on $50,000 if it persisted: $164,086, more than three times the position.

Nobody paid 328% for a year; the point is that at that moment holding a leveraged long cost 0.9% of notional per day, and a position that was flat on price for ten days lost 9%. The mean print across the two months was 0.0201% per 8 hours, 22% annualised, still enormous.

**Print 2: a panic bottom.** The same endpoint for November 2022 shows −0.002514 (−0.2514%) at 2022-11-11 04:00 UTC, the morning FTX filed for bankruptcy (lesson 3).

- Payment per period: 50,000 × (−0.002514) = −$125.70. The sign means the short pays; the $50,000 long receives $125.70.
- Per day, if repeated: $377.10 received.
- Annualised: −0.002514 × 1,095 = −275.3%. Shorts were paying longs at a 275% annual rate to stay short.

The November 2022 mean was −0.0171% per 8 hours, −18.7% annualised. Being short the perp during the collapse was correct on price and expensive to hold.

**Print 3: today's rate.** Deribit's ticker on 2026-09-24 07:28 UTC reported funding_8h of 0.00004549 (0.004549%).

- Payment per period: 50,000 × 0.00004549 = $2.27.
- Per day: $6.82.
- Annualised: 0.00004549 × 1,095 = 4.98%.

**Print 4: what a month actually cost.** Annualising one print assumes it persists, and the chart shows it does not. So sum the real history. Deribit's get_funding_rate_history returned 719 hourly rows for 2026-08-25 08:00 to 2026-09-24 08:00 UTC. Summing the interest_1h field gives 0.00374, i.e. 0.374% of notional paid by longs over the 30 days.

- Cost on $50,000: 50,000 × 0.00374 = $187.00.
- Cost on a 1 BTC position at the mark of $84,268.18: 84,268.18 × 0.00374 = $315.16.
- Annualised realised: 0.374% × 365 ÷ 30 = 4.55%.

Compare with print 3's 4.98%: the single print overstated the realised month by about a tenth. Over the same window OKX's history endpoint for BTC-USDT-SWAP shows 100 8-hour prints averaging 0.00614%, which annualises to 6.72%; Deribit's mean 8-hour rate for the period was 0.00417%, or 4.57%. Same asset, same month, two venues, a 2-point gap in annual cost. The rate you pay is the one on the venue holding your position, which is why the carry trade in lesson 7 is not riskless across venues.

**Sanity check against the interest floor.** The 0.01% floor annualises to 10.95%. Every 2026 print in the chart is below it, which means that in this period the BitMEX-style clamp would not have bound and Deribit's continuous method produced lower rates than a floor-based formula. In April 2021 the floor was irrelevant because the premium term was thirty times larger.

## Reading a funding table quickly

A print of 0.01% is $1 per $10,000 per period, $3 per day, 10.95% per year. Memorise that anchor and scale: 0.1% is ten times it (109.5% per year), 0.001% is a tenth (1.1% per year). When you see a rate you should be able to say the annual number within a second, and if the annual number is above the return you expect from the trade over its holding period, the trade is a funding trade whether you meant it to be or not.

Two traps. First, some venues display funding per 4 hours or per 1 hour; multiply by the right number of periods (2,190 or 8,760). Second, "predicted" funding is an estimate of the next payment from the current premium; the realised rate is fixed only at the timestamp, and positions opened a minute before that timestamp pay the full period's rate.

## Booking funding in your own ledger

Funding never shows up as a trade, so most journals miss it. It is debited or credited to the margin balance at each timestamp, which means a position that is flat on price silently shrinks or grows. Record it as its own line: date, rate, notional at the mark, and the signed dollar amount. Over a month the sum of that column is the true carrying cost of the position, and it is the number to compare against the trade's expected edge.

Two checks make the ledger honest. Reconcile the sum of your recorded payments against the venue's own funding history for your account; a mismatch means you missed a period, usually one at 00:00 UTC on a weekend. And when you evaluate a strategy that holds perpetuals, subtract realised funding from gross P&L before you compute anything else. A long-only perp strategy in April 2021 that showed a 15% gross gain was, after funding at 0.9% a day for a fortnight, close to flat, and a backtest that ignores funding will never tell you that.

## Sources

- BitMEX REST API, GET /funding, XBTUSD (prints for 2021-04-10 and 2022-11-11 quoted above): https://www.bitmex.com/api/explorer/
- Deribit API, public/get_funding_rate_history, BTC-PERPETUAL (hourly rows 2025-07-31 to 2026-09-24): https://docs.deribit.com/#public-get_funding_rate_history
- OKX API v5, public data, "Get funding rate history", BTC-USDT-SWAP: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-funding-rate-history
- BitMEX, "Perpetual Contracts Guide" (interest rate floor and clamp): https://www.bitmex.com/app/perpetualContractsGuide
