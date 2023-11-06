from core.geomentry.shape import Shape
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import pandas as pd


class Triangle(Shape):
    """Підклас класу Shape для трикутників."""

    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length
        self.named_vertices = dict(Point=[], X=[], Y=[])
        self.points = dict()


    @property
    def vertices(self):
        """Повертає список вершин трикутника на основі довжин сторін."""
        return [
            [0, 0],  # ліва нижня вершина
            [self.side_length, 0],  # права нижня вершина
            [self.side_length / 2, self.side_length / 2],  # третя верхня
        ]

    @property
    def triangle(self):
        """Повертає об'єкт Polygon з модуля matplotlib.patches, що відповідає трикутнику."""
        return Polygon(self.vertices, closed=True, fill=None)

    @classmethod
    def list_to_tuple(cls, input_list):
        if isinstance(input_list, list):
            return tuple(input_list)
        else:
            raise ValueError("Input is not a list")

    def draw(self):
        """Малює трикутник на осях та показує його за допомогою модуля matplotlib.pyplot."""
        self.ax.add_patch(self.triangle)  # додає полігон до осей
        super().draw()  # викликає метод draw з базового класу Shape

    def init_points(self, points: str, **kwargs):
        """Додає мітки до вершин трикутника за допомогою модуля matplotlib.pyplot."""
        for i, point in enumerate(points):
            x, y = self.vertices[i]  # розпаковує координати вершини
            self.ax.plot(x, y, marker='o', label=point)  # додає точку та мітку до осі
            self.ax.annotate(point, (x, y))  # додає анотацію до точки
            # Оновлює словник та датафрейм з іменами вершин та їх координатами
            self.named_vertices['Point'].append(point)
            self.named_vertices['X'].append(x)
            self.named_vertices['Y'].append(y)
            self.points[point] = [x, y]
            self.convert_to_df()
        # Якщо є параметр parallels, то додає точки та мітки до паралельної лінії
        if kwargs.get('parallels'):
            for parallel in kwargs['parallels']:
                to_parallel = kwargs['parallels'][parallel]
                for point in to_parallel:
                    points_t = Triangle.list_to_tuple(self.named_vertices['Point'])
                    if point not in points_t:
                        self.named_vertices['Point'].append(point)
                        x = self.points[parallel[0]][0]
                        y = self.points[to_parallel[0]][1]
                        self.named_vertices['X'].append(x)
                        self.named_vertices['Y'].append(y)
                        self.points[point] = [x, y]
                        self.convert_to_df()
                        x, y = self.df[point]  # розпаковує координати точки
                        self.ax.plot(x, y, marker='o', label=point)  # додає точку та мітку до осі
                        self.ax.plot([self.df.loc[0, point], self.df.loc[0, to_parallel[0]]],
                                     [self.df.loc[1, point], self.df.loc[1, to_parallel[0]]], 'g-', label=to_parallel)
                        self.ax.annotate(point, (x, y))  # додає анотацію до точки
        if kwargs.get('need'):
            points = kwargs['need']
            self.ax.plot([self.df.loc[0, points[0]], self.df.loc[0, points[1]]],
                         [self.df.loc[1, points[0]], self.df.loc[1, points[1]]], '--', label=points)
