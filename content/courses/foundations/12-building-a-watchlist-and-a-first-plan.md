---
{
  "title": "Building a Watchlist and a First Plan",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "With a 10,000 dollar account and a 1 percent risk rule, you buy a stock at 62.26 with a stop at 58.52. The largest position the rule allows is:", "opts": ["100 shares", "26 shares", "160 shares", "16 shares"], "correct": 1, "explain": "Risk per share is 62.26 minus 58.52, or 3.74 dollars. The 100 dollar risk budget divided by 3.74 is 26.7, rounded down to 26 shares."},
    {"q": "Why does the sizing rule start from the stop distance rather than from a fixed dollar amount per position?", "opts": ["Because brokers require it", "Because it makes every position carry the same loss if the stop is hit, regardless of the stock's price or volatility", "Because it maximises returns", "Because stops are always hit"], "correct": 1, "explain": "A wider stop means fewer shares; a tighter stop means more. The dollar loss at the stop is constant, so no single trade can do disproportionate damage."},
    {"q": "Which of these is the weakest reason to add a stock to a watchlist?", "opts": ["It trades more than a million shares a day with a tight spread", "It is in a sector you do not already own", "A friend said it was going to double", "Its next earnings date is known and you have read its last 10-Q"], "correct": 2, "explain": "A watchlist is a research queue. Liquidity, diversification and having done the reading are criteria; a tip is not."},
    {"q": "A written trade plan must contain an exit rule for both:", "opts": ["The broker and the exchange", "A loss (the stop) and a gain or a time limit (the target or review date)", "Dividends and buybacks", "Pre-market and after-hours"], "correct": 1, "explain": "Deciding in advance where you are wrong and where you are done is what separates a plan from a hope. Both sides must be written before entry."},
    {"q": "What is the purpose of paper trading a plan before funding it?", "opts": ["To prove the strategy is profitable", "To find execution and process errors, such as wrong order types or unrealistic fills, at no cost", "To satisfy the pattern day trader rule", "To generate tax losses"], "correct": 1, "explain": "A few weeks of paper trading cannot prove a strategy works, but it reliably exposes mechanical mistakes before they cost money."}
  ],
  "task": "Build a watchlist of eight to twelve stocks that meet the liquidity and size filters in this lesson, and write a complete one-paragraph plan for one of them using the template."
}
---

## A watchlist is a research queue, not a shopping list

Beginners build watchlists by adding whatever they hear about. The result is 60 tickers, no criteria, and a screen full of red and green that produces impulse trades. A useful watchlist is small, filtered, and annotated: each name is there for a stated reason, with the numbers that reason depends on, and it stays only as long as the reason holds.

This lesson gives you the filters, the columns, and then the second half of the job: turning one watchlist name into a written plan with a position size and an exit rule. The capstone that follows asks you to do it three times.

## Filters: what gets on the list

Apply these in order. A stock that fails any one does not go on.

1. **Liquidity.** Average daily volume above one million shares and a bid-ask spread under 10 basis points of price during regular hours (Lesson 2). Below this, your own orders move the price and every round trip costs real money.
2. **Size.** Market capitalisation above 2 billion dollars (Lesson 4). This removes most of the manipulation, most of the delisting risk, and most of the companies with no analyst coverage to check your reading against.
3. **Filings you have opened.** You have read at least the MD&A of the most recent 10-Q or 10-K (Lesson 6). Not the summary on a finance site; the filing. If you have not, the stock is a candidate, not a watchlist member.
4. **A reason.** One sentence: why this company, why now. "Services revenue growing 13 percent with margins expanding" is a reason. "It went up a lot" is not. "It went down a lot" is not either.
5. **Sector spread.** No more than three names from any one GICS sector. A list of eight semiconductor companies is one idea eight times.

Eight to fifteen names is enough. If the list grows beyond twenty, cut it.

## Columns: what to record

For each name, keep the following, updated when the numbers change rather than daily:

- Ticker, company, GICS sector, market cap bucket
- Price on the date you added it, and the date
- Average daily volume and typical spread in basis points
- Trailing P/E, P/S, dividend yield (Lessons 7 and 8)
- Next earnings date
- Your one-sentence reason
- The price at which you would act, and the price at which the reason is wrong

The last line is the bridge to the plan. If you cannot fill it in, you do not yet have a view; you have an interest.

## The plan: six lines before any order

A plan is written before the entry, and it has six components. Missing any one of them means the trade is not planned.

**1. Thesis.** Two or three sentences: what you expect to happen to the business, and why the price does not already reflect it. Include the number that would prove you wrong.

**2. Entry.** The price and order type (Lesson 3). A limit order at a stated price, or a stop-buy above a stated level, with a time-in-force. Not "around here".

**3. Stop.** The price at which the thesis is invalidated, or at which the loss exceeds what you are willing to accept, whichever comes first. This is where you are wrong. Write it down. It is a sell stop order (or a mental level you will act on without exception, if you have reasons not to place the order in the market).

**4. Size.** Derived from the stop, not chosen independently. See the next section.

**5. Exit for a gain, or a time limit.** A target price at which the thesis has played out, or a date by which you will reassess regardless of price. Many good plans have both: "sell half at the target, reassess the rest at the next earnings report."

**6. Review date.** When you will reread the thesis against new information: usually the next earnings date. If the thesis has broken but the stop has not been hit, the review is what gets you out.

## Position sizing: the 1 percent rule

Decide the maximum amount you are prepared to lose on one trade if the stop is hit. One percent of the account is the conventional starting point for beginners; some use half a percent, few professionals use more than two. Then:

Shares = (account size × risk percentage) ÷ (entry price − stop price)

Round down. The position value (shares × entry) is an output, not an input. A stock with a wide stop gets a small position; a stock with a tight stop gets a larger one; the dollar loss at the stop is the same for both.

Two guardrails on top:

- **Position cap.** No single position larger than a stated share of the account, commonly 10 to 20 percent, regardless of what the sizing formula allows. A tight stop on a 500-dollar stock can produce a position larger than is sensible.
- **Total open risk.** The sum of (shares × distance to stop) across all open positions, as a percentage of the account. Cap it at something like 5 percent. This limits the damage from a day when everything falls together, which is the day stops all get hit at once.

> **Callout:** A stop limits the loss from an orderly decline. It does not limit the loss from a gap (Lesson 3). Sizing at 1 percent means a gap that opens twice as far below your stop as you planned costs 2 percent, which is survivable. Sizing at 10 percent means the same gap costs 20 percent.

## Before real money: paper, then small

Run the plan in a paper-trading account for at least a few weeks. The point is not to prove the strategy works; a few weeks of results are noise. The point is to catch mechanical errors: a stop placed on the wrong side, a Day order that expired, a fill assumption that was unrealistic in a thin stock. Then start with real money at a size where a full loss at the stop is an amount you would not mention to anyone. Increase only after a written review of at least ten completed trades.

Keep a journal. For each trade: the plan as written before entry, what happened, and one sentence on what you would change. The journal, not the P&L, is where the learning is.

## Table

The watchlist as it looked on 31 December 2024 for three names used throughout this course, with the plan columns filled in. Financial data from each company's most recent annual report at that date; prices are official closes.

| Column | AAPL | MSFT | KO |
| --- | --- | --- | --- |
| Sector | Information Technology | Information Technology | Consumer Staples |
| Market cap | 3.79 trillion | 3.13 trillion | 268 billion |
| Price at close, 31 Dec 2024 | 250.42 | 421.50 | 62.26 |
| Typical spread | 1 cent (0.4 bp) | 1 to 2 cents (0.4 bp) | 1 cent (1.6 bp) |
| Trailing P/E (reported EPS) | 41 | 36 | 25 |
| Dividend yield | 0.4 percent | 0.8 percent | 3.1 percent |
| Next earnings date | 30 January 2025 | 29 January 2025 | 11 February 2025 |
| Stop (6 percent below close) | 235.39 | 396.21 | 58.52 |
| Risk per share | 15.03 | 25.29 | 3.74 |

Two Information Technology names is within the three-per-sector limit; a third would fill it.

## Worked example

Account: 10,000 dollars. Risk per trade: 1 percent, or 100 dollars. Position cap: 20 percent, or 2,000 dollars. Total open risk cap: 5 percent, or 500 dollars. Entries at the 31 December 2024 closes; stops 6 percent below, a round figure chosen for illustration rather than from each stock's volatility.

**AAPL.** Entry 250.42, stop 235.39, risk per share 15.03. Shares: 100 ÷ 15.03 = 6.65, rounded down to 6. Position: 6 × 250.42 = 1,502.52 dollars. Loss at stop: 6 × 15.03 = 90.18 dollars.

**MSFT.** Entry 421.50, stop 396.21, risk per share 25.29. Shares: 100 ÷ 25.29 = 3.95, rounded down to 3. Position: 3 × 421.50 = 1,264.50 dollars. Loss at stop: 75.87 dollars.

**KO.** Entry 62.26, stop 58.52, risk per share 3.74. Shares: 100 ÷ 3.74 = 26.7, rounded down to 26. Position: 26 × 62.26 = 1,618.76 dollars. Loss at stop: 97.24 dollars.

**Totals.** Capital deployed: 4,385.78 dollars, 44 percent of the account, with 5,614 dollars in cash. Every position is under the 2,000 dollar cap. Total open risk: 90.18 + 75.87 + 97.24 = 263.29 dollars, or 2.6 percent of the account, well inside the 5 percent cap. If every stop is hit in an orderly market, the account is down 2.6 percent. If every stock gaps to double the stop distance, it is down about 5.3 percent. Either way the account survives to make the next decision, which is the entire purpose of the exercise.

**One full plan, for KO.** Thesis: Coca-Cola grows revenue in the mid single digits with a 79 percent payout ratio and a 3.1 percent yield; the position is an income holding, and the thesis is wrong if the company cuts the dividend or organic revenue growth turns negative for two consecutive quarters. Entry: limit buy 26 shares at 62.26, good-till-cancelled. Stop: sell stop at 58.52. Size: 26 shares, 1,618.76 dollars, 97.24 dollars at risk. Exit: reassess at 70.00 (a 12 percent gain, roughly two years of dividends plus growth); otherwise hold through the next two earnings reports. Review date: 11 February 2025, the fourth-quarter report.

Six lines. Every number traceable to a filing, a quote or a rule. That is a plan.

## Sources

- SEC Office of Investor Education, "Introduction to Investing" (research and planning basics): https://www.investor.gov/introduction-investing
- FINRA, "Asset Allocation and Diversification": https://www.finra.org/investors/investing/investing-basics/asset-allocation-diversification
- SEC, EDGAR Full-Text Search (for locating the filings behind each watchlist entry): https://www.sec.gov/edgar/search/
- SEC Office of Investor Education, "Day Trading" investor bulletin (risk of frequent trading without a plan): https://www.investor.gov/introduction-investing/investing-basics/glossary/day-trading
