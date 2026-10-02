---
{
  "title": "Capstone: Price a One-Month BTC Cash-and-Carry",
  "duration": "45 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Using the 2026-09-24 07:28 UTC snapshot (index 84,256.40, BTC-30OCT26 mark 84,719.61, 36 days), the annualised basis is", "opts": ["0.55%", "5.57%", "4.03%", "2.18%"], "correct": 1, "explain": "463.21 over 84,256.40 is 0.5498% for 36 days; times 365 over 36 is 5.57%."},
    {"q": "The liquidation price of a 3x short perpetual opened at 84,268.18 with 0.5% maintenance margin is", "opts": ["56,600", "84,690", "111,936", "126,402"], "correct": 2, "explain": "Entry times (1 + 1/3 minus 0.005) = 84,268.18 times 1.32833 = 111,936.23, a 32.8% rally."},
    {"q": "At Kraken Tier 5 maker fees (0.15% each spot leg) and a 0.035% future taker fee, the net carry on 1 BTC via the October future is", "opts": ["$463.21", "$180.79", "$334.74", "Negative"], "correct": 1, "explain": "463.21 minus 252.77 minus 29.65 is $180.79, which is less than the $334.74 a 13-week bill would pay on the same capital over 36 days."},
    {"q": "Over the previous 30 days the perpetual short would have received 0.374% of notional in funding, $315.16 on 1 BTC. The perp carry after the same fees nets", "opts": ["$315.16", "$3.40", "$180.79", "$278.95"], "correct": 1, "explain": "315.16 minus 252.77 of spot fees minus 58.99 of perp fees (open and close) is $3.40, against $278.95 the bill would pay over 30 days."},
    {"q": "The exit plan for a collapsing basis must be written before entry because", "opts": ["Venues require it", "The collapse arrives with negative funding, a rallying or crashing price, or a halted venue, and each demands a different action that cannot be reasoned out under margin pressure", "Basis never collapses", "It is needed for taxes"], "correct": 1, "explain": "Lessons 7 and 12 gave the three failure modes. The rubric awards points for a plan with explicit triggers, not for a plan that says you will decide at the time."}
  ],
  "task": "Submit your carry pricing with every calculation shown and score it against the rubric before reading the worked example."
}
---

## The exercise

Price a one-month BTC cash-and-carry trade on a stated date, from a snapshot you take yourself or from the one supplied below, and write the plan for its failure. The exercise is graded on whether every number can be traced to a source and a formula, not on whether the trade looks attractive. In the sample solution it does not, and recognising that is part of the grade.

Use 1 BTC of notional unless you prefer your own size. Show every calculation. Cite every price to the endpoint and timestamp it came from.

### Supplied snapshot, 2026-09-24 07:28 UTC

From Deribit's public API: btc_usd index 84,256.40; BTC-PERPETUAL mark 84,268.18, funding_8h 0.004549%; BTC-30OCT26 mark 84,719.61, expiring 2026-10-30 08:00 UTC (36.0 days); BTC-27NOV26 mark 85,079.43 (64 days); maker fee 0.015%, taker 0.035%. From Deribit's funding history: hourly funding on BTC-PERPETUAL summed to 0.374% of notional over the 30 days to 2026-09-24 08:00 UTC. From BitMEX's instrument endpoint: maintenance margin 0.5%. From Yahoo Finance: ^IRX (13-week T-bill) 4.028% on 2026-09-23; BTC-USD 2026 year-to-date daily standard deviation 2.45%. From Kraken's fee schedule: Tier 1 maker 0.40%, taker 0.80%; Tier 5 maker 0.15%, taker 0.30%; Tier 12 maker 0.00%, taker 0.10%.

If you take your own snapshot, record the UTC timestamp of every quote and pull them within the same minute.

### Part 1: the basis

State spot (or index), the dated future's mark and its exact days to expiry. Compute the dollar basis, the basis as a percentage, and the simple annualised basis. Do the same for the next tenor and comment on the shape of the curve. State the perpetual's current 8-hour funding rate and its simple annualised equivalent, and the realised funding over the previous 30 days from the venue's history endpoint.

### Part 2: the perp leg at 3x

For a 1 BTC short perpetual at the mark, compute the margin posted at 3x and the liquidation price using the venue's maintenance margin. Express the distance to liquidation in per cent and in daily standard deviations. State where the margin to defend the short would come from if BTC rallied 20%, and how long it would take to get there.

### Part 3: funding over the month

Compute the funding the short receives over 30 days two ways: the current rate held constant (rate × 90 periods × notional) and the realised sum of the previous 30 days. State which you would budget on and why.

### Part 4: fees, cash, and the verdict

Choose a fee tier and state it. Compute fees for the spot buy, the spot sell, and the derivative leg (open only for the future, open and close for the perp). Compute the net carry for the future version and the perp version. Compute what the same capital earns in 13-week bills over the same days. State, in one sentence each, whether the future carry and the perp carry beat cash at your tier, and at what spot fee rate the future carry would exactly match the bill.

### Part 5: the exit plan

Write the plan for three events, each with a numeric trigger and a specific action: funding turns negative (state the rate and duration that triggers action), the price moves against the short (state the price at which you add margin, from where, and the price at which you close both legs), and the derivatives venue halts withdrawals (state which of re-hedge, unwind or hold you do, and within what time). Then state the single condition under which you would enter this trade at all.

## Worked example

Basis: 84,719.61 − 84,256.40 = $463.21 = 0.5498% over 36 days = 5.57% annualised; November gives 0.9768% over 64 days = 5.57%; the curve is flat. Perp funding 0.004549% × 1,095 = 4.98% annualised on the print; 0.374% realised over 30 days = 4.55%.

Liquidation: margin 84,268.18 ÷ 3 = $28,089.39; liquidation at 84,268.18 × (1 + 1/3 − 0.005) = $111,936.23, 32.8% away, 13.4 daily sigmas. A 20% rally to 101,121.82 costs the short $16,853.64, leaving $11,235.76; the spot gain of the same size sits on the other venue and must be withdrawn, confirmed and deposited to reach the short.

Funding: constant-rate 84,268.18 × 0.00004549 × 90 = $345.02; realised 84,268.18 × 0.00374 = $315.16. Budget on the smaller, and on nothing if the last month included a negative stretch.

Fees at Tier 5 maker for spot (0.15%) and taker for the derivative (0.035%): spot legs $252.77; future $29.65; perp $58.99. Future net: 463.21 − 252.77 − 29.65 = $180.79 (2.18% annualised). Perp net: 315.16 − 252.77 − 58.99 = $3.40. Bills: $334.74 over 36 days, $278.95 over 30. Neither version beats cash at this tier. The future version matches the bill when spot fees total 463.21 − 29.65 − 334.74 = $98.82, or 0.059% per leg; only Tier 12 clears it, netting $433.56.

## Chart

![Dollar decomposition of the 1 BTC cash-and-carry against BTC-30OCT26 from the sample solution: basis captured $463.21, spot fees at Tier 5 maker (0.15% each way) −$252.77, future taker fee −$29.65, net carry $180.79, against $334.74 that the 13-week Treasury bill (4.028%, Yahoo ^IRX, 2026-09-23) would pay on the same $84,256.40 over 36 days.](figures/capstone-carry-pnl.svg)

Exit plan, sample: funding below −0.01% per 8 hours for three consecutive prints closes the perp short and rolls into the October future if its basis is still positive, otherwise unwinds both legs. Price: at 95,000 (a 12.7% rally, 5.2 sigmas) transfer $10,000 from the spot venue to the derivatives venue; at 105,000 close both legs regardless of basis. Venue halt: unwind the spot within one hour of confirming the halt, book the frozen margin as a receivable at its last mark, do not re-hedge. Entry condition: net carry after fees exceeds the bill by at least 2 points annualised, which on this snapshot requires either a fee tier below 0.06% on spot or a basis above 7.5%.

## Rubric

| Criterion | What earns full marks | Points |
|---|---|---|
| Basis pricing | Spot, future mark, exact days and timestamp stated with source; dollar, percentage and annualised basis computed for two tenors; perp funding annualised from the print and from realised history | 20 |
| Liquidation arithmetic | Margin at 3x, maintenance rate cited to the venue, liquidation price from the formula, distance in per cent and daily sigmas, margin-transfer path described with a time estimate | 20 |
| Funding over the month | Both methods computed, difference explained, a budgeting choice stated with a reason that references the funding history's sign | 15 |
| Fees and cash comparison | Fee tier stated and cited; every leg's fee computed; net carry for both versions; T-bill return on the same capital over the same days; the break-even spot fee derived | 20 |
| Exit plan | Three events each with a numeric trigger and a specific action; the venue-halt action chosen from re-hedge, unwind or hold with a time limit; a stated entry condition that references cash, not zero | 20 |
| Traceability | Every number traceable to a cited endpoint, page or formula in this course; no unsourced rates; the verdict follows from the numbers rather than from the trade's appeal | 5 |

Total: 100. A submission scoring 80 or more with no criterion below half marks has priced a carry trade the way a desk would. A submission that concludes the trade is attractive at an entry-tier fee schedule has made an arithmetic error somewhere in Part 4 and should find it before any money follows.

## Sources

- Deribit API, public/get_book_summary_by_currency, public/ticker, public/get_funding_rate_history, public/get_instruments (snapshot 2026-09-24 07:28 UTC): https://docs.deribit.com/
- BitMEX REST API, GET /instrument?symbol=XBTUSD (maintenance margin 0.5%): https://www.bitmex.com/api/explorer/
- Yahoo Finance chart API, ^IRX and BTC-USD daily bars: https://query1.finance.yahoo.com/v8/finance/chart/%5EIRX?range=1mo&interval=1d
- Kraken, "Fee Schedule" (spot maker-taker tiers): https://www.kraken.com/features/fee-schedule
