---
{
  "title": "What an Event Is to a Market",
  "duration": "15 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "Which of these is a scheduled event in the sense this course uses?", "opts": ["A CEO resignation announced at 7 a.m.", "An FDA rejection letter", "The BLS Employment Situation release at 8:30 a.m. on a published date", "A short-seller report posted at noon"], "correct": 2, "explain": "Scheduled events have a date and time published in advance by the source, so the market can price the uncertainty before it resolves. The other three arrive without warning and cannot be priced ahead of time."},
    {"q": "NVIDIA released its second-quarter fiscal 2027 results on August 26, 2026. When did the first tradable reaction occur?", "opts": ["At the 9:30 a.m. open on August 27", "During the 5 p.m. conference call", "In the after-hours session on August 26, minutes after the 4 p.m. close", "At the 8:30 a.m. pre-market on August 27"], "correct": 2, "explain": "NVIDIA releases after the close; the stock traded 203.50 to 226.25 in extended hours on August 26 before the regular session ever opened."},
    {"q": "Why does the course tell you to take event dates from the primary source rather than a free screener?", "opts": ["Screeners are illegal to use for trading", "Screeners estimate dates from past patterns and can be wrong by days or a week", "Primary sources publish the consensus estimate", "Screeners only cover S&P 500 names"], "correct": 1, "explain": "Most earnings screeners project dates from prior-year cadence until the company confirms; a projected date is a guess. The company's IR page, the Fed's calendar and the BLS schedule are the record."},
    {"q": "An index inclusion is announced Thursday after the close, effective before Tuesday's open. On which close do index funds actually have to buy?", "opts": ["Thursday", "Friday", "Monday", "Tuesday"], "correct": 2, "explain": "'Effective prior to the open on Tuesday' means the index changes overnight Monday to Tuesday, so funds that track the index trade the Monday close. Reddit's August 2026 inclusion followed exactly this pattern."},
    {"q": "What is the defining feature of an event for a trader, as this lesson frames it?", "opts": ["It always produces a large price move", "Uncertainty resolves at a known moment, so the price of that uncertainty can be observed beforehand", "It is only relevant to options traders", "It happens after hours"], "correct": 1, "explain": "An event compresses information arrival into a moment. Because the moment is known, option prices before it carry a measurable price for the uncertainty, which is what the rest of the course works with."}
  ],
  "task": "Build a one-page list of every scheduled event that touches your three most-traded names in the next 30 days, each with its source URL, date and release time in your local time zone."
}
---

## An event is a moment when information arrives all at once

Most of the time a stock's price drifts on a trickle of information: an analyst note, a supplier comment, a macro print somewhere in the world. An event is different. It is a moment when a large block of information that the market has been waiting for lands in a single instant, and the price has to absorb it immediately. For a company that is quarterly earnings. For the whole market it is the Federal Reserve's rate decision, the Consumer Price Index, or the monthly jobs report.

What makes an event tradeable is not the size of the move. It is that the *timing* of the move is known in advance. When you know that uncertainty will resolve at 4:20 p.m. on a Wednesday, you can observe what the market is willing to pay to be protected from, or exposed to, that resolution. That price lives in the option chain, and you already know how to read a chain from the options course. This course is about what to do with it around a date.

Two ideas carry through every lesson. First, the market prices events before they happen, and that price can be compared to what actually happened afterward. Second, the *reaction* to an event is a separate object from the event itself: a beat can fall, a miss can rally, and the first print of the tape is frequently reversed within the hour. You will spend most of this course learning to separate what was expected, what happened, and what the price did.

## Scheduled versus unscheduled

A **scheduled** event has a date and a time published in advance by its source. The Fed publishes the year's FOMC meeting dates in advance on its website; the statement is released at 2:00 p.m. Eastern on the second day of each meeting. The Bureau of Labor Statistics publishes a release schedule for CPI and the Employment Situation, both at 8:30 a.m. Eastern. Companies announce their earnings date and call time by press release, typically two to four weeks before the report.

An **unscheduled** event arrives without warning: a guidance cut on a Tuesday morning, a regulatory action, a data breach, a merger leak, a CEO departure. You cannot position for it in advance because there is nothing in the chain that prices it, beyond the general level of implied volatility. This course is about scheduled events only. Unscheduled events are a risk-management topic, covered in lesson 10 under gap risk, not a trading topic.

The scheduled events that matter for a U.S. equity or index trader fall into six groups:

- **Earnings reports.** Quarterly, dated by company press release. Most large companies report either before the open (roughly 6:00 to 8:00 a.m. Eastern) or after the close (4:01 to 4:30 p.m.). NVIDIA reports after the close with a call at 5:00 p.m. Eastern.
- **FOMC decisions.** Eight per year. Statement at 2:00 p.m. Eastern, press conference at 2:30 p.m. Four of the eight include the Summary of Economic Projections (the dot plot).
- **CPI.** Monthly, 8:30 a.m. Eastern, roughly the second week of the month.
- **Employment Situation (NFP).** Monthly, 8:30 a.m. Eastern, usually the first Friday.
- **Index rebalances and inclusions.** S&P 500 changes are announced by press release, usually after the close, and become effective before the open of a stated date. The Russell reconstitution takes effect after the close of a published Friday.
- **Product launches and company events.** Apple's September event, an analyst day, an FDA decision date (PDUFA). These have a date but often not a precise minute.

## Why the calendar source matters

Free screeners project earnings dates from the prior year's cadence until the company confirms. A projected date can be off by a week. If you put on an earnings straddle a week early, you paid a week of theta for nothing, and if you sold premium a week late, you sold *into* the report rather than after it. The reliable sources are:

- The company's investor relations page ("NVIDIA Sets Conference Call for Third-Quarter Financial Results" is a press release, and its date is the date).
- The SEC's EDGAR system, where the 8-K with the results is filed within minutes of the release.
- The Federal Reserve's FOMC calendar page.
- The BLS release schedule pages for CPI and the Employment Situation.
- S&P Dow Jones Indices press releases and FTSE Russell's reconstitution schedule.

Exchange calendars (NYSE, Nasdaq) give you market holidays and early closes, which change when "after the close" is: on a half day the close is 1:00 p.m.

## The anatomy of a single event

Take NVIDIA's report of August 26, 2026, which you will use throughout the course. The company announced results for its second quarter of fiscal 2027 after the 4:00 p.m. close, with the conference call at 5:00 p.m. Eastern. The regular session had closed at 209.66. The stock had already been trading in extended hours before the release, and the first minutes after it were violent: the 4:20 p.m. five-minute bar printed a low of 203.50, nearly 3% below the close, then the 5:20 p.m. bar printed a high of 226.25, nearly 8% above it. By the 9:30 a.m. open on August 27 the price was 222.86, a gap of 6.30% over the prior close, and the day closed at 227.98, up 8.74%.

Notice the four distinct prices in that story: the close before, the after-hours prints, the next open, and the next close. Each is a different answer to "how did the stock react," and each is used by a different kind of trader. Option sellers care about the close-to-close move against the expiry. Gap traders care about the open. The extended-hours prints are where most of the information arrived and where almost nobody could trade in size.

## Worked example

Count the scheduled events an NVDA trader faced in the 30 days around that report, and note the timing of each, using only primary calendars.

- **August 7, 2026, 8:30 a.m. ET:** Employment Situation for July (BLS schedule).
- **August 12, 2026, 8:30 a.m. ET:** CPI for July (BLS schedule).
- **August 13, 2026, after the close:** S&P Dow Jones Indices announced Reddit would replace AvalonBay Communities in the S&P 500 effective prior to the open on August 18. Not an NVDA event, but it moved a name many NVDA traders also hold.
- **August 26, 2026, after 4:00 p.m. ET:** NVIDIA Q2 FY2027 results; call 5:00 p.m. ET.
- **September 4, 2026, 8:30 a.m. ET:** Employment Situation for August.
- **September 11, 2026, 8:30 a.m. ET:** CPI for August.
- **September 15–16, 2026:** FOMC meeting; statement 2:00 p.m. ET on the 16th, press conference 2:30 p.m., with projections.

Seven scheduled moments in 30 trading days, four of them macro releases that move the whole tape. Now compute the reaction to the one company event, from the daily bars (Yahoo Finance chart API, daily interval, 496 rows from 2024-10-01 to 2026-09-23):

- Close before, August 26: 209.66
- Open after, August 27: 222.86. Gap = 222.86 / 209.66 − 1 = 1.0630 − 1 = **+6.30%**
- Close after, August 27: 227.98. Close-to-close = 227.98 / 209.66 − 1 = 1.0874 − 1 = **+8.74%**
- Intraday range on August 27: high 230.47, low 220.90. Range = (230.47 − 220.90) / 222.86 = 9.57 / 222.86 = **4.29%** of the open.
- Volume: 298.9 million shares on August 27 versus 179.9 million on August 26, a ratio of 1.66.

The gap captured 72% of the close-to-close move (6.30 / 8.74). That ratio, how much of the reaction is already in the open, is one of the numbers you will log in the event journal in lesson 11. When it is near 1, the open was the whole story and there was nothing left for a day trader; when it is well below 1, the day continued the move; when it is negative, the open reversed.

## Table

| Event | Source | Typical time (ET) | Who publishes the date |
|---|---|---|---|
| Earnings | Company press release, EDGAR 8-K | Pre-market ~6–8 a.m. or post-close 4:01–4:30 p.m. | The company, 2–4 weeks ahead |
| FOMC | Federal Reserve | Statement 2:00 p.m., press conference 2:30 p.m. | Fed, a year ahead |
| CPI | BLS | 8:30 a.m. | BLS, a year ahead |
| Employment Situation | BLS | 8:30 a.m. | BLS, a year ahead |
| S&P 500 change | S&P Dow Jones Indices | Announced after close; effective prior to a stated open | S&P DJI, usually 3–5 trading days ahead |
| Russell reconstitution | FTSE Russell | Effective after the close of a stated Friday | FTSE Russell, months ahead |
| Product launch / PDUFA | Company or FDA | Varies; often no fixed minute | Company or agency |

## What this course assumes and what it will not do

You should already be comfortable with delta, implied volatility, and vertical spreads from the options course; when this course says "the ATM straddle" or "vega" it will not stop to define them. It will teach you how to read an implied move, how implied has compared to realised in the academic record, why option premium collapses after an event, what the FOMC and BLS days actually look like minute by minute, what index inclusion does and no longer does, and how to size and journal event trades so that after a year you can say whether you have any edge at all.

It will not tell you that any of these structures makes money. The evidence, which you will read directly, is mixed and regime-dependent, and costs eat a large share of whatever is there. The point of the journal in lesson 11 is that your own record is the only evidence that applies to you.

## Sources

- Federal Reserve, FOMC Meeting calendars and information: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- Bureau of Labor Statistics, Consumer Price Index release schedule: https://www.bls.gov/schedule/news_release/cpi.htm and Employment Situation schedule: https://www.bls.gov/schedule/news_release/empsit.htm
- NVIDIA, "NVIDIA Announces Financial Results for Second Quarter Fiscal 2027," August 26, 2026: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- S&P Dow Jones Indices, "Reddit Set to Join S&P 500," August 13, 2026: https://press.spglobal.com/2026-08-13-Reddit-Set-to-Join-S-P-500-and-Sun-Communities-to-Join-S-P-MidCap-400
