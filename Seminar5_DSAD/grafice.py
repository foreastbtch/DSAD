import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.preprocessing as skpp


# Grafic linii


def lines(t, vars, titlu="Grafic linii", eticheta_x="X"):
    fig = plt.figure(figsize=(13, 7))
    # print(type(fig))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": 'b'})
    ax.set_xlabel(eticheta_x, fontdict={"fontsize": 12, "color": 'b'})
    for v in vars:
        ax.plot(t[v], label=v)
    ax.legend()
    plt.show()


def scatter3d(t, var1, var2, var3, titlu="Scatterplot 3D"):
    fig = plt.figure(figsize=(8, 8))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": 'b'})
    ax.set_xlabel(var1, fontdict={"fontsize": 12, "color": 'b'})
    ax.set_ylabel(var2, fontdict={"fontsize": 12, "color": 'b'})
    ax.set_zlabel(var3, fontdict={"fontsize": 13, "color": 'b'})
    ax.scatter(t[var1], t[var2], t[var3], c='r')
    nume_instante = list(t.index)
    for i in nume_instante:
        ax.text(t.loc[i, var1], t.loc[i, var2], t.loc[i, var3], i)
    plt.show()


def pie(t, var, by=None, titlu="Diagrama de structura"):
    assert isinstance(t, pd.DataFrame)
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": 'b'})
    if by is None:
        ax.pie(t[var], labels=t.index)
        ax.set_xlabel(var)
    else:
        tg = t[[var, by]].groupby(by=by).agg(np.mean)
        ax.pie(tg[var], labels=tg.index)
        ax.set_xlabel(var + ": Grupare dupa " + by)
    plt.show()


def bubble(t, var1, var2, var3, titlu="Bubble Chart"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": 'b'})
    ax.set_xlabel(var1, fontdict={"fontsize": 12, "color": 'b'})
    ax.set_ylabel(var1, fontdict={"fontsize": 12, "color": 'b'})
    scalare = skpp.MinMaxScaler(feature_range=(100, 2000))
    n = len(t)
    x = t[var3].values.reshape((n, 1))
    d = scalare.fit_transform(x)
    ax.scatter(t[var1], t[var2], s=d, alpha=0.5, label=var3)
    for i in range(n):
        ax.text(t[var1][i], t[var2][i], t.index[i])
    leg = ax.legend()
    for handle in leg.legendHandles:
        handle.set_sizes([50])
    plt.show()


def boxplot(t, vars, titlu="Grafic box"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": 'b'})
    ax.boxplot(t[vars].values, labels=vars, showmeans=True, meanline=True)
    plt.show()
