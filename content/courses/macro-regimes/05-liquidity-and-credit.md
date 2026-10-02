---
{
  "title": "Liquidity and Credit: The Fed Balance Sheet, Reverse Repo and High-Yield Spreads",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "The Fed's total assets (FRED WALCL) went from $4.16 trillion on 2020-02-26 to $7.17 trillion on 2020-06-10. What does that number measure?", "opts": ["Bank lending", "Federal debt", "Securities the Fed bought with newly created reserves: the quantity side of monetary policy, as opposed to the price side (the funds rate)", "The money supply"], "correct": 2, "explain": "When the Fed buys a Treasury it credits a bank's reserve account. The balance sheet is the running total of those purchases less what has matured or been sold. It is a stock; the funds rate is a price."},
    {"q": "The overnight reverse repo facility (RRPONTSYD) peaked at $2.55 trillion on 2022-12-30 and was $11 billion on 2026-09-29. Why do traders watch it?", "opts": ["It is the Fed's profit", "It is where money funds park cash they cannot place elsewhere at a better rate; a large balance means the system has more reserves than it wants, a balance near zero means quantitative tightening is now draining reserves banks actually use", "It measures inflation", "It sets the funds rate"], "correct": 1, "explain": "While the RRP was full, balance-sheet reduction drained the RRP rather than bank reserves, so it had little effect on funding markets. Once it emptied, each further reduction came out of reserves."},
    {"q": "In the 2022 decline (2022-01-03 to 2022-10-12) HYG's price fell 17.7% and LQD's fell 22.8%, while in the 2020 decline (2020-02-19 to 2020-03-23) HYG fell 22.2% and LQD 12.5%. What distinguishes the two?", "opts": ["Nothing; both were credit crises", "LQD is riskier than HYG", "2022 was worse for credit", "2020 was a credit event (the riskier bond fell more); 2022 was a rates event (the longer-duration investment-grade bond fell more even though it is safer)"], "correct": 3, "explain": "LQD has roughly twice HYG's duration and far better credit quality. When it falls more than HYG, the driver is the discount rate, not default risk. That is the signature of the 2022 regime."},
    {"q": "FRED served the ICE BofA high-yield option-adjusted spread (BAMLH0A0HYM2) only from 2023-10-02 when pulled for this course. How does the lesson handle the earlier stress episodes?", "opts": ["It uses the HYG and LQD price drawdowns from Yahoo Finance as a proxy for credit stress and says so, and cites the spread only for the window FRED actually returned", "It invents values", "It skips them", "It uses the VIX instead"], "correct": 0, "explain": "A proxy is fine if it is labelled as one. The HYG price is a traded ETF, so it is a legitimate stress gauge in its own right, but it is not the same number as the index OAS."},
    {"q": "The high-yield spread peaked at 4.61 percentage points on 2025-04-07 during the tariff shock, against a 2023-2026 low of 2.59 on 2025-01-22. SPY fell 18.8% peak to trough. HYG's price fell only 5.0%. What does the comparison say about that episode?", "opts": ["Credit was in crisis", "Equity volatility was severe but credit barely moved: the episode was an equity and policy shock, not a credit or funding shock, which is consistent with its short duration", "HYG is broken", "Spreads are irrelevant"], "correct": 1, "explain": "A 2-point widening from a very tight base is a moderate move. When equities fall hard and credit does not, the growth axis has not turned; that reads as a correction, not a regime change on the credit axis."}
  ],
  "task": "Pull WALCL and RRPONTSYD from FRED and write down, for the last four year-ends, the balance sheet size and the RRP balance side by side."
}
---

## Price and quantity

Lesson 3 covered the price of money. This lesson covers its quantity, and the market that reprices fastest when the quantity is wrong: corporate credit.

The Federal Reserve's balance sheet (FRED WALCL, total assets, weekly as of Wednesday) is the running total of the securities the Fed has bought and not yet let mature. When it buys a Treasury from a bank, it pays by crediting the bank's reserve account, which is money that did not exist the day before. Quantitative easing is a policy of buying at scale; quantitative tightening is letting holdings mature without reinvesting. The funds rate is the price of reserves; the balance sheet is their supply.

The path is the story of the last two decades. Total assets were $0.91 trillion on 2008-09-03, two weeks before Lehman. They were $2.24 trillion on 2008-12-31, $4.50 trillion on 2014-12-31 after three rounds of QE, and $3.76 trillion on 2019-08-28 after the first attempt at tightening. Then the pandemic: $4.16 trillion on 2020-02-26, $7.17 trillion on 2020-06-10, a $3 trillion expansion in fifteen weeks, larger than the entire 2008-2014 programme. The peak was $8.97 trillion on 2022-04-13. Tightening from June 2022 brought it to $6.89 trillion at the end of 2024 and a low of $6.54 trillion on 2025-12-03; on 2026-09-23 it stood at $6.75 trillion.

## Where excess reserves go

If the Fed creates more reserves than banks want to hold, the surplus has to go somewhere, and where it goes tells you whether liquidity is abundant or merely adequate. The overnight reverse repurchase facility (FRED RRPONTSYD, daily) lets money-market funds and others lend cash to the Fed overnight at a fixed rate against Treasury collateral. When the funds have more cash than they can place at a better rate, the facility fills.

The balance was $134 billion on 2021-03-31. By 2021-12-31 it was $1.90 trillion; it peaked at $2.55 trillion on 2022-12-30 and was still $2.03 trillion on 2023-06-30. Then it drained: $473 billion at the end of 2024, $11 billion on 2026-09-29. The reading matters for one reason. While the facility was full, quantitative tightening removed reserves that nobody was using; the balance sheet shrank by two trillion and funding markets barely noticed. Once the facility is empty, each further reduction comes out of reserves that banks actually hold, and that is the point at which balance-sheet policy starts to bite. Mid-September 2019, when overnight repo rates spiked far above the funds target with the balance sheet near $3.8 trillion and the Fed had to resume purchases, is the prior example of what happens when that threshold is misjudged.

## Credit spreads as the stress gauge

A corporate bond yields more than a Treasury of the same maturity, and the gap, adjusted for any embedded options, is the option-adjusted spread. The spread on the high-yield index (ICE BofA US High Yield, FRED BAMLH0A0HYM2) is the cleanest single reading of how much the market fears defaults, because high-yield issuers are the first to fail when growth turns. The investment-grade spread (BAMLC0A0CM) tells the same story with less amplitude.

There is a data problem to report honestly. When pulled for this course on 2026-09-30, FRED served the high-yield spread only from 2023-10-02 (785 daily observations to 2026-09-29), regardless of the start date requested. That window contains one stress episode. For the earlier episodes the lesson uses the prices of the two large credit ETFs from Yahoo Finance, HYG (high yield, launched April 2007) and LQD (investment grade, July 2002), as a proxy. An ETF price is not a spread, but its drawdown during a stress window is a fair gauge of how hard credit was hit, and comparing the two funds separates a credit shock from a rates shock, which a spread alone does not do.

## Reading a stress episode

Two questions sort every episode. Did high yield fall more than investment grade? If so the driver is default fear, a credit event. Did investment grade fall as much or more? Then the driver is the discount rate, a rates event, because LQD carries roughly twice HYG's duration and far less default risk. And did credit fall as much as equity? If equity falls hard and credit barely moves, the growth axis has not turned; the episode is an equity or policy shock.

The worked example runs six episodes through those questions. The 2008 and 2020 declines are credit events: HYG fell three times as much as LQD. The 2022 decline is a rates event: LQD fell more than HYG. The 2025 tariff shock is an equity event: SPY fell 18.8% while HYG's price fell 5.0% and the spread widened to 4.61 points, well short of any prior crisis reading. The 2011 and 2015-16 episodes sit between: moderate credit stress, no rates component.

## How the axis enters a regime model

Liquidity and credit are slow variables that set the background against which the fast variables (trend, volatility) are read. A VIX spike with the balance sheet expanding, the RRP full and spreads tight is a different animal from the same spike with reserves draining and spreads at 6 points. The first is 2021 or early 2025; the second is 2008. The classifier of lesson 9 does not include this axis, on purpose, and the lesson explains what adding it would cost. But the sizing policy of lesson 10 should, and the case studies of lesson 12 show why: the two bear markets of 2008 and 2020 were resolved by the balance sheet, and the 2022 bear market was caused by it.

## Worked example

Data: FRED WALCL (weekly, Wednesday), RRPONTSYD (daily), BAMLH0A0HYM2 (daily, served from 2023-10-02), pulled 2026-09-30. Yahoo Finance chart API daily bars for HYG (4,900 rows, 2007-04-11 to 2026-09-30), LQD (6,082 rows, 2002-07-30 to 2026-09-30) and SPY; the current session is dropped. Episode returns use the unadjusted close for HYG and LQD (so distributions are excluded and the price move is the stress reading) and the adjusted close for SPY (total return). Each is the close on the trough date divided by the close on the peak date, minus one; where a date is not a session, the nearest prior session is used.

Balance-sheet changes: 2020-02-26 to 2020-06-10, 7.17 - 4.16 = +$3.01 trillion in 15 weeks. 2022-04-13 to 2026-09-23, 6.75 - 8.97 = -$2.22 trillion over about 232 weeks, roughly $9.6 billion a week on average. RRP drain: 2,553.7 (2022-12-30) to 11.4 (2026-09-29), a fall of $2.54 trillion, which is larger than the balance-sheet reduction over the same period (WALCL went from $8.55 trillion on 2022-12-28 to $6.75 trillion, a fall of $1.80 trillion). Because the RRP is a liability of the Fed, the arithmetic says the other liabilities, chiefly bank reserves and the Treasury's account, rose by roughly the $0.74 trillion difference: the drain came out of the RRP, not out of reserves.

Stress episodes (peak date to trough date: HYG price, LQD price, SPY total return):

2008-06-30 to 2009-03-09: HYG -34.4%, LQD -10.7%, SPY -46.0%. Ratio HYG/LQD 3.2: credit event. 2011-07-22 to 2011-10-03: HYG -11.5%, LQD +0.5%, SPY -17.9%: credit stress, no rates component. 2015-06-30 to 2016-02-11: HYG -14.9%, LQD -1.4%, SPY -10.2%: credit (energy) stress exceeding equity stress. 2020-02-19 to 2020-03-23: HYG -22.2%, LQD -12.5%, SPY -33.7%: credit and funding event, resolved by the balance sheet. 2022-01-03 to 2022-10-12: HYG -17.7%, LQD -22.8%, SPY -24.5%: rates event. 2025-02-19 to 2025-04-08: HYG -5.0%, LQD -2.1%, SPY -18.8%; the FRED spread on 2025-04-08 was 4.57 points, having peaked at 4.61 on 2025-04-07 from 2.59 on 2025-01-22: equity shock.

Spread readings in the window FRED served: 4.42 on 2023-10-31, 3.93 on 2024-08-05 (the yen carry unwind), 4.61 on 2025-04-07, 3.08 on 2026-09-29. Calendar-year price-plus-distribution returns for context: HYG -17.6% and LQD +2.4% in 2008; HYG +28.5% and LQD +8.4% in 2009; HYG -11.0% and LQD -17.9% in 2022.

## Table

| Episode | Window | HYG price | LQD price | SPY total return | Reading |
|---|---|---|---|---|---|
| Financial crisis | 2008-06-30 to 2009-03-09 | -34.4% | -10.7% | -46.0% | Credit event |
| Euro / debt-ceiling | 2011-07-22 to 2011-10-03 | -11.5% | +0.5% | -17.9% | Credit stress |
| Energy / China | 2015-06-30 to 2016-02-11 | -14.9% | -1.4% | -10.2% | Credit stress > equity |
| Pandemic | 2020-02-19 to 2020-03-23 | -22.2% | -12.5% | -33.7% | Credit and funding event |
| Tightening | 2022-01-03 to 2022-10-12 | -17.7% | -22.8% | -24.5% | Rates event |
| Tariff shock | 2025-02-19 to 2025-04-08 | -5.0% | -2.1% | -18.8% | Equity shock (OAS peak 4.61) |

Balance sheet at the same moments (WALCL, nearest Wednesday): $0.91T (2008-09-03) rising to $2.24T (2008-12-31); $4.16T (2020-02-26) rising to $7.17T (2020-06-10); $8.97T peak (2022-04-13) falling through the 2022 window; $6.54T low (2025-12-03).

The one row where the tool disagrees with the headline is 2022: the worst year for a diversified bond portfolio in the sample shows up as a moderate credit drawdown and a severe rates drawdown. If you had been reading only the high-yield spread that year you would have concluded the environment was manageable, and for credit it was. For duration it was not.

## Sources

- Federal Reserve Bank of St. Louis, FRED: https://fred.stlouisfed.org/series/WALCL, https://fred.stlouisfed.org/series/RRPONTSYD, https://fred.stlouisfed.org/series/BAMLH0A0HYM2
- Board of Governors of the Federal Reserve System, "Credit and Liquidity Programs and the Balance Sheet": https://www.federalreserve.gov/monetarypolicy/bst.htm
- Federal Reserve Bank of New York, "Reverse Repo Operations": https://www.newyorkfed.org/markets/desk-operations/reverse-repo
- Gilchrist, S. and Zakrajšek, E. (2012), "Credit Spreads and Business Cycle Fluctuations", American Economic Review 102(4), https://doi.org/10.1257/aer.102.4.1692
