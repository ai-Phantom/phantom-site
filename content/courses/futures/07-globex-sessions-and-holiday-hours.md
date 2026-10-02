---
{
  "title": "The Sessions: Globex Overnight, the RTH Open, the Close and Holidays",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Between 2026-08-24 and 2026-09-24, what share of ES volume traded in the 9 a.m. and 10 a.m. ET hours combined?", "opts": ["About 5%", "About 12%", "About 28%", "About 50%"], "correct": 2, "explain": "12.3% in the 9 o'clock hour plus 16.2% in the 10 o'clock hour = 28.5%, from Yahoo Finance 1-hour bars. The first hour after the 9:30 cash open is the densest of the day along with the last."},
    {"q": "Which hours, in Eastern time, carry the thinnest ES volume?", "opts": ["9 to 11 a.m.", "3 to 5 p.m.", "6 p.m. to 3 a.m.", "12 to 2 p.m."], "correct": 2, "explain": "Each hour from 6 p.m. to 3 a.m. ET carried under 1% of monthly volume. Europe's open around 3 to 4 a.m. ET lifts it to about 1.5%; the U.S. open is ten times that."},
    {"q": "The Globex trading day dated Tuesday 2026-09-22 began at:", "opts": ["9:30 a.m. ET Tuesday", "12:00 a.m. ET Tuesday", "6:00 p.m. ET Monday 2026-09-21", "5:00 p.m. ET Tuesday"], "correct": 2, "explain": "Equity index futures open at 6:00 p.m. ET the evening before. The session's date is the date of its settlement, not of its first trade."},
    {"q": "What happens to ES on the NYSE early-close day after Thanksgiving, 2026-11-27?", "opts": ["Normal hours", "CME halts equity index futures early, around midday CT, and reopens for the next session at the usual evening time", "Futures are closed all day", "Only the micros trade"], "correct": 1, "explain": "CME abbreviates equity index sessions on NYSE early-close and some holiday dates; the exact halt time is published on the CME holiday calendar about two weeks ahead."},
    {"q": "On Labor Day, Monday 2026-09-07, the Yahoo Finance ES=F daily series has no bar. Why?", "opts": ["ES never trades on Mondays", "The exchange was closed for the entire day including the evening", "There was no daily settlement because the session was a holiday halt, and Globex reopened for the Tuesday session that evening", "Data outage"], "correct": 2, "explain": "On U.S. holidays CME typically halts equity index trading around midday CT with no settlement, then opens the next trading day at 5:00 p.m. CT. A session with no settlement produces no daily bar."}
  ],
  "task": "Print the CME holiday calendar for the next quarter, mark every date with an early halt or no settlement, and note the NYSE early closes of 2026-11-27 and 2026-12-24 next to them."
}
---

## A 23-hour market with a two-hour heart

ES trades from 6:00 p.m. ET Sunday to 5:00 p.m. ET Friday, with a maintenance break from 5:00 to 6:00 p.m. ET each weekday. That is 23 hours a day. But the volume is not spread over those 23 hours. Almost all of it happens between the New York cash open at 9:30 a.m. and the cash close at 4:00 p.m. ET, and within that window it piles up at the two ends. The rest of the day is a different market: thinner, slower, prone to sharp air pockets, and driven by other regions' news.

Knowing the clock is not a trading edge; it is a safety requirement. The same order that fills at one tick of slippage at 10:15 a.m. can fill three ticks away at 2:15 a.m., and the same 30-point move that is ordinary at the open is an event overnight.

## The three sessions

**Globex overnight (6:00 p.m. to about 4:00 a.m. ET).** The Asian session. ES tracks Tokyo, Hong Kong and Sydney equities, the yen and Treasury futures, plus any U.S. after-hours earnings. Volume per hour is 0.1% to 0.8% of the day's total. The book is real but shallow; a few hundred contracts can move price several ticks. The U.S. session's settlement has already happened, so your overnight P&L is being marked against tomorrow's settlement, and the margin call from a bad overnight move arrives in the morning.

**European session (about 3:00 a.m. to 9:30 a.m. ET).** Frankfurt and London open around 3:00 a.m. ET; volume steps up to about 1.5% per hour. The 8:30 a.m. ET U.S. economic releases (payrolls, CPI, GDP) land in this window and can produce the largest single-minute moves of the day, in a book that is still a fraction of what it will be an hour later. The 8 o'clock hour carries roughly 3% of daily volume, twice the hour before it.

**Regular trading hours, RTH (9:30 a.m. to 4:00 p.m. ET).** The cash stock market is open, index arbitrage is active, and every institutional flow that needs to reference the index is here. The first hour is the densest: 12.3% of monthly volume in the 9 o'clock hour (which contains only thirty minutes of RTH) and 16.2% in the 10 o'clock hour. Volume sags through lunch to about 7.5% at 1 p.m., then climbs into the close. The 3 o'clock hour matches the morning peak at 16.2%, driven by the 4:00 p.m. cash close, the market-on-close imbalance, and the ES settlement window. The 4 o'clock hour, after the cash close, still holds 3.4%, mostly hedging against the closing prints, before the 5:00 p.m. maintenance break.

## The open and the close, specifically

The 9:30 a.m. ET open is when overnight information gets priced against real depth. The first five-minute bar of RTH on 2026-09-22 traded 31,930 contracts against 6,598 in the bar before it (Yahoo Finance 5-minute data), a fivefold jump in one bar. Spreads are one tick but the queue at each level is short and turns over fast. The classic mistake is to treat a pre-open price as a reliable reference; it is a thin estimate.

The 4:00 p.m. ET close is the settlement event. The CME settlement price for ES is derived from trading around 3:00 p.m. CT; this is the number your variation margin will be calculated against (Lesson 4). Volume in the final five minutes before 4:00 p.m. on 2026-09-22 was 79,783 contracts, the largest bar of the day. Between 4:00 and 5:00 p.m. ET the book thins fast: the 4:30 bar traded 982 contracts, one-eightieth of the 3:55 bar.

## Holidays

CME does not simply close on U.S. holidays. It publishes a holiday calendar, usually finalised about two weeks ahead, with three possible treatments for equity index futures: a full session, an early halt (typically around midday CT, with no daily settlement or with a settlement at the halt), or a closed day. On several holidays Globex opens the evening before as usual, halts around midday, and reopens that evening for the next session.

The dates you need for 2026 come from the NYSE calendar, because CME's equity index hours follow the cash market: New Year's Day (Thu 2026-01-01), Martin Luther King Jr. Day (Mon 01-19), Washington's Birthday (Mon 02-16), Good Friday (Fri 04-03), Memorial Day (Mon 05-25), Juneteenth (Fri 06-19), Independence Day observed (Fri 07-03), Labor Day (Mon 09-07), Thanksgiving (Thu 11-26) and Christmas (Fri 12-25). NYSE early closes at 1:00 p.m. ET fall on Fri 2026-11-27 and Thu 2026-12-24; CME abbreviates the ES session on those days too. Confirm each on the CME calendar; the halt times move from year to year.

Two things to expect on holiday sessions. Volume is a small fraction of normal, so any order larger than a few contracts should be worked as a limit. And an early halt with no settlement means your position carries two nights of risk against one mark, with the margin call arriving after the reopen.

## Worked example

Take the full Globex day dated Tuesday 2026-09-22, from 6:00 p.m. ET on Monday 2026-09-21 to 5:00 p.m. ET on Tuesday, using Yahoo Finance 5-minute bars for ES=F (the front contract, ESZ26). Total volume across the day: 1,258,983 contracts. Split it into sessions:

- Globex overnight, 6:00 p.m. to 4:00 a.m. ET: 85,520 contracts, 6.8% of the day, over ten hours. Average 8,552 per hour.
- Europe to the cash open, 4:00 a.m. to 9:30 a.m.: 188,306 contracts, 15.0%, over five and a half hours. Average 34,237 per hour.
- RTH first hour, 9:30 to 10:30 a.m.: 214,934 contracts, 17.1%, in one hour.
- Midday, 10:30 a.m. to 3:00 p.m.: 512,190 contracts, 40.7%, over four and a half hours. Average 113,820 per hour.
- Last hour, 3:00 to 4:00 p.m.: 220,655 contracts, 17.5%, in one hour.
- After the cash close, 4:00 to 5:00 p.m.: 37,378 contracts, 3.0%.

The first and last RTH hours together carried 34.6% of the day in two hours, 17.3% per hour. The overnight ten hours carried 6.8% in total, 0.68% per hour. The ratio is 25 to 1. A 2 a.m. trade is being done in a market with one twenty-fifth of the participation of a 10 a.m. trade, and Lesson 11 shows what that does to the dollar value of a point.

Cross-check with the month: Yahoo Finance 1-hour bars for ES=F from 2026-08-24 to 2026-09-24 total 30,409,043 contracts. The 9 a.m., 10 a.m., 11 a.m. and 3 p.m. hours took 12.3%, 16.2%, 12.5% and 16.2%, or 57.2% of the month in four hours. The seven hours from 6 p.m. to 1 a.m. took 3.3% combined.

## Chart

![Bar chart of the share of ES volume by hour of day in Eastern time from 2026-08-24 to 2026-09-24, from Yahoo Finance 1-hour bars for ES=F: under 1% per hour from 6 p.m. to 3 a.m., rising to 12.3% at 9 a.m., 16.2% at 10 a.m., dipping to 7.5% at 1 p.m., and 16.2% at 3 p.m., with regular-trading-hours bars highlighted.](figures/es-volume-by-hour.svg)

The chart is the monthly aggregate; the day-by-session split above is one specific day, and the two agree on the shape: two peaks at the open and the close, a lunchtime trough, and an overnight that barely registers.

## Sources

- CME Group, E-mini S&P 500 contract specifications (trading hours) — https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.contractSpecs.html
- CME Group, holiday calendar and trading hours — https://www.cmegroup.com/trading-hours.html
- NYSE Group, 2026, 2027 and 2028 Holiday and Early Closings Calendar (press release, 2025-12-23) — https://s2.q4cdn.com/154085107/files/doc_news/NYSE-Group-Announces-2026-2027-and-2028-Holiday-and-Early-Closings-Calendar-2025.pdf
