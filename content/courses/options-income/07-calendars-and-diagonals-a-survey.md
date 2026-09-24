---
{
  "title": "Calendars and Diagonals: A Survey",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The chain's calendar sells the October 9 100 call (17 DTE) at 2.50 and buys the December 18 100 call (87 DTE) at 5.91. What is the position's maximum loss?", "opts": ["5.91", "3.41, the debit paid", "2.50", "Unlimited above 100"], "correct": 1, "explain": "A long calendar is a debit position whose worst case is both options going to zero (a huge move either way, with the back month collapsing); you cannot lose more than the 3.41 paid."},
    {"q": "On October 9 the front call expires and XYZ is at 100. The remaining December call (70 DTE) is worth 5.26. Calendar P&L?", "opts": ["+5.26", "+2.50", "+1.85", "-0.65"], "correct": 2, "explain": "The front expired worthless; the position is the back call alone, worth 5.26, against a 3.41 cost: +1.85 per share, the maximum of the profile at the strike."},
    {"q": "Unlike every other structure in this course, a long calendar has:", "opts": ["Negative theta", "Positive vega, because the long back month has more vega than the short front month", "Unlimited risk", "No assignment risk"], "correct": 1, "explain": "The 87-day option's vega exceeds the 17-day option's, so the calendar gains when implied volatility rises. It is short realised movement (like the condor) but long implied volatility, a different bet."},
    {"q": "A diagonal sells the October 105 call at 0.77 against the December 100 call at 5.91. Compared with the calendar it:", "opts": ["Costs more (5.14), adds a bullish tilt, and leaves 5 points of room for the stock to rise before the short strike", "Costs less and is neutral", "Has unlimited upside risk", "Cannot be assigned"], "correct": 0, "explain": "Debit 5.91 - 0.77 = 5.14. The short call is 5 points higher, so the position wants a modest rise toward 105 and keeps more of the back call's delta."},
    {"q": "Why does this course treat calendars at survey depth rather than as a core income structure?", "opts": ["They are illegal in cash accounts", "Their P&L depends on the term structure of implied volatility between two expirations, which the single-volatility model chain and most retail volatility tools do not show", "They have no theta", "They require portfolio margin"], "correct": 1, "explain": "A calendar is a bet on the front-month IV falling relative to the back-month IV, plus a bet on the stock staying near the strike. Pricing that bet needs two implied volatilities and a view on how they move together."}
  ],
  "task": "On a real chain, price a one-month/three-month at-the-money calendar at its mids, record the implied volatility of each expiration, and note whether the front month is trading above or below the back month."
}
---

## A different kind of premium sale

Everything so far sells time in a single expiration and takes the stock's movement as the risk. A calendar spread sells time in one expiration and buys it in a later one at the same strike. On the chain, with a second, nearer expiration added: sell the October 9, 2026 100 call (17 days) at its model price of 2.50 and buy the December 18, 2026 100 call (87 days) at 5.91. Net debit 3.41. Same strike, different dates.

The front option decays faster than the back one, which is the source of the trade's positive theta, and the back option carries more vega than the front, which makes the position long implied volatility. That second property is what sets calendars apart from every other structure in this course. A covered call, a cash-secured put, a credit spread and a condor all lose when implied volatility rises. A calendar gains. It is short realised movement, because a big move either way ruins it, and long implied movement at the same time.

## The profile at the front expiration

The natural way to read a calendar is at the moment the front option expires, October 9. At that point the position is just the back call, 70 days from expiration, minus whatever the front call is worth in the money.

From the model, with IV unchanged at 28%:

- XYZ 100: front expires worthless; December 100 call worth 5.26; P&L 5.26 - 3.41 = +1.85.
- XYZ 97: back call 3.76; P&L +0.35.
- XYZ 103: back call 7.05, front settles for 3.00; net 4.05; P&L +0.64.
- XYZ 95: back call 2.93; P&L -0.48.
- XYZ 105: back 8.39, front 5.00; net 3.39; P&L -0.02.
- XYZ 90: back 1.40; P&L -2.01. XYZ 110: back 12.20, front 10.00; net 2.20; P&L -1.21.

The shape is a tent centred on the strike, with a peak of +1.85 (54% of the debit) if the stock is exactly at 100 and break-evens near 96 and 105. The maximum loss is the 3.41 paid, and reaching it needs a very large move. Compare the condor: 22 points of flat profit and a cliff. The calendar has a narrow peak and a gentle slope. It wants the stock pinned, and it wants it pinned right now, not merely inside a range.

The numbers above hold implied volatility fixed, and that is the caveat. Reprice the calendar on day one at 24% IV: the model debit falls to 2.98, so the position bought at 3.41 is marked at a 0.43 loss before anything has happened. At 32% the debit would be 3.84, a 0.43 gain. Four volatility points move the calendar by 0.43, nearly a quarter of its maximum profit. On a single-volatility model the effect is symmetric; on a real chain the two expirations have different implied volatilities, and the trade is really a bet that the front month's IV falls relative to the back month's.

## Diagonals

A diagonal is a calendar with different strikes. Sell the October 105 call at 0.77 against the December 100 call at 5.91: debit 5.14. The short call is now 5 points above the long, so the position keeps most of the long call's delta (0.56 minus the short's 0.23, roughly 0.33 net) and profits from a moderate rise toward 105 as well as from time. At the October expiration with XYZ at 103 the back call is worth 7.05, the front expires worthless: P&L 7.05 - 5.14 = +1.91. At 100: 5.26 - 5.14 = +0.12. At 108: back 10.61, front 3.00; net 7.61; P&L +2.47. Below 97 the position loses, as a long call would, but more slowly than a bare long call because the 0.77 sold offsets some decay.

The poor man's covered call is the diagonal taken to its extreme: a deep in-the-money long call six to twelve months out replaces the stock, and short calls are sold against it each month. It behaves like a covered call with less capital and more sensitivity to implied volatility, and it carries a risk the stock version does not: if the short call goes in the money and is assigned, you deliver shares you do not own and your broker exercises or buys against the long call, usually at a worse price than you would have chosen. Treat assignment on any diagonal as a real event to plan for, not a technicality.

## Where calendars fit in an income plan

Calendars and diagonals are useful in two situations. The first is when implied volatility is low by the measures in Lesson 8 and selling premium outright is unattractive: the calendar's long vega turns low IV from a headwind into an entry condition. The second is around known events, where front-month IV is elevated relative to the back month; selling the inflated front against the back is a term-structure trade rather than a directional one, and it needs the two implied volatilities in front of you, not a single number.

What calendars are not is a replacement for the condor or the wheel. They are a different bet, on the shape of the volatility curve between two dates, and the single-volatility chain in this course cannot fully price that bet. That is why the treatment here is a survey: know the structure, price it at the front expiration as above, understand that IV moves it as much as the stock does, and add it to your plan only when you can see both expirations' implied volatilities and have a reason to expect the front to fall relative to the back.

## Worked example

Long 100 calendar on the chain, per share, commissions excluded.

Entry, September 22: sell October 9 100 call at 2.50; buy December 18 100 call at 5.91. Debit 5.91 - 2.50 = 3.41. Maximum loss 3.41.

Greeks at entry from the model: front delta 0.52, back delta 0.56, net +0.04 (near neutral). Front theta faster than back; net positive. Net vega positive (87-day vega exceeds 17-day vega).

October 9, front expiration, IV 28%:

- 100: 5.26 - 0 - 3.41 = +1.85.
- 97: 3.76 - 3.41 = +0.35.
- 103: 7.05 - 3.00 - 3.41 = +0.64.
- 95: 2.93 - 3.41 = -0.48.
- 105: 8.39 - 5.00 - 3.41 = -0.02.
- 92: 1.92 - 3.41 = -1.49.
- 108: 10.61 - 8.00 - 3.41 = -0.80.

Approximate break-evens: between 95 and 97 on the downside (about 96), between 103 and 105 on the upside (about 105).

Volatility sensitivity on day one: at 24% the calendar is worth 2.98 (-0.43); at 32% 3.84 (+0.43).

Diagonal alternative: sell October 105 call at 0.77 against the same December 100 call. Debit 5.14. October 9 at 103: 7.05 - 0 - 5.14 = +1.91. At 100: 5.26 - 5.14 = +0.12. At 108: 10.61 - 3.00 - 5.14 = +2.47. At 95: 2.93 - 5.14 = -2.21.

## Table

Calendar and diagonal at the October 9 front expiration, per share, IV held at 28%. Back-month values are the model's December 100 call with 70 days remaining.

| XYZ on Oct 9 | Dec 100 call (70 DTE) | Oct 100 call settles | 100 calendar P&L (debit 3.41) | Oct 105 call settles | 100/105 diagonal P&L (debit 5.14) |
|---|---|---|---|---|---|
| 90 | 1.40 | 0.00 | -2.01 | 0.00 | -3.74 |
| 95 | 2.93 | 0.00 | -0.48 | 0.00 | -2.21 |
| 97 | 3.76 | 0.00 | +0.35 | 0.00 | -1.38 |
| 100 | 5.26 | 0.00 | +1.85 | 0.00 | +0.12 |
| 103 | 7.05 | 3.00 | +0.64 | 0.00 | +1.91 |
| 105 | 8.39 | 5.00 | -0.02 | 0.00 | +3.25 |
| 108 | 10.61 | 8.00 | -0.80 | 3.00 | +2.47 |
| 110 | 12.20 | 10.00 | -1.21 | 5.00 | +2.06 |

## Sources

- Options Clearing Corporation, *Characteristics and Risks of Standardized Options*, chapter on spreads and early assignment: https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document
- Cboe Global Markets, Options Institute, calendar and diagonal spread reference: https://www.cboe.com/education/
- Cboe Global Markets, Margin Manual (calendar spread requirements): https://www.cboe.com/us/options/strategy_based_margin/
