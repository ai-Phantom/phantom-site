---
{
  "title": "What Day Trading Is, the Rule That Replaced PDT, and the Base Rates",
  "duration": "16 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "Under FINRA Regulatory Notice 26-10, what happened to the $25,000 pattern-day-trader minimum equity requirement?", "opts": ["It was raised to $50,000", "It was eliminated and replaced by an intraday margin standard, effective June 4, 2026", "It was extended to cash accounts", "It now applies only to options"], "correct": 1, "explain": "The notice replaces the day-trade count, the pattern-day-trader designation and the $25,000 minimum with an intraday margin deficit standard; firms may phase in until October 20, 2027."},
    {"q": "In Chague, De-Losso and Giovannetti's Brazilian study, what share of individuals who day traded for at least 300 days lost money?", "opts": ["About 50%", "About 75%", "97%", "12%"], "correct": 2, "explain": "97% of the persistent day traders lost money, and only 0.4% earned more than a bank teller's wage."},
    {"q": "Barber, Lee, Liu and Odean found that profitable day traders in Taiwan made up roughly what share of all day traders in an average year?", "opts": ["1.6%", "16%", "40%", "60%"], "correct": 0, "explain": "Only about 1.6% were profitable in the average year, and 80% of day traders quit within two years."},
    {"q": "Our 60-session SPY opening-range test earned $0.25 per share per trade with a standard error of $0.27. What does that tell you?", "opts": ["The rule is proven profitable", "The 95% confidence interval includes zero, so the sample cannot distinguish the rule from a coin flip", "The rule loses money", "The standard error is irrelevant for trading"], "correct": 1, "explain": "Mean minus and plus 1.96 standard errors spans -$0.27 to +$0.77; a result that straddles zero is not evidence of an edge."},
    {"q": "Why does a day trader's ledger look worse than a buy-and-hold investor's before any skill is considered?", "opts": ["Day traders pay higher taxes on losses", "Each round trip pays the spread and slippage, and a day trader makes hundreds of round trips a year", "Brokers charge day traders a monthly fee", "Intraday prices are more predictable"], "correct": 1, "explain": "Costs are paid per round trip. Frequency multiplies them, so the hurdle a day trader must clear grows with every trade."}
  ],
  "task": "Write down, in dollars, the most you are willing to lose learning this skill over the next six months, and put that number at the top of your trading journal before opening a platform."
}
---

## What the job actually is

Day trading means opening and closing a position inside one regular session, so you go home flat. Nothing about the label says how many trades you take: a day trader might place one opening-range trade at 09:50 and be finished by 11:00, or scalp dozens of times. What the label does say is that every position pays its round-trip costs the same day, and that your results are determined by many small decisions rather than a handful of large ones.

This course teaches one instrument (SPY, the S&P 500 ETF), one family of setups (the opening range, VWAP pullbacks and short scalps) and one discipline (measuring your own expectancy after costs). It does not promise that any of this makes money. The final lesson asks you to prove, on your own log, whether it does for you.

## The rule that governed day trading, and what replaced it

For a quarter of a century FINRA Rule 4210 defined a "pattern day trader" as a margin customer who made four or more day trades in five business days, provided those trades were more than 6% of the account's total trades in the window. Once flagged, the account had to hold at least $25,000 in equity, and it received day-trading buying power of four times its maintenance margin excess. Fall below $25,000 and the account was restricted to closing trades until it was topped up.

That framework is gone. FINRA Regulatory Notice 26-10, published April 20, 2026, adopted amendments to Rule 4210 that eliminate the day-trade count, the pattern-day-trader designation and the $25,000 minimum, replacing them with an intraday margin standard. Under the new standard, on any day a customer's transactions reduce intraday maintenance margin, the firm must calculate an intraday margin deficit and require it to be met as promptly as possible. The amendments took effect June 4, 2026, with an 18-month phase-in that ends October 20, 2027, so your broker may still be operating under the old count-based system while it migrates.

Two things follow. First, the $25,000 barrier no longer decides who can day trade, which means more small accounts will try. Second, nothing about the change alters the economics below. The regulator's own investor publication, "Day Trading: Your Dollars at Risk," still says that day traders "typically suffer severe financial losses in their first months of trading, and many never graduate to profit-making status." The rule was a speed bump, not the reason people lose.

## What the published studies say

Two large academic studies used complete records rather than survey answers, and both counted every trader, not just the ones who kept going.

Chague, De-Losso and Giovannetti observed every individual who started day trading Brazilian equity index futures between 2013 and 2015 and kept at it for at least 300 sessions. Of those persistent traders, 97% lost money. Only 0.4% earned more than a bank teller's wage, about US$54 a day, and the single best performer made about US$310 a day with a daily standard deviation of US$2,560. The authors found no evidence that performance improved with experience.

Barber, Lee, Liu and Odean studied the full Taiwan Stock Exchange record from 1992 to 2006, a market where day trading was a fifth of all volume. Profitable day traders made up about 1.6% of all day traders in an average year. About 80% quit within two years, and after three years only 13% were still trading. The ones who quit were disproportionately the ones losing, which means the survivors you see on social media are a filtered sample.

A skeptic can argue that these samples are from other countries and other decades. The reply is that costs, not geography, drive the result. Every round trip pays the bid-ask spread and any slippage, and a day trader makes hundreds of round trips a year. Before any skill is considered, the ledger starts with a hole the size of the trading frequency times the cost per trade. Lesson 5 quantifies that hole.

## What our own test can and cannot say

Throughout this course the worked examples come from one dataset: SPY 5-minute bars for 60 regular sessions, 2026-06-30 to 2026-09-23, pulled from Yahoo Finance's chart API on 2026-09-24. Lesson 3 tests a simple 15-minute opening-range breakout on it, and that test earned money over the 60 sessions. It is important to see now, before you like the rule, how little that proves.

## Worked example

The rule (details in lesson 3) took exactly one trade per session, 60 trades in total, with a fixed $0.02 per share round-trip cost. The per-trade results after costs were:

- 35 winning trades, average +$1.83 per share
- 25 losing trades, average −$1.96 per share
- Total: 35 × 1.8303 + 25 × (−1.9624) = 64.06 − 49.06 = +$15.00 per share

Mean per trade = 15.00 / 60 = +$0.250 per share.

The standard deviation of per-trade P&L was $2.073, so the standard error of the mean is 2.073 / √60 = 2.073 / 7.746 = $0.268.

A 95% confidence interval is mean ± 1.96 × standard error = 0.250 ± 0.525, which runs from −$0.27 to +$0.77 per share. The interval contains zero. The t-statistic is 0.250 / 0.268 = 0.93, well below the 2.0 that would usually be asked for before calling something a real effect.

Measured in R (profit divided by the dollars risked on that trade), the mean was +0.156R with a standard error of 0.119R, t = 1.31. Same conclusion.

Scale it to a real account: 100 shares per trade is $1,500 over 60 sessions, or $25 a session. The confidence interval on that is −$1,650 to +$4,650. A result that could plausibly have been a $1,650 loss is not a business plan.

## Table

Base rates from the two complete-record studies, alongside the test you will replicate in the capstone.

| Source | Market and period | Who was counted | Result |
|---|---|---|---|
| Chague, De-Losso, Giovannetti (2020) | Brazil, index futures, 2013–2015 starters | Everyone who persisted 300+ days | 97% lost money; 0.4% beat a bank teller's wage |
| Barber, Lee, Liu, Odean (2014) | Taiwan, all equities, 1992–2006 | Every day trader, every year | ~1.6% profitable in an average year; 80% quit within 2 years |
| SEC, "Day Trading: Your Dollars at Risk" | US, investor publication | Regulator's summary | "Severe financial losses in their first months"; many never become profitable |
| This course, lesson 3 test | SPY 5-min bars, 60 sessions to 2026-09-23 | One rule, one trade per day | +$0.25/share/trade, 95% CI −$0.27 to +$0.77 |

## How to use the rest of this course

Read every setup in the following lessons as a hypothesis. The session-structure lesson tells you when volume and range exist. The opening-range and VWAP lessons define setups precisely enough to test. The scalping lesson shows why costs, not entries, decide whether short-horizon trading can work at all. The risk, stops and journaling lessons give you the arithmetic that keeps a losing streak from ending the experiment. The technology lesson tells you what you need and what you do not. The playbook lesson and the capstone put it together into a 30-session log that you grade against a rubric.

If, after 30 logged sessions, your expectancy after costs is not distinguishable from zero, the correct response is not to add indicators. It is to either extend the sample or stop. The studies above were mostly written about people who did neither.

## Sources

- FINRA, Regulatory Notice 26-10, "FINRA Adopts New Intraday Margin Standards to Replace the Day Trading Margin Requirements" (April 20, 2026): https://www.finra.org/rules-guidance/notices/26-10
- U.S. Securities and Exchange Commission, "Day Trading: Your Dollars at Risk": https://www.sec.gov/investor/pubs/daytips.htm
- Fernando Chague, Rodrigo De-Losso and Bruno Giovannetti, "Day Trading for a Living?" (2020), SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3423101
- Brad Barber, Yi-Tsung Lee, Yu-Jane Liu and Terrance Odean, "Do Day Traders Rationally Learn About Their Ability?" (2014): https://faculty.haas.berkeley.edu/odean/papers/Day%20Traders/Day%20Trading%20and%20Learning%20110217.pdf
