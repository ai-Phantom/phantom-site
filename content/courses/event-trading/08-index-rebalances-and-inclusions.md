---
{
  "title": "Index Rebalances and Inclusions",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Greenwood and Sammon (2025) report that the average abnormal return on S&P 500 addition announcements fell from about 7.4% in the 1990s to:", "opts": ["About 5%", "About 3%", "Less than 1% over the most recent decade", "It rose to 10%"], "correct": 2, "explain": "The paper's title is 'The Disappearing Index Effect.' The addition premium has shrunk to under 1% as more liquidity providers pre-position and as index funds have become a larger, more predictable share of demand."},
    {"q": "S&P Dow Jones Indices announced on August 13, 2026 that Reddit would join the S&P 500 'effective prior to the open on August 18.' On which day did index funds have to complete their buying?", "opts": ["August 13", "August 14", "August 17, at the close", "August 18, at the open"], "correct": 2, "explain": "The index changes overnight between the 17th and the 18th, so funds that must hold the index at the 18th's open buy at the close on the 17th. RDDT's volume on August 17 was 37.8 million shares, eight times the pre-announcement day."},
    {"q": "RDDT closed at 158.12 on August 13, 178.09 on August 14, and 158.25 on August 18. What is the correct summary?", "opts": ["The inclusion added 12.6% permanently", "The announcement-day pop of 12.6% was fully given back by the effective date; the round trip was +0.08%", "The stock fell because of the inclusion", "Index funds sold the stock"], "correct": 1, "explain": "The whole announcement premium was returned in three sessions, with the heaviest selling on the very day index funds bought. Whoever sold to the index funds at the August 17 close had bought lower after the announcement."},
    {"q": "The June 2026 Russell reconstitution took effect after the close on June 26. IWM traded 39.8 million shares that day against about 26.5 million on the prior four days. Why is the volume concentrated at the close?", "opts": ["The exchange requires it", "Index funds track the closing price, so the reconstitution trades are executed in the closing auctions to match the index's own repricing", "Retail traders sell on Fridays", "Options expire"], "correct": 1, "explain": "FTSE Russell reconstitutes at the close, and index-tracking funds minimise tracking error by trading in the NYSE closing auction and the Nasdaq Closing Cross at the same price the index uses. That is why the closing auction on reconstitution day is one of the largest single liquidity events of the year."},
    {"q": "Chang, Hong and Liskovich (2015) used a regression discontinuity design around the Russell 1000/2000 cutoff. What did that design let them measure cleanly?", "opts": ["The effect of earnings on price", "The price effect of index membership itself, by comparing firms just above and just below the cutoff that are otherwise nearly identical", "The Fed's effect on small caps", "Nothing; the design failed"], "correct": 1, "explain": "Firms on either side of the rank cutoff differ almost only in which index they land in, so the difference in their returns isolates the demand from index funds. They found additions to the Russell 2000 rose and deletions fell."}
  ],
  "task": "Find the next S&P Dow Jones Indices quarterly rebalance date and the next FTSE Russell reconstitution effective date, and put both on your event calendar with the announcement date for each."
}
---

## A different kind of event

Earnings and macro releases move prices by delivering information. Index changes move prices by delivering *order flow*. When S&P Dow Jones Indices adds a company to the S&P 500, every fund that tracks the index has to own it by the effective date, and every fund that tracks the index the company left has to sell it. Nothing about the company changed. The demand for its shares did, predictably, on a published date.

That predictability is why the index effect has been studied since Shleifer (1986) and why, as Greenwood and Sammon document in "The Disappearing Index Effect," it has mostly been arbitraged away. This lesson covers the mechanics of S&P 500 changes, the annual and now semi-annual Russell reconstitution, what the evidence says about the size of the effect over time, and what remains for a trader who is not a market-maker.

## S&P 500 changes: announcement, effective date, and who trades when

S&P Dow Jones Indices manages the S&P 500 by committee, following a published methodology. Changes come in two forms: **ad hoc** replacements, when a constituent is acquired, delisted or otherwise leaves and a replacement is named; and the **quarterly rebalance**, effective after the close on the third Friday of March, June, September and December, when the committee can make multiple changes at once. The September 2026 rebalance, for example, was announced on September 4 and became effective prior to the open on Monday, September 21, meaning funds traded the September 18 close.

Every change is announced by press release, usually after the market closes, with the language "effective prior to the open of trading on [date]." The trade for index funds therefore happens at the *close of the last trading day before* the effective date, because that close is the price at which the index itself reprices. The days between the announcement and the effective date are when everyone else positions.

## Worked example

Reddit's addition to the S&P 500, announced August 13, 2026, effective prior to the open on Tuesday, August 18. Reddit replaced AvalonBay Communities, which was being acquired by fellow constituent Equity Residential. RDDT daily bars from the Yahoo Finance chart API (495 rows, 2024-10-01 to 2026-09-23):

- **August 13 (announcement after the close):** close **158.12**, volume 4.66 million.
- **August 14:** open 175.78, high 184.28, close **178.09**, volume 21.5 million. Announcement-day reaction: 178.09 / 158.12 − 1 = **+12.63%**. Gap at the open: 175.78 / 158.12 − 1 = +11.17%.
- **August 17 (index funds buy at this close):** close **164.50**, volume **37.8 million**, eight times the August 13 volume. Day: 164.50 / 178.09 − 1 = **−7.63%**.
- **August 18 (effective date):** close **158.25**, volume 7.45 million. Day: −3.80%.
- **August 19:** close 151.71, −4.13%. **August 20:** 150.31.

Round trip from the pre-announcement close to the effective date close: 158.25 / 158.12 − 1 = **+0.08%**. From the announcement-day close to the effective date: −11.14%. Two days later the stock was 4.9% *below* where it had been before the announcement.

Read the volume. The announcement-day buyers, 21.5 million shares at an average price well above 170, were not index funds; index funds had no need to own the stock until the 17th. They were traders front-running the index demand. On the 17th, 37.8 million shares changed hands, most of them in the closing auction, and the index funds bought from the people who had bought on the 14th. The front-runners were paid to provide liquidity: they bought at 175 and sold at 164. That is not a typo. The demand from index funds was so well anticipated that the anticipation overshot, and the trade that "always works" lost 6% for the people who put it on at the open on the 14th.

This is one inclusion. The academic average is what tells you whether it was typical.

## What the evidence says

Greenwood and Sammon (2025) compile S&P 500 additions and deletions over several decades and measure the abnormal return around the announcement. Their headline finding: the average announcement-to-effective abnormal return for additions was about **7.4% in the 1990s** and has fallen to **less than 1%** over the most recent decade in their sample. Deletions show the mirror decline. They attribute the shrinkage to several forces: index funds now trade more patiently and more predictably, liquidity providers pre-position, and additions are more often companies that were already widely held. The effect has not vanished on the announcement day, as RDDT shows, but the *net* effect by the effective date has.

Chang, Hong and Liskovich (2015) attacked the identification problem from the other end. Around the Russell 1000/2000 cutoff, firms ranked just above and just below differ almost only in which index they fall into. Using that discontinuity they showed additions to the Russell 2000 experienced price increases and deletions price declines, that the effects have trended over time, and that particular types of funds supply the liquidity to indexers. Their paper is the cleanest evidence that index demand *itself* moves prices, separate from any news about the firm.

## The Russell reconstitution

FTSE Russell reconstitutes the Russell U.S. indexes on a published schedule. For June 2026: rank day was April 30 (membership is determined by market capitalisation on that date), preliminary addition and deletion lists were posted from May 22, and the reconstitution took effect **after the close on Friday, June 26, 2026**. FTSE Russell's press release cited roughly $12.2 trillion benchmarked to or invested in products based on the Russell U.S. indexes, 62 expected additions to the Russell 1000 and 237 to the Russell 2000, and noted that at the June 2025 reconstitution $217.2 billion traded across U.S. exchanges at the close.

2026 is also the first year of **semi-annual** reconstitution. The second one has rank day on the last business day of October (October 30, 2026) and takes effect after the close on the second Friday of December, **December 11, 2026**.

The reconstitution's price effect is now mostly a closing-auction phenomenon. IWM, the Russell 2000 ETF, traded **39.8 million** shares on June 26, 2026 against an average of about **26.5 million** on the four preceding sessions (22.8, 26.8, 28.7 and 27.6 million), a ratio of 1.5, with the close at 299.83 against 298.91 the day before. The closing auction absorbs the flow at a single price; for the trader, the reconstitution is a liquidity event to be aware of rather than a directional trade, unless you hold a name on the preliminary list and want to know why it is behaving strangely in June.

## Table

| Date | Event | RDDT close | Day change | Volume (m) |
|---|---|---|---|---|
| 2026-08-13 | Announcement after close | 158.12 | | 4.66 |
| 2026-08-14 | First trading day after announcement | 178.09 | +12.63% | 21.50 |
| 2026-08-17 | Last close before effective; index funds buy | 164.50 | −7.63% | 37.85 |
| 2026-08-18 | Effective prior to open | 158.25 | −3.80% | 7.45 |
| 2026-08-20 | Two days after | 150.31 | −0.93% | 7.67 |

## What is left for a trader

Three things, none of them the obvious one.

The **announcement-day gap** is real and large, but you cannot get it: the announcement comes after the close and the gap is in the open. Buying the open on the 14th was the losing trade.

The **effective-date close** is a liquidity event. If you hold an added name for other reasons, the closing auction on the day before the effective date is the most liquid moment it will have for months, and a good time to trim without moving the price. If you hold a deleted name, the same auction is where the selling concentrates.

The **preliminary list** for Russell, posted a month before the effective date, is public information about a future demand shock. Chang, Hong and Liskovich's evidence says the demand moves prices; Greenwood and Sammon's evidence says the market has largely learned to price it ahead. The position in between, which their work supports, is that the effect is now small, front-loaded to the announcement, and often reversed by the effective date. It is a tilt to be aware of when you already have a position, not a strategy.

## Sources

- Greenwood, R., and Sammon, M. (2025). "The Disappearing Index Effect." Journal of Finance 80(2), 657–698. https://doi.org/10.1111/jofi.13410
- Chang, Y.-C., Hong, H., and Liskovich, I. (2015). "Regression Discontinuity and the Price Effects of Stock Market Indexing." Review of Financial Studies 28(1), 212–246. https://doi.org/10.1093/rfs/hhu041
- S&P Dow Jones Indices, "Reddit Set to Join S&P 500 and Sun Communities to Join S&P MidCap 400," August 13, 2026: https://press.spglobal.com/2026-08-13-Reddit-Set-to-Join-S-P-500-and-Sun-Communities-to-Join-S-P-MidCap-400
- FTSE Russell (LSEG), "FTSE Russell Begins June 2026 Semi-Annual Russell US Indexes Reconstitution": https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2026/ftse-russell-begins-june-2026-semi-annual-russell-us-indexes-reconstitution and reconstitution hub: https://www.lseg.com/en/ftse-russell/russell-reconstitution
