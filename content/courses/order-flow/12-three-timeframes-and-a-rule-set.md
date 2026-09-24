---
{
  "title": "Reading Structure at Three Timeframes and Building a Rule Set",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Which of these belongs on the daily (session) timeframe checklist?", "opts": ["The last ten prints", "The prior close, the opening auction print and the published closing imbalance", "Delta for the current 1-minute bar", "The best bid size"], "correct": 1, "explain": "Session-level structure is set by the auctions and the reference prices that benchmark flow targets."},
    {"q": "Rule 3 in the set says never send a market order in the first 60 seconds after a scheduled release. The lesson that justifies it is:", "opts": ["Lesson 2, auctions", "Lesson 5, dealers widen spreads when the informed share jumps", "Lesson 9, HFT races", "Lesson 11, spoofing"], "correct": 1, "explain": "Glosten-Milgrom: the spread widens 2.5× in the worked example when the probability of informed trading rises. A market order fills into that widened quote."},
    {"q": "At 14:00 in session REP-A, the three-timeframe read was: session +0.92 from open, 30-minute CVD falling for seven slots, tape showing sellers absorbed. The rule set's instruction is:", "opts": ["Buy, because absorption is bullish", "Sell, because delta is negative", "Do not initiate; the timeframes disagree and absorption has no real-time resolution", "Send a market order"], "correct": 2, "explain": "Rule 6: when the session and the 30-minute flow disagree, the read is 'unresolved', and the rule set forbids new positions on unresolved reads."},
    {"q": "Why does the rule set size positions by order size as a share of average daily volume?", "opts": ["Because brokers require it", "Because expected impact scales with the square root of that ratio, and above about 0.5% of ADV an order must be worked", "Because volume is always the same", "Because it maximises fills"], "correct": 1, "explain": "Lesson 10's square-root law. The threshold is a rule of thumb; the mechanism is not."},
    {"q": "What is the correct response to a 5,000-share bid appearing two ticks below the market?", "opts": ["Treat it as support", "Treat it as a spoof", "Treat it as neither: displayed size is not a commitment, and rules must not depend on it", "Hit it immediately"], "correct": 2, "explain": "Lessons 1 and 11: depth can be withdrawn in microseconds and its display may be deliberate. A rule that depends on displayed size is a rule that can be gamed."}
  ],
  "task": "Write your own version of the rule set with at most eight rules, each citing the lesson whose evidence justifies it, and delete any rule you cannot justify."
}
---

## Three timeframes, one market

The preceding eleven lessons described the market at three resolutions. The session: auctions, the volume curve, the prior close and the closing imbalance, benchmark flow that trades on a schedule. The half hour: delta and cumulative delta, the persistent imbalances left by algorithms slicing parent orders, the drift of dealer inventories. The tape: individual prints, aggressors, the book, the microsecond races and the occasional spoof. Each resolution has a different mix of information and noise, and the mistake most order-flow traders make is reading the tape as if it carried session-level meaning.

This lesson assembles what the evidence supports into a rule set, and applies it to representative session REP-A from lesson 7 to show what "applying" means. The rule set is not a strategy and no performance is claimed for it. It is a list of things the course has shown to be true about how prices form, written as constraints on your own behaviour.

## The session timeframe

What is fixed before 09:30: the prior close, the overnight range in futures, the scheduled releases and their times. What is set at 09:30: the opening auction print, which resolves overnight information into one price. What is scheduled: the volume curve (14% of volume in the first half hour, 21% in the last, 4% at the trough in lesson 2's sample), the 15:50 imbalance publication and the 16:00 close.

The session-level read is a list of reference prices, not a forecast. Where is price relative to the open, the prior close and the session VWAP? Is the closing imbalance published yet, and which side? Is this a release day? Those questions answer themselves from public data and they set what the lower timeframes mean: a delta divergence at 11:00 on a quiet day is a different thing from the same divergence at 15:52 with a 2-million-share sell imbalance published.

## The half-hour timeframe

Delta and CVD by half hour describe who was aggressive and whether price followed. Lesson 7's evidence: the contemporaneous relation is strong, the predictive relation weak, and absorption (flow one way, price flat) is genuinely ambiguous in real time. Lesson 10 adds that half-hour imbalances are autocorrelated because parent orders persist. So the half-hour read is a classification into three states: flow and price agree (trend, likely a parent order working), flow and price disagree (absorption, unresolved), or flow is flat (nothing to read). The rule set treats only the first as actionable and even then only as a filter.

## The tape timeframe

The tape tells you who crossed the spread in the last minute and what the book looks like now. Lesson 6's evidence: aggressor classification is 70–85% accurate on exchange prints and worse off-exchange; large midpoint prints have no aggressor. Lesson 1 and lesson 11: displayed size is not a commitment. Lesson 9: you are not in the race and nothing on the tape is being hidden from you, but everything on it was seen by faster participants first. The tape timeframe is therefore for execution, not for deciding. It answers "is now a bad moment to send this order?" (wide spread, thin inside, a release seconds away) and nothing larger.

## Worked example

Apply the rule set to REP-A at two moments. Recall the session: open 187.10; 09:30 delta +0.29M, price to 187.42; by 11:30 price 188.20 with CVD +0.36M; 10:30 through 14:00 delta negative in seven of eight slots, price holding 188.02–188.20; 15:00 CVD −0.06M, price 187.61; close 187.24. Average daily volume for the representative stock: 8 million shares. Your intended order: 20,000 shares.

Moment 1, 10:05. Session read: price +0.86 from the open, above the opening print, no release scheduled, no imbalance yet (it is 10:05). Half-hour read: two positive-delta slots, price up with them: flow and price agree. Tape read: spread $0.02, inside sizes in the low thousands, no prints larger than 5,000 in the last minute.

- Rule 1 (session reference): price above open and prior close; the session read is "up".
- Rule 2 (half-hour agreement): delta and price agree; the half-hour read is "trend".
- Rule 5 (size): 20,000 / 8,000,000 = 0.25% of ADV. Below the 0.5% threshold; a single limit order is acceptable, but Rule 5 still forbids a market order above 0.1% of ADV, and 0.25% exceeds it, so the order is placed as a limit at the inside, not at market.
- Rule 3 (release): not applicable.
- Rule 7 (displayed size): the rule set does not use it.

Conclusion at 10:05: a long entry is permitted by the rule set. Whether it is a good trade is a question the rule set does not answer; it only says nothing in the structure forbids it.

Moment 2, 14:00. Session read: price +0.92, still above open; no imbalance published yet. Half-hour read: delta negative in seven of eight slots, CVD down from +0.40M to +0.19M, price flat: flow and price disagree, state "absorption". Tape read: sellers hitting bids in size (several 10,000-share prints at the bid in the last half hour), bids refreshing.

- Rule 2: half-hour read is "absorption", which Rule 6 classifies as unresolved.
- Rule 6 (disagreement): no new position on an unresolved read, in either direction.
- Rule 8 (existing positions): the 10:05 long, if taken, is held or reduced by the trader's own stop rule; the flow read does not force an exit because absorption has two outcomes and lesson 7 showed the flow cannot pick one.

Conclusion at 14:00: no new trade. In hindsight the absorption resolved to the downside at 15:00 and the day closed +0.14, so a short at 14:00 would have worked and a long added at 14:00 would have lost. The rule set forbade both, which is the point: a rule that says "sell absorption" would have been wrong on a day where passive buyers won, and the evidence in lesson 7 says those days are as common as this one. Rules are about the distribution, not the instance.

The arithmetic worth repeating from this example: 20,000 shares is 0.25% of ADV; under lesson 10's square-root model with 1.5% daily volatility the expected impact of sending it aggressively is 150 × √0.0025 = 150 × 0.05 = 7.5 basis points, or $0.14 on a $187 stock, which is seven times the $0.02 spread. That number, and not any signal, is why Rule 5 exists.

## Table

| # | Rule | Justifying evidence |
|---|---|---|
| 1 | Before 09:30, write down the prior close, overnight futures range, scheduled release times and the volume curve; after 09:30, the opening print; after 15:50, the imbalance side and size | Lesson 2: auctions and benchmark flow set the session's reference prices |
| 2 | Classify each half hour as trend (delta and price agree), absorption (they disagree) or flat; only trend is actionable, and only as a filter | Lesson 7: contemporaneous relation strong, predictive weak; absorption unresolved in real time |
| 3 | No market orders in the 60 seconds around a scheduled release or in the first 60 seconds after 09:30 | Lesson 5: spread widens 2.5× in the model when the informed share jumps; Lesson 2: opening volatility |
| 4 | For any order above 0.1% of the stock's ADV, use a limit order; above 0.5%, work it in slices or use the closing auction | Lesson 10: impact ≈ σ√(Q/V); Lesson 2: auction liquidity |
| 5 | Never send an order at market in the last ten minutes unless it is an MOC entered before the cutoff | Lesson 2: 15:50 cutoffs and imbalance-driven drift |
| 6 | When the session read and the half-hour read disagree, take no new position in either direction | Lesson 7: REP-A absorption; Chordia et al. on weak prediction |
| 7 | No rule may depend on displayed size at any level of the book | Lessons 1 and 11: depth is withdrawable in microseconds and may be a spoof |
| 8 | Exits are governed by a stop written before entry, not by flow; flow may tighten a stop, never widen it | Lesson 7: flow describes, does not forecast; Lesson 10: shortfall includes opportunity cost |
| 9 | Read your broker's Rule 606 report quarterly and route away from any venue whose payment structure you cannot explain | Lessons 3 and 4: rebates and PFOF go to the broker; SEC 1.08 bp shortfall estimate |

Nine rules, each traceable to a measured fact. Add a tenth only if you can name the lesson and the number that justify it.

## Sources

- Anat Admati and Paul Pfleiderer, "A Theory of Intraday Patterns: Volume and Price Variability", Review of Financial Studies 1(1), 1988: https://doi.org/10.1093/rfs/1.1.3
- Nasdaq, "Nasdaq Closing Cross" FAQ (imbalance publication and cutoffs used in Rules 1 and 5): https://www.nasdaqtrader.com/content/productsservices/Trading/ClosingCrossfaq.pdf
- Tarun Chordia, Richard Roll and Avanidhar Subrahmanyam, "Order Imbalance, Liquidity, and Market Returns", Journal of Financial Economics 65(1), 2002: https://doi.org/10.1016/S0304-405X(02)00136-8
- SEC, "Proposed Rule to Enhance Order Competition" fact sheet, Release No. 34-96495 (December 2022): https://www.sec.gov/files/34-96495-fact-sheet.pdf
