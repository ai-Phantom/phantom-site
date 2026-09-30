---
{
  "title": "Liquidity, Halts and the First 15 Minutes",
  "duration": "15 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Under the Limit Up-Limit Down plan, what is the price band for a Tier 1 stock (S&P 500 or Russell 1000 member) trading above $3.00 during most of the regular session?", "opts": ["1%", "5%", "10%", "20%"], "correct": 1, "explain": "Tier 1 securities above $3.00 carry 5% bands around a reference price that is the average of trades over the prior five minutes. Tier 2 securities carry 10%, and the bands are doubled in the last 25 minutes of the session."},
    {"q": "How does a LULD trading pause get triggered?", "opts": ["Any trade outside the band", "The stock stays in a Limit State, unable to trade past the band, for 15 seconds, after which the listing exchange declares a five-minute pause", "The SEC calls the exchange", "Volume exceeds a threshold"], "correct": 1, "explain": "Quotes are prevented from crossing the band; if the market sits at the band for 15 seconds without trading through it, the primary exchange pauses trading for five minutes, extendable by another five."},
    {"q": "NVDA opened at 195.95 on November 20, 2025, up 5.06%, printed a high of 196.00 and closed at 180.64. What does this show about the open after earnings?", "opts": ["The open is always the low", "The open can be the extreme of the day; the whole 8.2% fall from open to low happened in the regular session, after the gap had already priced the news", "The stock was halted", "The gap was reversed in pre-market"], "correct": 1, "explain": "The opening print was within five cents of the day's high. Anyone who bought the open 'because it beat' rode the full reversal. The gap is the market's first guess and the session is the market's revision."},
    {"q": "On August 27, 2026, NVDA's first 15 minutes carried 59.9 million shares against 263.7 million for the session. What share of the day's volume was that?", "opts": ["About 5%", "About 12%", "About 23%", "About 50%"], "correct": 2, "explain": "59.9 / 263.7 = 0.227. Roughly a quarter of the day's volume traded in the first 3.8% of the session, which is why the first 15 minutes after an earnings gap have the widest range and, usually, the widest spreads."},
    {"q": "Why does the reference price mechanism mean a stock can fall 8% over a session without a LULD pause?", "opts": ["Because the bands do not apply to large caps", "Because the reference price is recomputed every five minutes from recent trades, so a steady decline moves the band down with the price and only a sudden 5% drop within a few minutes hits it", "Because pauses only happen in the afternoon", "Because NVDA is exempt"], "correct": 1, "explain": "LULD stops sudden dislocations, not trends. A stock that falls 1% every ten minutes stays inside a band that follows it down."}
  ],
  "task": "For the next post-earnings open in a name you follow, record the first 5-minute bar's open, high, low, close and volume, the 15-minute range, and the bid-ask spread at 9:30:30 and at 9:45, and compare the spread to the prior day's."
}
---

## Price is not the only thing that changes at an event

Every worked example so far has quoted a close, an open, a high and a low as though you could have traded at them. Around an event you often cannot, or not at a size and a spread that would make the trade worth doing. The order book empties before the print and refills only gradually afterward. Spreads that are a cent wide at noon are a quarter wide at 9:30:05 after an earnings gap. Market-wide circuit breakers and single-stock price bands can stop trading entirely for five minutes at exactly the moment you most want out. This lesson is about the plumbing: what the Limit Up-Limit Down mechanism does, what the first 15 minutes after a gap look like in volume and range, and what the extended-hours session is and is not.

## Limit Up-Limit Down

The Limit Up-Limit Down plan (LULD) is the single-stock volatility mechanism approved by the SEC and operated jointly by the exchanges and FINRA. It works with **price bands** around a **reference price**:

- The reference price is the arithmetic mean of eligible trades over the preceding five minutes, updated only when a new calculation would differ from the current reference by at least 1%.
- **Tier 1** securities (S&P 500 and Russell 1000 constituents, plus selected ETPs) trading above $3.00 have bands of **5%** above and below the reference. Between $0.75 and $3.00 the band is 20%; below $0.75 it is the lesser of $0.15 or 75%.
- **Tier 2** securities (everything else on the national market system) above $3.00 have **10%** bands; below $3.00, 20%.
- In the **last 25 minutes** of the regular session, from 3:35 to 4:00 p.m., bands are doubled for Tier 1 securities and for Tier 2 securities below $3.00.

Quotes are prevented from crossing the band. If the best bid reaches the upper band, or the best offer reaches the lower band, the stock enters a **Limit State**. If it does not trade back inside within **15 seconds**, the primary listing exchange declares a **Trading Pause** of five minutes, which can be extended by another five if the reopening auction cannot find a price inside the bands.

Two consequences follow for an event trader. First, the mechanism is designed to stop *sudden* dislocations, not trends. Because the reference price is a trailing five-minute mean, a stock that falls steadily carries its band down with it. Second, a pause does not protect you. When trading resumes it reopens by auction, at whatever price clears the accumulated orders, which can be well past the band that triggered the pause. A stop order that was resting during the pause fills at the reopening price.

NVDA is Tier 1. At a reference price near 210, the band is ±10.50. On the morning of August 27, 2026 the stock opened 6.3% above the prior close, but the reference price for the opening period is derived from the opening trades themselves, so the gap does not trigger a pause; only a sudden 5% move *from* the opening level within minutes would.

## The first 15 minutes

Volume and range concentrate at the open after an overnight event because that is when the largest number of participants can trade at once. The market-on-open auction sets the first price; the following minutes are the market working through everyone who wanted to act at 4:20 p.m. the night before but could not.

## Worked example

NVIDIA's August 26, 2026 report, from Yahoo Finance 5-minute bars with extended hours included (384 bars across August 26 and 27) and the daily series.

**After hours, August 26.** Regular close 209.66. The report crossed shortly after 4:00 p.m.

- 4:15 p.m. bar: high 211.20.
- 4:20 p.m. bar: open 210.81, **low 203.50**, close 207.64. Low is 203.50 / 209.66 − 1 = **−2.94%** from the close.
- 4:30 p.m. bar: low 205.26. 4:45: 209.59.
- 5:00 p.m. (call begins): 214.86. 5:05: 219.67.
- 5:20 p.m. bar: **high 226.25**, close 218.90. High is 226.25 / 209.66 − 1 = **+7.91%**.
- 7:45 p.m.: 218.73. Extended session drifted between 217 and 219 for the last two hours.

Swing from the 4:20 low to the 5:20 high: 226.25 / 203.50 − 1 = **+11.18%** inside one hour, with the sign of the reaction reversing once between the two. The feed reports no volume for these bars; the after-hours book in a name like NVDA is a small fraction of the regular session and the spreads during that hour were multiples of the day's.

**The open, August 27.**

- 9:25 pre-market bar: close 222.86 (the opening print was 222.86, matching this).
- 9:30 bar: open 222.59, high 225.50, low 221.22, close 222.30, volume **39.1 million** shares in five minutes.
- 9:35 bar: low 220.90, close 223.19, 9.7 million. 9:40: high 225.83, close 224.94, 11.1 million.
- First 15 minutes: high 225.83, low **220.90**, range 4.93 = **2.21%** of the open; volume **59.9 million**.
- Full session: high 230.47, low 220.90 (the low of the day was in the first ten minutes), volume 263.7 million. First-15-minute share of volume: 59.9 / 263.7 = **22.7%**.

**A different open, November 20, 2025.** Prior close 186.52. Open **195.95** (+5.06%). High **196.00**, five cents above the open. Low 179.85. Close **180.64**, which is −3.15% on the day and **−7.81% from the open**. Volume 343.5 million against 247.2 million the prior day. Here the opening print was, to within a nickel, the high of the day, and the whole reversal happened inside the regular session. No pause: an 8.2% fall spread over six and a half hours never breached a 5% band around a five-minute trailing reference.

## Table

| Window | NVDA price path | Move | Notes |
|---|---|---|---|
| Aug 26, 4:20 p.m. bar | low 203.50 | −2.94% vs close | first after-hours reaction, thin book, no volume reported |
| Aug 26, 5:20 p.m. bar | high 226.25 | +7.91% vs close | +11.18% from the 4:20 low within an hour |
| Aug 27, 9:30 open | 222.86 | +6.30% gap | 39.1m shares in the first 5-min bar |
| Aug 27, first 15 min | 220.90–225.83 | 2.21% range | 59.9m shares, 22.7% of the day |
| Aug 27, session | close 227.98 | +8.74% on day | low of day was 220.90 at 9:35 |
| Nov 20, 2025, open | 195.95 | +5.06% gap | high of day 196.00, within 5 cents of the open |
| Nov 20, 2025, session | close 180.64 | −7.81% from open | no LULD pause; decline was gradual |

## What the plumbing means for each kind of trader

**If you hold options through the print,** you cannot do anything until 9:30 in almost every retail account, and by then the stock has moved, the implied vol has crushed, and the option's bid-ask has widened to reflect the uncertainty of the first minutes. The first useful quote you will see is usually five to fifteen minutes into the session. A market order at 9:30:01 in a post-earnings option is a donation.

**If you hold stock through the print with a stop,** the stop is a market order that triggers at the first print past your level. On November 20, 2025 a stop at 190 on a long position from the prior week would have triggered somewhere below 190 in the late-morning decline and filled at the next print; on August 27, 2026 a stop at 205 on a short position would have triggered at the 222.86 open and filled there or worse, 8% past the stop. Lesson 10 works the sizing arithmetic.

**If you want to trade the reaction,** the first 15 minutes are where the range is, where the volume is, and where the spreads are widest. The November 2025 case shows the open can be the extreme of the day; the August 2026 case shows the low of the day can be printed at 9:35 and the high at midday. Neither is a rule. What both show is that the opening print is the market's first guess after a night of thin trading, and the session revises it. A trader who has decided in advance to do nothing until 9:45, and to use limit orders after that, gives up the first move and avoids the worst spreads. Whether that is a good trade depends on your journal, not on this lesson.

**During a pause,** do nothing. The reopening auction will set a price; entering a market order into a pause guarantees you the worst side of it.

## Sources

- Limit Up-Limit Down Plan, official plan site with the current band table and pause rules: https://www.luldplan.com/
- Nasdaq Trader, current and historical trading halts: https://www.nasdaqtrader.com/Trader.aspx?id=TradeHalts
- FINRA, order types (market, limit, stop): https://www.finra.org/investors/investing/investment-products/stocks/order-types
- NVIDIA, "NVIDIA Announces Financial Results for Second Quarter Fiscal 2027," August 26, 2026: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
