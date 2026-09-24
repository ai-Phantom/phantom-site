---
{
  "title": "Regulation and Taxes: Property, Not Currency",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "IRS Notice 2014-21, question 1, states that for federal tax purposes virtual currency is treated as", "opts": ["Currency", "Property", "A security", "A collectible"], "correct": 1, "explain": "A-1 reads that virtual currency is treated as property and that general tax principles applicable to property transactions apply."},
    {"q": "You swap 0.25 BTC for ETH on 2026-03-16 without touching dollars. Is that a taxable event?", "opts": ["No, only sales for dollars are taxable", "Yes; A-6 of the notice says exchanging virtual currency for other property produces gain or loss measured against your adjusted basis", "Only if the ETH is later sold", "Only above $10,000"], "correct": 1, "explain": "Every disposition of property is a realisation event. Coin-to-coin swaps, paying for goods and paying a fee in crypto all count."},
    {"q": "0.5 BTC bought 2025-10-06 at $124,752.53 and sold 2026-09-24 at $84,242.04 produces", "opts": ["A long-term loss of $20,255", "A short-term loss of $20,255, because the holding period of 353 days is under one year", "No loss until the year ends", "A gain"], "correct": 1, "explain": "(84,242.04 minus 124,752.53) times 0.5 is minus $20,255.25. Held 353 days, twelve short of the long-term threshold."},
    {"q": "Which US agency determined in 2015 that bitcoin and other virtual currencies are commodities under the Commodity Exchange Act?", "opts": ["The SEC", "The CFTC, in its order against Coinflip, Inc.", "The IRS", "FinCEN"], "correct": 1, "explain": "The CFTC's September 2015 order (press release 7231-15) is the foundation of its jurisdiction over crypto derivatives."},
    {"q": "Form 1099-DA is", "opts": ["A form for reporting mining income", "The information return brokers use to report digital asset sale proceeds to the IRS and to you", "A form for foreign accounts", "Optional"], "correct": 1, "explain": "The IRS's page for Form 1099-DA describes broker reporting of digital asset proceeds; the numbers reported there must reconcile to your own Form 8949."}
  ],
  "task": "Export every trade, swap and fee from each venue and wallet you used this year into one spreadsheet with date, asset, quantity, dollar value and cost basis, before the next lesson."
}
---

## Who regulates what

The survey-level map of US crypto regulation has four agencies and a new statute.

The Commodity Futures Trading Commission treats bitcoin and other virtual currencies as commodities. Its 2015 order against Coinflip, Inc. (press release 7231-15) was the first to say so, and it is why BTC futures on regulated US exchanges fall under the CFTC and why the agency polices fraud and manipulation in the underlying spot market even though it does not license spot venues.

The Securities and Exchange Commission asserts that many tokens, and some products built on them, are securities, and has brought enforcement actions against exchanges on that basis; its June 2023 press release announcing charges against Coinbase is the canonical example, and litigation over which tokens are securities has continued since. Whether a given token is a security decides which venue may list it, and that question is unsettled at the time of writing.

The Financial Crimes Enforcement Network, in its 2013 guidance, treats exchangers and administrators of virtual currency as money services businesses subject to the Bank Secrecy Act, which is why every US-facing exchange collects identity documents and reports suspicious activity.

The Internal Revenue Service treats virtual currency as property. That single word, from Notice 2014-21, drives the rest of this lesson.

Congress added a fifth piece in 2025: the GENIUS Act (Public Law 119-27) created a federal regime for payment stablecoins (lesson 4). Market-structure legislation covering the rest of the industry has been proposed repeatedly and you should check the current state of it rather than rely on this page.

## Property, and what follows from it

Notice 2014-21, Q&A 1: for federal tax purposes virtual currency is treated as property, and general tax principles applicable to property transactions apply. Q&A 6: exchanging virtual currency for other property produces taxable gain or loss, measured as the fair market value received minus the adjusted basis of what you gave up.

The consequences are mechanical and unforgiving:

- Every disposition is a realisation event. Selling for dollars, swapping one coin for another, paying for a coffee, and paying a network fee in the coin are all sales of property at fair market value on that date.
- Gains and losses are capital, short-term if held one year or less and long-term if held more than one year, reported on Form 8949 and Schedule D like stock.
- Basis is what you paid, in dollars, including fees. Coins received as payment or as staking or mining rewards are ordinary income at their dollar value on receipt (Q&A 3 and Q&A 8 of the notice), and that value becomes their basis.
- Since tax year 2025 brokers report digital asset proceeds on Form 1099-DA; what they report must reconcile to your own records, and the venues cannot see your basis for coins you moved between them.

The IRS digital assets page and its FAQ extend the notice to hard forks, airdrops and staking. The FAQ is updated; the notice is not, so read both.

## Worked example

A trader makes three transactions, all priced at Yahoo Finance's daily closes for the dates involved.

**Purchase, 2025-10-06.** Buys 0.5 BTC at the day's close of $124,752.53. Cost: 0.5 × 124,752.53 = $62,376.27. Add a 0.15% maker fee of $93.56. Adjusted basis: $62,469.83, or $124,939.66 per BTC.

**Swap, 2026-03-16.** Exchanges 0.25 BTC for ETH. BTC closed at $74,861.09 and ETH at $2,351.18. This is a disposition of 0.25 BTC:

- Amount realised: 0.25 × 74,861.09 = $18,715.27.
- Basis of the 0.25 BTC given up: 0.25 × 124,939.66 = $31,234.92.
- Loss: 18,715.27 − 31,234.92 = −$12,519.65.
- Holding period: 2025-10-06 to 2026-03-16 is 161 days. Short-term.
- ETH received: 18,715.27 ÷ 2,351.18 = 7.960 ETH, with a basis of $18,715.27 (the value given up) and a new holding period starting 2026-03-16.

No dollars changed hands. The trader owes nothing on this leg because it is a loss, but the loss exists only if it is recorded now, with the dollar values of that day, and the ETH's basis is set by it.

**Sale, 2026-09-24.** Sells the remaining 0.25 BTC at the close of $84,242.04.

- Amount realised: 0.25 × 84,242.04 = $21,060.51.
- Basis: 0.25 × 124,939.66 = $31,234.92.
- Loss: −$10,174.41.
- Holding period: 2025-10-06 to 2026-09-24 is 353 days. Short-term, by twelve days.

**Year's result.** Two short-term capital losses totalling 12,519.65 + 10,174.41 = $22,694.06 on the BTC lots, plus an open ETH position with a $18,715.27 basis that at the 2026-09-24 close of $2,688.87 is worth 7.960 × 2,688.87 = $21,403.41, an unrealised gain of $2,688.14 that is not yet taxable. The realised losses offset capital gains from any source and up to $3,000 of ordinary income, with the rest carried forward.

Two observations. Had the trader waited until 2026-10-07 to sell, the second loss would have been long-term; for a loss that is worse, since short-term losses offset short-term gains taxed at ordinary rates, so the calendar cut the right way this time. And the wash-sale rule of section 1091 by its terms applies to stock and securities; whether and how it applies to digital assets has been the subject of legislative proposals, and the IRS has not extended it in the notice or FAQ. Check the current position before relying on that in either direction.

## Table

| Event | Taxable? | Character | What you must record |
|---|---|---|---|
| Buy crypto with dollars | No | Sets basis | Date, quantity, dollars paid including fees |
| Sell crypto for dollars | Yes | Capital gain or loss | Proceeds, basis, holding period |
| Swap coin for coin | Yes | Capital gain or loss on the coin given up | Fair value of both sides on the date; new basis for the coin received |
| Pay for goods or fees in crypto | Yes | Capital gain or loss | Fair value on the date |
| Receive coins for services, mining, staking | Yes | Ordinary income at receipt | Dollar value on receipt; becomes basis |
| Transfer between your own wallets | No | None | Keep the record so basis follows the coins |
| Perpetual funding received or paid | Consult a professional | Treatment of perp P&L and funding is not addressed in the notice | Every payment, dated, in dollars |
| Loss on a failed exchange | Depends on facts | Possibly a capital loss when the claim is fixed; timing is contested | Petition date, claim amount, distributions |

The last two rows are where this course's authority ends. Perpetual swaps are not mentioned in the 2014 notice; how their funding payments and mark-to-market are characterised is a question for a tax professional who works on derivatives, and the answer may differ between a CFTC-regulated future and an offshore perp.

## What to do

Keep one ledger, in dollars, from the first trade. Every venue export is incomplete because venues cannot see what you did elsewhere; the FTX customers of lesson 3 who could not document basis had a second problem on top of the first. Reconcile the ledger to every 1099-DA you receive. And if any position is large enough that a mistake costs more than an hour of a professional's time, buy the hour.

## Sources

- Internal Revenue Service, Notice 2014-21 (virtual currency treated as property; Q&A 1, 3, 6, 8): https://www.irs.gov/pub/irs-drop/n-14-21.pdf
- Internal Revenue Service, "Digital Assets" and "Frequently Asked Questions on Virtual Currency Transactions": https://www.irs.gov/filing/digital-assets and https://www.irs.gov/individuals/international-taxpayers/frequently-asked-questions-on-virtual-currency-transactions
- Internal Revenue Service, "About Form 1099-DA, Digital Asset Proceeds From Broker Transactions": https://www.irs.gov/forms-pubs/about-form-1099-da
- Commodity Futures Trading Commission, press release 7231-15, "CFTC Orders Bitcoin Options Trading Platform Operator and its CEO to Cease Illegally Offering Bitcoin Options", 2015-09-17: https://www.cftc.gov/PressRoom/PressReleases/7231-15
