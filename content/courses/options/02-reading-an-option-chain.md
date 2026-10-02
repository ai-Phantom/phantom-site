---
{
  "title": "Reading an Option Chain",
  "duration": "15 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "XYZ is at 100. Which of these is an out-of-the-money (OTM) option?", "opts": ["The 95 call", "The 105 put", "The 105 call", "The 100 call"], "correct": 2, "explain": "A call is OTM when the strike is above the stock price; a put is OTM when the strike is below. The 95 call and 105 put are in the money (ITM); the 100 call is at the money (ATM)."},
    {"q": "An option shows volume 1,840 and open interest 12,400. What does open interest measure?", "opts": ["Contracts traded today", "Contracts outstanding that have not been closed or exercised", "Contracts the market maker is quoting", "Contracts held by retail accounts"], "correct": 1, "explain": "Open interest is the number of contracts currently open, updated overnight by the OCC. Volume is today's trade count and resets each session."},
    {"q": "The XYZ 100 call is quoted 4.08 x 4.24. If you place a market order to buy, you should expect to pay about:", "opts": ["4.08", "4.16", "4.24", "The last trade price"], "correct": 2, "explain": "A market buy order fills at the ask, 4.24. The mid, 4.16, is where a patient limit order often fills, and the last trade may be stale."},
    {"q": "Which quote is the most expensive to trade, measured by spread as a percent of mid?", "opts": ["4.08 x 4.24", "2.11 x 2.21", "0.38 x 0.44", "10.95 x 11.15"], "correct": 2, "explain": "0.06 / 0.41 = 14.6%, far wider in relative terms than 0.16/4.16 = 3.8%, 0.10/2.16 = 4.6% or 0.20/11.05 = 1.8%. Cheap OTM options are usually the costliest to trade."},
    {"q": "Which of the following is a reasonable liquidity screen for a retail-sized order?", "opts": ["Volume above zero at some point this week", "Open interest above the number of contracts you want to trade, and a spread under about 5% of mid", "Any strike listed by the exchange", "Only the strike with the highest last price"], "correct": 1, "explain": "Open interest large relative to your order and a tight relative spread are the two chain columns that predict whether you can get in and out near mid. Volume helps but resets daily."}
  ],
  "task": "Pull up a real chain for any large-cap stock at the nearest monthly expiration and, for the ATM call, write down bid, ask, mid, spread as a percent of mid, volume and open interest."
}
---

## The chain is a price list, not a prediction

An option chain is the table your broker shows for every strike and expiration on an underlying. It looks intimidating because it packs two instruments (calls and puts), a dozen or more strikes, and half a dozen columns into one screen. Read it in the right order and it is simply a price list with a liquidity report attached.

Most brokers lay calls on the left, puts on the right, and strikes down the middle. Expirations sit in tabs or collapsible sections, nearest first. The Phantom Traders signal cards quote a single row of that table, so once you can read the whole chain you can read any card.

## Bid, ask, mid and last

The **bid** is the highest price someone will pay right now; the **ask** (or offer) is the lowest price someone will sell for. You buy at the ask and sell at the bid if you use market orders. The difference is the **spread**, and it is the first cost of every options trade.

The **mid** is (bid + ask) / 2. It is the fairest single estimate of the option's value at that moment, and it is the price the models in Lessons 3 to 8 produce. Limit orders placed at or slightly through the mid frequently fill on liquid contracts because market makers compete for order flow; on illiquid contracts you will pay closer to the ask.

The **last** column is the price of the most recent trade. On an active contract it is a fine sanity check. On a quiet contract it can be hours or days old, and the stock may have moved several dollars since. Never anchor on last; anchor on the current bid and ask.

Always convert the spread to a percentage of the mid. A 0.16 spread on a 4.16 option is 3.8%, tolerable. A 0.06 spread on a 0.41 option is 14.6%, which means the option must gain almost 15% before you are back to flat on a round trip. Lesson 9 turns this into a hard rule.

## Volume and open interest

**Volume** is the number of contracts traded so far today. It resets to zero every session. **Open interest** is the number of contracts that exist, that is, have been opened and not yet closed, exercised or expired. The OCC updates it once overnight, so the figure you see during the day is yesterday's close.

Volume tells you whether the contract is being traded now; open interest tells you whether there is a standing pool of positions you can trade against. For a retail-sized order the practical screens are open interest well above the number of contracts you intend to trade and volume that is not zero. A strike with 12,400 open interest and 1,840 traded today will let you in and out near mid. A strike with 30 open interest and no volume may be quoted, but the quote is an invitation, not a market.

Two patterns worth noticing. Open interest clusters at round strikes and at the monthly expiration; weeklies and odd strikes are thinner. And unusually high volume relative to open interest (say volume 5,000 on open interest 900) means new positions are being opened today, which is often reported as "unusual activity". It is information about flow, not about direction; someone opening a call may be a buyer or a seller.

## Moneyness: ITM, ATM, OTM

**Moneyness** describes where the strike sits relative to the stock price.

- A call is **in the money (ITM)** when the stock is above the strike; it has intrinsic value equal to stock minus strike.
- A put is ITM when the stock is below the strike; intrinsic value is strike minus stock.
- **At the money (ATM)** means the strike closest to the stock price. With XYZ at 100.00, the 100 strike is ATM for both calls and puts.
- **Out of the money (OTM)** means a call with strike above the stock or a put with strike below. Intrinsic value is zero; the whole premium is time value.

Traders abbreviate distance from the money in two ways. In dollars or percent ("5% OTM") and, more usefully, in delta ("the 35-delta call"). Lesson 4 explains why delta is the better ruler. For now, read the chain vertically: as you move down the call column from low strikes to high, price falls, from deep ITM near the stock price itself toward zero far OTM. The put column does the reverse.

## Implied volatility and the Greeks columns

Most chains let you add columns for implied volatility (IV), delta, gamma, theta and vega. They are computed by the broker from the mid price using a model, and they update tick by tick. Lessons 4 to 7 teach each one; for now note that a chain with IV shown lets you compare the price of options on different stocks on a common scale. A 4.16 call on a $100 stock and a 41.60 call on a $1,000 stock may be identical in every way but the share price.

## Worked example

Here is the XYZ November 6, 2026 chain (45 DTE) as of Tuesday 22 September 2026, with XYZ at $100.00. As in Lesson 1, this is a representative chain built from a pricing model at 28% implied volatility and a 4% rate, not a live quote, so that every lesson's arithmetic ties out. Volume and open interest are illustrative.

Reading the 100 call row:

1. **Bid 4.08 / ask 4.24.** Mid = (4.08 + 4.24) / 2 = **4.16**. Spread = 4.24 - 4.08 = 0.16. Relative spread = 0.16 / 4.16 = **3.8%**.
2. **Volume 1,840, open interest 12,400.** Liquid: a ten-lot is 0.08% of open interest.
3. **Moneyness.** Stock 100.00, strike 100: ATM. Intrinsic = max(100.00 - 100, 0) = **0**. The entire 4.16 is time value.
4. **Cost of one contract at mid:** 4.16 x 100 = $416. At the ask: $424. The 0.08 you save by getting filled at mid is $8 per contract, 1.9% of the trade.

Reading the 110 call row:

1. **Bid 0.96 / ask 1.04.** Mid **1.00**. Spread 0.08, relative spread 0.08 / 1.00 = **8.0%**, more than double the ATM figure.
2. **Volume 610, open interest 4,900.** Still tradable.
3. **Moneyness.** Strike 110 is 10% above the stock: OTM. Intrinsic 0; all time value.

Reading the 95 put row:

1. **Bid 1.64 / ask 1.74.** Mid **1.69**. Spread 0.10, relative spread 0.10 / 1.69 = **5.9%**.
2. **Moneyness.** A put at 95 with stock at 100 is 5% OTM. Intrinsic 0.

Reading the 95 call row:

1. **Bid 7.05 / ask 7.25.** Mid **7.15**. Spread 0.20, relative spread 0.20 / 7.15 = **2.8%**.
2. **Moneyness.** ITM by 5.00. Intrinsic = 100.00 - 95 = **5.00**; time value = 7.15 - 5.00 = **2.15**. Lesson 3 explains that split.

Notice what the relative spreads did: 2.8% for the ITM call, 3.8% ATM, 5.9% for the 5%-OTM put, 8.0% for the 10%-OTM call. The cheaper the option, the larger the toll on the way in and out.

## Table

XYZ Nov 6, 2026 expiration (45 DTE), XYZ at 100.00. Representative chain; mids are the model values used throughout the course.

| Strike | Call bid | Call ask | Call mid | Call vol | Call OI | Put bid | Put ask | Put mid | Put vol | Put OI |
|---|---|---|---|---|---|---|---|---|---|---|
| 85 | 15.45 | 15.71 | 15.58 | 40 | 620 | 0.14 | 0.18 | 0.16 | 380 | 5,100 |
| 90 | 10.95 | 11.15 | 11.05 | 120 | 1,450 | 0.58 | 0.64 | 0.61 | 910 | 8,300 |
| 95 | 7.05 | 7.25 | 7.15 | 330 | 3,100 | 1.64 | 1.74 | 1.69 | 1,220 | 9,700 |
| 100 | 4.08 | 4.24 | 4.16 | 1,840 | 12,400 | 3.61 | 3.73 | 3.67 | 1,510 | 10,800 |
| 105 | 2.11 | 2.21 | 2.16 | 1,270 | 9,200 | 6.55 | 6.73 | 6.64 | 260 | 2,400 |
| 110 | 0.96 | 1.04 | 1.00 | 610 | 4,900 | 10.35 | 10.57 | 10.46 | 70 | 900 |
| 115 | 0.38 | 0.44 | 0.41 | 290 | 2,700 | 14.70 | 14.98 | 14.84 | 20 | 310 |

## A reading routine

Before you look at any strike, look at three things: the stock price, the expiration's DTE, and the ATM straddle (ATM call mid plus ATM put mid, here 4.16 + 3.67 = 7.83). The straddle is the market's rough price for a one-way move by expiration, a number you will use in Lesson 8. Then go to the strike you care about and read bid, ask, spread-as-percent, open interest, and moneyness, in that order. It takes twenty seconds and it prevents most of the expensive mistakes that follow from reading "last" or from trading a strike nobody else is in.

## Sources

- Cboe Global Markets, Options Institute, reading an option chain and quote data: https://www.cboe.com/education/
- Options Clearing Corporation, daily volume and open interest statistics: https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest
- FINRA, Investor Insights on options: https://www.finra.org/investors/investing/investment-products/options
- U.S. Securities and Exchange Commission, Investor Bulletin: An Introduction to Options: https://www.sec.gov/investor/alerts/ib_introductionoptions.pdf
