---
{
  "title": "How Options Are Priced",
  "duration": "12 min",
  "free": true,
  "status": "published",
  "quiz": {
    "q": "What happens to an option's time value as it approaches expiration?",
    "opts": [
      "It increases as the deadline creates urgency",
      "It remains constant until the final week",
      "It decreases, accelerating rapidly in the last 30 days",
      "It only changes if the underlying stock moves"
    ],
    "correct": 2
  }
}
---

<p>Option pricing is both art and science. Understanding what drives an option's price — and how it changes minute by minute — is essential before you risk capital. Most options traders who lose money do so not because their directional view was wrong, but because they did not understand the pricing mechanics working against them.</p>
        <h2>Intrinsic Value</h2>
        <p>The intrinsic value of an option is the amount by which it is currently <em>in the money</em>. An AAPL $210 call with AAPL at $220 has $10 of intrinsic value — it is worth at least $10 because you could exercise it and immediately profit $10 per share. An out-of-the-money option (AAPL $230 call with AAPL at $220) has zero intrinsic value — it has only time value.</p>
        <h2>Time Value (Extrinsic Value)</h2>
        <p>Time value is the portion of an option's premium above its intrinsic value. It reflects the probability that the option will move further into the money before expiration. A 6-month option has more time value than a 2-week option on the same stock at the same strike — more time means more opportunity for the stock to move.</p>
        <p><strong>Time decay (theta):</strong> Time value evaporates as expiration approaches — and it does so non-linearly, accelerating rapidly in the last 30 days before expiry. This is the core mechanic option sellers exploit: they collect time value and wait for it to decay. It is also the mechanic that quietly destroys the accounts of option buyers who hold positions too long.</p>
        <h2>Implied Volatility (IV)</h2>
        <p>IV is the market's expectation of future price movement, expressed as an annualised percentage. High IV = expensive options. Low IV = cheap options. IV is the single most important variable in options pricing after the underlying price itself.</p>
        <p>A stock with 20% IV and one with 80% IV might have the same price and same strike — but the 80% IV option will cost 4× as much. This matters profoundly for strategy selection: when IV is high, selling options is more attractive; when IV is low, buying options is relatively cheaper.</p>
        <div class="course-callout blue"><strong>IV Rank:</strong> IV in isolation means nothing. IV Rank contextualises current IV against its own 52-week range. An IV Rank of 80 means IV is in the 80th percentile of its range over the past year — historically elevated. This is when selling premium makes statistical sense.</div>
