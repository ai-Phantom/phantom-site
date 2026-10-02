---
{
  "title": "Section 1256 Contracts: 60/40 Treatment, Year-End Mark and Form 6781",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Under IRC section 1256(a)(3), gain on a regulated futures contract held for two days is treated as:", "opts": ["60% long-term and 40% short-term, regardless of holding period", "100% short-term", "100% long-term", "Ordinary income"], "correct": 0, "explain": "Section 1256(a)(3) treats 60% of the gain or loss as long-term and 40% as short-term whatever the holding period. Pub. 550 calls this the 60/40 rule."},
    {"q": "Which of these is NOT a section 1256 contract?", "opts": ["An E-mini S&P 500 futures contract on the CME", "A cash-settled option on the S&P 500 index (a broad-based index)", "A listed call option on SPY, an exchange-traded fund", "A regulated futures contract on crude oil"], "correct": 2, "explain": "Pub. 550: a nonequity option is a listed option that is not an equity option; broad-based index options qualify. An option on SPY is an option on stock (the fund's shares) and is an equity option, so it is outside section 1256 unless held by a dealer."},
    {"q": "You hold an open futures position on December 31. For tax purposes you must:", "opts": ["Report nothing until you close it", "Report it only if it shows a gain", "Elect out on Form 6781", "Treat it as sold at fair market value on the last business day of the year and report the gain or loss"], "correct": 3, "explain": "Section 1256(a)(1) requires each contract held at year end to be treated as sold for its fair market value on the last business day of the taxable year, with the gain or loss taken into account for that year."},
    {"q": "On Form 6781 (2025), the 40% short-term and 60% long-term portions of the net section 1256 gain flow to:", "opts": ["Form 8949 Part I and Part II", "Schedule D line 4 and line 11 respectively", "Form 4797", "Schedule C"], "correct": 1, "explain": "Form 6781 line 8 (40%) is entered on Schedule D line 4 and line 9 (60%) on Schedule D line 11, per the form instructions."},
    {"q": "In the worked example, 2 MES contracts bought 2025-11-20 at 6,557.50 and marked at 6,892.50 on 2025-12-31 produced a 2025 gain of:", "opts": ["$335.00", "$1,675.00", "$3,350.00, split $2,010 long-term and $1,340 short-term", "$6,700.00"], "correct": 2, "explain": "(6,892.50 − 6,557.50) = 335 index points × $5 per point × 2 contracts = $3,350.00; 60% is $2,010.00 long-term and 40% is $1,340.00 short-term."}
  ],
  "task": "Open last year's Form 1099-B from your futures or options broker and find box 8, box 9, box 10 and box 11, the aggregate profit or loss on section 1256 contracts."
}
---

## A separate regime for futures and index options

Everything in lessons 1 to 4 assumed a holding period decided the rate and that a loss could be disallowed as a wash sale. IRC section 1256 replaces both ideas for a defined list of contracts. Section 1256(a)(1) says each section 1256 contract you hold at the close of the taxable year is treated as sold for its fair market value on the last business day of the year, and the gain or loss is taken into account for that year. Section 1256(a)(3) says any gain or loss on such a contract, whether from that year-end mark or from an actual close, is treated as 40% short-term and 60% long-term capital gain or loss, regardless of how long you held the position. Publication 550 states the consequence directly: the wash-sale rules do not apply to losses on commodity futures contracts, and section 1256(a)(4) removes the straddle rules where every leg is a section 1256 contract.

## Which contracts qualify

Section 1256(b)(1) lists five: any regulated futures contract, any foreign currency contract, any nonequity option, any dealer equity option, and any dealer securities futures contract. For an individual trader the first three matter. A regulated futures contract under section 1256(g)(1) is one traded on a qualified board or exchange where the amount deposited and withdrawn depends on a system of marking to market: index, bond, energy, metal, agricultural and currency futures on the CME, CBOT, NYMEX, COMEX and ICE all qualify. A foreign currency contract under section 1256(g)(2) is an interbank forward in a currency in which regulated futures also trade. A nonequity option under section 1256(g)(3) is any listed option that is not an equity option; Publication 550 says these include debt options, commodity futures options, currency options and broad-based stock index options, giving the S&P 500 index as its example, and adds that cash-settled index options traded on a qualified exchange are nonequity options when the SEC determines the index is broad based.

The exclusions matter as much. An equity option is an option on a single stock or on a narrow-based index, and section 1256 does not reach it in a non-dealer's hands. An option on an exchange-traded fund is an option to buy or sell shares of the fund, which are stock, so SPY, QQQ and IWM options are equity options taxed under lesson 6 even though the fund tracks a broad index. Options on the S&P 500 index itself (cash-settled, SEC-designated broad based) are nonequity options and get 60/40. Section 1256(b)(2) also excludes securities futures contracts on single stocks unless held by a dealer, and all swaps.

## The arithmetic of 60/40

The blended rate is 0.4 × your ordinary marginal rate + 0.6 × your long-term rate. For a 2025 single filer in the 24% bracket with a 15% long-term rate, that is 9.6% + 9% = 18.6% instead of 24%. At the top, 0.4 × 37% + 0.6 × 20% = 26.8% instead of 37%, before the 3.8% NIIT which applies equally to both. At the bottom of the scale, a filer whose taxable income is under the section 1(h) zero-rate breakpoint pays 0.4 × 12% = 4.8% on a futures gain. The treatment cuts both ways: a section 1256 loss is 60% long-term, so it offsets long-term gains first in the lesson 2 netting order.

Because the year-end mark forces recognition, a profitable open position on December 31 is taxed in that year with no cash raised from a sale. Publication 550's example shows the reversal: a contract bought for $50,000, marked at $57,000 on December 31 (a $7,000 gain recognised) and sold on February 3 for $56,000 produces a $1,000 loss in the second year, because the basis was reset by the mark. The mark also means a losing open position generates a deductible loss in the year of the mark, subject to the ordinary capital loss limits.

## Form 6781 and the 1099-B

Section 1256 contracts are not reported on Form 8949. Your futures or options broker reports them in aggregate on Form 1099-B: box 8 is realised profit or loss on contracts closed during the year, box 9 is the unrealised profit or loss on contracts open at the end of the prior year, box 10 is the unrealised profit or loss on contracts open at the end of this year, and box 11 is the aggregate profit or loss for the year, box 8 minus box 9 plus box 10. Form 6781 Part I takes the box 11 figure from each broker on line 1, nets them, and on line 8 multiplies the net by 40% for Schedule D line 4 (short-term) and on line 9 by 60% for Schedule D line 11 (long-term). Attach Form 6781 to the return.

One election belongs here. If your section 1256 contracts show a net loss for the year, box D on Form 6781 lets an individual elect under section 1212(c) to carry that loss back three years against net section 1256 gains in those years, rather than forward under the ordinary carryover rules. Publication 550 explains the limits: the loss carried back cannot exceed the net section 1256 gain of the carryback year and cannot create or increase a net operating loss. It is claimed by amending the earlier year on Form 1040-X with an amended Form 6781 and Schedule D.

## Worked example

On 2025-11-20 you bought 2 Micro E-mini S&P 500 futures (MES) at the Yahoo Finance MES=F continuous-contract daily close of 6,557.50. MES has a contract multiplier of $5 per index point (a CME Group specification, not an IRS figure). MES is a regulated futures contract on a qualified board, so it is a section 1256 contract.

You held both contracts through year end. The last business day of 2025 was Wednesday 2025-12-31, when MES=F closed at 6,892.50. Section 1256(a)(1) treats the position as sold at that price: gain = (6,892.50 − 6,557.50) × $5 × 2 = 335 × $10 = $3,350.00, recognised in 2025 although nothing was sold. Section 1256(a)(3) splits it: long-term 60% = $2,010.00; short-term 40% = $1,340.00.

On the broker's 2025 Form 1099-B, box 8 shows $0 (nothing closed), box 9 shows $0 (nothing open at the end of 2024), box 10 shows $3,350.00 and box 11 shows $3,350.00. Form 6781: line 1, $3,350.00; line 7 (net), $3,350.00; line 8, $1,340.00 to Schedule D line 4; line 9, $2,010.00 to Schedule D line 11.

Tax, 2025 single filer in the 24% bracket with a 15% long-term rate and no other gains: short-term $1,340.00 × 0.24 = $321.60; long-term $2,010.00 × 0.15 = $301.50; total $623.10, an effective 18.6% on $3,350.00. Had the same gain been a short-term stock trade, the tax would have been $3,350.00 × 0.24 = $804.00. The 60/40 saving is $180.90.

On 2026-01-05 you closed both contracts at the close of 6,943.75. Your basis was reset to the 2025-12-31 mark, so the 2026 gain is (6,943.75 − 6,892.50) × $5 × 2 = $512.50, again 60/40, and it will appear in box 8 of the 2026 Form 1099-B with $3,350.00 in box 9 reversing the prior mark.

## Chart

![Ordinary bracket rate versus the section 1256 60/40 blended rate (0.4 × ordinary + 0.6 × long-term) for a 2025 single filer, no NIIT: 10% versus 4.0%, 12% versus 4.8%, 22% versus 17.8%, 24% versus 18.6%, 32% versus 21.8%, 35% versus 23.0%, 37% versus 26.8%. Sources: IRC section 1256(a)(3); Rev. Proc. 2024-40 sections 2.01 and 2.03.](figures/sixty-forty-blended-vs-ordinary.svg)

## Traders and section 1256

Publication 550 says gain or loss from trading section 1256 contracts is capital gain or loss subject to the mark-to-market rule even for someone who trades them as a business, so the 60/40 treatment survives trader status. The section 475(f) election of lesson 7 has two parts: paragraph (f)(1) covers securities and paragraph (f)(2) covers commodities, and they are made separately. A trader who elects for securities only keeps 60/40 on futures; a trader who also elects for commodities converts futures gains to ordinary income and gives up the blended rate, which is rarely wanted for a profitable futures book but can be wanted for a losing one, since ordinary losses escape the $3,000 cap.

## Sources

- IRC section 1256, Section 1256 contracts marked to market: https://www.law.cornell.edu/uscode/text/26/1256
- IRS Publication 550, Investment Income and Expenses (Section 1256 Contracts Marked to Market): https://www.irs.gov/publications/p550
- Form 6781, Gains and Losses From Section 1256 Contracts and Straddles, and instructions: https://www.irs.gov/pub/irs-pdf/f6781.pdf
- Instructions for Form 1099-B, boxes 8 to 11: https://www.irs.gov/instructions/i1099b
