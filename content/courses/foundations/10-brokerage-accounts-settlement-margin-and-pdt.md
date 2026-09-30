---
{
  "title": "Brokerage Accounts, Settlement, Margin and the PDT Rule",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "In a cash account you sell a stock on Monday and use the proceeds to buy another stock the same day, then sell that second stock on Tuesday morning. Under T+1 this is:", "opts": ["Perfectly fine", "A good-faith violation, because the second purchase was funded with unsettled proceeds that you then sold before they settled", "A pattern day trade", "A margin call"], "correct": 1, "explain": "Monday's sale settles Tuesday. Selling the second stock before that settlement means you sold something you had not yet paid for with settled funds. Three such violations in twelve months typically trigger a 90-day restriction."},
    {"q": "Regulation T allows you to borrow up to what fraction of a stock purchase in a margin account?", "opts": ["25 percent", "50 percent", "75 percent", "100 percent"], "correct": 1, "explain": "Reg T sets initial margin at 50 percent: you must put up at least half. FINRA's 25 percent maintenance requirement, and brokers' higher house requirements, apply after the purchase."},
    {"q": "You buy 19,810 dollars of stock with 10,000 dollars of your own cash on margin. With a 30 percent house maintenance requirement, a margin call arrives when the position falls to roughly:", "opts": ["17,800 dollars", "14,000 dollars", "12,500 dollars", "9,800 dollars"], "correct": 1, "explain": "The loan is 9,810 dollars. Equity is value minus loan; equity divided by value must stay above 0.30, so value must stay above 9,810 divided by 0.70, about 14,015 dollars, a 29 percent decline."},
    {"q": "The pattern day trader rule applies when you make four or more day trades in five business days in a:", "opts": ["Cash account", "Margin account, when those trades are more than 6 percent of your total trades in that period", "Retirement account", "Any account with under 25,000 dollars"], "correct": 1, "explain": "FINRA Rule 4210 defines a pattern day trader by margin-account activity. A cash account is not subject to the rule but is limited by settled funds instead."},
    {"q": "SIPC protection covers:", "opts": ["Losses from a stock falling in price", "Up to 500,000 dollars of securities and cash, including up to 250,000 dollars in cash, if your broker fails", "All losses in a margin account", "Losses from a bad fill"], "correct": 1, "explain": "SIPC protects custody, not performance. It returns your assets if the broker becomes insolvent; it does nothing about market losses."}
  ],
  "task": "Log in to your broker, find whether your account is cash or margin, and write down the house maintenance requirement and margin interest rate from the account disclosures."
}
---

## Choosing a broker

The broker is the intermediary that holds your cash and securities, routes your orders, and reports to the tax authorities. Before opening an account, check four things:

1. **Registration.** Look the firm up on FINRA BrokerCheck. It should be a FINRA member and SIPC member. If it is not, stop.
2. **SIPC coverage.** If the broker fails, SIPC returns customer securities and cash up to 500,000 dollars per customer, including a 250,000 dollar limit on cash. Most large brokers carry additional private insurance above that. SIPC does not cover losses from price moves, bad advice, or unregistered products.
3. **Costs.** Commissions are zero for US stocks and ETFs at most large brokers. What varies: margin interest rates (a spread of several percentage points between brokers), fees for wire transfers and paper statements, and options contract fees.
4. **Order routing and payment for order flow.** Brokers must publish a quarterly Rule 606 report showing where they route orders and what they are paid. Payment for order flow is legal and disclosed; it is the reason commissions are zero. It does not mean your fill is worse than the NBBO, but it is worth knowing where your orders go.

## Cash accounts versus margin accounts

A **cash account** lets you buy securities only with settled cash. You cannot borrow, cannot short stock, and are not subject to the pattern day trader rule. It is the right starting point.

A **margin account** lets you borrow against your securities to buy more, short sell, and, at some brokers, trade options beyond basic strategies. It is more flexible, carries interest costs and liquidation risk, and is where the pattern day trader rule lives. Many brokers open margin accounts by default; check which you have.

## Settlement and what it constrains

Since 28 May 2024, US stocks and ETFs settle T+1: the cash and shares change hands one business day after the trade. This drives three constraints in a cash account:

- **Withdrawals.** Sale proceeds are not withdrawable until settlement. Sell Monday, wire Tuesday.
- **Good-faith violations.** You may buy with unsettled proceeds, but if you then sell that new position before the original proceeds settle, you have used money you did not yet have. Brokers typically impose a 90-day restriction to settled-cash-only trading after three good-faith violations in twelve months.
- **Free-riding.** Buying and then selling a security without ever paying for the purchase with settled funds. This is a Regulation T violation and brings a mandatory 90-day freeze.

In a margin account these constraints disappear, because the broker lends you the money between trade and settlement. That convenience is the reason many active traders use margin accounts even if they never intend to borrow overnight.

## How margin works

Three numbers govern a margin loan:

- **Initial margin (Regulation T): 50 percent.** To buy 20,000 dollars of stock, you must put up at least 10,000 dollars of your own money. The Federal Reserve sets this.
- **Maintenance margin (FINRA Rule 4210): 25 percent.** After purchase, your equity (market value minus loan) must stay above 25 percent of market value. This is the regulatory floor.
- **House maintenance: typically 30 to 35 percent**, higher for volatile or concentrated positions. Brokers may set it at anything above the FINRA floor and may raise it without notice.

When equity falls below the maintenance requirement, the broker issues a margin call: deposit cash or securities, or reduce the position. Brokers are not obliged to wait; the margin agreement you signed permits them to liquidate positions of their choosing, without notice, to restore the requirement. In a fast market, this is exactly when it happens.

Interest accrues daily on the loan at the broker's margin rate, which in 2024 and 2025 ranged from around 6 percent to over 13 percent depending on broker and balance. It is charged whether or not the position makes money.

> **Callout:** Margin doubles your gains and doubles your losses, and adds an interest cost and a liquidation trigger that a cash position never has. The worked example shows a 10 percent decline in the stock producing a 20 percent loss of your capital.

## The pattern day trader rule

FINRA Rule 4210(f)(8)(B) defines a **day trade** as buying and selling (or selling short and buying to cover) the same security in the same day in a margin account. A **pattern day trader** is a customer who makes four or more day trades within five business days, provided those trades are more than 6 percent of the account's total trades in that period.

Once flagged as a pattern day trader:

- You must maintain minimum equity of **25,000 dollars** in the account at all times you day trade. If equity falls below that at the close of any day, day trading is prohibited until it is restored.
- Your day-trading buying power is up to four times your maintenance margin excess, rather than two times.
- The flag is persistent. Brokers may remove it once on request; after that it stays.

The rule does not apply to cash accounts. In a cash account you can day trade as often as settled cash allows: every trade must be paid with settled funds, and proceeds from a sale today settle tomorrow, so the practical limit is the size of your settled balance each day.

FINRA has proposed replacing the 25,000-dollar minimum-equity framework with an intraday margin requirement. As of this writing the proposal is not final. Check finra.org for the current rule before relying on any summary, including this one.

## Extended hours and other account settings

Most brokers require you to opt in to extended-hours trading. Only limit orders are accepted, liquidity is thin, and stops do not trigger. Most also require explicit approval for options and for short selling. Leave these off until you have a reason to turn them on. Also check the default order settings: some apps default to market orders, which Lesson 3 explains is the wrong default for anything but the most liquid names.

## Table

Cash versus margin accounts on the dimensions that matter to a beginner.

| Feature | Cash account | Margin account |
| --- | --- | --- |
| Buying power | Settled cash only | Cash plus up to 50 percent borrowed (Reg T) |
| Unsettled proceeds | Usable, but selling before settlement is a good-faith violation | Usable freely; broker lends until settlement |
| Short selling | Not permitted | Permitted with approval |
| Interest cost | None | Daily interest on the borrowed balance |
| Liquidation risk | None | Broker may sell positions without notice on a margin call |
| Pattern day trader rule | Does not apply | Applies; 25,000 dollar minimum once flagged |
| Loss possible | Up to the amount invested | More than the amount invested |
| Suitable for | Starting out; buy-and-hold; any account under 25,000 dollars | Experienced traders who understand the liquidation math |

## Worked example

Microsoft (MSFT) closed at 421.50 dollars on 31 December 2024. You have 10,000 dollars in a margin account with a 30 percent house maintenance requirement and a 10 percent margin interest rate, and you buy 47 shares.

**The position.** 47 × 421.50 = 19,810.50 dollars. Your equity: 10,000 dollars. Loan: 9,810.50 dollars. Initial margin: 10,000 ÷ 19,810.50 = 50.5 percent, just above the Reg T minimum.

**Margin call price.** Equity ÷ market value must stay at or above 0.30. Equity is market value minus the 9,810.50 loan, so (V − 9,810.50) ÷ V ≥ 0.30, which gives V ≥ 9,810.50 ÷ 0.70 = 14,015 dollars. Divided by 47 shares: **298.19 dollars**, a decline of 29.3 percent from your entry. Under the 25 percent FINRA floor the call would come at 13,081 dollars, or 278.32 per share.

**A 10 percent decline.** MSFT falls to 379.35. Position value: 17,829.45. Equity: 17,829.45 − 9,810.50 = 8,018.95. You have lost 1,981.05 dollars, **19.8 percent of your capital**, on a 10 percent move. In a cash account, the same 10,000 dollars would have bought 23 shares, and the same decline would have cost 969 dollars.

**Interest.** At 10 percent on 9,810.50, the loan costs about 981 dollars a year, or roughly 2.69 dollars per day. Holding the position for a year, MSFT must rise about 5 percent just to cover the interest on the borrowed half.

**A 30 percent decline.** MSFT at 295.05, below the call price. Position value 13,867.35; equity 4,056.85; equity ratio 29.3 percent. The broker demands you restore 30 percent, which means depositing about 103 dollars, or, if you do not respond in time, sells shares for you. If the decline happened overnight on an earnings gap, the call and the liquidation may arrive together at the open.

**Day-trade count.** If, over the next week, you buy and sell MSFT within the same day four times and make no other trades, you are a pattern day trader. With 10,000 dollars of equity, well below 25,000, day trading in this account is then prohibited until the equity is restored. The same four trades in a cash account, funded each day with settled cash, would be permitted.

## Sources

- SEC, "Shortening the Securities Transaction Settlement Cycle" (T+1 investor resources): https://www.sec.gov/tplus1
- FINRA, "Margin Accounts" (investor guide): https://www.finra.org/investors/investing/investment-accounts/margin-accounts
- FINRA Rule 4210, Margin Requirements (including pattern day trader provisions): https://www.finra.org/rules-guidance/rulebooks/finra-rules/4210
- SIPC, "What SIPC Protects": https://www.sipc.org/for-investors/what-sipc-protects
