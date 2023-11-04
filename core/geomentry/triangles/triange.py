from core.geomentry.shape import Shape
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


class Triangle(Shape):
    """Підклас класу Shape для трикутників."""

    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length

    @property
    def vertices(self):
        """Повертає список вершин трикутника на основі довжин сторін."""
        return [
            [0, 0],  # ліва нижня вершина
            [self.side_length, 0],  # права нижня вершина
            [self.side_length / 2, self.side_length / 2],  # третя верхня
        ]
    @property
    def named_vertices(self):
        return {}

    @named_vertices.setter
    def named_vertices(self, point):
        self.named_vertices = point

    @property
    def triangle(self):
        """Повертає об'єкт Polygon з модуля matplotlib.patches, що відповідає трикутнику."""
        return Polygon(self.vertices, closed=True, fill=None)

    def draw(self):
        """Малює трикутник на осях та показує його за допомогою модуля matplotlib.pyplot."""
        self.ax.add_patch(self.triangle)  # додає полігон до осей
        super().draw()  # викликає метод draw з базового класу Shape

    def init_points(self, points: str, **kwargs):
        """Додає мітки до вершин трикутника за допомогою модуля matplotlib.pyplot."""
        for i, point in enumerate(points):
            self.ax.plot(*self.vertices[i], marker='o', label=point)  # додає точку та мітку до кожної вершини
            self.named_vertices = {point: self.vertices[i]}
            self.ax.annotate(point, (self.vertices[i]))  # додає точку та мітку до кожної вершини
        if kwargs.get('parallels'):
            for parallel in kwargs['parallels']:
                self.ax.plot()

