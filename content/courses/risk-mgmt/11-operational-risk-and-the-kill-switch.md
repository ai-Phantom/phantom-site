---
{
  "title": "Operational Risk: Brokers, Fat Fingers, Keys and the Kill Switch",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "On 2012-08-01, Knight Capital's trading system sent orders for about 45 minutes that produced over 4 million executions in 154 stocks and a loss the SEC put at more than $460 million. What was the root cause the SEC's order identified?", "opts": ["A software deployment that left old, dormant order-routing code active on one of eight servers, with no pre-trade controls that could stop the resulting order flow", "A market crash", "A rogue trader", "A hacked API key"], "correct": 0, "explain": "The order found that Knight had no adequate controls to prevent the entry of erroneous orders and no kill switch that staff knew how to use. The trades were all individually valid; the process that generated them was broken. That is what operational risk looks like."},
    {"q": "$460 million over 45 minutes is roughly", "opts": ["$1 million a minute", "$10 million a minute, about $170,000 a second", "$100 million a minute", "$1,000 a second"], "correct": 1, "explain": "460 ÷ 45 ≈ 10.2 million per minute. A kill switch that halts on a daily loss of two times VaR would have fired within the first minute; the point is not the threshold but that it must be automatic, because no human review runs on that clock."},
    {"q": "The daily reconciliation compares", "opts": ["This year's P&L to last year's", "Realised to implied volatility", "VaR to ES", "The book as your own system believes it to be (positions, cash, equity) with the broker's statement of the same, line by line, with any break above a written tolerance investigated before the next session"], "correct": 3, "explain": "Every other lesson computes risk from positions you believe you hold. If the belief is wrong, every number after it is wrong. The reconciliation is the check that the inputs are true, and it is the one control that is entirely within your power to run correctly."},
    {"q": "Which of the following is a pre-trade control in the sense of SEC Rule 15c3-5, as opposed to a post-trade one?", "opts": ["The daily reconciliation", "The monthly risk review", "A per-order size cap, a price collar around the last trade, and a per-minute order-rate limit that rejects the order before it reaches the market", "The VaR report"], "correct": 2, "explain": "15c3-5 requires broker-dealers with market access to have risk controls that prevent the entry of erroneous orders. For a trader running an API, the same controls belong in the order path itself: an order that fails the checks never leaves the machine."},
    {"q": "MF Global failed on 2011-10-31 with a shortfall in segregated customer funds of about $1.6 billion, and Lehman's UK broker-dealer froze prime-brokerage client assets in its 2008 administration. What is the book-level lesson?", "opts": ["The broker is a counterparty; hold cash beyond working needs elsewhere, keep positions at more than one broker if the book is large enough to justify it, and know what protection (SIPC, segregation) covers and does not cover before the day it matters", "Choose a bigger broker", "Brokers cannot fail", "Only futures brokers fail"], "correct": 0, "explain": "Both were large, regulated firms. Neither failure was predictable from the trader's screen. The only defence is structural: diversification of counterparties and a written understanding of what happens to each asset class in each failure mode."}
  ],
  "task": "Write your kill-switch triggers as four numbers, implement them in the order path if you trade through an API, and run one reconciliation by hand tonight."
}
---

## The risk that has no distribution

Market risk has a distribution you can estimate. Operational risk does not. It is the loss from a process failing: a broker that stops paying, a decimal in the wrong place, a credential in the wrong hands, code that does what it was told rather than what was meant. The Basel Committee's definition is "the risk of loss resulting from inadequate or failed internal processes, people and systems or from external events," and its principles for managing it were written for banks but apply unchanged to a one-person book with an API key.

The distinguishing feature is that operational losses are not sized by the market. A fat finger can lose a year's return in a minute in a market that did nothing. So the controls are not statistical; they are structural, and the question for each is not "how likely" but "what stops it."

## Broker failure

The broker is a counterparty. Two cases define the risk.

MF Global, a futures commission merchant and broker-dealer, filed for bankruptcy on 2011-10-31 with a shortfall in customer segregated accounts that the trustee put at about $1.6 billion; the CFTC's 2013 order found the firm had used customer funds to meet its own obligations in its final days. Customers were made whole eventually; "eventually" was more than two years, during which their capital was unavailable.

Lehman Brothers' UK entity, LBIE, held prime-brokerage client assets that had been rehypothecated under standard agreements. When LBIE entered administration on 2008-09-15 those assets were frozen and became unsecured claims. Funds that had assumed their assets were theirs discovered they were the administrator's.

The controls: know what protection applies (SIPC covers securities and cash at a US broker-dealer to a limit and does not cover futures or losses from market movement; segregation rules govern futures accounts); hold cash beyond working needs outside the broker; if the book is large enough, split it across two brokers and keep the split current. None of this is free and all of it is cheaper than two years without your capital.

## Fat fingers and runaway code

Knight Capital, 2012-08-01. A deployment of new order-routing code to eight servers reached seven; the eighth retained old, dormant code that a repurposed flag then activated. For about 45 minutes from the open, the SEC's order records, the system sent millions of orders, executing more than 4 million trades in 154 stocks for more than 397 million shares, accumulating a net long position of about $3.5 billion and a net short of about $3.15 billion, and losing more than $460 million. Knight had no pre-trade controls capable of stopping the flow and no procedure for shutting the system off; staff spent the 45 minutes trying to diagnose the problem while the orders kept going. The firm was sold within the year.

Every element of that is a control that was missing. SEC Rule 15c3-5, the market access rule, now requires broker-dealers to have pre-trade controls that reject orders exceeding size and credit thresholds and prevent erroneous orders. For a trader on an API, the same controls belong in your own order path: a per-order share and notional cap; a price collar that rejects any order more than a few percent from the last trade; a rate limit on orders per minute; a check that the resulting position does not exceed the lesson 6 cap; and a hard daily loss limit that halts everything.

## Keys and access

An API key is the book. Anyone holding it can trade the account. The controls are ordinary security practice applied without exception: keys stored in a secrets manager or the operating system keychain, never in a file that is committed, logged, pasted into a chat or emailed; keys scoped to the minimum permission (trading, not withdrawal, where the broker allows the distinction); IP allow-listing where offered; rotation on a schedule and immediately on any suspicion; and a second factor on the account itself. A key that has appeared anywhere it should not is treated as compromised and rotated the same hour.

## The kill switch

The kill switch is the control that works when every other control has failed. It has three properties. It is automatic: it fires on a number, not on a decision. It is total: it cancels every open order and blocks new ones, and at the second threshold it flattens the book. And it has been tested: the button has been pressed in a live account with a small position, so that its behaviour on the day is known.

Triggers, for a book like this one: daily loss beyond twice the one-day 95% VaR halts new orders; beyond three times, flattens; any position deviating from the intended one by more than a set number of shares halts; order rate above a ceiling halts; loss of connectivity to the broker for more than a set number of seconds cancels all resting orders.

## Worked example

Two calculations, one from Knight and one from the course book.

**Knight's loss rate.** $460 million over 45 minutes = $10.2 million per minute = **$170,000 per second**. Suppose Knight had a kill switch set at a daily loss of 2% of firm equity, a few million dollars. At $170,000 per second it would have fired in under a minute, and the loss would have been under 1% of what it was. The threshold is almost irrelevant; what mattered was that nothing automatic existed.

**The book's daily reconciliation, 2026-09-23.** Your system's belief, from lesson 2: long market value $899,403; short market value $249,985; equity $1,000,000. Cash is therefore equity minus long market value plus short proceeds: 1,000,000 − 899,403 + 249,985 = **$350,582**. The broker's statement should show those four numbers, and each position's share count, to within the tolerance you set: one share on any line, and $50 on cash, say.

Now suppose the broker shows NVDA at 655 shares rather than 665. The break is 10 shares × $225.51 = **$2,255** of market value, and it means either a partial fill you did not record or a fill you recorded that did not happen. Both are investigated before the open, because until they are, every number in the risk report is off by an unknown amount, and the VaR you computed for a 665-share position is the VaR of a book you do not hold.

**Kill-switch thresholds for the book**, from lesson 4's numbers: one-day 95% VaR $9,972. Halt new orders at a daily loss of **$19,944**; flatten at **$29,916**. Position deviation halt: any line more than 5 shares from target. Order-rate halt: more than 20 orders in any minute (this book should send perhaps 20 a day). Connectivity: cancel all resting orders after 30 seconds without a heartbeat.

Note the arithmetic on the flatten threshold: $29,916 is three VaRs, which lesson 4 says the book breaches on roughly one day in a thousand under the normal assumption and more often in practice. In a genuine crash the switch will fire on a day when flattening is expensive. That is accepted; the switch is not a market-risk tool, and the loss it caps is the one that comes from the process, not the market. If it fires on a market day, lesson 7's rule should have fired first.

## Table

| Control | Failure it stops | Threshold for this book | Automatic? | Tested? |
|---|---|---|---|---|
| Per-order cap | Fat finger | ≤ 2× target shares; ≤ $50,000 notional | Yes, in order path | Quarterly |
| Price collar | Bad limit, stale quote | Reject if > 3% from last trade | Yes | Quarterly |
| Order-rate limit | Runaway loop | > 20 orders/minute halts | Yes | Quarterly |
| Daily loss halt | Anything | −$19,944 (2× VaR) halts new orders | Yes | Monthly |
| Daily loss flatten | Anything | −$29,916 (3× VaR) flattens | Yes | Monthly, small size |
| Position deviation | Unrecorded fill | > 5 shares on any line halts | Yes | Daily, via reconciliation |
| Heartbeat | Connectivity loss | 30 s without broker response cancels resting orders | Yes | Monthly |
| Reconciliation | Wrong inputs to everything | Break > 1 share or > $50 cash investigated before open | Manual, daily | Every day is the test |
| Key hygiene | Theft, leak | Secrets store, minimum scope, rotate on any exposure | Partly | On rotation |
| Counterparty split | Broker failure | Cash beyond needs held elsewhere; second broker above a size | Structural | On review |

Thresholds derived from the book's one-day 95% VaR of $9,972 (lesson 4) and its position sizes (lesson 2).

## Where this sits in the framework

Operational controls are the floor under everything else. A VaR computed on a mis-recorded position is fiction; a drawdown rule that cannot cancel orders because the connection is down is decoration; a hedge held at a broker that has frozen the account is a claim in an administration. The controls in the table are cheap, boring and never optional, and the reconciliation is the one to do first, tonight, by hand, so that you know what a clean one looks like before you see a dirty one.

## Sources

- U.S. Securities and Exchange Commission (2013). In the Matter of Knight Capital Americas LLC, Release No. 34-70694. https://www.sec.gov/litigation/admin/2013/34-70694.pdf
- U.S. Securities and Exchange Commission (2010). Risk Management Controls for Brokers or Dealers with Market Access, Rule 15c3-5, Release No. 34-63241. https://www.sec.gov/rules/final/2010/34-63241.pdf
- Commodity Futures Trading Commission (2013). CFTC Files and Simultaneously Settles Charges Against MF Global Inc., Release 6626-13. https://www.cftc.gov/PressRoom/PressReleases/6626-13
- Basel Committee on Banking Supervision (2021). "Revisions to the Principles for the Sound Management of Operational Risk." BCBS d515. https://www.bis.org/bcbs/publ/d515.htm
