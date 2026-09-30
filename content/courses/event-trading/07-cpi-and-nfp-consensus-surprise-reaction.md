---
{
  "title": "CPI and NFP: Consensus, Surprise, Reaction",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "When are CPI and the Employment Situation released?", "opts": ["9:30 a.m. ET, when the market opens", "8:30 a.m. ET, an hour before the regular session opens", "2:00 p.m. ET", "After the close"], "correct": 1, "explain": "Both BLS releases are published at 8:30 a.m. Eastern, so the first reaction happens in the pre-market, in futures and in extended-hours ETF trading, before most retail traders can act at normal spreads."},
    {"q": "The August 2026 jobs report showed +162,000 payrolls against a Dow Jones consensus of +53,000, and SPY fell. Which reading is correct?", "opts": ["The data was bad for the economy", "A large positive surprise on growth raised the expected path of interest rates, which is negative for equity valuations; 'beat' does not mean 'bullish'", "The consensus was wrong so the market ignored it", "Payrolls do not move stocks"], "correct": 1, "explain": "With the Fed leaning toward hikes in 2026, stronger employment meant a higher probability of tighter policy. The equity reaction to a macro surprise depends on what the surprise implies for rates, not on whether the number is 'good.'"},
    {"q": "The surprise that matters for a macro print is measured as:", "opts": ["Actual minus the previous month", "Actual minus the consensus forecast recorded before the release", "Actual minus the Fed's target", "The headline number alone"], "correct": 1, "explain": "Markets price the consensus in advance. Only the deviation from consensus is new information at 8:30. The prior month's number was already known and priced."},
    {"q": "On September 11, 2026 core CPI printed +0.3% against +0.2% expected. SPY dipped in the 8:30 bar and closed the day up 0.85%. What does this illustrate?", "opts": ["Hot inflation is bullish", "The first reaction to a print and the day's close are different objects; other information, and the headline being in line, dominated a small core miss", "The BLS revised the number", "The market was closed"], "correct": 1, "explain": "The knee-jerk reaction lasted one five-minute bar. By 9:00 the ETF was above its pre-release level. A trader who acted on the first print alone was on the wrong side of the day."},
    {"q": "Why does the course recommend recording the consensus yourself, before the release, rather than looking it up afterward?", "opts": ["Consensus numbers are secret", "Post-release write-ups quote whichever consensus fits the story; the pre-release figure you logged is the one you actually traded against", "The BLS deletes it", "It is faster"], "correct": 1, "explain": "Consensus varies by survey (Dow Jones, Bloomberg, Reuters). After the fact, coverage may cite the one that makes the print look more or less surprising. Your journal needs the figure you had at 8:29."}
  ],
  "task": "Before the next CPI release, write down the headline and core consensus from one named survey, then log the 8:30 SPY bar's open, high, low and close, the 9:30 open and the day's close."
}
---

## Two prints that set the tone for the month

The Consumer Price Index and the Employment Situation are the two monthly releases that most reliably move the whole market, because they are the two inputs the Federal Reserve talks about most. Both come from the Bureau of Labor Statistics. Both are released at 8:30 a.m. Eastern on dates published a year in advance on the BLS schedule pages. The jobs report is usually the first Friday of the month; CPI is usually the second week. Both are released while the regular session is closed, so the first reaction is in stock index futures, in Treasury futures, and in the pre-market trading of ETFs like SPY.

The mechanics of trading them come down to three numbers: what the market expected, what printed, and what the difference implies for interest rates. That last step is where most new event traders go wrong, because "good" economic news is often bad for stocks and the sign flips depending on what the Fed is worried about that quarter.

## Consensus and surprise

Markets do not react to the level of a number; they react to its deviation from what was already priced. The **consensus** is the median forecast from a survey of economists, compiled by Dow Jones, Bloomberg, Reuters and others in the days before the release. The **surprise** is actual minus consensus. Everything else, the prior month's figure, the year-over-year rate, was known before 8:30 and is already in the price.

Three details matter in practice:

- **Which consensus.** Surveys differ by a tenth on CPI and by tens of thousands on payrolls. Record the one you used, by name, before the release. After the fact, commentary will cite whichever consensus makes the print look most dramatic.
- **Which line.** CPI has a headline and a core (ex food and energy) figure, each month-over-month and year-over-year. The jobs report has the payroll change, the unemployment rate, average hourly earnings, and revisions to the prior two months. The market can react to a different line than the one in the headline, and often does: a core CPI miss with an in-line headline, or a payroll beat with a large downward revision.
- **The direction of the mapping.** In a regime where the Fed is fighting inflation, a hot CPI or strong payroll number raises expected rates and tends to hurt equities. In a regime where the Fed is worried about growth, a weak jobs number can hurt equities directly. The same print has the opposite sign in the two regimes. The regime is the thing to know before 8:30, and the FOMC's most recent statement tells you which one you are in.

## What moves on a beat versus a miss

For CPI, a hotter-than-expected core print pushes Treasury yields up and equities down within seconds, with the size of the move roughly proportional to the surprise in tenths. A cooler print does the reverse. For payrolls the mapping runs through the same channel but with more moving parts: a big beat with weak wage growth can be read as "growth without inflation" and rally stocks; a beat with hot earnings growth can sell them off.

What you should expect at 8:30 is a one-to-three-minute burst of activity in futures, a pre-market ETF move that is frequently retraced or extended by 9:30, and a regular session whose close is only loosely related to the first print. The worked example shows both a retracement and a continuation, on two prints eleven days apart.

## Worked example

Both examples use SPY 5-minute bars from the Yahoo Finance chart API with pre-market included (187 bars for September 11, 189 for September 4; pre-market bars carry no volume in this feed) and the BLS releases themselves.

**Employment Situation for August 2026, released Friday, September 4, 2026, 8:30 a.m. ET.** Nonfarm payrolls +162,000. Unemployment rate 4.1%, unchanged. June revised up 11,000 to +31,000; July revised up 44,000 to +21,000. Average hourly earnings +0.3% on the month. The Dow Jones consensus, as reported the day before, was **+53,000**. Surprise: 162,000 − 53,000 = **+109,000**, roughly double the expectation.

- 8:25 bar close (pre-market): **773.56**.
- 8:30 bar: open 774.01, high 774.10, low **770.50**, close 771.55. First-bar move from 8:25: 771.55 / 773.56 − 1 = **−0.26%**; to the bar's low, −0.40%.
- 8:45 bar: low 770.90, a second test of the low, then 771.26.
- 9:30 regular-session open: **772.01**. From the 8:25 level: −0.20%. Prior day's close (September 3): 773.17.
- Day's close: **770.19**. Day: 770.19 / 773.17 − 1 = **−0.39%**.

A very strong jobs number and the market fell, modestly, and stayed down. In September 2026 the FOMC was twelve days from a hike; a payroll beat of that size raised the odds of it. This is the "beat is bearish" case.

**CPI for August 2026, released Friday, September 11, 2026, 8:30 a.m. ET.** Headline CPI-U +0.4% month over month, seasonally adjusted, and +3.4% over twelve months. Core +0.3% on the month, +2.4% over twelve months. The BLS noted gasoline rose 3.9% and accounted for over a third of the monthly increase. Consensus: headline +0.4% (in line), core **+0.2%** (surprise +0.1), year-over-year figures in line.

- 8:25 bar close: **763.50** (it had risen from 762.22 at 8:00).
- 8:30 bar: open 763.24, low **760.39**, close 762.61. First-bar move: 762.61 / 763.50 − 1 = **−0.12%**; to the low, −0.41%.
- 8:50 bar: 765.04. By 9:00: **765.93**, +0.32% above the 8:25 level. The dip had fully reversed within thirty minutes.
- 9:30 open: 764.72. Prior close (September 10): 757.83, so the pre-market session as a whole had the ETF up 0.91%.
- Day's close: **764.29**. Day: 764.29 / 757.83 − 1 = **+0.85%**.

A core miss of one tenth, an in-line headline dominated by gasoline, and a knee-jerk dip that lasted one bar. The rest of the pre-market and the day went the other way. Anyone who sold the 8:30 low on "hot core" was wrong within twenty minutes.

## Table

| Release | Date / time (ET) | Line | Consensus | Actual | Surprise | 8:30 bar (from 8:25 close) | Day (close to close) |
|---|---|---|---|---|---|---|---|
| Employment Situation, Aug 2026 | Sep 4, 8:30 a.m. | Nonfarm payrolls | +53,000 (Dow Jones) | +162,000 | +109,000 | −0.26% (low −0.40%) | −0.39% |
| CPI, Aug 2026 | Sep 11, 8:30 a.m. | Core m/m | +0.2% | +0.3% | +0.1 pt | −0.12% (low −0.41%) | +0.85% |
| CPI, Aug 2026 | Sep 11, 8:30 a.m. | Headline m/m | +0.4% | +0.4% | 0 | | |

## What you can do with this

You cannot trade the 8:30 bar. The regular session is closed, the pre-market ETF spread is wide, and the futures move is over before a retail order routes. What you can do is decide, before 8:30, what you will do at 9:30 under each outcome, and then let the first hour tell you which outcome you are in. The CPI example is the reason: the tradeable information at 9:00 was not "core was hot" but "the market has already rejected the hot-core reaction." That was visible, and it was visible with half an hour to spare.

Three rules for the journal, which lesson 11 formalises:

1. Log the consensus, by survey name, the night before. Not after.
2. Log the 8:30 bar's low or high as the "first reaction," separately from the 9:30 open and the close. The gap between the first reaction and the close is the number that tells you whether the market is trading the print or something else.
3. Log the regime, in one line, from the most recent FOMC statement ("inflation remains elevated" versus "risks to employment have risen"). The same surprise maps to opposite reactions across regimes, and without that column you will average across them and see nothing.

The Savor–Wilson result from lesson 6 applies here too: announcement days as a class have carried a higher average return than non-announcement days, which they read as a premium for bearing the announcement's risk. That is a reason to be less quick to flatten *into* a print if you were long anyway, and it is not a reason to buy the morning of one.

## Sources

- Bureau of Labor Statistics, "The Employment Situation — August 2026," released September 4, 2026: https://www.bls.gov/news.release/empsit.nr0.htm and release schedule: https://www.bls.gov/schedule/news_release/empsit.htm
- Bureau of Labor Statistics, "Consumer Price Index — August 2026," released September 11, 2026: https://www.bls.gov/news.release/cpi.nr0.htm and release schedule: https://www.bls.gov/schedule/news_release/cpi.htm
- Savor, P., and Wilson, M. (2013). "How Much Do Investors Care About Macroeconomic Risk? Evidence from Scheduled Economic Announcements." Journal of Financial and Quantitative Analysis 48(2), 343–375. https://doi.org/10.1017/S002210901300015X
- Federal Reserve, FOMC statement of September 16, 2026 (the regime reference for both prints): https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm
