import numpy as np
from scipy.stats import shapiro, kstest, norm, chi2


def nan_replace(x):
    is_nan = np.isnan(x)
    # print(is_nan)
    k = np.where(is_nan)
    # print(k)
    x[k] = np.nanmean(x[:, k[1]], axis=0)
    # axis = 0 calculul se face pe coloane


# Salvare matrice ndarray in fisier csv
def salvare(x, nume_linii=None, nume_coloane=None, nume_fisier="out.csv"):
    n = np.shape(x)[0]
    f = open(nume_fisier, "w")
    if nume_coloane is not None:
        if nume_linii is not None:
            f.write(",")
        f.write(",".join(nume_coloane) + "\n")
    for i in range(n):
        if nume_linii is not None:
            f.write(nume_linii[i] + ",")
        f.write(",".join([str(j) for j in x[i, :]]) + "\n")
    f.close()


# Standardizare/centrare matrice
def standardizare(x, scal=True, nlib=0):
    assert isinstance(x, np.ndarray)
    x_ = x - np.mean(x, axis=0)
    if scal:
        x_ /= np.std(x, axis=0, ddof=nlib)
    return x_


def teste_concordanta(x, p=0.05):
    n, m = np.shape(x)
    t_stat = np.empty((m, 6))
    t_test = np.empty((m, 3), dtype=bool)
    for i in range(m):
        v = x[:, i]
        t_stat[i, 0:2] = shapiro(v)
        t_stat[i, 2:4] = kstest(v, 'norm')
        t_stat[i, 4:6] = chi2_test(v)
    t_test[:, 0] = t_stat[:, 1] > p
    t_test[:, 1] = t_stat[:, 3] > p
    t_test[:, 2] = t_stat[:, 5] > p
    return t_stat, t_test


def chi2_test(v):
    f, l = np.histogram(v, bins='sturges')
    m = len(f)
    n = len(v)
    media = np.mean(v)
    std = np.std(v)
    # standard deviation
    d = norm.cdf(l[1:], media, std) - norm.cdf(l[:m], media, std)
    # cumulative distribution function
    fe = n * d
    # statistica_test = np.sum((f - fe) * (f - fe) / fe)
    # p_value = chi2.cdf(statistica_test, m - 1)
    # return statistica_test, p_value
    statistica_test = 0
    for i in range(m):
        if fe[i] != 0:
            statistica_test += ((f[i] - fe[i]) * (f[i] - fe[i]) / (fe[i] * fe[i]))
    p_value = 1 - chi2.cdf(statistica_test, m - 1)
    return statistica_test, p_value
