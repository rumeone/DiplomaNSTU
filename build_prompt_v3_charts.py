#!/usr/bin/env python3
"""Build PNG chart report for prompt v3 results using matplotlib."""

from __future__ import annotations

from html import escape
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


DEEPSEEK_DIR = Path("outputs_deepseek_prompt_v3")
GROK_DIR = Path("outputs_grok_prompt_v3")
OUTPUT_DIR = Path("charts/prompt_v3_report")

STRATEGIES = [
    "zero_shot",
    "constraint_guided",
    "structured_cot",
    "self_refine",
]

LABELS = {
    "zero_shot": "Zero-shot",
    "constraint_guided": "Constraint-guided",
    "structured_cot": "Structured CoT",
    "self_refine": "Self-refine",
}

COLORS = {
    "zero_shot": "#4C72B0",
    "constraint_guided": "#55A868",
    "structured_cot": "#C44E52",
    "self_refine": "#8172B3",
}

MODEL_COLORS = {
    "DeepSeek": "#4C72B0",
    "Grok": "#DD8452",
}

LLM_COLUMNS = [
    ("llm_readability", "Readability"),
    ("llm_maintainability", "Maintainability"),
    ("llm_correctness", "Correctness"),
    ("llm_efficiency", "Efficiency"),
    ("llm_pythonic_style", "Code Style"),
    ("llm_overall_score", "Overall"),
]


def load_results(base_dir: Path) -> pd.DataFrame:
    path = base_dir / "reports" / "raw_results.csv"

    if not path.exists():
        raise FileNotFoundError(path)

    df = pd.read_csv(path)

    numeric_cols = [
        "pylint_score",
        "radon_cc_avg",
        "radon_cc_max",
        "radon_mi",
        *[col for col, _ in LLM_COLUMNS],
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df["passed_bool"] = (
        df["passed"]
        .astype(str)
        .str.lower()
        .map({"true": True, "false": False})
        .fillna(False)
    )

    df["code_lines"] = (
        df["code"]
        .fillna("")
        .map(lambda text: len(str(text).splitlines()))
    )

    return df


def ensure_output() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_png(fig, filename: str) -> str:
    ensure_output()

    path = OUTPUT_DIR / filename

    fig.savefig(
        path,
        dpi=220,
        bbox_inches="tight",
    )

    plt.close(fig)

    return filename


def metric_values(df: pd.DataFrame, col: str) -> list[float]:
    return [
        float(
            df.loc[
                df["strategy"] == strategy,
                col,
            ]
            .dropna()
            .mean()
        )
        for strategy in STRATEGIES
    ]


def pass_rates(df: pd.DataFrame) -> list[float]:
    return [
        float(
            df.loc[
                df["strategy"] == strategy,
                "passed_bool",
            ].mean()
        )
        * 100
        for strategy in STRATEGIES
    ]


def bar_chart(
    title: str,
    values: list[float],
    ylabel: str,
    filename: str,
    max_value: float | None = None,
    suffix: str = "",
) -> str:
    fig, ax = plt.subplots(figsize=(10, 6))

    labels = [LABELS[s] for s in STRATEGIES]
    colors = [COLORS[s] for s in STRATEGIES]

    bars = ax.bar(
        labels,
        values,
        color=colors,
    )

    ax.set_title(
        title,
        fontsize=18,
        weight="bold",
    )

    ax.set_ylabel(ylabel)

    if max_value:
        ax.set_ylim(0, max_value)

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.4,
    )

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{value:.2f}{suffix}",
            ha="center",
            va="bottom",
            fontsize=10,
            weight="bold",
        )

    return save_png(fig, filename)


def grouped_bar_chart(
    title: str,
    deepseek_values: list[float],
    grok_values: list[float],
    ylabel: str,
    filename: str,
    max_value: float | None = None,
    suffix: str = "",
) -> str:
    fig, ax = plt.subplots(figsize=(11, 6))

    x = np.arange(len(STRATEGIES))
    width = 0.35

    bars1 = ax.bar(
        x - width / 2,
        deepseek_values,
        width,
        label="DeepSeek",
        color=MODEL_COLORS["DeepSeek"],
    )

    bars2 = ax.bar(
        x + width / 2,
        grok_values,
        width,
        label="Grok",
        color=MODEL_COLORS["Grok"],
    )

    ax.set_xticks(x)

    ax.set_xticklabels([
        LABELS[s]
        for s in STRATEGIES
    ])

    ax.set_ylabel(ylabel)

    ax.set_title(
        title,
        fontsize=18,
        weight="bold",
    )

    if max_value:
        ax.set_ylim(0, max_value)

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.4,
    )

    ax.legend()

    for bars in [bars1, bars2]:
        for bar in bars:
            h = bar.get_height()

            ax.text(
                bar.get_x() + bar.get_width() / 2,
                h,
                f"{h:.1f}{suffix}",
                ha="center",
                va="bottom",
                fontsize=9,
            )

    return save_png(fig, filename)


def stacked_pylint_distribution(
    df: pd.DataFrame,
    model: str,
    filename: str,
) -> str:
    ranges = [
        ("0-2", 0, 2),
        ("2-4", 2, 4),
        ("4-6", 4, 6),
        ("6-8", 6, 8),
        ("8-10", 8, 10.0001),
    ]

    data = {}

    for strategy in STRATEGIES:
        scores = df.loc[
            df["strategy"] == strategy,
            "pylint_score",
        ].dropna()

        vals = []

        for _, low, high in ranges:
            pct = (
                ((scores >= low) & (scores < high)).mean()
                * 100
            )

            vals.append(pct)

        data[LABELS[strategy]] = vals

    chart_df = pd.DataFrame(
        data,
        index=[r[0] for r in ranges],
    ).T

    fig, ax = plt.subplots(figsize=(10, 6))

    chart_df.plot(
        kind="bar",
        stacked=True,
        ax=ax,
    )

    ax.set_ylabel("Percent")

    ax.set_title(
        f"{model}: Pylint Score Distribution",
        fontsize=18,
        weight="bold",
    )

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.4,
    )

    ax.legend(title="Score range")

    return save_png(fig, filename)


def heatmap(
    title: str,
    row_labels: list[str],
    col_labels: list[str],
    matrix: list[list[float]],
    filename: str,
    vmin=0.0,
    vmax=10.0,
) -> str:
    fig, ax = plt.subplots(figsize=(10, 5))

    im = ax.imshow(
        matrix,
        cmap="Blues",
        vmin=vmin,
        vmax=vmax,
    )

    ax.set_xticks(np.arange(len(col_labels)))
    ax.set_yticks(np.arange(len(row_labels)))

    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

    plt.setp(
        ax.get_xticklabels(),
        rotation=20,
        ha="right",
    )

    for i in range(len(row_labels)):
        for j in range(len(col_labels)):
            ax.text(
                j,
                i,
                f"{matrix[i][j]:.2f}",
                ha="center",
                va="center",
                color="black",
                fontsize=10,
                weight="bold",
            )

    ax.set_title(
        title,
        fontsize=18,
        weight="bold",
    )

    fig.colorbar(im)

    return save_png(fig, filename)


def diff_heatmap(
    deepseek: pd.DataFrame,
    grok: pd.DataFrame,
    filename: str,
) -> str:
    rows = [
        (
            "Pass rate",
            [
                g - d
                for d, g in zip(
                    pass_rates(deepseek),
                    pass_rates(grok),
                )
            ],
        ),
        (
            "Pylint",
            [
                g - d
                for d, g in zip(
                    metric_values(deepseek, "pylint_score"),
                    metric_values(grok, "pylint_score"),
                )
            ],
        ),
        (
            "Radon MI",
            [
                g - d
                for d, g in zip(
                    metric_values(deepseek, "radon_mi"),
                    metric_values(grok, "radon_mi"),
                )
            ],
        ),
        (
            "CC avg*",
            [
                d - g
                for d, g in zip(
                    metric_values(deepseek, "radon_cc_avg"),
                    metric_values(grok, "radon_cc_avg"),
                )
            ],
        ),
        (
            "LLM Overall",
            [
                g - d
                for d, g in zip(
                    metric_values(
                        deepseek,
                        "llm_overall_score",
                    ),
                    metric_values(
                        grok,
                        "llm_overall_score",
                    ),
                )
            ],
        ),
    ]

    data = np.array([r[1] for r in rows])

    fig, ax = plt.subplots(figsize=(10, 5))

    vmax = np.abs(data).max()

    im = ax.imshow(
        data,
        cmap="RdYlGn",
        vmin=-vmax,
        vmax=vmax,
    )

    ax.set_xticks(np.arange(len(STRATEGIES)))

    ax.set_xticklabels([
        LABELS[s]
        for s in STRATEGIES
    ])

    ax.set_yticks(np.arange(len(rows)))

    ax.set_yticklabels([
        r[0]
        for r in rows
    ])

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(
                j,
                i,
                f"{data[i, j]:+.2f}",
                ha="center",
                va="center",
                fontsize=10,
                weight="bold",
            )

    ax.set_title(
        "Grok minus DeepSeek",
        fontsize=18,
        weight="bold",
    )

    fig.colorbar(im)

    return save_png(fig, filename)


def scatter(
    df: pd.DataFrame,
    model: str,
    filename: str,
) -> str:
    fig, ax = plt.subplots(figsize=(9, 7))

    for strategy in STRATEGIES:
        sub = df[
            df["strategy"] == strategy
        ]

        ax.scatter(
            sub["pylint_score"],
            sub["llm_overall_score"],
            label=LABELS[strategy],
            color=COLORS[strategy],
            alpha=0.65,
        )

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    ax.set_xlabel("Pylint score")
    ax.set_ylabel("LLM overall")

    ax.set_title(
        f"{model}: Pylint vs LLM Overall",
        fontsize=18,
        weight="bold",
    )

    ax.grid(
        True,
        linestyle="--",
        alpha=0.4,
    )

    ax.legend()

    return save_png(fig, filename)


def summary_table(df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for strategy in STRATEGIES:
        sub = df[
            df["strategy"] == strategy
        ]

        rows.append(
            {
                "Strategy": LABELS[strategy],
                "Pass rate": f"{sub['passed_bool'].mean() * 100:.2f}%",
                "Pylint": f"{sub['pylint_score'].mean():.2f}",
                "CC avg": f"{sub['radon_cc_avg'].mean():.2f}",
                "MI": f"{sub['radon_mi'].mean():.2f}",
                "LLM overall": f"{sub['llm_overall_score'].mean():.2f}",
            }
        )

    return pd.DataFrame(rows)


def html_table(df: pd.DataFrame) -> str:
    return df.to_html(
        index=False,
        escape=False,
        classes="summary",
    )

def boxplot_metric(
    df: pd.DataFrame,
    metric: str,
    title: str,
    ylabel: str,
    filename: str,
    ylim: tuple[float, float] | None = None,
) -> str:
    fig, ax = plt.subplots(figsize=(10, 6))

    data = [
        df.loc[
            df["strategy"] == strategy,
            metric,
        ].dropna()
        for strategy in STRATEGIES
    ]

    bp = ax.boxplot(
        data,
        patch_artist=True,
        tick_labels=[LABELS[s] for s in STRATEGIES],
        widths=0.6,
        medianprops=dict(
            color="black",
            linewidth=2,
        ),
    )

    for patch, strategy in zip(bp["boxes"], STRATEGIES):
        patch.set_facecolor(COLORS[strategy])
        patch.set_alpha(0.7)

    ax.set_title(
        title,
        fontsize=18,
        weight="bold",
    )

    ax.set_ylabel(ylabel)

    if ylim:
        ax.set_ylim(*ylim)

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.4,
    )

    return save_png(fig, filename)


def build_html(
    images: list[tuple[str, str]],
    deepseek: pd.DataFrame,
    grok: pd.DataFrame,
) -> None:
    cards = "\n".join(
        f'<section><h2>{escape(title)}</h2><img src="{escape(filename)}" alt="{escape(title)}"></section>'
        for title, filename in images
    )

    html = f"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Prompt v3 Charts</title>

<style>
body {{
    font-family: Arial, sans-serif;
    margin: 32px;
    color: #222;
}}

h1 {{
    margin-bottom: 4px;
}}

h2 {{
    margin-top: 36px;
}}

img {{
    max-width: 100%;
    border: 1px solid #ddd;
    background: white;
}}

table.summary {{
    border-collapse: collapse;
    margin: 12px 0 28px;
}}

table.summary th,
table.summary td {{
    border: 1px solid #ccc;
    padding: 6px 10px;
    text-align: right;
}}

table.summary th:first-child,
table.summary td:first-child {{
    text-align: left;
}}

.note {{
    color: #666;
}}
</style>

</head>

<body>

<h1>Prompt v3 Experiment Charts</h1>

<p class="note">
Sources:
outputs_deepseek_prompt_v3/reports and
outputs_grok_prompt_v3/reports.
</p>

<h2>DeepSeek Summary</h2>

{html_table(summary_table(deepseek))}

<h2>Grok Summary</h2>

{html_table(summary_table(grok))}

{cards}

</body>
</html>
"""

    ensure_output()

    (OUTPUT_DIR / "index.html").write_text(
        html,
        encoding="utf-8",
    )


def main() -> None:
    deepseek = load_results(DEEPSEEK_DIR)
    grok = load_results(GROK_DIR)

    deepseek_llm = [
        [
            float(
                deepseek.loc[
                    deepseek["strategy"] == s,
                    col,
                ].mean()
            )
            for s in STRATEGIES
        ]
        for col, _ in LLM_COLUMNS
    ]

    grok_llm = [
        [
            float(
                grok.loc[
                    grok["strategy"] == s,
                    col,
                ].mean()
            )
            for s in STRATEGIES
        ]
        for col, _ in LLM_COLUMNS
    ]

    images = [
        (
            "DeepSeek pass rate",
            bar_chart(
                "DeepSeek: Functional Pass Rate",
                pass_rates(deepseek),
                "Pass rate, %",
                "01_deepseek_pass_rate.png",
                100,
                "%",
            ),
        ),
        (
            "DeepSeek Pylint boxplot",
            boxplot_metric(
                deepseek,
                "pylint_score",
                "DeepSeek: Pylint Score Distribution by Strategy",
                "Pylint Score (0-10)",
                "20_deepseek_pylint_boxplot.png",
                (0, 10),
            ),
        ),
        (
            "Grok Pylint boxplot",
            boxplot_metric(
                grok,
                "pylint_score",
                "Grok: Pylint Score Distribution by Strategy",
                "Pylint Score (0-10)",
                "21_grok_pylint_boxplot.png",
                (0, 10),
            ),
        ),
        (
            "DeepSeek Pylint mean",
            bar_chart(
                "DeepSeek: Pylint Mean Score",
                metric_values(deepseek, "pylint_score"),
                "Pylint score",
                "02_deepseek_pylint.png",
                10,
            ),
        ),
        (
            "DeepSeek Pylint distribution",
            stacked_pylint_distribution(
                deepseek,
                "DeepSeek",
                "03_deepseek_pylint_distribution.png",
            ),
        ),
        (
            "DeepSeek Radon MI",
            bar_chart(
                "DeepSeek: Maintainability Index",
                metric_values(deepseek, "radon_mi"),
                "MI",
                "04_deepseek_mi.png",
                100,
            ),
        ),
        (
            "DeepSeek CC average",
            bar_chart(
                "DeepSeek: Average Cyclomatic Complexity",
                metric_values(deepseek, "radon_cc_avg"),
                "CC avg",
                "05_deepseek_cc.png",
            ),
        ),
        (
            "DeepSeek LLM heatmap",
            heatmap(
                "DeepSeek: LLM-Judge Mean Scores",
                [label for _, label in LLM_COLUMNS],
                [LABELS[s] for s in STRATEGIES],
                deepseek_llm,
                "06_deepseek_llm_heatmap.png",
                0,
                10,
            ),
        ),
        (
            "DeepSeek Pylint vs LLM",
            scatter(
                deepseek,
                "DeepSeek",
                "07_deepseek_scatter.png",
            ),
        ),
        (
            "Grok pass rate",
            bar_chart(
                "Grok: Functional Pass Rate",
                pass_rates(grok),
                "Pass rate, %",
                "08_grok_pass_rate.png",
                100,
                "%",
            ),
        ),
        (
            "Grok Pylint mean",
            bar_chart(
                "Grok: Pylint Mean Score",
                metric_values(grok, "pylint_score"),
                "Pylint score",
                "09_grok_pylint.png",
                10,
            ),
        ),
        (
            "Grok Pylint distribution",
            stacked_pylint_distribution(
                grok,
                "Grok",
                "10_grok_pylint_distribution.png",
            ),
        ),
        (
            "Grok Radon MI",
            bar_chart(
                "Grok: Maintainability Index",
                metric_values(grok, "radon_mi"),
                "MI",
                "11_grok_mi.png",
                100,
            ),
        ),
        (
            "Grok CC average",
            bar_chart(
                "Grok: Average Cyclomatic Complexity",
                metric_values(grok, "radon_cc_avg"),
                "CC avg",
                "12_grok_cc.png",
            ),
        ),
        (
            "Grok LLM heatmap",
            heatmap(
                "Grok: LLM-Judge Mean Scores",
                [label for _, label in LLM_COLUMNS],
                [LABELS[s] for s in STRATEGIES],
                grok_llm,
                "13_grok_llm_heatmap.png",
                0,
                10,
            ),
        ),
        (
            "DeepSeek vs Grok pass rate",
            grouped_bar_chart(
                "DeepSeek vs Grok: Functional Pass Rate",
                pass_rates(deepseek),
                pass_rates(grok),
                "Pass rate, %",
                "14_compare_pass_rate.png",
                100,
                "%",
            ),
        ),
        (
            "DeepSeek vs Grok Pylint",
            grouped_bar_chart(
                "DeepSeek vs Grok: Pylint Mean Score",
                metric_values(deepseek, "pylint_score"),
                metric_values(grok, "pylint_score"),
                "Pylint score",
                "15_compare_pylint.png",
                10,
            ),
        ),
        (
            "DeepSeek vs Grok Radon MI",
            grouped_bar_chart(
                "DeepSeek vs Grok: Maintainability Index",
                metric_values(deepseek, "radon_mi"),
                metric_values(grok, "radon_mi"),
                "MI",
                "16_compare_mi.png",
                100,
            ),
        ),
        (
            "DeepSeek vs Grok CC average",
            grouped_bar_chart(
                "DeepSeek vs Grok: Average Cyclomatic Complexity",
                metric_values(deepseek, "radon_cc_avg"),
                metric_values(grok, "radon_cc_avg"),
                "CC avg",
                "17_compare_cc.png",
            ),
        ),
        (
            "DeepSeek vs Grok LLM overall",
            grouped_bar_chart(
                "DeepSeek vs Grok: LLM Overall",
                metric_values(
                    deepseek,
                    "llm_overall_score",
                ),
                metric_values(
                    grok,
                    "llm_overall_score",
                ),
                "Score",
                "18_compare_llm.png",
                10,
            ),
        ),
        (
            "DeepSeek vs Grok metric deltas",
            diff_heatmap(
                deepseek,
                grok,
                "19_compare_delta_heatmap.png",
            ),
        ),
    ]

    build_html(
        images,
        deepseek,
        grok,
    )

    print(f"saved: {OUTPUT_DIR / 'index.html'}")
    print(f"saved PNG charts: {len(images)}")


if __name__ == "__main__":
    main()