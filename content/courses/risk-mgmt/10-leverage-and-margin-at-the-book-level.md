---
{
  "title": "Leverage and Margin at the Book Level",
  "duration": "18 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Under Regulation T the initial margin requirement on a book with $899,403 long and $249,985 short is", "opts": ["$299,846", "$449,702", "$574,694", "$1,149,388"], "correct": 2, "explain": "Reg T requires 50% of both long and short market value at initiation: 0.5 × (899,403 + 249,985) = $574,694. With $1,000,000 of equity the book has $425,306 of excess, and its gross could not exceed 200% of equity at initiation whatever its risk profile."},
    {"q": "Portfolio margin under FINRA Rule 4210(g) stresses a broad-index equity book across a range of about ±15% and requires the worst-case loss. For this book that is about $97,400, 9.7% of equity, against 57.5% under Reg T. What does the difference tell you?", "opts": ["Portfolio margin is safer", "Portfolio margin prices the hedge: because the shorts offset the longs in a market move, the worst-case loss is small, and the broker lends against that; the leverage it permits is the risk it does not require you to fund", "Reg T is a mistake", "The shorts are free"], "correct": 1, "explain": "Reg T is strategy-agnostic; portfolio margin is risk-based. The same book can be run at nearly six times the gross under portfolio margin, and the stress that sets the requirement (±15%) is smaller than the moves the book's components made in March 2020 (−32% to −48%)."},
    {"q": "The book at 4x gross under portfolio margin (long $3.60M, short $1.00M on $1M equity) suffers a gap of −20% on the longs and +10% on the shorts. What happens?", "opts": ["A loss of 20%", "The broker waives the requirement", "Nothing, because the shorts hedge it", "A loss of $819,516, 82% of equity, leaving $180,484 against a recomputed requirement of $266,723: a margin call of about $86,000 that must be met with new cash or by liquidating into the gap"], "correct": 3, "explain": "The same gap at 1x gross costs 20.5% and leaves $728,440 of excess. Leverage does not change the book's direction; it multiplies the loss by the gross multiple and converts a bad day into an involuntary liquidation."},
    {"q": "Replaying the book's current weights through 2020-02-19 to 2020-03-23 gives a −14.35% loss at 1x gross. At 4x gross the same replay is", "opts": ["−57.4%", "−28.7%", "−14.35%", "−100%"], "correct": 0, "explain": "Four times the positions is four times the P&L: −57.4%. That is a survivable loss for a book that can post the call and a terminal one for a book that cannot, which is why leverage is set by the funding available in a gap and not by what the margin rules permit."},
    {"q": "At a $50M scale, the book's ARKK short would be 55,700 shares against a 30-day average volume of 4.80 million, about 0.12 days to close at 10% of volume. Why does the lesson still call funding, not volume, the binding liquidity constraint for this book?", "opts": ["Because ARKK is illiquid", "Because every position could be closed inside a session at 10% of volume; what cannot be done inside a session is raising cash for a margin call, so the question is where the money comes from on the morning of a gap, not whether the shares can be sold", "Because volume data is unreliable", "Because shorts cannot be covered"], "correct": 1, "explain": "Brunnermeier and Pedersen distinguish market liquidity (can it be sold) from funding liquidity (can the position be financed). For a large-cap book the second binds first, and it binds hardest when the first is also deteriorating."}
  ],
  "task": "Compute your book's Reg T and portfolio-margin requirements, then write down, in dollars and hours, where the cash for a call equal to 20% of equity would come from."
}
---

## Leverage is a funding decision

At the position level, leverage is a sizing question. At the book level it is a funding question: who lends you the difference between what you own and what you have, on what terms, and what happens on the day those terms are enforced. The margin rules answer the first two parts. Only you can answer the third, and the third is what decides whether a bad day is a loss or an ending.

The two regimes in US equities are Regulation T and portfolio margin. They produce very different permitted leverage for the same book, and understanding why is the point of this lesson.

## Regulation T and FINRA 4210

Regulation T, the Federal Reserve's rule, sets initial margin at 50% of the market value of any long or short equity position. A book with $1,000,000 of equity can therefore hold at most $2,000,000 of gross positions at initiation, whatever their risk.

FINRA Rule 4210 sets maintenance: 25% of long market value and, for shorts at $5 or above, 30% of short market value. Most brokers apply house minimums above these, commonly 30% and 35%. When equity falls below the maintenance requirement the broker issues a call, which must be met promptly, and the broker retains the right to liquidate without notice.

Reg T is strategy-blind. A hedged long-short book and a naked long book of the same gross are treated identically.

## Portfolio margin

Portfolio margin, permitted under FINRA 4210(g) for accounts above $100,000 (most brokers require more), replaces the fixed percentages with a stress test. Positions are grouped by underlying, each group is revalued across a set of price shocks, and the requirement is the largest loss across the shocks, netted across the book. For broad-based index products and their components the shock range is roughly ±15%; for narrower groups it is wider.

Because the shocks are applied to the whole book at once, a short that offsets a long reduces the requirement. The permitted leverage is then large: for a book whose longs and shorts move together, the worst-case loss across ±15% can be a tenth of its gross or less. Portfolio-margin deficiencies must be met within three business days under the rule, and the broker may act sooner.

The important subtlety: the requirement is computed on shocks of ±15%. The book's positions moved −32% to −48% in five weeks in 2020. The margin rule does not require you to fund the crisis; it requires you to fund a moderate day, and it lends you the difference.

## Funding a call in a gap

A margin call is met with cash or by reducing positions. On the morning of a gap, cash from outside must already be at the broker or be wired inside the day; positions must be sold into the gap, at the prices the gap made. Neither is a plan unless it was arranged before.

The questions to answer in writing: how much unencumbered cash sits at the broker; how much can be wired from elsewhere and by what time; which positions would be sold first and what they would fetch at 10% of their average volume in one session; and, if the answer to all of these is smaller than the call implied by lesson 5's stress VaR at the book's current gross, the gross is too high.

## Worked example

The course book: long market value $899,403, short market value $249,985, equity $1,000,000, gross 114.9%. Prices at the 2026-09-23 close.

**Reg T.** Initial requirement = 0.5 × (899,403 + 249,985) = **$574,694**. Excess = 1,000,000 − 574,694 = $425,306. Maintenance at the FINRA minimums = 0.25 × 899,403 + 0.30 × 249,985 = 224,851 + 74,996 = **$299,846**. Maximum gross this equity could support at initiation: 200%.

**Portfolio margin.** Treat the book as one broad-index group and shock the whole thing by −15% to +15% in ten steps. The worst case for a net-long book is the −15% shock: longs lose 0.15 × 899,403 = $134,910; shorts gain 0.15 × 249,985 = $37,498; net loss **$97,413**, 9.7% of equity. That is the requirement. Against Reg T's 57.5%, the same book ties up a sixth of the capital.

**A gap at 1x.** Longs −8%, shorts +4% (adverse on both legs). Loss = 0.08 × 899,403 + 0.04 × 249,985 = 71,952 + 9,999 = **$81,952**, 8.2% of equity. Equity after: $918,048. Reg T maintenance on the new values: 0.25 × 827,451 + 0.30 × 259,984 = **$284,858**; excess $633,190. Portfolio-margin requirement recomputed: 0.15 × (827,451 − 259,984) = $85,120; excess $832,928. No call under either regime. A 1.15x-gross book absorbs a bad gap with room.

**The same book at 4x gross under portfolio margin.** Long $3,597,612, short $999,940, gross 460%, still on $1,000,000 equity. Requirement = 0.15 × (3,597,612 − 999,940) = **$389,651**, 39% of equity. Permitted, with $610,349 of excess.

Gap 1, longs −8% / shorts +4%: loss 287,809 + 39,998 = **$327,807**, 32.8% of equity. Equity $672,193. Requirement on the shrunken book 0.15 × (3,309,803 − 1,039,938) = $340,480. Excess $331,714. No call, but a third of the capital is gone on a day that at 1x was an 8% loss.

Gap 2, longs −15% / shorts +8%: loss 539,642 + 79,995 = **$619,637**, 62.0% of equity. Equity $380,363. Requirement $296,705. Excess $83,658. No call, by $84,000, with 38% of the capital left.

Gap 3, longs −20% / shorts +10%: loss 719,522 + 99,994 = **$819,516**, 82.0% of equity. Equity $180,484. Requirement 0.15 × (2,878,090 − 1,099,934) = $266,723. **Deficiency $86,240.** The call must be met within three business days with cash, or by liquidating roughly $575,000 of net exposure (86,240 ÷ 0.15) into a market that has just gapped 20%.

**The 2020 replay.** Current weights held from 2020-02-19 to 2020-03-23 lost 14.35% at 1x gross (lesson 5). At 4x gross: **−57.4%**. The March 2020 path was not a single gap; it was 23 sessions of them, with calls arriving daily and positions being sold into each one. A book at 4x would have been liquidated by the broker well before the low.

**Market liquidity.** Thirty-day average daily volume to 2026-09-23 (Yahoo), and days to close each position at 10% of that volume, at $1M and at $50M of equity with the same weights:

At $1M, every position is under 0.03% of its ADV and closes inside minutes. At $50M: NVDA 33,250 shares vs ADV 121.9M, 0.003 days; MSFT 12,000 vs 21.7M, 0.01; AMZN 22,050 vs 33.9M, 0.01; JPM 17,800 vs 6.75M, 0.03; XOM 31,000 vs 14.5M, 0.02; UNH 12,100 vs 4.80M, 0.03; COST 4,950 vs 1.98M, 0.02; GLD 15,250 vs 11.0M, 0.01; IWM 26,600 vs 19.8M, 0.01; ARKK 55,700 vs 4.80M, **0.12 days**. Even at fifty times the size, the whole book closes inside one session. The binding constraint is not whether the shares can be sold; it is what they fetch on the day and where the cash for the call comes from.

## Table

| Regime and gross | Requirement | % of equity | Excess at start | Gap −8% / +4%: loss | Gap −20% / +10%: loss | Call? |
|---|---|---|---|---|---|---|
| Reg T, 1.15x | $574,694 initial; $299,846 maint. | 57.5% / 30.0% | $425,306 | $81,952 (8.2%) | $204,879 (20.5%) | No |
| Portfolio margin, 1.15x | $97,413 | 9.7% | $902,587 | $81,952 (8.2%) | $204,879 (20.5%) | No |
| Portfolio margin, 4.6x | $389,651 | 39.0% | $610,349 | $327,807 (32.8%) | $819,516 (82.0%) | Yes: $86,240 deficiency |

Book as of 2026-09-23: long $899,403, short $249,985, equity $1,000,000. Portfolio-margin requirement approximated as the −15% index shock on the net long. Reg T maintenance at FINRA minimums (25% long, 30% short).

## Setting the gross

The margin rule says what is permitted. The gross is set by a different calculation: the largest loss the stress test in lesson 5 produces at this gross, plus the funding available to meet the resulting call, must leave the book alive with enough equity to continue. For this book, the stress VaR was $42,357 at 1.15x gross on a one-day horizon; the 2020 replay was −14.35% over five weeks. At 2x gross those become $73,700 and −25%; at 4x, $147,000 and −57%. The line is drawn where the multi-week number is survivable with the cash you actually have, and for most books that is between 1.5x and 2.5x, well inside what portfolio margin would permit.

Three rules for the risk document. Gross is capped by the stress replay, not by the broker. Unencumbered cash equal to the one-day stress VaR times three sits at the broker at all times. And the liquidation order is written down in advance, most liquid and least loved first, so that the decision on the morning of the gap has already been made.

## Sources

- FINRA Rule 4210, Margin Requirements. https://www.finra.org/rules-guidance/rulebooks/finra-rules/4210
- Regulation T, 12 CFR Part 220, Board of Governors of the Federal Reserve System. https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-220
- Brunnermeier, M. K. and Pedersen, L. H. (2009). "Market Liquidity and Funding Liquidity." *Review of Financial Studies* 22(6). https://doi.org/10.1093/rfs/hhn098
- Yahoo Finance historical data (volume), the ten book tickers. https://finance.yahoo.com/quote/ARKK/history/
