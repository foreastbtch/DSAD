import pandas as pd
from functii import nan_replace
from acp import acp

t = pd.read_csv("Mortalitate.csv", index_col=0)
nan_replace(t)

model_acp = acp(t)
model_acp.fit()
tabel_varianta = model_acp.tabelare_varianta()
print(tabel_varianta)
tabel_varianta.to_csv("Varianta.csv")
model_acp.plot_varianta()
