---
{
  "title": "Record-Keeping: Form 8949, Schedule D, the 1099-B and Working With a CPA",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Under Exception 1 in the Form 8949 instructions, you may skip Form 8949 and report totals directly on Schedule D line 1a or 8a when:", "opts": ["The broker reported basis to the IRS and the 1099-B shows no adjustments in box 1f or 1g, and the Ordinary box is not checked", "You have fewer than 100 trades", "All trades were profitable", "You used a CPA"], "correct": 0, "explain": "Exception 1 covers transactions (other than collectibles) on a 1099-B showing basis reported to the IRS, with no adjustment in box 1f or 1g and the Ordinary box in box 2 unchecked. Anything with an adjustment must go on Form 8949."},
    {"q": "Your broker reported the basis of replacement shares as $54,669 to the IRS, but the correct basis after a cross-account wash sale is $65,434. On Form 8949 Part I, box A, you enter:", "opts": ["$65,434 in column (e) and nothing in column (g)", "$54,669 in column (e), code B in column (f), and −$10,765 in column (g)", "$54,669 in column (e) and code W", "Nothing; the broker's figure is final"], "correct": 1, "explain": "The Form 8949 instructions for code B: when the basis was reported to the IRS, enter the reported basis in column (e) even though it is incorrect, and correct it in column (g) using the Worksheet for Basis Adjustments (reported basis minus correct basis)."},
    {"q": "Generally, how long must you keep records supporting an item on a return, if no special situation applies?", "opts": ["1 year", "10 years", "Until the period of limitations for that return runs out, generally 3 years after filing", "Forever"], "correct": 2, "explain": "IRS, How long should I keep records: keep records until the period of limitations expires, generally 3 years (IRC section 6501(a)); 6 years if you omit more than 25% of gross income; 7 years for a worthless securities or bad debt loss; indefinitely for no return or a fraudulent return."},
    {"q": "Records showing what you paid for shares should be kept:", "opts": ["Until the period of limitations expires for the year in which you dispose of the shares", "3 years from purchase", "Until the next 1099-B arrives", "Only if the shares are noncovered"], "correct": 0, "explain": "The IRS records page: keep records relating to property until the period of limitations expires for the year in which you dispose of the property, because you need them to figure gain or loss."},
    {"q": "For a trader with a section 475(f) election, trading-business securities sales are reported on:", "opts": ["Form 8949 with code W", "Schedule D line 1a", "Form 6781", "Form 4797 Part II line 10, with an attached statement"], "correct": 3, "explain": "The Form 4797 instructions: report on line 10 all gains and losses from securities held in connection with the trading business, including year-end marks, with a statement in the same format showing each transaction, and enter 'Trader—see attached' in column (a)."}
  ],
  "task": "Build a one-page list of every 2025 tax document you expect (each 1099-B, 1099-DA, 1099-DIV, 1099-INT, 5498, K-1) with the issuer and the date it is due to arrive."
}
---

## How the forms fit together

A trader's capital transactions travel through three layers. Brokers report each sale to you and the IRS on Form 1099-B (securities) or Form 1099-DA (digital assets), and report section 1256 contracts in aggregate in 1099-B boxes 8 to 11. You transcribe and correct those sales on Form 8949, one row per sale or one summary row per category with an attached statement. Form 8949 totals, Form 6781 for section 1256 contracts, capital gain distributions and any carryover from last year meet on Schedule D, which produces the net figure on Form 1040 line 7 and feeds the capital gain tax worksheet. A trader with a section 475(f) election instead reports trading-business securities on Form 4797 Part II line 10, with an attached statement listing each transaction and separately identifying positions marked at year end (Form 4797 instructions).

The Form 8949 instructions explain the purpose: it lets you and the IRS reconcile the amounts reported on information returns with the amounts on your return. That is the right way to think about it. The IRS matches your Schedule D to the 1099-Bs it received; your job is to report the broker's numbers and then show, in columns (f) and (g), exactly where and why your numbers differ.

## The six boxes and the two exceptions

Part I of Form 8949 is short-term and Part II long-term, using the holding-period rule of lesson 1. Each part is filed separately for each box. Box A (Part I) or D (Part II): reported on a 1099-B showing basis was reported to the IRS. Box B or E: reported on a 1099-B without basis reported to the IRS. Box C or F: no 1099-B at all. Digital assets use G, H, I and J, K, L instead (lesson 11). Check one box per page.

Exception 1 lets you skip Form 8949 for sales on a 1099-B that shows basis reported to the IRS, shows no adjustment in box 1f (accrued market discount) or box 1g (wash sale loss disallowed), and does not have the Ordinary box checked; report their totals directly on Schedule D line 1a (short-term) or line 8a (long-term). Exception 2 lets you report all sales on an attached statement in the same format, typically the broker's own realised gain/loss report, and enter only the totals on Form 8949 with the broker's name and "see attached statement" in column (a). Don't write "available upon request" in place of the detail.

## Reconciling the 1099-B

Read the 1099-B before you trust it. Check four things. First, that every sale you made appears, including option expirations and assignments, which brokers sometimes show in a separate section. Second, the basis on noncovered lots, which brokers are not required to report: stock acquired before 2011 and anything transferred in without basis information arrives as box B or E with a blank or wrong basis, and you supply it. Third, box 1g, which the broker fills only for wash sales within the same account and CUSIP (1099-B instructions); wash sales across accounts, brokers, your spouse or your IRA are yours to find. Fourth, section 1256 aggregates in box 11, which go to Form 6781, not Form 8949.

Form 8949 column (f) codes record each correction: W for a wash-sale loss you cannot deduct (positive amount in column (g)); B when the basis on the 1099-B is incorrect (reported basis stays in column (e), correction in column (g) if basis was reported to the IRS); O for other adjustments; and several more for special cases. The Worksheet for Basis Adjustments in Column (g) computes a code B adjustment as reported basis minus correct basis.

## Worked example

This is lesson 3's wash sale, with the repurchase made at a second broker so neither firm sees it.

Broker A, 2025 Form 1099-B, box 12 checked (basis reported): 100 SPY acquired 2025-02-19, sold 2025-04-04; box 1d proceeds $50,528.00; box 1e basis $61,293.00; box 1g $0.00. Broker B, 2025 Form 1099-B, box 12 checked: 100 SPY acquired 2025-04-24, sold 2025-12-01; box 1d $68,027.00; box 1e $54,669.00; box 1g $0.00. All prices are Yahoo Finance daily closes for SPY.

Your own wash-sale check finds that the 2025-04-24 purchase at Broker B falls inside the window 2025-03-05 to 2025-05-04 around the 2025-04-04 loss sale at Broker A. Section 1091 disallows the $10,765.00 loss and adds it to the replacement's basis: $54,669.00 + $10,765.00 = $65,434.00.

Form 8949, Part I, box A, row 1 (Broker A sale): (a) 100 sh SPY; (b) 02/19/2025; (c) 04/04/2025; (d) $50,528.00; (e) $61,293.00; (f) W; (g) $10,765.00; (h) = $50,528.00 − $61,293.00 + $10,765.00 = $0.00.

Row 2 (Broker B sale): (a) 100 sh SPY; (b) 04/24/2025, the trade date of the replacement purchase as column (b) instructs; (c) 12/01/2025; (d) $68,027.00; (e) $54,669.00, the basis Broker B reported; (f) B; (g) basis worksheet: reported $54,669.00 minus correct $65,434.00 = −$10,765.00; (h) = $68,027.00 − $54,669.00 − $10,765.00 = $2,593.00. The tacked holding period, from 2025-02-20, is still under a year, so Part I is correct either way.

Totals carried to Schedule D line 1b: (d) $118,555.00; (e) $115,962.00; (g) $10,765.00 − $10,765.00 = $0.00; (h) $2,593.00. The IRS sees both 1099-B amounts in columns (d) and (e) exactly as reported, and the codes explain the difference. Had you filed the two 1099-Bs as reported, your 2025 return would have shown a $10,765.00 loss and a $13,358.00 gain, the same $2,593.00 net in this case because both legs closed in 2025; had the replacement still been open on December 31, the unreported wash sale would have overstated your 2025 loss by $10,765.00.

## Table

| Record | Keep until | Source |
|---|---|---|
| Return and supporting records, general case | 3 years after filing (a return filed early is treated as filed on the due date) | IRC 6501(a); IRS, How long should I keep records |
| If income omitted exceeds 25% of gross income shown | 6 years after filing | IRC 6501(e)(1)(A); same |
| Claim for a worthless-securities or bad-debt loss | 7 years | IRS, How long should I keep records |
| No return filed, or a fraudulent return | Indefinitely | IRC 6501(c); same |
| Purchase confirmations and basis records for a position | Until the limitation period expires for the year you dispose of it | IRS, How long should I keep records |
| Worked example: the 2025-02-19 SPY confirmation | At least until April 15, 2029 (3 years after the April 15, 2026 due date of the 2025 return) | Same |

## Working with a CPA

Bring documents, not summaries. A CPA or enrolled agent preparing a trader's return needs: every Form 1099-B, 1099-DA, 1099-DIV and 1099-INT, including corrected forms, which brokers often issue in March; the consolidated statements and realised gain/loss detail behind them; your own lot records for noncovered positions and for crypto by wallet; a list of every account you and your spouse hold, including IRAs, for the cross-account wash-sale check; the prior year's return with Schedule D and the Capital Loss Carryover Worksheet; the dated section 475(f) election statement and Form 3115 if you have elected; Form 1040-ES payment confirmations; and the trading-expense records from lesson 8 if you claim trader status. Ask how they will test trader status, how they handle same-index fund replacements, and whether they file Form 8949 by transaction or by attached statement. A preparer can only defend what you can document, and every position in this course, from specific identification to trader status, rests on records made at the time.

## Sources

- Instructions for Form 8949 (boxes A to L; Exceptions 1 and 2; codes W and B; Worksheet for Basis Adjustments): https://www.irs.gov/instructions/i8949
- Instructions for Schedule D (Form 1040), 2025: https://www.irs.gov/instructions/i1040sd
- Instructions for Form 1099-B (box 1g; boxes 8 to 11): https://www.irs.gov/instructions/i1099b
- IRS, How long should I keep records?: https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records
