---
{
  "title": "Earnings and News Inside a Swing",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Across the 20-stock universe from 2024-09 to 2026-09, opening gaps of 5% or more occurred on what share of stock-days?", "opts": ["About 10%", "About 1.3%, 134 of 9,991", "Less than 0.1%", "About 25%"], "correct": 1, "explain": "Rare per day, but with twenty names over two years they arrive more than once a week somewhere in the book. The question is never whether but where."},
    {"q": "The average size of those gaps, measured in the prior day's ATR, was about 2.5, and 73 of 134 exceeded 2 ATRs. For a stop placed 2 ATRs below entry this means:", "opts": ["The stop will always hold", "More than half of large gaps jump straight through a 2-ATR stop, so the fill lands well beyond it and the loss exceeds the planned 1R", "Stops should be removed before earnings", "ATR is the wrong measure"], "correct": 1, "explain": "A stop is a market order once triggered. On a gap it fills at the open, which was on average 2.5 ATRs away and sometimes 5 or 6."},
    {"q": "UNH opened at 481.95 on 2025-04-17 after closing at 585.04 the day before. In ATR terms that gap was:", "opts": ["About −1 ATR", "About −2 ATRs", "About −5.7 ATRs", "About −0.5 ATR"], "correct": 2, "explain": "The gap was −17.6% of price, which was 5.7 times the prior 14-day ATR. The system's UNH position, entered 2025-04-09 with a 2-ATR stop, exited at the open for −2.29R."},
    {"q": "In the sample, upward gaps of 5% or more were followed by an average further gain of about +3.3% over the next ten sessions with 68% positive. Downward gaps were followed by:", "opts": ["An average further fall of −5%", "An average further move of about +1.4%, with only 54% continuing lower; no downside drift showed up in this sample", "Exactly zero", "A reversal in every case"], "correct": 1, "explain": "The post-gap drift documented in the earnings literature appeared on the upside here and not on the downside. The lesson reports both rather than the half that fits the story."},
    {"q": "The lesson's rule for a position that will be held through a scheduled earnings report is:", "opts": ["Double the position", "Either exit before the report, or cut the size so that a 3-ATR gap costs no more than the planned 1% of equity", "Move the stop closer", "Convert to a limit order"], "correct": 1, "explain": "A tighter stop does nothing against a gap. Only size limits what a gap can cost, and the report date is known in advance."}
  ],
  "task": "For every stock on your ranked list, find the next scheduled earnings date from the company's investor relations page or its most recent 8-K on EDGAR, and mark which ones fall within the next three weeks."
}
---

A swing trade lives overnight, and overnight is when the news arrives. Most days it is noise. A few times a year per stock it is a scheduled earnings report, and a handful of times it is something nobody scheduled. This lesson measures how often large gaps happened in the course's twenty stocks, what they did to a 2-ATR stop, whether the move continued afterwards, and what to do about a report that falls inside a position you are already in.

## What the literature says about earnings

Ball and Brown (1968) were the first to show that stock prices continue to drift in the direction of an earnings surprise for weeks after the announcement. Bernard and Thomas (1989) measured the drift carefully: sorting stocks by the size of the surprise, the top decile kept outperforming the bottom decile for about sixty trading days after the report, by several percentage points. The effect is called post-earnings-announcement drift and it is one of the reasons momentum exists at all; Chan, Jegadeesh and Lakonishok (1996) showed that price momentum and earnings-surprise momentum overlap, with each carrying information the other does not.

For a swing trader the drift is a source of setups: the breakout that follows a strong report is one of the cleanest triggers there is, because the range it clears was formed before the information arrived. The report itself, though, is a different animal. Before it, you do not know the direction, only that the move will be large. Trading the report is a bet on the coin; trading the drift is a bet on the tail.

## Worked example

Data: daily bars for the twenty stocks from Yahoo Finance's chart API, pulled 2026-09-24, covering 2024-09-25 to 2026-09-23, 9,991 stock-days. A gap is the open divided by the prior close, minus one. The ATR is the 14-day value as of the prior close, so the gap is measured against the volatility a trader would have known when placing the stop.

Gaps of 5% or more in either direction: **134**, or 1.34% of stock-days. That is rare per stock per day and frequent for a book: with twenty names, a 5% gap landed somewhere in the universe about every seven sessions.

Measured in ATRs, the mean absolute gap was **2.51 ATRs**. Seventy-three of the 134, more than half, exceeded 2 ATRs; forty-seven exceeded 3. A stop placed 2 ATRs below entry, which is the course default, would have been jumped rather than hit by most of them. When a stop is jumped, the order fills at the open, and the loss is the gap, not the stop.

By ticker, the gaps concentrated: TSLA 19, AVGO 15, UNH 14, META 14, AMZN 11, NFLX 9, LLY 9, NVDA 9. Two names, TSLA and AVGO, produced a quarter of them. That is a sizing input: a stock that gaps 5% every six weeks needs a smaller position than its ATR alone implies, because the ATR is the average of ordinary days and the gaps are the days that matter.

The largest gaps and what followed over the next ten sessions:

| Ticker | Date | Gap | Gap in ATRs | Next 10 sessions |
|---|---|---|---|---|
| AVGO | 2024-12-13 | +18.4% | +5.3 | +4.8% |
| UNH | 2025-04-17 | −17.6% | −5.7 | −11.9% |
| UNH | 2026-01-27 | −16.4% | −6.7 | −3.4% |
| AVGO | 2025-09-05 | +16.2% | +5.3 | +3.0% |
| NFLX | 2025-01-22 | +14.8% | +5.2 | +6.0% |
| AVGO | 2026-06-04 | −14.7% | −4.0 | −1.8% |
| TSLA | 2024-10-24 | +14.5% | +3.8 | +14.0% |
| LLY | 2025-04-17 | +14.4% | +3.2 | −1.9% |
| TSLA | 2024-11-06 | +13.2% | +3.1 | +18.5% |
| AVGO | 2025-01-27 | −12.8% | −3.6 | +16.3% |

Take UNH on 2025-04-17. The prior close was 585.04 and the open 481.95: 481.95 / 585.04 − 1 = **−17.6%**. The prior day's ATR was 18.06 (585.04 − 481.95 = 103.09, and 103.09 / 18.06 = 5.7 ATRs). The system in lesson 12 was long UNH from 2025-04-09, a breakout in the post-correction rebound, with a stop 2 ATRs below entry. The gap took the stop out at the open for **−2.29R**: a trade sized to lose 1% of equity lost 2.3%. Ten sessions later UNH was another 11.9% lower, so the exit at the open was the right one; the point is that no stop placement could have made it a 1R loss.

Now the drift. Upward gaps of 5% or more with ten sessions of data afterwards: **72**, mean further move **+3.3%**, positive in 68% of cases. Downward gaps: **61**, mean further move **+1.4%**, lower in only 54% of cases. On this sample the upside drift is there and the downside drift is not. AVGO on 2025-01-27 gapped down 12.8% and was 16.3% higher ten days later. The literature's drift is an average over thousands of announcements sorted by the size of the earnings surprise, not by the size of the price gap, and this universe is twenty large, heavily-followed names over two years. Report both halves; a course that showed only the upside table would be selling you a story.

## Rules for a scheduled report

The report date is public. Companies announce it weeks ahead on their investor relations pages, and the report itself arrives as a Form 8-K on EDGAR. There is no excuse for being surprised by a scheduled event.

**Do not enter within three sessions before a report.** A breakout two days before earnings is a breakout that will be decided by a coin flip you cannot see. Wait for the report and trade the drift.

**If a report falls inside an open position, choose one of two things.** Exit at the close before the report, or cut the position to a size at which a 3-ATR gap against you costs no more than the 1% you planned. For a stock with a 3% ATR that means a position of 1% / (3 × 3%) = 11% of equity, roughly two thirds of the normal 2-ATR size. Holding full size through a report on the grounds that the trade is "working" is holding a 1% risk that has quietly become a 3% one.

**A tighter stop is not a defence.** The UNH gap was 5.7 ATRs. A stop at 1 ATR would have filled at the same open as a stop at 2.

**After an upward gap on a report, the pullback is the setup.** The gap defines a new range; a close back above the gap-day high after a two-to-five-session pause is the breakout trigger from lesson 5 with the information already in the price. TSLA's 2024-10-24 gap was followed by +14% over ten sessions and a further gap on 2024-11-06; the pause between them was the entry.

## Unscheduled news

Nobody scheduled UNH's second gap on 2026-01-27 or AVGO's on 2026-06-04. Unscheduled news is why the sizing rule in lesson 7 and the heat cap exist. You cannot avoid it; you can arrange that it costs a survivable amount. A book at 5% heat with a 1% risk per position, hit by a 3-ATR gap in one name, loses about 1.5% of equity. That is a bad day. A book at 20% heat with 4% positions hit by the same gap loses 6% on one headline, and two of those in a month is how a year's work disappears.

The last defence is the list itself. If a stock has gapped 5% or more four times in a year, it is telling you what kind of stock it is. Rank it, trade it, and size it as the gapper it has shown itself to be.

## Sources

- Ball, R. and Brown, P. (1968). An empirical evaluation of accounting income numbers. *Journal of Accounting Research*, 6(2), 159–178. https://doi.org/10.2307/2490232
- Bernard, V. L. and Thomas, J. K. (1989). Post-earnings-announcement drift: delayed price response or risk premium? *Journal of Accounting Research*, 27, 1–36. https://doi.org/10.2307/2491062
- U.S. Securities and Exchange Commission, Investor.gov glossary: Form 8-K. https://www.investor.gov/introduction-investing/investing-basics/glossary/form-8-k
- Yahoo Finance historical data, UNH: https://finance.yahoo.com/quote/UNH/history/
