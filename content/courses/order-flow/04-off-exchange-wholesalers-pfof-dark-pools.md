---
{
  "title": "Off-Exchange Trading: Wholesalers, Payment for Order Flow, Dark Pools and ATSs",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "According to Cboe's 2025 review of FINRA TRF data, what share of US consolidated equity volume traded off-exchange in 2025?", "opts": ["25.3%", "37.0%", "45.0%", "50.6%"], "correct": 3, "explain": "50.6%, up 361 basis points on 2024, and the first full year above half. Off-exchange volume first exceeded on-exchange in a single month in November 2024."},
    {"q": "Of that off-exchange volume, roughly what fraction traded on ATSs (dark pools) versus with principal dealers (wholesalers and internalisers)?", "opts": ["50/50", "18.7% ATS, 81.3% dealers", "81.3% ATS, 18.7% dealers", "100% ATS"], "correct": 1, "explain": "Cboe's breakdown of the TRF: 18.7% ATS, 81.3% principal dealers. Dark pools are the smaller part of off-exchange trading."},
    {"q": "Robinhood Securities' Rule 606 report for October 2025 shows Virtu paying 91.2325 cents per hundred shares for S&P 500 market orders. On a 200-share order in a $250 stock, what is that in basis points of notional?", "opts": ["0.04 bps", "0.36 bps", "3.6 bps", "36 bps"], "correct": 1, "explain": "Payment = 2 × $0.912325 = $1.82; notional = 200 × 250 = $50,000; 1.82 / 50,000 = 0.0000365 = 0.36 basis points."},
    {"q": "The SEC's December 2022 order competition proposal estimated the 'competitive shortfall' in wholesaler price improvement at:", "opts": ["0.1 basis point, $50 million a year", "1.08 basis points, about $1.5 billion a year", "10 basis points, $15 billion a year", "Zero"], "correct": 1, "explain": "The fact sheet: 1.08 basis points per dollar traded by wholesalers, about $1.5 billion annually, on the more than 90% of retail marketable orders routed to them."},
    {"q": "Why can a wholesaler profitably fill retail orders inside the NBBO when an exchange market maker cannot?", "opts": ["Wholesalers are exempt from Reg NMS", "Retail flow carries lower adverse-selection cost, so the expected loss per share to informed traders is smaller", "Wholesalers have no inventory risk", "Exchanges forbid price improvement"], "correct": 1, "explain": "Segmenting retail flow removes most of the informed traders from the pool. A dealer facing uninformed flow can quote a tighter effective spread and still earn a margin."}
  ],
  "task": "Download one week of FINRA's OTC transparency data for a stock you follow and compute what percentage of its consolidated volume printed off-exchange."
}
---

## Half the market you cannot see

Everything in lessons 1 through 3 happened on exchanges: displayed books, protected quotes, fee schedules. In 2025, according to Cboe's analysis of FINRA trade-reporting data, 50.6% of US consolidated equity share volume did not trade on any of them. It traded off-exchange, was reported to a FINRA Trade Reporting Facility (TRF) after the fact, and appeared on the tape with a "D" venue code and no book behind it. November 2024 was the first month in which more shares traded off-exchange than on; 2025 was the first full year above half.

Off-exchange trading is two very different businesses that share a reporting facility. The larger is principal dealing: wholesalers such as Citadel Securities, Virtu, G1 Execution Services, Jane Street, Hudson River Trading and Two Sigma Securities that buy retail order flow from brokers and fill it from their own inventory. The smaller is agency crossing on alternative trading systems (ATSs), the "dark pools" run by banks and independent operators where institutions match against each other, usually at the midpoint of the NBBO, without displaying. Cboe's breakdown of the 2025 TRF volume: 18.7% ATS, 81.3% principal dealers.

## Wholesalers and payment for order flow

When you send a marketable order through a retail broker, the broker almost never sends it to an exchange. The SEC's December 2022 order competition proposal (Release 34-96495) put the figure at more than 90% of individual investors' marketable orders routed to a small group of wholesalers. The wholesaler fills the order itself, typically at a price slightly better than the NBBO, and pays the broker for the privilege. That payment is payment for order flow (PFOF), and Rule 606 requires every broker to disclose it quarterly, venue by venue, in cents per hundred shares.

Why is retail flow worth paying for? Because it is uninformed in the aggregate. A market maker on an exchange quotes to everyone, including hedge funds and other market makers who trade only when they know something. A wholesaler that has bought a broker's retail flow faces a pool with far fewer informed traders, so the expected loss to adverse selection per share is smaller, and it can fill inside the NBBO and still profit. The SEC's analysis estimated that wholesalers' price improvement did not fully pass through this lower cost: a "competitive shortfall" of 1.08 basis points per dollar traded, about $1.5 billion a year. That proposal was not adopted, but the estimate remains the best public measurement of what segmentation is worth.

Robinhood Securities' Rule 606 report for the fourth quarter of 2025 shows the machinery for October 2025, S&P 500 stocks: 41.54% of non-directed orders were market orders. Virtu Americas received 47.06% of non-directed orders and paid 91.2325 cents per hundred shares on market orders; G1 Execution Services received 14.21% and paid 103.7570; Jane Street 13.56% and 126.3832; Citadel Securities 10.30% and 53.4429; Hudson River Trading 9.02% and 83.3171; Two Sigma Securities 5.85% and 94.1033. The same table shows different rates for marketable and non-marketable limit orders. These are the numbers as filed; the worked example converts one of them into something you can compare to a spread.

## Dark pools and ATSs

An ATS is a broker-dealer-operated matching venue registered under Regulation ATS rather than as an exchange. Most equity ATSs are dark: they display no quotes, match at or inside the NBBO (frequently the midpoint), and exist so that institutions can trade size without showing it to the book in lesson 1. FINRA publishes weekly volume and trade counts for every ATS, by security, on a two-week delay for Tier 1 NMS stocks, and quarterly aggregates that let you rank venues by shares and average trade size.

The economics of a dark pool are the mirror image of a wholesaler's. There is no dealer taking the other side and no PFOF; the operator earns a small fee per share crossed. The risk to a user is information leakage and adverse selection from other users. The SEC has brought actions against several operators for misrepresenting who was inside their pools and how orders were handled; those cases are the reason you should read an ATS's Form ATS-N, which is public, before assuming "dark" means "protected."

## What prints off-exchange and what it tells you

Off-exchange trades hit the tape a few hundred microseconds to a few seconds after execution, marked with the TRF venue and often at prices with three or four decimals (sub-penny fills are allowed for executions, only quoting is restricted to pennies under Rule 612). A print at 187.1187 in a stock quoting 187.11/187.12 is almost certainly a wholesaler filling a retail buy with $0.0013 of price improvement. A 250,000-share print at exactly the midpoint is likely an ATS cross or a negotiated block. Reading those codes is lesson 6.

What you cannot see is the order flow before it prints: a wholesaler's inventory, an ATS's resting interest, the size of a block being worked. The displayed book is the visible half of the market, and it is now the smaller half.

## Worked example

Start from Cboe's 2025 figures: average daily consolidated volume 17.6 billion shares, off-exchange share 50.6%, of which 18.7% ATS and 81.3% principal dealers.

- Off-exchange shares per day = 17.6 billion × 0.506 = 8.906 billion.
- On-exchange = 17.6 − 8.906 = 8.694 billion, or 49.4% of the total.
- ATS share of the whole market = 0.506 × 0.187 = 0.0946 = 9.5%, i.e. 17.6 × 0.0946 = 1.665 billion shares a day.
- Principal dealer share of the whole market = 0.506 × 0.813 = 0.4114 = 41.1%, i.e. 7.240 billion shares a day.

So for every 100 shares that trade, about 49 cross an exchange book, about 41 are filled by a dealer against its own inventory, and about 9 cross in a dark pool. For comparison, Cboe's April 2023 figures were 45% off-exchange with ATSs at 25% of that, so the dealer segment has grown faster than the ATS segment.

Now the PFOF number. Robinhood Securities, October 2025, S&P 500 market orders, Virtu: 91.2325 cents per hundred shares.

- Per share: 91.2325 / 100 = $0.00912.
- A 200-share market buy in a $250 stock: payment to the broker = 200 × 0.00912 = $1.82. Notional = 200 × 250 = $50,000. Payment as a share of notional = 1.82 / 50,000 = 0.0000365 = 0.36 basis points.
- The same order in a $25 stock: notional $5,000; 1.82 / 5,000 = 3.6 basis points, ten times larger relative to the trade, because PFOF is quoted per share, not per dollar.

Compare to the spread economics from lesson 3. If the NBBO is $0.01 wide on the $250 stock, the half-spread is $0.005, or 0.2 basis points. The wholesaler pays the broker 0.36 basis points, gives you some price improvement inside the spread, and still expects to profit, which is only possible because the flow it bought loses less to informed traders than the displayed quote assumes. And using the SEC's 1.08-basis-point shortfall estimate on the $50,000 order: 50,000 × 0.000108 = $5.40 of price improvement that, in the SEC's model, competition would have delivered and the current structure does not. That is the number the December 2022 proposal was arguing over. It is small on any one order and, at 90% of retail marketable volume, about $1.5 billion a year in aggregate.

## Chart

![Bar chart of the 2025 share of US consolidated equity volume: exchanges 49.4%, off-exchange principal dealers 41.1%, off-exchange ATSs 9.5%, with the April 2023 off-exchange total (45.0%) and the 2025 off-exchange total (50.6%) for comparison. Source: Cboe, 2025 U.S. Equities Year in Review and Off-Exchange Trends (April 2023), both based on FINRA TRF data.](figures/on-vs-off-exchange-share-2025.svg)

Dealers, not dark pools, are the bulk of the off-exchange market. When someone says "half of all trading is in dark pools," the FINRA data says otherwise.

## Sources

- Cboe Global Markets, "2025 U.S. Equities Year in Review" (TRF 50.6% of consolidated volume; 18.7% ATS / 81.3% principal dealers; ADV 17.6 billion shares): https://www.cboe.com/insights/posts/2025-u-s-equities-year-in-review
- SEC, "Proposed Rule to Enhance Order Competition" fact sheet, Release No. 34-96495 (December 2022): https://www.sec.gov/files/34-96495-fact-sheet.pdf
- Robinhood Securities, LLC, SEC Rule 606 report, Q4 2025 (filed on EDGAR): https://www.sec.gov/Archives/edgar/data/1783879/000178387926000007/a287900_606xnmsx2025xq4x.htm
- FINRA, OTC (ATS & Non-ATS) Transparency data: https://www.finra.org/filing-reporting/otc-transparency
