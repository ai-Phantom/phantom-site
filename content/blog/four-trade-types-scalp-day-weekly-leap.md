---
{"title": "Four Trade Types: Scalp, Day, Weekly and LEAP", "cat": "bots", "tag": "Bots & Signals", "emoji": "📡", "excerpt": "Phantom runs four option trade types. Each has its own scan window, contract range, exit rules, position size and Discord channel.", "date": "2026-10-02", "read": "6 min", "status": "published"}
---

Phantom does not trade one style. It runs four option trade types side by side: scalp, day trade, weekly and LEAP. Each has its own clock, its own contract range and its own exit rules.

If you mix them up, the signals look contradictory. A scalp CALL and a LEAP PUT on the same ticker can both be valid. They answer different questions over different time frames.

Every trade described here is a paper trade. No real money is at risk.

## The four types at a glance

| Type | When it looks | Contract | Stop | Trail | Size | Channel |
|---|---|---|---|---|---|---|
| Scalp | Every 2 min, 9:45-11:30 a.m. and 2:30-3:45 p.m. | 1-35 DTE, delta 0.75-0.88 | -45% | None; 180-min max hold | $1,000 | #scalps |
| Day trade | Every 2 min by default; opens 9:45 a.m. to a 3:00 p.m. cutoff | 1-35 DTE, delta 0.40-0.55 base | -22% | Arms at +10%, trails 5% | $1,000 | #day-trades |
| Weekly | Every 15 min; entries before 1:00 p.m. | 7-60 DTE, delta 0.40-0.55 | -15% | Arms at +20%, trails 8% | $1,000 | #trade-log |
| LEAP | Every 15 min; short entry windows | 120-365 DTE, delta 0.65-0.80 | -25% | Arms at +25%, trails 10% | $5,000 | #leaps |

All times are Eastern. DTE means days to expiration. Delta is how much the option's price moves for a $1 move in the stock. Higher delta means the contract behaves more like the stock.

"Trail arms at +10%, trails 5%" means this: nothing trails until the option is up 10%. From then on, a trailing stop follows the best price 5% behind it.

## Scalps

Scalps are the shortest trades and the narrowest setup.

By default there is only one scalp: a **CALL-only, in-the-money oversold bounce**. It fires when RSI is below 30. It also fires when RSI is below 35 and both Williams %R and Stochastic are oversold.

Only seven tickers qualify: CRWD, AMD, SPY, IWM, NVDA, TSLA and COIN.

The scalper runs every 2 minutes, but only in two windows: 9:45 to 11:30 a.m. and 2:30 to 3:45 p.m. ET. Outside those windows it does nothing.

Contracts are in the money, with delta between 0.75 and 0.88 and 1 to 35 days to expiration. The exit is blunt: a 45% stop, no trailing stop, and a maximum hold of 180 minutes.

## Day trades

Day trades are the main Phantom signal. They come from the full scored setup: indicators, weights, regime and the confidence tiers.

The scanner runs every 2 minutes by default. It starts in premarket, but no paper trade opens outside regular hours. The first 15 minutes after the open are also blocked, so the earliest open is 9:45 a.m. ET. New day trades stop at 3:00 p.m. ET.

The contract picker looks at 1 to 35 days to expiration. The base delta range is 0.40 to 0.55. More volatile tickers shift that range higher:

- Tier 1: 0.40 to 0.55
- Tier 2: 0.45 to 0.60
- Tier 3: 0.50 to 0.65
- Tier 4: 0.55 to 0.65

The exit is a 22% stop. Once the option is up 10%, a trailing stop arms 5% behind the best price. Any position with one day or less to expiration is force-closed at 3:50 p.m. ET.

Contracts with 0 to 2 days to expiration that are out of the money are blocked outright. Options that short-dated and out of the money can lose value very quickly.

HIGH-confidence day trades post to #day-trades with a role ping. MEDIUM ones post there without the ping. LOW setups go to #screener-drops.

## Weeklies

Weeklies are swing trades meant to last days, not hours.

The weekly loop runs every 15 minutes and only takes entries before 1:00 p.m. ET. A setup qualifies in one of two ways:

1. **A high score.** The scored setup reaches 75 or more.
2. **The swing-trend setup.** The 20, 50 and 100 EMAs are stacked upward, and RSI sits between 40 and 55 or price is near its 52-week high. This one is CALL-only.

Contracts differ by route. A high-score weekly uses 7 to 60 days to expiration and delta 0.40 to 0.55. The swing-trend setup uses 7 to 45 days and a higher delta of 0.65 to 0.80.

Exits differ too:

- **Default weekly:** 15% stop, trail arms at +20%, trails 8%.
- **Swing-trend weekly:** 35% stop, trail arms at +40%, trails 20%.

One detail trips people up. Phantom posts its weeklies to **#trade-log**, not #weekly. The #weekly channel carries Bullseye's alerts.

## LEAPs

LEAPs are long-dated options. They are the slowest Phantom trade.

The setup is a trend filter. Price must be more than 1% beyond its 50-day average. The 50-day must be at least 2% away from the 200-day. Then a confirming day is required.

The LEAP loop runs every 15 minutes. By default it attempts entries from :45 to :59 in the 9 a.m., 12 p.m. and 2 p.m. ET hours, and an operator setting can open it to every scan. LEAP opens stop at a 3:30 p.m. ET cutoff. A setup refused only because of the time of day, such as inside the first 15 minutes of the session, stays eligible for a later scan. Any other refusal ends that ticker's LEAP attempts for the day, and each ticker gets at most one LEAP entry per day.

Contracts run 120 to 365 days to expiration, with delta between 0.65 and 0.80. That puts them in the money.

LEAPs are the only type with a bigger budget: $5,000 per paper trade. The stop is 25%. The trail arms at +25% and trails 10%.

LEAP signals post to #leaps.

## Caps on how many can be open

Each type has a limit on open paper positions:

- Day trades: 15
- Scalps: 8
- Weeklies: 8
- LEAPs: 5

There is also a cap of 25 open positions in total across the bots. When a cap is full, new setups of that type are skipped until something closes.

## How to use this

When a signal posts, check its type first. The type tells you:

- How long the trade is expected to last.
- How far it can move against the position before the stop.
- Which channel to watch for follow-up.

A scalp that hits its stop and a LEAP that is down 10% are not the same story. Read each one on its own clock.

## Sources

- Phantom Traders bot code (October 2026)
- Options Industry Council (OCC), [options education](https://www.optionseducation.org/)

*Educational content, not financial advice. Signals are paper-traded.*
