import pandas as pd
from insurance_costs.analysis import (
    compute_region_stats,
    compute_bmi_stats,
    compute_smoker_bmi_stats,
)


def test_compute_region_stats():
    df = pd.DataFrame({"region": ["a", "b", "a"], "charges": [100, 200, 300]})
    region_stats, region_with_max = compute_region_stats(df)
    assert "region" in region_stats.columns
    assert region_with_max in region_stats["region"].values


def test_compute_bmi_stats():
    df = pd.DataFrame({"bmi": [17, 22, 27, 32], "charges": [100, 200, 300, 400]})
    bmi_stats, overall_mean = compute_bmi_stats(df)
    assert "mean_charge" in bmi_stats.columns
    assert overall_mean == 250.0


def test_compute_smoker_bmi_stats():
    df = pd.DataFrame(
        {"bmi": [20, 30, 20, 30], "charges": [100, 200, 150, 250], "smoker": ["yes", "no", "yes", "no"]}
    )
    mean_table, r_smokers, r_nonsmokers = compute_smoker_bmi_stats(df)
    assert "yes" in mean_table.columns and "no" in mean_table.columns
    assert isinstance(r_smokers, float) and isinstance(r_nonsmokers, float)
