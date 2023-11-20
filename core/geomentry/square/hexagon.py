import math

import pandas as pd
from matplotlib.patches import Polygon

from core.geomentry.shape import Shape


class Hexagon(Shape):
    """Підклас класу Shape для шестикутників."""

    def __init__(self, side_length):
        super().__init__()  # викликає конструктор базового класу
        self.side_length = side_length  # зберігає довжину сторони шестикутника
        self.named_vertices = dict(Point=[], X=[], Y=[])
        self.points = {}

    @property
    def hexagon(self):
        """Повертає об'єкт Polygon з модуля matplotlib.patches, що відповідає трикутнику."""
        return Polygon(self.vertices, closed=True, fill=None)

    def draw(self):
        """Малює трикутник на осях та показує його за допомогою модуля matplotlib.pyplot."""
        self.ax[0].add_patch(self.hexagon)  # додає полігон до осей
        self.ax[1].add_patch(self.hexagon)  # додає полігон до осей
        super().draw()  # викликає метод draw з базового класу Shape

    def area(self):
        """Повертає площу шестикутника за формулою S = (3 * sqrt(3) / 2) * side_length ** 2."""
        return (3 * math.sqrt(3) / 2) * self.side_length ** 2  # обчислює та повертає площу

    def perimeter(self):
        """Повертає периметр шестикутника за формулою P = 6 * side_length."""
        return 6 * self.side_length  # обчислює та повертає периметр

