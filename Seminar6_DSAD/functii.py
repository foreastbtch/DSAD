import pandas as pd
from pandas.api.types import is_numeric_dtype


def nan_replace(t):
    assert isinstance(t, pd.DataFrame)
    nume_variabile = list(t.columns)
    for v in nume_variabile:
        if any(t[v].isna()):
            if is_numeric_dtype(t[v]):
                t[v].fillna(t[v].mean(), inplace=True)
            else:
                modulul = t[v].mode()[0]
                t[v].fillna(modulul, inplace=True)
