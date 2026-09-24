"""Figures for Stock Market Foundations.

Run from this directory:  cd figures && python3 make_figures.py

Every number below is taken from the lesson it illustrates (its worked
example or its described chart); nothing is fitted or invented. Each figure
notes its lesson and the source the lesson cites.
"""
import sys
from pathlib import Path

# scripts/ sits at the repo root: figures -> foundations -> courses -> content -> root
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
from svgfig import COLORS, bar_chart, flow_diagram, line_chart  # noqa: E402

OUT = Path(__file__).resolve().parent


def trade_lifecycle():
    """Lesson 1 worked example: 10 AAPL at the 31 Dec 2024 close (250.42),
    T+1 settlement rolling over the 1 Jan holiday to Thu 2 Jan 2025.
    Source: SEC T+1 resources; NYSE trading calendar."""
    flow_diagram(
        OUT / "trade-lifecycle.svg",
        steps=[
            "Order sent",
            "Broker routes",
            "Filled at NBBO",
            "NSCC clears and nets",
            "DTC settles T+1",
        ],
        title="Trade lifecycle: 10 AAPL bought at the close, Tue 31 Dec 2024",
        notes=[
            "10 shares, 2,504.20 dollars at 250.42",
            "retail market order: usually a wholesaler",
            "250.41 bid / 250.42 ask; fill 250.415",
            "tape print in ms; one net obligation per broker",
            "Thu 2 Jan 2025 (1 Jan holiday): shares in, cash out",
        ],
    )


def spread_cost():
    """Lesson 2: the spread expressed in basis points of the midpoint.
    AAPL 0.01 / 250.415 = 0.4 bps (worked example); a 5-cent spread on a
    5-dollar stock = 100 bps and a 20-cent spread on a 10-dollar stock =
    200 bps (lesson text); the hypothetical 4-dollar stock with bid 3.98 /
    ask 4.06 = 0.08 / 4.02 = 199 bps (worked example)."""
    bar_chart(
        OUT / "spread-cost-basis-points.svg",
        labels=["AAPL 250.42, 1c spread", "5-dollar stock, 5c", "4-dollar stock, 8c", "10-dollar stock, 20c"],
        values=[0.4, 100, 199, 200],
        title="Round-trip cost of the spread, in basis points of price",
        y_label="basis points (1 bp = 0.01%)",
        y_fmt=lambda v: f"{v:g} bps",
    )


def earnings_decomposition():
    """Lesson 5 described chart: EPS estimate 5.00 -> 5.50 (+10%), multiple
    30 -> 24 (-20%), price 150 -> 132 (-12%). Price = EPS x P/E. Each term is
    indexed to 100 before the report so the three changes share one axis."""
    before = COLORS[1]  # "after" bars are coloured by direction of change
    bar_chart(
        OUT / "earnings-times-multiple.svg",
        labels=["EPS 5.00", "EPS 5.50", "P/E 30", "P/E 24", "Price 150", "Price 132"],
        values=[100, 110, 100, 80, 100, 88],
        title="Price = EPS x P/E: before and after the report, indexed to 100",
        y_label="before the report = 100",
        colors=[before, COLORS[0], before, COLORS[3], before, COLORS[3]],
    )


def total_return():
    """Lesson 8 described chart: 10,000 dollars, 5% annual price growth, 3%
    dividend yield, 20 years. Price only 26,533; dividends taken as cash
    36,450 (price plus about 9,920 of accumulated dividends); dividends
    reinvested 10,000 x 1.08^20 = 46,610."""
    years = list(range(21))
    price_only = [10_000 * 1.05 ** t for t in years]
    # each year's dividend is 3% of that year's share value, kept as cash
    dividends_as_cash = [p + 300 * (1.05 ** t - 1) / 0.05 for t, p in zip(years, price_only)]
    reinvested = [10_000 * 1.08 ** t for t in years]
    line_chart(
        OUT / "total-return-vs-price-return.svg",
        {
            "Dividends reinvested (total return, 8%/yr)": reinvested,
            "Dividends taken as cash": dividends_as_cash,
            "Price only (5%/yr)": price_only,
        },
        title="10,000 dollars over 20 years: 5% price growth, 3% dividend yield",
        y_label="value, dollars",
        x_labels=[str(t) for t in years],
        annotations=[(20, "46,610")],
        hlines=[(26_533, "price only: 26,533")],
    )


def expense_ratio_drag():
    """Lesson 9 worked example: 10,000 dollars, 30 years, 7% gross index
    return, net of each fund's expense ratio (prospectuses as of 2024):
    VOO / IVV 0.03%, SPY 0.0945%, a hypothetical active fund at 0.75%."""
    years = list(range(31))

    def grow(net_rate):
        return [10_000 * (1 + net_rate) ** t for t in years]

    line_chart(
        OUT / "expense-ratio-drag-30-years.svg",
        {
            "No fee (7.00%)": grow(0.07),
            "VOO/IVV 0.03%": grow(0.0697),
            "SPY 0.0945%": grow(0.069055),
            "Active 0.75%": grow(0.0625),
        },
        title="10,000 dollars for 30 years at 7% gross, net of the expense ratio",
        y_label="value, dollars",
        x_labels=[str(t) for t in years],
        annotations=[(30, "no fee: 76,100")],
    )


def margin_loss():
    """Lesson 10 worked example: 10,000 dollars of capital, MSFT at 421.50.
    Margin account buys 47 shares (loan 9,810.50); cash account buys 23.
    A 10% decline costs 969 dollars in cash (9.7%) and 1,981.05 on margin
    (19.8%). A 30% decline (MSFT 295.05) leaves margin equity at 4,056.85,
    a loss of 5,943.15 (59.4%); in cash, 23 x 126.45 = 2,908.35 (29.1%)."""
    bar_chart(
        OUT / "margin-vs-cash-loss.svg",
        labels=["cash, MSFT -10%", "margin, MSFT -10%", "cash, MSFT -30%", "margin, MSFT -30%"],
        values=[969.45, 1_981.05, 2_908.35, 5_943.15],
        title="Dollars lost of your 10,000 when MSFT falls from 421.50",
        y_label="loss, dollars (cash: 23 shares; margin: 47 shares, 9,810.50 borrowed)",
        y_fmt=lambda v: f"{v:,.0f}",
        colors=[COLORS[3]] * 4,
    )


if __name__ == "__main__":
    trade_lifecycle()
    spread_cost()
    earnings_decomposition()
    total_return()
    expense_ratio_drag()
    margin_loss()
    print("wrote", sorted(p.name for p in OUT.glob("*.svg")))
