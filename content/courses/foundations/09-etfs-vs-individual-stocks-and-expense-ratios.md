---
{
  "title": "ETFs vs Individual Stocks and Expense Ratios",
  "duration": "14 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "An expense ratio of 0.03 percent on a 10,000 dollar holding costs how much per year?", "opts": ["3 dollars", "30 dollars", "300 dollars", "0.30 dollars"], "correct": 0, "explain": "0.03 percent is 0.0003. Multiplied by 10,000 dollars, that is 3 dollars per year, deducted from the fund's assets daily rather than billed to you."},
    {"q": "What keeps an ETF's market price close to the value of its holdings?", "opts": ["The SEC sets the price daily", "Authorised participants create and redeem shares in exchange for the underlying basket, arbitraging any gap", "The fund manager buys back shares below NAV", "Nothing; ETFs routinely trade at large discounts"], "correct": 1, "explain": "The creation and redemption mechanism lets large dealers exchange baskets of stock for ETF shares and vice versa, which closes premiums and discounts for liquid ETFs."},
    {"q": "SPY charges 0.0945 percent and VOO charges 0.03 percent to track the same index. Over 30 years on 10,000 dollars at 7 percent gross, the difference in ending value is closest to:", "opts": ["About 14 dollars", "About 140 dollars", "About 1,400 dollars", "About 14,000 dollars"], "correct": 2, "explain": "The gap of 0.0645 percent per year compounds to roughly 1,400 dollars on a 75,000 dollar ending value. Small fees matter over long periods, but this gap is far smaller than the gap to a 0.75 percent fund."},
    {"q": "A 3x leveraged ETF is designed to deliver three times the index's return over:", "opts": ["Any holding period", "One year", "One day", "One quarter"], "correct": 2, "explain": "Leveraged and inverse ETFs reset daily. Over longer periods, compounding of daily moves means the return can differ greatly from three times the index, especially in volatile markets."},
    {"q": "Compared with a traditional mutual fund, an ETF:", "opts": ["Can only be bought at the end-of-day NAV", "Trades throughout the day at market prices with a bid-ask spread", "Has no expense ratio", "Is not regulated under the Investment Company Act"], "correct": 1, "explain": "ETFs trade like stocks on an exchange. Mutual funds are bought and sold once a day at NAV directly with the fund."}
  ],
  "task": "Look up the expense ratio, average daily volume and typical bid-ask spread of two ETFs that track the same index, and write down which you would choose and why."
}
---

## What an ETF is

An exchange-traded fund is a pooled investment that holds a basket of securities and issues shares that trade on an exchange like a stock. Buy one share of an S&P 500 ETF and you own a tiny slice of about 500 companies, weighted as the index weights them. The fund is regulated under the Investment Company Act of 1940, publishes its holdings daily, and charges an expense ratio that is deducted from the fund's assets a little each day.

The price you pay is the market price on the exchange, not the net asset value (NAV) of the holdings. The two stay close because of a mechanism called creation and redemption: large dealers known as authorised participants can hand the fund a basket of the underlying stocks and receive new ETF shares, or hand back ETF shares and receive the stocks. If the ETF trades above NAV, they create shares and sell them; if below, they buy shares and redeem them. For liquid ETFs the premium or discount is a few basis points. For ETFs holding illiquid assets (some bond and foreign-market funds) it can widen during stress.

## Index versus active

Most ETF assets sit in index funds, which hold whatever a published index holds and change only when the index changes. Their job is to track, and the number to check is **tracking difference**: the fund's return minus the index's return, which over time is roughly the expense ratio plus or minus small operational effects.

Active ETFs have a manager choosing holdings. They charge more, and their returns depend on the manager. They are a legitimate product, but a beginner comparing an active ETF to an index fund should insist on a track record of several years, net of fees, against the relevant index.

## The expense ratio

The expense ratio is the annual cost of owning the fund, stated as a percentage of assets. It covers management, administration, custody and index licensing. It is not billed to you; it is subtracted from the fund's assets continuously, so it shows up as a slightly lower return than the index.

Three things about it:

- **It compounds.** A fee taken every year reduces the base that grows in every subsequent year. The worked example quantifies this.
- **It is not the only cost.** The bid-ask spread when you trade, any premium or discount to NAV, and the fund's own trading costs inside the portfolio are on top. For a liquid index ETF these are tiny; for a niche ETF they can exceed the expense ratio.
- **Lower is not automatically better if the funds differ.** Compare fees only between funds that hold the same thing. A 0.20 percent fund tracking the Nasdaq-100 and a 0.03 percent fund tracking the S&P 500 are different bets, not a fee comparison.

## Diversification: what an ETF buys you

Owning one stock exposes you to everything that can happen to one company: a failed product, a fraud, a lawsuit, an executive scandal. That is idiosyncratic risk, and it is unrewarded: the market does not pay you extra for bearing risk you could have diversified away. An index ETF removes almost all of it. What remains is market risk: the whole index falls in a recession, and so does your fund.

The trade-off is symmetric. An index fund will never go to zero because of one company, and it will never triple because of one company either. Owning individual stocks is a choice to take concentrated risk in exchange for the possibility of concentrated return, and it is only sensible when you have done the research that Lessons 5 through 7 describe and are willing to be wrong.

A common structure is a core of one or two broad index ETFs, which is most of the capital, and a smaller sleeve of individual stocks. Whether that split is 90/10 or 60/40 is a personal decision about how much you want to research and how much variance you can tolerate.

## Tax and trading differences

ETFs are generally more tax-efficient than mutual funds in a taxable account because the creation and redemption mechanism lets the fund hand out low-basis shares in kind rather than selling them, so index ETFs rarely distribute capital gains. You still owe tax on dividends the fund pays out and on your own gain when you sell.

Because they trade like stocks, ETFs are subject to everything in Lesson 3: use limit orders, avoid the first minutes after the open when the underlying stocks have not all opened and spreads are wide, and check the spread relative to price. SPY's spread is typically one cent on a 500-dollar-plus price, effectively zero. A thinly traded thematic ETF may show a 20-cent spread on a 25-dollar price, nearly one percent.

## Products to avoid until you understand them

> **Callout:** Leveraged and inverse ETFs reset daily. A 3x fund aims for three times the index's return each day, not over a year. Because of the compounding of daily moves, a volatile sideways market erodes them steadily, and a holding period of months can produce a loss even when the index finishes higher. FINRA and the SEC have both issued warnings on them. They are trading instruments, not investments.

Also treat with care: ETFs with under 50 million dollars in assets (closure risk), commodity ETFs structured as partnerships (K-1 tax forms), and exchange-traded notes, which are unsecured debt of a bank rather than a fund holding assets.

## Table

The three ways to own the S&P 500, and an individual stock for comparison.

| Attribute | Individual stock | Index ETF (for example SPY, VOO, IVV) | Index mutual fund |
| --- | --- | --- | --- |
| What you own | One company | About 500 companies, market-cap weighted | Same |
| Pricing | Continuous, market price | Continuous, market price near NAV | Once daily at NAV |
| Annual cost | None beyond spread | 0.03 to 0.09 percent for the large S&P 500 funds | Similar for index funds; higher for active |
| Company-specific risk | Full | Negligible | Negligible |
| Minimum purchase | One share, or a fraction at many brokers | One share, or a fraction at many brokers | Often a dollar minimum, sometimes 1,000 dollars or more |
| Capital-gains distributions | None until you sell | Rare for index ETFs | Possible each year, even if you did not sell |
| Order types available | All | All | None; you place a buy or sell for NAV |

## Worked example

Three ETFs track the S&P 500. Their expense ratios, from the funds' own prospectuses as of 2024: SPDR S&P 500 ETF Trust (SPY) 0.0945 percent; Vanguard S&P 500 ETF (VOO) 0.03 percent; iShares Core S&P 500 ETF (IVV) 0.03 percent. Add a hypothetical actively managed fund at 0.75 percent, a typical figure for an active equity fund.

Assume 10,000 dollars invested for 30 years and a gross index return of 7 percent per year. The fund's net return is 7 percent minus the expense ratio.

- **VOO or IVV** at 0.03 percent: net 6.97 percent. Ending value: 10,000 × 1.0697^30 ≈ **75,500 dollars**.
- **SPY** at 0.0945 percent: net 6.9055 percent. Ending value: 10,000 × 1.069055^30 ≈ **74,100 dollars**.
- **0.75 percent active fund** (assume it matches the index before fees, which most do not): net 6.25 percent. Ending value: 10,000 × 1.0625^30 ≈ **61,600 dollars**.
- **No fee at all** (the index itself): 10,000 × 1.07^30 ≈ 76,100 dollars.

Reading it:

- The gap between SPY and VOO is about 1,400 dollars over 30 years, under 2 percent of the ending value. Real, but small; SPY's far larger trading volume and tighter options market are why it remains the most-traded ETF despite the higher fee. For a buy-and-hold investor the cheaper fund wins; for someone trading it daily, the liquidity may be worth more than the fee.
- The gap between the 0.03 percent fund and the 0.75 percent fund is about 13,900 dollars, or 18 percent of the ending value. That is the cost of the fee alone, before asking whether the active manager added anything.
- Fees are one of the few things in investing you know in advance with certainty. Returns are not.

## Sources

- SEC Office of Investor Education, "Mutual Funds and Exchange-Traded Funds (ETFs): A Guide for Investors": https://www.investor.gov/introduction-investing/investing-basics/investment-products/mutual-funds-and-exchange-traded-funds-etfs
- FINRA Fund Analyzer (fee comparison tool): https://tools.finra.org/fund_analyzer/
- State Street Global Advisors, SPDR S&P 500 ETF Trust (SPY) fund page and prospectus: https://www.ssga.com/us/en/intermediary/etfs/spdr-sp-500-etf-trust-spy
- Vanguard, Vanguard S&P 500 ETF (VOO) fund page and prospectus: https://investor.vanguard.com/investment-products/etfs/profile/voo
