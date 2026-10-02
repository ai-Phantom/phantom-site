---
{
  "title": "Equity Options: Premiums, Exercise, Assignment, Covered Calls and Straddles",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "You write a call for a $450 premium and it expires worthless eleven months later. The premium is:", "opts": ["Long-term capital gain", "Ordinary income", "Not taxable until the stock is sold", "Short-term capital gain, regardless of how long the option was open"], "correct": 3, "explain": "Pub. 550, Writers of puts and calls: if your obligation expires, the amount you received for writing the call or put is short-term capital gain. The writer's holding period is irrelevant."},
    {"q": "A call you wrote against 100 shares is assigned. For the stock sale you:", "opts": ["Report the premium separately as ordinary income", "Add the premium to the amount realised on the stock; the gain is long- or short-term by the stock's holding period", "Subtract the premium from the stock basis", "Treat the whole gain as short-term"], "correct": 1, "explain": "Pub. 550: if a call you write is exercised and you sell the underlying stock, increase your amount realised on the sale by the amount you received for the call. Character follows the stock's holding period."},
    {"q": "You bought a put for $300 and later exercised it to sell your shares. The $300 is:", "opts": ["Subtracted from the amount realised on the stock sale", "A short-term loss on the option", "Added to the basis of the stock", "Ignored"], "correct": 0, "explain": "Pub. 550, Holders of puts and calls: if you exercise a put, reduce your amount realised on the sale of the underlying stock by the cost of the put."},
    {"q": "A qualified covered call under Publication 550 must, among other things, be:", "opts": ["Granted more than 30 days before expiration, not more than 12 months, and not deep in the money", "Cash settled", "Written on an index", "Held to expiration"], "correct": 0, "explain": "Pub. 550 lists the conditions: exchange traded, granted more than 30 days before expiration, not more than 12 months (or meeting published benchmark rules), not deep in the money (strike not below the lowest qualified benchmark), not by an options dealer, and capital in character."},
    {"q": "Which option is taxed under section 1256's 60/40 rule rather than the Publication 550 puts-and-calls rules?", "opts": ["A call on AAPL", "A put on SPY", "A cash-settled option on the S&P 500 index", "A LEAPS call on TSLA"], "correct": 2, "explain": "Options on individual stocks and on ETF shares are equity options; a cash-settled option on a broad-based index is a nonequity option and a section 1256 contract (Pub. 550; IRC section 1256(g)(3))."}
  ],
  "task": "Take three closed option trades from last year and classify each outcome as expired, closed, exercised or assigned, then write the Pub. 550 rule that applies to each."
}
---

## Options are capital assets with their own timing rules

A listed option on a stock or on an exchange-traded fund is an equity option, and Publication 550's rules for puts and calls govern it. The principle is simple: the premium is not income or expense when it changes hands. It waits until the option is ended by expiry, by a closing transaction, or by exercise, and then it is taxed differently depending on whether you were the holder or the writer and how the option ended. Table 4-3 in Publication 550 summarises the outcomes; this lesson works through each.

Everything here is for equity options in a non-dealer's hands. Options on a broad-based index such as the S&P 500 index are nonequity options taxed under section 1256 (lesson 5), and Publication 550's own example shows the contrast: a $4,000 premium that expires produces a $4,000 short-term loss to the holder of an equity option, but a $1,600 short-term and $2,400 long-term loss to the holder of a nonequity option.

## If you buy options

Buying a put or a call is a capital expenditure, not a deduction. If you sell the option before exercise, the difference between what you paid and what you receive is a capital gain or loss, long-term or short-term by how long you held the option; a LEAPS held more than a year can produce a long-term gain. If the option expires, its cost is a capital loss on the expiration date, with the same holding-period test. If you exercise a call, its cost is added to the basis of the shares you buy, and the shares' holding period starts the day after exercise, not when you bought the call. If you exercise a put, its cost reduces the amount realised on the shares you sell, and the character follows the shares' holding period.

Publication 550 adds a trap for protective puts. Buying a put is generally treated as a short sale for the holding-period rules: if you have held the underlying stock one year or less when you buy the put, any gain on the put is short-term and, more importantly, the stock's holding period is wiped out and starts again only when the put is exercised, sold or expires. A trader who buys a put to protect a nine-month-old position resets that position's clock.

## If you write options

Writing a put or call brings in cash that is carried in a deferred account, in Publication 550's phrase, until one of three things happens. If the obligation expires, the whole premium is short-term capital gain, whatever the term of the option. If you close by buying the option back, the difference between what you paid and what you received is short-term capital gain or loss. If a put you wrote is exercised and you are assigned the shares, the premium reduces your basis in the shares and their holding period starts on the assignment date. If a call you wrote is exercised and your shares are called away, the premium is added to the amount realised on the shares and the gain or loss on the shares is long-term or short-term by the shares' holding period.

Two practical consequences follow. First, a writer's income is always short-term when the option itself is the thing that produces it, so a systematic premium-selling strategy is taxed at ordinary rates however long each contract runs. Second, assignment on a covered call does not change the character of the stock gain, so a call written against a lot held for years produces a long-term gain when assigned, with the premium folded in.

## Covered calls and the straddle rules

IRC section 1092 defers losses on offsetting positions in a straddle to the extent of unrecognised gain on the other leg, and Publication 550 says a straddle includes stock when one of the offsetting positions is an option on that stock. A covered call is therefore a straddle in form, and without an exception a loss on the call could be deferred while the stock gain sits unrecognised, and the stock's holding period could be suspended. The exception is the qualified covered call. Publication 550 sets its conditions: the option is exchange traded; it is granted more than 30 days before expiration; it is granted not more than 12 months before expiration (or meets published benchmark rules for longer terms); it is not deep in the money; you are not an options dealer; and gain or loss on it is capital. Deep in the money means a strike below the lowest qualified benchmark, which is the highest available strike below the applicable stock price (the prior day's close, or the opening price if more than 110% of it); for options with a term over 90 days and a strike over $50, it is the second-highest strike below that price.

If the call is qualified and the straddle is not part of a larger straddle, the loss-deferral rules do not apply. Two residual rules remain even for a qualified call. Publication 550's Capital loss on qualified covered call options paragraph says that where the qualified call is in the money (strike below the applicable stock price), a loss on the option is treated as long-term if the stock would give long-term gain, and the stock's holding period does not include any period during which you are the writer of the option. And a special year-end rule reinstates loss deferral where the call or the stock is closed at a loss in one year, the gain on the other leg lands in the next year, and the surviving leg was held less than 30 days after the close. An out-of-the-money qualified call triggers neither.

## Worked example

You bought 100 AAPL on 2024-08-01 at the Yahoo Finance daily close of $218.36, cost $21,836.00. On 2025-09-02 you wrote one AAPL call expiring 2025-10-17 with a $240 strike for a premium of $4.50 a share, $450.00. The premium is an assumed figure for illustration because the Yahoo chart API used in this course does not return historical option quotes; the stock prices are real closes.

Qualified covered call test. Exchange traded, yes. Granted 45 days before expiration, more than 30 and less than 12 months, yes. Applicable stock price is the close on the last trading day before the grant, 2025-08-29, at $232.14. The $240 strike is above that price, so the call is out of the money; it cannot be below the lowest qualified benchmark and is not deep in the money. Capital in character and you are not a dealer. The call is qualified, the straddle rules do not apply, and because it is out of the money the stock's holding period is not suspended.

Outcome 1, assignment. AAPL closed at $252.29 on 2025-10-17, above the strike, and the call was assigned. Amount realised on the shares = $240 × 100 + $450.00 = $24,450.00. Gain = $24,450.00 − $21,836.00 = $2,614.00. The shares were held from 2024-08-02 to 2025-10-17, more than a year, so the entire $2,614.00, premium included, is long-term. Tax at a 15% rate: $392.10. Note that the shares were worth $25,229.00 at the close; the $779.00 of upside above the strike went to the option holder and is not your income or your loss.

Outcome 2, expiry. Had AAPL finished below $240, the call would have expired and the $450.00 would be a short-term capital gain on 2025-10-17, taxed at 24% for $108.00, while you kept the shares and their long-term holding period.

Outcome 3, buy-back. Had you closed the call on 2025-10-16 (AAPL close $247.45) by paying $13.00 a share, $1,300.00, the result is a short-term capital loss of $450.00 − $1,300.00 = −$850.00 on the option, deductible in 2025 against other gains because the qualified-call exception removes the straddle deferral, and the shares keep their long-term status. Under the special year-end rule this would change only if you then sold the shares at a gain in 2026 within 30 days of closing the call.

Holder's side. The buyer of your call paid $450.00 on 2025-09-02. On assignment the buyer's basis in 100 AAPL is $24,000.00 + $450.00 = $24,450.00 with a holding period starting 2025-10-18; had the call expired, the buyer's $450.00 would be a short-term capital loss on 2025-10-17.

## Table

| Event | Holder of the option | Writer of the option | Pub. 550 rule |
|---|---|---|---|
| Expires | Cost is a capital loss on the expiry date; long- or short-term by holding period of the option | Premium is short-term capital gain on the expiry date | Holders/Writers of puts and calls |
| Closed before expiry | Proceeds less cost is capital gain or loss, by holding period of the option | Premium less buy-back cost is short-term gain or loss | Same |
| Call exercised/assigned | Add cost of call to basis of shares bought; holding period starts day after exercise | Add premium to amount realised on shares; character by the shares' holding period | Table 4-3 |
| Put exercised/assigned | Subtract cost of put from amount realised on shares sold | Subtract premium from basis of shares acquired; holding period starts on purchase | Table 4-3 |
| Worked example, 2025-10-17 assignment | Basis $24,450.00 in 100 AAPL | Long-term gain $2,614.00 on shares bought 2024-08-01 | Tax year 2025 |

## Sources

- IRS Publication 550, Investment Income and Expenses (Puts and Calls; Table 4-3; Straddles; Qualified covered call options): https://www.irs.gov/publications/p550
- IRC section 1092, Straddles: https://www.law.cornell.edu/uscode/text/26/1092
- IRC section 1256(g)(3), nonequity option defined: https://www.law.cornell.edu/uscode/text/26/1256
