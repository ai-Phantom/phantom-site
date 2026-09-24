---
{
  "title": "What an Option Is: The Contract",
  "duration": "14 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "You buy one XYZ 100 call for 4.16. What do you pay, before commissions?", "opts": ["$4.16", "$41.60", "$416", "$4,160"], "correct": 2, "explain": "Standard equity options carry a 100-share multiplier, so a quoted premium of 4.16 costs 4.16 x 100 = $416 per contract."},
    {"q": "Who guarantees that an assigned option seller performs?", "opts": ["The exchange where it traded", "The Options Clearing Corporation (OCC)", "The buyer's broker", "FINRA"], "correct": 1, "explain": "The OCC is the central counterparty for every listed U.S. option; it stands between buyer and seller so neither depends on the other's credit."},
    {"q": "An American-style option can be exercised:", "opts": ["Only on the expiration date", "Only if it is in the money", "Any business day up to and including expiration", "Only by the writer"], "correct": 2, "explain": "American style allows exercise on any trading day before expiration; European style allows exercise only at expiration. Most listed stock options are American; most cash-settled index options are European."},
    {"q": "You are short a 100 put and the stock closes at 99.50 on expiration Friday. Absent contrary instructions, what happens?", "opts": ["Nothing, it expires worthless", "The OCC auto-exercises the long side and you are assigned 100 shares at 100", "You receive 100 shares at 99.50", "Your broker closes it for you at the last price"], "correct": 1, "explain": "The OCC exercises by exception any option that is in the money by $0.01 or more at expiration, so the long put is exercised and the short is assigned: you buy 100 shares at 100."},
    {"q": "Which statement about exercise and assignment is correct?", "opts": ["Buyers are assigned; sellers exercise", "Sellers choose when to be assigned", "Buyers choose to exercise; sellers are assigned at random by the OCC and their broker", "Assignment can only happen at expiration"], "correct": 2, "explain": "Exercise is the holder's right. The OCC assigns exercises to clearing members at random and the broker allocates to customers by its approved method; an American-style short can be assigned on any business day."}
  ],
  "task": "Open your broker's options approval page, find your current approval level, and write down which of the four rights (buy call, buy put, sell call, sell put) you are permitted to use today."
}
---

## What you are actually buying

An option is a contract between two parties about a future transaction in a stock. A **call** gives its holder the right, but never the obligation, to buy 100 shares of the underlying stock at a fixed price on or before a fixed date. A **put** gives its holder the right to sell 100 shares under the same terms. The fixed price is the **strike**, the fixed date is the **expiration**, and the price you pay for the contract is the **premium**.

Everything else in this course is a consequence of that paragraph. The seller of the contract, called the **writer**, takes on the mirror-image obligation: a call writer must deliver shares at the strike if asked; a put writer must buy them. The buyer's risk is capped at the premium. The writer's risk is not capped by the contract itself, which is why brokers restrict who may write uncovered options.

You will meet four positions, and only four, in single-leg trading. Long call: you paid for the right to buy. Long put: you paid for the right to sell. Short call: you were paid to accept the obligation to sell. Short put: you were paid to accept the obligation to buy. Spreads, which come later, are combinations of these.

## The 100-share multiplier

A standard U.S. equity option covers 100 shares. Quotes on the chain are per share, so a call quoted at 4.16 costs 4.16 x 100 = $416 for one contract. This is the single most common arithmetic mistake new traders make, in both directions: some think a 4.16 option costs $4.16 and buy ten, and some think a 0.41 option is nearly free and forget that ten of them cost $410.

The multiplier can change. After a stock split, a special dividend, a spin-off or a merger, the OCC adjusts outstanding contracts so that their economic value is preserved. An adjusted contract might deliver 150 shares, or 100 shares plus cash, and its symbol usually carries a suffix. Adjusted contracts trade with wider spreads and behave oddly on the chain, so the practical rule is: if the deliverable is not exactly 100 shares of the ordinary stock, do not trade it until you have read the OCC adjustment memo.

Index options such as SPX are cash-settled and carry a $100 multiplier on the index level rather than shares. The Phantom Traders signal cards quote everything per share, in line with the chain, and let you multiply.

## Who stands behind the contract

When you buy a call, you are not lending your money to some specific seller and hoping they honour it. Every listed U.S. option clears through the **Options Clearing Corporation (OCC)**. The OCC becomes the buyer to every seller and the seller to every buyer the moment a trade matches. If a writer is assigned and cannot perform, the writer's clearing firm is on the hook, and behind that firm sits the OCC's guarantee fund. This is the reason options can be traded anonymously across a dozen exchanges and still be fungible: an XYZ 100 call bought on Cboe is identical to one bought on Nasdaq PHLX, because the OCC issues both.

The OCC also publishes the **Options Disclosure Document**, formally titled *Characteristics and Risks of Standardized Options*. Your broker is required to give it to you before approving your account. Read it once; it is the source of every rule in this lesson.

## Expiration

Options stop existing on their expiration date. For standard monthly equity options this is the third Friday of the month; if that Friday is an exchange holiday, expiration is the Thursday before. Since 2022 most large stocks and ETFs also list **weekly** options expiring every Friday, and the biggest index products list options expiring every trading day. An option expiring today is a **0DTE** contract. The chain and the signal cards express time to expiration as **DTE**, days to expiration, counted in calendar days.

The last moment to trade an expiring equity option is the close of regular trading on expiration day. The last moment to instruct your broker to exercise or to *not* exercise is typically an hour or so after the close, and that cutoff is set by your broker, not the OCC. Lesson 11 covers what happens in that window.

## Exercise and assignment

**Exercise** is what the holder does: they tell their broker to use the right. A call holder who exercises pays strike x 100 and receives 100 shares. A put holder who exercises delivers 100 shares and receives strike x 100. The broker passes the instruction to the OCC, which selects a writer.

**Assignment** is what happens to the writer. The OCC assigns exercise notices to its clearing members at random; the broker then allocates them to its customers who are short that contract, using a method it has filed with regulators, most often random or first-in-first-out. You cannot choose to be assigned and you cannot refuse.

Two facts about assignment are worth memorising now. First, at expiration the OCC applies **exercise by exception**: any option that is in the money by $0.01 or more is automatically exercised unless the holder instructs otherwise. A short 100 put with the stock at 99.99 will be assigned. Second, for American-style options assignment can happen on any business day, not just expiration. It is rare when the option still has time value, because the holder gives that value up by exercising, but it is not zero, and Lesson 11 shows exactly when it becomes likely.

## American versus European

An **American-style** option can be exercised on any business day up to and including expiration. Nearly all listed options on individual stocks and ETFs in the U.S. are American.

A **European-style** option can be exercised only at expiration. Most cash-settled index options, SPX and its weeklies among them, are European. Since nobody can exercise early, a short European option can never be assigned before expiration, and settlement is a cash transfer equal to the in-the-money amount rather than a delivery of shares. This makes them simpler to hold through expiration, at the cost of some tax and margin differences you should read about before trading them.

The pricing difference between the two styles is usually small for calls on non-dividend stocks and larger for puts and for calls on stocks about to pay a dividend. Lesson 8 explains why.

## Worked example

Take a representative chain for a stock we will call XYZ, priced at $100.00 on Tuesday 22 September 2026. The November 6 expiration is 45 calendar days away, so every contract in that column is **45 DTE**. This chain is a model-generated illustration built at 28% implied volatility and a 4% interest rate, not a live quote; the same chain runs through every lesson so the numbers always tie out.

The XYZ Nov 100 call is quoted 4.08 bid / 4.24 ask. You buy one at the ask.

- Cost: 4.24 x 100 = **$424.00** plus commission. If your broker charges $0.65 per contract, total outlay is $424.65.
- Right acquired: buy 100 XYZ at $100.00 any business day through Friday 6 November 2026.
- Maximum loss: the $424.65 you paid. The stock can go to zero and you owe nothing further.
- Break-even at expiration: strike + premium = 100 + 4.24 = **$104.24**. Below that at expiration the trade loses; above it the trade earns (S - 104.24) x 100.

Now suppose XYZ closes at $107.00 on expiration Friday and you do nothing. The option is $7.00 in the money, well past the $0.01 exception threshold, so the OCC exercises it. On Monday your account shows 100 XYZ shares and a debit of $10,000 cash. Your position is worth $10,700, so your gain is 10,700 - 10,000 - 424.65 = **$275.35**, and you now own stock with $10,700 of market risk. If you did not want the shares, you needed either to sell the call before the close on Friday for roughly its intrinsic value of 7.00 (netting the same $275 without the stock) or to file a do-not-exercise instruction with your broker.

The mirror image: the trader who sold you that call was assigned. They delivered 100 shares for $10,000. If they owned the shares already, they sold them at 100 and kept the 4.08 (or so) they collected; if they did not, their broker bought the shares at market to deliver, and they lost (107 - 100 - 4.08) x 100 = $292 before commissions.

## Table

The four single-leg positions and their obligations, using the same XYZ Nov 100 contracts.

| Position | You paid or received | Your right or obligation | Max loss per contract | What happens at expiry if XYZ = 107 |
|---|---|---|---|---|
| Long 100 call | Paid 4.24 | Right to buy 100 sh at 100 | $424 | Auto-exercised; you buy 100 sh at 100 |
| Short 100 call | Received 4.08 | Obligation to sell 100 sh at 100 | Unlimited (uncovered) | Assigned; you deliver 100 sh at 100 |
| Long 100 put | Paid 3.73 | Right to sell 100 sh at 100 | $373 | Expires worthless |
| Short 100 put | Received 3.61 | Obligation to buy 100 sh at 100 | $9,639 (stock to zero) | Expires worthless; you keep 3.61 |

## Why this matters for the rest of the course

Every Greek, every spread and every risk rule in the next twelve lessons is a statement about how the premium on this contract changes and what the two parties owe each other. When a signal card reads "XYZ 100C, 45 DTE, delta 0.54, spread cost 0.16", you now know what each word refers to: the strike, the days to the November 6 expiration, a sensitivity you will meet in Lesson 4, and the bid-ask spread you will learn to read in Lesson 2.

## Sources

- Options Clearing Corporation, *Characteristics and Risks of Standardized Options* (the Options Disclosure Document): https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document
- Options Clearing Corporation, exercise and assignment procedures and adjustments: https://www.theocc.com/clearance-and-settlement/clearing/exercise-and-assignment
- Cboe Global Markets, Options Institute education on contract specifications: https://www.cboe.com/education/
- U.S. Securities and Exchange Commission, Investor.gov, options basics: https://www.investor.gov/introduction-investing/investing-basics/glossary/options
