---
{
  "title": "Cost Basis Methods and Netting Capital Losses",
  "duration": "16 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "You hold three lots of the same ETF and sell part of the position without telling your broker which lot to sell. Under Publication 550 the shares sold are:", "opts": ["The lot with the highest cost", "The lot with the lowest cost", "The shares you acquired first (FIFO)", "Whichever lot the broker chooses at year end"], "correct": 2, "explain": "Pub. 550, Identifying stock or bonds sold: if you cannot adequately identify the shares you sold, the basis of the securities you sell is the basis of the securities you acquired first."},
    {"q": "Specific identification of a lot at the time of sale is adequate if:", "opts": ["You note the lot in your own spreadsheet after the sale", "You tell the broker which shares to sell at the time of the sale and receive written confirmation within a reasonable time", "You use the average basis on your return", "The broker's default method is FIFO"], "correct": 1, "explain": "Pub. 550: you adequately identify shares held by a broker if, at the time of sale, you specify to the broker the particular shares to be sold and, within a reasonable time, the broker confirms that specification in writing."},
    {"q": "The average basis method may be used for:", "opts": ["Any listed stock", "Individual stocks and ETFs held in a margin account", "Mutual fund shares and shares acquired through a dividend reinvestment plan after 2011 and left with a custodian", "Only section 1256 contracts"], "correct": 2, "explain": "Pub. 550 limits average basis to identical shares acquired at different times and prices and left with a custodian that are either mutual fund (regulated investment company) shares or shares acquired after 2011 in a dividend reinvestment plan."},
    {"q": "For tax year 2025 a net capital loss can reduce ordinary income by at most:", "opts": ["$3,000 ($1,500 if married filing separately), with the rest carried forward", "$10,000 per year", "Any amount, if you are an active trader", "Nothing; capital losses only offset capital gains"], "correct": 0, "explain": "IRC section 1211(b) allows capital losses against capital gains plus the lower of $3,000 ($1,500 married filing separately) or the excess of losses over gains. Section 1212(b) carries the remainder forward with its character."},
    {"q": "In the worked example the net short-term loss was $5,500 and the net long-term gain was $1,200. The carryforward to 2026 is:", "opts": ["$4,300 long-term", "$1,300 short-term", "$5,500 short-term", "$2,500 long-term"], "correct": 1, "explain": "Net the two: $5,500 loss less $1,200 gain is a $4,300 net capital loss. $3,000 is deducted in 2025 and the $1,300 remainder carries forward as a short-term loss under section 1212(b), because it came from the excess of net short-term loss over net long-term gain."}
  ],
  "task": "Log in to your broker, find the default cost-basis method on each account and the setting for identifying lots at the time of sale, and write both down."
}
---

## Why basis comes before rates

Lesson 1 assumed you knew the gain. In practice the gain is whatever proceeds exceed your adjusted basis, and for a position built in several purchases the basis of the shares you sold is a choice, made at the moment of sale, that changes this year's bill and next year's. IRC section 1012 sets basis at cost; section 1011 adjusts it for events such as wash-sale disallowances (lesson 3) and return-of-capital distributions. The Form 8949 instructions require you to report the basis your broker reported in column (e) and to fix any error in column (g), so you need to know which method the broker applied.

## FIFO, the default

Publication 550, under Identifying stock or bonds sold, states the default: if you buy and sell securities at various times in varying quantities and you cannot adequately identify the shares you sell, the basis of the securities you sell is the basis of the securities you acquired first. First in, first out is what every broker applies unless you instruct otherwise. In a rising market it sells your oldest, cheapest shares first and produces the largest gain; it also tends to produce long-term gains, because the oldest shares are the ones most likely to have passed the one-year mark. Neither effect is good or bad on its own.

## Specific identification

Publication 550 also says that if you can adequately identify the shares you sold, their basis is the cost of those particular shares. For shares held by a broker, you adequately identify them if, at the time of the sale, you specify to the broker the particular shares to be sold and, within a reasonable time, the broker confirms that specification in writing. The confirmation can be electronic. Most brokers expose this as a lot-selection screen on the order ticket or as a standing instruction such as highest cost first. The identification must happen at or before the sale; you cannot re-designate lots when you prepare the return the following spring. Treasury Regulation section 1.1012-1(c) carries the same rule and adds that a standing order is acceptable.

Specific identification lets you sell the highest-cost lot to minimise a gain, or a long-term lot rather than a short-term one, or a loss lot to offset a gain elsewhere. It is the mechanism behind every harvesting decision in lesson 4.

## Average basis, for funds only

The average basis method divides the total basis of all identical shares in an account by the number of shares. Publication 550 restricts it to identical shares acquired at different times and prices and left with a custodian that are either shares of a mutual fund (a regulated investment company) or shares acquired after 2011 through a dividend reinvestment plan. For covered securities you elect it by written notice to the broker and it applies to sales after the notice; for noncovered securities you elect it on the return by using it. Once you use average basis for a fund, you cannot switch that fund back to cost basis except by revoking within the window Pub. 550 describes. Exchange-traded funds organised as regulated investment companies can qualify; individual stocks cannot. If your broker offers average cost on a stock position, that is a reporting convenience, not a tax method, and the return must use FIFO or specific identification.

## Netting: the order of operations

Once every sale has a gain or loss and a holding period, Schedule D nets them in a fixed order. Short-term gains and losses are combined in Part I to a net short-term figure; long-term gains and losses are combined in Part II to a net long-term figure. If one is a gain and the other a loss, they are netted against each other. What survives is either net capital gain, taxed as in lesson 1, or a net capital loss.

IRC section 1211(b) limits the loss: capital losses are allowed to the extent of capital gains plus the lower of $3,000 ($1,500 for a married person filing separately) or the excess of the losses over the gains. The $3,000 is written into the statute and is not indexed for inflation, which is why it feels small. Section 1212(b) carries the unused amount to the next year and preserves its character: the excess of net short-term loss over net long-term gain carries as a short-term loss, and the excess of net long-term loss over net short-term gain carries as a long-term loss. The $3,000 deducted is treated as absorbing short-term loss first. Carryforwards do not expire while you live; the Schedule D instructions' Capital Loss Carryover Worksheet recomputes them each year. They cannot be transferred to your estate or heirs.

## Worked example

Cost basis. You bought QQQ in three lots during 2025, each at the Yahoo Finance daily close: 50 shares on 2025-01-06 at $524.54 (basis $26,227.00); 50 shares on 2025-04-07 at $423.69 (basis $21,184.50); 50 shares on 2025-06-02 at $523.21 (basis $26,160.50). On 2025-11-03 you sold 50 shares at the close of $632.08, proceeds $31,604.00. Every lot was held one year or less, so the gain is short-term whichever lot is chosen.

Under FIFO the broker sells the 2025-01-06 lot: gain = $31,604.00 − $26,227.00 = $5,377.00. If you had specified the highest-cost lot, which is the same January lot here, the answer is the same $5,377.00. If you had specified the 2025-06-02 lot: $31,604.00 − $26,160.50 = $5,443.50, slightly worse. If you had (unwisely) specified the April lot: $31,604.00 − $21,184.50 = $10,419.50, nearly double the taxable gain. At a 24% marginal rate the difference between the January lot and the April lot is ($10,419.50 − $5,377.00) × 0.24 = $1,210.20 of 2025 tax.

If these had been mutual fund shares and you had elected average basis, the average would be ($26,227.00 + $21,184.50 + $26,160.50) ÷ 150 = $73,572.00 ÷ 150 = $490.48 per share, and the gain on 50 shares would be $31,604.00 − $24,524.00 = $7,080.00. Note that the method only moves gain between years: the 100 shares still held carry the remaining basis, $47,345.00 under FIFO or $49,048.00 under average, so the total gain over the life of the position is identical.

Netting. Suppose your whole 2025 year, after basis is settled, comes to: short-term gains $9,200; short-term losses $14,700; long-term gains $6,100; long-term losses $4,900. Part I nets to $9,200 − $14,700 = −$5,500. Part II nets to $6,100 − $4,900 = +$1,200. Netting the two gives a net capital loss of $4,300. Section 1211(b) allows $3,000 of it against 2025 ordinary income on Form 1040 line 7. The remaining $1,300 carries to 2026. Its character: the excess of the net short-term loss ($5,500) over the net long-term gain ($1,200) is $4,300; the $3,000 deducted is treated as reducing that short-term figure, leaving a $1,300 short-term loss carryover and no long-term carryover. At a 24% marginal rate the $3,000 deduction saved $720 in 2025; the $1,300 will save whatever rate applies when it is used.

## Table

| Method | Who may use it | When you choose | 2025-11-03 QQQ sale: gain on 50 shares |
|---|---|---|---|
| FIFO | Everyone; the default when no lot is identified | Automatic | $5,377.00 (2025-01-06 lot) |
| Specific identification | Anyone holding identifiable lots | At or before the sale, confirmed in writing by the broker | $5,377.00 to $10,419.50 depending on lot |
| Average basis | Mutual fund shares; DRIP shares acquired after 2011 | Written notice to broker (covered) or on the return (noncovered) | $7,080.00 if the shares were fund shares |
| Loss netting | Everyone | Fixed order on Schedule D | Net loss $4,300; deduct $3,000; carry $1,300 short-term |

Sources: Pub. 550 (Identifying stock or bonds sold; Average Basis); IRC sections 1211(b) and 1212(b); Instructions for Schedule D (Form 1040), 2025.

## Practical notes

Set the lot-identification default on every account now, before you need it; a standing instruction of highest cost first is accepted by Reg. 1.1012-1(c)(8) and most brokers. When you transfer a position between brokers, the basis follows it under the cost-basis reporting rules for covered securities (acquired after 2010 for stock), but noncovered lots arrive with no basis and you must supply it from your own records. Remember that a carryforward is only useful against future gains or $3,000 a year of ordinary income, so a trader who realises large losses in a bad year and then stops trading may carry them for a very long time.

## Sources

- IRS Publication 550, Investment Income and Expenses (Identifying stock or bonds sold; Average Basis; Capital Losses): https://www.irs.gov/publications/p550
- IRC section 1211, Limitation on capital losses: https://www.law.cornell.edu/uscode/text/26/1211
- IRC section 1212, Capital loss carrybacks and carryovers: https://www.law.cornell.edu/uscode/text/26/1212
- Instructions for Schedule D (Form 1040), 2025, Capital Loss Carryover Worksheet: https://www.irs.gov/instructions/i1040sd
