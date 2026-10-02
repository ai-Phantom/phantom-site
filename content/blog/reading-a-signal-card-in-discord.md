---
{"title": "Reading a Signal Card in Discord", "cat": "bots", "tag": "Bots & Signals", "emoji": "📡", "excerpt": "What each field on a Phantom signal card means, which numbers are display values, and how to follow the paper trade in #trade-log and #trade-recap.", "date": "2026-10-02", "read": "6 min", "status": "published"}
---

A signal card packs a lot into a small box. Ticker, direction, contract, score, entry, stop, targets. It is easy to read it as an instruction. It is not. It is a summary of what a bot saw and what its paper trade is set up to do.

This post walks through each field, flags the ones that are easy to misread, and shows you where to follow what happened next.

## First, check the channel

Where a card appears tells you what kind of signal it is before you read a word:

- **#day-trades:** Phantom day trades. HIGH-confidence cards also come with a role ping.
- **#screener-drops:** LOW-confidence setups that did not reach the day-trade bar.
- **#scalps:** Phantom scalps.
- **#leaps:** Phantom LEAPs.
- **#trade-log:** a journal of every paper trade Phantom opens. Phantom's weeklies also post here.
- **#weekly:** Bullseye's weekly alerts. Bullseye's paper trading is switched off, so these are alerts only.
- **#scout:** Scout alerts. Scout never opens trades.
- **#trade-recap:** recaps of what the bots did.

So a weekly CALL in #weekly and a weekly CALL in #trade-log come from different bots with different scorers.

## Ticker and direction

The ticker is the underlying stock or ETF. CALL or PUT is the direction.

For Phantom, the direction is simply the side that won. Phantom adds up CALL points and PUT points separately, and the bigger total sets the direction. If the trend filter is on (it is by default), Phantom only posts CALLs when the market trend is up and PUTs when it is down.

## Trade type

The type tells you the clock the trade runs on. Phantom has four:

- **Scalp:** minutes to a few hours. The default scalp is a CALL-only bounce in an in-the-money contract, held for at most 180 minutes.
- **Day trade:** the main scored signal. Short-dated contracts.
- **Weekly:** a swing trade lasting days.
- **LEAP:** long-dated contracts, 120 to 365 days out.

Read every other field in light of the type. A 20% drop means very different things on a scalp and a LEAP.

## The contract

The card names an option: a strike and an expiration.

Here is a subtlety. On some cards, the contract shown is a suggestion from a quick rule of thumb. For day trades, that rule aims for about 30 days to expiration on HIGH setups and 45 days on MEDIUM and LOW ones, with an out-of-the-money strike sized from the stock's typical move.

The paper trade does not use that rule. When it opens, it picks a contract from the live option chain, inside a fixed range of days to expiration and delta. For day trades that range is 1 to 35 days and a delta of roughly 0.40 to 0.55, shifted higher for more volatile tickers.

So the contract on the card and the contract in the paper trade can differ. If you want to know what was actually opened, check #trade-log.

## Score and confidence tier

Phantom's score is points, not a percentage. It can be shown as "score/100," but it has no hard cap at 100.

The tier is what to focus on:

- **HIGH:** 80 or more.
- **MEDIUM:** 50 to 79.
- **LOW:** below 50.

Every Phantom day-trade card has already cleared a minimum of 35 points, at least three agreeing signals (or two with a premium signal), and at least one premium signal. A day-trade setup under 80 has also repeated in the same direction on a second scan.

Bullseye is different. Its score is normalized to a 0-100 scale, and its labels are EXTREME (90+), HIGH (80+) and SOLID (70+). Its minimum is 65. Do not compare a Bullseye 80 to a Phantom 80 directly. They are built differently.

## Entry

The entry is the reference price on the card at the time of the signal. The paper trade itself only opens with a live quote. If there is no live quote, the bot does not open the trade.

By the time you read a card, the price has probably moved. The entry is a reference point, not a fill you can expect to get.

## Stop and targets

This is the field most often misread.

The stop and targets printed on a card are display values. The bot's paper trade follows its own managed exit, which can be different.

For example, a day-trade card may show a target and stop such as "+50 / −30." The paper trade behind it actually runs on these rules:

- A 22% stop.
- Once the option is up 10%, a trailing stop arms.
- The trail follows the best price 5% behind it.
- Positions with one day or less to expiration are closed at 3:50 p.m. ET.

The other types have their own managed exits:

- **Scalp:** 45% stop, no trail, 180-minute maximum hold.
- **Weekly:** 15% stop, trail arms at +20%, trails 8%. The swing-trend weekly uses a 35% stop, arms at +40% and trails 20%.
- **LEAP:** 25% stop, trail arms at +25%, trails 10%.

Hold-time hints on a card are display text too. When the card and the managed exit disagree, **the managed exit is what the paper trade follows.**

## Following a trade after the card

A card and a paper open are separate steps. Do not assume a card means a paper position exists. Gates at the moment of opening can still stop a trade: a spread that is too wide, a full position cap, or a missing live quote.

Here is how to follow up:

1. **Check #trade-log.** Every paper trade Phantom opens is journaled there. If the open is not there, assume it did not happen.
2. **Watch the clock for the type.** A scalp resolves within hours. A LEAP can run for months.
3. **Check #trade-recap** for the bots' recaps of what happened.

## A quick checklist

When a new card lands, run through this:

- Which channel, and so which bot and type?
- CALL or PUT, and does it match the market trend?
- What tier? HIGH, MEDIUM or LOW?
- Is the contract on the card the one in #trade-log?
- What is the managed exit for this type, regardless of the card's targets?

Five questions. Thirty seconds. You will read cards far more accurately.

Remember: every trade the bots take is on a paper account. A card shows what a bot saw and how its paper trade is set up. It is not a recommendation to buy anything.

## Sources

- Phantom Traders bot code (October 2026)
- Options Industry Council (OCC), [options education](https://www.optionseducation.org/)

*Educational content, not financial advice. Signals are paper-traded.*
