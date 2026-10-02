---
{
  "title": "Regulation NMS, the NBBO, Order Protection and Maker-Taker",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "What does Rule 611 of Regulation NMS require?", "opts": ["All orders must route to the NYSE", "Trading centers must have procedures to prevent executing at prices inferior to protected quotations on other venues", "Brokers must charge no more than $0.003 per share", "Stocks must quote in pennies"], "correct": 1, "explain": "Rule 611 is the Order Protection (trade-through) Rule. It protects the best displayed, automated quotations across venues."},
    {"q": "Under the 2005 Rule 610(c), the maximum fee for accessing a protected quote in a stock priced at $1 or more is:", "opts": ["$0.001 per share", "$0.003 per share", "$0.01 per share", "1% of notional"], "correct": 1, "explain": "The access fee cap is three tenths of a cent per share. The 2024 amendments cut it to $0.001, with compliance delayed to November 2026."},
    {"q": "Nasdaq charges $0.0030 per share to remove liquidity and pays a baseline $0.0018 (Tape A/B) to add displayed liquidity. On a 10,000-share order, what is the difference between taking and making?", "opts": ["$12", "$18", "$30", "$48"], "correct": 3, "explain": "Taking costs 10,000 × 0.0030 = $30; making earns 10,000 × 0.0018 = $18. The swing is $48."},
    {"q": "Why does maker-taker pricing create a conflict for a broker routing your limit order?", "opts": ["It does not", "The broker collects the rebate on your posted order but you bear the lower fill probability at a venue chosen for its rebate", "Rebates are illegal", "Rebates are paid to you directly"], "correct": 1, "explain": "The rebate goes to the routing broker, not the customer, so the broker's incentive can diverge from the customer's fill quality. Rule 606 reports exist to disclose it."},
    {"q": "What did the SEC propose on June 11, 2026?", "opts": ["To ban payment for order flow", "To rescind Rule 611 and Rule 610(e)", "To raise the access fee cap", "To merge the exchanges"], "correct": 1, "explain": "The June 2026 fact sheet proposes rescinding the trade-through rule and the lock/cross restrictions, with a 60-day comment period."}
  ],
  "task": "Find your broker's most recent Rule 606 report and write down the top three venues for your order type and the net payment per hundred shares each one paid or charged."
}
---

## The problem Reg NMS was written for

By the early 2000s, US stocks traded on several exchanges and ECNs at once. Nothing forced a venue to respect a better price displayed elsewhere, quotes updated at human speeds on the NYSE floor while ECNs were electronic, and a market order could easily fill at a worse price than one visible a few miles away. Regulation NMS, adopted by the SEC on June 9, 2005 (Release 34-51808) and effective August 29, 2005, rebuilt the plumbing. Four rules matter for a trader.

Rule 611, the Order Protection Rule, requires trading centers to have policies to prevent executing trades at prices inferior to a protected quotation displayed by another venue. A protected quotation is the best displayed, immediately and automatically accessible bid or offer on each exchange. The practical effect is that no venue may "trade through" a better price on another exchange; it must either match it or route to it.

Rule 610, the Access Rule, requires fair access to quotations, caps the fee for accessing a protected quote at $0.003 per share for stocks at $1 or more (Rule 610(c)), and requires exchanges to prohibit members from displaying quotes that lock or cross another venue's protected quote (Rule 610(e)).

Rule 612, the Sub-Penny Rule, bars quoting in increments finer than $0.01 for stocks priced at $1 or more, which is why the book in lesson 1 stepped in pennies.

Rule 603 governs consolidated market data: every exchange must send its best quotes and trades to a securities information processor (SIP), and the SIP computes the National Best Bid and Offer, the NBBO, which is the reference price for everything from order protection to Rule 605 execution-quality statistics to the price improvement a wholesaler claims when it fills your order.

## The NBBO and the exchanges

The NBBO is the best bid and the best ask across all exchanges at a moment in time, as computed by the SIP. It is not the best price available anywhere, because hidden orders, odd lots below the round-lot size, and off-exchange liquidity do not count toward it. It is the best displayed, protected price.

For most of 2020 through 2024 there were sixteen exchanges trading US equities: NYSE, NYSE Arca, NYSE American, NYSE National and NYSE Chicago; Nasdaq, Nasdaq BX and Nasdaq PSX; Cboe BZX, BYX, EDGX and EDGA; IEX; MEMX; MIAX Pearl; and LTSE. Sixteen matching engines with sixteen books for the same stock, tied together by Rule 611 so that the best price on any of them is protected on all of them. The SEC's current list of Section 6(a) registrants runs to 29, including options-only exchanges and 2025 entrants such as 24X National Exchange, the Texas Stock Exchange and Green Impact Exchange, so the number you should carry is "many, all protected," not any particular count.

Fragmentation is the price of competition. Each exchange competes on fees, speed, order types and data, and each publishes a fee schedule that determines what it costs to trade there.

## Maker-taker

Most exchanges charge a fee to the order that removes liquidity (the taker) and pay a rebate to the order that was resting (the maker). The fee is bounded above by Rule 610(c) at $0.003 per share; the rebate is whatever the exchange chooses, usually a little less than the fee so the exchange keeps the difference.

Nasdaq's price list for securities at $1.00 or more charges $0.0030 per share to remove liquidity for all participants. Adding displayed liquidity earns a baseline credit of $0.0018 per share in Tape A and B securities and $0.0013 in Tape C (Nasdaq-listed), rising through volume tiers to $0.00305 per share for members whose displayed adding volume exceeds 1.50% of consolidated volume. Note that top tier: it exceeds the take fee. Nasdaq is willing to lose a fraction of a cent on the highest-volume makers to attract their quotes, because their quotes attract takers who pay full freight.

The inverse model exists too. "Taker-maker" exchanges (Cboe BYX and EDGA, Nasdaq BX) pay the taker and charge the maker, which attracts orders that want to remove liquidity cheaply and makers who want queue position at a price where fewer people are resting.

Why should you care about fractions of a cent? Two reasons. First, they add up: a market maker quoting a million shares a day at a $0.0018 rebate collects $1,800 a day for being at the front of the queue, which is a large part of the reason the queue is long. Second, the rebate is paid to whoever routed the order, which is your broker, not you. A broker choosing where to post your limit order has a financial reason to prefer the venue with the highest rebate, which is not necessarily the venue where your order fills fastest. Rule 606 reports, which every retail broker must publish quarterly, disclose exactly those payments; the task at the end of this lesson asks you to read yours.

## What changed in 2024 and what is proposed for 2026

On September 18, 2024 the SEC adopted amendments (Release 34-101070) that set a $0.005 minimum tick for stocks whose quoted spread is narrow enough (the SEC estimated about 74% of stocks would move to half-penny ticks), cut the Rule 610(c) access fee cap from $0.003 to $0.001 per share, and accelerated the round-lot and odd-lot data changes from the 2020 market data rule. Compliance was originally November 2025 and was subsequently delayed to November 2026.

Then on June 11, 2026 the SEC proposed to rescind Rule 611 entirely, along with Rule 610(e)'s lock-and-cross restrictions, arguing that the 2005 rules had contributed to cost, complexity and fragmentation and that competition should shape routing instead. The comment period runs 60 days from Federal Register publication. If adopted, order protection would become a matter of broker best-execution duty rather than a venue-level prohibition. This course is written as of September 2026, so treat the trade-through rule as current law with a stated expiry risk, and check the SEC's site before relying on it.

## Worked example

You send a 10,000-share order in a $50 stock to Nasdaq. Compare the exchange economics of taking versus making, using Nasdaq's published rates for securities at or above $1.00.

Taking (marketable order that removes liquidity):

- Fee = 10,000 × $0.0030 = $30.00.
- As a share of notional: 30 / (10,000 × 50) = 30 / 500,000 = 0.006% = 0.6 basis points.
- Plus the half-spread you cross: at a $0.01 spread, 10,000 × 0.005 = $50.00, or 1.0 basis point.
- Total explicit cost of immediacy: $80.00, 1.6 basis points, before any price impact.

Making (non-marketable limit that rests and is filled):

- Baseline credit (Tape A/B) = 10,000 × $0.0018 = +$18.00.
- Top tier credit = 10,000 × $0.00305 = +$30.50.
- You also earn the half-spread instead of paying it: +$50.00.
- Net at baseline: +$68.00 (1.36 basis points earned), if and only if you get filled and the price does not move against you while you wait.

The swing between taking at baseline and making at baseline is 30 + 18 = $48.00 on a $500,000 order, or roughly one basis point. That is the fee half of the maker-taker incentive. The other half is the spread, and it is why lesson 5's market makers exist.

Check the same order against the access fee cap. The 2005 cap is $0.003; Nasdaq's take fee is exactly at it. Under the 2024 amendments the cap drops to $0.001, so the same 10,000-share take would cost at most $10.00. The rebate, which is not capped by rule, would have to shrink too, since exchanges cannot pay out more than they collect for long. That is the mechanism by which a regulatory fee cap reaches the queue in lesson 1: lower rebates mean fewer resting orders competing for the front, and less displayed depth.

## Chart

![Flow diagram of a retail marketable order under Reg NMS: the order goes to the broker's router, then to a wholesaler or an exchange, is checked against the NBBO under Rule 611 with the Rule 610 access fee cap, and prints on the SIP (exchange) or a FINRA TRF (off-exchange). Source: SEC Reg NMS Release 34-51808; SEC order competition fact sheet, December 2022.](figures/retail-order-routing-path.svg)

The diagram is the path in the abstract; lesson 4 puts numbers on each box.

## Sources

- SEC, Regulation NMS adopting release, Release No. 34-51808 (June 9, 2005): https://www.sec.gov/files/rules/final/34-51808.pdf
- SEC, "Regulation NMS Reforms" fact sheet, Release No. 34-105655 (June 11, 2026), proposing rescission of Rules 611 and 610(e): https://www.sec.gov/files/34-105655-fact-sheet.pdf
- Nasdaq Trader, "Price List – Trading Connectivity" (remove fee $0.0030; add credits $0.0013–$0.00305): https://www.nasdaqtrader.com/Trader.aspx?id=PriceListTrading2
- SEC Division of Trading and Markets, list of National Securities Exchanges registered under Section 6(a): https://www.sec.gov/about/divisions-offices/division-trading-markets/national-securities-exchanges
