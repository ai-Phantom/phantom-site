---
{
  "title": "Reading a Stock Quote",
  "duration": "13 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "A quote shows bid 49.95 and ask 50.05. If you send a market buy and then immediately a market sell, roughly what do you lose per share, ignoring price improvement?", "opts": ["Nothing, the price did not change", "0.05", "0.10", "0.20"], "correct": 2, "explain": "You buy at the ask (50.05) and sell at the bid (49.95). The round trip costs the full spread of 0.10 per share."},
    {"q": "Which number in a quote is the one most people mistakenly treat as the price they will actually pay?", "opts": ["The bid", "The last trade price", "The ask", "The previous close"], "correct": 1, "explain": "The last price is history. A buyer pays the ask, a seller receives the bid, and both can differ from the last print."},
    {"q": "AAPL closed at 250.42 with a one-cent spread. Expressed in basis points of the price, the spread is closest to:", "opts": ["0.4 basis points", "4 basis points", "40 basis points", "400 basis points"], "correct": 0, "explain": "0.01 divided by 250.42 is 0.00004, which is 0.004 percent, or 0.4 basis points."},
    {"q": "A stock shows volume of 120,000 shares against a 30-day average of 2,000,000 at 3:30 p.m. What is the most reasonable reading?", "opts": ["Heavy institutional buying", "A halt is likely", "Unusually quiet trading today; check for a holiday-shortened session or missing data", "The stock has been delisted"], "correct": 2, "explain": "Volume far below average late in the day means little interest or a data problem. It says nothing by itself about direction."},
    {"q": "Market capitalisation is calculated as:", "opts": ["Share price multiplied by shares outstanding", "Share price multiplied by daily volume", "Total assets minus total liabilities", "Annual revenue multiplied by the P/E ratio"], "correct": 0, "explain": "Market cap is what the market says the whole equity is worth: price times the number of shares that exist."}
  ],
  "task": "Pull up a Level 1 quote for one large-cap stock and one stock under 2 billion dollars in market cap, and write down the spread of each as a percentage of price."
}
---

## The quote is a snapshot, not a price

A stock quote is a bundle of numbers describing the state of the order book and the day's trading at one instant. Beginners read it as "the price is 250.42". Professionals read it as "the last trade was 250.42, someone will currently pay 250.41, someone will currently sell at 250.42, and here is how much has traded and how those numbers compare to normal". The difference decides whether you get filled at the price you expected.

This lesson walks through every field on a standard Level 1 quote, explains what each one is telling you, and shows how to turn the bid-ask spread into a cost you can compare across stocks.

## The core fields

**Last (or last trade).** The price of the most recent transaction, with its time and size. During regular hours it updates continuously; after 4:00 p.m. Eastern it usually shows the official closing auction price, and a separate field may show after-hours trades.

**Bid.** The highest price a buyer is currently willing to pay, and **bid size**, the number of shares wanted at that price. If you sell with a market order, this is roughly what you receive.

**Ask (or offer).** The lowest price a seller is currently willing to accept, and **ask size**. If you buy with a market order, this is roughly what you pay.

**Spread.** Ask minus bid. It is the market maker's compensation and your immediate cost of getting in and out. A one-cent spread on a 250-dollar stock is nearly free; a 20-cent spread on a 10-dollar stock is a two-percent round trip.

**Change and percent change.** Last price minus the previous official close. Note that "previous close" is the last regular-session close, so a stock that moved after hours shows a large change at 9:30 the next morning even though the news is hours old.

**Open, high, low.** The first regular-session trade and the day's extremes. The relationship between them is the day's candle on a chart.

**Volume.** Shares traded so far today in the regular session, sometimes including pre-market. Compare it to **average volume** (typically a 10-, 30- or 90-day average) before drawing any conclusion. Volume matters for two reasons: it tells you whether today is unusual, and it tells you how large a position you can trade without moving the price yourself.

**52-week high and low.** The extremes over the trailing year. Useful for context, dangerous as a signal on their own.

**Market capitalisation.** Share price multiplied by shares outstanding. It is the market's valuation of the entire company's equity and the first number to look at when deciding whether a company is large, mid or small; the next lesson on order types uses it, and Lesson 4 builds on it.

**Shares outstanding and float.** Outstanding is every share that exists. Float excludes shares held by insiders and other restricted holders, so it is the number actually available to trade. A small float with heavy volume is a recipe for violent moves.

## Level 1 versus Level 2

What we have described is Level 1: the best bid, best ask, and last trade. Level 2 shows the full depth of the book at each exchange or the aggregated depth by price: how many shares are bid at 250.40, 250.39, 250.38 and so on. Most brokers offer Level 2 for a fee or free with activity. For a beginner it is more distraction than information. What you need from it is one idea: the displayed size at the best bid and ask is the amount you can trade at that price right now. An order larger than that will walk down the book.

## Round lots, odd lots and the quote you see

Historically, the NBBO only counted orders of 100 shares or more (a round lot). Smaller odd-lot orders were invisible to the consolidated quote even if they were at better prices. This matters for high-priced stocks: 100 shares of a 1,000-dollar stock is 100,000 dollars, so most retail orders were odd lots and did not set the quote.

The SEC amended Regulation NMS in 2024 to define round lots by price: 100 shares for stocks priced at 250 dollars or less, 40 shares from 250.01 to 1,000 dollars, 10 shares from 1,000.01 to 10,000 dollars, and 1 share above that. It also required odd-lot quotes to be disseminated. Compliance dates ran into late 2025. The practical point: for high-priced stocks the quote you see now reflects more of the true book than it used to, but small orders at better prices can still exist. Your limit order will interact with them; your assumptions about "the" price should not depend on them.

## Turning the spread into a cost

The spread is only meaningful relative to the price. Convert it to basis points (one basis point is one hundredth of one percent):

spread in basis points = (ask minus bid) divided by the midpoint, multiplied by 10,000.

A spread of 0.01 on a 250-dollar stock is 0.4 basis points. A spread of 0.05 on a 5-dollar stock is 100 basis points, one full percent. Trading the second stock ten times costs ten percent of your capital in spread alone before any price movement. For a beginner this single calculation eliminates most of the tickers that cause trouble.

> **Callout:** The spread is the cost of immediacy. A limit order that rests at the bid can avoid paying it, at the risk of not being filled. Lesson 3 covers that trade-off.

## Table

The fields of a Level 1 quote, and the question each one answers.

| Field | What it is | The question to ask |
| --- | --- | --- |
| Last | Most recent trade price and time | How stale is this? Is it a regular-session or after-hours print? |
| Bid and bid size | Best resting buy order and its size | What will I get if I sell right now, and for how many shares? |
| Ask and ask size | Best resting sell order and its size | What will I pay if I buy right now, and for how many shares? |
| Spread | Ask minus bid | What is the round-trip cost, in basis points of price? |
| Change | Last minus previous regular close | Did the move happen today or overnight? |
| Volume versus average volume | Shares traded today versus normal | Is today unusual? Can I trade my size without moving it? |
| 52-week range | Trailing-year high and low | Where is today's price in context? |
| Market cap | Price times shares outstanding | How big is the company? What kind of holders own it? |
| Float | Shares actually available to trade | Could a small amount of buying move this violently? |

## Worked example

Apple (AAPL) on Tuesday, 31 December 2024, the last trading day of the year.

Recorded numbers from that session: the official close was 250.42 dollars, down 1.78 dollars (0.71 percent) from the prior close of 252.20. Regular-session volume was roughly 39 million shares, below AAPL's typical daily average of about 50 million that quarter, which is normal for a holiday-week session. Apple's most recent share count on its fiscal 2024 annual report was 15,115,823,000, so the market capitalisation at the close was about 3.79 trillion dollars (250.42 multiplied by 15.116 billion).

Representative numbers, typical for AAPL at that time rather than a recorded snapshot: a bid of 250.41 and an ask of 250.42 with several hundred shares displayed on each side. That is a one-cent spread.

Reading it:

- Spread cost: 0.01 divided by 250.415 is 0.00004, or 0.4 basis points. Buying 10 shares and immediately selling would cost about 10 cents in spread. For practical purposes AAPL is free to trade.
- Size: if the ask shows 300 shares, a market buy of 10 shares clears without moving the price. A market buy of 5,000 shares would walk up the book.
- Volume: 39 million against a 50 million average tells you the session was quiet, not that anything was wrong.
- Context: the 52-week range that day ran from about 164 dollars to about 260 dollars, so the close sat near the top of the year's range. That is context, not a signal.

Now compare a hypothetical thin stock: a 4-dollar company with a bid of 3.98 and an ask of 4.06, an 8-cent spread. That is 8 divided by 4.02, or 199 basis points, nearly two percent per round trip, 500 times AAPL's cost. Same broker, same order type, a completely different game.

## What the quote cannot tell you

A quote says nothing about why the price is where it is, whether the company is cheap or expensive, or where it will be tomorrow. It tells you the cost and feasibility of transacting right now. That is exactly what you need before you press the button, and nothing more. The lessons on earnings and valuation cover the "why"; the lesson on order types covers how to act on what the quote shows.

## Sources

- SEC Office of Investor Education, glossary entry "Bid-Ask Spread" and related terms: https://www.investor.gov/introduction-investing/investing-basics/glossary
- SEC, Regulation NMS: Minimum Pricing Increments, Access Fees, and Transparency of Better Priced Orders (round-lot and odd-lot amendments, 2024): https://www.sec.gov/rules-regulations/2024/09/s7-30-22
- FINRA, "Stocks: Understanding the Basics": https://www.finra.org/investors/investing/investment-products/stocks
- Apple Inc., Form 10-K for fiscal year 2024 (cover page share count): https://investor.apple.com/sec-filings/default.aspx
