import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts")); from svgfig import *

HERE = Path(__file__).resolve().parent


def make_scoring_flow():
    flow_diagram(
        HERE / "how-a-phantom-signal-is-scored-flow.svg",
        ["Signals fire", "x learned weight", "CALL vs PUT tally", "Bonuses and multipliers", "35 pts, 3 signals, premium", "Confidence tier"],
        title="How a Phantom score is built",
        notes=[
            "8 indicators, classic signals, TradingView alerts",
            "1.0 is neutral; weight depends on context",
            "bigger side wins; ties are rejected",
            "PUT x1.10, +10 agreement, regime bias",
            "or 2 signals when one is premium",
            "HIGH 80+, MEDIUM 50+, LOW below",
        ],
    )


def make_gate_sequence():
    flow_diagram(
        HERE / "entry-gates-why-most-setups-never-post-sequence.svg",
        ["Fresh setup", "Trend and score", "Earnings and confirm", "Clock and VIX", "Contract checks", "Paper open"],
        title="Gates a setup passes before a paper open",
        notes=[
            "skip if today's move is over 2.5x ATR",
            "with-trend only; 35+ points and a premium signal",
            "5 days before to 1 day after; under 80 must repeat",
            "9:45 ET start, macro window, VIX 30 or below",
            "spread cap, $0.50 premium, OTM ceiling, live quote",
            "position caps still apply",
        ],
    )


if __name__ == "__main__":
    make_scoring_flow()
    make_gate_sequence()
    print("wrote", sorted(p.name for p in HERE.glob("*.svg")))
