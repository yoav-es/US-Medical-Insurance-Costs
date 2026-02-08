import pandas as pd
from insurance_costs.data_io import load_data


def test_load_data(tmp_path):
    p = tmp_path / "sample.csv"
    p.write_text("age,sex,bmi,charges\n19,male,27.9,16884.92\n")
    df = load_data(p)
    assert df.shape[0] == 1
    assert "age" in df.columns
    assert df.iloc[0]["age"] == 19
