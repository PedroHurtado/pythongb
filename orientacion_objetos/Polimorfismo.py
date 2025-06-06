from abc import ABC, abstractmethod
from math import pi


class Figura(ABC):
    @abstractmethod
    def area(self):
        pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangulo(Figura):
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        ancho = abs(self.p2.x - self.p1.x)
        alto = abs(self.p2.y - self.p1.y)
        return ancho * alto


class Circulo(Figura):
    def __init__(self, radio: float):
        self.radio = radio

    def area(self):
        return pi * self.radio ** 2


if __name__ == "__main__":
    r = Rectangulo(Point(1, 2), Point(4, 6))
    c = Circulo(3)

    print(f"Área del rectángulo: {r.area()}")
    print(f"Área del círculo: {c.area()}")
