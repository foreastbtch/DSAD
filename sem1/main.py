import functii as f

nume_fisier = "Mortalitate.csv"

fisier = open(nume_fisier, "r")
# print(type(fisier))

linii = fisier.readlines()
# print(linii)
# for linie in linii:
#     print(linie[:-1])
# Preluare nume de variabile
nume_variabile = linii[0][:-1].split(",")
# print(nume_variabile)
# Preluare date in lista de tupluri.
tabel = []
for i in range(1, len(linii)):
    t = linii[i][:-1].split(",")
    # print(t)
    instanta = []
    instanta.append(t[0])
    for j in range(1, len(t)):
        instanta.append(float(t[j]) if t[j] != '' else 0)
    tabel.append(tuple(instanta))
print("Tabelul de date:")
for i in tabel:
    print(i)

# Calcul numar total de cazuri pe tari
tabel_mortalitate = f.sume(tabel)
print("Tabelul cu mortalitatea insumata:")
for i in tabel_mortalitate:
    print(i)

# Calcul medii pe variabile
k = 4
print("Media pentru variabila", nume_variabile[k], "este:", f.medie(tabel, k=k))

# Filtrare
# Filtrare tari cu RM_Adulti>100

i_filtru1 = filter(f.filtru_RM_Adulti, tabel)
tabel1 = [i for i in i_filtru1]
print("Tari cu Rm_Adulti>100:")
for i in tabel1:
    print(i)

limita1 = 100
limita2 = 200
i_filtru2 = filter(lambda x: f.filtru(x, k, limita1, limita2), tabel)
tabel2 = [i for i in i_filtru2]
print("Tari cu", nume_variabile[k], "intre", limita1, "si", limita2, ":")
for i in tabel2:
    print(i)

# Sortari
i_sort = sorted(tabel, key=lambda x: f.sortare(x, k))
tabel3 = [i for i in i_sort]

# Salvare tabel sortat in fisier text
f_out = open("f_sort.csv", "w")
f_out.write(",".join(nume_variabile))
f_out.write("\n")
for i in tabel3:
    t = [str(j) for j in i]
    f_out.write(",".join(t))
    f_out.write("\n")
f_out.close()

# Mapare
i_map = map(lambda x: f.selector(x, 0, 1, 3, 5, 7), tabel)
tabel4 = [i for i in i_map]
print("Noul tabel:")
for i in tabel4:
    print(i)
