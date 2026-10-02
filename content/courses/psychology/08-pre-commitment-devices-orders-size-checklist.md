---
{
  "title": "Pre-Commitment Devices: Orders, Fixed Size and the Checklist",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "In Haynes and colleagues' 2009 study, introducing a 19-item surgical safety checklist in eight hospitals changed the in-hospital death rate from:", "opts": ["1.5% to 0.8%", "10% to 5%", "0.8% to 1.5%", "It did not change"], "correct": 0, "explain": "Deaths fell from 1.5% to 0.8% and major complications from 11.0% to 7.0% across 3,733 patients before and 3,955 after. The checklist added no skill; it made existing skill reliable."},
    {"q": "Degani and Wiener's 1993 study of cockpit checklists concluded that a checklist's main function is:", "opts": ["To teach pilots to fly", "To provide a redundant, standardised verification of configuration so that memory lapses and interruptions do not become omissions", "To satisfy regulators", "To slow the crew down"], "correct": 1, "explain": "The checklist is a defence against the known failure modes of expert memory under workload, not a substitute for expertise. The same failure modes apply at 09:31."},
    {"q": "Ariely and Wertenbroch (2002) found that students who set their own binding deadlines:", "opts": ["Performed worse than students with no deadlines", "Performed better than students with no deadlines, but not as well as those given evenly spaced external deadlines", "Performed identically", "Refused to set them"], "correct": 1, "explain": "People will voluntarily bind themselves, and it helps; but self-set binds were less effective than externally imposed ones, which is why the orders should be at the broker, not in your head."},
    {"q": "A plan risks 1% of $20,000 with entry $50.00 and stop $48.50 (133 shares). Mid-trade the trader moves the stop to $47.00. Risk on the position is now:", "opts": ["$200, unchanged", "$266", "$399, about 2% of the account", "$600"], "correct": 2, "explain": "133 x (50.00 - 47.00) = $399. The plan's 1% became 2% by a single click with no change to the size rule, which is why the stop is not moved away from entry."},
    {"q": "Which of these is a pre-commitment device in the sense of this lesson?", "opts": ["Deciding to be disciplined", "A bracket order that submits the stop and target with the entry", "Reading about psychology", "Watching the P&L closely"], "correct": 1, "explain": "A device changes what is possible or costly at the moment of temptation. A bracket order makes the exit exist before the temptation does."}
  ],
  "task": "Configure a bracket order template at your broker with the stop and target legs as good-till-cancelled, and place your next trade through it and nothing else."
}
---

## Devices, not decisions

A pre-commitment device is something that changes what is possible, or what it costs, at the moment a decision would otherwise be made. Ulysses tied to the mast is the classic image; a bracket order at a broker is the trading equivalent, and it has the advantage of being free. This lesson covers the three devices that convert lesson 7's plan into something the doer executes rather than interprets: the orders, the size rule, and the checklist. The evidence for the checklist comes from surgery and aviation, because those are the fields that tested it.

## The evidence for checklists

Atul Gawande led a World Health Organization study, published by Haynes and colleagues in the New England Journal of Medicine in 2009, that introduced a 19-item surgical safety checklist in eight hospitals in eight cities, from Toronto and London to Ifakara in Tanzania. The items were things every surgical team already knew to do: confirm the patient's identity, confirm the site, confirm antibiotics were given, count the sponges. The study compared 3,733 patients before the checklist with 3,955 after.

The death rate fell from 1.5% to 0.8%. The rate of major in-hospital complications fell from 11.0% to 7.0%. The effect was present in both high-income and low-income sites. Nothing about the teams' skill changed. What changed was that steps everyone knew were now verified rather than remembered, and the specific failure mode of expertise under workload, the omission of a known step, was blocked.

Aviation got there first. Asaf Degani and Earl Wiener's 1993 paper in Human Factors, written for NASA, analysed how cockpit checklists work and fail. Their conclusion was that the checklist's job is redundant verification of aircraft configuration against a standard, and that its enemies are interruption, time pressure, the crew's confidence that they have already done the item, and poorly designed lists that are too long or ambiguous to be used under load. Every one of those enemies has a trading equivalent. A trader at 09:31 is interrupted, pressured, confident, and, if the plan is a paragraph rather than a list, unable to check it.

The transfer to trading is direct because the failure mode is the same. The stop is not omitted because the trader does not know to place it. It is omitted because the entry filled, the price moved, a second setup appeared, and the item was never verified. A five-line checklist, read aloud, is the cheapest defence in this course.

## The evidence that people will bind themselves

Dan Ariely and Klaus Wertenbroch (2002) tested whether people voluntarily pre-commit and whether it helps. Students in one class were given a free choice of deadlines for three papers, with a penalty for lateness; most chose to bind themselves with deadlines spaced through the term rather than putting all three at the end, and their grades were better than a no-deadline group's. But a third group, given evenly spaced deadlines by the instructor, did better still. People will tie themselves to the mast; they do not tie the knots as tightly as an outside party would.

For a trader, the outside party is the broker's order system. A stop that exists as a resting order is enforced by a machine that does not care about your thesis. A stop that exists in a plan document is enforced by you, at the moment when lessons 3 and 6 say you are least reliable. Both are pre-commitment; only one is Ariely and Wertenbroch's external deadline.

## Device one: orders placed with the entry

The bracket order, available at most US brokers, submits three legs together: the entry, a stop leg and a target leg, with the two exit legs linked so that filling one cancels the other. It is the mechanical form of lesson 2's rule. Its details matter:

Time in force on the exit legs must be good-till-cancelled, not day. A day-order stop expires at the close, and an overnight position with an expired stop is an unprotected position that looks protected. The bracket exists before the entry fills, so there is no interval in which the position is open and the stop is a decision. And the legs are modified only in the direction of less risk: a stop may move toward the entry, a target may move toward the entry, and nothing moves away.

For a plan with a time stop, the bracket does not cover the 15:55 exit; that one remains a checklist item, and the checklist below has it.

## Device two: size fixed by a rule computed before the open

Lesson 7 gave the formula: shares = floor(risk dollars / per-share risk), with risk dollars = 1% of prior-day closing equity. Two features make it a device rather than a guideline. The equity input is yesterday's close, so today's P&L cannot feed back into today's size; the trader who is up 2R at 11:00 cannot "press" and the trader who is down 2R cannot "recover". And the per-share risk is the planned stop distance, so the only way to take a bigger position is to plan a tighter stop, which the setup definition constrains.

The device fails in one specific way, which the worked example shows: a stop moved away from entry after the fill changes the dollar risk without touching the size rule. The rule against moving the stop is therefore part of the sizing device, not a separate discipline.

## Device three: the checklist

Degani and Wiener's design rules: short, unambiguous, ordered as the work is ordered, read aloud, with a challenge-response form where possible. Here is a pre-trade list built to those rules, for lesson 7's plan.

Before the open, once: prior-day equity written down; risk dollars computed; loss limit and maximum trades written down; bracket template loaded; alarm set for 15:55.

Before each order, aloud: setup condition observed on the chart, yes or no; time before 11:30, yes or no; trades today fewer than the maximum, yes or no; realised P&L above the loss limit, yes or no; per-share risk computed; shares computed; bracket ticket shows entry, stop and target with GTC on the exits. Any "no" ends the sequence.

After each exit, once: the trade logged with the lesson 9 fields; rule followed, yes or no, and if no, what deviated.

Seven items before an order is the right length. Degani and Wiener found long lists get skimmed; the surgical list was 19 items across three phases, and each phase was short.

## Worked example

Take the sizing device and show how a single un-bracketed action defeats it, with full arithmetic.

Account $20,000, risk 1% = $200 per trade. Entry $50.00, planned stop $48.50, per-share risk $1.50. Shares = floor(200 / 1.50) = 133. Dollar risk = 133 x 1.50 = $199.50, or 0.9975% of the account. Target at 2R = 50.00 + 2 x 1.50 = $53.00.

Bracketed: entry 133 at market, stop-market 133 at 48.50 GTC, limit 133 at 53.00 GTC. Outcomes: stop hit, -$199.50 = -1R; target hit, +133 x 3.00 = +$399 = +2R. At a 40% win rate the expectancy is 0.40 x 399 - 0.60 x 199.50 = 159.60 - 119.70 = +$39.90 per trade, +0.20R.

Un-bracketed, stop as a mental level: the price reaches $48.60 and the trader, with a $186 paper loss on screen, moves the stop to $47.00 "below the day's low". Risk is now 133 x (50.00 - 47.00) = $399, which is 2.0% of the account, and the plan's ratio has become 1:1 at the same win rate: expectancy = 0.40 x 399 - 0.60 x 399 = -$79.80 per trade, -0.40R of the original R. The size rule was never touched; it computed 133 shares correctly. The device that failed was the absence of the resting order.

Now the checklist's contribution. Suppose the trader omits the stop leg one time in twenty when placing brackets manually (a rate that is not unusual under time pressure), and that on those occasions the position behaves like the un-bracketed case. Over 200 trades a year, 10 are unprotected. If each costs the difference between the two expectancies, 39.90 - (-79.80) = $119.70, the omissions cost $1,197 a year on a $20,000 account, about 6%. A bracket template that cannot be submitted without both legs takes the omission rate to zero. That is what Haynes's 1.5% to 0.8% looks like at the scale of one account.

## Table

| Device | Moment it acts | What it makes impossible or costly | Failure mode to check |
|---|---|---|---|
| Bracket order, GTC exits | Before the entry fills | Holding a position with no stop; deciding the exit with a loss on screen | Day time-in-force on the exit legs; legs moved away from entry |
| Size from prior-day equity | Before the open | Pressing after wins; recovering after losses; size by feel | Stop moved after the fill, which changes risk without changing shares |
| Pre-order checklist, read aloud | Before each order | Omitting the stop; trading past the loss limit or trade cap; trading outside the setup's hours | List too long; items skipped because "I already know" |
| Post-exit log within 30 minutes | After each exit | Forgetting the deviation; reconstructing the trade from memory | Logged from memory the next day |
| Daily loss limit with physical exit | When the limit is hit | Continuing to trade on tilt | Limit renegotiated at the moment it is hit |

## What devices cannot do

A device makes a specific failure impossible or expensive. It does not make a setup profitable, and it does not remove the trader's ability to abandon the devices; you can always cancel the bracket. What the devices do is move the act of abandonment from a silent omission to a visible action that the checklist and the journal will record. Haynes's teams could still skip the count; the checklist made skipping it a thing someone had to say out loud. That is the standard: every deviation from the plan should require a positive act that leaves a mark. The journal, next lesson, is where the marks are counted.

## Sources

- Alex B. Haynes, Thomas G. Weiser, William R. Berry, Atul A. Gawande and others, "A Surgical Safety Checklist to Reduce Morbidity and Mortality in a Global Population", New England Journal of Medicine 360, 2009: https://doi.org/10.1056/NEJMsa0810119
- Asaf Degani and Earl L. Wiener, "Cockpit Checklists: Concepts, Design, and Use", Human Factors 35(2), 1993: https://doi.org/10.1177/001872089303500209
- Dan Ariely and Klaus Wertenbroch, "Procrastination, Deadlines, and Performance: Self-Control by Precommitment", Psychological Science 13(3), 2002: https://doi.org/10.1111/1467-9280.00441
