---
{
  "title": "How Markets Actually Work",
  "duration": "14 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "When you buy 10 shares of Apple through your broker, where does your money go?", "opts": ["To Apple, which uses it to fund operations", "To the investor or market maker who sold you the shares", "To the exchange as a listing fee", "To the SEC as a transaction tax"], "correct": 1, "explain": "Secondary-market trades move money between investors. Apple only received cash when it originally issued the shares."},
    {"q": "What is the NBBO?", "opts": ["The price at which the last trade printed", "The average of all bids and asks across the day", "The highest bid and lowest ask across all US exchanges at that moment", "The opening auction price on the primary listing exchange"], "correct": 2, "explain": "The National Best Bid and Offer is assembled from every exchange's quotes. Regulation NMS requires that market orders not be executed at prices worse than it."},
    {"q": "Why does a stock price rise?", "opts": ["Because there are more buyers than sellers", "Because the company reported good news", "Because buyers are willing to pay more than the lowest resting ask, consuming the offers above it", "Because the market maker raised the price"], "correct": 2, "explain": "Every trade has exactly one buyer and one seller. Price moves when aggressive orders exhaust the resting liquidity at one price and reach the next."},
    {"q": "A trade executed on Tuesday 31 December 2024 settled on which day, under the T+1 rule?", "opts": ["Tuesday 31 December 2024", "Wednesday 1 January 2025", "Thursday 2 January 2025", "Friday 3 January 2025"], "correct": 2, "explain": "T+1 means one business day after the trade. 1 January is a market holiday, so settlement rolled to Thursday 2 January."},
    {"q": "Which organisation writes and enforces the conduct rules that your broker must follow, under SEC oversight?", "opts": ["The Federal Reserve", "FINRA", "The New York Stock Exchange", "SIPC"], "correct": 1, "explain": "FINRA is the self-regulatory organisation for broker-dealers. SIPC insures customer assets if a broker fails; it does not write conduct rules."}
  ],
  "task": "Open your broker's app, find one stock you recognise, and write down its last price, the time of that price, and which exchange it is listed on."
}
---

## What a share is

A share of stock is a fractional claim on a company: a slice of its assets after debts, a vote at its annual meeting, and a share of any cash it chooses to pay out. Apple reported 15,115,823,000 shares outstanding on its fiscal 2024 annual report cover page. One share is therefore one fifteen-billionth of Apple. That is small, but it is real ownership, and it is why the price of a share ultimately tracks what the business earns.

The price you see on a screen is not set by Apple, by the exchange, or by a committee. It is the last price at which one owner agreed to sell and another agreed to buy. Everything else in this lesson explains how that agreement gets made, thousands of times per second, across dozens of venues.

## Primary market versus secondary market

Companies raise money by selling shares exactly once per share: at the initial public offering (IPO) or in a later follow-on offering. That is the primary market. Cash flows from investors to the company.

Every trade after that is the secondary market. When you buy Apple, your money goes to whoever sold you the shares, not to Apple. The company gets nothing from your purchase and loses nothing from your sale. Its interest in the secondary price is indirect: a higher price makes it cheaper to raise future capital, lets it pay employees in stock, and helps management keep their jobs.

> **Callout:** Almost all of the volume you will ever trade is secondary-market volume. You are trading against other investors, not with the company.

## Where trades actually happen

The United States has 16 registered stock exchanges. The three families that matter are NYSE (including NYSE Arca), Nasdaq, and Cboe (the BZX, BYX, EDGX and EDGA exchanges). A company lists on one exchange, but its shares trade on all of them, plus off-exchange venues.

Off-exchange trading includes:

- **Wholesale market makers** such as Citadel Securities and Virtu, who buy retail order flow from brokers and fill it from their own inventory.
- **Alternative trading systems (ATS)**, often called dark pools, where institutions match large orders without displaying them.
- **Broker internalisation**, where a broker matches its own customers against each other.

Roughly 40 to 50 percent of US share volume has traded off-exchange in recent years, and most retail market orders never touch an exchange at all. That is legal and tightly regulated, but you should know it: when you send a market order from a commission-free app, a wholesaler will usually be the counterparty.

## The National Best Bid and Offer

Because one stock trades on many venues, the SEC's Regulation NMS (National Market System) stitches the quotes together. At any moment the highest displayed bid and the lowest displayed ask across all exchanges form the **NBBO**. Rule 611 of Reg NMS, the Order Protection Rule, prohibits a venue from executing a trade at a price worse than a protected quote available elsewhere. Wholesalers who fill retail orders are expected to match or improve on the NBBO.

The practical result: for a large, liquid stock you will get a fill at or inside the national best price no matter which broker you use. The broker's routing choices matter more for how much price improvement you get and for thinly traded names.

## Table

Who is on the other side of your trade, what they want, and how much of the market they are.

| Participant | What they want | Share of activity |
| --- | --- | --- |
| Retail investors | Own businesses, trade around news, save for goals | Roughly 15 to 25 percent of volume, higher in meme-stock episodes |
| Institutions (mutual funds, pensions, endowments, insurers) | Deploy large pools of capital slowly, minimise market impact | The largest holders of most companies |
| Hedge funds | Absolute returns, often long-short or event-driven | Frequent, sometimes leveraged trading |
| Market makers and HFT firms | Earn the bid-ask spread and rebates, stay flat by day end | The majority of quotes and a large share of trades |
| Corporates | Buy back their own stock, issue shares for compensation | Apple alone repurchased about 95 billion dollars of stock in fiscal 2024 |
| Index funds | Track a benchmark, trade only on rebalances and flows | Own a quarter or more of many large companies |

The table above is the single most useful mental model in this course. When you trade, you are not trading against "the market". You are trading against one of these groups, each with different goals, time horizons and information. A market maker is happy to sell you shares at the ask and buy them back at the bid a second later; a pension fund is happy to hold for 30 years; a hedge fund may have spent three months modelling the company. Ask yourself, before every trade, which of them is likely on the other side and why they are willing to take it.

## Trading hours and the auctions

Regular hours are 9:30 a.m. to 4:00 p.m. Eastern, Monday to Friday, excluding exchange holidays. Two moments matter more than the rest of the day combined:

- **The opening auction** at 9:30, where the listing exchange collects all overnight orders and sets a single opening price that maximises matched volume.
- **The closing auction** at 4:00, which sets the official closing price used for index funds, mutual fund NAVs, and most performance reporting. The close is frequently the highest-volume minute of the day because index funds must trade there.

Extended hours (roughly 4:00 a.m. to 9:30 a.m. and 4:00 p.m. to 8:00 p.m. Eastern, depending on the broker) have far less volume, wider spreads, and no NBBO protection in the same sense. Earnings are usually released in these windows, which is why the biggest single-day moves in a stock often happen before most people are awake.

## Why prices move

"More buyers than sellers" is the most common wrong explanation. Every trade has exactly one buyer and one seller, so the counts are always equal. What actually happens:

1. Resting limit orders sit in the order book at each price: bids below the current price, asks above it.
2. An aggressive order (a market order, or a limit priced to cross) consumes the resting orders at the best price.
3. If it is larger than what rests at that price, it walks to the next price level. The last price printed moves.
4. Everyone else updates their own orders in response, and the book reshapes.

Price therefore reflects the balance of urgency, not the balance of headcount. News moves prices because it changes how urgent holders are to sell and how eager outsiders are to buy, and because market makers immediately widen their quotes when uncertainty spikes.

## The plumbing after the trade

A fill is a promise, not a transfer. After your order executes:

1. Your broker reports the trade to the National Securities Clearing Corporation (NSCC), a subsidiary of DTCC, which becomes the buyer to every seller and the seller to every buyer.
2. NSCC nets every broker's trades for the day into a single obligation per security.
3. On settlement day, the Depository Trust Company (DTC) moves the shares between brokers' accounts and cash moves the other way.

Since 28 May 2024, US equities settle on **T+1**: one business day after the trade date. Before that it was T+2. Settlement drives several rules you will meet later, including when you can withdraw sale proceeds and when a stock goes ex-dividend.

## Who regulates it

- **The SEC** writes the federal rules (Reg NMS, disclosure rules, the settlement cycle) and can bring enforcement cases.
- **FINRA** is the self-regulatory organisation for broker-dealers. It licenses brokers, writes conduct rules such as the margin and pattern-day-trading rules, and runs BrokerCheck, where you can look up any broker's disciplinary history.
- **The exchanges** are themselves self-regulatory organisations with their own rulebooks.
- **SIPC** protects customer assets up to 500,000 dollars (including 250,000 dollars cash) if a broker fails. It does not protect against losses from price moves.

## Worked example

You decide to buy 10 shares of Apple (AAPL) at the close on Tuesday, 31 December 2024. AAPL's official closing price that day was 250.42 dollars, so the trade value was 2,504.20 dollars.

What happened, step by step:

1. Your broker routed the order. If it was a market order from a retail app, it most likely went to a wholesaler, who filled it at or slightly better than the NBBO ask. If the NBBO was 250.41 bid by 250.42 ask, a fill at 250.415 would represent half a cent of price improvement, or 5 cents on the whole order.
2. The trade was reported to the consolidated tape within a fraction of a second and to NSCC for clearing.
3. Wednesday, 1 January 2025 was a market holiday, so T+1 settlement fell on Thursday, 2 January 2025. On that day DTC moved 10 shares into your broker's account, held in "street name" on your behalf, and 2,504.20 dollars moved out.
4. From that point you owned ten fifteen-billionths of Apple, roughly 0.00000007 percent. Apple's next dividend after that date, 25 cents per share, would arrive in your account provided you held the shares through the ex-dividend date.

Notice what did not happen: Apple received nothing, no exchange listing fee was charged to you, and the counterparty was almost certainly a market maker or another investor, not the company.

## Sources

- SEC Office of Investor Education, "How Stock Markets Work": https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work
- SEC, Regulation NMS adopting release (Rule 611, Order Protection): https://www.sec.gov/rules/final/34-51808.pdf
- SEC, "Shortening the Securities Transaction Settlement Cycle" (T+1): https://www.sec.gov/tplus1
- NYSE, Trading Hours and Calendars: https://www.nyse.com/markets/hours-calendars
