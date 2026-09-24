---
{
  "title": "The 0DTE Version of the Opening Range and Its Unique Risks",
  "duration": "17 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "On 2026-09-16 the equity opening-range long hit its target at 761.06 and netted +$1.15 per share. A 760 call bought at the same moment and held to the close was worth:", "opts": ["$1.06", "$1.67", "$0.70", "$0.00"], "correct": 3, "explain": "SPY closed at 754.07, below the 760 strike, so the call expired worthless regardless of what it was worth at 11:45."},
    {"q": "In the 60-session sample, how many sessions closed within 0.25% of the opening-range entry price?", "opts": ["5 of 60", "33 of 60", "47 of 60", "60 of 60"], "correct": 1, "explain": "33 sessions ended within 0.25% (about $1.90) of the entry, and 47 within 0.5%. A 0DTE option that needs a large move by 16:00 usually does not get one."},
    {"q": "Per Cboe's 0DTE product page, roughly what share of SPX options volume trades in zero-days-to-expiry contracts?", "opts": ["9%", "25%", "59%", "90%"], "correct": 2, "explain": "Cboe reports 59% of SPX volume and 48% of XSP volume traded 0DTE on the page cited in this lesson."},
    {"q": "Why does the equity rule's 'exit at 15:55 if nothing hit' have no equivalent for a 0DTE option?", "opts": ["Options cannot be sold intraday", "Because at 16:00 the option settles to intrinsic value; the time exit is forced and the residual premium is gone", "Brokers prohibit it", "The option keeps time value overnight"], "correct": 1, "explain": "Expiry is the ultimate time stop. Whatever extrinsic value was paid is exactly zero by the close."},
    {"q": "Which of these is a risk the 0DTE version has that the equity version does not?", "opts": ["The stop can gap", "The position can lose most of its value while the underlying moves in the intended direction slowly, through time decay", "Costs exist", "Volume is lower at midday"], "correct": 1, "explain": "A near-the-money 0DTE option loses extrinsic value continuously; a slow drift in your favour can still lose money."}
  ],
  "task": "Read the OCC's options disclosure document section on expiration and exercise, and write in your own words what happens to a SPY option you hold at 16:00 on its expiry day."
}
---

## What 0DTE means

A zero-days-to-expiry option is one that expires today. SPX, the cash-settled index option, has had daily expirations since 2022; SPY options expire on the same weekday schedule and are physically settled. Cboe's 0DTE product page reports that 59% of SPX volume and 48% of XSP volume trades in same-day contracts. The appeal to a day trader is leverage: a near-the-money SPY option costs a few dollars per share of exposure rather than $760, so the same dollar risk buys a much larger notional position. The cost of that leverage is that the option's price is a function of time as well as of SPY, and on the last day time is running out at its fastest.

This lesson translates the opening-range breakout of lesson 3 into a 0DTE call or put, using the same real sessions, and shows where the translation breaks. It does not use option prices: the free data source used throughout this course does not serve them without an authenticated session, and the course does not bypass that. What can be computed exactly from SPY bars is the option's intrinsic value at every 5-minute close, and in particular at 16:00, when intrinsic value is the only value there is. Anything about the premium you would have paid at 09:50 is labelled as an assumption.

## The translation

Equity rule: 15-minute range; long on the first 5-minute close above the high, short on the first close below the low; stop at the opposite edge; target 1R; exit 15:55. Its 0DTE version: on the long signal, buy the at-the-money call expiring today (the strike nearest SPY's price; SPY strikes are $1 apart near the money); on the short signal, buy the at-the-money put. Position size: risk the same dollars, so the number of contracts is (risk dollars) / (premium × 100), which typically means the whole premium is the stop.

Three things change immediately. First, the stop is no longer at a price level of SPY; it is the premium, and a premium can go to zero without SPY ever reaching the opposite edge of the range. Second, the target is no longer 1R in SPY terms, because the option's gain for a $1 move in SPY depends on its delta, roughly 0.5 at the money and rising as the option goes in the money. Third, there is no "exit at 15:55 flat" outcome. At 16:00 the option is worth exactly max(SPY − strike, 0) for a call, and all the extrinsic value you paid is gone.

## Worked example

Session: SPY, 2026-09-16, 5-minute bars, Yahoo Finance chart API.

The 15-minute range was 759.66 to 758.72. The 09:45 bar closed at 759.89, above the high. Equity entry at the 09:50 open: 759.89. Stop 758.72, R = 1.17. Target 761.06. The 11:45 bar printed a high of 761.67, through the target. Equity result: +1.17 gross, +1.15 net per share, a full win.

0DTE version: buy the 760 call at 09:50 with SPY at 759.89. Intrinsic value at entry = max(759.89 − 760, 0) = $0.00. Whatever you paid was entirely extrinsic value; call it P per share. (No sourced quote is available; a same-day at-the-money SPY option on a quiet morning has recently traded for somewhere in the region of a few tenths of a percent of the index level, but treat that as an assumption, not data.)

At 11:45, SPY's high of 761.67 puts the call $1.67 in the money. Its market value at that moment would have been the $1.67 intrinsic plus whatever extrinsic value remained with four hours to go: more than $1.67, and if P was around $2 to $3, roughly a break-even to modest gain. The equity trader had a rule that said "sell at 761.06" and did. A 0DTE trader with a rule that says "sell at the equity target" would have sold for intrinsic $1.06 plus remaining time value.

Held to the close: SPY fell from 761.67 at 11:45 to a low of 749.60 at 15:25 and closed at 754.07. Intrinsic value of the 760 call at 16:00 = max(754.07 − 760, 0) = $0.00. Loss = 100% of P, on a day when the equity trade was a clean win.

Same session, the equity trader who ignored the target and held to 15:55 would have sold at 754.07 for a loss of 5.82 per share, 4.97R. Both traders were punished for not taking the target; the option trader's punishment was total.

The distribution behind this: across the 60 sessions, SPY's close was within 0.25% of the opening-range entry price on 33 sessions and within 0.5% on 47. At a $760 index level, 0.25% is $1.90. A near-the-money option bought in the first half hour for a premium of P needs the close to be more than P beyond the strike just to return the premium. On the majority of days in this sample, the move from entry to close was smaller than what a plausible P would have been.

## Table

Three real sessions from the sample, equity rule versus the at-the-money 0DTE translation. Intrinsic values are exact from SPY bars; premium P is unsourced and left symbolic.

| Session | Signal and entry | Equity outcome (net $/share) | ATM strike | Intrinsic at entry | Best intrinsic during day (time) | Intrinsic at 16:00 | 0DTE held to close |
|---|---|---|---|---|---|---|---|
| 2026-07-01 | Long at 745.34 (10:00) | Target 748.31 hit 11:15, +2.95 | 745 call | 0.34 | 4.43 (12:20, SPY 749.43) | 0.70 | Return = 0.70 − P; loses unless P < 0.70 |
| 2026-09-16 | Long at 759.89 (09:50) | Target 761.06 hit 11:45, +1.15 | 760 call | 0.00 | 1.67 (11:45) | 0.00 | −100% of P |
| 2026-09-17 | Short at 760.22 (10:10) | Stopped 763.41 at 15:50, −3.21 | 760 put | 0.00 | 0.04 (10:05 low 759.96, before entry) | 0.00 | −100% of P |

On 2026-07-01, the day the equity trade worked best, the option's intrinsic value peaked at $4.43 two hours after the equity target and finished at $0.70. A 0DTE trader who sold at the equity target time would have collected intrinsic $3.31 plus time value; one who held for the close got $0.70. Every exit rule that the equity version treats as a mild preference becomes, in the option version, the difference between a gain and a total loss.

## The risks that are unique to the option version

Time decay against a correct call. On 2026-09-16 the direction was right for two hours and the option still could have lost money if the extrinsic value bled faster than the $1.67 intrinsic accrued. A slow drift in your favour is a loss.

Volatility crush. The premium P embeds an implied volatility. When the morning move resolves into a quiet afternoon, implied volatility falls and the option loses value even if SPY does not move against you. There is no equivalent in the equity trade.

Convexity in both directions. When the option is in the money its delta approaches 1 and it behaves like stock; when it is out of the money its delta approaches 0 and it stops responding to SPY at all. The 760 put on 2026-09-17 was effectively dead by early afternoon with SPY at 762.50: no stop was hit, there was simply nothing left to sell.

Assignment and pin risk. SPY options are physically settled. An option that finishes a cent in the money is exercised automatically under OCC rules unless you instruct otherwise, which can leave you with 100 shares of SPY per contract over the weekend, with the margin call that implies. The OCC's disclosure document is the reference; read it before the first expiry-day trade.

Spread as a share of premium. A one-cent spread on a $760 stock is 0.001%. A five-cent spread on a $2 option is 2.5%, and it is often wider. Lesson 5's cost arithmetic applies with the premium as the risk unit, and it is not favourable.

## What can be tested

The equity rule can be tested from free bar data. The option version cannot, honestly, without a record of option prices at each entry and exit, which you would have to pay for or collect yourself. If you want to trade the 0DTE version, collect that record first: for 30 sessions, note the at-the-money premium at the signal time and at the equity target time and at 15:55, and compute the P&L of each exit rule. That is the capstone with one extra column, and until it exists, the option version is an untested variant of a rule that is itself not yet distinguishable from zero.

## Sources

- Cboe Global Markets, 0DTE options product page (share of SPX and XSP volume traded 0DTE; risk statements): https://www.cboe.com/tradable-products/0dte/
- The Options Clearing Corporation, "Characteristics and Risks of Standardized Options" (the options disclosure document; expiration, exercise and assignment): https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document
- U.S. Securities and Exchange Commission, Investor.gov, "Options": https://www.investor.gov/introduction-investing/investing-basics/investment-products/options
- Yahoo Finance chart API, SPY 5-minute bars for 2026-07-01, 2026-09-16 and 2026-09-17: https://finance.yahoo.com/quote/SPY/history/
