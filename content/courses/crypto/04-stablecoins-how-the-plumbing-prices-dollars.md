---
{
  "title": "Stablecoins: How the Plumbing Prices Everything in Dollars",
  "duration": "16 min",
  "free": false,
  "status": "published",
  "quiz": [
    {"q": "Why do most crypto pairs quote against USDT or USDC rather than against bank dollars?", "opts": ["Stablecoins are legal tender", "A token on the same ledger settles in minutes, 24/7, and can be moved between venues without a bank", "Banks refuse all crypto business", "Stablecoins pay interest to holders"], "correct": 1, "explain": "A stablecoin is a dollar IOU that lives on-chain, so it settles at the speed of the chain and needs no banking hours. That convenience is why it became the unit of account, and why its issuer's balance sheet became everyone's problem."},
    {"q": "On 2023-03-11 Yahoo's USDC-USD daily bar printed a low of 0.8774 and a close of 0.9715. What caused the discount?", "opts": ["A smart-contract hack", "Circle disclosed about $3.3 billion of reserves at Silicon Valley Bank, which the FDIC had just closed", "The Federal Reserve banned USDC", "A Bitcoin halving"], "correct": 1, "explain": "The FDIC closed SVB on 2023-03-10. Circle's statement that night disclosed the exposure; secondary-market holders could not redeem over the weekend, so the token traded at a discount until the deposits were guaranteed."},
    {"q": "A holder of $100,000 face value of USDC who sold at the 0.9715 close on 2023-03-11 received", "opts": ["$100,000", "$97,150", "$87,740", "$0"], "correct": 1, "explain": "100,000 times 0.9715 is $97,150. A seller at the day's low would have received $87,740. A holder who did nothing was back to $1.00 within days, which is the trade-off the lesson works through."},
    {"q": "What does the GENIUS Act (Public Law 119-27, signed 2025-07-18) do?", "opts": ["Bans stablecoins in the United States", "Creates a federal framework for permitted payment stablecoin issuers, including reserve requirements", "Makes stablecoins legal tender", "Sets the price of USDT"], "correct": 1, "explain": "The act's short title is the Guiding and Establishing National Innovation for U.S. Stablecoins Act; it provides for the regulation of payment stablecoins and their issuers."},
    {"q": "Which stablecoin design failed completely in May 2022?", "opts": ["A fiat-reserved coin", "An algorithmic coin backed by a volatile sister token rather than dollar reserves", "A coin backed by Treasury bills", "A bank deposit token"], "correct": 1, "explain": "TerraUSD held no dollar reserves; its peg relied on minting and burning LUNA. When confidence broke, both went to near zero. Reserve quality is the whole question."}
  ],
  "task": "For each stablecoin you hold or trade against, find the issuer's most recent published reserve report and write down the share held in cash and short-dated Treasuries."
}
---

## The dollar on the ledger

Look at any crypto exchange and most pairs are not quoted against dollars. They are quoted against USDT or USDC, tokens that are meant to be worth one dollar each. Perpetual swaps (lesson 5) are margined and settled in them. The cash-and-carry trade in the capstone is priced in them. If you trade crypto you are, whether you noticed or not, holding a private company's dollar IOU as your cash balance, and you need to know how it is built.

A fiat-reserved stablecoin works like a money-market fund with a token instead of a share. The issuer takes dollars, holds them in reserves (bank deposits, Treasury bills, repo), and mints one token per dollar. Redemption runs in reverse: send tokens to the issuer, receive dollars, tokens are burned. The peg holds because anyone with an issuer account can arbitrage a discount by buying tokens below one dollar and redeeming at par.

On 2026-09-24 CoinGecko's simple-price endpoint reported USDT at $0.999826 with a market capitalisation of $183.5 billion and USDC at $0.999869 with $75.4 billion. Together that is about $259 billion of private dollar liabilities that trade around the clock and settle in minutes.

## Why the plumbing runs on tokens

The reason is banking hours. A bank wire moves during business days, in the bank's time zone, through correspondent banks that may refuse crypto business. A token on the same chain as the asset you are trading settles in the next block, on a Sunday, to any address. Exchanges and market makers hold stablecoins so they can move collateral between venues in minutes when a price gap opens. Once the market makers price in stablecoins, the whole market does.

The convenience has a cost. Your cash is now exposed to three risks that bank cash is not: the issuer's reserve quality, the issuer's ability to process redemptions in stress, and the possibility that the token you hold is frozen or blacklisted by the issuer's contract. Each has been tested.

## The reserve question

Tether publishes attestations of USDT reserves on its transparency page. Circle publishes monthly reserve reports for USDC on its transparency page. The reports differ in auditor, frequency and detail, and the composition of reserves has changed over time. What you are looking for is simple: what share of reserves is cash at banks and short-dated US Treasuries, and what share is anything else. Anything else, whether commercial paper, loans, or other digital assets, is where a discount comes from when confidence breaks.

The other design, the algorithmic stablecoin, holds no dollar reserves at all. TerraUSD kept its peg by allowing holders to swap one UST for one dollar's worth of a sister token, LUNA, minted on demand. In May 2022 the mechanism reversed: UST slipped, holders redeemed into LUNA, LUNA's supply exploded, its price collapsed, and the redemption promise became worthless. Both tokens went to near zero within a week. Yahoo's USDT-USD bar for 2022-05-12, in the middle of that week, printed a low of 0.9485, the contagion reaching even the largest reserved coin for a few hours before redemptions at par pulled it back.

## Worked example

The cleanest test of a reserved stablecoin's plumbing came in March 2023.

On Friday 2023-03-10 the FDIC announced that the California Department of Financial Protection and Innovation had closed Silicon Valley Bank and appointed the FDIC as receiver. That evening Circle published a statement that about $3.3 billion of the roughly $40 billion of USDC reserves were held at SVB. Redemptions at Circle run through banks, and banks were closed for the weekend. Secondary-market holders who wanted dollars had one route: sell the token.

Yahoo Finance's USDC-USD daily bar for Saturday 2023-03-11 shows open 0.9995, high 1.0001, low 0.8774, close 0.9715. Work through what those prints meant to a holder of 100,000 USDC:

- Face value: $100,000.
- Sold at the close: 100,000 × 0.9715 = $97,150, a loss of $2,850 (2.85%).
- Sold at the low: 100,000 × 0.8774 = $87,740, a loss of $12,260 (12.26%).
- Held: on Sunday 2023-03-12 the Treasury, Federal Reserve and FDIC announced that SVB depositors would be made whole in full; the token returned to par during the following week. Loss: zero.

Now the other side of the trade. A participant with a Circle account who bought 100,000 USDC at the close of 0.9715 for $97,150 could redeem for $100,000 once banks reopened, a gross gain of $2,850 (2.93% on capital) for holding over a weekend, conditional on the reserves being good. At the low the same trade returned 100,000 ÷ 87,740 − 1 = 13.97%. That return is the market's price for two things it could not verify on a Saturday: whether the $3.3 billion would be recovered, and whether redemptions would resume.

What decided the outcome was not the token's code. It was a federal deposit guarantee announced on a Sunday. The peg is only as good as the assets behind it and the institutions those assets sit in, and neither is on the blockchain.

## Table

| Stablecoin design | Backing | Redemption path | Stress episode and low print | Outcome |
|---|---|---|---|---|
| Fiat-reserved, bank-heavy | Cash at banks, T-bills, repo | Issuer account, banking hours | USDC, 2023-03-11: low 0.8774, close 0.9715 (Yahoo) | Par restored after SVB depositor guarantee |
| Fiat-reserved, mixed | Cash, T-bills, other assets per attestation | Issuer account, minimums apply | USDT, 2022-05-12: low 0.9485 (Yahoo) | Par restored within hours via redemptions |
| Algorithmic | Sister token minted on demand, no dollar reserves | Swap into sister token | TerraUSD, May 2022 | Both tokens to near zero |
| Bank deposit token / regulated payment stablecoin | Segregated reserves under a federal or state regime | Issuer, with regulatory redemption rules | GENIUS Act framework from 2025 | Untested in a systemic stress at the time of writing |

## Regulation catches up

Until 2025 US stablecoin issuers were regulated, if at all, as state money transmitters or trust companies. Public Law 119-27, the GENIUS Act, was signed on 2025-07-18. Its text provides for the regulation of payment stablecoins: who may issue them, what reserves they must hold, and how redemption and disclosure work. The details are in the statute on govinfo.gov, and the implementing rules will keep changing; what matters for a trader is that reserve quality is moving from a voluntary attestation to a legal requirement, and that a compliant issuer's token and a non-compliant issuer's token are different credits even if both trade at $1.00.

## What to do with this

Three rules. Treat every stablecoin balance as an unsecured, uninsured deposit with its issuer, sized like the exchange balances in lesson 3. Know the redemption path for each coin you hold, because in a discount the holder with an issuer account has an arbitrage and the holder without one has a loss. And when a stablecoin you are margined in trades away from par, understand that your perpetual position's collateral just changed value while your liquidation price, computed in that same token, did not move at all.

## Sources

- Federal Deposit Insurance Corporation, press release PR-16-2023, "FDIC Creates a Deposit Insurance National Bank of Santa Clara to Protect Insured Depositors of Silicon Valley Bank", 2023-03-10: https://www.fdic.gov/news/press-releases/2023/pr23016.html
- Circle Internet Financial, "An Update on USDC and Silicon Valley Bank", 2023-03-10 (issuer statement disclosing the $3.3 billion exposure): https://www.circle.com/blog/an-update-on-usdc-and-silicon-valley-bank
- Public Law 119-27, "Guiding and Establishing National Innovation for U.S. Stablecoins Act" (GENIUS Act), 2025-07-18: https://www.govinfo.gov/content/pkg/PLAW-119publ27/pdf/PLAW-119publ27.pdf
- Yahoo Finance chart API, USDC-USD daily bars: https://query1.finance.yahoo.com/v8/finance/chart/USDC-USD?range=5y&interval=1d
