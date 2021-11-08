import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt


class acp():
    def __init__(self, t, variabile_observate=None):
        if variabile_observate is None:
            variabile_observate = list(t)
        self.__x = t[variabile_observate].values

    def fit(self, std=True, nlib=0):
        x_ = self.__x - np.mean(self.__x, axis=0)
        if std:
            x_ = x_ / np.std(self.__x, axis=0)
        n, m = np.shape(x_)
        r_cov = (1 / (n - nlib)) * x_.T @ x_
        # x transpus ori x
        valp, vecp = np.linalg.eig(r_cov)
        k = np.flipud(np.argsort(valp))
        self.__alpha = valp[k]
        # print(k, valp, self.__alpha, sep="\n")
        self.__a = vecp[:, k]
        self.__c = x_ @ self.__a
        self.etichete_componente = ["comp" + str(i + 1) for i in range(m)]

    def tabelare_varianta(self):
        procent_varianta = self.__alpha * 100 / np.sum(self.__alpha)
        tabel_varianta = DataFrame(
            data={
                "Varianta": self.alpha,
                "Procent varianta": procent_varianta,
                "Varianta cumulata": np.cumsum(self.__alpha),
                "Procent cumulat": np.cumsum(procent_varianta)
            }, index=self.etichete_componente
        )
        return tabel_varianta

    def plot_varianta(self):
        fig = plt.figure("Plot varianta", figsize=(12, 7))
        ax = fig.add_subplot(1, 1, 1)
        assert isinstance(ax, plt.Axes)
        ax.set_title("Plot varianta", fontdict={"fontsize": 16, "color": 'b'})
        ax.set_xlabel("Componente")
        ax.set_ylabel("Varianta")
        m = len(self.etichete_componente)
        x = np.arange(1, m + 1)
        ax.set_xticks(x)
        ax.plot(x, self.__alpha)
        ax.scatter(x, self.__alpha, c='r')
        ax.axhline(1, c='g', label="Kaiser")
        ax.legend()
        plt.show()

    @property
    def alpha(self):
        return self.__alpha

    @property
    def a(self):
        return self.__a

    @property
    def x(self):
        return self.__x

    @property
    def c(self):
        return self.__c
