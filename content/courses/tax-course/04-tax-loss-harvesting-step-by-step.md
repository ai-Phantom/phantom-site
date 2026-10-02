---
{
  "title": "Tax-Loss Harvesting Step by Step, With the Replacement Question",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Harvesting a loss in a taxable account primarily does which of the following?", "opts": ["Eliminates the tax on the position permanently", "Creates a refundable credit", "Reduces the NIIT threshold", "Defers tax by resetting your basis lower, and can convert a short-term loss now into a long-term gain later"], "correct": 3, "explain": "The harvested loss offsets gains or up to $3,000 of ordinary income now (IRC section 1211(b)), but the replacement position starts at a lower basis, so the gain reappears when you eventually sell. The benefit is timing plus any rate difference."},
    {"q": "You harvested a $21,430 loss in 2025 and had no capital gains that year. How much reduces your 2025 ordinary income?", "opts": ["$21,430", "$3,000, with $18,430 carried forward", "$10,715", "Nothing until you have gains"], "correct": 1, "explain": "With no gains to absorb it, section 1211(b) limits the deduction against ordinary income to $3,000; section 1212(b) carries the remaining $18,430 forward as a short-term loss."},
    {"q": "Which replacement bought on the same day as the loss sale is clearly outside the wash-sale rule under Publication 550?", "opts": ["A fund tracking a different index with different holdings", "The same ETF from the same sponsor", "A call option on the ETF you just sold", "The same ETF bought in your IRA"], "correct": 0, "explain": "Pub. 550 treats an option to acquire the same security and an IRA purchase as triggers. It says securities of one issuer are ordinarily not substantially identical to those of another, which covers a fund tracking a different index; it does not rule on two funds tracking the same index."},
    {"q": "A December harvest must be executed by:", "opts": ["The settlement date in January is fine", "January 31 of the following year", "The trade date on or before December 31", "The date you file the return"], "correct": 2, "explain": "For securities traded on an established market, gain or loss is recognised on the trade date; a sale executed on December 31 that settles in January belongs to the December year. Wash-sale purchases in January still count against it."},
    {"q": "In the worked example, waiting 31 days in cash and rebuying SPY on 2025-05-09 meant:", "opts": ["The loss was disallowed", "Re-entering $67.86 per share higher, $13,572 on 200 shares, which exceeded the tax value of the loss", "No change in basis", "The rebuy was a wash sale"], "correct": 1, "explain": "SPY closed at $496.48 on 2025-04-08 and $564.34 on 2025-05-09. The 31-day gap avoided the wash sale but cost $13,572 of missed appreciation against a tax value of roughly $5,143 at a 24% rate."}
  ],
  "task": "For each open position with a paper loss, write down its lot dates, adjusted basis, the 30-day look-back for any purchase of the same security in any of your accounts, and the replacement you would use."
}
---

## What harvesting actually does

Tax-loss harvesting means selling a position that shows a loss so that the loss becomes real for tax purposes, then keeping your market exposure through some other position. Nothing in the Code is called harvesting; it is an application of three rules you already have. The realised loss enters the Schedule D netting of lesson 2, where it offsets capital gains first and then up to $3,000 of ordinary income under section 1211(b), with the rest carried forward under section 1212(b). The replacement must avoid the section 1091 wash-sale trap of lesson 3. And the replacement position starts at today's lower price as its basis, so the gain you avoided taxing comes back when the replacement is sold.

That last point is the one to hold onto. Harvesting is a deferral, and its value has three sources: the time value of paying tax later rather than now; the possibility that the eventual gain will be long-term at 15% or 20% when the loss offset a short-term gain at up to 37%; and, if you never sell, the step-up in basis at death under section 1014, which is outside this course. If you harvest a loss and then sell the replacement six months later at a gain, you have converted a loss into a smaller short-term gain in the same year and gained very little.

## Step 1: find the loss lots

Work lot by lot, not position by position. A position with an overall gain can contain a lot with a loss, and specific identification (lesson 2) lets you sell that lot alone. Use adjusted basis, including any wash-sale additions and any return-of-capital reductions, and check that the lot has not already been marked as a replacement for an earlier loss. Losses inside an IRA, a Roth IRA or a 401(k) cannot be harvested at all; there is no capital loss inside a tax-deferred account.

## Step 2: check the 61-day window in both directions

Before selling, look back 30 days across every account you and your spouse hold: any purchase of the same security, including a dividend reinvestment or a call option, will disallow part or all of the loss. Then commit to not buying it back, or anything substantially identical, for 30 days after the sale, again in every account. Cancel automatic reinvestment on the security in every account for the duration.

## Step 3: choose the replacement

You have four choices, and the tax certainty declines as the tracking quality rises.

Cash for 31 days is certain and costs you the market's move for a month, in either direction. A fund on a different index, for example a Nasdaq-100 fund replacing an S&P 500 fund, is treated by Publication 550 as a different issuer's security and is not substantially identical, at the cost of a different exposure. A fund on the same index from a different sponsor tracks almost perfectly, and this is where the IRS has published nothing: Publication 550 says only that securities of one corporation are ordinarily not substantially identical to those of another, and that all the facts and circumstances matter. Many practitioners treat same-index funds as substantially identical because the economic exposure is the same; others do not. This course does not resolve it, and a CPA should decide for your return. Buying the same fund back inside 30 days is the fourth choice and it is simply a wash sale.

## Step 4: execute by trade date and record everything

Gain and loss on listed securities are recognised on the trade date, so a sale on December 31 counts for that year even though it settles in January. Write down the lot sold, the proceeds, the adjusted basis, the loss, the window dates, and the replacement. In February, reconcile the broker's Form 1099-B box 1g against your own wash-sale check; the broker only reports same-account, same-CUSIP wash sales, and you must add any others on Form 8949 with code W (lesson 12).

## Worked example

You bought 200 SPY on 2024-12-02 at the Yahoo Finance daily close of $603.63, cost $120,726.00. On 2025-04-08, the lowest close of the year at $496.48, you sold the lot: proceeds $99,296.00, loss $21,430.00. Held 127 days, so short-term. You had no purchases of SPY in any account after 2025-03-09 and you switched off dividend reinvestment.

Tax value of the loss. If you have $21,430 or more of 2025 short-term gains elsewhere and are in the 24% bracket, the loss saves $21,430 × 0.24 = $5,143.20 of 2025 tax, or $5,957.54 if the NIIT also applies (27.8%). If you have no gains, the loss saves only $3,000 × 0.24 = $720 in 2025 and the remaining $18,430 waits as a short-term carryforward.

Path A, cash for 31 days. The window closes 2025-05-08 and you rebuy 200 SPY on 2025-05-09 at the close of $564.34, cost $112,868.00. The market moved $67.86 a share while you were out, $13,572.00 on 200 shares, which is more than the tax value of the loss in the best case. Your new basis is $112,868.00 against the old $120,726.00. At the 2025-12-31 close of $681.92 the unrealised gain on the new lot is ($681.92 − $564.34) × 200 = $23,516.00, versus ($681.92 − $603.63) × 200 = $15,658.00 had you never sold. The $7,858.00 difference is the harvested loss of $21,430.00 less the $13,572.00 you missed: the loss was deferred, not removed, and the deferral shrank because you were out of the market.

Path B, a different-index fund the same day. With the $99,296.00 of proceeds you bought 238 QQQ at the 2025-04-08 close of $416.06, cost $99,022.28, leaving $273.72 in cash. QQQ is a Nasdaq-100 fund, a different index with different holdings, so under Publication 550's ordinary reading it is not substantially identical to SPY. On 2025-05-09 QQQ closed at $487.97 and the lot was worth $116,136.86, an unrealised gain of $17,114.58. If you now switch back to SPY, you realise a $17,114.58 short-term gain in 2025 and your net harvested loss for the year shrinks to $21,430.00 − $17,114.58 = $4,315.42. If you keep QQQ, you keep the full loss for 2025 and carry a $99,022.28 basis in a position you did not originally want.

Path C, a same-index fund. VOO closed at $456.74 on 2025-04-08 and tracks the same S&P 500 index. Whether it is substantially identical to SPY is unsettled; if a CPA advises against it, treat it as path B with tighter tracking and the risk that the loss is disallowed on examination.

## Chart

![The harvesting decision in the order the questions are asked: confirm the loss per lot on adjusted basis; confirm the account is taxable; check every account, spouse and IRA for a substantially identical purchase within 30 days either side; sell and choose the replacement (cash for 31 days, a different-index fund, or a same-index fund from another sponsor, which is unsettled); record the lot, dates and disallowed amounts and reconcile the 1099-B. Built from Publication 550, Wash Sales, tax year 2025.](figures/harvesting-decision-flow.svg)

## When not to harvest

Do not harvest a loss you cannot use: if you already have a large carryforward and no gains, adding to it has no 2025 value and only lowers future basis. Do not harvest a long-term loss to offset a short-term gain if you can instead hold the winner past a year; the netting order can leave you spending a 15%-rate loss against a 24%-rate gain in a later year when you would have preferred the reverse. Do not harvest in a position you intend to add to within 30 days. And do not confuse the fund's own distributions with harvesting: a fund that pays a capital gain distribution in December is taxable whether or not you sold.

## Sources

- IRS Publication 550, Investment Income and Expenses (Wash Sales; Capital Losses): https://www.irs.gov/publications/p550
- IRC section 1091, Loss from wash sales of stock or securities: https://www.law.cornell.edu/uscode/text/26/1091
- IRC section 1211, Limitation on capital losses: https://www.law.cornell.edu/uscode/text/26/1211
- Instructions for Form 8949 (code W; trade-date reporting): https://www.irs.gov/instructions/i8949
