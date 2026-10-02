---
{
  "title": "Capstone: Rank, Select and Compute Expectancy",
  "duration": "45 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The capstone's ranking date is 2026-06-30 and the lookback is six months. The starting close for the relative-strength calculation is therefore from:", "opts": ["2026-01-02", "2025-12-31", "2025-06-30", "2026-03-31"], "correct": 1, "explain": "Six months before the ranking date is the last trading day of 2025, 2025-12-31. Using any other start date changes every number in the ranking."},
    {"q": "CAT closed at 572.87 on 2025-12-31 and 1064.90 on 2026-06-30. Its six-month relative strength is:", "opts": ["+49.2%", "+85.9%", "+185.9%", "+46.2%"], "correct": 1, "explain": "1064.90 / 572.87 − 1 = 1.859 − 1 = +85.9%. It ranked first of twenty by a wide margin."},
    {"q": "With a $50,000 account, 1% risk and a 2-ATR stop, CAT's ATR of 39.78 on 2026-06-30 implies a position of:", "opts": ["62 shares", "6 shares, about $6,389", "12 shares", "25 shares"], "correct": 1, "explain": "Stop distance 2 × 39.78 = 79.56; 500 / 79.56 = 6.28, rounded down to 6 shares; 6 × 1064.90 = $6,389, or 12.8% of the account."},
    {"q": "Expectancy of a set of trades is computed as:", "opts": ["Total profit divided by the number of winners", "Win rate × average winning R plus loss rate × average losing R, which equals the average R per trade", "Average winner minus average loser", "The best trade's R"], "correct": 1, "explain": "For the prior-year answer key, 0.429 × 1.97 + 0.571 × (−1.03) = 0.845 − 0.588 = +0.26R per trade."},
    {"q": "Your prior-year expectancy comes out at +0.19R rather than the answer key's +0.26R. Under the rubric this:", "opts": ["Fails the exercise", "Is acceptable if every trade is listed with its entry, stop and exit and the differences are explained (ATR seeding, rounding, fill assumptions); the method is graded, not the match to the key", "Means Yahoo's data changed", "Should be adjusted upward to match"], "correct": 1, "explain": "Small implementation choices move the result by tenths of an R. A transparent trade list that can be checked is worth more than a matching number that cannot."}
  ],
  "task": "Submit the capstone: the ranked table, three trade plans, the prior-year trade list with expectancy, and the one-page write-up."
}
---

This capstone asks you to do, on a stated date with public data, what the course has been building toward: rank a universe, choose the strongest names, plan each trade completely, and measure what the same rule would have delivered over the prior year. Everything you need is in lessons 4 through 12. The answer key at the end lets you check your ranking and your expectancy; the rubric tells you how the work is graded, and it grades the method more than the match.

## The exercise

**Universe.** The twenty stocks used throughout: AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA, AVGO, JPM, V, UNH, LLY, XOM, COST, HD, PG, NFLX, CAT, WMT, JNJ.

**Data.** Daily bars from Yahoo Finance's chart API: `https://query1.finance.yahoo.com/v8/finance/chart/<TICKER>?range=2y&interval=1d`. Record the date you pulled them. Use unadjusted closes for the ranking and for all price levels; use the open, high, low and close for triggers, stops and fills.

**Account.** $50,000, 1% risk per trade, maximum 25% of equity in one position, maximum 5% portfolio heat.

### Part 1: rank

Ranking date: **2026-06-30**. Lookback: six months, so the starting close is that of **2025-12-31**. For each stock compute close(2026-06-30) / close(2025-12-31) − 1. Produce a table of all twenty, sorted from strongest to weakest, with both closes and the percentage. State SPY's return over the same window beneath it.

### Part 2: select and plan

Take the top three. For each, write a complete trade plan as of the close of 2026-06-30:

1. **Trigger.** Which of the three triggers from lesson 5 applies, and the exact price and condition. If the stock is already above its 20-day high, say so and specify the pullback condition instead. State the 50-day average and whether it is rising.
2. **Stop.** The 14-day ATR on 2026-06-30, the 2-ATR distance, and the technical level nearest to it. State which stop you would use and why, per lesson 6.
3. **Size.** Shares from $500 / (2 × ATR), rounded down; the position value; its share of the account; and whether the 25% cap binds.
4. **Exit.** The 10-day-low trailing rule, stated with the 10-day low as of 2026-06-30 so the initial trailing level is known.
5. **Events.** The next scheduled earnings date for the company, from its investor relations page or EDGAR, and what the plan does if a report falls within the expected holding period.

Then compute the portfolio heat if all three are entered at full size and confirm it is within the cap.

### Part 3: the prior year's expectancy

Run the lesson-12 baseline rule over the twenty stocks for signals from **2025-07-01 to 2026-06-30**, with the same fills, stop, exit and costs. Produce the trade list: ticker, signal date, entry date and price, stop, exit date and price, exit reason, R after costs. Then compute:

- number of trades, win rate, average winning R, average losing R;
- expectancy = win rate × average win + loss rate × average loss;
- total R, and the account return at 1% risk per trade;
- the breakdown of average R by exit reason.

State SPY's return over the same window for comparison.

### Part 4: write-up

One page. What the ranking says about leadership on 2026-06-30. Whether the three trade plans are ones you would actually take, and if not, why. What the prior-year expectancy does and does not tell you about the next year, in the terms of lesson 12's final section. Any place where your numbers differ from the answer key, with the reason.

## Worked example

This is the answer key for the parts that have one answer, with the arithmetic shown. Computed from Yahoo Finance daily bars pulled 2026-09-24.

**Ranking.** The top of the table:

CAT: 1064.90 / 572.87 − 1 = **+85.9%**.
UNH: 415.63 / 330.11 − 1 = **+25.9%**.
JNJ: 253.97 / 206.95 − 1 = **+22.7%**.
GOOGL: 357.37 / 313.00 − 1 = +14.2%. XOM: 136.72 / 120.34 − 1 = +13.6%. LLY: 1199.43 / 1074.68 − 1 = +11.6%.

The bottom three were META (−14.7%), MSFT (−22.9%) and NFLX (−23.8%). SPY over the window, 2025-07-01 to 2026-06-30, returned +20.9%.

Compare this with the 2026-03-31 ranking in lesson 4. CAT and JNJ are in the top three on both dates; XOM slipped from first to fifth; UNH went from eighteenth to second on the strength of its spring recovery. That is what a six-month ranking looks like three months later: the leaders persist, the middle churns.

**Sizes on 2026-06-30.** ATR(14) and the resulting positions at $500 risk and a 2-ATR stop:

CAT: ATR 39.78, stop distance 79.56, 500 / 79.56 = 6.28, so **6 shares**, 6 × 1064.90 = **$6,389** (12.8% of equity).
UNH: ATR 10.04, stop distance 20.08, 500 / 20.08 = 24.9, so **24 shares**, 24 × 415.63 = **$9,975** (20.0%).
JNJ: ATR 5.66, stop distance 11.32, 500 / 11.32 = 44.2, so **44 shares**, 44 × 253.97 = **$11,175** (22.4%).

No position breaches the 25% cap. Heat if all three are entered: 6 × 79.56 + 24 × 20.08 + 44 × 11.32 = 477 + 482 + 498 = $1,457, or 2.9% of equity, within the 5% cap. Your trigger, technical stop and earnings sections are judged on reasoning, not on matching a key.

**Prior-year expectancy.** The baseline rule from 2025-07-01 to 2026-06-30 produced **70 trades**: 30 winners and 40 losers, a win rate of **42.9%**. Average winner **+1.97R**, average loser **−1.03R**.

Expectancy = 0.429 × 1.97 + 0.571 × (−1.03) = 0.845 − 0.588 = **+0.26R** per trade. Total **+18.0R**. By exit reason: 40 trailing exits averaging +1.34R, 26 stops averaging −1.05R, 4 gaps through the stop averaging −2.13R. Best trades: XOM entered 2025-12-30, +8.84R; CAT entered 2025-09-17, +7.28R; GOOGL entered 2025-08-11, +4.53R. Worst: UNH entered 2026-01-23, −3.42R on the 2026-01-27 gap.

If your figures land within a few tenths of an R of these with a checkable trade list, the difference is implementation: how the ATR was seeded, whether a stop touched on the entry day counts, rounding of fills. Explain the difference; do not adjust to match.

## Table

The full 2026-06-30 ranking for checking Part 1:

| Rank | Ticker | 6-month RS | Rank | Ticker | 6-month RS |
|---|---|---|---|---|---|
| 1 | CAT | +85.9% | 11 | AMZN | +3.3% |
| 2 | UNH | +25.9% | 12 | HD | +2.5% |
| 3 | JNJ | +22.7% | 13 | PG | +2.3% |
| 4 | GOOGL | +14.2% | 14 | WMT | +1.7% |
| 5 | XOM | +13.6% | 15 | JPM | +1.6% |
| 6 | LLY | +11.6% | 16 | V | −2.2% |
| 7 | AVGO | +9.1% | 17 | TSLA | −6.5% |
| 8 | COST | +8.5% | 18 | META | −14.7% |
| 9 | NVDA | +7.3% | 19 | MSFT | −22.9% |
| 10 | AAPL | +6.4% | 20 | NFLX | −23.8% |

## Rubric

| Criterion | What earns full marks | Points |
|---|---|---|
| Ranking (Part 1) | All twenty computed from the stated closes, sorted, SPY stated; matches the key within rounding; data pull date recorded | 15 |
| Trade plans (Part 2) | Each of the three has a numeric trigger, a stop with both the ATR and the technical level, a share count with the cap checked, the initial trailing level, and an earnings date with a stated action; heat computed | 25 |
| Expectancy (Part 3) | Full trade list with entries, stops, exits and reasons; costs applied; win rate, average win and loss, expectancy, total R and exit-reason breakdown computed correctly from the list; SPY stated | 35 |
| Honesty and interpretation (Part 4) | Differences from the key explained rather than hidden; the limits of a one-year sample stated; any plan you would not take identified with a reason | 15 |
| Reproducibility | A reader with the same data source can recompute every number from what is written | 10 |
| **Total** | | **100** |

A submission that matches the key but cannot be recomputed from its own pages scores lower than one that differs by 0.05R and shows every step.

## Sources

- Jegadeesh, N. and Titman, S. (1993). Returns to buying winners and selling losers. *Journal of Finance*, 48(1), 65–91. https://doi.org/10.1111/j.1540-6261.1993.tb04702.x
- Bailey, D. H., Borwein, J. M., López de Prado, M. and Zhu, Q. J. (2014). Pseudo-mathematics and financial charlatanism. *Notices of the American Mathematical Society*, 61(5), 458–471. https://doi.org/10.1090/noti1105
- U.S. Securities and Exchange Commission, EDGAR full-text search (for scheduled reports and 8-K filings). https://www.sec.gov/edgar/search/
- Yahoo Finance historical data, CAT: https://finance.yahoo.com/quote/CAT/history/
