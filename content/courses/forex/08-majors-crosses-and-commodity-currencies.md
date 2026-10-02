---
{
  "title": "Majors, Crosses and Commodity Currencies, and How Pairs Move Together",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "What distinguishes a cross from a major pair?", "opts": ["A cross has wider spreads", "A cross does not contain the US dollar", "A cross is quoted in pipettes", "A cross is only traded in Asia"], "correct": 1, "explain": "EUR/JPY, GBP/JPY and AUD/JPY are crosses. Their prices are derived from the two dollar pairs, and most of their liquidity is too."},
    {"q": "Over the year to 2026-09-23, daily changes in EUR/USD and USD/CHF had a correlation of −0.88. What does that imply for a trader long EUR/USD and short USD/CHF?", "opts": ["The positions hedge each other", "The positions are nearly the same bet: both are short dollars against a European currency", "The positions are independent", "One will always profit"], "correct": 1, "explain": "A negative correlation between EUR/USD and USD/CHF means EUR/USD and CHF/USD move together. Long EUR/USD and short USD/CHF is one dollar-short bet expressed twice."},
    {"q": "Two positions each risk $100 and their returns have correlation 0.88. What is the combined one-sigma risk?", "opts": ["$100", "$141", "$194", "$200"], "correct": 2, "explain": "√(100² + 100² + 2 × 0.88 × 100 × 100) = 100 × √3.76 = $194, almost the $200 of perfect correlation."},
    {"q": "Why are AUD, NZD and CAD called commodity currencies?", "opts": ["They are backed by gold", "Their countries' exports are dominated by raw materials, so export revenue and the terms of trade move with commodity prices", "They are quoted against commodities", "They only trade during commodity market hours"], "correct": 1, "explain": "The RBA's own explainer attributes swings in the Australian dollar to the terms of trade, driven by iron ore, coal and gas prices."},
    {"q": "Which currency pair was the most traded in April 2025 according to the BIS survey?", "opts": ["USD/JPY", "EUR/USD", "GBP/USD", "USD/CNY"], "correct": 1, "explain": "EUR/USD remained the largest pair; the top ten pairs all contain the dollar."}
  ],
  "task": "Compute the correlation of daily changes between two pairs you trade, using one year of closes from any source, and decide whether you have been running one position twice."
}
---

## The three families

Currency pairs are conventionally sorted into three groups. The **majors** are the dollar pairs of the most traded currencies: EUR/USD, USD/JPY, GBP/USD, USD/CHF, AUD/USD, USD/CAD and NZD/USD. The BIS 2025 survey found the dollar on one side of 89.2% of all trades and the top ten pairs all containing the dollar, with EUR/USD the largest, so this group is where the liquidity lives.

**Crosses** are pairs with no dollar in them: EUR/JPY, GBP/JPY, EUR/GBP, AUD/JPY, EUR/CHF and so on. A cross price is arithmetic on two dollar pairs (EUR/JPY = EUR/USD × USD/JPY), and much of its liquidity is synthetic too: a dealer quoting EUR/JPY may hedge with two dollar trades. Spreads are wider, and a cross moves whenever either leg moves.

**Exotics** are dollar pairs of smaller or less freely traded currencies: USD/MXN, USD/ZAR, USD/TRY, USD/CNH and dozens more. The BIS notes that the renminbi reached 8.5% of turnover in 2025, so "exotic" is a statement about liquidity and convertibility, not size. Lesson 3 showed what that means for costs.

## Commodity currencies

Australia, New Zealand and Canada export raw materials: iron ore, coal and gas for Australia; dairy and meat for New Zealand; oil for Canada. The Reserve Bank of Australia's explainer on exchange rates makes the mechanism explicit: when commodity prices rise, Australia's terms of trade improve, export income rises, and demand for the Australian dollar rises with it; the reverse happens when they fall. Norway (oil), Chile (copper), South Africa (gold, platinum) and Brazil (iron ore, soybeans) are the same story with wider spreads.

Two practical consequences. First, these currencies inherit the volatility of their commodities. Over the year to 2026-09-23, annualised volatility from ECB reference rates was 7.8% for AUD/USD and 8.1% for NZD/USD against 5.4% for EUR/USD. Second, they carry a risk-sentiment loading: commodity demand is a bet on global growth, so the Australian dollar tends to fall when equities fall, which is why AUD/JPY (a commodity currency against a funding currency) is the market's favourite risk barometer and the vehicle for the 2008 crash in lesson 7.

## Correlation: pairs are not independent

Because every major has the dollar on one side, the majors are mostly one variable, the dollar, viewed from seven angles. The table below shows the correlation of daily log changes between the majors over 2025-09-23 to 2026-09-23, computed from the ECB's daily reference rates (256 observations; dollar pairs derived from the euro rates).

Read the signs with care. EUR/USD and USD/CHF at −0.88 does not mean the euro and the franc diverge; it means EUR/USD rising (dollar falling) coincides with USD/CHF falling (dollar falling). The franc and the euro move together against the dollar almost perfectly. EUR/USD and GBP/USD at +0.84 says the same thing for sterling. AUD/USD and NZD/USD at +0.81 are near-twins. USD/CAD, quoted the other way round, is negatively correlated with all of them for the same reason.

The one pair that stands apart is AUD/JPY, whose correlation with EUR/USD is only +0.08: it is not a dollar bet at all but a risk bet, correlated +0.61 with USD/JPY and +0.55 with AUD/USD, that is, with both of its legs' risk sensitivity.

## Worked example

You hold two positions, each sized (lesson 2) to risk $100 at its stop: long EUR/USD and short USD/CHF. You believe you have diversified. Test it.

**Step 1: identify the exposure.** Long EUR/USD is long euros, short dollars. Short USD/CHF is short dollars, long francs. Both positions are short the dollar against a European currency.

**Step 2: look up the correlation.** From the table, the correlation of daily changes between EUR/USD and USD/CHF over the year was −0.88. Because you are short USD/CHF, the correlation between your two positions' P&L is +0.88.

**Step 3: combine the risks.** For two positions with one-sigma dollar risks a and b and correlation ρ, the combined one-sigma risk is √(a² + b² + 2ρab).

- ρ = +0.88 (your actual book): √(100² + 100² + 2 × 0.88 × 100 × 100) = 100 × √(1 + 1 + 1.76) = 100 × √3.76 = **$194**.
- ρ = 0 (what you assumed): 100 × √2 = **$141**.
- ρ = +1 (one position, doubled): **$200**.

You are running $194 of risk while budgeting for $141, and you are within 3% of simply having doubled one trade. If your plan caps total open risk at 2% of a $10,000 account, this book is at 1.94%, not the 1.41% you would have written down.

**Step 4: the alternative.** Replace the USD/CHF short with a long AUD/JPY (correlation +0.08 with EUR/USD): combined risk = 100 × √(2 + 0.16) = **$147**. Nearly independent, and you now hold one dollar view and one risk-appetite view rather than the same dollar view twice. Whether that is a better book depends on whether you want a risk-appetite view; the point is that you now know what you hold.

The same arithmetic warns against the classic "hedge" of long EUR/USD and long USD/CHF: combined risk = 100 × √(2 − 1.76) = $49, which is a position that barely moves and pays two spreads and two swaps (long USD/CHF received +2.80% but long EUR/USD paid −2.36% in the OANDA table of lesson 7, a net of +0.44%, minus costs).

## Table

Correlation of daily log changes, ECB reference rates, 2025-09-23 to 2026-09-23 (256 observations). Annualised volatility in the last column.

| Pair | EUR/USD | GBP/USD | AUD/USD | NZD/USD | USD/CAD | USD/JPY | USD/CHF | AUD/JPY | Ann. vol |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EUR/USD | 1.00 | +0.84 | +0.70 | +0.75 | −0.63 | −0.58 | −0.88 | +0.08 | 5.4% |
| GBP/USD | +0.84 | 1.00 | +0.72 | +0.74 | −0.61 | −0.47 | −0.75 | +0.19 | 6.1% |
| AUD/USD | +0.70 | +0.72 | 1.00 | +0.81 | −0.61 | −0.33 | −0.61 | +0.55 | 7.8% |
| NZD/USD | +0.75 | +0.74 | +0.81 | 1.00 | −0.65 | −0.43 | −0.74 | +0.30 | 8.1% |
| USD/CAD | −0.63 | −0.61 | −0.61 | −0.65 | 1.00 | +0.34 | +0.61 | −0.21 | 4.3% |
| USD/JPY | −0.58 | −0.47 | −0.33 | −0.43 | +0.34 | 1.00 | +0.58 | +0.61 | 8.1% |
| USD/CHF | −0.88 | −0.75 | −0.61 | −0.74 | +0.61 | +0.58 | 1.00 | −0.01 | 6.8% |
| AUD/JPY | +0.08 | +0.19 | +0.55 | +0.30 | −0.21 | +0.61 | −0.01 | 1.00 | 9.2% |

Exotics over the same window: USD/MXN 7.4%, USD/ZAR 11.0%, USD/TRY 1.5% annualised (the lira's low daily volatility hides a 17.9% one-way drift; see lesson 3).

## Correlation with equities and commodities

The signs above are one year's sample and they drift. In a year dominated by the dollar, the majors correlate near ±0.8 as here; in a year dominated by a single country's story, they decouple. The relationships with other asset classes drift more. The usual patterns, which you should verify rather than assume, are: the yen and the franc strengthen when equities fall; the Australian and Canadian dollars weaken when equities and their commodities fall; gold and the dollar move inversely more often than not. Each of these is a tendency with a sign that has flipped for months at a time. Lesson 12's journal asks you to record the correlation you assumed when you sized a book, so you can check later whether it held.

## Sources

- Bank for International Settlements, "OTC foreign exchange turnover in April 2025" (currency and pair shares): https://www.bis.org/statistics/rpfx25_fx.htm
- European Central Bank, euro foreign exchange reference rates (daily history used for correlations and volatility): https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html
- Reserve Bank of Australia, Explainer: "Exchange Rates and the Australian Economy": https://www.rba.gov.au/education/resources/explainers/exchange-rates-and-the-australian-economy.html
- OANDA TMS Brokers S.A., swap points table valid 2026-09-21 to 2026-09-27: https://www.oanda.com/eu-en/document/91
