---
{
  "title": "Reading an Earnings Report and Guidance",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Which section of a Form 10-K contains management's own narrative explanation of why results changed?", "opts": ["Item 1, Business", "Item 1A, Risk Factors", "Item 7, Management's Discussion and Analysis", "Item 9A, Controls and Procedures"], "correct": 2, "explain": "MD&A (Item 7) is where management explains revenue and margin drivers, liquidity, and known trends. It is the most useful section for a first read."},
    {"q": "Apple's fiscal 2024 net income was 93.7 billion dollars including a 10.2 billion dollar one-time tax charge. Excluding the charge, net income would have been closest to:", "opts": ["83.5 billion", "93.7 billion", "103.9 billion", "114.1 billion"], "correct": 2, "explain": "93.7 plus 10.2 equals 103.9 billion dollars. Adding back a one-time charge is the simplest normalisation and the first one to check."},
    {"q": "A company reports adjusted EPS of 3.00 and GAAP EPS of 1.20. What must it provide under Regulation G?", "opts": ["An auditor's letter approving the adjustment", "A reconciliation showing each item that bridges GAAP to the adjusted figure", "A restated prior-year figure", "Nothing, adjusted figures are unregulated"], "correct": 1, "explain": "Reg G requires a quantitative reconciliation. Read it: recurring items labelled one-time are the main way adjusted numbers mislead."},
    {"q": "Gross margin is:", "opts": ["Revenue minus all expenses", "Revenue minus cost of sales, usually expressed as a percentage of revenue", "Operating income minus taxes", "Net income divided by shares"], "correct": 1, "explain": "Gross margin measures what is left after the direct cost of producing what was sold. Apple's fiscal 2024 gross margin was 46.2 percent."},
    {"q": "Guidance of 'revenue growth in the low-to-mid single digits' with a gross margin range of 46 to 47 percent tells you:", "opts": ["Exactly what next quarter's EPS will be", "The company's expectations for the top line and one key margin, which you must combine with share count and tax rate to estimate EPS", "That the company will beat consensus", "Nothing useful"], "correct": 1, "explain": "Guidance gives the inputs, not the answer. Building the estimate yourself is how you learn whether the consensus is reasonable."}
  ],
  "task": "Open the most recent 10-Q of a company you follow on EDGAR, read Item 2 (MD&A) and write down the two reasons management gives for the change in revenue."
}
---

## Four documents, one story

An earnings event produces four documents, and beginners usually read only the first:

1. **The press release**, furnished on Form 8-K. Headline revenue, EPS, segment results, guidance, and a few management quotes. Two to four pages of narrative plus condensed financial tables.
2. **The conference call**, with a transcript available within a day. Prepared remarks restate the release; the question-and-answer session is where analysts probe weak spots.
3. **The investor presentation**, if the company produces one. Charts of the same numbers, sometimes with extra operating metrics.
4. **The Form 10-Q or 10-K**, filed with the SEC days or weeks later. The full financial statements, notes, risk factors, and management's discussion. This is the audited (annually) or reviewed (quarterly) record.

The release is written to persuade; the filing is written to comply. When they disagree, the filing wins. This lesson shows you what to pull from each, using Apple's fiscal 2024 annual report as the worked example.

## The structure of a 10-K

A 10-K is organised into numbered items. The ones that matter for a first read:

- **Item 1, Business.** What the company sells, to whom, and how. Read this once per company, not every year.
- **Item 1A, Risk Factors.** A long list of things that could go wrong, written by lawyers. Skim for risks that are specific rather than boilerplate: a named customer, a named regulator, a named competitor. Changes from the prior year matter more than the list itself.
- **Item 7, Management's Discussion and Analysis (MD&A).** Management explains why revenue, margins and cash flow changed, discusses liquidity, and describes known trends. This is the most valuable section per minute of reading.
- **Item 8, Financial Statements.** The income statement, balance sheet, cash flow statement, statement of shareholders' equity, and the notes. The notes are where debt maturities, segment detail, tax items and share-count changes live.

A 10-Q is the same structure with fewer items and unaudited statements; its MD&A is Item 2 of Part I.

## The three statements in five minutes

**Income statement.** Revenue at the top, net income at the bottom, and a series of subtractions between them. The lines to check: revenue growth, gross margin (revenue minus cost of sales, as a percentage of revenue), operating margin (operating income divided by revenue), and diluted EPS. Compare each to the same period a year earlier, not to the previous quarter, unless the business has no seasonality.

**Balance sheet.** What the company owns and owes at a point in time. Check cash and marketable securities, total debt, and shareholders' equity. Net cash (cash minus debt) or net debt is the single number that tells you whether the company can survive a bad year without raising money.

**Cash flow statement.** Where cash actually came from and went. Operating cash flow should track net income over time; if it lags persistently, earnings quality is suspect. Below it, capital expenditure, buybacks, dividends and debt changes tell you what management did with the money.

## GAAP, non-GAAP and the reconciliation

Most companies lead with "adjusted" figures. Under Regulation G, any non-GAAP measure in a release must be accompanied by the most comparable GAAP measure and a reconciliation between them. Read the reconciliation every time. The standard adjustments:

- **Stock-based compensation.** Non-cash, but a real cost: it dilutes you. Companies that exclude it flatter their margins, especially in software.
- **Amortisation of acquired intangibles.** Reasonable to exclude for comparability, since it is a legacy of accounting for past deals.
- **Restructuring and one-time charges.** Legitimate when genuinely rare. A company that has restructuring charges nine years out of ten is describing a recurring cost.
- **Litigation and tax settlements.** Usually fair to isolate, but note the cash impact.

The test: would the business look the same next year if this item disappeared? If yes, excluding it is fair. If the item recurs, it belongs in your estimate of earnings power.

## Reading guidance

Guidance is management's forecast. It comes in several forms, and the form tells you something:

- **A range for revenue and a margin**, common at large companies. Apple guides verbally on the call to a revenue growth range and a gross margin range rather than to EPS.
- **A point estimate plus or minus a percentage**, as NVIDIA gives (45.0 billion dollars plus or minus 2 percent).
- **Full-year EPS ranges**, common at industrials and consumer companies.
- **No guidance**, which some companies adopt on principle and others adopt when visibility is poor. A company that withdraws guidance it previously gave is telling you something.

Whatever the form, do the arithmetic yourself. Take guided revenue, apply the guided gross margin, subtract a reasonable operating expense figure (last quarter's, adjusted for any stated change), apply the tax rate, divide by diluted shares. If your number lands far from consensus, either you have misread the guidance or the market is expecting a beat. Both are worth knowing before the report.

> **Callout:** Guidance ranges are usually set to be beaten. Compare the guided range to what the company subsequently reported for the last four quarters and you will learn each management team's habit.

## Table

Where to find each number, and the check to run on it.

| What you want | Where it is | Check |
| --- | --- | --- |
| Revenue growth and mix | Press release tables; 10-K Item 8, segment note | Year-over-year, by segment; is growth coming from the segment with the best margin? |
| Gross and operating margin | Income statement | Direction versus prior year; does MD&A explain the change? |
| GAAP versus adjusted EPS | Reg G reconciliation in the release | Which items recur? Recompute EPS with recurring items included |
| One-time items | MD&A; income tax and contingencies notes | Add back genuinely one-time charges; leave recurring ones in |
| Cash and debt | Balance sheet; debt note | Net cash or net debt; maturities in the next two years |
| Cash generation | Cash flow statement | Operating cash flow versus net income; capex trend |
| Share count | Cover page; EPS note; equity statement | Diluted shares rising (dilution) or falling (buybacks)? |
| Guidance | Release and call transcript | Rebuild EPS from the guided inputs; compare to consensus |
| New risks | 10-K Item 1A, compared to last year's | Anything named and specific that was not there before |

## Worked example

Apple's Form 10-K for the fiscal year ended 28 September 2024, filed on 1 November 2024. All figures are from the consolidated statements in Item 8 and the MD&A in Item 7.

**Income statement.** Net sales were 391.0 billion dollars, up 2 percent from 383.3 billion. Products contributed 294.9 billion (iPhone 201.2 billion) and Services 96.2 billion, up 13 percent. Gross margin was 180.7 billion dollars, or 46.2 percent of sales, up from 44.1 percent the prior year; MD&A attributes the increase to Services mix and cost savings. Operating income was 123.2 billion dollars, a 31.5 percent operating margin. Net income was 93.7 billion dollars, down from 97.0 billion. Diluted EPS was 6.08 dollars on 15.41 billion diluted shares, down from 6.13 dollars.

**The one-time item.** Net income fell while operating income rose. The income tax note explains: the provision for income taxes was 29.7 billion dollars, an effective rate of 24.1 percent, and includes a one-time charge of 10.2 billion dollars following the European Court of Justice's September 2024 decision on the State Aid case. Add it back: 93.7 plus 10.2 equals 103.9 billion dollars of net income, and dividing by 15.41 billion diluted shares gives an underlying EPS of about 6.75 dollars, up roughly 10 percent rather than down 1 percent. That single note changes the year from a decline to healthy growth.

**Balance sheet.** Cash and cash equivalents of 29.9 billion, current marketable securities of 35.2 billion and non-current marketable securities of 91.5 billion, for about 156.7 billion dollars in total. Commercial paper of 10.0 billion plus term debt of 96.7 billion (10.9 billion current, 85.8 billion non-current) gives total debt of about 106.6 billion. Net cash was therefore about 50 billion dollars.

**Cash flow.** Operating cash flow of 118.3 billion dollars, comfortably above net income. Share repurchases of 94.9 billion dollars and dividends of 15.2 billion dollars: essentially all the cash generated was returned to shareholders. Diluted share count fell from 15.81 billion to 15.41 billion, about 2.5 percent, which is why EPS held up better than net income.

**Guidance.** On the accompanying call, management guided the December quarter to revenue growth in the low-to-mid single digits year over year and a gross margin of 46 to 47 percent. Take the prior-year December quarter's 119.6 billion dollars, grow it 4 percent to about 124.4 billion, apply a 46.5 percent gross margin for about 57.8 billion of gross profit, subtract roughly 15.2 billion of operating expenses (the guided range), tax at 16 percent, and divide by about 15.2 billion shares: a little under 2.35 dollars of EPS. Apple subsequently reported 124.3 billion dollars of revenue and 2.40 dollars of EPS for that quarter. The rebuild landed within a few percent, which is the point: guidance plus arithmetic gets you close enough to judge whether the consensus is sane.

## Sources

- SEC Office of Investor Education, "How to Read a 10-K/10-Q": https://www.sec.gov/files/reada10k.pdf
- Apple Inc., Form 10-K for the fiscal year ended 28 September 2024 (EDGAR, CIK 0000320193): https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000320193&type=10-K
- SEC, Regulation G, Conditions for Use of Non-GAAP Financial Measures: https://www.sec.gov/rules/final/33-8176.htm
- SEC Office of Investor Education, glossary entry "Form 10-Q": https://www.investor.gov/introduction-investing/investing-basics/glossary/form-10-q
