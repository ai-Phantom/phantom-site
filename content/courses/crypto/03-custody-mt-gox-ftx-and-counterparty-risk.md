---
{
  "title": "Custody: Exchange vs Self-Custody, and What Mt. Gox and FTX Teach",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "In John J. Ray III's December 2022 testimony to the House Financial Services Committee, which of these was listed as a cause of FTX's collapse?", "opts": ["A single rogue trader", "Commingling of FTX.com customer assets with the Alameda trading platform", "A software bug in the matching engine", "A 51% attack on Bitcoin"], "correct": 1, "explain": "Ray's written testimony lists commingling of customer assets with Alameda, Alameda using client funds for margin trading, about $5 billion spent on investments and over $1 billion of loans to insiders."},
    {"q": "An FTX customer held 1 BTC on 2022-11-11, the petition date, when Yahoo's BTC-USD close was $17,034. Under a plan paying 118% of petition-date value in dollars, roughly what did the customer receive?", "opts": ["1 BTC", "About $20,100", "About $84,000", "Nothing"], "correct": 1, "explain": "1.18 times 17,034 is about $20,100 in cash. With BTC at $84,242 on 2026-09-24, the coin itself would be worth four times more. Bankruptcy claims are fixed in dollars at the petition date."},
    {"q": "Why does the Mt. Gox trustee's website still matter in 2026?", "opts": ["Mt. Gox reopened as an exchange", "Creditors of a 2014 failure were still receiving repayments, with deadlines extended to October 2026", "It publishes BTC prices", "It is the official Bitcoin website"], "correct": 1, "explain": "The Tokyo civil rehabilitation proceeding has run for more than a decade; the trustee's notice extended repayment deadlines to 2026-10-31."},
    {"q": "What does Coinbase's 10-K say could happen to customer crypto held in custody if Coinbase entered bankruptcy?", "opts": ["It is FDIC insured", "It could be treated as estate property and customers as general unsecured creditors", "It is automatically returned within 24 hours", "It is held by the SEC"], "correct": 1, "explain": "The filing says custodially held assets may be considered property of a bankruptcy estate and customers could be general unsecured creditors; it is a disclosure, not a prediction, and the legal treatment remains untested for that firm."},
    {"q": "The most reliable protection against a venue failure is", "opts": ["Choosing the largest venue", "Keeping only working capital on any venue and holding the rest in keys you control", "Diversifying across three venues with the same business model", "Buying the venue's token"], "correct": 1, "explain": "Diversifying across custodians reduces the size of any one loss; self-custody removes the counterparty entirely. Size on-venue balances as unsecured credit, because that is what they are."}
  ],
  "task": "List every venue balance you hold, label each as working capital or idle, and withdraw the idle balances to a wallet you control before the next lesson."
}
---

## Counterparty risk without a safety net

A US brokerage customer is protected by segregation rules, SIPC coverage up to $500,000, and a regulator that examines the books. None of that exists by default on a crypto exchange. Whatever protections a venue offers are contractual, vary by jurisdiction, and have been tested in court only a handful of times. Two of those tests, Mt. Gox and FTX, are the whole syllabus for this lesson, because between them they cover both ways an exchange can fail: losing the coins and misusing the coins.

## Mt. Gox: the coins were gone

Mt. Gox, based in Tokyo, was at one point the largest bitcoin exchange in the world. In February 2014 it halted withdrawals, then filed for bankruptcy protection in the Tokyo District Court, stating that roughly 850,000 BTC belonging to customers and the company were missing; about 200,000 were later found in an old wallet. The proceeding was converted to civil rehabilitation in 2018, which allowed creditors to be repaid in bitcoin rather than in the yen value of their 2014 claims.

The trustee's website, mtgox.com, still carries the creditor filing system and notices. Its current notice states that the deadlines for the Base Repayment, Early Lump-Sum Repayment and Intermediate Repayment were moved from 2025-10-31 to 2026-10-31. That is the timeline: a customer who lost access in February 2014 has been waiting more than twelve years, and some are still waiting.

Two things made Mt. Gox survivable for creditors at all. The claims were converted to a coin-denominated repayment, so creditors captured the price rise from about $500 in 2014; and there were recovered coins to distribute. Neither was guaranteed. The default outcome in an insolvency is a fixed claim in fiat at the petition date, which is what FTX customers got.

## FTX: the coins were used

FTX Trading Ltd. and about 130 affiliates filed for Chapter 11 in the District of Delaware on 2022-11-11 (case 22-11068). John J. Ray III, who had run the Enron liquidation, was appointed CEO. His written testimony to the House Financial Services Committee on 2022-12-13 lists what he found, and it is worth reading in full because it is a primary document, not a news account. Among the causes he identifies:

- Customer assets from FTX.com were commingled with assets of Alameda, the affiliated trading firm.
- Alameda used client funds for margin trading, exposing customers to losses.
- Roughly $5 billion was spent on businesses and investments.
- Loans and other payments to insiders exceeded $1 billion.
- There were no adequate controls: he describes a complete failure of corporate controls at every level of the organisation.

The founder was convicted on seven counts and, per the Department of Justice's press release, sentenced on 2024-03-28 to 25 years in prison. The bankruptcy plan became effective in early 2025 and repays customer claims in cash based on the dollar value of their holdings on the petition date, with recoveries stated in the plan documents on the claims agent's site at more than 100 cents on that dollar. The press reported this as customers being made whole. The worked example shows why a customer who held bitcoin would not describe it that way.

## Worked example

Take a customer who held exactly 1 BTC on FTX.com when the petition was filed on 2022-11-11. Yahoo Finance's BTC-USD daily bar for that date closed at $17,034 (the bar's low was $16,543 and the high $17,651; the day before, 2022-11-10, had ranged from $15,834 to $18,054, and 2022-11-09 had printed the cycle's low region at $15,683).

Step 1: the claim. Bankruptcy fixes the claim in dollars at the petition date. Using the close: claim = 1 × 17,034 = $17,034.

Step 2: the recovery. Assume the plan's stated recovery for that class is 118% of the petition-date claim: 17,034 × 1.18 = $20,100. Paid in dollars, over the distribution schedule, more than two years later.

Step 3: the opportunity cost. The Yahoo close on 2026-09-24 was $84,242.04. The coin the customer thought they owned is now worth $84,242. Recovery as a share of the coin's current value: 20,100 ÷ 84,242 = 23.9%.

Step 4: compare to self-custody. A holder of 1 BTC in their own wallet on 2022-11-11 has 1 BTC today, worth $84,242, minus nothing. The difference, $64,142, is the cost of counterparty risk on this one occasion, and it is a cost that shows up even though the plan paid more than 100% of the legal claim.

Step 5: compare to Mt. Gox. A Mt. Gox creditor's claim was converted to a coin-denominated repayment. A creditor allocated 1 BTC of repayment receives an asset worth $84,242 today, not the roughly $500 the coin was worth at the 2014 filing. Same asset, two insolvencies, opposite treatment, and the customer had no say in which one they got.

The arithmetic generalises. Any time a venue fails in a rising market, a fiat-denominated claim converts your upside into the venue's estate. Any time it fails in a falling market, the claim is worth more than the coins, but the venue is also more likely to be short of assets to pay it.

## What the failures have in common

Neither venue told customers anything was wrong until withdrawals stopped. Both had been operating normally, processing withdrawals in full, the week before. Both were, at the time, among the largest and most trusted venues in the industry. Both failures were discovered by customers only when the exchange could not meet a withdrawal wave.

That is the operational lesson: you cannot detect this risk from the outside in time to act on it. Proof-of-reserves publications help only if they include liabilities, and most do not. The mitigation has to be structural, decided before anything goes wrong.

## Table

| | Mt. Gox (Tokyo, 2014) | FTX (Delaware, 2022) |
|---|---|---|
| Failure mode | Coins missing (about 850,000 BTC announced; about 200,000 recovered) | Customer assets commingled and lent to affiliate; spent on investments and insider loans |
| Warning to customers | Withdrawal delays, then halt | Withdrawal surge, then halt within days |
| Proceeding | Bankruptcy, converted to civil rehabilitation 2018 | Chapter 11, case 22-11068, filed 2022-11-11 |
| Claim denomination | Converted to BTC/BCH repayments | Dollars at petition-date value |
| Time to distribution | More than ten years; deadlines now 2026-10-31 | About two years to plan effectiveness |
| What a 1 BTC holder got | An allocation in coins, capturing the price rise | About $20,100 cash against a coin now worth $84,242 |
| Regulatory outcome | Japan introduced exchange registration under the Payment Services Act | Founder sentenced to 25 years (DOJ, 2024-03-28) |

## A custody policy you can actually follow

Write three numbers down. The first is working capital: the amount you need on venues to run your strategy for a week. The second is the maximum share of your crypto net worth you will hold on any single venue. The third is the maximum share you will hold on all venues combined. Everything above those limits lives in keys you control, and lesson 12 turns this into a plan that survives a venue failure with the rest of your risk budget.

Treat every on-venue balance, when you size it, as an unsecured loan to a private company whose books you cannot see. Coinbase says as much in its own 10-K. The venues that failed did not.

## Sources

- John J. Ray III, written testimony before the U.S. House Committee on Financial Services, 2022-12-13: https://docs.house.gov/meetings/BA/BA00/20221213/115246/HHRG-117-BA00-Wstate-RayJ-20221213.pdf
- U.S. Department of Justice, S.D.N.Y., "Samuel Bankman-Fried Sentenced To 25 Years In Prison", 2024-03-28: https://www.justice.gov/usao-sdny/pr/samuel-bankman-fried-sentenced-25-years-prison
- MtGox Co., Ltd. Rehabilitation Trustee, creditor notices and repayment deadline changes: https://www.mtgox.com/
- Coinbase Global, Inc., Form 10-K for fiscal 2022, risk factors on custodial assets: https://www.sec.gov/Archives/edgar/data/1679788/000167978823000031/coin-20221231.htm
