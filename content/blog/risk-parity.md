---
{"title": "Risk Parity: Sizing Positions Based on Risk, Not Dollars", "cat": "education", "tag": "Education", "emoji": "📘", "excerpt": "Equal dollars are not equal risk. Learn how risk parity sizes positions by volatility, how to approximate it, and where it falls short.", "date": "2026-10-02", "read": "5 min", "status": "published"}
---
Most people size positions in dollars. "I'll put 10% in each of 10 stocks." It feels fair. Every position gets the same slice.

But the same slice of money does not carry the same risk. A volatile growth stock can swing several times more than a steady utility. Put 10% in each and the volatile one drives most of your day-to-day results.

Risk parity is a way to fix that. You size each position by how much risk it adds, not by how many dollars it uses.

## Dollars versus risk

Here is a simple example. You own two stocks.

- Stock A has annualized volatility of 40%.
- Stock B has annualized volatility of 20%.

Split your money 50/50. Stock A's standalone risk is 0.5 × 40 = 20. Stock B's is 0.5 × 20 = 10. Stock A carries two-thirds of that risk while using only half your money.

Now size them by the inverse of their volatility. Weight A by 1/40 and B by 1/20, then scale so the weights add to 100%. You get about 33% in A and 67% in B.

Check the risk. A is 0.333 × 40 ≈ 13.3. B is 0.667 × 20 ≈ 13.3. Each position now carries the same standalone risk. That is the core idea of risk parity.

## What risk parity actually means

Risk parity aims for each holding to contribute equally to total portfolio risk. Riskier positions get smaller weights. Calmer positions get larger ones.

The version above is called inverse-volatility weighting. It is the simple form. It ignores how positions move together.

The full version is called equal risk contribution. It accounts for correlation. A position that moves with everything else adds more risk than its own volatility suggests. A position that zigs when others zag adds less.

Maillard, Roncalli and Teïletche studied this approach in a 2010 paper. They showed that the volatility of an equal risk contribution portfolio sits between two familiar portfolios. It is no lower than the minimum-variance portfolio and no higher than the equal-weight portfolio. In other words, it is a middle ground between chasing the lowest risk and splitting money evenly.

## Volatility, not just beta

You may see people use beta for this. Beta measures how much a stock tends to move with the overall market. That is useful, but it misses part of the picture.

A stock can have a modest beta and still swing wildly on its own news. Volatility captures both market risk and company-specific risk. That is why most risk parity methods start with volatility.

Beta and volatility also change over time. A number you read once can be stale a few months later. Recompute on a schedule.

## How professional funds use it

Institutional risk parity usually works across asset classes, not single stocks. Think stocks, bonds and commodities.

Bonds are usually less volatile than stocks. So an equal-risk portfolio ends up holding much more in bonds. That can mean lower expected returns. To lift returns, many risk parity funds use leverage on the whole portfolio.

Asness, Frazzini and Pedersen explored why this can work in a 2012 paper. Their argument is that many investors avoid leverage. Instead, they reach for higher returns by overweighting risky assets. That may leave safer assets with better returns per unit of risk. Risk parity tries to capture that gap.

Leverage brings its own risks. Borrowing costs rise. Margin calls can force selling at bad times. You do not need leverage to use the core idea in your own sizing.

## A practical way to approximate it

You do not need a perfect model to benefit. A rough version helps.

1. **Measure volatility.** Take daily returns for each holding over a set period, such as the last 60 or 90 trading days. Compute the standard deviation. Multiply by the square root of 252 to annualize.
2. **Invert it.** For each holding, compute 1 divided by its volatility.
3. **Scale to 100%.** Divide each inverse by the sum of all inverses. Those are your target weights.
4. **Set a cap.** Very calm assets can end up with huge weights. Cap any single position at a level you are comfortable with.
5. **Rebalance on a schedule.** Monthly or quarterly is common. More often adds trading costs and, in a taxable account, possible taxes.

The SEC's investor guide on rebalancing makes a related point. Before you rebalance, consider transaction fees and tax consequences.

## Where risk parity falls short

Risk parity is a sizing rule, not a crystal ball. Know its limits.

**It looks backward.** Volatility estimates come from the past. A calm stock can turn volatile fast, often right when it matters.

**Correlations change.** In a sell-off, assets that usually move separately can fall together. Your diversification can shrink just when you need it.

**Low volatility is not the same as safe.** A bond can have low daily volatility and still lose value when interest rates rise. Stocks and bonds can fall at the same time.

**It ignores expected returns.** Risk parity sizes by risk alone. It does not ask whether a position is a good idea. You still need a reason to own each holding.

## The takeaway

Equal dollars are not equal risk. If one or two volatile names drive most of your swings, your portfolio is less diversified than it looks.

Start simple. Measure each holding's volatility. Shift weight away from the wildest names and toward steadier ones. Rebalance on a schedule. You will end up with a portfolio where no single position dominates your results.

For more on measuring exposure, see the free opening lessons of Portfolio Risk Management on our Courses page.

## Sources

- Maillard, S., Roncalli, T., & Teïletche, J. (2010). "The Properties of Equally Weighted Risk Contribution Portfolios." *Journal of Portfolio Management*, 36(4), 60–70.
- Asness, C. S., Frazzini, A., & Pedersen, L. H. (2012). "Leverage Aversion and Risk Parity." *Financial Analysts Journal*, 68(1), 47–59.
- U.S. Securities and Exchange Commission. "Beginners' Guide to Asset Allocation, Diversification, and Rebalancing." Investor.gov. https://www.investor.gov/additional-resources/general-resources/publications-research/info-sheets/beginners-guide-asset

*Educational content, not financial advice.*
