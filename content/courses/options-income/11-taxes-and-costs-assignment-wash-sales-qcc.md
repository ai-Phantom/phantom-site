---
{
  "title": "Taxes and Costs: Assignment, Wash Sales, Qualified Covered Calls",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Per IRS Publication 550, when a put you wrote is exercised and you buy the shares, the premium you received:", "opts": ["Reduces your cost basis in the shares, and the holding period starts on the purchase date", "Is reported as short-term gain on the assignment date", "Is added to the amount realised when you later sell", "Is ordinary income"], "correct": 0, "explain": "Publication 550, 'Writers of puts and calls': decrease your basis in the stock by the amount received for the put; the holding period begins when you buy the stock, not when you wrote the put. On the chain: 95 - 1.69 = 93.31."},
    {"q": "When a call you wrote against shares is exercised, the premium:", "opts": ["Is short-term gain on the exercise date", "Reduces the basis of the shares", "Is added to the amount realised on the sale of the shares, and the gain's character follows the shares' holding period", "Is deferred until the next tax year"], "correct": 2, "explain": "Publication 550: increase your amount realised on the sale of the stock by the amount received for the call. The wheel's called-away leg realises 95 + 2.88 = 97.88 against a 93.31 basis."},
    {"q": "Which of these calls on shares you hold is NOT a qualified covered call under Publication 550?", "opts": ["The December 18 95 call sold on November 6 with XYZ at 92 (42 days)", "The November 6 105 call sold on September 22 (45 days)", "The October 9 100 call sold on September 22 with XYZ at 100 (17 days)", "The November 6 100 call sold on September 22 (45 days)"], "correct": 2, "explain": "A qualified covered call must be granted more than 30 days before expiration (and not more than 12 months), be exchange-traded, and not be deep in the money. Seventeen days fails the first test, so the straddle rules apply and the shares' holding period is affected."},
    {"q": "You sell 100 XYZ at a loss on November 6 and on November 20 write an XYZ put. Which statement is correct?", "opts": ["No wash sale, because a put is not stock", "Publication 550 says the wash sale rule applies if you enter into a contract or option to acquire substantially identical stock within the 61-day window, and the IRS has treated a deep-in-the-money written put as such a contract; an out-of-the-money put is a grey area to avoid", "Wash sales only apply to purchases of stock", "The put's premium offsets the loss"], "correct": 1, "explain": "Publication 550's wash sale section covers 'a contract or option to acquire' the stock. Revenue Ruling 85-87 applied it to a written put so deep in the money that assignment was near-certain. The safe practice is to wait 31 days or keep the put clearly out of the money."},
    {"q": "Which cost is largest on the chain's 90/85 + 110/115 iron condor at market fills?", "opts": ["Commissions of a few dollars per contract", "Assignment fees", "Margin interest", "The bid/ask toll of about 0.12 per share, 12% of the 1.04 credit, on the way in alone"], "correct": 3, "explain": "Four legs at half the bid/ask each cost 0.03 + 0.02 + 0.04 + 0.03 = 0.12, or $12 per condor per side; closing early costs a similar amount again. Per-contract commissions are usually smaller; assignment fees only apply if a leg is assigned."}
  ],
  "task": "Find your broker's fee schedule and write down the per-contract commission, the exercise and assignment fee, and whether it charges for expiring options, then compute the round-trip cost of the chain's condor at your rates."
}
---

## What this lesson does and does not do

This is a survey of the United States federal rules that change a premium seller's after-tax result, drawn from IRS Publication 550 (2025 edition), and of the trading costs that change the before-tax one. It is not tax advice, it is not state tax, and the rules have exceptions the publication spells out. Read the sections named here in the publication itself before filing anything.

Nothing here changes the arithmetic of earlier lessons; it changes what you keep.

## How the writer's premium is taxed

Publication 550, "Writers of puts and calls", sets four outcomes. You do not report the premium when you receive it; it sits in a deferred account until one of these happens.

**The option expires.** The premium is short-term capital gain on the expiration date, regardless of how long you were short. The chain's 95 put expiring on November 6 with XYZ at 97 is a $169 short-term gain dated November 6.

**You close it.** The difference between the premium received and the cost to close is short-term gain or loss on the closing date. Buying the November 95 put back at 5.28 on October 16 (Lesson 9) is a $359 short-term loss dated October 16, and the roll's new leg starts its own deferred account.

**A put is assigned.** No gain or loss is recognised on the option. The premium reduces the basis of the shares you buy, and the shares' holding period starts on the assignment date, not the date you wrote the put. Chain: assigned at 95 after collecting 1.69, basis 93.31.

**A call is assigned.** No gain or loss on the option. The premium increases the amount realised on the shares, and the gain or loss on the shares is long- or short-term by the shares' holding period. Chain wheel: called at 95 after collecting 2.88, amount realised 97.88; against basis 93.31 the gain is 4.57 per share, $457, short-term because the shares were held from November 6 to December 18.

The holder's side, which you learned in the previous course, is the mirror: a purchased option that expires is a loss on the expiration date, an exercised call adds its cost to the shares' basis, an exercised put reduces the amount realised.

## Qualified covered calls

Writing a call against shares you hold is, in tax terms, an offsetting position: a straddle. The straddle rules can defer losses and, more importantly for income sellers, suspend the shares' holding period, so that stock held eleven months never becomes long-term while a call is written against it. Congress carved out an exception for ordinary covered calls, the **qualified covered call**, and Publication 550 gives its conditions:

- The option is traded on a national securities exchange.
- It is granted more than 30 days before expiration and (for options entered into after July 28, 2002) not more than 12 months before, or meets the term and benchmark rules published in the Internal Revenue Bulletin.
- It is not deep in the money: its strike is not lower than the **lowest qualified benchmark (LQB)**, the highest available strike below the stock's price at the time the option is written. For options with more than 90 days to expiration and a strike above $50, the LQB is the second-highest strike below the stock price.
- You are not an options dealer writing it in that capacity, and gain or loss on it is capital.

On the chain: the November 105 and 100 calls (45 days) and the December 95 call written November 6 with XYZ at 92 (42 days) are all qualified; the October 9 100 call (17 days) is not. A December 90 call written with XYZ at 92 has a strike equal to the LQB (90 is the highest listed strike below 92), so it is not deep in the money and is qualified; a December 85 would not be. If you write a qualified covered call that is in the money, Publication 550 adds a further rule: any loss on the option is long-term if the shares' gain would be long-term, and the shares' holding period excludes the period you were the writer.

The practical rule for the wheel: sell calls with more than 30 days to expiration at or above the LQB, which the at-or-above-basis rule from Lesson 4 almost always satisfies, and never write a short-dated call against shares approaching a year of holding.

## Wash sales with options

The wash sale rule disallows a loss on stock or securities if you buy substantially identical stock or securities within 30 days before or after the sale. Publication 550 extends it in two directions that matter here. First, "the wash sale rules apply to losses from sales or trades of contracts and options to acquire or sell stock or securities": closing an XYZ put at a loss and writing another XYZ put of the same strike and expiration a week later can be a wash sale on the option. Second, the rule applies "if you entered into a contract or option to acquire the stock or securities" within the window, so selling shares at a loss and buying a call, or writing a put deep enough in the money that acquisition is nearly certain (Revenue Ruling 85-87), can disallow the stock loss.

Disallowed losses are not lost; they are added to the basis of the replacement position and deferred. For an income seller who is constantly re-entering the same names, that deferral can push losses from December into January every year. The clean practices: wait 31 days after a loss sale before writing puts on that name, keep written puts out of the money, and do not roll a losing option into the same strike and expiration on a different date as a way of "resetting".

## Index options and Section 1256

Options on broad-based indexes such as SPX are nonequity options and Section 1256 contracts. They are marked to market at year-end and any gain or loss is 60% long-term and 40% short-term regardless of holding period (Publication 550, "Section 1256 Contracts Marked to Market"). Equity and ETF options, XYZ's among them, are not. The same premium on an index carries a lower federal rate for most sellers, and the cash settlement removes assignment entirely. That is one reason the Cboe benchmarks from Lessons 1 to 3 are built on SPX, and one factor in choosing where to run an income plan.

## The cost side

Before tax, three costs recur. The **bid/ask toll** is the largest and the least visible: half the spread on each leg, each way. On the chain, the 95/90 put spread costs 0.08 to open at half-spreads (7% of its 1.08 credit) and about the same to close; the four-leg condor costs 0.12 (12% of 1.04). Far out-of-the-money legs have the widest relative spreads, which is why the 90/85 spread in Lesson 5 gave up 11% of its credit. **Commissions** are per contract and per leg; they are small on liquid names and large as a fraction of a 0.16 wing. **Assignment and exercise fees** are charged by some brokers per event; a wheel takes assignment on roughly one cycle in three and should budget for it. Interest on cash-secured collateral is a credit, not a cost, and should be recorded.

None of these is optional and all belong in the plan's ledger (Lesson 12) at the rates your own broker charges.

## Worked example

The Lesson 4 wheel cycle, tax and cost lines. Per contract.

Leg 1: November 95 put written September 22 for 1.69. Assigned November 6 with XYZ 92.00. No gain or loss on the option. Shares: 100 at 95.00, basis reduced by 1.69 to 93.31 ($9,331). Holding period starts November 6.

Leg 2: December 18 95 call written November 6 for 2.88, XYZ 92.00. Qualified covered call check: exchange-traded, yes; 42 days to expiration, more than 30 and less than 12 months, yes; strike 95 versus LQB 90 (highest strike below 92.00; the option has 90 days or fewer so the second-highest rule does not apply), not deep in the money, yes. Qualified; holding period continues.

Called away December 18 at 95.00: amount realised 95.00 + 2.88 = 97.88 ($9,788). Gain 97.88 - 93.31 = 4.57 ($457). Holding period November 6 to December 18, 42 days: short-term capital gain of $457 reported on the December 18 sale. No separate option line.

Alternative: call expires December 18 with XYZ at 92. Report $288 short-term gain on December 18. Shares still held at basis 93.31, holding period intact.

Alternative: the October 9 100 call written September 22 (17 days) against shares. Not qualified. Straddle rules apply; if the shares were held less than a year, the holding period is affected for the period of the straddle.

Wash sale check: on December 18 you sell shares at a loss of 1.31 (92.00 versus 93.31) and on December 23 write a January 92 put. The put is at the money, not deep in the money; Revenue Ruling 85-87 addressed a deep-in-the-money put. Grey area; the safe course is to write the put on January 19 or later.

Costs on the cycle at half-spread fills: 95 put bid/ask 1.64 / 1.74, toll 0.05 ($5); the December call, assume a 0.10 spread, toll 0.05 ($5); commissions and any assignment fee at your broker's schedule. The Lesson 6 condor: opening toll $12, closing toll about $12, four commissions each way.

## Table

Tax treatment of each outcome for the option writer, from Publication 550, "Writers of puts and calls", with the chain's numbers.

| Event | Option gain or loss | Effect on shares | Character | Chain example |
|---|---|---|---|---|
| Written option expires | Premium is gain on expiration date | None | Short-term | November 95 put expires: +$169 on Nov 6 |
| Written option closed | Premium minus closing cost | None | Short-term | 95 put bought back at 5.28 on Oct 16: -$359 |
| Written put assigned | None | Basis = strike - premium; holding period starts at assignment | Follows shares | Basis 95 - 1.69 = 93.31 from Nov 6 |
| Written call assigned | None | Amount realised = strike + premium | Follows shares' holding period | 95 + 2.88 = 97.88; gain $457 short-term |
| Non-qualified covered call (30 days or fewer, or deep ITM) | As above | Straddle rules; holding period affected | Per straddle rules | October 9 100 call, 17 days |
| Broad-index option (SPX) | Marked to market at year-end | Cash-settled, no shares | 60% long-term / 40% short-term | Not applicable to XYZ |

## Sources

- Internal Revenue Service, Publication 550 (2025), *Investment Income and Expenses*, chapter 4: "Writers of puts and calls", "Wash Sales", "Qualified covered call options and optioned stock", "Section 1256 Contracts Marked to Market": https://www.irs.gov/publications/p550
- Internal Revenue Service, Revenue Ruling 85-87, 1985-1 C.B. 268 (written put as a contract to acquire stock for wash sale purposes): https://www.irs.gov/irb
- Options Clearing Corporation, *Characteristics and Risks of Standardized Options*, chapter on transaction costs and tax considerations: https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document
