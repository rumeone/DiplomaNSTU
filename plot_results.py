#!/usr/bin/env python3
"""Build comparison charts for LLM code-generation experiment results.

Examples:
    python plot_results.py
    python plot_results.py --left-dir outputs_deepseek --right-dir outputs_grok
    python plot_results.py --left-dir outputs_deepseek_prompt_v2 --right-dir outputs_grok_prompt_v2 --output-dir charts/prompt_v2_compare
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

try:
    from scipy import stats
except ImportError:  # pragma: no cover - depends on local environment
    stats = None


STRATEGY_ORDER = ["zero_shot", "constraint_guided", "structured_cot", "self_refine"]
STRATEGY_LABELS = {
    "zero_shot": "Zero-Shot",
    "constraint_guided": "Constraint-\nGuided",
    "structured_cot": "Structured\nCoT",
    "self_refine": "Self-Refine",
}

LLM_DIMS = [
    "llm_readability",
    "llm_maintainability",
    "llm_correctness",
    "llm_efficiency",
    "llm_pythonic_style",
    "llm_overall_score",
]
LLM_LABELS = {
    "llm_readability": "Readability",
    "llm_maintainability": "Maintainability",
    "llm_correctness": "Correctness",
    "llm_efficiency": "Efficiency",
    "llm_pythonic_style": "Pythonic Style",
    "llm_overall_score": "Overall",
}

METRICS = [
    ("pylint_score", "Pylint Score (0-10)", "Pylint Score", True, (0, 10.5)),
    ("radon_mi", "Maintainability Index", "Maintainability Index", True, (0, 105)),
    ("radon_cc_avg", "Cyclomatic Complexity (avg)", "Cyclomatic Complexity", False, None),
    ("llm_overall_score", "LLM-Judge Overall (0-10)", "LLM-Judge Overall", True, (0, 10.5)),
]

LEFT_COLOR = "#4C72B0"
RIGHT_COLOR = "#DD8452"


@dataclass(frozen=True)
class ResultSet:
    """Loaded experiment result files for one model/run."""

    label: str
    raw: pd.DataFrame
    summary: pd.DataFrame | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate comparison charts from run_pipeline_async.py outputs.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--left-dir", type=Path, default=Path("outputs_deepseek"))
    parser.add_argument("--right-dir", type=Path, default=Path("outputs_grok"))
    parser.add_argument("--left-label", default="DeepSeek")
    parser.add_argument("--right-label", default="Grok")
    parser.add_argument("--output-dir", type=Path, default=Path("charts/compare"))
    parser.add_argument(
        "--strategy",
        action="append",
        choices=STRATEGY_ORDER,
        help="Strategy to include. Can be repeated. Defaults to all known strategies.",
    )
    return parser.parse_args()


def result_path(base_dir: Path, filename: str) -> Path:
    return base_dir / "reports" / filename


def load_raw(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"raw results not found: {path}")

    df = pd.read_csv(path)
    required = {"task_id", "strategy", "sample_index"}
    missing = sorted(required - set(df.columns))
    if missing:
        raise ValueError(f"{path} is missing required columns: {', '.join(missing)}")

    numeric_cols = [
        "pylint_score",
        "bandit_issues",
        "radon_cc_avg",
        "radon_cc_max",
        "radon_mi",
        *LLM_DIMS,
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    for col in ["pylint_score", *LLM_DIMS]:
        if col in df.columns:
            df.loc[(df[col] < 0) | (df[col] > 10), col] = np.nan

    if "radon_mi" in df.columns:
        df.loc[(df["radon_mi"] < 0) | (df["radon_mi"] > 100), "radon_mi"] = np.nan

    if "passed" in df.columns:
        df["passed_bool"] = df["passed"].astype(str).str.lower().map(
            {"true": True, "false": False}
        )

    return df


def load_summary(path: Path) -> pd.DataFrame | None:
    if not path.exists():
        return None
    df = pd.read_csv(path)
    if "strategy" not in df.columns:
        return None
    return df.set_index("strategy")


def load_result_set(base_dir: Path, label: str) -> ResultSet:
    return ResultSet(
        label=label,
        raw=load_raw(result_path(base_dir, "raw_results.csv")),
        summary=load_summary(result_path(base_dir, "summary.csv")),
    )


def available_strategies(frames: Iterable[pd.DataFrame], requested: list[str] | None) -> list[str]:
    if requested:
        return requested
    present: set[str] = set()
    for frame in frames:
        present.update(frame["strategy"].dropna().astype(str))
    return [strategy for strategy in STRATEGY_ORDER if strategy in present]


def means_and_stds(df: pd.DataFrame, strategies: list[str], col: str) -> tuple[list[float], list[float]]:
    means = []
    stds = []
    for strategy in strategies:
        values = df.loc[df["strategy"] == strategy, col].dropna()
        means.append(float(values.mean()) if not values.empty else np.nan)
        stds.append(float(values.std()) if len(values) > 1 else 0.0)
    return means, stds


def save_current(output_dir: Path, filename: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_dir / filename, dpi=180, bbox_inches="tight")
    plt.close()
    print(f"saved: {output_dir / filename}")


def grouped_bar(
    left: ResultSet,
    right: ResultSet,
    strategies: list[str],
    col: str,
    ylabel: str,
    title: str,
    filename: str,
    output_dir: Path,
    ylim: tuple[float, float] | None = None,
) -> None:
    if col not in left.raw.columns or col not in right.raw.columns:
        print(f"skipped {filename}: missing column {col}")
        return

    x = np.arange(len(strategies))
    width = 0.36
    fig, ax = plt.subplots(figsize=(10, 5.5))

    for index, (dataset, color) in enumerate([(left, LEFT_COLOR), (right, RIGHT_COLOR)]):
        means, stds = means_and_stds(dataset.raw, strategies, col)
        offset = (index - 0.5) * width
        bars = ax.bar(
            x + offset,
            means,
            width,
            yerr=stds,
            label=dataset.label,
            color=color,
            alpha=0.88,
            capsize=4,
            edgecolor="white",
        )
        for bar, mean in zip(bars, means):
            if np.isfinite(mean):
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height(),
                    f"{mean:.2f}",
                    ha="center",
                    va="bottom",
                    fontsize=8,
                )

    ax.set_xticks(x)
    ax.set_xticklabels([STRATEGY_LABELS[s] for s in strategies])
    ax.set_ylabel(ylabel)
    ax.set_title(f"{title}\nmean +/- std")
    if ylim:
        ax.set_ylim(*ylim)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    save_current(output_dir, filename)


def grouped_box(
    left: ResultSet,
    right: ResultSet,
    strategies: list[str],
    col: str,
    ylabel: str,
    title: str,
    filename: str,
    output_dir: Path,
) -> None:
    if col not in left.raw.columns or col not in right.raw.columns:
        print(f"skipped {filename}: missing column {col}")
        return

    pos_left = np.arange(1, len(strategies) * 3, 3)
    pos_right = pos_left + 1
    data_left = [left.raw.loc[left.raw["strategy"] == s, col].dropna().values for s in strategies]
    data_right = [right.raw.loc[right.raw["strategy"] == s, col].dropna().values for s in strategies]

    fig, ax = plt.subplots(figsize=(11, 5.5))
    bp_left = ax.boxplot(
        data_left,
        positions=pos_left,
        widths=0.75,
        patch_artist=True,
        medianprops={"color": "white", "linewidth": 2},
    )
    bp_right = ax.boxplot(
        data_right,
        positions=pos_right,
        widths=0.75,
        patch_artist=True,
        medianprops={"color": "white", "linewidth": 2},
    )
    for patch in bp_left["boxes"]:
        patch.set_facecolor(LEFT_COLOR)
        patch.set_alpha(0.82)
    for patch in bp_right["boxes"]:
        patch.set_facecolor(RIGHT_COLOR)
        patch.set_alpha(0.82)

    ax.set_xticks(pos_left + 0.5)
    ax.set_xticklabels([STRATEGY_LABELS[s] for s in strategies])
    ax.set_ylabel(ylabel)
    ax.set_title(f"{title}\ndistribution by strategy")
    ax.legend(
        handles=[
            mpatches.Patch(color=LEFT_COLOR, alpha=0.82, label=left.label),
            mpatches.Patch(color=RIGHT_COLOR, alpha=0.82, label=right.label),
        ]
    )
    ax.grid(axis="y", alpha=0.3)
    save_current(output_dir, filename)


def pass_rate_chart(
    left: ResultSet,
    right: ResultSet,
    strategies: list[str],
    output_dir: Path,
) -> None:
    def pass_rates(dataset: ResultSet) -> list[float]:
        if dataset.summary is not None and "pass_rate" in dataset.summary.columns:
            return [
                float(dataset.summary.loc[s, "pass_rate"]) * 100 if s in dataset.summary.index else np.nan
                for s in strategies
            ]
        if "passed_bool" not in dataset.raw.columns:
            return [np.nan for _ in strategies]
        return [
            float(dataset.raw.loc[dataset.raw["strategy"] == s, "passed_bool"].fillna(False).mean()) * 100
            for s in strategies
        ]

    x = np.arange(len(strategies))
    width = 0.36
    fig, ax = plt.subplots(figsize=(10, 5.5))
    for index, (dataset, color) in enumerate([(left, LEFT_COLOR), (right, RIGHT_COLOR)]):
        vals = pass_rates(dataset)
        bars = ax.bar(
            x + (index - 0.5) * width,
            vals,
            width,
            label=dataset.label,
            color=color,
            alpha=0.88,
            edgecolor="white",
        )
        for bar, value in zip(bars, vals):
            if np.isfinite(value):
                ax.text(bar.get_x() + bar.get_width() / 2, value, f"{value:.1f}%", ha="center", va="bottom", fontsize=8)

    ax.set_xticks(x)
    ax.set_xticklabels([STRATEGY_LABELS[s] for s in strategies])
    ax.set_ylim(0, 105)
    ax.set_ylabel("Pass Rate (%)")
    ax.set_title("Functional Pass Rate")
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    save_current(output_dir, "00_pass_rate.png")


def llm_dimensions_chart(left: ResultSet, right: ResultSet, strategies: list[str], output_dir: Path) -> None:
    dims = [dim for dim in LLM_DIMS if dim in left.raw.columns and dim in right.raw.columns]
    if not dims:
        print("skipped LLM dimensions chart: no LLM columns")
        return

    x = np.arange(len(strategies))
    width = 0.36
    rows = int(np.ceil(len(dims) / 3))
    fig, axes = plt.subplots(rows, 3, figsize=(16, 4.8 * rows), squeeze=False)
    fig.suptitle("LLM-Judge Dimensions", fontsize=14, y=1.01)

    for ax, dim in zip(axes.flat, dims):
        for index, (dataset, color) in enumerate([(left, LEFT_COLOR), (right, RIGHT_COLOR)]):
            means, stds = means_and_stds(dataset.raw, strategies, dim)
            ax.bar(
                x + (index - 0.5) * width,
                means,
                width,
                yerr=stds,
                label=dataset.label,
                color=color,
                alpha=0.88,
                capsize=3,
                edgecolor="white",
            )
        ax.set_xticks(x)
        ax.set_xticklabels([STRATEGY_LABELS[s] for s in strategies], fontsize=8)
        ax.set_ylim(0, 10.5)
        ax.set_ylabel("Score")
        ax.set_title(LLM_LABELS.get(dim, dim))
        ax.grid(axis="y", alpha=0.3)
        ax.legend(fontsize=8)

    for ax in axes.flat[len(dims):]:
        ax.axis("off")

    save_current(output_dir, "09_llm_dimensions.png")


def radar_chart(left: ResultSet, right: ResultSet, strategies: list[str], output_dir: Path) -> None:
    dims = [dim for dim in LLM_DIMS if dim != "llm_overall_score" and dim in left.raw.columns and dim in right.raw.columns]
    if len(dims) < 3:
        print("skipped radar chart: not enough LLM dimensions")
        return

    labels = [LLM_LABELS[d] for d in dims]
    angles = np.linspace(0, 2 * np.pi, len(dims), endpoint=False).tolist()
    angles += angles[:1]

    fig, axes = plt.subplots(1, len(strategies), figsize=(5 * len(strategies), 5), subplot_kw={"polar": True})
    if len(strategies) == 1:
        axes = [axes]
    fig.suptitle("LLM-Judge Profile by Strategy", fontsize=14, y=1.04)

    for ax, strategy in zip(axes, strategies):
        for dataset, color in [(left, LEFT_COLOR), (right, RIGHT_COLOR)]:
            vals = dataset.raw.loc[dataset.raw["strategy"] == strategy, dims].mean().tolist()
            vals += vals[:1]
            ax.plot(angles, vals, "o-", linewidth=2, label=dataset.label, color=color)
            ax.fill(angles, vals, alpha=0.1, color=color)
        ax.set_thetagrids(np.degrees(angles[:-1]), labels, fontsize=8)
        ax.set_ylim(0, 10)
        ax.set_title(STRATEGY_LABELS[strategy].replace("\n", " "))
        ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.15), fontsize=8)

    save_current(output_dir, "10_radar_by_strategy.png")


def paired_values(left: ResultSet, right: ResultSet, strategy: str, col: str) -> tuple[np.ndarray, np.ndarray]:
    keys = ["task_id", "strategy", "sample_index"]
    left_part = left.raw.loc[left.raw["strategy"] == strategy, keys + [col]].dropna()
    right_part = right.raw.loc[right.raw["strategy"] == strategy, keys + [col]].dropna()
    merged = left_part.merge(right_part, on=keys, suffixes=("_left", "_right"))
    return merged[f"{col}_left"].to_numpy(), merged[f"{col}_right"].to_numpy()


def heatmap_diff(left: ResultSet, right: ResultSet, strategies: list[str], output_dir: Path) -> None:
    rows = []
    row_labels = []
    for col, _, label, higher_better, _ in METRICS:
        if col not in left.raw.columns or col not in right.raw.columns:
            continue
        diff = []
        for strategy in strategies:
            left_mean = left.raw.loc[left.raw["strategy"] == strategy, col].mean()
            right_mean = right.raw.loc[right.raw["strategy"] == strategy, col].mean()
            value = right_mean - left_mean
            diff.append(value if higher_better else -value)
        rows.append(diff)
        row_labels.append(label)

    for dim in LLM_DIMS:
        if dim == "llm_overall_score" or dim not in left.raw.columns or dim not in right.raw.columns:
            continue
        diff = [
            right.raw.loc[right.raw["strategy"] == strategy, dim].mean()
            - left.raw.loc[left.raw["strategy"] == strategy, dim].mean()
            for strategy in strategies
        ]
        rows.append(diff)
        row_labels.append(LLM_LABELS[dim])

    if not rows:
        print("skipped heatmap: no comparable metrics")
        return

    matrix = np.array(rows, dtype=float)
    vmax = max(float(np.nanmax(np.abs(matrix))), 0.25)
    fig, ax = plt.subplots(figsize=(10, 0.55 * len(row_labels) + 3))
    im = ax.imshow(matrix, cmap="RdYlGn", aspect="auto", vmin=-vmax, vmax=vmax)
    ax.set_xticks(range(len(strategies)))
    ax.set_xticklabels([STRATEGY_LABELS[s] for s in strategies])
    ax.set_yticks(range(len(row_labels)))
    ax.set_yticklabels(row_labels)

    for i in range(len(row_labels)):
        for j in range(len(strategies)):
            value = matrix[i, j]
            if np.isfinite(value):
                ax.text(j, i, f"{value:+.3f}", ha="center", va="center", fontsize=9)

    plt.colorbar(im, ax=ax, label=f"Delta ({right.label} - {left.label}); green = {right.label} better")
    ax.set_title("Metric Difference Heatmap")
    save_current(output_dir, "11_metric_diff_heatmap.png")


def statistical_tests(left: ResultSet, right: ResultSet, strategies: list[str], output_dir: Path) -> None:
    if stats is None:
        print("skipped statistical tests: scipy is not installed")
        return

    rows = []
    comparable = [metric[0] for metric in METRICS if metric[0] in left.raw.columns and metric[0] in right.raw.columns]
    comparable.extend(dim for dim in LLM_DIMS if dim in left.raw.columns and dim in right.raw.columns and dim not in comparable)

    for col in comparable:
        for strategy in strategies:
            left_values, right_values = paired_values(left, right, strategy, col)
            if len(left_values) >= 3:
                test_name = "paired_ttest"
                t_stat, p_value = stats.ttest_rel(left_values, right_values, nan_policy="omit")
                diff = right_values - left_values
                effect = diff.mean() / diff.std(ddof=1) if diff.std(ddof=1) > 0 else 0.0
                left_mean = left_values.mean()
                right_mean = right_values.mean()
                n = len(left_values)
            else:
                left_values = left.raw.loc[left.raw["strategy"] == strategy, col].dropna().to_numpy()
                right_values = right.raw.loc[right.raw["strategy"] == strategy, col].dropna().to_numpy()
                if len(left_values) < 3 or len(right_values) < 3:
                    continue
                test_name = "welch_ttest"
                t_stat, p_value = stats.ttest_ind(left_values, right_values, equal_var=False)
                pooled_std = np.sqrt((left_values.std(ddof=1) ** 2 + right_values.std(ddof=1) ** 2) / 2)
                effect = (right_values.mean() - left_values.mean()) / pooled_std if pooled_std > 0 else 0.0
                left_mean = left_values.mean()
                right_mean = right_values.mean()
                n = min(len(left_values), len(right_values))

            rows.append(
                {
                    "metric": LLM_LABELS.get(col, col),
                    "strategy": strategy,
                    "test": test_name,
                    "n": n,
                    f"{left.label}_mean": round(float(left_mean), 4),
                    f"{right.label}_mean": round(float(right_mean), 4),
                    "mean_diff_right_minus_left": round(float(right_mean - left_mean), 4),
                    "t_stat": round(float(t_stat), 4),
                    "p_value": round(float(p_value), 6),
                    "effect_size": round(float(effect), 4),
                    "significant_0_05": bool(p_value < 0.05),
                }
            )

    output_dir.mkdir(parents=True, exist_ok=True)
    stat_df = pd.DataFrame(rows)
    stat_df.to_csv(output_dir / "12_stat_tests.csv", index=False, encoding="utf-8")
    print(f"saved: {output_dir / '12_stat_tests.csv'}")

    if stat_df.empty:
        return

    pivot = stat_df.pivot_table(index="metric", columns="strategy", values="p_value", aggfunc="first")
    pivot = pivot.reindex(columns=strategies)
    fig, ax = plt.subplots(figsize=(10, 0.55 * len(pivot.index) + 3))
    matrix = pivot.to_numpy(dtype=float)
    im = ax.imshow(matrix, cmap="RdYlGn_r", aspect="auto", vmin=0, vmax=0.2)
    ax.set_xticks(range(len(strategies)))
    ax.set_xticklabels([STRATEGY_LABELS[s] for s in strategies])
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            value = matrix[i, j]
            if np.isfinite(value):
                mark = "*" if value < 0.05 else ""
                ax.text(j, i, f"{value:.3f}{mark}", ha="center", va="center", fontsize=9)
    plt.colorbar(im, ax=ax, label="p-value; * = p < 0.05")
    ax.set_title("Statistical Significance")
    save_current(output_dir, "12_pvalue_heatmap.png")


def main() -> None:
    args = parse_args()
    left = load_result_set(args.left_dir, args.left_label)
    right = load_result_set(args.right_dir, args.right_label)
    strategies = available_strategies([left.raw, right.raw], args.strategy)
    if not strategies:
        raise SystemExit("No known strategies found in input files.")

    print(f"left:  {args.left_dir} ({left.label})")
    print(f"right: {args.right_dir} ({right.label})")
    print(f"out:   {args.output_dir}")
    print(f"strategies: {', '.join(strategies)}")

    pass_rate_chart(left, right, strategies, args.output_dir)

    for idx, (col, ylabel, title, _higher_better, ylim) in enumerate(METRICS, start=1):
        grouped_bar(left, right, strategies, col, ylabel, f"{title}: {left.label} vs {right.label}", f"{idx:02d}_{col}_bar.png", args.output_dir, ylim)
        grouped_box(left, right, strategies, col, ylabel, f"{title}: {left.label} vs {right.label}", f"{idx:02d}_{col}_box.png", args.output_dir)

    llm_dimensions_chart(left, right, strategies, args.output_dir)
    radar_chart(left, right, strategies, args.output_dir)
    heatmap_diff(left, right, strategies, args.output_dir)
    statistical_tests(left, right, strategies, args.output_dir)

    print("done")


if __name__ == "__main__":
    main()
