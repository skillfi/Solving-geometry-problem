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

    @property
    def vertices(self):
        """Повертає список вершин паралелограма на основі основи, висоти та кута."""
        # Знаходить координати першої вершини паралелограма
        x0 = 0  # початкова координата x
        y0 = 0  # початкова координата y
        # Створює порожній список для зберігання вершин
        vertices = []
        # Додає першу вершину до списку
        vertices.append([x0, y0])
        # Знаходить координати другої вершини за формулою
        # x = x0 + base
        # y = y0
        x = x0 + self.base
        y = y0
        # Додає другу вершину до списку
        vertices.append([x, y])
        # Знаходить координати третьої вершини за формулою
        # x = x0 + base + height * cos(angle)
        # y = y0 + height * sin(angle)
        x = x0 + self.base + self.height * math.cos(self.angle)
        y = y0 + self.height * math.sin(self.angle)
        # Додає третю вершину до списку
        vertices.append([x, y])
        # Знаходить координати четвертої вершини за формулою
        # x = x0 + height * cos(angle)
        # y = y0 + height * sin(angle)
        x = x0 + self.height * math.cos(self.angle)
        y = y0 + self.height * math.sin(self.angle)
        # Додає четверту вершину до списку
        vertices.append([x, y])
        # Повертає список вершин
        return vertices

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
