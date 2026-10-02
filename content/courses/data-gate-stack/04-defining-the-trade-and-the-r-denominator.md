---
{
  "title": "Defining the Trade: Entry, Stop, R and the Collapsed Denominator",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A pullback rule enters at the close of the third consecutive lower close and puts its stop at the lowest low of those three bars. Why does its R denominator collapse systematically rather than occasionally?", "opts": ["Because SPY is volatile", "Because a third down day frequently closes at or near the three-day low, so entry minus stop is close to zero by construction", "Because the vendor rounds lows", "Because the target is too far"], "correct": 1, "explain": "The stop is the entry bar's own extreme. The geometry, not bad luck, produces a near-zero risk on a fraction of trades, and each of those trades reports an enormous R for an ordinary move."},
    {"q": "On SPY 2010-2025, the same pullback entries produced a mean move of +0.407% with the three-bar-low stop and +0.395% with a one-ATR stop, but +1.626 R against +0.412 R. What does the four-fold difference in R measure?", "opts": ["The ATR stop is worse", "The three-bar stop captures more upside", "Sampling error", "The denominator, and nothing else; the price paths were essentially identical"], "correct": 3, "explain": "A 0.3 percentage-point difference in the move cannot produce a four-fold difference in R. The difference is 32 trades with stops inside 0.1% of price, one of which reported 152.6 R for a 3.9% move."},
    {"q": "The P2 denominator gate first measured thin-stop trades' share of NET total R and produced a false failure on a short rule where a single ordinary +2.00 R winner read as −33% of the total. Why?", "opts": ["The net total was −6.00 R, near zero, so any single trade was a large fraction of it; the gate about unstable denominators had an unstable denominator", "The winner was an outlier", "Shorts should not be measured in R", "The total should have been in dollars"], "correct": 0, "explain": "The fix was gross R, the sum of absolute returns, which is at least as large as any numerator and bounded in [0, 1]. Verified on every real case: the artefact still failed at 51% and the false failure passed at 2.0%."},
    {"q": "A gap-fill rule achieved a 59.2% win rate against a required 59.6%. Cost was 0.1 of the 0.4 percentage-point gap. What kind of failure is this?", "opts": ["A data defect", "A collapsed denominator", "Exact neutrality: the market prices the fill correctly and no artefact explains it away", "Underpowered"], "correct": 2, "explain": "Every other failure in the notes had a cause. This one had none, which makes it the cleanest no-edge result in the catalogue. Not every failure is a bug to find."},
    {"q": "Why is R the wrong unit for a time exit?", "opts": ["R is only for options", "R normalises by stop distance, so a rule with no bracket ranks the size of the entry bar's range rather than the outcome; a 0.086% stop turns an ordinary 2% move into +23 R", "Time exits are always in dollars", "It is not; R is universal"], "correct": 1, "explain": "The unit is part of the experiment. A bracketed trade's natural unit is R; a time exit's is percent of price. Measured in R the exit surface ranked a two-day hold best; in percent a twenty-day hold earned seventeen times the one-day hold."}
  ],
  "task": "For your own rule, compute each trade's stop distance as a percentage of the entry price and report the share of gross R carried by trades below 0.1%; if it exceeds 25%, rewrite the stop before running any other test."
}
---

## The trade is the unit of measurement

Before a rule can be tested it has to say what a trade is: the price at which it enters, the price at which it admits it was wrong, and the price or time at which it leaves. Every statistic afterwards is computed per trade, and the most common way to make a statistic lie is to define the trade so that its unit of risk is unstable.

The stack calls this family of checks P, for preconditions, and runs them after the data gates and before any inference. P0 asks whether the detector used any bar after the one it fired on. P2 asks whether the risk denominator is real. P3 asks whether the trades are independent of each other. This lesson is about P2, with P0 covered in Lesson 3 and P3 in Lesson 8.

## R and why it is used

R is the outcome of a trade divided by the distance from entry to stop. A trade that risks $1.00 per share and makes $2.00 is +2 R; one that is stopped is −1 R. It is the natural unit for a bracketed trade because it makes trades with different stop widths comparable and it is what position sizing consumes: a fixed fraction of equity per R means the dollar loss on a stop is the same on every trade.

The convenience hides a division. If the stop is close to the entry, the denominator is small, and an ordinary move in the numerator becomes an enormous R. A rule does not have to be designed to do this; it only has to put the stop somewhere that is sometimes very close to the entry, and a whole class of sensible-sounding stops does exactly that.

## The collapsed denominator

The research notes (Phantom Traders, 2026, internal) record the second setup ever run through the stack, dated 2026-09-14: a three-bar pullback whose stop was the lowest low of the last three bars and whose entry was the third bar's close. It passed all six gates then in the stack with an average winner of +10.6 R. The top five trades supplied +366.2 of +564.2 total R, 65% of the result; the largest reward-to-risk was 194.7 to 1; the single best trade risked 0.0253% of price and returned +165.6 R. Twenty-four of 251 trades had risk under 0.05% of price and carried 58% of the result.

The geometry is the cause. A pullback's third down day frequently closes at the three-day low, so entry minus stop is close to zero systematically. The minimum-risk guard in the harness was set at 0.01% of price, calibrated for a different setup, and caught none of them.

The part worth remembering is that the stack passed it. An inflated R inflates every downstream number at once. The average winner sails through the geometry gate, because a 194-to-1 payoff needs almost no win rate. The effect size sails through the power gate. The random-entry null is beaten partly because the real setup collapses denominators more systematically than random-date entries do; the null was matched on bracket geometry but not on the realised risk distribution. The holdout holds, because the artefact is present in both halves. Six green gates on a division by nearly zero.

## The P2 gate and its own collapse

The gate built in response fails a study when trades whose stop sits closer than 0.1% of price carry more than 25% of total R. It is not a fat-tail filter; trend following is legitimately concentrated and must survive it. It rejects concentration caused by a vanishing denominator. On the two real setups it discriminated cleanly: the three-bar pullback had 44 of 251 trades below the floor carrying 72% of R and failed; an inside-day setup, whose stop was the parent bar's low, a full bar from entry, had 3 of 388 carrying 0% and passed. Same gate, opposite verdicts, and the difference was the stop placement alone.

Then the gate's own denominator collapsed the same day. The first version measured the thin trades' share of net total R. Net total R is the strategy's profit, which goes to zero for exactly the near-break-even strategies the gate must still judge, so any single trade becomes a huge share of it. A short inside-day run exposed it: one ordinary +2.00 R winner out of 75 read as −33% of the total, because the total was −6.00 R. The fix was gross R, the sum of absolute trade outcomes, which is at least as large as any numerator by construction and bounded between 0 and 1. Verified on every real case rather than argued: inside-day long 0.7%, pullback v2 0.0%, inside-day short 2.0% (previously a false failure), pullback v1 51% (still caught).

One more thing happened that day. The regression test for the fix was added by a string replacement whose anchor did not match, so the test was never inserted, and the suite still reported that all checks passed because 34 unrelated checks did. An unrun test is indistinguishable from a passing one. Verify a new test by finding its own text in the output, never by the summary line.

## The clean no-edge

Not every failure at this layer is an artefact. A gap-down fill rule achieved a 59.2% win rate against the 59.6% its bracket and cost required. Friction was 0.1 of the 0.4 percentage-point gap, nearly irrelevant, because the risk unit was a full gap width. Nothing explained it away: not beta, not a collapsed denominator, not a stale stamp. The market prices the fill correctly. The notes call it the cleanest result in the catalogue, and it is worth knowing what one looks like, because most failures come with a cause and this one came with none.

## Worked example

The pullback geometry reproduces on SPY daily bars from Yahoo Finance, 2010-01-04 to 2025-12-31, fetched 2026-09-30, dividend-adjusted OHLC. The rule: after three consecutive lower closes, buy at the third close; stop at the lowest low of those three bars; no target; exit at the stop or at the close of the tenth bar after entry. R is the exit move divided by entry minus stop. Trades do not overlap.

With the three-bar-low stop: 219 trades, mean +1.626 R, total +356.1 R, win rate 21.0%, mean price move +0.407%, median stop distance 0.345% of price. Thirty-two trades had a stop inside 0.1% of price, and those 32 carried 30.3% of gross R. The top five trades carried 43.4% of gross R. The largest was entered 2014-12-16 at 197.91 with a stop at 197.86, a risk of 0.05 / 197.91 = 0.025% of price; it exited 2014-12-31 up 3.855%, and 3.855 / 0.025 = 152.6 R. The second largest, 2011-11-25, risked 0.120% for +8.35%, or 69.4 R.

With the stop replaced by one 14-day average true range below entry, on the same entry signals: 201 trades, mean +0.412 R, total +82.7 R, win rate 36.8%, mean price move +0.395%, median stop distance 1.040%. No trade had a stop inside 0.1% of price. The top five carried 8.7% of gross R and the largest trade was 6.8 R.

Put the two mean moves side by side: +0.407% and +0.395%. The price paths are the same paths; the rule buys the same days. The ratio of the mean R figures is 1.626 / 0.412 = 3.9. A difference of 0.012 percentage points in the numerator cannot produce a four-fold difference in the ratio; the whole of it is the denominator. The P2 gate reads 30.3% of gross R from thin-stop trades against a 25% bar and fails the first version; it reads 0.0% and passes the second.

A note on the smaller effect underneath: the three-bar version's win rate of 21% with a large mean R and the ATR version's 37% with a small one describe the same 0.4% average move. Neither number on its own tells you anything the other does not, once the denominator is fixed.

![Ten bars, one per trade, showing the ten largest R multiples from the SPY three-bar pullback with the three-bar-low stop, 2010-2025. Each bar is labelled with the stop distance as a percentage of price; the two red bars, at 0.025% and 0.099%, are the ones inside the 0.1% floor, including the 152.6 R trade.](figures/collapsed-denominator-top-trades.svg)

## Table

Where a stop can sit and what it does to the denominator, with the cases from this lesson and the notes.

| Stop placement | Risk floor | Denominator behaviour | Case |
|---|---|---|---|
| Lowest low of the entry bar and its predecessors | none; can be one tick | Collapses whenever the entry closes at the window low | 3-bar pullback: 32 of 219 trades under 0.1% carried 30.3% of gross R here; 44 of 251 carried 72% in the notes |
| Parent bar's low (inside-day) | about one bar's range | Stable; risk is a real distance | Inside-day: 3 of 388 under the floor, 0% of R |
| Fixed fraction of price | that fraction | Stable, ignores volatility | Used in Lesson 6 to show cost in R |
| One ATR below entry | recent range | Stable, scales with volatility | Same entries: max 6.8 R, top five 8.7% of gross |
| Full gap width (gap fill) | the gap | Stable and large; cost nearly irrelevant | 59.2% achieved vs 59.6% required |

Two rules follow. Never set a stop on the entry bar's own extreme. And when a result looks good, check the risk denominator before anything else: the top-five share of gross R is the one-line diagnostic.

## Sources

- Kelly, J. L. (1956). "A New Interpretation of Information Rate." Bell System Technical Journal 35(4). https://doi.org/10.1002/j.1538-7305.1956.tb03809.x
- Harvey, C. R., Liu, Y. (2014). "Evaluating Trading Strategies." Journal of Portfolio Management 40(5). https://doi.org/10.3905/jpm.2014.40.5.108
- Yahoo Finance, SPY historical data (daily bars for the worked example): https://finance.yahoo.com/quote/SPY/history/
