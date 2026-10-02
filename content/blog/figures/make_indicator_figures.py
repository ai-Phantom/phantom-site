import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts")); from svgfig import *
"""Figures for the eight indicator blog posts.

Data: SPY daily bars from Yahoo Finance's public chart API, fetched with curl,
period1=1640995200 (2022-01-01 UTC), period2=1790812800 (2026-10-01 UTC),
interval=1d. Expect dataGranularity "1d" and 1,190 rows, 2022-01-03 .. 2026-09-30.
OHLC are as Yahoo serves them (split-adjusted, not dividend-adjusted).

    python3 make_indicator_figures.py            # redraw from indicator_data.json (offline)
    python3 make_indicator_figures.py --refresh  # re-fetch, recompute, rewrite the JSON, redraw

Every indicator below re-implements the logic the Phantom Traders bots use,
with the same parameters. Two evaluation modes are used:
  * full history: one pass over all 1,190 bars (what a charting platform shows);
  * rolling year: each day is computed from only the trailing 250 bars, which is
    how a scanner that loads about a year of daily bars sees it. Long averages,
    the reversal-probability statistics and market-structure labels depend on
    where that window starts, so both are reported where they differ.
"""
import json
import math
import subprocess
import datetime as dt

HERE = Path(__file__).resolve().parent
DATA = HERE / "indicator_data.json"
TICKER = "SPY"
PERIOD1, PERIOD2 = 1640995200, 1790812800
EXPECTED_ROWS = 1190
ROLLING_BARS = 250


# ---------------------------------------------------------------- data

def fetch_bars(ticker=TICKER):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
           f"?period1={PERIOD1}&period2={PERIOD2}&interval=1d")
    raw = subprocess.run(["curl", "-s", "-A", "Mozilla/5.0", url], check=True, capture_output=True, text=True).stdout
    result = json.loads(raw)["chart"]["result"][0]
    granularity = result["meta"]["dataGranularity"]
    assert granularity == "1d", f"expected daily bars, got {granularity}"
    quote = result["indicators"]["quote"][0]
    new_york = dt.timezone(dt.timedelta(hours=-4))
    dates = [dt.datetime.fromtimestamp(t, new_york).date().isoformat() for t in result["timestamp"]]
    assert len(dates) == EXPECTED_ROWS, f"expected {EXPECTED_ROWS} rows, got {len(dates)}"
    assert dates[0] == "2022-01-03" and dates[-1] == "2026-09-30", (dates[0], dates[-1])
    assert None not in quote["close"]
    return dates, quote["open"], quote["high"], quote["low"], quote["close"]


# ---------------------------------------------------------------- shared math

def ema_series(values, period):
    """EMA seeded with the simple average of the first `period` values."""
    out = [None] * len(values)
    if len(values) < period:
        return out
    k = 2 / (period + 1)
    ema = sum(values[:period]) / period
    out[period - 1] = ema
    for i in range(period, len(values)):
        ema = values[i] * k + ema * (1 - k)
        out[i] = ema
    return out


def sma_series(values, period):
    out = [None] * len(values)
    for i in range(period - 1, len(values)):
        out[i] = sum(values[i - period + 1:i + 1]) / period
    return out


def rma_series(values, period):
    out = [None] * len(values)
    if len(values) < period:
        return out
    out[period - 1] = sum(values[:period]) / period
    for i in range(period, len(values)):
        out[i] = (out[i - 1] * (period - 1) + values[i]) / period
    return out


def atr_series(highs, lows, closes, period):
    """Wilder ATR; first value is the plain average of the first `period` true ranges."""
    n = len(closes)
    if n < period + 1:
        return [None] * n
    true_ranges = [None] + [max(highs[i] - lows[i], abs(highs[i] - closes[i - 1]), abs(lows[i] - closes[i - 1]))
                            for i in range(1, n)]
    out = [None] * n
    out[period] = sum(true_ranges[1:period + 1]) / period
    for i in range(period + 1, n):
        out[i] = (out[i - 1] * (period - 1) + true_ranges[i]) / period
    return out


def rsi_series(closes, period):
    n = len(closes)
    out = [None] * n
    if n < period + 1:
        return out
    gains = [0.0] + [max(closes[i] - closes[i - 1], 0) for i in range(1, n)]
    losses = [0.0] + [max(closes[i - 1] - closes[i], 0) for i in range(1, n)]
    average_gain = sum(gains[1:period + 1]) / period
    average_loss = sum(losses[1:period + 1]) / period
    out[period] = 100.0 if average_loss == 0 else 100 - 100 / (1 + average_gain / average_loss)
    for i in range(period + 1, n):
        average_gain = (average_gain * (period - 1) + gains[i]) / period
        average_loss = (average_loss * (period - 1) + losses[i]) / period
        out[i] = 100.0 if average_loss == 0 else 100 - 100 / (1 + average_gain / average_loss)
    return out


def normal_cdf(z):
    """Abramowitz-Stegun approximation, as in the original script."""
    sign = -1 if z < 0 else 1
    x = abs(z) / math.sqrt(2)
    t = 1 / (1 + 0.3275911 * x)
    erf = 1 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * math.exp(-x * x)
    return 0.5 * (1 + sign * erf)


# ---------------------------------------------------------------- 1. gaps

GAP_FRACTION, GAP_RANGE_BARS, GAP_LOOKBACK = 0.30, 14, 50


def average_range(highs, lows, end_index):
    start = max(0, end_index - GAP_RANGE_BARS + 1)
    return sum(highs[k] - lows[k] for k in range(start, end_index + 1)) / (end_index - start + 1)


def gap_flags(highs, lows):
    """Flags for the last bar: new gap up/down, or fill of a still-open gap."""
    flags = {"gap_up_new": False, "gap_down_new": False, "gap_up_filled": False, "gap_down_filled": False}
    i = len(highs) - 1
    threshold = GAP_FRACTION * average_range(highs, lows, i - 1)
    if lows[i] - highs[i - 1] >= threshold:
        flags["gap_up_new"] = True
    elif lows[i - 1] - highs[i] >= threshold:
        flags["gap_down_new"] = True
    for j in range(max(GAP_RANGE_BARS, i - GAP_LOOKBACK), i):
        threshold_j = GAP_FRACTION * average_range(highs, lows, j - 1)
        is_up = lows[j] - highs[j - 1] >= threshold_j
        is_down = lows[j - 1] - highs[j] >= threshold_j and not is_up
        if not (is_up or is_down):
            continue
        top, bottom = (lows[j], highs[j - 1]) if is_up else (lows[j - 1], highs[j])
        filled_before = any((is_up and lows[k] <= bottom) or (is_down and highs[k] >= top) for k in range(j + 1, i))
        if filled_before:
            continue
        if is_up and lows[i] <= bottom:
            flags["gap_up_filled"] = True
        elif is_down and highs[i] >= top:
            flags["gap_down_filled"] = True
    return flags


# ---------------------------------------------------------------- 2. UT Bot

def utbot_stop(highs, lows, closes, key_value=1.0, atr_period=10):
    atr = atr_series(highs, lows, closes, atr_period)
    stop = [None] * len(closes)
    for i in range(atr_period, len(closes)):
        loss = key_value * atr[i]
        previous = stop[i - 1] if stop[i - 1] is not None else 0.0
        if closes[i] > previous and closes[i - 1] > previous:
            stop[i] = max(previous, closes[i] - loss)
        elif closes[i] < previous and closes[i - 1] < previous:
            stop[i] = min(previous, closes[i] + loss)
        elif closes[i] > previous:
            stop[i] = closes[i] - loss
        else:
            stop[i] = closes[i] + loss
    return stop, atr


def utbot_signals(closes, stop):
    signals = {}
    for i in range(1, len(closes)):
        if stop[i] is None or stop[i - 1] is None:
            continue
        if closes[i - 1] < stop[i - 1] < closes[i] and closes[i] > stop[i]:
            signals[i] = "buy"
        elif closes[i - 1] > stop[i - 1] > closes[i] and closes[i] < stop[i]:
            signals[i] = "sell"
    return signals


# ---------------------------------------------------------------- 4. Zero Lag

def zero_lag(highs, lows, closes, length=70, multiplier=1.2):
    n = len(closes)
    lag = (length - 1) // 2
    adjusted = [closes[i] + (closes[i] - closes[i - lag]) if i >= lag else closes[i] for i in range(n)]
    zlema = ema_series(adjusted, length)
    atr = atr_series(highs, lows, closes, length)
    highest_atr = [None] * n
    for i in range(length, n):
        window = [atr[j] for j in range(max(length, i - length * 3 + 1), i + 1) if atr[j] is not None]
        highest_atr[i] = max(window) if window else None
    trend = [0] * n
    for i in range(1, n):
        trend[i] = trend[i - 1]
        if zlema[i] is None or highest_atr[i] is None:
            continue
        upper = zlema[i] + highest_atr[i] * multiplier
        lower = zlema[i] - highest_atr[i] * multiplier
        if closes[i] > upper and closes[i - 1] <= upper:
            trend[i] = 1
        elif closes[i] < lower and closes[i - 1] >= lower:
            trend[i] = -1
    return zlema, highest_atr, trend


# ---------------------------------------------------------------- 5. Trend reversal probability

def reversal_probability(highs, lows, oscillator_period=20):
    """Probability for the last bar, computed only from the bars passed in."""
    n = len(highs)
    midpoints = [(h + l) / 2 for h, l in zip(highs, lows)]
    fast, slow = sma_series(midpoints, 5), sma_series(midpoints, 34)
    oscillator = [(fast[i] - slow[i]) if slow[i] is not None else None for i in range(n)]
    changes = [None] + [(oscillator[i] - oscillator[i - 1]) if oscillator[i - 1] is not None and oscillator[i] is not None else None
                        for i in range(1, n)]
    rises = [max(c, 0) if c is not None else 0.0 for c in changes]
    falls = [-min(c, 0) if c is not None else 0.0 for c in changes]
    rise_rma, fall_rma = rma_series(rises[34:], oscillator_period), rma_series(falls[34:], oscillator_period)
    centred_rsi = [None] * n
    for offset, (rise, fall) in enumerate(zip(rise_rma, fall_rma)):
        if rise is None:
            continue
        value = 100.0 if fall == 0 else (0.0 if rise == 0 else 100 - 100 / (1 + rise / fall))
        centred_rsi[34 + offset] = value - 50
    bars_in_phase, previous_count, durations, last_sign = 0, 0, [], None
    for value in centred_rsi:
        if value is None:
            continue
        sign = 1 if value >= 0 else -1
        if last_sign is not None and sign != last_sign:
            if previous_count > 0:
                durations.insert(0, previous_count)
            bars_in_phase = 0
        else:
            bars_in_phase += 1
        previous_count, last_sign = bars_in_phase, sign
    mean = sum(durations) / len(durations)
    sd = (sum((d - mean) ** 2 for d in durations) / len(durations)) ** 0.5
    z = (bars_in_phase - mean) / sd
    return {"probability": normal_cdf(z), "bars_in_phase": bars_in_phase, "mean": mean, "sd": sd, "z": z,
            "oscillator": centred_rsi[-1], "phases": len(durations)}


# ---------------------------------------------------------------- 6. QQE MOD

def qqe_line(closes, rsi_length=6, smoothing=5, factor=3.0):
    n = len(closes)
    rsi = [50.0 if r is None else r for r in rsi_series(closes, rsi_length)]
    smoothed = ema_series(rsi, smoothing)
    rsi_moves = [0.0] + [abs(smoothed[i - 1] - smoothed[i]) if smoothed[i - 1] is not None and smoothed[i] is not None else 0.0
                         for i in range(1, n)]
    move_average = ema_series(rsi_moves, rsi_length * 2 - 1)
    long_band, short_band, direction = [0.0] * n, [0.0] * n, [0] * n
    for i in range(1, n):
        direction[i] = direction[i - 1]
        if smoothed[i] is None or move_average[i] is None:
            continue
        distance = move_average[i] * factor
        new_long, new_short = smoothed[i] - distance, smoothed[i] + distance
        long_band[i] = max(long_band[i - 1], new_long) if smoothed[i - 1] is not None and smoothed[i - 1] > long_band[i - 1] and smoothed[i] > long_band[i - 1] else new_long
        short_band[i] = min(short_band[i - 1], new_short) if smoothed[i - 1] is not None and smoothed[i - 1] < short_band[i - 1] and smoothed[i] < short_band[i - 1] else new_short
        if smoothed[i - 1] is not None:
            if smoothed[i] > short_band[i - 1] and smoothed[i - 1] <= short_band[i - 1]:
                direction[i] = 1
            elif long_band[i - 1] > smoothed[i] and long_band[i - 1] <= smoothed[i - 1]:
                direction[i] = -1
    line = [long_band[i] if direction[i] == 1 else (short_band[i] if direction[i] == -1 else None) for i in range(n)]
    return line, smoothed


def qqe_bands(line, i, length=50, multiplier=0.35):
    window = [v - 50 for v in line[i - length + 1:i + 1]]
    basis = sum(window) / length
    deviation = multiplier * (sum((v - basis) ** 2 for v in window) / length) ** 0.5
    return basis, deviation


# ---------------------------------------------------------------- 7. MACD_X

def macd_pair(closes):
    e12, e26, e5, e15 = (ema_series(closes, p) for p in (12, 26, 5, 15))
    slow = [(a - b) if b is not None else None for a, b in zip(e12, e26)]
    fast = [(a - b) if b is not None else None for a, b in zip(e5, e15)]
    return slow, fast


def fractal_lows(values):
    return [i for i in range(2, len(values) - 2) if None not in values[i - 2:i + 3]
            and values[i] < min(values[i - 2], values[i - 1], values[i + 1], values[i + 2])]


def fractal_highs(values):
    return [i for i in range(2, len(values) - 2) if None not in values[i - 2:i + 3]
            and values[i] > max(values[i - 2], values[i - 1], values[i + 1], values[i + 2])]


def macdx_flags(closes):
    slow, fast = macd_pair(closes)
    i = len(closes) - 1
    flags = {
        "trend_buy": fast[i] > 0 >= fast[i - 1] and slow[i] < fast[i] and slow[i] > slow[i - 1] and slow[i] < 0,
        "trend_sell": fast[i] < 0 <= fast[i - 1] and slow[i] > fast[i] and slow[i] < slow[i - 1] and slow[i] > 0,
        "counter_buy": fast[i] > slow[i] and fast[i - 1] <= slow[i - 1] and fast[i] < 0,
        "counter_sell": fast[i] < slow[i] and fast[i - 1] >= slow[i - 1] and fast[i] > 0,
        "bull_divergence": None, "bear_divergence": None,
    }
    price_lows, price_highs, macd_lows, macd_highs = fractal_lows(closes), fractal_highs(closes), fractal_lows(slow), fractal_highs(slow)
    if len(price_lows) >= 2 and len(macd_lows) >= 2 and i - max(price_lows[-1], macd_lows[-1]) <= 10:
        if closes[price_lows[-1]] < closes[price_lows[-2]] and slow[macd_lows[-1]] > slow[macd_lows[-2]]:
            flags["bull_divergence"] = (price_lows[-2], price_lows[-1], macd_lows[-2], macd_lows[-1])
    if len(price_highs) >= 2 and len(macd_highs) >= 2 and i - max(price_highs[-1], macd_highs[-1]) <= 10:
        if closes[price_highs[-1]] > closes[price_highs[-2]] and slow[macd_highs[-1]] < slow[macd_highs[-2]]:
            flags["bear_divergence"] = (price_highs[-2], price_highs[-1], macd_highs[-2], macd_highs[-1])
    return flags


# ---------------------------------------------------------------- 8. SMC structure

def structure_events(highs, lows, closes, size):
    """Swing pivots and BOS/CHoCH breaks, LuxAlgo-style leg logic, closes only."""
    n = len(highs)
    legs = [0] * n
    for i in range(size, n):
        if highs[i - size] > max(highs[i - size + 1:i + 1]):
            legs[i] = 0
        elif lows[i - size] < min(lows[i - size + 1:i + 1]):
            legs[i] = 1
        else:
            legs[i] = legs[i - 1]
    swing_high = swing_low = None
    high_crossed = low_crossed = True
    bias, events = 0, []
    for i in range(size + 1, n):
        if legs[i] != legs[i - 1]:
            if legs[i] == 1:
                swing_low, low_crossed = lows[i - size], False
                events.append((i, "swing low", i - size, swing_low))
            else:
                swing_high, high_crossed = highs[i - size], False
                events.append((i, "swing high", i - size, swing_high))
        if swing_high is not None and not high_crossed and closes[i] > swing_high >= closes[i - 1]:
            events.append((i, "bullish CHoCH" if bias == -1 else "bullish BOS", None, swing_high))
            high_crossed, bias = True, 1
        if swing_low is not None and not low_crossed and closes[i] < swing_low <= closes[i - 1]:
            events.append((i, "bearish CHoCH" if bias == 1 else "bearish BOS", None, swing_low))
            low_crossed, bias = True, -1
    return events


# ---------------------------------------------------------------- compute everything

def r(v, d=2):
    return None if v is None else round(v, d)


def compute():
    dates, opens, highs, lows, closes = fetch_bars()
    idx = {d: i for i, d in enumerate(dates)}

    def span(start, end):
        return [i for i, d in enumerate(dates) if start <= d <= end]

    def rolling(i):
        s = i - ROLLING_BARS + 1
        return slice(s, i + 1)

    out = {"source": {"ticker": TICKER, "period1": PERIOD1, "period2": PERIOD2, "rows": len(dates),
                      "first": dates[0], "last": dates[-1]}}

    # 1. Gaps: Feb-Jun 2025
    w = span("2025-02-03", "2025-06-30")
    gap_days = {}
    for i in w:
        flags = [k for k, v in gap_flags(highs[:i + 1], lows[:i + 1]).items() if v]
        if flags:
            gap_days[dates[i]] = flags
    gap_detail = {}
    for d in ("2025-04-03", "2025-04-04", "2025-04-09", "2025-04-29", "2025-05-12"):
        i = idx[d]
        avg = average_range(highs, lows, i - 1)
        gap_detail[d] = {"high": r(highs[i]), "low": r(lows[i]), "prev_high": r(highs[i - 1]), "prev_low": r(lows[i - 1]),
                         "avg_range14": r(avg, 3), "threshold": r(GAP_FRACTION * avg, 3)}
    out["gaps"] = {"dates": [dates[i] for i in w], "ohlc": [[r(opens[i]), r(highs[i]), r(lows[i]), r(closes[i])] for i in w],
                   "fires": gap_days, "detail": gap_detail}

    # 2. UT Bot: Dec 2025 - Jun 2026
    stop, atr10 = utbot_stop(highs, lows, closes)
    signals = utbot_signals(closes, stop)
    w = span("2025-12-01", "2026-06-30")
    out["utbot"] = {"dates": [dates[i] for i in w], "close": [r(closes[i]) for i in w], "stop": [r(stop[i]) for i in w],
                    "signals": {dates[i]: {"side": s, "prev_close": r(closes[i - 1]), "close": r(closes[i]),
                                           "prev_stop": r(stop[i - 1]), "stop": r(stop[i]), "atr10": r(atr10[i])}
                                for i, s in signals.items() if i in w}}

    # 3. EMA stack: Jan-Aug 2025, full history, plus the rolling-year cross dates
    emas = {p: ema_series(closes, p) for p in (20, 50, 100, 200)}
    w = span("2025-01-02", "2025-08-29")
    crosses = {}
    for i in w:
        if emas[50][i - 1] <= emas[200][i - 1] and emas[50][i] > emas[200][i]:
            crosses[dates[i]] = "golden"
        if emas[50][i - 1] >= emas[200][i - 1] and emas[50][i] < emas[200][i]:
            crosses[dates[i]] = "death"
    rolling_crosses = {}
    for i in w:
        part = closes[rolling(i)]
        e50, e200 = ema_series(part, 50), ema_series(part, 200)
        if e50[-2] <= e200[-2] and e50[-1] > e200[-1]:
            rolling_crosses[dates[i]] = "golden"
        if e50[-2] >= e200[-2] and e50[-1] < e200[-1]:
            rolling_crosses[dates[i]] = "death"
    fan = {}
    previous = None
    for i in w:
        a, b, c, d = (emas[p][i] for p in (20, 50, 100, 200))
        state = "bullish" if a > b > c > d else ("bearish" if a < b < c < d else "mixed")
        if state != previous:
            fan[dates[i]] = state
        previous = state
    detail = {d: {"close": r(closes[idx[d]]), **{f"ema{p}": r(emas[p][idx[d]]) for p in (20, 50, 100, 200)},
                  "prev_ema50": r(emas[50][idx[d] - 1]), "prev_ema200": r(emas[200][idx[d] - 1])}
              for d in list(crosses) + ["2025-06-03"]}
    out["ema"] = {"dates": [dates[i] for i in w], "close": [r(closes[i]) for i in w],
                  **{f"ema{p}": [r(emas[p][i]) for i in w] for p in (20, 50, 100, 200)},
                  "crosses": crosses, "rolling_year_crosses": rolling_crosses, "fan_changes": fan, "detail": detail}

    # 4. Zero Lag: Jan-Oct 2025
    zlema, highest_atr, trend = zero_lag(highs, lows, closes)
    w = span("2025-01-02", "2025-10-31")
    events = {}
    for i in w:
        tags = []
        if trend[i] == 1 and trend[i - 1] != 1:
            tags.append("bullish trend change")
        if trend[i] == -1 and trend[i - 1] != -1:
            tags.append("bearish trend change")
        if closes[i] > zlema[i] and closes[i - 1] <= zlema[i - 1] and trend[i] == trend[i - 1] == 1:
            tags.append("bullish entry")
        if closes[i] < zlema[i] and closes[i - 1] >= zlema[i - 1] and trend[i] == trend[i - 1] == -1:
            tags.append("bearish entry")
        if tags:
            events[dates[i]] = {"tags": tags, "close": r(closes[i]), "prev_close": r(closes[i - 1]), "zlema": r(zlema[i]),
                                "highest_atr70": r(highest_atr[i], 3), "band_width": r(highest_atr[i] * 1.2),
                                "upper": r(zlema[i] + highest_atr[i] * 1.2), "lower": r(zlema[i] - highest_atr[i] * 1.2)}
    out["zerolag"] = {"dates": [dates[i] for i in w], "close": [r(closes[i]) for i in w], "zlema": [r(zlema[i]) for i in w],
                      "upper": [r(zlema[i] + highest_atr[i] * 1.2) for i in w], "lower": [r(zlema[i] - highest_atr[i] * 1.2) for i in w],
                      "events": events}

    # 5. Trend reversal probability: Jan-Jul 2026, rolling year
    w = span("2026-01-02", "2026-07-31")
    rows = []
    for i in w:
        res = reversal_probability(highs[rolling(i)], lows[rolling(i)])
        rows.append({"date": dates[i], "close": r(closes[i]), "probability": round(res["probability"], 4),
                     "bars_in_phase": res["bars_in_phase"], "mean": r(res["mean"], 3), "sd": r(res["sd"], 3),
                     "z": r(res["z"], 3), "oscillator": r(res["oscillator"]), "phases": res["phases"]})
    out["trp"] = {"rows": rows}

    # 6. QQE MOD: Jan-Jun 2026
    line, smoothed = qqe_line(closes, factor=3.0)
    _, smoothed_secondary = qqe_line(closes, factor=1.61)
    assert all(abs(a - b) < 1e-9 for a, b in zip(smoothed, smoothed_secondary) if a is not None)
    w = span("2026-01-02", "2026-06-30")
    series = {"rsi_minus_50": [], "upper": [], "lower": []}
    states, previous = {}, None
    for i in w:
        basis, deviation = qqe_bands(line, i)
        value = smoothed[i] - 50
        series["rsi_minus_50"].append(r(value))
        series["upper"].append(r(basis + deviation))
        series["lower"].append(r(basis - deviation))
        state = "buy" if value > 3 and value > basis + deviation else ("sell" if value < -3 and value < basis - deviation else "none")
        if state != previous:
            states[dates[i]] = {"state": state, "close": r(closes[i]), "rsi_minus_50": r(value, 3), "basis": r(basis, 3),
                                "deviation": r(deviation, 3), "upper": r(basis + deviation, 3), "lower": r(basis - deviation, 3)}
        previous = state
    out["qqe"] = {"dates": [dates[i] for i in w], **series, "state_changes": states}

    # 7. MACD_X: Feb-Jul 2026
    slow, fast = macd_pair(closes)
    w = span("2026-02-02", "2026-07-31")
    fires = {}
    for i in w:
        flags = macdx_flags(closes[:i + 1])
        on = {k: v for k, v in flags.items() if v}
        if on:
            entry = {"close": r(closes[i]), "macd_12_26": r(slow[i], 3), "prev_macd_12_26": r(slow[i - 1], 3),
                     "macd_5_15": r(fast[i], 3), "prev_macd_5_15": r(fast[i - 1], 3), "flags": sorted(on)}
            for key in ("bull_divergence", "bear_divergence"):
                if on.get(key):
                    p1, p2, m1, m2 = on[key]
                    entry[key] = {"price_pivots": [[dates[p1], r(closes[p1])], [dates[p2], r(closes[p2])]],
                                  "macd_pivots": [[dates[m1], r(slow[m1], 3)], [dates[m2], r(slow[m2], 3)]]}
            fires[dates[i]] = entry
    out["macdx"] = {"dates": [dates[i] for i in w], "macd_12_26": [r(slow[i], 3) for i in w],
                    "macd_5_15": [r(fast[i], 3) for i in w], "fires": fires}

    # 8. SMC: Jan-Aug 2025; the label the rolling year gives vs full history
    w = span("2025-01-02", "2025-08-29")
    rolling_events = {}
    for d in ("2025-04-04", "2025-06-27"):
        window = rolling(idx[d])
        rolling_events[d] = {"window_start": dates[window.start],
                             "events": [(dates[window.start + i], kind, dates[window.start + p] if p is not None else None, r(level))
                                        for i, kind, p, level in structure_events(highs[window], lows[window], closes[window], 50)]}
    part = rolling(idx["2025-06-27"])
    full_events = [(dates[i], kind, dates[p] if p is not None else None, r(level))
                   for i, kind, p, level in structure_events(highs, lows, closes, 50) if dates[i] >= "2024-01-01"]
    internal = [(dates[part.start + i], kind, r(level))
                for i, kind, p, level in structure_events(highs[part], lows[part], closes[part], 5)
                if p is None and "2025-01-02" <= dates[part.start + i] <= "2025-06-27"]
    out["smc"] = {"dates": [dates[i] for i in w], "close": [r(closes[i]) for i in w],
                  "rolling_year_swing_events_seen_on": rolling_events, "full_history_swing_events": full_events,
                  "rolling_year_internal_breaks": internal,
                  "detail": {d: {"close": r(closes[idx[d]]), "prev_close": r(closes[idx[d] - 1])} for d in ("2025-04-04", "2025-06-27")}}
    return out


# ---------------------------------------------------------------- draw

def at(dates, d):
    return dates.index(d)


def draw(data):
    src = data["source"]
    print(f"{src['ticker']} {src['rows']} daily rows {src['first']} .. {src['last']}")

    g = data["gaps"]
    candle_chart(HERE / "indicator-gaps.svg", [tuple(x) for x in g["ohlc"]],
                 title="SPY daily, Feb-Jun 2025: two gaps down, then both filled",
                 y_label="$ per share", x_labels=g["dates"],
                 marks=[(at(g["dates"], "2025-04-04"), "gaps down 4/3 + 4/4"), (at(g["dates"], "2025-04-09"), "fill 4/9"),
                        (at(g["dates"], "2025-04-29"), "fill 4/29"), (at(g["dates"], "2025-05-12"), "gap up 5/12")])

    u = data["utbot"]
    line_chart(HERE / "indicator-ut-bot.svg", {"SPY close": u["close"], "ATR trailing stop (key 1.0, ATR 10)": u["stop"]},
               title="UT Bot on SPY daily, Dec 2025 - Jun 2026", y_label="$ per share", x_labels=u["dates"],
               annotations=[(at(u["dates"], "2026-03-03"), "sell 3/3"), (at(u["dates"], "2026-03-31"), "buy 3/31"),
                            (at(u["dates"], "2026-05-15"), "sell 5/15")])

    e = data["ema"]
    line_chart(HERE / "indicator-ema-stack.svg",
               {"SPY close": e["close"], "EMA 20": e["ema20"], "EMA 50": e["ema50"], "EMA 100": e["ema100"], "EMA 200": e["ema200"]},
               title="SPY daily with EMA 20/50/100/200, Jan-Aug 2025", y_label="$ per share", x_labels=e["dates"],
               annotations=[(at(e["dates"], "2025-04-11"), "death cross 4/11"), (at(e["dates"], "2025-05-19"), "golden cross 5/19")])

    z = data["zerolag"]
    line_chart(HERE / "indicator-zero-lag-trend.svg",
               {"SPY close": z["close"], "ZLEMA 70": z["zlema"], "Upper band": z["upper"], "Lower band": z["lower"]},
               title="Zero Lag (70, 1.2) on SPY daily, Jan-Oct 2025", y_label="$ per share", x_labels=z["dates"],
               annotations=[(at(z["dates"], "2025-02-24"), "bear trend 2/24"), (at(z["dates"], "2025-04-24"), "bull trend 4/24"),
                            (at(z["dates"], "2025-10-10"), "bear trend 10/10")])

    t = data["trp"]["rows"]
    t_dates = [row["date"] for row in t]
    line_chart(HERE / "indicator-trend-reversal-probability.svg",
               {"Reversal probability, % (trailing 250 bars)": [round(row["probability"] * 100, 1) for row in t]},
               title="Trend Reversal Probability on SPY daily, Jan-Jul 2026", y_label="%", x_labels=t_dates,
               hlines=[(84, "0.84 high"), (98, "0.98 extreme")], pad=0.04,
               annotations=[(at(t_dates, "2026-03-12"), "3/12: 99.4%"), (at(t_dates, "2026-04-08"), "phase flips 4/8"),
                            (at(t_dates, "2026-05-27"), "5/27: 98.4%")])

    q = data["qqe"]
    line_chart(HERE / "indicator-qqe-mod.svg",
               {"Smoothed RSI(6) minus 50": q["rsi_minus_50"], "Bollinger upper (50, 0.35)": q["upper"], "Bollinger lower": q["lower"]},
               title="QQE MOD on SPY daily, Jan-Jun 2026", y_label="RSI points from 50", x_labels=q["dates"],
               hlines=[(3, "+3 threshold"), (-3, "-3 threshold")],
               annotations=[(at(q["dates"], "2026-03-03"), "sell starts 3/3"), (at(q["dates"], "2026-04-07"), "buy starts 4/7")])

    m = data["macdx"]
    line_chart(HERE / "indicator-macd-x.svg", {"MACD 12/26": m["macd_12_26"], "MACD 5/15": m["macd_5_15"]},
               title="MACD_X on SPY daily, Feb-Jul 2026", y_label="$ (EMA difference)", x_labels=m["dates"],
               hlines=[(0, "zero")],
               annotations=[(at(m["dates"], "2026-04-08"), "trend buy 4/8"), (at(m["dates"], "2026-06-04"), "bear divergence 6/4"),
                            (at(m["dates"], "2026-06-09"), "trend sell 6/9")])

    s = data["smc"]
    line_chart(HERE / "indicator-smc-structure.svg", {"SPY close": s["close"]},
               title="SPY daily, Jan-Aug 2025: swing structure (size 50), one-year window", y_label="$ per share", x_labels=s["dates"],
               hlines=[(613.23, "swing high 613.23"), (510.27, "swing low 510.27 (2024)"), (481.80, "swing low 481.80")],
               annotations=[(at(s["dates"], "2025-04-04"), "bearish BOS 4/4 (as seen from 6/27)"), (at(s["dates"], "2025-06-27"), "bullish CHoCH 6/27")])
    print("wrote", sorted(p.name for p in HERE.glob("indicator-*.svg")))


if __name__ == "__main__":
    if "--refresh" in sys.argv or not DATA.exists():
        DATA.write_text(json.dumps(compute(), indent=1))
    draw(json.loads(DATA.read_text()))
