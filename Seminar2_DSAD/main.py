from shapes import shape
from shapes import rectangle

try:
    a = shape([2, 4, 3], [1, 1, 3], "Figura A")
    print(a)
    print("Coordonate x pentru", a.eticheta, ":")
    print(a.x)
    print("Perimetru pentru", a.eticheta, ":")
    print(a.perimetru())
    b = shape([3, 5, 4], [3, 3, 5], "Figura B")
    print("Test egalitate intre", a.eticheta, "si", b.eticheta, ":", a == b)
    c = rectangle(2, 2, 4, 3, "Dreptunghi 1")
    print(c)
    print("Perimetrul pentru", c.eticheta, ":", c.perimetru())
except Exception as ex:
    print(ex)
