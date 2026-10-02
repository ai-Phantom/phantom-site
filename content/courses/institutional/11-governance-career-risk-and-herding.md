---
{
  "title": "Governance, Career Risk and the Herding It Produces",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {
      "q": "Goyal and Wahal (2008) studied thousands of manager hiring and firing decisions by US plan sponsors from 1994 to 2003. Their central finding was:",
      "opts": [
        "Plan sponsors hired managers after strong three-year returns, and those managers' subsequent excess returns were about zero; fired managers on average went on to outperform their replacements",
        "Plan sponsors consistently identified skilled managers in advance",
        "Hiring decisions were random with respect to past performance",
        "Fired managers continued to underperform"
      ],
      "correct": 0,
      "explain": "The hire-after-a-good-run, fire-after-a-bad-run cycle buys high and sells low at the manager level. Round-trip costs of the switching made it worse."
    },
    {
      "q": "A value manager was hired in January 2017 after HML returned +22.80% in 2016, and fired in December 2020 after four years in which HML compounded to −62.8%. What happened to HML in the two years after the firing?",
      "opts": [
        "It fell a further 30%",
        "It was flat",
        "It returned +25.60% and +25.70%, about +58% cumulative",
        "The data do not cover 2021–2022"
      ],
      "correct": 2,
      "explain": "Fama-French HML: 2021 +25.60%, 2022 +25.70%; 1.256 x 1.257 = 1.579. The committee sold the factor at its low."
    },
    {
      "q": "Scharfstein and Stein's (1990) model of herding predicts that a manager evaluated relative to peers will:",
      "opts": [
        "Take maximum idiosyncratic risk to stand out",
        "Always index",
        "Ignore reputation entirely",
        "Mimic others' decisions even when private information says otherwise, because failing with the crowd is less damaging to reputation than failing alone"
      ],
      "correct": 3,
      "explain": "When compensation and job security depend on relative standing, an unconventional loss is career-ending while a conventional loss is forgiven; the rational response is to herd."
    },
    {
      "q": "Which governance design most directly reduces the hire-high, fire-low cycle?",
      "opts": [
        "Larger investment committees",
        "Writing the firing criteria (process breach, key-person departure, style drift, capacity) into the IPS before hiring, and excluding trailing returns from the list",
        "Quarterly manager reviews focused on the last quarter's return",
        "Rotating consultants every year"
      ],
      "correct": 1,
      "explain": "If returns cannot trigger a firing, the committee cannot sell at the low; it can only act on the things that predict future problems."
    },
    {
      "q": "Norway's fund underperformed its benchmark by 0.45 percentage points in 2024, roughly 75 billion kroner, while beating it by 0.25 points a year since 1998. What is the governance-appropriate response?",
      "opts": [
        "Fire the management team for the largest shortfall in kroner ever recorded",
        "Evaluate the shortfall against the tracking-error limit and the multi-decade record, and change nothing unless the process broke",
        "Double the tracking-error limit",
        "Switch to full indexing immediately"
      ],
      "correct": 1,
      "explain": "A one-year relative shortfall inside the mandate's risk limit is noise against a 26-year record of small outperformance. Reacting to the kroner figure would be the career-risk reflex the mandate was built to resist."
    }
  ],
  "task": "Write your own firing rule for any fund or strategy you hold: three conditions, none of which is a trailing return."
}
---

## Who decides, and what they are afraid of

Institutional money is run by committees. A board of trustees owns the IPS and the strategic allocation, an investment committee approves managers and monitors results, an internal staff or an outsourced CIO implements, and a consultant advises the committee. Each layer meets on a schedule, sees a report, and has to decide whether to act. The structure exists to make sure no single person can bet the fund. Its side effect is that every person in it is judged on a short cycle by people who see the results before they see the reasoning.

That side effect has a name in the literature: career risk. A staff member who deviates from the consensus and loses is fired; one who follows the consensus and loses is forgiven, because everyone lost. Scharfstein and Stein (1990) showed formally that a manager evaluated on relative reputation will rationally mimic others' decisions even when his own information says otherwise. The result is herding: the same managers hired at the same time, the same asset classes added after they have run, the same strategies abandoned after they have fallen.

The individual investor does not have a committee. But the mechanism, judge the decision by the last result and act on it, is the same one that drives most individual mistakes, and the institutional fixes are the same.

## The evidence on hiring and firing

Goyal and Wahal (2008) assembled thousands of decisions by US pension plans, endowments and foundations to hire and fire investment managers between 1994 and 2003. Managers were hired after strong three-year excess returns. Post-hiring excess returns were, on average, statistically indistinguishable from zero. Managers were fired for underperformance, and the fired managers on average outperformed the managers hired to replace them over the following years. Add the transition costs of switching (Lesson 8) and the round trip was a reliable way to lose money.

Jenkinson, Jones and Martinez (2016) looked at the consultants who advise these committees and found that consultants' manager recommendations, which drove large flows, did not predict subsequent outperformance. Since committees hire consultants partly to have someone to blame, this is the career-risk mechanism operating one level up.

Neither study says committees are stupid. It says that a governance structure that reviews trailing returns quarterly, in a room where nobody wants to defend a losing position, produces this pattern regardless of who is in the room.

## What good governance looks like

The institutions with long records share a few design features.

**Decision rights written down.** The board sets policy; the staff implements within ranges; nobody in between can change either. Yale's investment committee has historically met a handful of times a year and delegated implementation to the investments office under a written policy. The IPS is the boundary.

**Firing rules that exclude returns.** Managers are terminated for process breaches, key-person departures, style drift, capacity growth beyond the strategy's limits, or operational failures. A bad three years alone does not trigger review, because the evidence says it does not predict the next three.

**Evaluation horizons matched to the strategy.** A private-equity program is judged after ten years; a factor tilt after a full cycle; an index mandate on tracking error every month. The reporting cadence is chosen to match, so that the committee is not shown, and tempted to act on, numbers that are noise.

**Pre-commitment.** Rebalancing bands, spending rules and commitment pacing are set in advance so that the crisis-time decision has already been made. The 2008 endowments that suffered least were the ones whose liquidity rules were mechanical.

**Small committees, long tenure.** Turnover on a board resets institutional memory; the ten-year plan gets re-litigated every time the membership changes.

**An explicit tolerance for looking wrong.** Norway's mandate is the clearest example: the fund's management is allowed a stated expected tracking error, and the Ministry reports every year that a shortfall inside that limit is within the mandate. In 2024 the fund trailed its benchmark by 0.45 percentage points, about 75 billion kroner, the largest kroner shortfall in its history; the same report shows +0.25 points a year since 1998. A governance structure that treated 2024 as a firing offence would have been optimizing for the headline.

## Worked example

Replay the hire-fire cycle with a real factor and real dates, using Fama-French HML annual returns.

**The hire.** A committee reviews US equity managers in late 2016. A value manager whose returns track HML shows a strong recent year: HML 2016 +22.80%. Three-year record 2014–2016: 0.9815 × 0.9052 × 1.2280 = 1.091, or +9.1% cumulative relative to the market. The consultant recommends; the committee allocates $1 billion on January 1, 2017.

**The hold.** HML 2017 −13.42%, 2018 −9.63%, 2019 −10.36%, 2020 −46.94%. Cumulative: 0.8658 × 0.9037 × 0.8964 × 0.5306 = 0.372. The $1 billion of factor exposure is worth $372 million relative to the market: a $628 million relative loss over four years. Each quarterly report shows a red number; by 2019 the manager is "under review"; the 2020 collapse ends it.

**The fire.** December 2020, the mandate is terminated and moved to a growth manager (or to the index), with transition costs of, say, 30 basis points on $1 billion: $3 million.

**The aftermath.** HML 2021 +25.60%, 2022 +25.70%. Cumulative: 1.256 × 1.257 = 1.579, +57.9%. Had the committee held, the $372 million of relative value would have recovered to $372 × 1.579 = $587 million by end-2022. The firing locked in the loss at the low and missed the largest two-year value rally since the data began in the 1920s.

**The counterfactual that matters.** Suppose instead the IPS had said: "The value sleeve is sized at 10% of US equity; it is reviewed on process every year and on returns every seven years; drift beyond ±3 points is rebalanced." Then the committee would have been *buying* HML in each of 2017–2020 as the sleeve shrank below 10%, and the 2021–2022 recovery would have been earned on a larger base. Nothing about that requires forecasting when value would turn. It requires only that the return number be removed from the list of things a committee may act on within a seven-year window.

## Table

| Governance layer | Decides | Cadence | Typical failure | Design fix |
|---|---|---|---|---|
| Board of trustees | IPS, spending rule, strategic allocation | Annual review; amendment by vote | Re-litigating policy after a bad year | Cooling-off period; amendment requires an asset-liability study |
| Investment committee | Manager hiring and firing, ranges | Quarterly | Hiring on trailing 3-year returns; firing at the low (Goyal and Wahal) | Firing criteria exclude returns; horizon matched to strategy |
| Staff / OCIO | Implementation, rebalancing, tactical bets within ranges | Monthly | Herding with peers to avoid unconventional losses (Scharfstein and Stein) | Explicit tracking-error tolerance; measure TAA separately |
| Consultant | Recommendations, benchmarks, reports | Quarterly | Recommendations that do not predict (Jenkinson et al.) | Pay for process and data, not picks; track the consultant's record |
| Individual investor | All of the above, alone | Whenever the app is opened | Same reflexes, faster | Write the rules before the drawdown; review on a calendar, not on a price |

## Scaling it down

You are the whole governance stack. The useful move is to split the roles in time: the "board" writes the IPS once a year, in calm conditions; the "staff" executes the rebalancing rule on the calendar; and the "committee" reviews holdings on a fixed date with a checklist that does not include "how did it do last quarter". The firing rule for any fund you own should have three conditions and none of them a return: a change in the manager or strategy, a fee increase, a breach of the role the fund plays in your policy. If none of those has happened, the answer to "should I sell this after a bad year" is written down already, and it is no.

## Sources

- Goyal, A., and Wahal, S. (2008), "The Selection and Termination of Investment Management Firms by Plan Sponsors," *Journal of Finance* 63(4): https://doi.org/10.1111/j.1540-6261.2008.01375.x
- Jenkinson, T., Jones, H., and Martinez, J. V. (2016), "Picking Winners? Investment Consultants' Recommendations of Fund Managers," *Journal of Finance* 71(5): https://doi.org/10.1111/jofi.12289
- Scharfstein, D. S., and Stein, J. C. (1990), "Herd Behavior and Investment," *American Economic Review* 80(3): https://www.jstor.org/stable/2006678
- Kenneth R. French Data Library, Fama/French factors (annual HML): https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
