from functii import citireTabelaDb
from nan_replace_pandas import nan_replace
from grafice import lines, scatter3d, pie, bubble, boxplot

t = citireTabelaDb("db5.db", "Teritorial", "Indicativ")
nan_replace(t)

# print(t)
variabile = list(t)
print(variabile)

# Grafic linii
lines(t, ['RataSom', 'RataAbScolar'], eticheta_x="Indicativ judete")

# Grafic puncte 3D = scatterplot
scatter3d(t, "PIB", "RataSom", "ExecBVenituri")

# Diagrama de structura
pie(t, "PIB")
# Diagrama de structura la nivel de regiune
pie(t, "PIB", "Regiunea")
# Diagrama de structura la nivel de macroregiune
pie(t, "PIB", "Macroregiunea")

# Bubble chart
bubble(t, "PIB", "Export", "ExecBVenituri")

# Box
boxplot(t, ["PIB", "Export", "ExecBVenituri"])
boxplot(t, ["Export", "ExecBVenituri"])
