---
{
  "title": "Measuring Exposure: Gross, Net, Beta and Sector",
  "duration": "18 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "A book on $1,000,000 of equity holds $899,403 long and $249,985 short. Its gross and net exposure are", "opts": ["89.9% and 25.0%", "64.9% and 114.9%", "114.9% and 64.9%", "100% and 0%"], "correct": 2, "explain": "Gross adds the absolute values: (899,403 + 249,985) / 1,000,000 = 114.9%. Net subtracts the short from the long: (899,403 − 249,985) / 1,000,000 = 64.9%. Gross is what you have at risk if everything moves against you; net is your directional bet."},
    {"q": "The book's dollar net is 64.9% but its beta-adjusted net on one-year betas is about 0.30. Why do they differ so much?", "opts": ["Because the shorts (IWM at 1.19, ARKK at 2.28) carry more market sensitivity per dollar than most of the longs, so 25% of short dollars offsets far more than 25% of market exposure", "The betas were computed wrongly", "Because gold has no beta", "Because net exposure ignores the shorts"], "correct": 0, "explain": "Beta-adjusted net weights each position by its beta to SPY. Two high-beta shorts cancel much of the long side's market exposure, and the two negative-beta longs (XOM and COST over this window) pull it lower still. The book is a 65% dollar bet but only a 30% market bet."},
    {"q": "Over the one-year window, XOM's beta to SPY was −0.57, but its three-year beta was +0.19. Which conclusion is sound?", "opts": ["XOM is a permanent hedge against the market", "Energy stocks have no beta", "The three-year number is always the right one", "Beta is a sample estimate that moves with the window, so the exposure report should show more than one window and treat the disagreement itself as information"], "correct": 3, "explain": "A negative one-year beta and a positive three-year beta means the relationship changed during the last year, not that XOM has become a hedge for all time. Reporting both windows prevents you from building a hedge on a relationship that may already be gone."},
    {"q": "Technology is 27% of NAV in the book, from two positions. What exposure does that sector number miss?", "opts": ["Nothing; sector is the complete picture", "The factor overlap: AMZN and the short ARKK also load on the same growth factor, so the growth exposure is larger than the tech label and the ARKK short partly offsets it", "The dividend yield of each stock", "Whether the positions were bought this year"], "correct": 1, "explain": "Sector labels follow a classification scheme; factor exposure follows what the returns actually do. NVDA's beta to QQQ was 1.30 and ARKK's was 1.45, so the ARKK short cancels a slice of growth exposure that a sector table shows as untouched."},
    {"q": "What is the single most important reason to compute exposures from shares times price every day rather than from the target weights you set at entry?", "opts": ["Regulators require it", "Target weights are usually wrong", "Prices move, so actual weights drift from targets; a position that has rallied is now a bigger share of NAV and of risk than the number you wrote down", "Daily computation is faster"], "correct": 2, "explain": "Exposure is a fact about today's marks, not about the plan. The worked example rounds share counts to whole shares and then recomputes weight as shares × price ÷ NAV; a 15% target that has run 40% is a 21% position."}
  ],
  "task": "Rebuild your own book's exposure table from shares × last close: gross, net, beta-adjusted net on two windows, and net by sector."
}
---

## Exposure is the first number in the report

Before volatility, before VaR, before any stress test, the risk report answers one question: what do we own, in what size, and how much of it moves with the market? That is exposure, and it is worth measuring properly because every later number is computed from it. A VaR built on the wrong exposure is precisely wrong.

You measure exposure in four layers. Dollar exposure: gross and net. Market exposure: beta-adjusted net. Sector exposure: net by classification. Factor exposure: what the returns actually load on, whatever the label says. Each layer catches something the previous one hides.

## Gross and net

Gross exposure is the sum of the absolute values of all positions divided by equity. Net exposure is longs minus shorts divided by equity. A book that is 90% long and 25% short is 115% gross and 65% net.

Gross is your exposure to being wrong on everything at once: it is the number that margin, liquidity and operational risk care about, because a short that goes against you costs money just as a long does. Net is your directional bet: if the whole market moves 1% and every position moves with it, net times 1% is your P&L.

Both are stated as a percentage of equity, not of long market value. A manager who says "we are 60% net" and a manager who says "we are 60% long" may be describing very different books; the second one has said nothing about shorts.

## Beta-adjusted net

Dollar net treats every position as if it moved one-for-one with the market. It does not. A 10% short in an ETF with a beta of 2.3 offsets 23% of market exposure, not 10%. A 10% long in a stock whose beta over the window was negative adds negative market exposure.

Beta-adjusted net is the sum over positions of weight times beta, where beta is the slope of the position's daily returns regressed on SPY's daily returns. It answers: if SPY moves 1%, what does the book move, on average, from market exposure alone?

Beta is an estimate from a window, and it changes with the window. Report at least two windows. When a one-year beta and a three-year beta disagree by more than half a unit, the relationship has changed recently, and any hedge built on it deserves a second look. The worked example below has a position whose one-year beta is −0.57 and whose three-year beta is +0.19.

## Sector and factor

Sector exposure is net weight grouped by classification. It is quick and it catches the obvious concentration, but it is only as good as the labels. A retailer with a cloud business is "consumer discretionary"; a chip designer and a software company are both "technology" although their returns share less than you would guess.

Factor exposure looks past the label at what the returns do. The simplest version is a beta to a factor proxy: QQQ for large-cap growth, IWM for small caps, XLE for energy, TLT for duration. A long NVDA and a short ARKK both load heavily on growth, so a sector table that shows technology at 27% and "growth ETF" at −10% is understating the tech long and overstating its separation from the short. Lesson 6 turns this into the overlap problem; here you just need to see that the four layers give four different pictures of the same ten lines.

## Worked example

The course book, used through lesson 12. Ten positions, marked at the 2026-09-23 close, on $1,000,000 of equity. Prices are Yahoo Finance closes. Share counts are target weight × NAV ÷ price, rounded to whole shares; weights are then recomputed from shares × price, which is why they are not exactly the round targets.

Longs: NVDA 665 shares × $225.51 = $149,964 (15.0%). MSFT 240 × $500.59 = $120,142 (12.0%). AMZN 441 × $249.27 = $109,928 (11.0%). JPM 356 × $337.53 = $120,161 (12.0%). XOM 620 × $161.23 = $99,963 (10.0%). UNH 242 × $371.29 = $89,852 (9.0%). COST 99 × $904.70 = $89,565 (9.0%). GLD 305 × $392.88 = $119,828 (12.0%).

Shorts: IWM −532 × $281.92 = −$149,981 (−15.0%). ARKK −1,114 × $89.77 = −$100,004 (−10.0%).

Long market value: $899,403. Short market value: $249,985.

Gross = (899,403 + 249,985) ÷ 1,000,000 = **114.9%**. Net = (899,403 − 249,985) ÷ 1,000,000 = **64.9%**.

Betas to SPY are ordinary least squares slopes on daily returns, Yahoo adjusted closes, one-year window 2025-09-24 to 2026-09-23, 251 returns. (One data note: at the time of the pull, Yahoo's series for XOM, UNH, COST and ARKK lacked a 2026-09-22 row; the 09-21 close was carried forward, which places those names' two-day move on 09-23.) SPY's own annualised volatility over the window was 13.0%.

One-year betas: NVDA 1.90, MSFT 0.95, AMZN 1.44, JPM 0.78, XOM −0.57, UNH 0.43, COST −0.13, GLD 0.75, IWM 1.19, ARKK 2.28.

Weight × beta: NVDA 0.150 × 1.90 = 0.285. MSFT 0.120 × 0.95 = 0.114. AMZN 0.110 × 1.44 = 0.158. JPM 0.120 × 0.78 = 0.094. XOM 0.100 × (−0.57) = −0.057. UNH 0.090 × 0.43 = 0.039. COST 0.090 × (−0.13) = −0.012. GLD 0.120 × 0.75 = 0.090. IWM −0.150 × 1.19 = −0.179. ARKK −0.100 × 2.28 = −0.228.

Sum: **beta-adjusted net ≈ 0.31** (0.306 on unrounded inputs). Dollar net says 65% of NAV moves with the market; beta says 31% does. The gap is the two high-beta shorts and the two negative-beta longs.

Three-year betas (2023-09-25 to 2026-09-23): NVDA 2.04, MSFT 0.97, AMZN 1.40, JPM 0.87, XOM 0.19, UNH 0.26, COST 0.44, GLD 0.25, IWM 1.12, ARKK 2.03. Beta-adjusted net on those: **0.42**. The two windows disagree by 0.11 of market exposure, mostly because XOM, COST and GLD have behaved differently in the last year than in the three-year average. Both numbers go in the report.

Sector, net of NAV: Technology 27.0% (NVDA, MSFT). Financials 12.0%. Gold 12.0%. Consumer discretionary 11.0%. Energy 10.0%. Health care 9.0%. Consumer staples 9.0%. Growth ETF −10.0%. Small-cap index −15.0%.

Factor check, one-year betas to QQQ: NVDA 1.30, MSFT 0.54, AMZN 0.83, ARKK 1.45, IWM 0.69. The growth long (NVDA + MSFT + AMZN, 38% of NAV) has a QQQ-beta-weighted exposure of 0.150 × 1.30 + 0.120 × 0.54 + 0.110 × 0.83 = 0.195 + 0.065 + 0.091 = 0.351; the two shorts offset −0.100 × 1.45 − 0.150 × 0.69 = −0.145 − 0.104 = −0.249. Net growth-factor exposure is about 0.10, far smaller than the 27% "technology" line suggests, because the shorts are doing most of their work against growth, not against the broad market.

## Chart

![Net exposure of the ten-position book by sector, percent of NAV, at the 2026-09-23 close. Technology 27%, financials 12%, gold 12%, consumer discretionary 11%, energy 10%, health care 9%, staples 9%, growth ETF −10%, small-cap index −15%. Prices from Yahoo Finance.](figures/book-exposure-by-sector.svg)

## Reading the four layers together

Dollar view: 115% gross, 65% net, a moderately levered long-biased book.

Market view: 0.31 to 0.42 beta-adjusted net depending on window, a book that would be expected to capture a third to two-fifths of a market move.

Sector view: technology-heavy at 27%, with a bar of gold and a short in small caps that has no sector at all.

Factor view: growth exposure mostly neutralised by the ARKK short; the residual market exposure is carried by JPM, GLD and the small net technology leg.

None of these views is wrong and none is complete. The report shows all four, every day, from shares times price. Lesson 3 adds the volatility of each line; lesson 4 combines them into a loss estimate; lesson 5 shows what happens to the combination when the correlations that make the shorts work stop working.

## Sources

- Sharpe, W. F. (1964). "Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk." *Journal of Finance* 19(3). https://doi.org/10.1111/j.1540-6261.1964.tb02865.x
- Fama, E. F. and French, K. R. (1993). "Common risk factors in the returns on stocks and bonds." *Journal of Financial Economics* 33(1). https://doi.org/10.1016/0304-405X(93)90023-5
- Yahoo Finance historical data, SPY and the ten book tickers. https://finance.yahoo.com/quote/SPY/history/
