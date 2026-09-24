---
{
  "title": "Quoting: Base and Quote Currency, Pips, Pipettes, Lots and Pip Value",
  "duration": "17 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "In the quote USD/JPY 157.92, which currency is the base and what does the number mean?", "opts": ["JPY is the base; 157.92 dollars per yen", "USD is the base; 157.92 yen per dollar", "Both are base currencies", "USD is the base; 157.92 dollars per yen"], "correct": 1, "explain": "The first currency is the base and the price is how many units of the quote currency (yen) buy one unit of base (one dollar)."},
    {"q": "What is one pip in USD/JPY?", "opts": ["0.0001", "0.001", "0.01", "1"], "correct": 2, "explain": "Yen pairs are quoted to two decimals, so a pip is 0.01. Most other pairs use 0.0001."},
    {"q": "What is the pip value, in US dollars, of one standard lot of USD/JPY at 157.92?", "opts": ["$10.00", "$6.33", "$1.00", "$15.79"], "correct": 1, "explain": "0.01 × 100,000 = 1,000 yen per pip; 1,000 / 157.92 = $6.33."},
    {"q": "A broker quotes EUR/USD at 1.13913 / 1.13919. How wide is the spread?", "opts": ["6 pips", "0.6 pips", "0.06 pips", "60 pips"], "correct": 1, "explain": "The fifth decimal is a pipette, a tenth of a pip. Six pipettes is 0.6 pips."},
    {"q": "You buy 0.25 lots of EUR/USD and the price rises 40 pips. What is your gain?", "opts": ["$40", "$100", "$250", "$1,000"], "correct": 1, "explain": "One lot is $10 per pip in a USD-quoted pair; 0.25 lots is $2.50 per pip; 40 pips × $2.50 = $100."}
  ],
  "task": "Compute the pip value in your account currency for one standard lot of EUR/USD, USD/JPY, GBP/USD and USD/CAD using today's rates from your broker, and keep the sheet; you will reuse it in every later lesson."
}
---

## Reading a currency pair

A currency pair is written as BASE/QUOTE, and the price is the number of units of the quote currency that one unit of the base currency buys. EUR/USD at 1.1411 means one euro costs 1.1411 dollars. USD/JPY at 157.92 means one dollar costs 157.92 yen.

The arrangement is fixed by convention, not economics. The euro is always the base against everything; sterling is the base against everything except the euro; the dollar is the base against the yen, the Swiss franc, the Canadian dollar and most emerging currencies, but the quote currency against the euro, sterling, the Australian and New Zealand dollars. You will get used to it. The practical point is that "buying EUR/USD" means buying euros and selling dollars, and "selling USD/JPY" means selling dollars and buying yen. You are always long one currency and short another; there is no such thing as a one-sided position.

When the pair rises, the base is strengthening against the quote. When EUR/USD goes from 1.1411 to 1.1511, the euro gained about 0.88% against the dollar, or, equivalently, the dollar lost about 0.87% against the euro (the two percentages differ slightly because the base of the calculation differs).

## Pips and pipettes

A pip ("percentage in point") is the smallest conventional price increment. For most pairs it is the fourth decimal place, 0.0001. For yen pairs, which trade at prices in the hundreds, it is the second decimal, 0.01. So EUR/USD moving from 1.1411 to 1.1451 moved 40 pips; USD/JPY moving from 157.92 to 158.32 also moved 40 pips.

Most brokers now quote a fifth decimal (third for yen pairs), called a pipette or fractional pip. A quote of 1.13913 / 1.13919 (bid / ask, as shown on IG's EUR/USD page when this lesson was written on 2026-09-24) has a spread of 0.00006, which is 0.6 pips or 6 pipettes. Be careful when a platform reports "points": some vendors mean pipettes, some mean pips.

A pip is a price unit, not a money unit. How much money a pip is worth depends on your position size and on which currency the pair is quoted in, which is the subject of the rest of this lesson.

## Lots

Position size in FX is expressed in lots of the base currency:

- Standard lot: 100,000 units of base currency
- Mini lot: 10,000 units
- Micro lot: 1,000 units

Most retail brokers let you trade in steps of 0.01 standard lots (one micro lot). tastyfx's product details, for example, state a contract size of 100,000 base currency with a minimum of 0.01 lots, plus 10,000-unit mini contracts on seven dollar pairs. "Buying 0.25 lots of EUR/USD" means buying 25,000 euros.

Notional value is lots × contract size × price in the quote currency. For 0.25 lots of EUR/USD at 1.1411: 25,000 × 1.1411 = $28,527.50. That is the amount you actually control, and the amount that leverage (lesson 4) is measured against.

## Pip value: the arithmetic

The value of one pip on one lot is:

pip value (in quote currency) = pip size × contract size

For EUR/USD: 0.0001 × 100,000 = 10 US dollars per pip per standard lot. Because the quote currency is the dollar, that is already in dollars and it does not change with the exchange rate. This is why the dollar-quoted pairs (EUR/USD, GBP/USD, AUD/USD, NZD/USD) are the easiest to size for a dollar account: $10 per pip per lot, $1 per mini lot, $0.10 per micro lot, always.

For a pair where the dollar is the base, the pip value is in the foreign currency and must be converted:

pip value (USD) = pip size × contract size ÷ current price

For USD/JPY at 157.92: 0.01 × 100,000 = 1,000 yen; 1,000 ÷ 157.92 = $6.33 per pip per lot. Note the direction: a stronger yen (lower USD/JPY) makes each pip worth more dollars.

For a cross with neither currency being the dollar, convert the quote currency to dollars at its own rate:

pip value (USD) = pip size × contract size × (quote currency's USD rate)

For EUR/GBP, one pip on one lot is £10; at GBP/USD 1.3276 that is $13.28.

## Worked example

Use the ECB's euro reference rates for 2026-09-23 (the ECB fixes at about 14:15 CET each business day). EUR/USD was 1.1411, EUR/JPY 180.20, EUR/GBP 0.8595, EUR/CAD 1.6077, EUR/AUD 1.6146. Deriving the dollar crosses: USD/JPY = 180.20 ÷ 1.1411 = 157.92; GBP/USD = 1.1411 ÷ 0.8595 = 1.3276; USD/CAD = 1.6077 ÷ 1.1411 = 1.4089; AUD/USD = 1.1411 ÷ 1.6146 = 0.7067.

Now size a trade. Your account is in US dollars, you will risk $100, and your stop is 40 pips away.

**EUR/USD.** Pip value per lot is $10. Dollars per pip you can afford: $100 ÷ 40 pips = $2.50 per pip. Lots = $2.50 ÷ $10 = 0.25 lots, or 25,000 euros. Check: 0.25 × $10 × 40 = $100.

**USD/JPY at 157.92.** Pip value per lot = 1,000 yen ÷ 157.92 = $6.332. Dollars per pip: $2.50. Lots = 2.50 ÷ 6.332 = 0.395, rounded down to the broker's 0.01 step: 0.39 lots, or 39,000 dollars. Check: 0.39 × $6.332 × 40 = $98.78, just inside the $100 budget. (Rounding up to 0.40 would give $101.31, just outside it. Always round down.)

**USD/CAD at 1.4089.** Pip value per lot = C$10 ÷ 1.4089 = $7.098. Lots = 2.50 ÷ 7.098 = 0.352, round down to 0.35 lots. Check: 0.35 × 7.098 × 40 = $99.37.

**GBP/USD at 1.3276.** Quote currency is the dollar, so pip value is $10 per lot regardless of the rate. Lots = 0.25, same as EUR/USD.

Notice what changed and what did not. The dollar risk was fixed at $100 in every case; the stop was fixed at 40 pips; the only variable was the pip value, and the pip value was set by which currency is the quote. That is the whole skill. If your account were in euros instead, you would convert each pip value into euros at EUR/USD and the arithmetic would be otherwise identical.

One more conversion that catches people: profit on a non-dollar-quoted pair is realised in the quote currency and converted when you close. Some brokers charge for that conversion; tastyfx states a 0.5% charge on the conversion rate for non-USD quote-currency pairs. On a £100 profit that is 50 pence, small but not zero, and it is a reason dollar-account traders lean toward dollar-quoted pairs.

## Table

| Pair | Price (ECB fix, 2026-09-23) | Pip size | Pip value, 1 lot, in quote currency | Pip value, 1 lot, in USD | Lots for $2.50 per pip |
| --- | --- | --- | --- | --- | --- |
| EUR/USD | 1.1411 | 0.0001 | $10.00 | $10.00 | 0.25 |
| GBP/USD | 1.3276 | 0.0001 | $10.00 | $10.00 | 0.25 |
| AUD/USD | 0.7067 | 0.0001 | $10.00 | $10.00 | 0.25 |
| USD/JPY | 157.92 | 0.01 | ¥1,000 | $6.33 | 0.39 |
| USD/CAD | 1.4089 | 0.0001 | C$10 | $7.10 | 0.35 |
| USD/CHF | 0.8229 | 0.0001 | CHF 10 | $12.15 | 0.20 |
| EUR/GBP | 0.8595 | 0.0001 | £10 | $13.28 | 0.18 |
| USD/MXN | 17.439 | 0.0001 | MXN 10 | $0.57 | 4.36 |

The last row is a warning rather than a suggestion. A pip in USD/MXN is worth 57 cents per lot because the peso is a small unit, so the pair moves hundreds of pips a day and a "40-pip stop" would be inside the spread. Pip counts are not comparable across pairs; dollar risk is. Lesson 3 makes that concrete.

## Sources

- European Central Bank, euro foreign exchange reference rates, 2026-09-23 fix: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html
- IG, EUR/USD market page (quote 1.13913 / 1.13919, pip value USD 10 per contract, accessed 2026-09-24): https://www.ig.com/uk/forex/markets-forex/eur-usd
- tastyfx, forex product details (contract size, minimum size, conversion charge): https://www.tastyfx.com/help-and-support/product-details/what-are-tastyfxs-forex-product-details/
