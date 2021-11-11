import pandas as pd
from functii import nan_replace, tabelare_matrice
from acp import acp
from grafice import plot_corelatii, corelograma, plot_instante, show
import numpy as np

t = pd.read_csv("Mortalitate.csv", index_col=0)
nan_replace(t)

model_acp = acp(t)
model_acp.fit()
tabel_varianta = model_acp.tabelare_varianta()
print(tabel_varianta)
tabel_varianta.to_csv("Varianta.csv")
model_acp.plot_varianta()
r_xc = model_acp.r_xc

r_xc_t = tabelare_matrice(r_xc,
                          t.columns,
                          model_acp.etichete_componente,
                          "r_xc.csv")
nrcomp = min(model_acp.nrcomp_p, model_acp.nrcomp_k, model_acp.nrcomp_c)
for i in range(1, nrcomp):
    plot_corelatii(r_xc_t, "comp1", model_acp.etichete_componente[i], aspect=1)
corelograma(r_xc_t)

t_comp = tabelare_matrice(model_acp.c,
                          t.index,
                          model_acp.etichete_componente,
                          "comp.csv")

plot_instante(t_comp, "comp1", "comp2", aspect=1)
plot_instante(t_comp, "comp1", "comp5", aspect=1)

# Calcul scoruri
s = model_acp.c / np.sqrt(model_acp.alpha)
t_scoruri = tabelare_matrice(s, t.index, model_acp.etichete_componente, "s.csv")
plot_instante(t_scoruri, "comp1", "comp2", titlu="Plot scoruri", aspect=1)

# Calcul cosinusuri
c2 = model_acp.c * model_acp.c
cosin = np.transpose(c2.T / np.sum(c2, axis=1))
t_cosin = tabelare_matrice(cosin, t.index, model_acp.etichete_componente, "cosin.csv")

# Calcul contributii
contrib = c2 * 100 / np.sum(c2, axis=0)
t_contrib = tabelare_matrice(contrib, t.index, model_acp.etichete_componente, "contrib.csv")

# Comunalitati

show()
