---
{
  "title": "Capstone: A Twelve-Trade Tax Year, From Trade List to Schedule D",
  "duration": "45 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Trade 1 bought NVDA on 2024-07-01. Which sale date is the earliest that makes the gain long-term?", "opts": ["2025-06-30", "2025-07-01", "2025-07-02", "2025-12-31"], "correct": 2, "explain": "Counting begins the day after purchase, 2024-07-02. A sale on 2025-07-01 is exactly one year, which is not more than one year (IRC section 1222). 2025-07-02 is the first long-term date."},
    {"q": "Trade 2's $5,382.50 SPY loss is disallowed because:", "opts": ["SPY is an ETF", "Trade 3 bought 50 SPY on 2025-04-24, within 30 days after the 2025-04-04 loss sale", "The loss exceeded $3,000", "SPY is a section 1256 contract"], "correct": 1, "explain": "IRC section 1091(a): the purchase of substantially identical shares within 30 days after the loss sale disallows the loss, and section 1091(d) adds it to the replacement shares' basis."},
    {"q": "Trade 3's adjusted basis after the wash-sale adjustment is:", "opts": ["$32,717.00", "$27,334.50", "$30,646.50", "$34,013.50"], "correct": 0, "explain": "Cost $27,334.50 (50 × $546.69) plus the disallowed $5,382.50 = $32,717.00, so its reported gain on 2025-12-01 is $34,013.50 − $32,717.00 = $1,296.50."},
    {"q": "How much of trade 12's MES gain is long-term on Form 6781 line 9?", "opts": ["$0, because it was held 41 days", "$1,340.00", "$3,350.00", "$2,010.00"], "correct": 3, "explain": "IRC section 1256(a)(3): 60% of $3,350.00, the gain marked at the 2025-12-31 close, is long-term, $2,010.00; 40%, $1,340.00, is short-term."},
    {"q": "Under a securities-only section 475(f) election the capstone's 2025 tax rises by $152.68. Why?", "opts": ["The wash-sale loss is disallowed twice", "Trade 11's $1,696.50 long-term AAPL gain becomes ordinary and loses the 9-point gap between 24% and 15%", "The MES gain becomes ordinary", "The NIIT applies"], "correct": 1, "explain": "With the election the wash sale is ignored but the total securities result is the same $25,172.60, because both SPY legs closed in 2025. The only change is character: $1,696.50 × (24% − 15%) = $152.685, or $152.68 with the arithmetic carried through."}
  ],
  "task": "Complete the exercise on paper before reading the model answer, then score yourself against the rubric and write down each point you lost and the lesson that covers it."
}
---

## The exercise

You are preparing the 2025 federal return of a single filer. The facts: wages $120,000 on Form W-2; no other income; standard deduction $15,750 (Rev. Proc. 2025-32 section 3.01, as amended for 2025); no capital loss carryover from 2024; no section 475 election in effect. All stock and ETF trades were made in one taxable brokerage account, all shares were covered securities with basis reported to the IRS, and every sale used specific identification confirmed by the broker in writing, so the lots sold are exactly those listed. The futures were traded at a separate futures broker. Prices are Yahoo Finance daily closes on the dates shown. MES, the Micro E-mini S&P 500 future, has a $5 multiplier per index point (a CME contract specification, not an IRS figure).

Answer five tasks. One: classify each trade as short-term, long-term or section 1256 and compute its gain or loss. Two: identify the wash sale, the disallowed amount, the adjusted basis of the replacement shares and their holding period. Three: complete the Form 8949 summary lines, Form 6781 lines 1, 7, 8 and 9, and Schedule D lines 1b, 4, 7, 8a or 8b, 11, 15 and 16. Four: compute the 2025 federal income tax under scenario A (trades as listed) and scenario B (trade 1's NVDA sold on 2025-07-02 at $157.25 instead of 2025-06-30), and state whether the net investment income tax applies. Five: explain what would change if a securities-only section 475(f) election had been in effect for 2025, and when it would have had to be made.

## The trade list

| # | Ticker | Qty | Bought | Buy price | Sold | Sell price |
|---|---|---|---|---|---|---|
| 1 | NVDA | 100 | 2024-07-01 | $124.30 | 2025-06-30 | $157.99 |
| 2 | SPY | 50 | 2025-02-19 | $612.93 | 2025-04-04 | $505.28 |
| 3 | SPY | 50 | 2025-04-24 | $546.69 | 2025-12-01 | $680.27 |
| 4 | TSLA | 40 | 2025-03-10 | $222.15 | 2025-05-27 | $362.89 |
| 5 | QQQ | 30 | 2025-01-06 | $524.54 | 2025-04-07 | $423.69 |
| 6 | AAPL | 60 | 2025-06-20 | $201.00 | 2025-12-15 | $274.11 |
| 7 | IWM | 100 | 2025-04-08 | $174.82 | 2025-12-19 | $250.79 |
| 8 | TSLA | 20 | 2025-09-15 | $410.04 | 2025-12-22 | $488.73 |
| 9 | NVDA | 50 | 2025-01-24 | $142.62 | 2025-02-24 | $130.28 |
| 10 | QQQ | 30 | 2025-06-02 | $523.21 | 2025-11-03 | $632.08 |
| 11 | AAPL | 50 | 2024-08-01 | $218.36 | 2025-10-17 | $252.29 |
| 12 | MES (2 contracts, long) | 2 | 2025-11-20 | 6,557.50 | open at 2025-12-31 | 6,892.50 (2025-12-31 close) |

## Worked example

This is the model answer. Work the exercise before reading it.

Task 1, classification. Gains are proceeds minus cost, quantity times price. Trade 1: $15,799.00 − $12,430.00 = $3,369.00; held from 2024-07-02 to 2025-06-30, under a year, short-term. Trade 2: $25,264.00 − $30,646.50 = −$5,382.50, short-term. Trade 3: $34,013.50 − $27,334.50 = $6,679.00 before adjustment, short-term. Trade 4: $14,515.60 − $8,886.00 = $5,629.60. Trade 5: $12,710.70 − $15,736.20 = −$3,025.50. Trade 6: $16,446.60 − $12,060.00 = $4,386.60. Trade 7: $25,079.00 − $17,482.00 = $7,597.00. Trade 8: $9,774.60 − $8,200.80 = $1,573.80. Trade 9: $6,514.00 − $7,131.00 = −$617.00. Trade 10: $18,962.40 − $15,696.30 = $3,266.10. Trades 4 to 10 are all short-term. Trade 11: $12,614.50 − $10,918.00 = $1,696.50, held from 2024-08-02 to 2025-10-17, long-term. Trade 12 is a regulated futures contract, a section 1256 contract (lesson 5), marked at the 2025-12-31 close: (6,892.50 − 6,557.50) × $5 × 2 = $3,350.00.

Task 2, the wash sale. Trade 2 sold SPY at a loss on 2025-04-04; trade 3 bought 50 SPY on 2025-04-24, 20 days later and inside the window 2025-03-05 to 2025-05-04. Section 1091(a) disallows all $5,382.50, because the same number of shares was repurchased. Section 1091(d): trade 3's basis becomes $27,334.50 + $5,382.50 = $32,717.00, and its holding period includes trade 2's, so it runs from 2025-02-20; trade 3 is still short-term at 2025-12-01. Trade 3's reported gain is $34,013.50 − $32,717.00 = $1,296.50. Because both trades were in one account with one CUSIP, the broker reports $5,382.50 in 1099-B box 1g for trade 2 and the adjusted $32,717.00 in box 1e for trade 3. No other loss is affected: trade 5's QQQ loss on 2025-04-07 has no QQQ purchase between 2025-03-08 and 2025-05-07 (trade 10 is 2025-06-02), and trade 9's NVDA loss on 2025-02-24 has no NVDA purchase between 2025-01-25 and 2025-03-26. Holding trade 1's older NVDA lot through that window does not matter: section 1091 looks for acquisitions.

Task 3, the forms, scenario A. Form 8949 Part I, box A, all ten short-term sales: column (d) $179,079.40; (e) $160,985.80; (g) $5,382.50 (trade 2, code W); (h) $23,476.10. Equivalent and acceptable: trade 2 alone on Form 8949 and the other nine on Schedule D line 1a under Exception 1; the line 7 result is identical. Part II, box D, trade 11: (d) $12,614.50; (e) $10,918.00; (h) $1,696.50, which qualifies for Exception 1 and may go directly on Schedule D line 8a. Form 6781: line 1, $3,350.00 (1099-B box 11 from the futures broker); line 7, $3,350.00; line 8 (40%), $1,340.00; line 9 (60%), $2,010.00. Schedule D: line 1b, $23,476.10; line 4, $1,340.00; line 7, $24,816.10; line 8a or 8b, $1,696.50; line 11, $2,010.00; line 15, $3,706.50; line 16, $28,522.60.

Task 4, the tax. Rates from Rev. Proc. 2024-40, Table 3 and section 2.03. Taxable income before trading: $120,000 − $15,750 = $104,250. Scenario A: ordinary taxable income = $104,250 + $24,816.10 = $129,066.10; tax = $17,651 + 24% × ($129,066.10 − $103,350) = $17,651 + $6,171.86 = $23,822.86. Net capital gain $3,706.50 sits above that, inside the 15% band (which runs to $533,400): $3,706.50 × 15% = $555.98. Total 2025 income tax $24,378.84. Without the trades it would be $17,651 + 24% × $900 = $17,867.00, so the trading year cost $6,511.84.

Scenario B: trade 1 sells on 2025-07-02 for $15,725.00, a $3,295.00 gain, long-term because the holding period now exceeds one year. Part I loses the NVDA row: (d) $163,280.40; (e) $148,555.80; (g) $5,382.50; (h) $20,107.10. Part II gains it: (d) $28,339.50; (e) $23,348.00; (h) $4,991.50. Schedule D line 7 = $21,447.10; line 15 = $7,001.50. Ordinary taxable income $125,697.10; tax = $17,651 + 24% × $22,347.10 = $23,014.30. Capital gain tax: $7,001.50 × 15% = $1,050.23. Total $24,064.53, which is $314.31 less than scenario A on a gain that was $74.00 smaller. A sale on 2025-07-01 would still have been short-term.

NIIT: modified AGI is $120,000 + $28,522.60 = $148,522.60 in scenario A and $148,448.60 in B, below the $200,000 threshold of IRC section 1411(b), so no NIIT.

Task 5, a section 475(f) election. To be effective for 2025 the statement had to be filed by April 15, 2025 with the 2024 return or extension request (Rev. Proc. 99-17 section 5.03; Topic 429), and the taxpayer must actually qualify as a trader, which twelve trades in a year almost certainly do not support. Assuming both: the eleven securities trades go on Form 4797 Part II line 10 as ordinary income, not Form 8949. Section 1091 no longer applies to them, so trade 2's $5,382.50 loss is allowed and trade 3's gain is $6,679.00 on its unadjusted basis; the net is unchanged at $25,172.60 because both legs closed in 2025. No securities were open at year end, so there is no mark. Trade 12 stays under section 1256 at 60/40, because a commodities election under section 475(f)(2) is separate. Ordinary taxable income = $104,250 + $25,172.60 + $1,340.00 = $130,762.60; tax = $17,651 + 24% × $27,412.60 = $24,230.02; plus $2,010.00 × 15% = $301.50; total $24,531.52. That is $152.68 more than scenario A: trade 11's long-term gain lost its 15% rate. Trading expenses would move to Schedule C (lesson 8). The election helps a losing year or a year of heavy cross-period wash sales. It does not help this one.

## Chart

![Reported gain or loss per capstone trade on Form 8949 and Form 6781 for tax year 2025, scenario A, after the wash-sale adjustment: trade 2's $5,382.50 SPY loss is reported as $0 (code W) and recovered through trade 3's basis, which reports $1,296.50 instead of $6,679.00; trade 12 is the $3,350.00 MES year-end mark. Prices: Yahoo Finance daily closes. Sources: IRC sections 1091 and 1256; Instructions for Form 8949.](figures/capstone-gain-loss-by-trade.svg)

## Rubric

| Criterion | What earns full marks | Points |
|---|---|---|
| Holding periods and classification | All twelve trades classified correctly, with trade 1 short-term in A and long-term only from 2025-07-02 in B, and trade 12 under section 1256 | 20 |
| Wash sale | Trade 2 identified, $5,382.50 disallowed with code W, trade 3 basis $32,717.00 and tacked holding period; trades 5 and 9 correctly cleared | 20 |
| Section 1256 | Year-end mark at 6,892.50, $3,350.00 gain, Form 6781 lines 8 and 9 at $1,340.00 and $2,010.00 | 15 |
| Form 8949 and Schedule D | Column totals and Schedule D lines 7, 15 and 16 tie to $24,816.10, $3,706.50 and $28,522.60 (A) and $21,447.10 and $7,001.50 (B) | 20 |
| Tax computation | $24,378.84 (A) and $24,064.53 (B) with each rate and threshold cited by tax year and Rev. Proc.; NIIT correctly ruled out | 15 |
| Section 475(f) analysis | Deadline of April 15, 2025, Form 4797, wash sale and character changes, MES unchanged, $24,531.52 and the reason for the $152.68 difference | 10 |

## Sources

- Instructions for Form 8949 (boxes, codes W and B, Exception 1): https://www.irs.gov/instructions/i8949
- Form 6781 and instructions: https://www.irs.gov/pub/irs-pdf/f6781.pdf
- Rev. Proc. 2024-40 (2025 rate tables and section 1(h) breakpoints): https://www.irs.gov/pub/irs-drop/rp-24-40.pdf
- IRC section 1091, Loss from wash sales of stock or securities: https://www.law.cornell.edu/uscode/text/26/1091
