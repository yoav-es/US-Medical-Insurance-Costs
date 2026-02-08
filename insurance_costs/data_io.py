from pathlib import Path
import pandas as pd
from typing import Union


def load_data(path: Union[str, Path]) -> pd.DataFrame:
    '''Load CSV data into a DataFrame.'''
    p = Path(path)
    return pd.read_csv(p)


def save_report(text: str, path: Union[str, Path]) -> None:
    '''Save a simple text report to disk.'''
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
