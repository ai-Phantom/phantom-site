---
{
  "title": "Leverage and Liquidation: Why 100x Liquidates on Noise",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "With initial margin 1% and maintenance margin 0.5%, how far must price fall to liquidate a 100x long opened at 84,268.18?", "opts": ["1%", "0.5%, to about 83,847", "10%", "It cannot be liquidated"], "correct": 1, "explain": "Distance = 1/leverage minus maintenance = 1% minus 0.5% = 0.5%. 84,268.18 times 0.995 is 83,846.84."},
    {"q": "BTC's realised daily standard deviation in 2026 year to date is about 2.45%. A 0.5% liquidation distance is therefore", "opts": ["Two standard deviations", "About one fifth of a standard deviation", "Ten standard deviations", "Unrelated to volatility"], "correct": 1, "explain": "0.5 divided by 2.45 is 0.2. A move that small happens many times inside a normal day; the position is liquidated by noise, not by a trend."},
    {"q": "A 3x short perpetual opened at 84,268.18 with 0.5% maintenance is liquidated at about", "opts": ["56,600", "111,936", "84,690", "168,536"], "correct": 1, "explain": "Short liquidation = entry times (1 + 1/L minus m) = 84,268.18 times 1.32833 = 111,936. Price must rise 32.8%."},
    {"q": "Why does the liquidation price depend on the mark price rather than the last trade?", "opts": ["Mark is lower", "Because the engine marks margin to an index-anchored price so a single thin-book print cannot trigger it", "Mark updates once a day", "Regulators require it"], "correct": 1, "explain": "Lesson 5 covered the three prices. Liquidation checks maintenance against unrealised P&L at the mark."},
    {"q": "What happens to the margin left in a position when the engine liquidates it?", "opts": ["It is returned in full", "The engine closes the position; remaining margin goes to the insurance fund or covers the shortfall, and the trader typically receives nothing", "It is converted to spot", "It is doubled"], "correct": 1, "explain": "Liquidation is not a stop-loss at the maintenance level. The engine takes over the position and the maintenance margin is consumed by the close and the fund."}
  ],
  "task": "For your largest open or planned leveraged position, compute its liquidation price by hand from the venue's maintenance margin, then compare that distance to the asset's realised daily standard deviation."
}
---

## Leverage is a distance, not a multiplier

Retail platforms sell leverage as a multiplier on gains. The useful way to think about it is as a distance: the percentage move against you at which the venue closes your position and keeps your margin. That distance is set by two numbers on the contract's specification page, the initial margin and the maintenance margin, and it can be computed before you trade. Almost nobody does, which is why liquidation is the most common way retail crypto accounts end.

## The two margins

BitMEX's public instrument endpoint for XBTUSD, queried on 2026-09-24, reports initMargin 0.01 and maintMargin 0.005. Initial margin of 1% means the venue will open a position on 1% of its notional: 100x leverage. Maintenance margin of 0.5% means the venue will keep the position open only while your margin balance, marked to the mark price, remains at least 0.5% of notional. Deribit and other venues publish their own tables, and most step the maintenance rate up with position size so that a very large account cannot run 100x on a position the book could not absorb; the exact table is on each venue's margin page and the arithmetic below applies to whichever numbers you find there.

The initial margin you choose to post is what sets your leverage. Post 1% and you are at 100x; post 33.3% and you are at 3x. Maintenance does not change with your choice. So the distance to liquidation is the gap between what you posted and what the venue insists you keep.

## The formula

For an isolated-margin position with leverage L (so initial margin 1/L) and maintenance margin m, ignoring fees and funding:

- Long liquidation price = entry × (1 − 1/L + m).
- Short liquidation price = entry × (1 + 1/L − m).
- Distance to liquidation = 1/L − m.

With cross margin, the whole account balance backs the position, so the distance is larger and depends on your other positions; the same formula applies with the account's free balance in place of 1/L. Funding payments and fees drain margin over time, which pulls the liquidation price toward the entry for a long that pays funding. Venues also charge a liquidation fee out of the maintenance margin, which is why you receive nothing back.

## Chart

![Adverse price move that triggers liquidation as a function of leverage, from the formula distance = 1/L minus 0.5% maintenance (BitMEX XBTUSD maintMargin). At 100x the distance is 0.5%; at 3x it is 32.8%. The dashed line is one daily standard deviation of BTC-USD close-to-close returns in 2026 year to date, 2.45%, computed from Yahoo Finance daily bars: every leverage above about 20x is liquidated by a one-sigma day.](figures/liquidation-distance-vs-leverage.svg)

## Worked example

Open a long at the Deribit BTC-PERPETUAL mark of 84,268.18 (2026-09-24 07:28 UTC), and use the BitMEX margin parameters of m = 0.5%. Compute the liquidation price at each leverage.

- 100x: distance 1/100 − 0.005 = 0.005 = 0.5%. Liquidation at 84,268.18 × 0.995 = 83,846.84.
- 50x: 0.02 − 0.005 = 1.5%. Liquidation 84,268.18 × 0.985 = 83,004.16.
- 20x: 0.05 − 0.005 = 4.5%. Liquidation 80,476.11.
- 10x: 0.10 − 0.005 = 9.5%. Liquidation 76,262.70.
- 5x: 0.20 − 0.005 = 19.5%. Liquidation 67,835.88.
- 3x: 0.3333 − 0.005 = 32.83%. Liquidation 56,600.13.
- 2x: 0.50 − 0.005 = 49.5%. Liquidation 42,555.43.

Now put those distances against how much BTC actually moves. Yahoo Finance's daily BTC-USD closes for 2026 year to date give an annualised realised volatility of 46.8% (lesson 9). The daily standard deviation is 46.8% ÷ √365 = 2.45%. So:

- 100x: 0.5% ÷ 2.45% = 0.2 sigma. A move this size occurs, in either direction, on essentially every day, usually several times intraday.
- 50x: 1.5% = 0.6 sigma. Most days.
- 20x: 4.5% = 1.8 sigma. About one day in fourteen closes beyond this in one direction; intraday ranges reach it more often.
- 10x: 9.5% = 3.9 sigma on a daily close, but BTC's worst single day in 2022 was −17.4% and in 2025 was −9.1%, so a 10x long is one bad day from zero.
- 3x: 32.8%. BTC fell 32.5% from its 2025-10-06 close of $124,753 to the 2026-09-24 close of $84,242, so a 3x long opened at the top, held with no margin added, would have been liquidated during the following year.

The short side of the capstone's carry trade: a 3x short opened at 84,268.18 is liquidated at 84,268.18 × (1 + 0.3333 − 0.005) = 111,936.23, a 32.8% rally. The margin posted is 84,268.18 ÷ 3 = $28,089.39. If BTC rallies 20% to 101,121.82 the short's unrealised loss is $16,853.64, leaving $11,235.76 of margin, 13.3% of the original notional against a maintenance requirement that at the new price is 0.5% × 101,121.82 = $505.61, so the position survives; but the spot leg's $16,853 gain is on another venue and cannot be posted unless you move it, which takes a withdrawal, a confirmation and a deposit, at 03:00 on a Sunday if that is when the rally comes.

## Why 100x liquidates on noise

A liquidation distance of 0.5% is inside the bid-ask bounce of a volatile day. It is also inside the gap between mark and last that lesson 5 described: the mark can sit tens of dollars from the last trade, and $421 (0.5% of 84,268) is not a large number. The 100x position is not a bet on direction; it is a bet that the mark price will not wander half a per cent in the wrong direction before it wanders in the right one, and the realised volatility says it will, with high probability, within hours.

Venues know this. The insurance fund exists because liquidations at 100x frequently cannot be closed at the maintenance level in a fast market, and the fund absorbs the gap; when it cannot, auto-deleveraging closes profitable positions on the other side without their consent. High leverage is therefore not just a risk to the trader using it but to everyone on the venue.

## The practical rule

Compute the liquidation price before every leveraged order and write it on the order ticket next to the stop. If the liquidation price is closer than three daily standard deviations, you are not trading the asset, you are trading the noise. For BTC at 2.45% a day that means a distance of at least 7.4%, which caps leverage at roughly 12x on this maintenance table, and a trader who wants to survive a 2022-style −17% day needs a distance above that, which caps it near 5x. Lesson 12 pushes the number lower still once the 76.6% drawdown is on the table.

## Margin that leaks

The formula above assumes the margin you posted is still there. It is not, for two reasons. Funding (lesson 6) is debited from margin every period, so a long paying 0.374% of notional over a month has, at 10x, lost 3.7% of its posted margin to funding alone, and its liquidation price has crept toward the entry by roughly 0.37% of price. Fees on the opening trade come out of the same balance. Recompute the liquidation price after every funding timestamp, or keep a buffer of at least the expected month of funding above the formula's result. Cross margin hides this leak by drawing on the account balance, which is convenient until several positions draw on it at once.

## Sources

- BitMEX REST API, GET /instrument?symbol=XBTUSD (initMargin 0.01, maintMargin 0.005, read 2026-09-24): https://www.bitmex.com/api/explorer/
- BitMEX, "Isolated Margin" (isolated versus cross margin mechanics): https://www.bitmex.com/app/isolatedMargin
- Deribit Knowledge Base, "Margin and Liquidation" (tiered maintenance margin, mark-based liquidation): https://www.deribit.com/kb/deribit-margin-and-liquidation
- Yahoo Finance chart API, BTC-USD daily bars (2026 year-to-date realised volatility): https://query1.finance.yahoo.com/v8/finance/chart/BTC-USD?range=2y&interval=1d
