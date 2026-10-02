---
{
  "title": "The Wash-Sale Rule: Section 1091 and the 61-Day Window",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "You sell 100 shares at a loss on 2025-04-04. The wash-sale window runs:", "opts": ["From 2025-03-05 to 2025-05-04, 30 days before and 30 days after plus the sale day", "From 2025-04-04 to 2025-05-04 only", "For the rest of the calendar year", "For 60 days after the sale"], "correct": 0, "explain": "IRC section 1091(a) disallows the loss if substantially identical stock or securities are acquired within a period beginning 30 days before the date of the sale and ending 30 days after that date, a 61-day window including the sale day."},
    {"q": "A wash-sale loss that is disallowed is:", "opts": ["Lost permanently in every case", "Added to the basis of the replacement shares, and the old holding period is added to the new one", "Deductible in the following year automatically", "Reported as a long-term loss"], "correct": 1, "explain": "Section 1091(d) and Pub. 550: add the disallowed loss to the cost of the new stock, and the holding period of the new stock includes the holding period of the stock sold. The exception is a replacement bought in an IRA, where Pub. 550 says the loss cannot be added to basis."},
    {"q": "Which of the following purchases within the window does NOT trigger the rule for a loss on XYZ common stock?", "opts": ["Your spouse buys XYZ common", "You buy an XYZ call option", "You buy XYZ in your Roth IRA", "You buy common stock of a different, unrelated company in the same industry"], "correct": 3, "explain": "Pub. 550: stocks of one corporation are ordinarily not substantially identical to stocks of another. A spouse's purchase, a contract or option to acquire, and a purchase in your IRA or Roth IRA are all listed as triggering the rule."},
    {"q": "Your broker's Form 1099-B box 1g shows no disallowed wash-sale loss. You sold at a loss in one account and rebought the same stock in another account at the same broker within 30 days. Which is correct?", "opts": ["The loss is allowed because the broker did not report it", "The loss is allowed because the accounts are separate", "The loss is still disallowed; brokers are only required to report wash sales within the same account and CUSIP, and you must apply the rule yourself on Form 8949 with code W", "The loss is halved"], "correct": 2, "explain": "Pub. 550: box 1g shows the disallowed loss only when the sale and purchase were in the same account with the same CUSIP; however, you cannot deduct a loss from a wash sale even if it is not reported on Form 1099-B."},
    {"q": "You sell 100 shares at a $10,765 loss and buy back 40 shares within the window. How much of the loss is disallowed?", "opts": ["All $10,765", "None, because fewer shares were repurchased", "$6,459", "$4,306, the portion matched to the 40 shares repurchased"], "correct": 3, "explain": "Section 1091(b) and Pub. 550, More or less stock bought than sold: match the shares bought with an equal number of the shares sold. 40 of 100 shares are matched, so 40% of the loss, $4,306, is disallowed and $6,459 is deductible."}
  ],
  "task": "List every account you or your spouse control, including IRAs and any account at a second broker, because a wash-sale check has to run across all of them."
}
---

## What the statute says

IRC section 1091(a) is short. If you sell stock or securities at a loss and, within a period beginning 30 days before the date of the sale and ending 30 days after that date, you acquire substantially identical stock or securities, or enter into a contract or option to acquire them, no deduction is allowed for the loss. The only exception is a dealer in securities acting in the ordinary course of business. The window is therefore 61 days: 30 before, the sale day, 30 after. It is measured in calendar days, not trading days, and the acquisition on either side of the sale counts.

Two features of the statute surprise traders. First, the rule looks backwards as well as forwards: shares bought on 2025-03-20 can disallow a loss on other shares of the same stock sold on 2025-04-04, even though the purchase came first. Publication 550's Example 1 under More or less stock bought than sold is exactly this fact pattern. Second, the rule applies to losses only. A gain inside the window is fully taxable; there is no symmetry.

## Disallowed is not destroyed

Section 1091(d) supplies the second half of the rule. The basis of the replacement shares is the basis of the shares sold, increased or decreased by the difference between the two prices. In plain terms: add the disallowed loss to the cost of the new shares. Publication 550 adds that the holding period of the new shares includes the holding period of the shares sold. The loss is postponed, not lost, and you recover it when you finally sell the replacement outside any window. The cost of a wash sale is therefore timing: the loss you wanted this year arrives whenever the replacement position is closed, and the tacked holding period can also turn what would have been a short-term gain on the replacement into a long-term one.

The exception, and the one place a loss really is destroyed, is an IRA. Publication 550 lists acquiring substantially identical stock for your traditional or Roth IRA as a trigger and says the basis adjustment does not apply in that case (Rev. Rul. 2008-5 is the underlying ruling). The loss disappears because the IRA has no basis to adjust.

## Across accounts, spouses and options

The statute speaks of the taxpayer, and Publication 550 makes the perimeter explicit. A purchase in any account you own counts, including a second broker and your IRA. If you sell stock and your spouse, or a corporation you control, buys substantially identical stock, you also have a wash sale. Acquiring a contract or option to buy the stock counts as acquiring the stock, so selling shares at a loss and buying a call inside the window is a wash sale, and section 1091(f) says the rule still applies when the contract settles in cash. Section 1091(e) applies similar rules to closing a short sale at a loss when substantially identical stock is sold, or another short sale entered into, within the window.

Brokers report only part of this. The Form 1099-B instructions require box 1g, wash sale loss disallowed, only when the sale and the purchase occurred in the same account in covered securities with the same CUSIP number; reporting across accounts is permitted but not required. Publication 550 is blunt: you cannot deduct a loss from a wash sale even if it is not reported on Form 1099-B. The reconciliation is yours, and lesson 12 shows where it goes on Form 8949 (code W in column (f), the disallowed amount as a positive number in column (g)).

## Substantially identical

The Code does not define the phrase and the IRS has not published a bright-line test for funds. Publication 550 says you must consider all the facts and circumstances, that stocks or securities of one corporation are ordinarily not substantially identical to those of another, and that bonds or preferred stock of the same company are not ordinarily identical to its common unless convertible on terms that make them trade together. Options and the underlying stock are treated as identical for the purpose of the acquisition trigger. What Publication 550 does not address is two exchange-traded funds that track the same index from different sponsors, or a fund and a different index fund with overlapping holdings. Practitioners disagree; the safest reading treats same-index funds as substantially identical and different-index funds as not, and lesson 4 works through the replacement choice with that uncertainty in view. Publication 550 states plainly that the wash-sale rules do not apply to losses on commodity futures contracts and foreign currencies, which is why section 1256 contracts (lesson 5) are outside the rule.

## Worked example

You bought 100 SPY on 2025-02-19 at the Yahoo Finance daily close of $612.93, cost $61,293.00. The market fell through March and on 2025-04-04 you sold at the close of $505.28, proceeds $50,528.00, for a loss of $10,765.00. Held 44 days, so short-term.

The window runs from 2025-03-05 (30 days before) to 2025-05-04 (30 days after). On 2025-04-24 the market had rebounded and you bought 100 SPY back at the close of $546.69, cost $54,669.00. That purchase is inside the window and the shares are the same security, so section 1091(a) disallows the entire $10,765.00 loss for 2025.

Basis of the replacement shares under section 1091(d): $54,669.00 + $10,765.00 = $65,434.00. Holding period: the replacement shares are treated as held since the original lot's holding period began, 2025-02-20.

On 2025-12-01 you sold the replacement shares at the close of $680.27, proceeds $68,027.00. Gain on the adjusted basis: $68,027.00 − $65,434.00 = $2,593.00. Without the adjustment the gain would have been $68,027.00 − $54,669.00 = $13,358.00; the $10,765.00 difference is the deferred loss arriving. Holding period with tacking: 2025-02-20 through 2025-12-01, still under one year, so short-term. Over the two trades your economic result was −$10,765.00 + $13,358.00 = $2,593.00, and that is exactly the taxable gain. Nothing was lost; the loss simply could not be claimed in a year when you were still long the same exposure.

Partial repurchase. Had you bought back only 40 shares on 2025-04-24, section 1091(b) and Publication 550 match them to 40 of the 100 shares sold: 40% of the loss, $4,306.00, is disallowed and added to the basis of the 40 new shares ($21,867.60 + $4,306.00 = $26,173.60), and the other $6,459.00 is deductible in 2025.

Had you instead waited until 2025-05-05, one day after the window closed, to rebuy, the full $10,765.00 would have been deductible in 2025, subject to the netting rules of lesson 2.

## Chart

![The 61-day wash-sale window around the 2025-04-04 sale of 100 SPY: window opens 2025-03-05, sale at $505.28 (loss $10,765 on shares bought 2025-02-19 at $612.93), repurchase 2025-04-24 at $546.69 inside the window (basis becomes $65,434 and the holding period tacks), window closes 2025-05-04, and the deferred loss is recognised when the replacement is sold 2025-12-01 at $680.27 for a $2,593 gain. Tax year 2025. Sources: IRC section 1091(a) and (d); Yahoo Finance daily closes.](figures/wash-sale-61-day-window.svg)

## Where traders get caught

Active traders in a single name trigger the rule constantly, and the broker's box 1g will show a stream of small disallowed losses that are recovered as long as the position is eventually closed and stays closed for 31 days. The dangerous cases are the ones the broker cannot see: a loss in a taxable account matched to an automatic dividend reinvestment in an IRA holding the same fund; a loss on shares while a covered call you wrote is assigned and shares are called away, then rebought; a loss in your account while your spouse's account holds a standing buy order in the same stock; and year-end losses taken in late December with a January repurchase, which defer the loss out of the year you needed it. Lesson 7 covers the one legal exit from the rule for a trading business, the section 475(f) election, under which section 475(d)(1) switches off wash-sale treatment for securities held in the trading business.

## Sources

- IRC section 1091, Loss from wash sales of stock or securities: https://www.law.cornell.edu/uscode/text/26/1091
- IRS Publication 550, Investment Income and Expenses (Wash Sales): https://www.irs.gov/publications/p550
- Instructions for Form 1099-B, Box 1g, Wash Sale Loss Disallowed: https://www.irs.gov/instructions/i1099b
- Instructions for Form 8949, code W: https://www.irs.gov/instructions/i8949
