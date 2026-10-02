---
{
  "title": "The Technology: Data Feeds, Latency, Hotkeys, and Paper Trading First",
  "duration": "14 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "For the 60 reference entries, the average absolute gap between the signal bar's close and the next bar's open was:", "opts": ["$0.001", "$0.014", "$0.08", "$0.25"], "correct": 1, "explain": "Mean absolute gap $0.014, mean signed gap +$0.001, maximum $0.08. On a $2.18 average R that is 0.6%."},
    {"q": "Budish, Cramton and Shim argue that the latency arms race is:", "opts": ["A benefit to all traders", "A consequence of continuous-time trading that a frequent batch auction would remove, and that transfers wealth to the fastest", "Irrelevant to equity markets", "Required by regulation"], "correct": 1, "explain": "Their analysis shows the race is a design flaw of continuous limit-order books; a retail trader cannot win it and should not enter it."},
    {"q": "Why does a 5-minute-bar strategy not need a low-latency feed?", "opts": ["Because bars are never revised", "Because the decision is made once per bar at a known time, and a delay of a second changes the fill by a fraction of a cent on average", "Because SPY is illiquid", "It does need one"], "correct": 1, "explain": "The decision cadence is 300 seconds; a one-second delay is 0.3% of it. The measured slippage confirms the cost is small."},
    {"q": "What is the main purpose of a hotkey for this course's playbook?", "opts": ["To enter faster than market makers", "To place the entry, stop and target as one bracket order with a pre-computed share count, so that the plan is executed as written", "To scalp", "To cancel orders"], "correct": 1, "explain": "The value is in removing manual steps where the plan gets edited, not in speed."},
    {"q": "The reason to paper trade the playbook for 30 sessions before funding it is:", "opts": ["To learn the platform only", "To produce the first 30 rows of the journal and a measured expectancy before real money is exposed to a rule of unknown sign", "Paper trading is more profitable", "Brokers require it"], "correct": 1, "explain": "Paper results overstate fills slightly, but they establish whether the rule and your execution of it are close to the test in lesson 3."}
  ],
  "task": "Configure a bracket order template in your platform's paper account with entry, stop and target fields, and place one using tomorrow's opening-range numbers."
}
---

## What the technology has to do

For the playbook in this course the technology has four jobs: deliver 5-minute bars that agree with the market's, let you place an entry with an attached stop and target without editing anything by hand, record every fill, and stay out of the way. Nothing in the reference rule requires speed, depth-of-book data, a co-located server or a second monitor. This lesson says what you need, measures what latency actually costs a bar-based rule, and explains why the arms race you read about is not your race.

## Data feeds

Three tiers exist. Consolidated real-time top-of-book and trades from the SIP (the securities information processors that Regulation NMS created) is what brokers show by default; it is sufficient for everything here. Direct exchange feeds and full-depth books (Nasdaq TotalView and the like) are sold to firms that need microseconds and queue positions; lesson 6 explained why they do not change a bar-based decision. Delayed or unofficial data, which includes free web APIs such as the Yahoo Finance endpoint this course's tests were built from, is fine for research and for building your log after the fact, and unfit for placing live orders because it can lag, revise or drop bars.

Be specific about what your bars are. The 5-minute bars used in this course are regular-session only, timestamped at the bar's open, with the 16:00 print excluded. A platform that includes pre-market volume in the 09:30 bar, or that builds bars on a different clock, will give you a different opening range on some days. Before the capstone, compare your platform's 09:30 to 09:45 high and low against a second source for three sessions; if they disagree by more than a cent or two, find out why.

## Latency, measured

A bar-based rule makes its decision at a known moment (the close of a 5-minute bar) and acts at the next opportunity (the open of the next bar). The cost of that delay is the difference between the two prices, and it is measurable on the 60 reference trades.

## Worked example

For each of the 60 reference entries (2026-06-30 to 2026-09-23, SPY 5-minute bars, Yahoo Finance), take the signal bar's close and the next bar's open, signed in the direction of the trade (positive when the open was worse for the trader).

- Mean signed gap: +$0.001 per share (the open was, on average, a tenth of a cent worse than the signal close).
- Median signed gap: $0.000.
- Mean absolute gap: $0.014 per share.
- Largest absolute gap: $0.08 per share.

On a 50-share position (lesson 7's sizing on a $30,000 account) the average gap is 50 × 0.014 = $0.70 and the worst is $4.00, against an average risk per trade of about $148. As a share of R: 0.014 / 2.18 = 0.6% on average, 0.08 / 2.18 = 3.7% at worst.

Now suppose your feed is one second late and your order takes another second to arrive. You are acting two seconds into a 300-second bar. If price moved uniformly through the bar, the expected cost of those two seconds is 2/300 of the average bar range: 0.0067 × $0.50 = $0.003 per share. Even at the open, with a $0.94 median bar range, it is $0.006. The measured bar-to-bar gap above already dwarfs it. For this playbook, a two-second delay is not a cost you can measure in a 60-trade sample.

Compare a scalper targeting $0.20. The same two seconds at the open is $0.006 of an $0.20 target, 3%, before the spread. Their decisions happen many times a minute, so the delay compounds across every decision. Latency matters exactly in proportion to how often you decide and how little you are trying to capture.

## Why the arms race is not yours

Budish, Cramton and Shim showed that continuous limit-order-book markets create a race to be first when public information arrives, that the race rewards speed rather than information, and that its winners collect from everyone who is slower. That includes every retail trader, always. You cannot buy your way into the race: the participants have measured their advantages in microseconds and paid for exchange colocation, microwave links and hardware you cannot rent. What you can do is stop competing on the dimension they win on. A rule that decides once per bar has taken itself out of the race by design; the measured cost above is what it pays for that.

## Hotkeys and bracket orders

The one piece of technology this course insists on is a bracket order: an entry with a stop and a target attached, submitted as a unit. Its value is not speed. It is that the plan you wrote before 09:30 (entry level, stop at the range edge, target at 1R, shares from the stop) is what gets sent, with no step in between where a hand can edit a number. Every deviation in lesson 10's "rule followed" column starts with a manual step.

Set the template up so that you enter three numbers: entry, stop, target. Compute shares from the stop outside the platform (a one-line spreadsheet: risk dollars divided by entry minus stop, rounded down) and enter the count. Check that the stop is a stop-market, not a stop-limit, unless you have thought about what happens to a stop-limit on a fast move through the level and decided you want that. Check that the time-in-force is "day" and that the bracket cancels its other leg on a fill. Place one on the paper account and watch it execute before the first live one.

Hotkeys beyond that (buy 100 at market, flatten, reverse) belong to scalping and to the discretionary habit of doing something because the button is there. The playbook has one entry and three exits, and the bracket handles all four.

## Table

What each component needs to do for this course's playbook, and what it does not.

| Component | Needed | Not needed | Reason |
|---|---|---|---|
| Market data | Consolidated real-time top of book and trades; regular-session 5-minute bars | Direct exchange feeds, full depth, sub-second timestamps | Decisions happen once per bar; measured bar-to-bar slippage is 0.6% of R |
| Charting | 5-minute bars with a session VWAP; ability to draw two horizontal lines | Indicator packages | The setup uses the range and VWAP only |
| Order entry | Bracket (entry + stop + target), stop-market, day time-in-force | One-click market buttons, reverse, scale hotkeys | Removes hand edits from the plan |
| Connection | Ordinary broadband; a phone as backup to flatten | Colocation, dedicated lines | Two seconds of latency costs a fraction of a cent |
| Records | Fill-level export of every order with timestamps | Screen recording | Journal fields in lesson 10 come from fills |
| Research data | Free 5-minute bars (Yahoo chart API or equivalent) for tests and journal back-fill | Paid tick data | The 60-session tests in this course ran on the free source |

## Paper trading first, and its limits

Trade the playbook in a paper account for the full 30-session capstone before funding it. The purpose is not to learn the buttons, though that happens. It is to produce the first 30 rows of the journal and a measured expectancy before real money is exposed to a rule whose sign the 60-session test could not establish.

Paper fills flatter you. Simulated brackets fill at the touch, where a live stop-market can fill through the level and a live limit target can be touched and not filled; the difference is usually a cent or two on SPY, and lesson 5's arithmetic tells you whether that matters for your R. Paper trading also removes the part of the experiment that the Brazilian and Taiwanese studies suggest matters most, the behaviour under loss. Treat the 30 paper sessions as a test of the rule and of your execution mechanics, and the first 30 funded sessions at the smallest size (lesson 7's 0.25% row) as the test of you.

## Sources

- Eric Budish, Peter Cramton and John Shim, "The High-Frequency Trading Arms Race: Frequent Batch Auctions as a Market Design Response," Quarterly Journal of Economics 130(4), 2015: https://doi.org/10.1093/qje/qjv027
- U.S. Securities and Exchange Commission, Regulation NMS, Release No. 34-51808 (consolidated market data and order protection): https://www.sec.gov/rules/final/34-51808.pdf
- Nasdaq, TotalView product documentation (what a full-depth direct feed contains): https://www.nasdaq.com/solutions/nasdaq-totalview
- Yahoo Finance chart API, SPY 5-minute bars used for the slippage measurement: https://finance.yahoo.com/quote/SPY/history/
