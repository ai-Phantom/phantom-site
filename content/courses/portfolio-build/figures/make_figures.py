"""Figures for "Building Your First Portfolio".

Every number below is copied from the lesson text it is embedded in (or is a
straight evaluation of a formula the lesson states, at points the lesson itself
works). Run from this directory:

    cd figures && python3 make_figures.py
"""
import sys
from pathlib import Path

# figures/ -> portfolio-build/ -> courses/ -> content/ -> repo root, which holds scripts/
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))

from svgfig import COLORS, H, MUTED, PAD_B, PAD_L, PAD_R, W, bar_chart, flow_diagram, line_chart  # noqa: E402

BLUE, YELLOW, RED = COLORS[1], COLORS[2], COLORS[3]


def pct(v):
    return f"{v:+.2f}".rstrip("0").rstrip(".") + "%"


def add_two_line_x_labels(path, label_pairs):
    """bar_chart draws one-line x labels; ten ticker pairs do not fit in one line
    each, so the chart is generated with blank labels and each pair is written
    beneath its bar on two lines, using the same slot geometry as bar_chart."""
    svg = Path(path).read_text()
    slot = (W - PAD_L - PAD_R) / len(label_pairs)
    extra = []
    for i, (top, bottom) in enumerate(label_pairs):
        x = PAD_L + i * slot + slot / 2
        for j, text in enumerate((top, bottom)):
            y = H - PAD_B + 18 + j * 13
            extra.append(f"<text x='{x:.1f}' y='{y}' fill='{MUTED}' text-anchor='middle' font-size='11'>{text}</text>")
    Path(path).write_text(svg.replace("</svg>", "\n".join(extra) + "\n</svg>"))


def recovery_arithmetic():
    """Lesson 9, table: gain required to return to the prior peak, L / (1 - L).
    The -90% row (+900%) is left off so the smaller bars stay legible."""
    losses = [10, 20, 25, 30, 40, 50, 60, 75]
    gains = [11.1, 25.0, 33.3, 42.9, 66.7, 100.0, 150.0, 300.0]
    bar_chart(
        "recovery-arithmetic.svg",
        [f"−{L}%" for L in losses],
        gains,
        title="Gain required to recover a drawdown: L ÷ (1 − L)",
        y_label="gain needed, %",
        y_fmt=pct,
        colors=[RED] * len(gains),
    )


def sp500_drawdowns():
    """Lesson 9: the four largest S&P 500 price drawdowns since 2000."""
    bar_chart(
        "sp500-drawdowns-since-2000.svg",
        ["Mar 2000–Oct 2002", "Oct 2007–Mar 2009", "Feb–Mar 2020", "Jan–Oct 2022"],
        [-49.1, -56.8, -33.9, -25.4],
        title="S&P 500: four largest price drawdowns since 2000",
        y_label="peak to trough, %",
        y_fmt=pct,
    )


def tech_pairwise_correlations():
    """Lesson 3, table: the ten pairwise correlations among AAPL, MSFT, GOOGL,
    AMZN and NVDA (daily returns, 2019-2023, rounded to one decimal)."""
    pairs = [
        ("AAPL", "MSFT", 0.7), ("AAPL", "GOOGL", 0.6), ("AAPL", "AMZN", 0.6), ("AAPL", "NVDA", 0.6),
        ("MSFT", "GOOGL", 0.7), ("MSFT", "AMZN", 0.6), ("MSFT", "NVDA", 0.6),
        ("GOOGL", "AMZN", 0.6), ("GOOGL", "NVDA", 0.5),
        ("AMZN", "NVDA", 0.5),
    ]
    path = "tech-pairwise-correlations.svg"
    bar_chart(
        path,
        [""] * len(pairs),
        [c for _, _, c in pairs],
        title="Correlation of daily returns between five technology stocks, 2019\u20132023",
        y_fmt=lambda v: f"{v:.1f}",
        colors=[BLUE] * len(pairs),
    )
    add_two_line_x_labels(path, [(a, b) for a, b, _ in pairs])


def position_weight_vs_stop_distance():
    """Lesson 5: shares = (account x risk) / (entry - stop), so position weight
    = risk per trade / stop distance. Evaluated for the lesson's 1% and 2% risk
    levels; the two worked points ($45 and $47.50 stops on a $50 entry) are
    annotated and the 15% weight cap is the lesson's example cap."""
    stop_distances = list(range(5, 21))  # 5% .. 20% below entry
    one_percent = [1.0 / d * 100 for d in stop_distances]
    two_percent = [2.0 / d * 100 for d in stop_distances]
    line_chart(
        "position-weight-vs-stop-distance.svg",
        {"1% risk per position": one_percent, "2% risk per position": two_percent},
        title="Position weight implied by the risk-per-trade rule",
        y_label="position weight, % of account",
        x_labels=[f"{d}% stop" for d in stop_distances],
        y_fmt=lambda v: f"{v:.0f}%",
        annotations=[
            (stop_distances.index(5), "stop $47.50: 100 shares, 20%"),
            (stop_distances.index(10), "stop $45: 50 shares, 10%"),
        ],
        hlines=[(15, "15% weight cap: take the smaller")],
    )


def capstone_stress_shocks():
    """Lesson 13, Parts 4-6: portfolio return under each shock, with and
    without the written stops, against the 25% risk budget."""
    labels = ["Market −20%, beta", "Market −20%, stops", "NVDA −50%, no stop", "NVDA −50%, stop hit", "Risk budget"]
    values = [-17.7, -14.7, -6.25, -2.0, -25.0]
    bar_chart(
        "capstone-stress-shocks.svg",
        labels,
        values,
        title="Capstone: the two shocks against the $10,000 sample portfolio",
        y_label="portfolio return, %",
        y_fmt=pct,
        colors=[RED, RED, YELLOW, YELLOW, MUTED],
    )


def rebalancing_rule_flow():
    """Lesson 8, 'The rule to write down': calendar check, threshold act."""
    flow_diagram(
        "rebalancing-rule-flow.svg",
        [
            "Fixed check date, twice a year",
            "Compare each weight to its target",
            "Inside the band: do nothing",
            "Outside: use cash flows first",
            "Still outside: sell to target",
        ],
        title="Rebalancing rule: check on the calendar, act on the threshold",
        notes=[
            "No trades between dates unless a satellite hits its stop",
            "Core: ±5 points. Satellite: ±25% of its target weight",
            "Wait for the next check date",
            "New contributions, dividends, the cash reserve. No sale, no tax",
            "Highest-basis, longest-held lots; mind the 30-day wash-sale rule",
        ],
    )


if __name__ == "__main__":
    recovery_arithmetic()
    sp500_drawdowns()
    tech_pairwise_correlations()
    position_weight_vs_stop_distance()
    capstone_stress_shocks()
    rebalancing_rule_flow()
    print("wrote 6 figures")
