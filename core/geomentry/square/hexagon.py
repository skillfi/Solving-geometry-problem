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
        self.ax.add_patch(self.hexagon)  # додає полігон до осей
        super().draw()  # викликає метод draw з базового класу Shape

    @property
    def vertices(self):
        """Повертає список вершин шестикутника на основі довжини сторони."""
        # Знаходить кут між сусідніми вершинами шестикутника
        angle = math.pi / 3  # 60 градусів у радіанах
        # Знаходить координати першої вершини шестикутника
        x0 = 0  # початкова координата x
        y0 = 0  # початкова координата y
        # Створює порожній список для зберігання вершин
        vertices = []
        # Додає першу вершину до списку
        vertices.append([x0, y0])
        # Ітерує по індексах від 1 до 5
        for i in range(1, 6):
            # Знаходить координати наступної вершини за формулою
            # x = x0 + side_length * cos(i * angle)
            # y = y0 + side_length * sin(i * angle)
            x = x0 + self.side_length * math.cos(i * angle)
            y = y0 + self.side_length * math.sin(i * angle)
            # Додає наступну вершину до списку
            vertices.append([x, y])
        # Повертає список вершин
        return vertices

    def area(self):
        """Повертає площу шестикутника за формулою S = (3 * sqrt(3) / 2) * side_length ** 2."""
        return (3 * math.sqrt(3) / 2) * self.side_length ** 2  # обчислює та повертає площу

    def perimeter(self):
        """Повертає периметр шестикутника за формулою P = 6 * side_length."""
        return 6 * self.side_length  # обчислює та повертає периметр

