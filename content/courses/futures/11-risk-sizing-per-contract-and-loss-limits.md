---
{
  "title": "Risk: Sizing per Contract, the Daily Loss Limit, and 2 a.m.",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A $25,000 account risks 1% per trade with a 20-point stop. How many ES contracts is that?", "opts": ["1", "2", "0; the risk of one contract ($1,000) is four times the budget", "5"], "correct": 2, "explain": "20 points x $50 = $1,000 per ES, against a $250 budget. The correct size is zero ES; in MES (20 x $5 = $100 each) it is two contracts."},
    {"q": "Can a $25,000 account hold one ES overnight when the CME initial margin is $27,526?", "opts": ["Yes, the maintenance level applies", "No; initial margin exceeds the entire account", "Yes, if the broker offers day-trading margin", "Only on Fridays"], "correct": 1, "explain": "Opening or carrying a position past the close requires the initial margin, and $27,526 is more than the account holds. Day-trading margin is intraday only."},
    {"q": "What is the purpose of a daily loss limit?", "opts": ["To satisfy the exchange", "To stop trading before a bad day becomes an account-changing day, at a point set in advance when you were not losing", "To increase position size after wins", "To guarantee profits"], "correct": 1, "explain": "The limit is a pre-commitment. Its value comes from having been set while calm; it is meaningless if it is revised at the moment it binds."},
    {"q": "A 2% adverse open at 7,772.50 costs how much on two ES?", "opts": ["$777.25", "$7,772.50", "$15,545.00", "$19,431.25"], "correct": 2, "explain": "155.45 points x $100 per point (two contracts) = $15,545, 62% of a $25,000 account, before any stop could act."},
    {"q": "Why is the 2 a.m. session more dangerous per contract than 10 a.m., if the point is $50 in both?", "opts": ["The multiplier doubles overnight", "Margin is higher overnight", "Depth is a small fraction of daytime depth, so the same order moves price more, stops slip further, and a normal daytime move is an outsized overnight one", "It is not; risk is identical"], "correct": 2, "explain": "The dollar per point is fixed; what changes is how many points a given flow moves the market and how far a stop slips. The 2 a.m. ET hour carried 0.8% of monthly volume against 16.2% at 10 a.m."}
  ],
  "task": "Write your per-trade risk in dollars, your daily loss limit in dollars, and the maximum MES and ES you may hold overnight given your current equity and today's CME initial margin; tape it to the monitor."
}
---

## Three numbers, decided before the trade

Every position in this course has been described by the same three quantities: how much the contract moves per point, how many points you are willing to be wrong by, and how much money you are willing to lose being wrong. Risk management is just making the third number a decision instead of an outcome.

**Dollars per point** is set by the exchange: $50 for ES, $5 for MES, $20 for NQ, $2 for MNQ. **Stop distance** in points is set by the trade: where the idea is proven wrong. **Risk per trade** in dollars is set by you, as a fraction of equity, before you look at the chart. The contract count follows:

contracts = risk per trade / (stop distance x dollars per point)

rounded *down*. If the answer is less than one for ES, the answer is zero ES, and you look at MES. If it is less than one for MES, the answer is no trade.

The common fraction is 0.5% to 1% of equity per trade. On $25,000 that is $125 to $250. Against a 20-point ES stop ($1,000) it is zero contracts; against a 20-point MES stop ($100) it is one or two. Traders who find these sizes insultingly small have not yet had the 2026-06-05 session (Lesson 4) happen to them.

## The margin constraint is separate, and it binds first

Sizing by risk tells you how many contracts you may hold. The exchange tells you how many you *can* hold, and for a small account the exchange is stricter than any risk rule at the moment you try to hold overnight.

CME's initial margin for ESZ26 was $27,526 (CME margins page figure, republished 2026-08-18). A $25,000 account cannot hold one ES past the close; it does not meet initial. In MES, at $2,753 per contract, the account could carry 9 (9 x $2,753 = $24,777), but doing so would leave $223 of free equity. Nine MES move $45 per point, so a 5-point move against you ($223 / $45 = 4.96 points) puts the account under initial, and maintenance on nine contracts is 9 x $2,502 = $22,518, a cushion of $2,482 or 55 points before a margin call. Margin capacity is not a size recommendation; it is a ceiling that the exchange thinks is safe for the exchange.

Intraday, brokers may extend day-trading margin of a few hundred dollars per ES. That changes the number of contracts the platform will let you buy at 10:00 a.m. It changes nothing about the $50 per point, and it is withdrawn, usually automatically, some minutes before the close, at which point the broker liquidates anything the exchange margin does not cover.

## The daily loss limit

Per-trade risk caps a single mistake. A daily loss limit caps a bad day: the sequence of three or four losses that each obeyed the rule, followed by the fifth that did not. A common setting is 2% to 3% of equity, $500 to $750 on $25,000, and the rule is absolute: when it is hit, all positions are flat and the platform is closed for the session. Many brokers and most prop-firm accounts enforce a daily limit mechanically; if yours does not, set it in the platform's risk settings, where it takes a deliberate act to override.

The limit works because it was set while you were not losing. Its whole value is that you do not get to renegotiate it at 2:47 p.m. after four losers.

## Why a point is $50, and why that matters at 2 a.m.

The multiplier is fixed by the spec; the market's behaviour is not. Three things change at night, and they multiply.

First, **depth**. From Lesson 7, the 2:00 a.m. ET hour carried 0.8% of monthly ES volume against 16.2% at 10:00 a.m., a 20-to-1 ratio, and the book is thinner in proportion. The flow that moves price one tick at 10:00 a.m. moves it several at 2:00 a.m.

Second, **gaps inside the session**. Overnight, price jumps across empty levels on a headline or an Asian-market print. A protective stop 20 points away fills 25 or 30 away, and $1,000 of intended risk on one ES becomes $1,250 or $1,500 without anything unusual happening.

Third, **you**. At 2:00 a.m. you are not at the screen, or you are and should not be. The position is being managed by resting orders whose failure modes (Lesson 10) are exactly the ones that thin markets trigger.

Put those together and "a point is $50" is the wrong sentence. The right one is that a normal overnight air pocket is five to ten points, $250 to $500 per ES, and it happens with no one on the other side of your stop.

## Worked example

Account $25,000. ESZ26 at 7,772.50 (Yahoo Finance close, 2026-09-23); multipliers $50 (ES) and $5 (MES); CME initial margin $27,526 (ES) and $2,753 (MES); 2% adverse open = 155.45 points; 5% adverse open = 388.625 points.

Step 1, risk per trade at 1%: $250.

Step 2, size for a 20-point stop. ES: $250 / (20 x $50) = 0.25, rounds to 0. MES: $250 / (20 x $5) = 2.5, rounds to 2. Two MES, risking $200 (0.8%).

Step 3, size for a 40-point stop (a wider, overnight-tolerant stop). MES: $250 / (40 x $5) = 1.25, rounds to 1. One MES, risking $200.

Step 4, margin check for overnight holding. Two MES require 2 x $2,753 = $5,506 initial, 22% of equity, fine. One ES requires $27,526, which is 110% of equity: not permitted.

Step 5, daily loss limit at 2%: $500. Two MES with a 20-point stop lose $200 per full stop-out; the limit allows two full losses and part of a third, then flat.

Step 6, the adverse-open stress, position by position, before any stop can act. Loss = adverse points x dollars per point.

- 1 MES: 2% = 155.45 x $5 = $777.25 (3.1% of equity); 5% = 388.625 x $5 = $1,943.13 (7.8%).
- 2 MES: 2% = $1,554.50 (6.2%); 5% = $3,886.25 (15.5%).
- 5 MES: 2% = $3,886.25 (15.5%); 5% = $9,715.63 (38.9%).
- 1 ES: 2% = $7,772.50 (31.1%); 5% = $19,431.25 (77.7%).
- 2 ES: 2% = $15,545.00 (62.2%); 5% = $38,862.50 (155% of equity, a deficit of $13,862.50).

The 2% figure is not hypothetical. The year to 2026-09-24 contained two daily closes worse than -2.6% (2025-10-10 and 2026-06-05) and an opening gap of -1.28% (2026-03-23). The 5% figure has not occurred in this data window; it occurred on multiple days in March 2020 and in October 2008, and the margin table exists because CME expects it to occur again.

Step 7, translate to 2 a.m. A two-MES position with a 20-point stop is $200 of intended risk. Add five points of overnight slippage: 25 x $10 = $250, the full per-trade budget. Add a 30-point air pocket on a headline: 50 x $10 = $500, the entire daily limit, from a position sized correctly by every rule above. The sizing was right; the hour was wrong. If you hold overnight, size for the overnight stop, which is wider, and accept fewer contracts.

![Bar chart of the dollar loss on a 2% adverse open of 155.45 points at 7,772.50 for five positions in a $25,000 account: 1 MES -$777, 2 MES -$1,555, 5 MES -$3,886, 1 ES -$7,773, 2 ES -$15,545. Price from Yahoo Finance ESZ26.CME close 2026-09-23; multipliers from the CME contract specifications.](figures/adverse-open-by-position.svg)

## Table

| Position | $ per point | Initial margin (CME, 2026-08-18 figure) | Can hold overnight on $25,000? | 20-pt stop risk | 2% adverse open | 5% adverse open |
|---|---|---|---|---|---|---|
| 1 MES | $5 | $2,753 | Yes | $100 | -$777.25 (3.1%) | -$1,943.13 (7.8%) |
| 2 MES | $10 | $5,506 | Yes | $200 | -$1,554.50 (6.2%) | -$3,886.25 (15.5%) |
| 5 MES | $25 | $13,765 | Yes | $500 | -$3,886.25 (15.5%) | -$9,715.63 (38.9%) |
| 9 MES | $45 | $24,777 | Barely ($223 free) | $900 | -$6,995.25 (28.0%) | -$17,488.13 (70.0%) |
| 1 ES | $50 | $27,526 | No | $1,000 | -$7,772.50 (31.1%) | -$19,431.25 (77.7%) |
| 2 ES | $100 | $55,052 | No | $2,000 | -$15,545.00 (62.2%) | -$38,862.50 (155%) |

## Sources

- CME Group, E-mini S&P 500 margins — https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.margins.html
- CME Group, Micro E-mini S&P 500 margins — https://www.cmegroup.com/markets/equities/sp/micro-e-mini-sandp-500.margins.html
- CME Group, Micro E-mini S&P 500 contract specifications — https://www.cmegroup.com/markets/equities/sp/micro-e-mini-sandp-500.contractSpecs.html
- CFTC, "Basics of Futures Trading" — https://www.cftc.gov/LearnAndProtect/EducationCenter/FuturesMarketBasics/index.htm
