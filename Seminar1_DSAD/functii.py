def sume(tabel):
    t = []
    for i in tabel:
        t.append((i[0], sum(i[1:len(i)])))
    return t


def medie(tabel, k=1):
    s = 0
    for i in tabel:
        s = s + i[k]
    return s / len(tabel)


def filtru_RM_Adulti(instanta):
    if instanta[1] > 100:
        return True
    else:
        return False


def filtru(instanta, k, l1, l2):
    if instanta[k] >= l1 and instanta[k] <= l2:
        return True
    else:
        return False


def sortare(instanta, k):
    return instanta[k]


def selector(instanta, *k):
    instanta_noua = []
    for i in k:
        instanta_noua.append(instanta[i])
    return tuple(instanta_noua)
