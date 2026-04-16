from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


def save_records_to_csv(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(records)
    df.to_csv(path, index=False, encoding="utf-8")


def save_records_to_json(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(records).to_json(path, orient="records", force_ascii=False, indent=2)


def _pass_rate_only_executed(passed: pd.Series) -> float:
    """Доля True среди строк, где тесты реально запускались (passed не null)."""
    s = passed.dropna()
    if s.empty:
        return float(np.nan)
    return float((s == True).mean())


def compute_summary(records: list[dict[str, Any]]) -> pd.DataFrame:
    df = pd.DataFrame(records)

    if df.empty:
        return pd.DataFrame()

    if "pylint_score" in df.columns:
        df["pylint_score"] = pd.to_numeric(df["pylint_score"], errors="coerce")
    else:
        df["pylint_score"] = np.nan

    if "bandit_issues" in df.columns:
        df["bandit_issues"] = pd.to_numeric(df["bandit_issues"], errors="coerce")
    else:
        df["bandit_issues"] = np.nan

    # Radon metrics
    if "radon_cc_avg" in df.columns:
        df["radon_cc_avg"] = pd.to_numeric(df["radon_cc_avg"], errors="coerce")
    else:
        df["radon_cc_avg"] = np.nan

    if "radon_cc_max" in df.columns:
        df["radon_cc_max"] = pd.to_numeric(df["radon_cc_max"], errors="coerce")
    else:
        df["radon_cc_max"] = np.nan

    if "radon_mi" in df.columns:
        df["radon_mi"] = pd.to_numeric(df["radon_mi"], errors="coerce")
    else:
        df["radon_mi"] = np.nan

    summary = (
        df.groupby("strategy", dropna=False)
        .agg(
            tasks=("task_id", "nunique"),
            generations=("task_id", "count"),
            generations_with_tests=("passed", lambda s: int(s.notna().sum())),
            pass_rate=("passed", _pass_rate_only_executed),
            avg_pylint=("pylint_score", "mean"),
            avg_bandit_issues=("bandit_issues", "mean"),
            # Radon metrics
            avg_cyclomatic_complexity=("radon_cc_avg", "mean"),
            max_cyclomatic_complexity=("radon_cc_max", "max"),
            avg_maintainability_index=("radon_mi", "mean"),
        )
        .reset_index()
    )

    return summary