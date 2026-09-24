---
{
  "title": "The Tape: Time and Sales, Block Prints, and What an Aggressor Is",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A print at 52.18 arrives while the NBBO is 52.17 / 52.18. Under the quote rule, the aggressor was:", "opts": ["The seller", "The buyer", "Unknown", "The exchange"], "correct": 1, "explain": "A trade at the ask means a marketable buy order consumed a resting sell. The buyer demanded immediacy; the buyer is the aggressor."},
    {"q": "A print at 52.175 arrives with the NBBO at 52.17 / 52.18. Lee and Ready's procedure says:", "opts": ["Classify as a buy", "Classify as a sell", "Apply the tick test: compare to the previous different price", "Discard the trade"], "correct": 2, "explain": "A midpoint trade gives the quote rule nothing to work with, so Lee and Ready fall back to the tick test."},
    {"q": "In the worked example, ten prints total 27,900 shares with 16,300 classified as buyer-initiated. The share of buy volume is:", "opts": ["42%", "50%", "58%", "84%"], "correct": 2, "explain": "16,300 / 27,900 = 0.584, i.e. 58.4% of the sample's volume was buyer-initiated."},
    {"q": "A 250,000-share print at exactly the NBBO midpoint, reported with a TRF venue code, is most likely:", "opts": ["A retail market order", "An ATS cross or negotiated block between institutions", "An opening auction print", "A spoofed order"], "correct": 1, "explain": "Midpoint size printed off-exchange is the signature of a dark-pool cross or a block. Retail wholesaler fills are small and usually sub-penny inside the spread."},
    {"q": "Why does aggressor classification degrade for off-exchange prints?", "opts": ["They have no price", "They are reported with a delay, so the NBBO at report time may not be the NBBO at execution", "They are always midpoint", "FINRA hides them"], "correct": 1, "explain": "TRF reports can lag execution; if the quote moved in between, the quote rule compares the print to the wrong quote. Off-exchange volume is half the tape, so this matters."}
  ],
  "task": "Export 100 consecutive prints in one stock from your platform, classify each by the quote rule (tick test for midpoints), and compute buy volume minus sell volume."
}
---

## What the tape is

Time and sales, the tape, is the consolidated record of every trade: timestamp, price, size, the venue that reported it and condition codes describing anything unusual about it. Exchange trades reach the tape through the SIP within microseconds of execution; off-exchange trades reach it through a FINRA Trade Reporting Facility, which must be done "as soon as practicable" and within ten seconds, so those prints can lag. The tape is the raw material of every order-flow tool in the next lesson, and reading it well is mostly a matter of knowing what each print is not.

## Three kinds of print

Regular-way exchange trades are the majority by count: a marketable order hit a resting order on a displayed book. Their size is usually small (round lots or odd lots of 100 shares or fewer), and their price is on the penny grid because Rule 612 prohibits sub-penny quotes.

Off-exchange prints, marked with the TRF venue, come in two visible flavours. Small prints at sub-penny prices (187.1187 in a stock quoting 187.11 / 187.12) are wholesaler fills of retail orders with fractional price improvement; the wholesaler is allowed to execute at a sub-penny price even though nobody may quote one. Large prints at exactly the midpoint are ATS crosses or negotiated blocks. Cboe's 2025 review put off-exchange volume at 50.6% of the consolidated tape, so on a share-weighted basis this category is the biggest.

Auction prints are the opening and closing crosses: one large print per exchange per stock, at the official open or close, carrying an auction condition code. In lesson 2's 60-session SPY sample the closing print alone was around eleven times a normal 5-minute bar's volume, and it should never be mixed into an aggressor calculation, because nobody was the aggressor in an auction.

Condition codes also flag odd lots, late reports, prior-reference-price trades (executed earlier, reported now), extended-hours trades, intermarket sweep orders and derivatively-priced trades such as VWAP crosses. A derivatively-priced print reports a price that was agreed by formula, not by a trader lifting an offer, and tells you nothing about who was aggressive.

## Block trades

A block is conventionally 10,000 shares or $200,000, though the number has lost meaning as average trade sizes fell below 200 shares. Most genuine institutional blocks are negotiated upstairs, crossed in an ATS, or worked algorithmically as thousands of child orders (lesson 10) that never show as a block at all. What prints as a large single trade is therefore a biased sample: crosses at the midpoint, closing-auction fills, and occasionally a real sweep through the book. A large print at the ask after a sweep is informative; a large print at the midpoint is a matched pair of institutions who agreed on a price, and it says nothing about direction.

## Aggressor: who demanded immediacy

Every regular trade has two sides, a resting order that was there first and an incoming order that chose to trade against it. The incoming order is the aggressor, and the aggressor's direction is what "buy volume" and "sell volume" mean in order-flow analysis. A trade at the ask happened because a buyer sent a marketable order and consumed a resting sell; the buyer was the aggressor and the print counts as buy volume. A trade at the bid was a marketable sell consuming a resting bid: sell volume.

Exchanges know the aggressor exactly and some feeds publish it. The consolidated tape does not, so the standard inference is Lee and Ready's 1991 procedure: compare the trade price to the prevailing quote (the quote rule); if the trade is above the midpoint it is a buy, below the midpoint a sell; if it is exactly at the midpoint, use the tick test, classifying an uptick or zero-uptick from the previous different price as a buy and a downtick or zero-downtick as a sell. Lee and Ready found the quote rule alone left a substantial share of trades unclassified at the midpoint, and that the tick test resolved most of them with reasonable accuracy on their data. Later studies on modern data put overall accuracy in the range of roughly 70–85% for exchange trades, worse for off-exchange prints where the report lags the execution and the quote has moved.

Two cautions. First, "aggressor" is a statement about impatience, not information. A closing-benchmark algorithm crossing the spread at 15:58 is an aggressor with no view at all. Second, each print has an aggressor but the sum over prints is not a sum of opinions: a 10,000-share print at the bid is one seller who wanted out and one or more resting buyers who were willing to be there. Whether that is bearish (a seller hitting) or bullish (a buyer absorbing) is the central ambiguity of lesson 7, and the tape alone cannot settle it.

## Worked example

Ten consecutive prints in a representative $52 stock at 10:14 Eastern. This tape is constructed for the lesson, not recorded from a real session; the NBBO shown is the quote prevailing at each print.

| # | Time | NBBO | Print | Size | Quote rule | Tick test | Class |
|---|---|---|---|---|---|---|---|
| 1 | 10:14:02 | 52.17 / 52.18 | 52.18 | 300 | at ask | — | Buy |
| 2 | 10:14:03 | 52.17 / 52.18 | 52.18 | 1,200 | at ask | — | Buy |
| 3 | 10:14:05 | 52.17 / 52.19 | 52.17 | 500 | at bid | — | Sell |
| 4 | 10:14:05 | 52.17 / 52.19 | 52.18 | 400 | midpoint | uptick from 52.17 | Buy |
| 5 | 10:14:08 | 52.17 / 52.19 | 52.1712 | 100 | below mid (TRF) | — | Sell |
| 6 | 10:14:09 | 52.18 / 52.19 | 52.19 | 8,000 | at ask | — | Buy |
| 7 | 10:14:09 | 52.18 / 52.20 | 52.20 | 2,500 | at ask | — | Buy |
| 8 | 10:14:11 | 52.18 / 52.20 | 52.19 | 10,000 | midpoint (TRF) | downtick from 52.20 | Sell |
| 9 | 10:14:14 | 52.18 / 52.20 | 52.18 | 1,000 | at bid | — | Sell |
| 10 | 10:14:15 | 52.18 / 52.20 | 52.20 | 3,900 | at ask | — | Buy |

Classify with the quote rule where possible, the tick test at the midpoint.

- Buy volume (prints 1, 2, 4, 6, 7, 10): 300 + 1,200 + 400 + 8,000 + 2,500 + 3,900 = 16,300 shares.
- Sell volume (prints 3, 5, 8, 9): 500 + 100 + 10,000 + 1,000 = 11,600 shares.
- Total = 27,900 shares. Buy share = 16,300 / 27,900 = 58.4%. Delta = 16,300 − 11,600 = +4,700 shares.

Now interrogate the number. Print 8 is 10,000 shares at exactly the midpoint, reported off-exchange. The tick test called it a sell because the previous different price (52.20) was higher, but a midpoint TRF print of that size is almost certainly an ATS cross between two institutions, with no aggressor at all. Remove it and the sell volume is 1,600, the total 17,900, and the buy share 91%. Alternatively, treat the tick test as gospel and it is 58%. The difference between 58% and 91% is one print, and it is exactly the kind of print the tape cannot classify. Print 5 (100 shares at 52.1712, below the midpoint of 52.18) is a wholesaler filling a retail sell with $0.0012 of price improvement: a genuine sell aggressor, tiny. Print 6, 8,000 shares lifting the offer and moving the ask from 52.19 to 52.20 in the next print, is the most informative trade on this tape: someone paid to be filled now, and the book moved.

Reported honestly: over these 15 seconds, aggressive buyers took 16,300 shares against the offer, one uncategorisable 10,000-share cross printed at the midpoint, and the ask ticked up two cents. That is what the tape says. "Delta +4,700" is a compression of it that hides the most important row.

## Table

| Print type | How to recognise it | Aggressor | What it tells you |
|---|---|---|---|
| Regular exchange trade | Penny price, SIP venue code, usually 100–500 shares | Quote rule, then tick test | Who crossed the spread; the raw material of delta |
| Wholesaler retail fill | TRF code, sub-penny price inside the NBBO, small size | Side of the midpoint | A retail order was filled with price improvement |
| ATS cross or block | TRF code, exactly the midpoint, thousands of shares | None | Two institutions matched; direction unknown |
| Auction print | Auction condition code at 09:30 or 16:00, very large | None | The official open or close; exclude from delta |
| Derivatively priced | VWAP or prior-reference condition code | None | A formula price, reported late; exclude from delta |

Three of the five rows have no aggressor. On a share-weighted basis they are a large part of the tape.

## Sources

- Charles Lee and Mark Ready, "Inferring Trade Direction from Intraday Data", Journal of Finance 46(2), 1991: https://doi.org/10.1111/j.1540-6261.1991.tb02683.x
- FINRA, Trade Reporting Frequently Asked Questions (10-second reporting requirement, TRF reporting): https://www.finra.org/filing-reporting/trade-reporting-faq
- Consolidated Tape Association, CTS Output Specification (trade condition codes, sale conditions): https://www.ctaplan.com/publicdocs/ctaplan/notifications/trader-update/CTS_Pillar_Output_Specification.pdf
- Joel Hasbrouck, "Measuring the Information Content of Stock Trades", Journal of Finance 46(1), 1991: https://doi.org/10.1111/j.1540-6261.1991.tb03749.x
