---
{
  "title": "Valuation Basics: P/E, P/S and EV/EBITDA",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "A stock trades at 250 dollars with trailing diluted EPS of 6.08 dollars. Its trailing P/E is closest to:", "opts": ["4.1", "24", "41", "62"], "correct": 2, "explain": "250 divided by 6.08 is about 41. The earnings yield, the inverse, is about 2.4 percent."},
    {"q": "Which ratio is most useful for a company that currently has negative earnings?", "opts": ["Trailing P/E", "Price-to-sales", "Dividend yield", "PEG"], "correct": 1, "explain": "P/E is undefined or meaningless when earnings are negative. P/S still works, though it ignores whether the company can ever convert sales into profit."},
    {"q": "Enterprise value differs from market capitalisation because it:", "opts": ["Excludes preferred stock", "Adds debt and subtracts cash, to reflect what a buyer of the whole company would pay", "Uses float instead of shares outstanding", "Is calculated using book value"], "correct": 1, "explain": "EV equals market cap plus debt minus cash. A company with large net cash has an EV below its market cap; a leveraged company has an EV well above it."},
    {"q": "A cyclical steel company shows a P/E of 5 at the top of a boom. The most likely explanation is:", "opts": ["The stock is a bargain", "The market expects earnings to fall sharply, so the low multiple reflects peak earnings", "The company has no debt", "The data is wrong"], "correct": 1, "explain": "Cyclicals look cheapest on P/E when earnings peak and most expensive when earnings trough. The multiple is pricing the cycle, not the current number."},
    {"q": "EV/EBITDA tends to flatter which kind of business?", "opts": ["A software company with no debt", "A capital-intensive business whose depreciation is a real, recurring cost", "A bank", "A company with a large cash pile"], "correct": 1, "explain": "EBITDA adds back depreciation. For businesses that must continually replace assets, that add-back hides a real cash cost and makes the company look cheaper than it is."}
  ],
  "task": "Compute trailing P/E, P/S and EV/EBITDA for one company you follow using its latest 10-K and the current price, and note which of the three you trust least and why."
}
---

## A ratio is a question, not an answer

Every valuation ratio divides a price by a measure of the business. The result tells you how many dollars the market pays for one dollar of that measure. It does not tell you whether that is too many or too few. A P/E of 41 for a company that will grow earnings 20 percent a year for a decade may be cheap; a P/E of 8 for a company whose earnings are about to halve is expensive. The ratio's job is to make you ask "what would have to be true for this price to make sense?" and then go check.

This lesson covers the three ratios you will see most often, shows how to compute each from a real filing, and, most importantly, lists the situations in which each one lies.

## Price-to-earnings

P/E = share price ÷ earnings per share.

Equivalently, market cap ÷ net income. Its inverse, the **earnings yield**, is EPS ÷ price, and is the most intuitive form: a P/E of 20 is a 5 percent earnings yield, directly comparable to a bond yield.

Two versions:

- **Trailing P/E** uses the last four reported quarters (trailing twelve months, TTM). It is factual and backward-looking.
- **Forward P/E** uses the consensus estimate for the next four quarters or the next fiscal year. It is what the market actually prices on, and it is only as good as the estimate.

Also specify GAAP or adjusted EPS. Most screens default to adjusted, which is usually higher, producing a lower and more flattering P/E.

**When P/E lies:**

- **Negative or tiny earnings.** A company earning one cent per share at 50 dollars has a P/E of 5,000. Meaningless.
- **One-time items.** A large charge or gain in the trailing period distorts it for a full year. Apple's fiscal 2024 is the worked example below.
- **Cyclical peaks and troughs.** Commodity producers, homebuilders and automakers look cheapest at the top of the cycle and most expensive at the bottom. The market prices the cycle, not the quarter.
- **Different capital structures.** P/E ignores debt entirely. Two companies with the same P/E can carry wildly different risk.
- **Buybacks funded by debt.** EPS rises while net income does not. P/E falls while the business is unchanged and more leveraged.

## Price-to-sales

P/S = market cap ÷ trailing twelve-month revenue.

It works when earnings do not: early-stage companies, companies in a temporary loss, or companies where accounting choices make earnings unreliable. Because revenue is harder to manipulate than earnings, it is also a useful sanity check.

**When P/S lies:**

- **It ignores margins.** A grocer with 2 percent net margins and a software company with 30 percent net margins both at 1.0 times sales are not equally cheap; the software company is earning fifteen times as much per dollar of revenue.
- **It ignores debt**, like P/E.
- **Revenue recognition.** Gross versus net reporting (a marketplace booking the full transaction value versus only its fee) can change revenue tenfold without changing the business.
- **It says nothing about whether profitability will ever arrive.** A company at 2 times sales that will never earn a profit is infinitely expensive.

## Enterprise value and EV/EBITDA

Enterprise value = market cap + total debt − cash and marketable securities (plus preferred stock and minority interest, when present).

EV is what it would cost to buy the entire company and settle its debts using its own cash. It is the right numerator whenever you want to compare companies with different balance sheets.

EBITDA = earnings before interest, taxes, depreciation and amortisation. In practice: operating income plus depreciation and amortisation, taken from the cash flow statement. It approximates the cash operating profit available to all capital providers, before the effects of financing choices and accounting for past investment.

EV/EBITDA is the standard multiple in acquisitions and in capital-structure-neutral comparisons. A company with a lot of net cash has an EV below its market cap, and EV/EBITDA will show it as cheaper than P/E suggests; a leveraged company shows the opposite.

**When EV/EBITDA lies:**

- **Depreciation is real.** For airlines, telecoms, shipping, retailers with leases and any capital-intensive business, the assets wear out and must be replaced. Adding back depreciation removes a genuine recurring cash cost. Use EV to EBIT or free cash flow instead.
- **Leases.** Since 2019, most leases sit on the balance sheet as debt. Whether you include lease liabilities in EV, and lease expense in EBITDA, must be consistent or the ratio is nonsense.
- **Stock-based compensation.** Not in EBITDA if the company excludes it, yet it dilutes you every year.
- **Banks and insurers.** Interest is their revenue, and debt is their raw material. EV and EBITDA are meaningless for financials; use price-to-book and return on equity.

## Comparing against what

A ratio in isolation means little. Three comparisons make it useful:

1. **Against the company's own history.** A stock at 30 times earnings that has averaged 20 over ten years is being paid for something new, and you should know what.
2. **Against sector peers.** Lesson 4 gave you the GICS sector. Compare within it. Cross-sector comparison of multiples is mostly noise.
3. **Against growth.** The PEG ratio (P/E divided by expected annual earnings growth in percent) is a crude adjustment: 41 times earnings with 20 percent growth is a PEG of about 2; 15 times with 3 percent growth is a PEG of 5. Crude, but it forces the question of what growth the price implies.

## Table

The three ratios, what each measures, and the failure mode to check first.

| Ratio | Formula | Best for | Fails when | First thing to check |
| --- | --- | --- | --- | --- |
| P/E | Price ÷ EPS | Profitable, stable, low-debt companies | Earnings negative, one-time items, cyclical peak, heavy debt | Are there one-time items in the trailing twelve months? |
| P/S | Market cap ÷ revenue | Loss-making or early-stage companies; sanity check | Margins differ across peers; gross versus net revenue | What is the net margin, and is it going to improve? |
| EV/EBITDA | (Market cap + debt − cash) ÷ (operating income + D&A) | Comparing companies with different balance sheets; acquisitions | Capital-intensive businesses, leases, banks | How large is capex relative to depreciation? |

## Worked example

Apple at the close of 31 December 2024, using the fiscal 2024 Form 10-K (year ended 28 September 2024) for all financial figures.

**Inputs.**
- Price: 250.42 dollars. Shares outstanding: 15,115,823,000. Market cap: 3,785 billion dollars.
- Fiscal 2024 revenue: 391.0 billion dollars.
- Fiscal 2024 net income: 93.7 billion dollars. Diluted EPS: 6.08 dollars.
- Operating income: 123.2 billion dollars. Depreciation and amortisation (cash flow statement): 11.4 billion dollars. EBITDA: 134.6 billion.
- Cash and marketable securities: about 156.7 billion. Total debt (commercial paper plus term debt): about 106.6 billion. Net cash: about 50.1 billion.

**Ratios.**
- Trailing P/E: 250.42 ÷ 6.08 = **41.2**. Earnings yield 2.4 percent.
- P/S: 3,785 ÷ 391.0 = **9.7**.
- Enterprise value: 3,785 − 50.1 = 3,735 billion. EV/EBITDA: 3,735 ÷ 134.6 = **27.7**.

**Where the P/E lies.** Fiscal 2024 net income included a one-time tax charge of 10.2 billion dollars (the European State Aid decision, covered in Lesson 6). Underlying net income was about 103.9 billion, or roughly 6.75 dollars per diluted share. On that basis the P/E is 250.42 ÷ 6.75 = **37.1**, four points lower. Neither number is "right"; the point is that a screen showing 41 and a screen showing 37 are both describing the same company, and you should know which one you are looking at.

**Where EV/EBITDA helps.** Apple's net cash reduces EV below market cap by about 1.3 percent, a small effect for Apple but a large one for a company whose cash is 30 percent of its market cap. EBITDA of 134.6 billion against operating income of 123.2 billion means depreciation is under 10 percent of operating profit; Apple is not capital-intensive, so EV/EBITDA does not flatter it much. For a telecom with D&A equal to half of operating income, the same ratio would be hiding a great deal.

**The question the ratios pose.** At 37 to 41 times earnings, with revenue growing 2 percent in fiscal 2024, the price implies that the market expects meaningfully faster growth ahead, continued margin expansion from Services, and continued share-count reduction, or it is paying a premium for safety. Whether those expectations are reasonable is the research. The ratio only told you what to research.

## Sources

- SEC Office of Investor Education, glossary entry "Price-Earnings (P/E) Ratio": https://www.investor.gov/introduction-investing/investing-basics/glossary/price-earnings-pe-ratio
- Apple Inc., Form 10-K for the fiscal year ended 28 September 2024 (EDGAR, CIK 0000320193): https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000320193&type=10-K
- SEC, Regulation G, Conditions for Use of Non-GAAP Financial Measures (EBITDA and adjusted earnings reconciliations): https://www.sec.gov/rules/final/33-8176.htm
- FINRA, "Evaluating Stocks": https://www.finra.org/investors/investing/investment-products/stocks/evaluating-stocks
