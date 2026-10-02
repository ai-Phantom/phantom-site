---
{"title": "Phantom, Bullseye and Scout Compared", "cat": "bots", "tag": "Bots & Signals", "emoji": "📡", "excerpt": "Three signal sources post in the Phantom Traders Discord. Here is what each one watches, how often it scans, and which ones paper-trade.", "date": "2026-10-02", "read": "5 min", "status": "published"}
---

Three different sources post signals in the Phantom Traders Discord: Phantom, Bullseye and Scout. A fourth input, TradingView alerts, feeds into Phantom's score.

They are not three copies of one bot. They watch different tickers, scan on different clocks, score differently, and only one of them opens paper trades. Knowing which is which keeps you from comparing numbers that do not mean the same thing.

## The short version

| | Phantom | Bullseye | Scout |
|---|---|---|---|
| Watchlist | 39 tickers | 32 tickers | 42 tickers |
| How often | Main scanner every 2 minutes by default | Every 15 minutes, regular hours | Every 5 minutes, weekdays, 8:00 a.m. to 3:55 p.m. Central |
| Trade types | Scalp, day trade, weekly, LEAP | Weekly | None |
| Signal basis | Additive points, no hard cap | Normalized to 0-100, minimum 65 | 15-minute bars, 5-minute confirmation |
| Paper trades? | Yes | No, switched off | No, alert-only |
| Where it posts | #day-trades, #scalps, #leaps, #trade-log | #weekly | #scout |

## Phantom: the main bot

Phantom is the workhorse. It is the only source here that opens paper trades, and it runs all four trade types.

**Watchlists.** The main watchlist has 39 tickers. Scalps use a separate 12-ticker list, and the default scalp setup only fires on seven of those. LEAPs use a 16-ticker list.

**Cadence.** The main day-trade scanner runs every 2 minutes by default. The scalper also runs every 2 minutes, but only in two windows: 9:45 to 11:30 a.m. and 2:30 to 3:45 p.m. ET. The weekly and LEAP loops run every 15 minutes.

**Scoring.** Phantom adds points from eight indicators ported from TradingView scripts, plus classic signals like RSI, MACD, Bollinger bands and volume surges. Each signal's points are multiplied by a learned weight. CALL and PUT points are tallied separately, and the bigger side wins. A setup needs at least 35 points, at least three agreeing signals (or two with a premium one), and at least one premium signal.

**Trades.** Every Phantom open is a paper trade, journaled in #trade-log. Day trades post to #day-trades, scalps to #scalps, LEAPs to #leaps. Phantom's weeklies go to #trade-log, not #weekly.

## Bullseye: weekly alerts

Bullseye is a smaller, simpler bot focused on weekly options.

**Watchlist and cadence.** It watches 32 tickers and scans every 15 minutes during regular hours.

**Scoring.** Bullseye uses its own scorer. It adds points from RSI, MACD, Bollinger bands, UT Bot, Williams %R, ATR and price range. Then it normalizes the total to a 0-100 scale. Of Phantom's eight ported indicators, it uses only UT Bot.

It posts when confidence is at least 65. Its labels are:

- **EXTREME:** 90 or more.
- **HIGH:** 80 or more.
- **SOLID:** 70 or more.

**Contracts.** For HIGH setups, Bullseye's suggested expiration is the next Friday that is at least two days out. Otherwise it suggests about 30 days to expiration.

**Paper trading is off.** This is the key difference. Bullseye's paper trading is switched off by default. It was turned off after its paper results, over a small sample of trades, fell well short of what its trades needed to break even. Its signals still post, but they are alerts only. No paper position stands behind a Bullseye card.

**Channels.** Bullseye posts to #weekly. If that channel is unavailable, it falls back to #day-trades. Its squeeze alerts go to #day-trades.

## Scout: a faster, wider radar

Scout is alert-only. It never opens trades.

**Watchlist.** Scout watches the widest list of the three: 42 tickers.

**Cadence.** It runs every 5 minutes on weekdays, from 8:00 a.m. to 3:55 p.m. Central time. That is 9:00 a.m. to 4:55 p.m. Eastern.

**Bars.** Scout reads 15-minute bars for its signal and uses 5-minute bars to confirm it.

**Channel.** Scout posts to #scout.

No paper trade stands behind a Scout alert. Treat it as a heads-up, not as a position with a managed stop and exit.

## TradingView alerts: an extra input

TradingView alerts are not a separate bot in Discord. They feed into Phantom's score.

Each fresh alert on a ticker from the last 30 minutes adds 15 points to Phantom's tally, up to five alerts per ticker. Once an alert is used, it does not count again.

The bots can also accept trades sent from TradingView directly. Those go through the same paper-trade opening step as Phantom's own trades, so every entry gate still applies. Allowed types are the same four: scalp, day trade, weekly and LEAP.

## How to use the three together

Each source answers a different question:

- **Scout** has the widest watchlist and the shortest scan interval. It alerts on intraday bars and never trades.
- **Phantom** asks whether enough signals agree, in the right market, to open a paper trade. It is the only one with a paper position behind it.
- **Bullseye** scores weekly setups on its own 0-100 scale. It is a second opinion, alert-only.

A few practical rules:

1. **Do not compare scores across bots.** A Bullseye 80 is on a 0-100 scale. A Phantom 80 is additive points. They are built differently.
2. **Check for a paper position.** Only Phantom opens paper trades. Look for the open in #trade-log.
3. **Mind the time frame.** Scout works from 15-minute bars. Phantom's trade types run from minutes to months. A Scout alert and a Phantom signal on the same ticker can point different ways.
4. **Remember Phantom's trend filter.** By default, Phantom will not post PUTs in an up-trending market or CALLs in a down-trending one. Scout and Bullseye may still alert in that direction.

## A note on paper trading

Phantom's trades are on a paper account. Bullseye and Scout do not trade at all. None of these sources should be read as a record of real-money results.

## Sources

- Phantom Traders bot code (October 2026)
- Options Industry Council (OCC), [options education](https://www.optionseducation.org/)

*Educational content, not financial advice. Signals are paper-traded.*
