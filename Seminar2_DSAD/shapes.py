from math import dist


class shape():
    def __init__(self, x, y, eticheta=None):
        if len(x) != len(y):
            raise Exception("Dimensiuni incorecte!")
        if eticheta is None:
            self.eticheta = "A"
        else:
            self.eticheta = eticheta
        self.__x = x
        self.__y = y

    def __str__(self):
        sir = self.eticheta + ","
        for i in range(len(self.__x)):
            sir += ("(" + str(self.__x[i]) + "," + str(self.__y[i]) + ")")
        return sir

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x_):
        self.__x = x_

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, y_):
        self.__y = y_

    def perimetru(self):
        p = 0
        n = len(self.__x)
        for i in range(n):
            p += dist(
                (self.__x[i], self.__y[i]),
                (self.__x[(i + 1) % n], self.__y[(i + 1) % n])
            )
        return p

    def __eq__(self, other):
        assert isinstance(other, shape)
        return self.perimetru() == other.perimetru()


class rectangle(shape):
    def __init__(self, x0, y0, w, h, eticheta=None):
        self.x0 = x0
        self.y0 = y0
        self.w = w
        self.h = h
        x_ = [x0, x0 + w, x0 + w, x0]
        y_ = [y0, y0, y0 + h, y0 + h]
        super().__init__(x_, y_, eticheta)

    def __str__(self):
        sir = self.eticheta + ","
        sir += ("(" + str(self.x0) + "," + str(self.y0) + "," +
                str(self.w) + "," + str(self.h) + ")")
        return sir

    def perimetru(self):
        return 2 * (self.w + self.h)
