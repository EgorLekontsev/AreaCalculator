from math import pi, sqrt

"""
Библиотека для вычисления площади фигур.

- Circle: площадь по радиусу
- Triangle: площадь по трём сторонам (формула Герона)
- Square: площадь по стороне квадрата

"""

class Shape:
    # Базовый интерфейс
    def area(self) -> float:
        raise NotImplementedError("Подклассы должны реализовать метод area()")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = float(radius)
        if self.radius <= 0:
            raise ValueError("Радиус должен быть больше нуля")

    def area(self) -> float:
        return pi * self.radius * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        sides = sorted([float(a), float(b), float(c)])
        self.a, self.b, self.c = sides
        if self.a <= 0.0:
            raise ValueError("Стороны треугольника должны быть положительными")
        if self.a + self.b <= self.c:
            raise ValueError("Стороны не удовлетворяют неравенству треугольника")

    def area(self) -> float:
        # По формуле Герона
        s = (self.a + self.b + self.c) / 2.0
        area_sq = s * (s - self.a) * (s - self.b) * (s - self.c)
        return sqrt(area_sq)

    def is_right(self) -> bool:
        # Проверка, является ли треугольник прямоугольным.
        a, b, c = self.a, self.b, self.c
        return a * a + b * b == c * c


class Square(Shape):
    def __init__(self, side):
        self.side = float(side)
        if self.side <= 0:
            raise ValueError("Стороны квадрата должны быть положительными")

    def area(self) -> float:
        return self.side * self.side
