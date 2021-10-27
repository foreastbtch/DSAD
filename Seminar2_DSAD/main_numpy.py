import pandas as pd
import numpy as np
import functii as f

tabel = pd.read_csv("Mortalitate.csv", index_col=0)
# print(tabel, type(tabel))
nume_instante = list(tabel.index)
nume_variabile = list(tabel.columns)
# print(nume_variabile, nume_instante, sep="\n")
# dictionar = {"c1": (3, 4, 5), "c2": (5, 8, 9)}
# print(dictionar["c2"])
# print(list(dictionar))
x = tabel.values
# print(x, type(x))

# Inlocuire valori lipsa cu mediile

f.nan_replace(x)
# exit(0)

# Calcul matrice de corelatii
r = np.corrcoef(x, rowvar=False)
print("Matrice de corelatii:", r, sep="\n")
