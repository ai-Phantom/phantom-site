---
{
  "title": "Expiration Mechanics: Pin Risk and Assignment",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "At expiration the OCC automatically exercises any equity option that is in the money by at least:", "opts": ["$1.00", "$0.50", "$0.05", "$0.01"], "correct": 3, "explain": "Exercise by exception applies a $0.01 threshold. A 100 call with the stock at 100.01 is exercised unless the holder instructs otherwise."},
    {"q": "You are long the 100/105 bull call spread. XYZ closes at 104.90 on expiration Friday. Absent instructions, on Monday you most likely hold:", "opts": ["100 shares bought at 100, because the long call was exercised and the short call expired OTM", "Nothing; the spread settled for 4.90 cash", "Short 100 shares at 105", "The spread, rolled to next week"], "correct": 0, "explain": "The long 100 call is 4.90 ITM and auto-exercised; the short 105 call is OTM and, unless its holder exercises after hours, expires. You own 100 shares with full stock risk."},
    {"q": "Pin risk refers to:", "opts": ["The risk that the exchange halts trading on expiration day", "Uncertainty about whether a short option will be assigned when the stock closes at or very near the strike, leaving you with an unknown stock position", "The risk of a margin call on a long call", "Theta on the last day"], "correct": 1, "explain": "When the stock pins near a short strike, some holders exercise and some do not, and after-hours moves can change the decision, so the writer does not know their Monday position until assignment notices arrive."},
    {"q": "Early exercise of an American call on a dividend-paying stock is most likely when:", "opts": ["The call is far OTM", "The dividend exceeds the call's remaining time value, the day before the ex-dividend date", "The stock is about to split", "IV is high"], "correct": 1, "explain": "The holder gives up the call's time value by exercising but captures the dividend by owning shares on the ex-date. When the dividend is larger than the time value, exercising is rational, so deep ITM calls get assigned the day before ex-div."},
    {"q": "Which position carries NO risk of ending up with an unwanted share position at expiration?", "opts": ["A short put on a stock", "A long put on a stock", "A short call spread on a stock", "A short SPX put spread (cash-settled, European)"], "correct": 3, "explain": "Cash-settled European index options settle in cash at expiration and cannot be exercised early, so there are no shares to receive or deliver."}
  ],
  "task": "Look up your broker's exercise cutoff time on expiration day and its do-not-exercise procedure, and write both down where you keep your trade plans."
}
---


## The last day is a different market

Everything before expiration is a matter of price: you can always close the position by trading it. On expiration day the contract stops being a price and becomes an instruction. Options that are in the money turn into stock positions overnight; options that are out of the money vanish; and a handful of contracts sitting exactly at a strike become a coin flip you do not get to call. This lesson covers the mechanics so that none of it surprises you.

## Exercise by exception

At expiration the OCC automatically exercises every equity option that is in the money by $0.01 or more, using the official closing price of the underlying on its primary exchange. This is called **exercise by exception**. The holder can override it with a **do-not-exercise** instruction, and can also exercise an option that is OTM at the close (rare, but permitted, and relevant when the stock moves after hours).

The practical consequence: a long 100 call with XYZ at 100.01 at the close becomes 100 shares of XYZ, and $10,000 of cash leaves your account, whether or not you have $10,000. Most brokers will close or liquidate positions in the final hours for accounts that cannot support the resulting stock, and some will do it without notice. Do not test that policy. If you do not want stock, sell the option before the close.

## Assignment at expiration

The mirror image: every short option that finishes $0.01 or more ITM will be assigned unless its holder files a do-not-exercise. A short 100 put with XYZ at 99.99 means you buy 100 shares at 100 on Monday. A short 105 call with XYZ at 105.01 means you sell 100 shares at 105, and if you do not own them you are short stock.

Assignment notices are processed overnight and typically appear in your account before Monday's open. You cannot know on Friday afternoon whether you were assigned; you can only know whether the contract closed ITM and infer that you almost certainly were.

## Pin risk

When the stock closes within a few cents of a short strike, the writer's Monday position is genuinely uncertain, and that uncertainty is **pin risk**. Three things create it. Some holders of an ITM-by-a-penny option file do-not-exercise because they do not want the shares, so a short can escape assignment. The stock trades after the close, and holders have until their broker's cutoff (often 5:30 pm Eastern, later at some firms) to decide; a stock that closed at 104.90 and trades at 105.40 at 5:00 pm will see the 105 calls exercised by holders who are paying attention, even though the OCC would not have exercised them automatically. And a spread's two legs are assessed independently: one can be exercised or assigned without the other.

Pin risk cannot be hedged in the last hour, because the position you need to hedge is unknown. It can only be avoided, by closing short options that are near the money before the close on expiration day, or by trading cash-settled products. For a credit spread, that means buying back a short leg that sits within roughly one day's expected move of the stock, even if it looks like it will expire worthless.

## Early exercise

An American option can be exercised on any business day, so a short can be assigned on any business day. Two situations make it rational for the holder and therefore likely for the writer.

**Calls before a dividend.** A call holder does not receive dividends; a shareholder does. On the ex-dividend date the stock drops by roughly the dividend, and so does the call. A holder of a deep ITM call can capture the dividend by exercising the day before the ex-date, at the cost of the call's remaining time value. The rule: early exercise is rational when the dividend exceeds the call's time value, which for a deep ITM call is approximately the price of the same-strike put plus the interest on the strike to expiration. Writers of deep ITM calls on dividend-paying stocks should expect assignment the day before ex-div, and covered call writers should expect to lose their shares (and the dividend) then.

**Deep ITM puts.** A put holder who exercises receives the strike in cash today rather than at expiration. When the interest on that cash exceeds the put's remaining time value, and there is no dividend coming, exercising early is rational. This is why the model 115 put in Lesson 3 showed negative time value: an American holder would already have exercised it. Writers of deep ITM puts should expect assignment when rates are meaningful and time value has run out.

Outside those two cases, early exercise gives away time value for nothing, and it is rare. Short OTM and ATM options with weeks remaining are almost never assigned early. "Almost" is the operative word: assignment is a random draw among all shorts, and someone occasionally exercises for reasons of their own.

## What happens to a spread when one leg is assigned

If the short leg of a vertical is assigned early, you receive the stock position and still own the long leg. You are not exposed beyond the spread's maximum loss, because the long leg still caps it, but your account now carries a stock position and its margin requirement, which can be large relative to the spread. The response is mechanical: either exercise the long leg (if ITM) to flatten the shares, or sell the long leg and close the shares in the market, whichever recovers more value. Most brokers will do one of these for you if the margin call is not met, at a time of their choosing. Doing it yourself at the open is better.

## Cash settlement

Index options such as SPX, and their weeklies, settle in cash: at expiration the ITM amount is credited or debited and no shares change hands. They are also European style, so there is no early assignment. Monthly SPX options expiring on the third Friday are **AM-settled** on the opening prices of the index components, so their last trading day is Thursday and their settlement value (SET) is known Friday morning, sometimes far from Thursday's close; the weeklies and end-of-month contracts are **PM-settled** on Friday's close. Both eliminate pin risk in shares, but AM settlement introduces its own overnight gap. Read the product's specification before the first trade.

## Worked example

XYZ November 6, 2026 expiration. You hold the bull call spread from Lesson 10: long one 100 call, short one 105 call, entered for a 2.00 debit. The following is a scenario on the representative chain.

**3:59 pm Friday 6 November. XYZ trades at 104.90.** The spread is worth about 4.90 (the 100 call is 4.90 ITM; the 105 call is 0.10 OTM and worth a cent or two). Your choices:

- **Close the spread now** at about 4.85 bid. P&L: (4.85 - 2.00) x 100 - 2.60 = **+$282.40**. No Monday position. This is the plan.
- **Do nothing.** The long 100 call will be auto-exercised at 4:00 pm's close of 104.90: you buy 100 XYZ at 100.00, a $10,000 debit. The short 105 call is OTM at the close and not auto-exercised. Unless the holder exercises anyway, on Monday you own 100 shares worth $10,490, with $10,490 of stock risk on a position that was supposed to have $200 of risk.

**5:15 pm Friday. XYZ trades at 105.35 in the after-hours session.** Holders of the 105 call have until the broker cutoff to exercise. A holder who is watching exercises: they pay 105 for stock worth 105.35. If that exercise is assigned to you, you sell 100 shares at 105 that you just bought at 100, and your Monday position is flat with a realised (5.00 - 2.00) x 100 = +$300 less commissions. If it is assigned to someone else, you are long 100 shares into Monday. You will not know which until the notice arrives, and you cannot hedge a position you do not know you have.

**Monday 9 November. XYZ opens at 102.50 on news.** If you were not assigned, your 100 shares bought at 100 are worth 102.50: +$250 on the shares, +$50 net after the 2.00 spread debit, versus the +$282 you could have locked in Friday afternoon. Had XYZ opened at 97.50, you would be down $250 on the shares and -$450 net on a trade whose maximum loss was supposed to be $200.

**The dividend case.** Suppose instead XYZ goes ex-dividend on 12 October for 0.75, and you are short the 85 call (from a deep ITM call spread) with the stock at 100 on 11 October. The 85 call's time value is 15.58 - 15.00 = 0.58, which is the 85 put (0.16) plus interest on 85 for 45 days (85 x (1 - 0.99508) = 0.42). The dividend, 0.75, exceeds 0.58, so exercising the day before ex-div captures 0.75 at a cost of 0.58: rational. Expect to be assigned on 11 October, deliver 100 shares at 85, and forgo the dividend. Had you been short the 95 call instead, its time value of 2.15 exceeds the dividend and assignment is unlikely.

## Table

Expiration outcomes for the XYZ 100/105 bull call spread by Friday closing price, if you do nothing.

| XYZ close | Long 100 call | Short 105 call | Monday position | Realised on spread |
|---|---|---|---|---|
| 99.50 | Expires (OTM) | Expires | None | -2.00 (full loss) |
| 100.01 | Auto-exercised | Expires | Long 100 sh at 100 | Unknown: stock risk |
| 102.00 | Auto-exercised | Expires | Long 100 sh at 100 | Unknown: stock risk |
| 104.90 | Auto-exercised | Expires unless holder exercises after hours | Long 100 sh at 100, or flat if assigned | Unknown: pin risk |
| 105.01 | Auto-exercised | Assigned unless holder files do-not-exercise | Flat, or long 100 sh at 100 | +3.00, or unknown |
| 108.00 | Auto-exercised | Assigned | Flat | +3.00 (max gain) |

Four of six rows end in "unknown". That is why the rule is to close spreads before the close on expiration day, with the sole exception of a spread where both legs are far enough OTM that a same-day move to the strike is implausible, and even then the cost of buying it back for 0.02 is usually worth paying.

## Sources

- Options Clearing Corporation, exercise and assignment procedures, including exercise by exception: https://www.theocc.com/clearance-and-settlement/clearing/exercise-and-assignment
- Options Clearing Corporation, *Characteristics and Risks of Standardized Options*: https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document
- Cboe Global Markets, SPX options product specifications (AM and PM settlement): https://www.cboe.com/tradable_products/sp_500/spx_options/specifications/
- FINRA, Investor Insights, options assignment and expiration: https://www.finra.org/investors/investing/investment-products/options
