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
        if std:
            self.nrcomp_k = np.where(self.alpha < 1)[0][0]
        else:
            self.nrcomp_k = None
        pondere = np.cumsum(self.alpha / sum(self.alpha))
        self.nrcomp_p = np.where(pondere > 0.8)[0][0] + 1
        #     where => ([],....,[])
        # pentru vector => ([])
        # pentru matrice=>([],[])
        eps = self.alpha[:(m - 1)] - self.alpha[1:]
        # print(eps)
        sigma = eps[:(m - 2)] - eps[1:]
        print(sigma)
        exista_negative = sigma < 0
        if any(exista_negative):
            self.nrcomp_c = np.where(exista_negative)[0][0] + 2
        else:
            self.nrcomp_c = None
        if std:
            self.r_xc = self.a * np.sqrt(self.__alpha)
            # r_xc=r corelatie intre x si c
        else:
            self.r_xc = np.corrcoef(self.__x, self.__c, rowvar=False)[:m, m:]
            # rowvar=false => sunt asezate pe coloane

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
        if self.nrcomp_k is not None:
            #     nr comp dupa kaiser
            ax.axhline(1, c='g', label="Kaiser")
        if self.nrcomp_c is not None:
            ax.axhline(self.alpha[self.nrcomp_c - 1], c='m', label="Cattell")
        ax.axhline(self.alpha[self.nrcomp_p - 1], c='c', label="Ponderea minimala (>0.8)")
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
