---
{
  "title": "What a Crypto Asset Is and What You Actually Hold",
  "duration": "16 min",
  "free": true,
  "status": "published",
  "quiz": [
    {"q": "What does a bitcoin private key actually give you?", "opts": ["A coin stored in a file on your computer", "The ability to sign a transaction that spends outputs locked to the matching public key", "A password to the Bitcoin network's central server", "A claim on an exchange's reserves"], "correct": 1, "explain": "The whitepaper defines a coin as a chain of digital signatures. The key does not contain value; it authorises a spend of outputs the ledger already assigns to your address."},
    {"q": "Your exchange dashboard shows 0.5 BTC. On the Bitcoin ledger, who controls that 0.5 BTC?", "opts": ["You, because the balance is in your name", "The exchange, whose keys control a pooled wallet; your balance is an entry in the exchange's database", "The miners", "Nobody until you withdraw"], "correct": 1, "explain": "An exchange balance is a liability of the exchange to you. Coinbase's own 10-K risk factor says custodial assets could become part of a bankruptcy estate, with customers treated as general unsecured creditors."},
    {"q": "In block 968,369 on 2026-09-24 the miner collected 3.14502694 BTC. How much of that was transaction fees?", "opts": ["3.125 BTC", "0.02002694 BTC", "0.5 BTC", "None; fees go to the network"], "correct": 1, "explain": "The subsidy after the April 2024 halving is 3.125 BTC. Reward minus subsidy is 3.14502694 minus 3.125 = 0.02002694 BTC in fees across 3,733 transactions."},
    {"q": "Why is a 12- or 24-word seed phrase dangerous to photograph?", "opts": ["Photos degrade the words", "Anyone with the words can derive every private key in the wallet and spend everything, with no recourse", "The wallet locks after a photo", "Seed phrases expire"], "correct": 1, "explain": "BIP-39 deterministically derives all keys from the seed. Possession of the words is possession of the funds, and on-chain transfers are final."},
    {"q": "At 2 sat/vB and a 140 vB transaction, what did it cost to move 0.5 BTC on-chain on 2026-09-24 at $84,242 per BTC?", "opts": ["About $0.24", "About $24", "0.5% of the amount", "$84.24"], "correct": 0, "explain": "140 vB times 2 sat/vB is 280 sat = 0.0000028 BTC, and 0.0000028 times $84,242 is about $0.24. On-chain fees depend on transaction size in bytes, not on the value moved."}
  ],
  "task": "Install a non-custodial wallet on a spare device, write its seed phrase on paper, then delete and restore the wallet from the paper before you send it a single satoshi."
}
---

## The asset is a ledger entry, not a file

Every market you have traded so far had a custodian between you and the asset. Your shares sit at the DTC in a broker's name; your futures margin sits at a clearing house. Crypto is the first asset class where you can hold the thing itself with no intermediary at all, and also the first where most people choose not to and never notice the difference until a venue fails.

Start with what a bitcoin is. Satoshi Nakamoto's 2008 whitepaper defines an electronic coin as a chain of digital signatures: each owner transfers the coin by signing a hash of the previous transaction and the next owner's public key. There is no coin object. There is a public ledger, replicated across thousands of nodes, that records which outputs are currently spendable and which public key must sign to spend them. Your "balance" is the sum of the unspent outputs the ledger assigns to addresses you can sign for.

Ethereum and most other chains use an account model rather than unspent outputs, but the principle is identical: the ledger holds the state, and a private key is the sole authority to change the part of the state assigned to you.

## Keys, addresses and seed phrases

A private key is a 256-bit number. From it a public key is derived by elliptic-curve multiplication, and from the public key an address is derived by hashing. The derivation runs in one direction only: anyone can check that a signature matches an address, nobody can recover the key from it.

Modern wallets do not ask you to manage hundreds of keys. Under BIP-39 they generate a random seed, encode it as 12 or 24 English words, and derive every key you will ever use from that seed. Two consequences follow. First, a backup of the words is a backup of everything, including addresses you have not used yet. Second, whoever has the words has the money. There is no fraud department, no chargeback and no reset link. Transfers are final within an hour and cannot be reversed by anyone, which is exactly the property that makes the asset useful and exactly the property that makes custody mistakes unrecoverable.

## On-chain balance versus exchange balance

When you buy on an exchange, the exchange typically moves nothing on-chain. It credits a row in its own database. The coins it holds for all customers sit in a small number of pooled wallets whose keys the exchange controls. Your dashboard balance is therefore an IOU: a promise by the exchange to deliver coins when you ask.

That distinction sounds academic until it is not. Coinbase's annual report for 2022 discloses, in its risk factors, that crypto assets it holds in custody for customers could be treated as property of a bankruptcy estate, in which case customers could be treated as general unsecured creditors. That is the largest, most regulated exchange in the United States telling you in an SEC filing that a balance on its screen is a claim, not a possession. Lesson 3 covers what happened to customers of Mt. Gox and FTX when that claim was tested.

Withdrawing to a wallet you control converts the IOU into a ledger entry only you can spend. The cost of doing so is an on-chain transaction fee, and the worked example shows how small that is.

## What a block actually contains

Bitcoin's ledger is extended roughly every ten minutes by a block. The miner who produces the block collects a subsidy of newly created coins, which halves every 210,000 blocks, plus all the fees attached to the transactions included. Since the April 2024 halving the subsidy is 3.125 BTC. Fees are bid in satoshis per virtual byte (sat/vB) because block space, not value, is what is scarce: a transaction moving 100 BTC and one moving 0.001 BTC occupy the same bytes and pay the same fee.

## Worked example

On 2026-09-24 at 07:12:10 UTC the mempool.space API reported the chain tip at block 968,369. That block contained 3,733 transactions and paid its miner 3.14502694 BTC. The API's recommended fee to be included in the next block was 2 sat/vB; the fee for inclusion within an hour was 1 sat/vB, and the median fee rate inside the block was 1.14 sat/vB.

Decompose the miner's reward:

- Subsidy after the 2024 halving: 3.125 BTC.
- Total fees: 3.14502694 − 3.125 = 0.02002694 BTC.
- Average fee per transaction: 0.02002694 ÷ 3,733 = 0.00000537 BTC = 537 sat.
- At the Yahoo Finance BTC-USD close for 2026-09-24 of $84,242.04, 537 sat is 0.00000537 × 84,242.04 = $0.45 per transaction.

Now price a withdrawal. Suppose you hold 0.5 BTC on an exchange and want it in your own wallet. A typical single-input, two-output SegWit transaction is about 140 virtual bytes. At the next-block rate of 2 sat/vB:

- Fee = 140 vB × 2 sat/vB = 280 sat = 0.0000028 BTC.
- In dollars: 0.0000028 × 84,242.04 = $0.24.
- As a share of the 0.5 BTC ($42,121) moved: 0.24 ÷ 42,121 = 0.00056%.

The point of the arithmetic is the last line. On this day, converting a $42,000 exchange IOU into an asset nobody else can touch cost a quarter of a dollar and about ten minutes. Fee rates are not always this low; the block's own fee range ran from 0.51 to 200 sat/vB, and in congested periods next-block rates have exceeded 100 sat/vB, which would make the same transaction cost about $12. Even then the fee is a rounding error against the risk it removes. Exchanges may add their own withdrawal charge on top of the network fee; that is a venue fee, not a network cost, and it is listed on the venue's fee page.

## Table

| Where the asset sits | Who holds the keys | What you have | What can go wrong |
|---|---|---|---|
| Your own wallet, seed on paper | You | Spendable outputs on the ledger | Loss or theft of the seed; no recovery |
| Hardware wallet | You, with the key in a secure chip | Same, with signing isolated from your computer | Device loss without seed backup; supply-chain tampering |
| Exchange account | The exchange, pooled wallets | A database credit, a liability of the exchange | Insolvency, hack, withdrawal freeze, regulator action |
| Qualified custodian, segregated | The custodian, per-client addresses | A contractual claim plus a visible on-chain address | Custodian failure; slower access; fees |
| Spot ETF share | The fund's custodian | A security tracking the price | Tracking error, management fee, no coins deliverable |

Every row below the first two is a promise. Promises can be very good; most of the time they are. The course's position is not that you must self-custody everything, it is that you should know which row each of your balances is in and size accordingly.

## What this means for trading

Three practical rules fall out of the mechanics.

First, only the balance you need for open orders and near-term trades belongs on an exchange. The rest costs pennies to move and nothing to hold in a wallet you control.

Second, test every wallet by restoring it from its seed before funding it. A backup that has never been restored is a hope.

Third, addresses are one-way. Sending to a mistyped address, to the wrong chain, or to a contract that cannot forward the coins destroys them. Send a small test amount first, every time, to any address you have not used before.

None of this makes you a better trader. It stops a good trade being wiped out by an operational error that no equity trader has ever had to think about.

## Sources

- Satoshi Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System", 2008: https://bitcoin.org/bitcoin.pdf
- BIP-39, "Mnemonic code for generating deterministic keys": https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki
- mempool.space REST API (block 968,369, recommended fees, 2026-09-24): https://mempool.space/docs/api/rest
- Coinbase Global, Inc., Form 10-K for fiscal 2022, risk factors on custodial assets in bankruptcy: https://www.sec.gov/Archives/edgar/data/1679788/000167978823000031/coin-20221231.htm
