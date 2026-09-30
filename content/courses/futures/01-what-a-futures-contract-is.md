---
{
  "title": "What a Futures Contract Is and Who Uses It",
  "duration": "16 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "You buy one E-mini S&P 500 (ES) contract on CME Globex. Who is your legal counterparty once the trade clears?", "opts": ["The trader who sold it to you", "Your broker", "CME Clearing, the clearinghouse", "The S&P 500 index provider"], "correct": 2, "explain": "After the match, the clearinghouse is substituted in as buyer to every seller and seller to every buyer. You never depend on the original seller's credit."},
    {"q": "A wheat farmer sells wheat futures in May to lock in a September price. Which role is the farmer playing?", "opts": ["Speculator", "Hedger", "Market maker", "Arbitrageur"], "correct": 1, "explain": "The farmer already owns the price risk of the crop; selling futures transfers that risk to someone willing to carry it. That is the definition of hedging."},
    {"q": "Which statement about a futures contract is TRUE?", "opts": ["Only the buyer has an obligation", "Both sides have an obligation; neither side has a right without a matching duty", "The seller can decline to deliver if prices rise", "Futures can only be closed at expiration"], "correct": 1, "explain": "Unlike an option, a futures contract binds both parties symmetrically. Either side can exit before expiration by taking the offsetting position, which is how most contracts are closed."},
    {"q": "Why does an exchange standardise contract size, months and delivery terms?", "opts": ["To make every contract interchangeable so that offsetting and liquidity are possible", "To satisfy IRS reporting rules", "Because the CFTC sets the multiplier", "To prevent hedgers from trading"], "correct": 0, "explain": "Standardisation is what lets a contract bought from one stranger be closed against a contract sold to another. Without it there is no fungibility and no central order book."},
    {"q": "How is the ES contract settled at expiration?", "opts": ["Delivery of 500 stock certificates", "Delivery of SPY shares", "Cash, against a special opening quotation of the S&P 500 on the third Friday", "It never expires"], "correct": 2, "explain": "Equity index futures are cash-settled. The final price is the Special Opening Quotation (SOQ) of the index on the third Friday of the contract month; the difference is paid in cash."}
  ],
  "task": "Open the CFTC's 'Basics of Futures Trading' page and write down, in one sentence each, what a hedger and a speculator are trying to do."
}
---

## The contract, stated plainly

A futures contract is a standardised, exchange-traded agreement to buy or sell a fixed quantity of something at a price agreed today, with settlement on a fixed future date. The Commodity Futures Trading Commission (CFTC) defines it as "an agreement to buy or sell a particular commodity at a future date" where the price and quantity are fixed now. Two words in that definition do all the work: *standardised* and *exchange-traded*.

Notice what is missing. There is no premium, no strike, no right that one side holds and the other lacks. A futures contract binds both parties symmetrically. If you are long, you have agreed to buy; if you are short, you have agreed to sell. Either of you can leave before the settlement date by entering the opposite trade, and nearly everyone does. The CFTC notes that most contracts "are liquidated by offsetting and do not result in delivery." That offset mechanism is what makes futures a trading instrument rather than a procurement contract.

For the E-mini S&P 500 (ES) contract, the "something" is not a physical good at all but $50 times the level of the S&P 500 index. Nothing is ever delivered. At expiration the exchange computes a final index value and the loser pays the winner in cash. Lesson 2 covers the exact terms.

## Standardisation is the product

An exchange does not invent a new contract every time two people want to trade. It publishes one specification and every contract of that month is identical: same size, same tick, same expiration, same settlement procedure. The CFTC points out that exchanges standardise "size, delivery locations, grades" precisely because that "enhances liquidity."

Standardisation makes contracts fungible. The ES contract you buy at 10:02 from someone in Chicago is identical to the one you sell at 10:47 to someone in Singapore, so the two cancel and you are flat. Without fungibility there could be no central order book, no continuous price, and no way to close a position without finding the original counterparty again. That is why every fact in this course starts from the specification page: the spec *is* the product.

## Who is on the other side

The CFTC's description of the market's economic purpose lists two functions: risk transfer and price discovery. Both rest on the same two groups of participants.

**Hedgers** already carry a price risk and want less of it. A refiner that must buy crude next month, an airline that burns jet fuel, a pension fund holding $2 billion of U.S. equities that needs to reduce exposure for a quarter, a bank with a mortgage book sensitive to ten-year yields. The CFTC's example is the wheat farmer who sells futures on a crop still in the ground to lock in a harvest price. A hedger's futures loss is offset by a gain on the thing being hedged, and vice versa. The hedger is buying certainty, not seeking profit on the contract itself.

**Speculators** carry no offsetting position. They take the other side of the hedger's trade because they believe the price will move in their favour, and they accept the risk in exchange for that possibility. Speculators are not a nuisance the market tolerates; they are the reason a hedger can find a counterparty at 2 a.m. on a Tuesday. The CFTC is blunt about the retail version of this role: "speculating in commodity futures and options is a volatile, complex and risky venture" that is rarely suitable for individual investors, and participants "can be required to pay more than they invested initially." Keep that sentence in mind for Lessons 3 and 4.

There is a third, quieter group: arbitrageurs and market makers who hold the futures price close to the price of the underlying by trading the two against each other. They are why an index future rarely strays more than a few points from its fair value (Lesson 5).

## The exchange and the clearinghouse are two different things

The **exchange** is the marketplace. For ES, that is CME Globex, the electronic platform of Chicago Mercantile Exchange Inc. It lists the contract, publishes the specification, runs the order book, matches buyers with sellers, sets trading hours, and enforces its rulebook.

The **clearinghouse** is the guarantor. For CME products that is CME Clearing. The CFTC describes its function exactly: it "acts as the buyer to all sellers and the seller to all buyers." The moment your order matches, the original counterparty disappears from your life. Your contract is now with the clearinghouse, and so is theirs. This is called novation. It means you never assess the creditworthiness of the person on the other side, because there is no person on the other side.

The clearinghouse can make that promise only because it collects collateral from every participant and re-marks every open position to the market price at least daily, paying and collecting the difference in cash. Those two mechanisms, the performance bond and daily settlement, are Lessons 3 and 4. For now the point is structural: the exchange runs the market; the clearinghouse guarantees the trades; your broker (a futures commission merchant, or FCM) sits between you and both, and is itself a member of the clearinghouse or clears through one that is.

## Long, short, and offset

Being **long** one ES means you have agreed to buy $50 times the S&P 500 at the price you traded. Being **short** means the reverse. Neither term implies a view about the underlying stocks; a pension fund can be short ES as a hedge while being very long equities.

You close a position by **offsetting**: a long sells the same contract month, a short buys it. Because the contracts are fungible, the clearinghouse nets the two and you have no position. You do not need permission, you do not need the original counterparty, and you do not wait for expiration. The overwhelming majority of ES volume is offsets, not new risk.

If you do nothing and the contract reaches its last trading day, it settles. For ES that is cash against the Special Opening Quotation (SOQ) of the index on the third Friday; for WTI crude it is physical delivery of 1,000 barrels in Cushing, Oklahoma. Lesson 8 explains why a retail trader must never hold crude to that point.

## Worked example

On 2026-09-23 the December 2026 ES contract (ESZ26) closed at 7,772.50 (Yahoo Finance daily bar for ESZ26.CME, pulled 2026-09-24). Take a pension fund and a speculator on opposite sides of a single contract at that price and follow the money for one day.

The contract's notional value is the index level times the CME multiplier of $50 per index point (CME Group, E-mini S&P 500 contract specifications):

7,772.50 x $50 = $388,625.00

The pension fund sells one contract to reduce its equity exposure by $388,625. The speculator buys it. Neither pays $388,625; each posts a performance bond, which Lesson 3 covers. Now suppose the next daily settlement is 7,742.50, a drop of 30.00 index points (this was ESZ26's Yahoo last trade on 2026-09-24).

Change in contract value = 30.00 points x $50 = $1,500.00

The speculator, who is long, has lost $1,500.00; the clearinghouse collects it from the speculator's broker at settlement. The pension fund, short, gains $1,500.00; the clearinghouse pays it to the fund's broker. But the fund also holds $388,625 of stocks that fell about 0.39% (30.00 / 7,772.50 = 0.00386), a loss of roughly $1,500 on the stock side. The fund is flat overall, which is what it wanted. The speculator is down $1,500 with no offset, which is what they accepted.

Neither party ever dealt with the other. Each has a contract with CME Clearing; the clearinghouse moved $1,500 from one account to the other. If the speculator's broker fails to pay, the clearinghouse still pays the fund, drawing on the broker's collateral and then its own guarantee fund. That is the whole architecture in one day.

## Table

| Participant | Why they trade ES | Typical position | Where their risk goes |
|---|---|---|---|
| Hedger (pension fund, asset manager) | Adjust equity exposure without selling stock | Short to reduce, long to add | Offset by the portfolio they hold |
| Speculator (prop desk, retail trader) | Profit from expected moves | Either; usually flat by close | Borne entirely by their account |
| Arbitrageur / market maker | Keep futures near fair value; earn the spread | Long one side, short the other | Small, hedged; they carry basis risk |
| Exchange (CME Globex) | Operates the market, earns fees | None | Not a party to trades |
| Clearinghouse (CME Clearing) | Guarantees every trade after novation | Zero net; long to every short and short to every long | Covered by margin, daily settlement and guarantee fund |

## Sources

- CFTC, "Basics of Futures Trading" — https://www.cftc.gov/LearnAndProtect/EducationCenter/FuturesMarketBasics/index.htm
- CFTC, "Economic Purpose of Futures Markets and How They Work" — https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/economicpurpose.html
- CME Group, E-mini S&P 500 contract specifications — https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.contractSpecs.html
- CME Group, Performance Bonds/Margins FAQ — https://www.cmegroup.com/solutions/risk-management/performance-bonds-margins/faq-performance-bonds-margins.html
