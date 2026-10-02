"""Figures for Technical Analysis Complete.

Run from this directory:  cd figures && python3 make_figures.py

Every chart redraws a result the lesson text already states, from the same
public data the lessons cite: Yahoo Finance daily bars for SPY (lessons 6-9)
and SPY 5-minute bars for one session (lesson 11). The first run fetches the
series from Yahoo's chart API and caches the raw responses in data/; later
runs are offline. The 5-minute cache matters: Yahoo only serves intraday bars
for the trailing 60 days, so the 16 Sep 2026 session cannot be re-fetched
after mid-November 2026.

Lesson 10's bar chart and lesson 12's diagram use numbers and rules the
lessons state; they need no series.

Values are checked against the lesson text before drawing. A mismatch raises,
so a figure can never quietly disagree with the prose beside it.
"""
from __future__ import annotations

import datetime as dt
import json
import math
import sys
import urllib.request
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
# figures -> technical -> courses -> content -> repo root, where scripts/svgfig.py lives
sys.path.insert(0, str(HERE.parents[3] / "scripts"))
from svgfig import bar_chart, candle_chart, flow_diagram, line_chart  # noqa: E402

DATA = HERE / "data"
NEW_YORK = ZoneInfo("America/New_York")
YAHOO = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?period1={start}&period2={end}&interval={interval}"


# ---------------------------------------------------------------- data

def _epoch(year, month, day):
    return int(dt.datetime(year, month, day, tzinfo=dt.timezone.utc).timestamp())


def fetch_bars(symbol, start, end, interval, cache_name):
    """Return [(timestamp, open, high, low, close, volume)] in New York time,
    prices rounded to cents to match Yahoo's historical-data page."""
    DATA.mkdir(exist_ok=True)
    cache = DATA / cache_name
    if not cache.exists():
        url = YAHOO.format(symbol=symbol, start=start, end=end, interval=interval)
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            cache.write_bytes(response.read())
    result = json.loads(cache.read_text())["chart"]["result"][0]
    quote = result["indicators"]["quote"][0]
    bars = []
    for stamp, o, h, l, c, v in zip(result["timestamp"], quote["open"], quote["high"],
                                     quote["low"], quote["close"], quote["volume"]):
        if c is None:
            continue
        when = dt.datetime.fromtimestamp(stamp, NEW_YORK)
        bars.append((when, round(o, 2), round(h, 2), round(l, 2), round(c, 2), v))
    return bars


def check(label, actual, expected, places=2):
    if round(actual, places) != round(expected, places):
        raise SystemExit(f"{label}: computed {actual!r}, lesson says {expected!r}")


# ---------------------------------------------------------------- indicators

def sma(values, length):
    out = [None] * len(values)
    running = 0.0
    for i, v in enumerate(values):
        running += v
        if i >= length:
            running -= values[i - length]
        if i >= length - 1:
            out[i] = running / length
    return out


def ema(values, length):
    k = 2 / (length + 1)
    out = []
    current = values[0]
    for i, v in enumerate(values):
        current = v if i == 0 else current + k * (v - current)
        out.append(current)
    return out


def rsi(values, length):
    """Wilder RSI: simple average over the first `length` changes, then k = 1/n."""
    out = [None] * len(values)
    changes = [values[i] - values[i - 1] for i in range(1, len(values))]
    gains = [max(ch, 0) for ch in changes]
    losses = [max(-ch, 0) for ch in changes]
    avg_gain = sum(gains[:length]) / length
    avg_loss = sum(losses[:length]) / length
    for i in range(length, len(changes)):
        if i > length:
            avg_gain += (gains[i] - avg_gain) / length
            avg_loss += (losses[i] - avg_loss) / length
        out[i + 1] = 100.0 if avg_loss == 0 else 100 - 100 / (1 + avg_gain / avg_loss)
    return out


def bollinger(values, length=20, width=2.0):
    middle = sma(values, length)
    upper, lower = [None] * len(values), [None] * len(values)
    for i in range(length - 1, len(values)):
        window = values[i - length + 1:i + 1]
        mean = middle[i]
        deviation = math.sqrt(sum((x - mean) ** 2 for x in window) / length)
        upper[i], lower[i] = mean + width * deviation, mean - width * deviation
    return middle, upper, lower


# ---------------------------------------------------------------- figures

def window(bars, first, last):
    return [b for b in bars if first <= b[0].date() <= last]


def day_labels(bars):
    return [b[0].strftime("%-d %b") for b in bars]


def figure_sma_cross(daily):
    """Lesson 6: SPY candles, Jan-Sep 2025, SMA 50 and 200, both 2025 crosses marked."""
    closes = [b[4] for b in daily]
    sma50, sma200 = sma(closes, 50), sma(closes, 200)
    dates = [b[0].date() for b in daily]
    golden = dates.index(dt.date(2025, 7, 1))
    death = dates.index(dt.date(2025, 4, 14))
    check("1 Jul 2025 SMA(50)", sma50[golden], 583.10)
    check("1 Jul 2025 SMA(200)", sma200[golden], 582.04)
    check("1 Jul 2025 close", closes[golden], 617.65)
    assert sma50[golden - 1] < sma200[golden - 1] < sma50[golden] + 1, "not a golden cross"
    check("14 Apr 2025 close", closes[death], 539.12)

    first, last = dt.date(2025, 1, 2), dt.date(2025, 9, 30)
    keep = [i for i, d in enumerate(dates) if first <= d <= last]
    ohlc = [daily[i][1:5] for i in keep]
    candle_chart(
        "spy-sma-50-200-cross-2025.svg",
        ohlc,
        title="SPY daily, Jan-Sep 2025: 50-day and 200-day SMA crosses",
        y_label="$",
        x_labels=[dates[i].strftime("%-d %b") for i in keep],
        overlays={"SMA 50": [sma50[i] for i in keep], "SMA 200": [sma200[i] for i in keep]},
        marks=[(keep.index(death), "14 Apr death cross"),
               (keep.index(golden), "1 Jul golden cross")],
    )


def figure_rsi(daily):
    """Lesson 7: RSI(2) and RSI(14), Sep-Nov 2022, with the 10 and 90 lines."""
    closes = [b[4] for b in daily]
    rsi2, rsi14 = rsi(closes, 2), rsi(closes, 14)
    dates = [b[0].date() for b in daily]
    low_day = dates.index(dt.date(2022, 10, 12))
    check("12 Oct 2022 RSI(2)", rsi2[low_day], 5.29)
    check("12 Oct 2022 RSI(14)", rsi14[low_day], 34.65)

    first, last = dt.date(2022, 9, 1), dt.date(2022, 11, 30)
    keep = [i for i, d in enumerate(dates) if first <= d <= last]
    line_chart(
        "spy-rsi2-rsi14-sep-nov-2022.svg",
        {"RSI(2)": [rsi2[i] for i in keep], "RSI(14)": [rsi14[i] for i in keep]},
        title="SPY, Sep-Nov 2022: RSI(2) against RSI(14)",
        y_label="RSI",
        x_labels=[dates[i].strftime("%-d %b") for i in keep],
        hlines=[(10, "RSI(2) < 10"), (90, "RSI(2) > 90"), (30, "RSI(14) < 30")],
        annotations=[(keep.index(low_day), "12 Oct: RSI(2) 5.3")],
    )


def figure_macd(daily):
    """Lesson 8: MACD line, signal line and histogram, Sep-Dec 2022."""
    closes = [b[4] for b in daily]
    ema12, ema26 = ema(closes, 12), ema(closes, 26)
    macd = [a - b for a, b in zip(ema12, ema26)]
    signal = ema(macd, 9)
    histogram = [a - b for a, b in zip(macd, signal)]
    dates = [b[0].date() for b in daily]
    oct13 = dates.index(dt.date(2022, 10, 13))
    check("13 Oct 2022 MACD", macd[oct13], -8.557, 3)
    check("13 Oct 2022 signal", signal[oct13], -8.842, 3)
    check("13 Oct 2022 histogram", histogram[oct13], 0.286, 3)
    oct28 = dates.index(dt.date(2022, 10, 28))
    check("28 Oct 2022 histogram peak", histogram[oct28], 3.58)
    dec6 = dates.index(dt.date(2022, 12, 6))
    assert histogram[dec6] < 0 < histogram[dec6 - 1], "6 Dec 2022 is not a bearish cross"
    check("6 Dec 2022 close", closes[dec6], 393.83)

    first, last = dt.date(2022, 9, 1), dt.date(2022, 12, 30)
    keep = [i for i, d in enumerate(dates) if first <= d <= last]
    # Histogram first: annotations attach to the first series, and all three
    # marked events (two sign flips and the peak) are histogram events.
    line_chart(
        "spy-macd-sep-dec-2022.svg",
        {"Histogram": [histogram[i] for i in keep],
         "MACD line": [macd[i] for i in keep],
         "Signal line": [signal[i] for i in keep]},
        title="SPY MACD(12, 26, 9), Sep-Dec 2022",
        y_label="points",
        x_labels=[dates[i].strftime("%-d %b") for i in keep],
        hlines=[(0, "zero")],
        annotations=[(keep.index(oct13), "13 Oct: 3rd signal cross in 6 days"),
                     (keep.index(oct28), "28 Oct: histogram peak +3.58"),
                     (keep.index(dec6), "6 Dec bearish cross")],
    )


def figure_bollinger(daily):
    """Lesson 9: SPY candles with 20-day, 2-sigma Bollinger Bands, Sep-Nov 2022."""
    closes = [b[4] for b in daily]
    middle, upper, lower = bollinger(closes)
    dates = [b[0].date() for b in daily]
    oct13 = dates.index(dt.date(2022, 10, 13))
    check("13 Oct 2022 SMA(20)", middle[oct13], 369.70, 1)
    check("13 Oct 2022 upper band", upper[oct13], 388.60)
    check("13 Oct 2022 lower band", lower[oct13], 350.79)
    check("13 Oct 2022 low", daily[oct13][3], 348.11)

    first, last = dt.date(2022, 9, 1), dt.date(2022, 11, 30)
    keep = [i for i, d in enumerate(dates) if first <= d <= last]
    candle_chart(
        "spy-bollinger-bands-sep-nov-2022.svg",
        [daily[i][1:5] for i in keep],
        title="SPY daily, Sep-Nov 2022: 20-day SMA and 2-sigma Bollinger Bands",
        y_label="$",
        x_labels=[dates[i].strftime("%-d %b") for i in keep],
        overlays={"SMA 20": [middle[i] for i in keep],
                  "Upper band": [upper[i] for i in keep],
                  "Lower band": [lower[i] for i in keep]},
        marks=[(keep.index(oct13), "13 Oct low 348.11")],
    )


def figure_breakouts():
    """Lesson 10: counts stated in the lesson (50-day closing-high breakouts, ten years)."""
    spy_total, spy_failed = 219, 163
    aapl_total, aapl_failed = 172, 110
    check("SPY failure rate", 100 * spy_failed / spy_total, 74.4, 1)
    check("AAPL failure rate", 100 * aapl_failed / aapl_total, 64.0, 1)
    bar_chart(
        "breakout-failure-counts-spy-aapl.svg",
        ["SPY held", "SPY failed (74.4%)", "AAPL held", "AAPL failed (64.0%)"],
        [spy_total - spy_failed, spy_failed, aapl_total - aapl_failed, aapl_failed],
        title="50-day closing-high breakouts, 2016-2026: held vs closed below the level in 20 days",
        y_label="breakouts",
        y_fmt=lambda v: f"{v:.0f}",
        colors=["#7eff5c", "#ff4d6a", "#7eff5c", "#ff4d6a"],
        pad=0,  # counts start at zero; padding would draw a negative region
    )


def figure_opening_range(five_minute):
    """Lesson 11: the 16 Sep 2026 session, 30-minute opening range, entry and stop."""
    session = [b for b in five_minute
               if b[0].date() == dt.date(2026, 9, 16) and dt.time(9, 30) <= b[0].time() < dt.time(16, 0)]
    assert len(session) == 78, f"expected 78 regular-session bars, got {len(session)}"
    opening = session[:6]
    range_high = max(b[2] for b in opening)
    range_low = min(b[3] for b in opening)
    check("16 Sep 2026 range high", range_high, 760.43)
    check("16 Sep 2026 range low", range_low, 758.72)
    times = [b[0].time() for b in session]
    entry = times.index(dt.time(11, 0))
    check("11:00 close", session[entry][4], 760.53)
    stop = next(i for i, b in enumerate(session) if i > entry and b[3] <= range_low)
    assert times[stop] == dt.time(14, 30), f"stop bar is {times[stop]}, lesson says 14:30"
    check("16:00 close", session[-1][4], 754.07)

    candle_chart(
        "spy-opening-range-2026-09-16.svg",
        [b[1:5] for b in session],
        title="SPY 5-minute bars, 16 Sep 2026: 30-minute opening range breakout",
        y_label="$",
        x_labels=[t.strftime("%H:%M") for t in times],
        overlays={"Range high 760.43": [range_high] * len(session),
                  "Range low 758.72": [range_low] * len(session)},
        marks=[(entry, "11:00 long 760.53"), (stop, "14:30 stop 758.72")],
    )


def figure_checklist():
    """Lesson 12: the five-part checklist, with the worked example's rules as notes."""
    flow_diagram(
        "rules-checklist-flow.svg",
        ["1. Regime filter", "2. Setup", "3. Entry", "4. Exit if wrong, exit if right", "5. Size"],
        title="A rules-based checklist: every part answerable yes or no from the data",
        notes=["Close above the 200-day SMA",
               "RSI(2) below 10, Wilder smoothing",
               "Next day's open; one position at a time",
               "Rule A: first close above the 5-day SMA. Rule B: 1 ATR stop, 2 ATR target, 10 days",
               "Shares = 0.5% of account / (entry - stop)"],
    )


def main():
    daily = fetch_bars("SPY", _epoch(2016, 9, 1), _epoch(2026, 9, 25), "1d", "spy-daily.json")
    five_minute = fetch_bars("SPY", _epoch(2026, 9, 14), _epoch(2026, 9, 23), "5m", "spy-5m-2026-09-14-to-22.json")
    figure_sma_cross(daily)
    figure_rsi(daily)
    figure_macd(daily)
    figure_bollinger(daily)
    figure_breakouts()
    figure_opening_range(five_minute)
    figure_checklist()
    print("wrote", sorted(p.name for p in HERE.glob("*.svg")))


if __name__ == "__main__":
    main()
