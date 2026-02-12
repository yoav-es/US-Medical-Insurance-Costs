import pandas as pd

# WHO BMI classification (used consistently by compute_bmi_stats and compute_smoker_bmi_stats)
BMI_BINS = [0, 18.5, 25, 30, float("inf")]
BMI_LABELS = ["Underweight", "Healthy", "Overweight", "Obese"]


def summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    '''Return descriptive statistics for numeric columns.'''
    return df.describe(include="number")


def group_by_smoker_charges(df: pd.DataFrame) -> pd.DataFrame:
    '''Return mean charges grouped by smoker status.'''
    if "smoker" in df.columns and "charges" in df.columns:
        return df.groupby("smoker")["charges"].mean().reset_index()
    return pd.DataFrame()


def compute_region_stats(df: pd.DataFrame) -> tuple[pd.DataFrame, str]:
    """Compute region-level statistics.

    Returns (region_stats, region_with_max_cost)
    """
    region_stats = (
        df.groupby("region", observed=True)["charges"]
        .agg(mean_charge="mean", sd_cost="std", count="size")
        .assign(pct_share=lambda d: d["count"] / len(df) * 100)
        .reset_index()
    )

    region_with_max_cost = region_stats.loc[region_stats["mean_charge"].idxmax(), "region"]
    return region_stats, region_with_max_cost


def compute_bmi_stats(df: pd.DataFrame, bins=None, labels=None) -> tuple[pd.DataFrame, float]:
    """Compute BMI class statistics. Returns (bmi_stats, overall_mean)."""
    if bins is None:
        bins = BMI_BINS
    if labels is None:
        labels = BMI_LABELS
    df = df.copy()
    df["bmi_class"] = pd.cut(df["bmi"], bins=bins, labels=labels, right=False)
    bmi_stats = (
        df.groupby("bmi_class", observed=True)["charges"]
        .agg(
            mean_charge="mean",
            median_charge="median",
            sd_charge="std",
            iqr_charge=lambda x: x.quantile(0.75) - x.quantile(0.25),
            count="size",
        )
        .assign(pct_share=lambda d: d["count"] / len(df) * 100)
    )
    overall_mean = df["charges"].mean()
    bmi_stats["mean_ratio"] = bmi_stats["mean_charge"] / overall_mean
    return bmi_stats, overall_mean


def compute_smoker_bmi_stats(df: pd.DataFrame) -> tuple[pd.DataFrame, float, float]:
    """Return pivot table of mean charges by bmi_class and smoker, plus correlations (smokers, nonsmokers)."""
    d = df.copy()
    # ensure bmi_class exists (uses same classification as compute_bmi_stats)
    if "bmi_class" not in d.columns:
        d["bmi_class"] = pd.cut(d["bmi"], bins=BMI_BINS, labels=BMI_LABELS, right=False)
    mean_table = d.pivot_table(index="bmi_class", columns="smoker", values="charges", aggfunc="mean")
    if "yes" in mean_table.columns and "no" in mean_table.columns:
        mean_table["gap_pct"] = (mean_table["yes"] / mean_table["no"] - 1) * 100
    # correlations
    r_smokers = df[df.smoker == "yes"][["bmi", "charges"]].corr().loc["bmi", "charges"]
    r_nonsmokers = df[df.smoker == "no"][["bmi", "charges"]].corr().loc["bmi", "charges"]
    return mean_table, r_smokers, r_nonsmokers
