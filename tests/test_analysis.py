import pandas as pd
from insurance_costs.analysis import summary_stats, group_by_smoker_charges


def test_summary_stats():
    df = pd.DataFrame({"age": [30, 40], "charges": [1000, 2000]})
    s = summary_stats(df)
    assert "charges" in s.columns
    assert s.loc["mean", "charges"] == 1500.0


def test_group_by_smoker_charges():
    df = pd.DataFrame({"smoker": ["yes", "no", "yes"], "charges": [100, 200, 300]})
    out = group_by_smoker_charges(df)
    assert out.shape[0] == 2
    assert "smoker" in out.columns
    # check mean calculation
    yes_mean = out.loc[out["smoker"] == "yes", "charges"].iloc[0]
    assert yes_mean == 200.0
