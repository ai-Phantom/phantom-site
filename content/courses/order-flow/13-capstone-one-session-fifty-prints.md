---
{
  "title": "Capstone: One Session, Fifty Prints, and What the Flow Did Not Predict",
  "duration": "20 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Print 33 in the capstone tape is 10,000 shares at 187.18 with the NBBO at 187.18 / 187.20. It is classified as:", "opts": ["Buy, because the price rose afterwards", "Sell, because it traded at the bid", "Unclassifiable", "Buy, because it is large"], "correct": 1, "explain": "The quote rule is mechanical: a print at the bid is a sell aggressor. What the price did next is not an input to the classification."},
    {"q": "Print 7 is 10,000 shares at 187.125 with the NBBO at 187.12 / 187.13. Under Lee and Ready it is:", "opts": ["A sell by the quote rule", "A buy by the tick test, since the previous different price was 187.12", "Excluded", "A buy by the quote rule"], "correct": 1, "explain": "Midpoint prints go to the tick test. The prior print was at 187.12, so 187.125 is an uptick and the tick test says buy; a midpoint print of that size is also plausibly a cross with no aggressor, which your write-up should note."},
    {"q": "Over the fifty prints, quote-rule sell volume is 33,100 and buy volume 20,300, yet the price rose from 187.10 to 187.25. The correct description is:", "opts": ["The classification is wrong", "Aggressive sellers were absorbed by passive buyers and the price rose anyway: flow and price disagreed", "Buyers were the aggressors", "The stock was manipulated"], "correct": 1, "explain": "This is the absorption case from lesson 7 in miniature. Delta was negative and price rose; the tape cannot say in real time which side will win."},
    {"q": "Session REP-B's cumulative delta is negative from 09:30 through 14:00 and turns positive at 14:30. Price closed at 187.90, up 0.80. What did the half-hour flow predict?", "opts": ["The whole day's rise", "Nothing about the morning; the afternoon rise coincided with positive delta but did not precede it", "A decline that did not happen", "The closing auction"], "correct": 1, "explain": "The morning rise happened against negative delta. The afternoon rise happened with positive delta. Coincident, not predictive, exactly as Chordia et al. found."},
    {"q": "Which of these earns zero points under the rubric's interpretation criterion?", "opts": ["Stating that the sample cannot distinguish absorption from a fading ceiling", "Claiming the negative morning delta 'signalled' the rise because absorption is bullish", "Noting that the 15:30 slot contains benchmark flow", "Listing the misclassification risk of off-exchange prints"], "correct": 1, "explain": "A post-hoc rule invented to fit the outcome is what the course spent twelve lessons teaching you not to do. The other three are exactly the honest limitations the rubric rewards."}
  ],
  "task": "Submit the classified tape, the half-hour delta table, the two charts and the write-up; then repeat the exercise on a real session from a stated public source and compare the two."
}
---

## The exercise

You will take one liquid stock's tape for one session, classify fifty consecutive prints as buyer- or seller-initiated, compute delta by half hour for the full session, compare cumulative delta to the price path, and write what the flow did and did not predict. The write-up is graded by the rubric at the end.

You may use either of two datasets. The preferred one is real: export time and sales and half-hour volume for one S&P 500 stock on one recent session from your broker's platform or another public source, state the source and the date, and use your platform's aggressor flags if it publishes them, or Lee-Ready classification if it does not. The fallback is representative session REP-B below, which was constructed for this capstone with the same proportions as lesson 7's REP-A and is not a real day. If you use REP-B, say so in the first line of your submission.

## Part 1: classify fifty prints

The tape below is the first fifty prints after 09:31 in REP-B, a representative $187 large-cap. Columns are time, the NBBO bid and ask prevailing at the print, the print price and the size. Apply the quote rule from lesson 6: a print above the midpoint is a buy, below the midpoint a sell. For prints exactly at the midpoint, apply the tick test against the previous different price. Record your classification in a sixth column.

| # | Time | Bid | Ask | Price | Size |
|---|---|---|---|---|---|
| 1 | 09:31:06 | 187.10 | 187.12 | 187.10 | 1,000 |
| 2 | 09:31:12 | 187.10 | 187.12 | 187.10 | 100 |
| 3 | 09:31:22 | 187.10 | 187.12 | 187.10 | 1,000 |
| 4 | 09:31:35 | 187.10 | 187.12 | 187.12 | 100 |
| 5 | 09:31:45 | 187.10 | 187.12 | 187.12 | 300 |
| 6 | 09:31:57 | 187.12 | 187.13 | 187.12 | 500 |
| 7 | 09:32:13 | 187.12 | 187.13 | 187.125 | 10,000 |
| 8 | 09:32:20 | 187.12 | 187.13 | 187.12 | 1,500 |
| 9 | 09:32:38 | 187.13 | 187.14 | 187.13 | 1,500 |
| 10 | 09:32:47 | 187.13 | 187.14 | 187.13 | 500 |
| 11 | 09:32:58 | 187.13 | 187.14 | 187.14 | 7,500 |
| 12 | 09:33:13 | 187.14 | 187.16 | 187.14 | 500 |
| 13 | 09:33:26 | 187.15 | 187.16 | 187.15 | 100 |
| 14 | 09:33:35 | 187.15 | 187.16 | 187.15 | 400 |
| 15 | 09:33:37 | 187.14 | 187.15 | 187.14 | 1,500 |
| 16 | 09:33:42 | 187.14 | 187.15 | 187.15 | 1,500 |
| 17 | 09:33:44 | 187.15 | 187.16 | 187.15 | 1,000 |
| 18 | 09:33:54 | 187.15 | 187.16 | 187.16 | 1,000 |
| 19 | 09:34:12 | 187.14 | 187.15 | 187.14 | 400 |
| 20 | 09:34:27 | 187.14 | 187.15 | 187.145 | 300 |
| 21 | 09:34:34 | 187.14 | 187.15 | 187.15 | 300 |
| 22 | 09:34:44 | 187.13 | 187.15 | 187.15 | 100 |
| 23 | 09:34:48 | 187.15 | 187.17 | 187.17 | 400 |
| 24 | 09:34:55 | 187.14 | 187.15 | 187.14 | 1,500 |
| 25 | 09:35:00 | 187.14 | 187.15 | 187.15 | 200 |
| 26 | 09:35:07 | 187.15 | 187.16 | 187.155 | 400 |
| 27 | 09:35:16 | 187.16 | 187.17 | 187.17 | 300 |
| 28 | 09:35:21 | 187.16 | 187.17 | 187.165 | 2,500 |
| 29 | 09:35:37 | 187.17 | 187.19 | 187.17 | 1,000 |
| 30 | 09:35:39 | 187.17 | 187.19 | 187.17 | 500 |
| 31 | 09:35:42 | 187.17 | 187.19 | 187.19 | 500 |
| 32 | 09:35:44 | 187.18 | 187.20 | 187.18 | 1,500 |
| 33 | 09:35:48 | 187.18 | 187.20 | 187.18 | 10,000 |
| 34 | 09:36:03 | 187.18 | 187.20 | 187.18 | 500 |
| 35 | 09:36:22 | 187.18 | 187.20 | 187.19 | 100 |
| 36 | 09:36:40 | 187.18 | 187.20 | 187.20 | 2,500 |
| 37 | 09:36:52 | 187.19 | 187.20 | 187.19 | 100 |
| 38 | 09:37:05 | 187.19 | 187.20 | 187.19 | 100 |
| 39 | 09:37:15 | 187.19 | 187.20 | 187.20 | 100 |
| 40 | 09:37:26 | 187.20 | 187.21 | 187.21 | 100 |
| 41 | 09:37:33 | 187.21 | 187.22 | 187.22 | 400 |
| 42 | 09:37:44 | 187.21 | 187.22 | 187.21 | 100 |
| 43 | 09:37:46 | 187.21 | 187.22 | 187.21 | 300 |
| 44 | 09:38:00 | 187.23 | 187.24 | 187.24 | 300 |
| 45 | 09:38:08 | 187.23 | 187.24 | 187.24 | 100 |
| 46 | 09:38:10 | 187.24 | 187.25 | 187.25 | 2,500 |
| 47 | 09:38:17 | 187.24 | 187.25 | 187.25 | 1,500 |
| 48 | 09:38:34 | 187.24 | 187.25 | 187.25 | 400 |
| 49 | 09:38:42 | 187.23 | 187.24 | 187.24 | 200 |
| 50 | 09:38:59 | 187.25 | 187.27 | 187.25 | 7,500 |

Report three totals: buy volume, sell volume and midpoint volume, first under the quote rule alone (midpoints left unclassified) and then with the tick test applied. Then answer, in two sentences, whether the sign of the eight-minute delta matches the sign of the price change from 187.10 to 187.25, and what that tells you.

## Part 2: delta by half hour

REP-B's full-session aggressor volumes in millions of shares, closing auction excluded, with the last regular print of each slot. Open 187.10.

| Slot | Buy | Sell | Close |
|---|---|---|---|
| 09:30 | 0.94 | 1.12 | 187.25 |
| 10:00 | 0.71 | 0.63 | 187.41 |
| 10:30 | 0.52 | 0.49 | 187.38 |
| 11:00 | 0.47 | 0.51 | 187.30 |
| 11:30 | 0.41 | 0.38 | 187.36 |
| 12:00 | 0.36 | 0.39 | 187.33 |
| 12:30 | 0.33 | 0.35 | 187.29 |
| 13:00 | 0.35 | 0.33 | 187.34 |
| 13:30 | 0.31 | 0.34 | 187.31 |
| 14:00 | 0.44 | 0.39 | 187.44 |
| 14:30 | 0.57 | 0.48 | 187.62 |
| 15:00 | 0.69 | 0.61 | 187.71 |
| 15:30 | 1.41 | 1.27 | 187.90 |

Compute delta per slot, cumulative delta, price change from the open, and session totals; check that the final cumulative delta equals total buy minus total sell. Plot cumulative delta and price change on the same axes as lesson 7's chart, and delta per slot as bars.

## Part 3: the write-up

Four hundred to seven hundred words, in this order. First, the source: data, date, classification method and its accuracy limits (lesson 6). Second, the description: for each phase you identify, what the flow and the price were doing, with numbers. Third, the comparison: where flow and price agreed or disagreed, and each half hour's state (trend, absorption, flat) under lesson 12's classification. Fourth, the prediction test: for each phase, whether the flow preceded, coincided with or followed the price move, with timing. Fifth, the limits: misclassification, off-exchange lag, benchmark contamination of the 15:30 slot, and the fact that one session is one draw.

Honest description earns marks; any rule discovered after seeing the close loses them. If you find yourself writing "absorption is bullish" because the day ended up, check whether you would have written "absorption is bearish" on REP-A, where it ended down.

## Worked example

The arithmetic for Part 1 and the first rows of Part 2, so you can check your own.

Part 1, quote rule alone. Prints at the ask (buys): 4, 5, 11, 16, 18, 21, 22, 23, 25, 27, 31, 36, 39, 40, 41, 44, 45, 46, 47, 48, 49. Sum: 100 + 300 + 7,500 + 1,500 + 1,000 + 300 + 100 + 400 + 200 + 300 + 500 + 2,500 + 100 + 100 + 400 + 300 + 100 + 2,500 + 1,500 + 400 + 200 = 20,300 shares over 21 prints. Prints at the bid (sells): the remaining 24 non-midpoint prints, sum 33,100 shares. Midpoint prints: 7, 20, 26, 28, 35, sum 10,000 + 300 + 400 + 2,500 + 100 = 13,300. Total 20,300 + 33,100 + 13,300 = 66,700. Quote-rule delta = 20,300 − 33,100 = −12,800 on the 53,400 classified shares.

Tick test on the midpoints. Print 7 at 187.125 follows 187.12 (print 6): uptick, buy. Print 20 at 187.145 follows 187.14: uptick, buy. Print 26 at 187.155 follows 187.15: uptick, buy. Print 28 at 187.165 follows 187.17 (print 27): downtick, sell. Print 35 at 187.19 follows 187.18: uptick, buy. Buys gain 10,000 + 300 + 400 + 100 = 10,800; sells gain 2,500. Full classification: buy 31,100, sell 35,600, delta = −4,500, buy share = 31,100 / 66,700 = 46.6%.

Price change: 187.25 − 187.10 = +0.15. Delta negative under both methods, price up. Two prints of 10,000 shares hit the bid (33 at 187.18) or crossed at the midpoint (7); the bid was refreshed each time and the quote rose eleven cents over the next three minutes. Sellers were aggressive and absorbed. Whether that absorption was accumulation was not knowable at 09:39.

Part 2, first three slots. 09:30: delta = 0.94 − 1.12 = −0.18; CVD −0.18; price +0.15. 10:00: delta = 0.71 − 0.63 = +0.08; CVD −0.10; price +0.31. 10:30: delta = 0.52 − 0.49 = +0.03; CVD −0.07; price +0.28. Session totals: buy 7.51, sell 7.29, delta +0.22; CVD ends at +0.22, check passed. CVD is negative through 14:00 and crosses zero at 14:30 with price already +0.52; the afternoon rise from 187.44 to 187.90 coincides with four positive-delta slots. The morning rise from 187.10 to 187.41 happened against a cumulative delta of −0.10. One session, two phases, one where flow matched and one where it did not, and neither where flow came first.

## Rubric

| Criterion | What earns full marks | Points |
|---|---|---|
| Source and method | Dataset named (real source and date, or "REP-B representative"); classification method stated with its accuracy limits; midpoint and off-exchange handling explained | 15 |
| Classification accuracy | All fifty prints classified; quote rule applied correctly; tick test applied only to midpoints and correctly; totals match the worked example within rounding (buy 31,100, sell 35,600 for REP-B) | 25 |
| Delta arithmetic | Delta, CVD and price change correct for all thirteen slots; session totals reconcile; two charts present and labelled, closing auction excluded | 20 |
| Comparison to price | Each half hour classified as trend, absorption or flat; phases identified with numbers; agreement and disagreement between flow and price stated explicitly | 15 |
| Interpretation and limits | Prediction test answered per phase with timing; limits section covers misclassification, off-exchange lag, benchmark contamination and single-session sampling; no rule invented after seeing the outcome | 25 |

Seventy points passes. A submission that finds the flow predicted nothing, and says so with correct arithmetic, scores identically to one that finds a coincidence and describes it as a coincidence.

## Sources

- Charles Lee and Mark Ready, "Inferring Trade Direction from Intraday Data", Journal of Finance 46(2), 1991: https://doi.org/10.1111/j.1540-6261.1991.tb02683.x
- Tarun Chordia, Richard Roll and Avanidhar Subrahmanyam, "Order Imbalance, Liquidity, and Market Returns", Journal of Financial Economics 65(1), 2002: https://doi.org/10.1016/S0304-405X(02)00136-8
- FINRA, OTC (ATS & Non-ATS) Transparency data, for checking the off-exchange share of any real session you use: https://www.finra.org/filing-reporting/otc-transparency
- Yahoo Finance, historical data pages (intraday bars for the half-hour volume of a real session): https://finance.yahoo.com/quote/SPY/history/
