---
{
  "title": "Post-Earnings-Announcement Drift",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "What did Bernard and Thomas (1989) document?", "opts": ["Stocks fully adjust to earnings news within one day", "Stocks with the most positive earnings surprises keep drifting up, and the most negative keep drifting down, for roughly 60 trading days after the announcement", "Earnings surprises are random", "Only large firms drift"], "correct": 1, "explain": "The drift is the continued movement in the direction of the surprise after the announcement, about 2% per side over 60 days in their sample, and stronger in small firms."},
    {"q": "Standardised unexpected earnings (SUE) divides the surprise by:", "opts": ["The share price", "The standard deviation of past surprises for that firm", "The number of analysts", "Revenue"], "correct": 1, "explain": "SUE scales the surprise so that firms with historically noisy earnings are not counted as big surprises every quarter; a 5-cent miss is large for a utility and noise for a biotech."},
    {"q": "Chordia, Goyal, Sadka, Sadka and Shivakumar (2009) found the drift strategy's monthly return was roughly:", "opts": ["The same in liquid and illiquid stocks", "2.43% in the most illiquid stocks and 0.04% in the most liquid", "Higher in the most liquid stocks", "Negative everywhere"], "correct": 1, "explain": "The drift is concentrated where trading is expensive. In the most liquid names, where a retail trader can actually execute, there is almost nothing left, and in the illiquid names the costs of getting in and out consume most of it."},
    {"q": "NVIDIA reported Q4 FY2026 revenue of $68.1 billion against its own guidance of $65.0 billion, and the stock fell 5.46% the next day. Which is the correct reading?", "opts": ["The report was a miss", "The report beat the company's guidance, but the price reaction depends on expectations that were higher than the guidance", "The drift will be negative because the reaction was negative", "Beats always rally"], "correct": 1, "explain": "The surprise against guidance was +4.8%, a beat. The reaction is a separate object: it reflects the gap between the print and whatever the marginal buyer had already assumed, which for NVDA was above the official range."},
    {"q": "Which of these is a fair statement about the drift for a retail trader in large, liquid names?", "opts": ["It is a reliable 4% per quarter", "It has historically been small in liquid stocks and is easily consumed by spreads and commissions, so it should be treated as a tilt, not a trade", "It only works with options", "It was disproved in 1990"], "correct": 1, "explain": "The academic magnitude is real but modest, concentrated in small illiquid stocks, and has shrunk since publication. In the names you can trade cheaply, the after-cost residual is close to zero."}
  ],
  "task": "For the last two reports of one name you follow, compute the surprise against the company's own guidance midpoint, the one-day reaction, and the 20-day return minus SPY's 20-day return."
}
---

## The anomaly that would not go away

In 1968 Ball and Brown showed that stock prices continue to move in the direction of an earnings surprise for weeks after the announcement. If markets absorbed news instantly, that would not happen: the price should jump once and then wander. Bernard and Thomas (1989) took the finding apart in detail. They sorted firms each quarter by the size of the earnings surprise, went long the top decile and short the bottom, and measured returns over the 60 trading days after the announcement. The good-news firms kept rising, roughly 2% over the window; the bad-news firms kept falling by a similar amount; and the effect was largest in small firms. They called it **post-earnings-announcement drift**, and asked in their title whether it was a delayed price response or a risk premium. Their evidence favoured delayed response: the market appeared to under-react to the information in the surprise, particularly to the fact that earnings surprises tend to repeat for a few quarters.

The finding is one of the most replicated in accounting research. It is also one of the most instructive for a trader, because what has happened to it since 1989 is a lesson in what happens to any published edge.

## Measuring the surprise

The academic measure is **standardised unexpected earnings**, SUE:

SUE = (actual EPS − expected EPS) / σ of past surprises

where expected EPS is either a seasonal random walk (this quarter last year, sometimes with a drift term) or the analyst consensus, and σ is the standard deviation of the firm's own past surprises. Scaling by σ is what makes the measure comparable across firms. A five-cent beat is enormous for a utility that never misses by more than a penny and meaningless for a company whose earnings swing by dollars.

For a retail trader without a consensus feed, there is a simpler and fully documented alternative: the surprise against the company's **own guidance**. Companies that guide publish a revenue range in the prior quarter's press release, and the actual revenue is in this quarter's. Both numbers are on the investor relations page and in the 8-K, so the surprise is a matter of record. It is not the same as consensus, and for a name like NVIDIA the market's real expectation sits above the official range, but it is reproducible and it is the number you can verify.

## Worked example

Take NVIDIA's three most recent reports where the prior guidance and the actual are both on record, using the company's press releases and the Yahoo Finance daily bars (496 rows, 2024-10-01 to 2026-09-23). SPY closes come from the same API.

**Report 1: February 25, 2026 (Q4 FY2026).** Guidance given November 19, 2025: revenue "$65.0 billion, plus or minus 2%." Actual: $68.1 billion. Surprise against the midpoint: 68.1 / 65.0 − 1 = **+4.8%**. Reaction, close before to close after: 195.56 → 184.89 = **−5.46%**. A beat that fell.

Drift after the reaction day (all returns from the February 26 close):

- +1 trading day (Feb 27): NVDA −4.16%, SPY −0.48%
- +5 trading days (Mar 5): NVDA −0.84%, SPY −1.16%
- +20 trading days (Mar 26): NVDA −7.38%, SPY −6.41%
- +60 trading days (May 22): NVDA +16.46%, SPY +8.17%

Abnormal return over 60 days, NVDA minus SPY: 16.46 − 8.17 = **+8.29%**. Positive, in the direction of the surprise and against the direction of the reaction.

**Report 2: May 20, 2026 (Q1 FY2027).** Guidance given February 25, 2026: "$78.0 billion, plus or minus 2%." Actual: $81.6 billion. Surprise: 81.6 / 78.0 − 1 = **+4.6%**. Reaction: 223.47 → 219.51 = **−1.77%**.

- +20 trading days (Jun 22): NVDA −4.95%, SPY +0.22%; abnormal **−5.17%**
- +60 trading days (Aug 18): NVDA +0.10%, SPY +3.33%; abnormal **−3.23%**

Negative drift after a positive surprise.

**Report 3: August 26, 2026 (Q2 FY2027).** Guidance given May 20, 2026: "$91.0 billion, plus or minus 2%." Actual: $96.2 billion. Surprise: 96.2 / 91.0 − 1 = **+5.7%**. Reaction: 209.66 → 227.98 = **+8.74%**.

- +1 trading day (Aug 28): NVDA −4.57%, SPY −0.23%; abnormal −4.34%
- +5 trading days (Sep 3): NVDA +0.21%, SPY +0.27%; abnormal −0.06%

The 60-day window had not closed when this lesson was written.

Three positive surprises of similar size, three different reactions (−5.5%, −1.8%, +8.7%), and two completed 60-day windows with abnormal drift of +8.3% and −3.2%. The average of two numbers of opposite sign tells you nothing, and that is the point. Bernard and Thomas's 2% per side is a *cross-sectional average over thousands of firm-quarters*. In a single name it is invisible under the noise of everything else that happens in 60 days. You will not find the drift by watching one stock; you find it, if at all, by holding a portfolio of the top-decile surprises against a portfolio of the bottom decile and waiting years.

## Table

| Report date | Guidance midpoint | Actual revenue | Surprise | Reaction (close to close) | 60-day abnormal (NVDA − SPY) |
|---|---|---|---|---|---|
| 2026-02-25 | $65.0bn | $68.1bn | +4.8% | −5.46% | +8.29% |
| 2026-05-20 | $78.0bn | $81.6bn | +4.6% | −1.77% | −3.23% |
| 2026-08-26 | $91.0bn | $96.2bn | +5.7% | +8.74% | window open |

## What remains after costs

The question for a trader is not whether the drift existed in a 1974–1986 sample but what is left of it now, in the stocks you can trade, after you pay to trade them. Chordia, Goyal, Sadka, Sadka and Shivakumar (2009) answered it directly. They sorted the drift strategy by liquidity and found the value-weighted long-short return was 2.43% per month in the most illiquid stocks and 0.04% per month in the most liquid. Then they estimated the transaction costs of actually running the strategy in the illiquid names and found the costs consumed most of the return. The drift lives precisely where it cannot be harvested cheaply; where it can be harvested cheaply, there is almost nothing to harvest.

Three further facts from the review literature (Fink 2021 surveys it) sharpen this:

- The drift has **declined** since the 1990s, consistent with capital chasing a published anomaly.
- A large part of the measured drift is realised in the first few days and around the *next* announcement, when the surprise repeats, rather than as a smooth glide.
- Much of what looks like drift in a simple sort is exposure to size, value and momentum factors that a retail trader could obtain more cheaply another way.

For a trader in large, liquid names the practical conclusion is that the drift is a **tilt, not a trade**. If you were already inclined to hold a stock that just beat, the evidence says the following weeks are slightly more likely to favour you than not, and you should not rush to fade a beat that gapped up. If you were not already inclined to hold it, the after-cost expected value of buying it for the drift alone is indistinguishable from zero in the names you can execute in.

## How the drift interacts with the reaction

The February 2026 example deserves one more look, because it is the common case. The company beat its guidance by 4.8% and the stock fell 5.5%. The reaction is not the surprise. The reaction measures the gap between the print and whatever the marginal holder had already priced, and for a stock that had risen into the report, the marginal holder had priced more than the official range. The drift literature is about the *surprise*; a trader who reads "fell 5.5%" as "bad news, expect negative drift" is mixing the two objects. In that instance the subsequent 60-day abnormal return was +8.3%, in the direction of the surprise.

This is why lesson 11 asks you to log the surprise, the reaction and the drift as three separate columns. Only with all three can you see which of them your process is actually responding to.

## Sources

- Bernard, V. L., and Thomas, J. K. (1989). "Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium?" Journal of Accounting Research 27 (Supplement), 1–36. https://doi.org/10.2307/2491062
- Chordia, T., Goyal, A., Sadka, G., Sadka, R., and Shivakumar, L. (2009). "Liquidity and the Post-Earnings-Announcement Drift." Financial Analysts Journal 65(4), 18–32. https://doi.org/10.2469/faj.v65.n4.3
- Fink, J. (2021). "A review of the Post-Earnings-Announcement Drift." Journal of Behavioral and Experimental Finance 29. https://www.sciencedirect.com/science/article/pii/S2214635020303750
- NVIDIA press releases with guidance and actuals: Q3 FY2026 (Nov 19, 2025) https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2026; Q1 FY2027 (May 20, 2026) https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027; Q2 FY2027 (Aug 26, 2026) https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
