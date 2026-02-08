import pandas as pd
from insurance_costs.processing import preprocess


def test_preprocess_categories():
    df = pd.DataFrame({"sex": ["male"], "smoker": ["yes"], "region": ["south"], "age": [30]})
    out = preprocess(df)
    assert out["sex"].dtype.name == "category"
    assert out["smoker"].dtype.name == "category"
    assert out["age"].dtype.kind in ("i", "f")  # numeric
