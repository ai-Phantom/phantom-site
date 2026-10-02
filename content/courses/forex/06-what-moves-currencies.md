---
{
  "title": "What Moves Currencies: Rates, Inflation, Current Accounts, Risk Sentiment and Intervention",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "On 2026-09-23 the Fed's target range was 3.75% to 4.00%, the ECB deposit rate 2.50% and the BoJ policy rate 1.25%. Which currency had the highest short-term rate?", "opts": ["Euro", "Yen", "US dollar", "They were equal"], "correct": 2, "explain": "The dollar, at a midpoint of 3.875%, versus 2.50% for the euro and 1.25% for the yen."},
    {"q": "Covered interest parity implies the one-month EUR/USD forward should trade where, relative to spot, when dollar rates exceed euro rates?", "opts": ["Below spot", "At spot", "Above spot", "Cannot be determined"], "correct": 2, "explain": "The higher-rate currency (USD, the quote) trades at a forward discount, which means EUR/USD forward is above spot: about +13 pips for one month at the rates on 2026-09-23."},
    {"q": "Why does a higher interest rate not guarantee a stronger currency?", "opts": ["Because rates never affect currencies", "Because it is the change in expected rates relative to what is priced, not the level, that moves the spot rate, and inflation can erode the real rate", "Because central banks always intervene", "Because only the current account matters"], "correct": 1, "explain": "Markets price the expected path. A hike that was fully expected moves nothing; a surprise does. And a high nominal rate with higher inflation is a low real rate."},
    {"q": "What is the usual sign of the relationship between global risk appetite and the Japanese yen?", "opts": ["Risk-off strengthens the yen as funding trades are unwound", "Risk-off weakens the yen", "There is no relationship", "The yen only moves on BoJ decisions"], "correct": 0, "explain": "The yen is a low-rate funding currency. When leveraged positions are cut, yen borrowings are repaid, which buys yen. Lesson 7 shows this in 2008 and 2024."},
    {"q": "How does a central bank or finance ministry intervene to weaken a rising foreign currency, and why is the effect often temporary?", "opts": ["It raises interest rates permanently", "It sells its reserves of the foreign currency and buys its own; the effect fades unless the rate differential that caused the move also changes", "It bans trading", "It cannot intervene"], "correct": 1, "explain": "Japan's Ministry of Finance sold dollars for yen in 2024; USD/JPY fell sharply on the days of intervention but the trend only reversed when rate expectations changed."}
  ],
  "task": "Write one paragraph, with sources, on why the dollar, the euro and the yen sit at their current policy rates and what the next scheduled decision for each is."
}
---

## The price of one money in another

An exchange rate is a relative price, so everything that moves it must be relative too: not US growth but US growth relative to European growth, not inflation but inflation relative to a trading partner's. This lesson organises the drivers into five groups, from fastest-acting to slowest, and then shows the one relationship that is close to mechanical, interest parity, with real numbers.

## Interest rates and their expected path

The most reliable short-term driver is the difference between two currencies' interest rates, and more precisely the difference between what markets expect those rates to be and what they turn out to be. Capital moves toward higher expected returns, and the return on holding a currency for a short period is its interest rate.

On 2026-09-23 the three largest currencies stood as follows. The Federal Reserve raised its federal funds target range on 2026-09-16 by a quarter point to **3.75% to 4.00%**. The European Central Bank's deposit facility rate has been **2.50%** since 2026-09-16, after increases in June and September 2026. The Bank of Japan raised its guideline for the uncollateralised overnight call rate to **around 1.25%** on 2026-09-18, from 1.0%. The Reserve Bank of Australia's cash rate target has been **4.35%** since May 2026.

The level tells you which way the carry flows (lesson 7). The change relative to expectations tells you which way spot moves on the day. A hike everyone expected is already in the price; a hike nobody expected reprices the whole forward curve. That is why lesson 9 is about the calendar.

## Inflation and real rates

A high nominal rate with higher inflation is a low real rate, and over months to years currencies tend to follow real rates. The mechanism runs through the central bank: inflation above target makes rate rises more likely, which supports the currency; inflation falling makes cuts more likely. In the short term, a CPI print that beats expectations therefore strengthens the currency because it moves the expected rate path, not because inflation itself is good for a currency. Over long horizons the sign flips: persistently higher inflation erodes purchasing power and the currency depreciates to compensate (purchasing power parity), which is why USD/TRY rose 17.9% in the year to 2026-09-23 in an almost straight line while the lira's policy rate stayed in double digits.

## Current account and capital flows

A country that imports more than it exports must sell its currency to pay for the difference, and a country that exports more accumulates foreign currency to sell. This is slow and steady rather than a daily driver, but it sets the background against which the other flows operate. It also creates the commodity-currency link: Australia's exports are dominated by iron ore, coal and gas, so a rise in those prices raises Australian export revenue and, all else equal, demand for the Australian dollar (lesson 8). Capital flows can overwhelm trade flows for years at a time, which is why the dollar, with a persistent current-account deficit, has spent long periods strengthening.

## Risk sentiment

When global investors are confident, they borrow in low-rate currencies and buy higher-yielding or riskier assets. When they are frightened, they reverse those positions. The yen and the Swiss franc, both low-rate currencies, are bought in a crisis because leveraged positions funded in them are repaid; the Australian dollar, the New Zealand dollar and emerging-market currencies are sold. Over the year to 2026-09-23, using ECB reference rates, daily changes in AUD/JPY had a correlation of +0.61 with USD/JPY and +0.55 with AUD/USD, which is the signature of a pair that expresses risk appetite from both sides. Lesson 7 shows how violent this can be.

## Intervention

Governments sometimes step into the market directly. Japan's Ministry of Finance, which controls intervention in Japan, publishes its operations monthly. It sold dollars for yen in late April and May 2024 and again in July 2024 when USD/JPY was above 160; the ECB's reference rates show USD/JPY at 161.58 on 2024-07-11 and 158.74 on 2024-07-12, a 284-pip drop on the day of the July operation. The Swiss National Bank has intervened for years to cap the franc, and emerging-market central banks intervene routinely. Intervention works on the day; it holds only if the interest-rate story that drove the move also changes, which in Japan's case it did on 2024-07-31 when the BoJ raised its rate to 0.25%.

## Worked example

Interest parity is the one place where the link between rates and exchange rates is arithmetic rather than judgement. Covered interest parity says the forward exchange rate must equal the spot rate adjusted for the two interest rates, otherwise a riskless profit exists. For a pair BASE/QUOTE with spot S, quote-currency rate i_q, base-currency rate i_b and a term of T years on a money-market basis:

F = S × (1 + i_q × T) ÷ (1 + i_b × T)

Use the ECB reference rates of 2026-09-23 and the policy rates above as proxies for one-month money-market rates (in practice dealers use deposit or OIS rates a little away from policy rates, but the structure is identical). T = 30/360.

**EUR/USD.** S = 1.1411. i_q (USD) = 3.875%, the midpoint of the Fed's range. i_b (EUR) = 2.50%.
Numerator: 1 + 0.03875 × 30/360 = 1.0032292. Denominator: 1 + 0.025 × 30/360 = 1.0020833. Ratio = 1.0011435.
F = 1.1411 × 1.0011435 = **1.14240**, which is 13.0 pips above spot. The higher-rate currency (the dollar) is at a forward discount: you receive more dollars per euro in a month than today, which exactly offsets the extra interest the dollars earn. A long EUR/USD position held for a month therefore pays about 13 pips of carry, which shows up as the negative swap in lesson 7.

**USD/JPY.** S = 157.92. i_q (JPY) = 1.25%. i_b (USD) = 3.875%.
Numerator: 1 + 0.0125 × 30/360 = 1.0010417. Denominator: 1.0032292. Ratio = 0.9978195.
F = 157.92 × 0.9978195 = **157.576**, which is 34.4 pips below spot. Long USD/JPY earns roughly 34 pips of carry per month at these rates, before the broker's markup.

**AUD/USD.** S = 0.7067. i_q (USD) = 3.875%. i_b (AUD) = 4.35%.
Ratio = 1.0032292 ÷ 1.0036250 = 0.9996056. F = 0.7067 × 0.9996056 = **0.70642**, 2.8 pips below spot. The Australian dollar, at a slightly higher rate, is at a small forward discount.

Check against a broker: OANDA TMS Brokers' published swap table for 2026-09-21 to 2026-09-27 quotes long USD/JPY at +1.81% per year, which at 157.92 is 157.92 × 0.0181 × 30/365 = 0.235 yen, or 23.5 pips per 30 days, against the 34.4 pips parity implies. The difference is the broker's financing spread (lesson 7).

## Table

| Currency | Policy rate on 2026-09-23 | Set by | Last change | 1-month CIP forward vs spot against USD |
| --- | --- | --- | --- | --- |
| US dollar | 3.75% to 4.00% (midpoint 3.875%) | FOMC | +25 bp, 2026-09-16 | Reference |
| Euro | 2.50% (deposit facility) | ECB Governing Council | +25 bp, effective 2026-09-16 | EUR/USD forward +13.0 pips |
| Japanese yen | Around 1.25% (overnight call rate) | BoJ Policy Board | +25 bp, 2026-09-18 | USD/JPY forward −34.4 pips |
| Australian dollar | 4.35% (cash rate target) | RBA Board | +25 bp, 2026-05-06 | AUD/USD forward −2.8 pips |

## Putting the drivers in order

For a trade held hours to days, the rate-expectations channel dominates, and the calendar of decisions and data is your map. For a trade held weeks to months, carry accrues daily and risk sentiment decides whether you keep it (lesson 7). For anything longer, inflation differentials and current accounts set the drift. Intervention is the wildcard: it is announced after the fact, it is largest when a currency has moved fastest, and it is aimed squarely at the most crowded position.

## Sources

- Board of Governors of the Federal Reserve System, FOMC statement, 16 September 2026 (the target-rate history is on the Board's open market operations page): https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm
- European Central Bank, key ECB interest rates: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html
- Bank of Japan, Change in the Guideline for Money Market Operations, 18 September 2026: https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260918a.pdf
- Reserve Bank of Australia, cash rate target history: https://www.rba.gov.au/statistics/cash-rate/
