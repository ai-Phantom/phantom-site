---
{
  "title": "Capstone: Three Companies, One Page Each",
  "duration": "20 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Which source satisfies the capstone's requirement to read a filing section?", "opts": ["A finance website's summary of the company", "The MD&A or Risk Factors section of the company's 10-K or 10-Q on EDGAR", "A YouTube video about the stock", "The company's marketing home page"], "correct": 1, "explain": "The exercise requires the primary document. Summaries and commentary are not filings, and the rubric awards no points for them."},
    {"q": "Your three companies are Nvidia, AMD and Broadcom. What rubric criterion do you fail?", "opts": ["Data provenance", "Sector diversity: all three are in the same GICS sector and industry", "Position sizing", "Exit rule"], "correct": 1, "explain": "The exercise requires three different GICS sectors. Three semiconductor names is one bet written three times."},
    {"q": "A submission states 'buy at around 60 and sell when it feels right'. Which criteria does it fail?", "opts": ["Only the entry", "Only the exit", "Both the entry and the exit rule, because neither is a specific, checkable number or date", "Neither; the thesis is what matters"], "correct": 2, "explain": "Every price in the plan must be a number with an order type, and the exit must be a price or a date. Vague language scores zero on those criteria."},
    {"q": "On a stated 10,000 dollar paper account with a 1 percent risk rule, a submission proposes 100 shares at 62.26 with a stop at 58.52. What is wrong?", "opts": ["Nothing", "The loss at the stop is 374 dollars, nearly four times the 100 dollar risk budget; the rule allows 26 shares", "The stop is too tight", "The account is too small to trade"], "correct": 1, "explain": "100 shares times a 3.74 dollar stop distance is 374 dollars of risk. The sizing formula, 100 divided by 3.74, gives 26 shares rounded down."},
    {"q": "Why must every number in the thesis carry a source and a date?", "opts": ["To make the page longer", "Because a reader, including you in six months, must be able to check whether the number was true and whether it has changed", "Because the SEC requires it", "Because prices never change"], "correct": 1, "explain": "Provenance is what turns an opinion into a checkable claim. A number with no source and no date cannot be verified or updated, and the rubric scores it as absent."}
  ],
  "task": "Submit three one-page theses, each with a sourced quote, a sourced filing excerpt, a position size on a stated paper account, and a written exit rule."
}
---

## The exercise

You will produce three one-page documents, one per company, each built entirely from primary sources and each ending in a trade plan you could execute tomorrow in a paper account. Everything you need was covered in Lessons 1 through 12. This page tells you exactly what to produce, gives a fully worked example, and shows the rubric your work will be scored against.

Time budget: roughly 90 minutes per company the first time. It gets faster.

## Step 1: choose three companies

Constraints, all mandatory:

- Three different GICS sectors (Lesson 4).
- Market capitalisation above 2 billion dollars.
- Average daily volume above one million shares.
- US-listed, filing 10-Ks and 10-Qs with the SEC (foreign private issuers file 20-Fs, which are fine to read but change the section names; avoid them for this exercise).
- At least one must pay a dividend, so that you practise the yield and payout arithmetic.

Write down, for each, why it is on your list in one sentence, before you open a single filing. You will compare that sentence to your final thesis; the difference is what you learned.

## Step 2: pull one quote per company

From your broker or an exchange data page, record for each company on the same day:

- Date and time of the quote, and the source
- Last price, bid, ask, bid size, ask size
- Day's volume and average daily volume
- Market capitalisation and shares outstanding
- 52-week high and low

Compute the spread in basis points (Lesson 2). If any of these fields is missing from your source, find one that shows them; a quote without a bid and ask is a headline, not a quote.

## Step 3: read one filing section per company

Go to EDGAR (sec.gov/edgar/search) and open the most recent 10-K or 10-Q. Read one of:

- **Item 7 (10-K) or Part I Item 2 (10-Q), Management's Discussion and Analysis**, or
- **Item 1A, Risk Factors.**

From MD&A, extract: revenue, the year-over-year change and the reasons management gives; gross margin and operating margin; one sentence about liquidity (cash, debt, buybacks or dividends). From Risk Factors, extract the one risk that is most specific to this company, not to every company, quoted in under 40 words with the page or section reference.

Also record from the same filing: diluted EPS for the trailing year (or the last four quarters), total cash and marketable securities, total debt, and diluted share count. You need these for Step 4.

## Step 4: compute the ratios

Using the quote from Step 2 and the filing from Step 3, compute trailing P/E, P/S and EV/EBITDA (Lesson 7), and, for the dividend payer, yield and payout ratio (Lesson 8). Show the arithmetic, not just the result. Note any one-time item that distorts the P/E, and show the adjusted figure alongside.

## Step 5: write the page

One page each, in this order, with no section longer than it needs to be:

1. **Header.** Company, ticker, sector, market cap bucket, date.
2. **Thesis.** Three sentences maximum: what you expect to happen to the business over your horizon, why the current price does not already reflect it, and the single observable number that would prove you wrong.
3. **Evidence.** Bullet list. Each bullet is one number, its source (filing, item and page, or quote source and timestamp), and its date. Include the ratios from Step 4 and the filing extract from Step 3.
4. **Plan.** Entry price and order type with time-in-force. Stop price. Position size, derived from a stated paper account size and risk percentage, with the formula shown. Exit for a gain (target price) or a time limit, or both. Review date.
5. **What I do not know.** Two or three sentences on the biggest gap in your understanding. Honesty here scores; false confidence does not.

## Step 6: size the whole set

Across the three positions, state the total capital deployed and the total open risk as percentages of the paper account, and confirm both are under your caps (Lesson 12). A set of three excellent single-page plans that together risk 15 percent of the account fails the exercise.

## Chart

Picture a horizontal stacked bar representing a 10,000 dollar paper account. Three coloured segments from the left show capital deployed in each position; the grey remainder is cash. Below it, a second, much shorter bar shows open risk: three thin segments, one per position, each the shares multiplied by the distance to the stop. For the worked example in Lesson 12, the top bar reads 1,503 (AAPL), 1,265 (MSFT) and 1,619 (KO) against 5,614 of cash, and the risk bar reads 90, 76 and 97 dollars, totalling 263 dollars against a 500 dollar cap drawn as a vertical line. Your submission should be describable the same way: three segments of similar height on the risk bar, none crossing the cap line. If one segment dwarfs the others, the sizing formula was not applied.

## Worked example

This is a complete page for one company, built from data as of 31 December 2024. Your pages should match this structure. Where this example uses that date's figures, yours must use current ones.

**Header.** The Coca-Cola Company (KO). Consumer Staples. Mega-cap. 31 December 2024.

**Thesis.** Coca-Cola is an income holding: a global beverage franchise growing revenue in the mid single digits with a 79 percent payout ratio and a 3.1 percent yield, backed by 62 consecutive years of dividend increases. The price already reflects the stability, so the expected return is roughly the yield plus mid-single-digit growth, not a re-rating. The thesis is wrong if organic revenue growth turns negative for two consecutive quarters or the dividend is not raised in February 2025.

**Evidence.**
- Quote: close 62.26 dollars, 31 December 2024, official closing auction price (source: NYSE closing price as reported by the broker). Typical spread one cent, 1.6 basis points. Approximately 4.31 billion shares outstanding; market cap about 268 billion dollars.
- 2024 Form 10-K, Item 8: net operating revenues 47.1 billion dollars; net income attributable to shareowners 10.6 billion; diluted EPS 2.46 dollars. (Filed February 2025; at 31 December 2024 the most recent filing was the third-quarter 10-Q, and the full-year figures here are used for clarity.)
- 2024 Form 10-K, Item 7 (MD&A): management attributes revenue growth to price and mix, partly offset by currency and the refranchising of bottling operations.
- 2024 Form 10-K, Item 1A: the company discloses ongoing litigation with the IRS over transfer pricing for tax years 2007 to 2009 and later years, and made a 6.0 billion dollar tax deposit in 2024 while appealing. This is the most company-specific risk on the list; an adverse final outcome would be a multi-billion-dollar cash cost.
- Dividend: 0.485 dollars quarterly during 2024, 1.94 dollars annualised. Yield: 1.94 ÷ 62.26 = 3.1 percent. Payout ratio: 1.94 ÷ 2.46 = 79 percent.
- Trailing P/E: 62.26 ÷ 2.46 = 25.3. P/S: 268 ÷ 47.1 = 5.7.

**Plan.** Paper account 10,000 dollars; risk per trade 1 percent (100 dollars); position cap 20 percent. Entry: limit buy at 62.26, good-till-cancelled. Stop: sell stop at 58.52 (6 percent below entry). Risk per share: 3.74 dollars. Size: 100 ÷ 3.74 = 26.7, rounded down to 26 shares; position value 1,618.76 dollars (16 percent of the account, within the cap); loss at stop 97.24 dollars. Exit: reassess at 70.00 dollars, or hold through two earnings reports, whichever comes first. Review date: 11 February 2025, fourth-quarter results, checking specifically for the dividend increase and organic growth.

**What I do not know.** I cannot estimate the probability or size of the IRS outcome; the 6.0 billion dollar deposit is the only hard number, and the company's own filings do not put a range on the final liability. I also do not know how much of the 2024 revenue growth was price rather than volume, which matters for whether growth is durable; the 10-K discusses both but I have not built the split.

That page is under 400 words, every number has a source and a date, and the plan could be entered in a paper account in two minutes. Produce three of them.

## Rubric

Scored out of 100. A submission below 70 is returned with the failing criteria marked; resubmit after fixing them.

| Criterion | Points | Full marks require | Zero marks if |
| --- | --- | --- | --- |
| Company selection | 10 | Three different GICS sectors; each above 2 billion dollars and one million shares per day; at least one dividend payer; selection reason stated for each | Two companies share a sector, or any fails the size or liquidity filter |
| Quote and data provenance | 20 | Every number on the page carries a source and a date; the quote includes bid, ask, sizes, volume and spread in basis points | Any number without a source, or a quote lacking bid and ask |
| Filing reading | 20 | A specific extract from MD&A or Risk Factors, with item and page, that is particular to the company and is used in the thesis | Extract is generic boilerplate, from a summary site, or absent |
| Ratios and arithmetic | 15 | P/E, P/S and EV/EBITDA shown with working; one-time items identified and an adjusted P/E given; yield and payout for the dividend payer | Ratios copied from a website without working, or arithmetic errors |
| Position size and portfolio risk | 20 | Stated account and risk percentage; shares derived from the stop with the formula shown; position and total open risk under stated caps | Size not derived from the stop, or total risk exceeds the caps |
| Exit rule and review date | 15 | A stop price, a target price or time limit, and a review date tied to a scheduled event; the thesis names the number that would prove it wrong | Any of the three is missing or expressed as a feeling rather than a number or date |

## Sources

- SEC, EDGAR Full-Text Search: https://www.sec.gov/edgar/search/
- SEC Office of Investor Education, "How to Read a 10-K/10-Q": https://www.sec.gov/files/reada10k.pdf
- The Coca-Cola Company, Form 10-K for the fiscal year ended 31 December 2024 (EDGAR, CIK 0000021344): https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000021344&type=10-K
- FINRA, "Asset Allocation and Diversification": https://www.finra.org/investors/investing/investing-basics/asset-allocation-diversification
