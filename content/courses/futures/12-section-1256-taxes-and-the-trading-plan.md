---
{
  "title": "Section 1256 Taxes (60/40) and Building the Futures Trading Plan",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Under Section 1256, a net gain on ES futures held for two hours is treated as:", "opts": ["100% short-term capital gain", "60% long-term and 40% short-term capital gain, regardless of holding period", "Ordinary income", "Tax-free"], "correct": 1, "explain": "The Form 6781 instructions state that gains and losses on section 1256 contracts are treated as 60% long-term and 40% short-term regardless of how long the contract was held."},
    {"q": "You are long one ES on December 31 with an unrealised gain of $3,000. For tax purposes:", "opts": ["Nothing is recognised until you close", "The contract is treated as sold at fair market value on the last business day of the year and the $3,000 is included in that year's 1256 result", "It is taxed as ordinary income", "It is deferred to the year you close"], "correct": 1, "explain": "Section 1256 contracts are marked to market at year end: open positions are treated as sold at FMV on the last business day of the tax year."},
    {"q": "On which form are Section 1256 gains and losses reported first?", "opts": ["Form 8949", "Schedule C", "Form 6781, Part I, then carried to Schedule D", "Form 1099-B only"], "correct": 2, "explain": "Form 6781 (Gains and Losses From Section 1256 Contracts and Straddles) computes the 60/40 split on lines 8 and 9; the results flow to Schedule D."},
    {"q": "What does the net section 1256 contracts loss election (box D on Form 6781) allow?", "opts": ["Deducting the loss as ordinary income", "Carrying the loss back three years against prior section 1256 gains", "Ignoring the mark-to-market rule", "Converting the loss to long-term"], "correct": 1, "explain": "An individual may elect to carry a net section 1256 loss back three years, but only to offset section 1256 gains in those years, subject to the limits in the instructions."},
    {"q": "Which item does NOT belong in a written futures trading plan?", "opts": ["The CME initial margin for each contract you trade and the date you last checked it", "The broker's expiry liquidation dates for the next two quarterly contracts", "A profit target for the year expressed as a percentage return", "The daily loss limit in dollars"], "correct": 2, "explain": "A plan contains rules you control: sizing, limits, dates, procedures. A return target is an outcome you do not control and tends to push size up when the target is behind schedule."}
  ],
  "task": "Draft the one-page plan using the table in this lesson, fill every row with a number or a date, and give a copy to someone who will ask you about it in a month."
}
---

## Why futures are taxed differently

U.S. tax law places regulated futures contracts in a category of their own. Section 1256 of the Internal Revenue Code covers, per the Form 6781 instructions, any "regulated futures contract, foreign currency contract, nonequity option, dealer equity option, or dealer securities futures contract." ES, NQ, MES, MNQ, CL, ZN and ZB are all regulated futures contracts: they trade on a qualified board or exchange (CME, NYMEX, CBOT) and are subject to daily mark-to-market by the clearinghouse. Two rules follow, and both are unlike anything in a stock account.

This lesson is a survey. It is not tax advice; it tells you which rules exist and where the IRS states them, so that you and your preparer are reading the same page.

## Rule one: the 60/40 split

Gains and losses on section 1256 contracts are treated as **60% long-term and 40% short-term capital gain or loss, regardless of how long you held the contract**. Form 6781 does the arithmetic on its face: line 8 multiplies the net by 40% for the short-term portion and line 9 by 60% for the long-term portion, and both are carried to Schedule D. A day trader in ES who never holds past the close still gets 60% of net gains taxed at long-term capital gains rates. A day trader in SPY does not; every gain is short-term.

Losses split the same way. A net 1256 loss is 60% long-term and 40% short-term capital loss, subject to the usual capital-loss rules.

## Rule two: mark-to-market at year end

Every section 1256 contract open on the last business day of your tax year is treated as sold at its fair market value on that day, per Publication 550 and the Form 6781 instructions. The unrealised gain or loss on December 31 is included in that year's result, and your basis is adjusted so it is not counted twice when you actually close. Your futures broker reports this on Form 1099-B, in the section 1256 boxes, as an aggregate profit or loss for the year that already includes the year-end mark. You do not list trades individually; the aggregate goes on Form 6781 line 1.

Two side effects. The wash-sale rule, which defers losses on stock repurchased within 30 days, does not apply to section 1256 contracts, because mark-to-market makes it unnecessary. And because open positions are marked, you cannot defer a gain into next year by holding through December 31.

## The loss carryback election

An individual with a **net section 1256 contracts loss** may elect, by checking box D on Form 6781, to carry the loss back three years, but only against section 1256 gains in those years and only to the extent it does not create or increase a net operating loss. The election is made on the return for the loss year and requires amended returns for the carryback years. It is one of the few places in the individual tax code where a current loss can recover tax already paid.

## Worked example

Illustrative rates, not a projection: assume a taxpayer whose marginal ordinary rate is 32% and whose long-term capital gains rate is 15%, with $10,000 of net trading gain for the year and no other capital transactions. Check your own brackets; the point is the mechanism.

Case A, $10,000 net gain from day-trading SPY shares. All short-term. Tax = $10,000 x 32% = $3,200.

Case B, $10,000 net gain from day-trading MES, reported on the 1099-B section 1256 aggregate. Form 6781 line 7: $10,000. Line 8 (40% short-term): $4,000; tax at 32% = $1,280. Line 9 (60% long-term): $6,000; tax at 15% = $900. Total tax = $2,180. Difference from Case A: $1,020, or 10.2 percentage points of the gain, from the contract type alone.

Case C, same year, but on December 31 the trader also holds two MES bought at 7,700.00 and the year-end fair market value (the settlement) is 7,772.50. Mark-to-market gain = (7,772.50 - 7,700.00) x $5 x 2 = 72.50 x $10 = $725.00, included in the year's aggregate even though the position is open. Line 7 becomes $10,725; short-term portion $4,290 (tax $1,372.80); long-term $6,435 (tax $965.25); total $2,338.05. When the position is closed in January at, say, 7,800.00, only the gain from 7,772.50 onward, (7,800.00 - 7,772.50) x $10 = $275.00, is next year's income.

Case D, a bad year: $8,000 net section 1256 loss, with $5,000 of section 1256 gains reported three years earlier. Electing box D, the trader may carry $5,000 of the loss back to that year and file an amended return for a refund of the tax paid on it; the remaining $3,000 is deducted currently within the capital-loss limits.

## From rules to a plan

A futures trading plan is a document that answers, before the market opens, every question this course has raised. It contains numbers and dates, not intentions. The test of a plan is whether a stranger could run your account from it for a week without asking you anything.

The rows below are the minimum. Fill each with a value from the sources named in the earlier lessons and put the date you checked it next to the value; margins, roll dates and holiday hours all change.

## Table

| Section | Rule to write down | Where the number comes from |
|---|---|---|
| Products | Which contracts you trade (e.g. MES only until equity exceeds $50,000) | Lesson 2 specs |
| Multiplier and tick | $ per point and $ per tick for each | CME spec pages |
| Exchange margin | Initial and maintenance per contract, with the date checked | CME margins pages, Lessons 3 and 4 |
| Overnight capacity | Max contracts that fit initial margin with 50% of equity free | Lesson 11 |
| Risk per trade | $ and % of equity (e.g. $250, 1%) | Lesson 11 |
| Daily loss limit | $ and %; action when hit (flat, platform closed) | Lesson 11 |
| Sizing formula | contracts = risk / (stop points x $ per point), rounded down | Lesson 11 |
| Sessions | Hours you trade; whether you hold through 6 p.m. to 4 a.m. ET; sizing rule for overnight | Lesson 7 |
| Events | Releases you will be flat for (8:30 a.m. data, FOMC, EIA Wednesday) | Lessons 8 and 9 |
| Orders | Entry type; exit always a bracket with server-held stop; no stop-limit as sole exit | Lesson 10 |
| Roll | Roll date and broker liquidation date for the next two quarters; roll via calendar spread | Lesson 6 |
| Expiry | Last trading day and, for physical contracts, first notice day | Lessons 8 and 9 |
| Term structure check | Note the front spread before any position held past a roll | Lesson 5 |
| Records | Keep the 1099-B, Form 6781 and a trade log with date, contract, size, stop, result | This lesson |
| Review | Weekly: compare every trade to the plan; monthly: recheck margins and dates | — |

## Sources

- IRS, About Form 6781, Gains and Losses From Section 1256 Contracts and Straddles — https://www.irs.gov/forms-pubs/about-form-6781
- IRS, Form 6781 and instructions (PDF) — https://www.irs.gov/pub/irs-pdf/f6781.pdf
- IRS, Publication 550, Investment Income and Expenses (Section 1256 Contracts Marked to Market) — https://www.irs.gov/publications/p550
- CME Group, E-mini S&P 500 margins — https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.margins.html
