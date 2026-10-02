---
{
  "title": "Manipulation and Its Detection: Spoofing, Layering, and the Prosecuted Cases",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The statutory definition of spoofing in the Commodity Exchange Act is:", "opts": ["Trading more than 1,000 contracts a day", "Bidding or offering with the intent to cancel the bid or offer before execution", "Cancelling any order within one second", "Trading on both sides of the market"], "correct": 1, "explain": "Section 4c(a)(5)(C), added by Dodd-Frank in 2010. Intent is the element; cancellation alone is legal and constant."},
    {"q": "Michael Coscia's 2013 CFTC settlement and 2015 criminal conviction concerned conduct over what period?", "opts": ["Ten years", "About ten weeks in 2011", "The 2010 flash crash", "2008 to 2016"], "correct": 1, "explain": "August 8 to October 18, 2011, on CME Globex, earning about $1.4 million. He was the first person criminally convicted under the Dodd-Frank anti-spoofing provision."},
    {"q": "JPMorgan's September 2020 resolution totalled $920 million. The CFTC's components were:", "opts": ["$920M fine only", "$436.4M fine, $311.7M restitution, $172M disgorgement", "$500M fine, $420M restitution", "$920M disgorgement"], "correct": 1, "explain": "A record CFTC penalty for spoofing in precious-metals and Treasury futures from 2008 to 2016, alongside a DOJ deferred prosecution agreement."},
    {"q": "In the representative pattern, the trader placed 3,000 contracts of spoof orders to get 200 filled. The order-to-fill ratio on that cycle was:", "opts": ["1.5 to 1", "15 to 1", "16 to 1", "3,000 to 1"], "correct": 2, "explain": "(3,000 + 200) / 200 = 16 orders entered per contract filled. Surveillance looks at ratios like this relative to a trader's own baseline."},
    {"q": "Why is a high cancellation rate, on its own, not evidence of spoofing?", "opts": ["Because cancellations are illegal anyway", "Because legitimate market makers cancel and replace quotes continuously as hedging instruments move; the element is intent, shown by pattern and timing", "Because exchanges delete cancel records", "Because only futures can be spoofed"], "correct": 1, "explain": "The cases were built on the pattern: large orders on one side, small fills on the other, cancellation within milliseconds of the fill, repeated thousands of times."}
  ],
  "task": "Read the CFTC's 2013 Coscia order and write down, in one sentence each, the three facts the CFTC relied on to show intent."
}
---

## What manipulation of the book looks like

Lesson 1 said displayed depth is a snapshot of intentions. Spoofing is the deliberate display of an intention the trader does not have: large orders placed to move other participants, cancelled before they can execute, while a small genuine order on the other side gets filled at the price the display created. Layering is the same idea with several orders stacked at successive price levels. Both exploit the fact that everyone in lessons 5 through 7 reads the book and the tape as information.

The Dodd-Frank Act of 2010 made spoofing an explicit offence in the Commodity Exchange Act: Section 4c(a)(5)(C) prohibits "bidding or offering with the intent to cancel the bid or offer before execution." The element is intent. Cancelling orders is legal and, as lesson 9 showed, happens millions of times a day as market makers reprice. What the cases below share is a pattern from which intent was inferred: size, timing, repetition and profit.

## The cases

Coscia. On July 22, 2013 the CFTC ordered Panther Energy Trading and its principal Michael Coscia to pay $2.8 million, comprising a $1.4 million civil penalty and $1.4 million of disgorged profits, and banned them from trading on CFTC-registered venues for a year. The conduct ran from August 8 to October 18, 2011, on CME Globex across a range of commodity futures, using an algorithm designed to place and quickly cancel bids and offers. On November 3, 2015 a federal jury in Chicago convicted Coscia on six counts of commodities fraud and six counts of spoofing, the first criminal conviction under the Dodd-Frank provision; prosecutors described a scheme that yielded more than $1 million over about two and a half months. In July 2016 he was sentenced to three years in prison. The mechanics, as the CFTC described them: place a small order on one side, then several large orders on the other side to create the appearance of pressure, and cancel the large orders within milliseconds once the small order filled.

Sarao. Navinder Singh Sarao, trading E-mini S&P 500 futures from his home in Hounslow, England, was charged in 2015 and pleaded guilty on November 9, 2016 to one count of wire fraud and one count of spoofing. The Justice Department stated that from at least January 2009 through April 2014 he used an automated program and other techniques to manipulate the E-mini market, and that he admitted to at least $12.8 million of illicit gains. A federal court in Chicago had ordered him to pay more than $38 million in monetary sanctions in the CFTC's parallel civil action. His conduct on May 6, 2010 was alleged to have contributed to the conditions of the flash crash; Kirilenko et al. (lesson 9) locate the trigger elsewhere, and the two accounts are compatible: a fragile market and a manipulator active in it on the same afternoon.

JPMorgan. On September 29, 2020 the CFTC ordered JPMorgan Chase & Co. and affiliates to pay $920 million, the largest penalty in CFTC history for spoofing: a $436.4 million fine, $311.7 million in restitution and more than $172 million in disgorgement. The DOJ entered a three-year deferred prosecution agreement on parallel charges; the SEC separately resolved the Treasury cash-market conduct. The conduct, from at least 2008 through 2016, involved numerous traders on the precious metals and Treasuries desks placing hundreds of thousands of orders in gold, silver, platinum, palladium, Treasury note and Treasury bond futures with the intent to cancel before execution. Two of the desk's traders were later convicted at trial in 2022.

Three cases, one pattern: a genuine order the trader wants filled, a much larger display on the opposite side, cancellation timed to the fill, thousands of repetitions.

## How it is detected

The prosecutions were built on exchange audit trails, which record every order, modification and cancellation with a timestamp and an account identifier. Surveillance systems at CME, the equity exchanges and FINRA look for combinations: orders that are large relative to the trader's fills; orders that rest for very short periods and are cancelled rather than executed; order-to-fill ratios far above the trader's own baseline; cancellations that cluster within milliseconds of a fill on the other side; and profit that accrues consistently on the small side. No single feature is dispositive, because legitimate strategies exhibit each of them. The pattern across thousands of cycles is what the Coscia jury was shown.

For you, the practical point is that spoofing exists, is prosecuted, and is invisible on a Level 2 screen in real time: a displayed 5,000-lot that vanishes could be a spoof or a market maker repricing. The defence is not detection but not depending on displayed size, which is what lesson 12's rules say.

## Worked example

A representative spoofing cycle in a futures contract, constructed to match the structure the CFTC described in the Coscia order. The numbers are illustrative; the CFTC order does not publish per-cycle sizes.

The book: bid 1,250.00 × 400 contracts, ask 1,250.25 × 350 contracts.

1. The trader places a genuine buy order for 200 contracts at 1,250.00, joining the bid.
2. Within a few milliseconds the trader places three sell orders: 1,000 at 1,250.50, 1,000 at 1,250.75, 1,000 at 1,251.00. The displayed ask side now shows 3,350 contracts within three ticks, against 600 on the bid.
3. Other participants' algorithms read the imbalance as selling pressure. Some sellers, seeing they are now far back in the queue at higher prices, hit the bid to get out ahead of the apparent wall. The trader's 200 contracts at 1,250.00 fill.
4. Within milliseconds of the fill, the trader cancels all three sell orders. Displayed ask depth drops from 3,350 to 350.
5. The trader mirrors the cycle: rests a genuine sell of 200 at 1,250.25, layers 3,000 of buy orders at 1,249.75, 1,249.50 and 1,249.25, waits for buyers to lift the offer, then cancels the layers.

Per round trip: bought 200 at 1,250.00, sold 200 at 1,250.25. Profit = 200 × 0.25 × $50 per point (E-mini multiplier) = $2,500. Fees at $2.50 per side per contract = 200 × 2 × 2.50 = $1,000. Net $1,500 per cycle.

Surveillance metrics for this cycle:

- Orders entered: 200 + 3,000 (buy side) and 200 + 3,000 (sell side) = 6,400 contracts. Filled: 400. Order-to-fill ratio = 6,400 / 400 = 16 to 1.
- Cancel ratio on the large orders: 6,000 entered, 6,000 cancelled, 0 filled: 100%.
- Resting time of large orders: milliseconds, terminating within milliseconds of the small side's fill.
- Fill profile: every fill on the small side, none on the large.

A market maker quoting the same contract might show an order-to-fill ratio of 16 to 1 too, but its cancels would be spread across both sides, uncorrelated with its own fills, and its large orders would sometimes fill. Two of the four metrics separate the cases; the joint pattern across a day of cycles is what makes the inference of intent, and at $1,500 per cycle a trader running the loop a hundred times a day earns $150,000, which is the scale of Coscia's $1.4 million over ten weeks.

Now the JPMorgan arithmetic. $920 million over conduct from 2008 through 2016: $436.4 + $311.7 + $172.0 = $920.1 million. Restitution of $311.7 million is the CFTC's measure of harm to other market participants, the people on the other side of hundreds of thousands of orders, most of whom were market makers and algorithms reading displayed depth exactly as this course has taught you to. That is the cost of trusting the book, quantified by a regulator.

## Chart

![Flow diagram of a spoofing cycle: rest a small genuine buy; layer large sell orders above the ask; the book looks heavy and sellers hit the bid; the small buy fills and the layers are cancelled within milliseconds; the pattern is mirrored to sell out. Source: pattern as described in CFTC Order, Panther Energy Trading and Michael Coscia, July 22, 2013.](figures/spoofing-cycle.svg)

The diagram is what the audit trail showed the jury. On your screen it looks like depth appearing and disappearing, which is also what legitimate quoting looks like.

## Sources

- CFTC, "CFTC Orders Panther Energy Trading LLC and its Principal Michael J. Coscia to Pay $2.8 Million ... for Spoofing", Release 6649-13 (July 22, 2013): https://www.cftc.gov/PressRoom/PressReleases/6649-13
- US Department of Justice, "Futures Trader Pleads Guilty to Illegally Manipulating the Futures Market in Connection With 2010 'Flash Crash'" (November 9, 2016): https://www.justice.gov/archives/opa/pr/futures-trader-pleads-guilty-illegally-manipulating-futures-market-connection-2010-flash
- CFTC, "CFTC Orders JPMorgan to Pay Record $920 Million for Spoofing and Manipulation", Release 8260-20 (September 29, 2020): https://www.cftc.gov/PressRoom/PressReleases/8260-20
- Commodity Exchange Act Section 4c(a)(5), 7 U.S.C. § 6c(a)(5) (disruptive practices, including spoofing): https://www.law.cornell.edu/uscode/text/7/6c
