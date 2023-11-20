import math

import pandas as pd

from core.geomentry.shape import Shape


class Parallelogram(Shape):
    """Підклас класу Shape для паралелограмів."""

    def __init__(self, base, height, angle):
        super().__init__()  # викликає конструктор базового класу
        self.base = base  # зберігає довжину основи паралелограма
        self.height = height  # зберігає висоту паралелограма
        self.angle = angle  # зберігає кут між основою та бічною стороною паралелограма
        self.named_vertices = dict(Point=[], X=[], Y=[])
        self.points = dict()

    def __init_points__(self, points):
        return super().init_points(points)  # викликаємо метод батьківського класу

    def draw(self):
        """Малює трикутник на осях та показує його за допомогою модуля matplotlib.pyplot."""
        self.ax[0].add_patch(self.polygon)  # додає полігон до осей
        self.ax[1].add_patch(self.polygon)  # додає полігон до осей
        super().draw()  # викликає метод draw з базового класу Shape

    def area(self):
        """Повертає площу паралелограма за формулою S = base * height."""
        return self.base * self.height  # обчислює та повертає площу

    def perimeter(self):
        """Повертає периметр паралелограма за формулою P = 2 * (base + side), де side = height / sin(angle)."""
        side = self.height / math.sin(self.angle)  # знаходить довжину бічної сторони
        return 2 * (self.base + side)  # обчислює та повертає периметр
