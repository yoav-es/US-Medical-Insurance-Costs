import pandas as pd


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    '''Lightweight preprocessing for the insurance dataset.'''
    df = df.copy()
    # cast common categorical columns to category dtype if present
    for col in ("sex", "smoker", "region"):
        if col in df.columns:
            df[col] = df[col].astype("category")
    # ensure numeric columns are numeric
    for col in ("age", "bmi", "children", "charges"):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df
