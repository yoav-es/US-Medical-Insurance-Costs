import pandas as pd
from insurance_costs.viz import plot_correlation


def test_plot_correlation(tmp_path):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    out = tmp_path / "corr.png"
    fig = plot_correlation(df, out_path=out)
    assert fig is not None
    assert out.exists()
