from matplotlib.patches import Polygon

from core.geomentry.shape import Shape


class Rhombus(Shape):
    """Підклас Rhombus, який наслідує клас Shape."""

    def __init__(self, side_length, angle):
        """Ініціалізує ромб з довжиною сторони та кутом повороту."""
        super().__init__()  # викликаємо конструктор батьківського класу
        self.side_length = side_length
        self.angle = angle
        self.named_vertices = dict(Point=[], X=[], Y=[])
        self.points = {}

    @property
    def rhombus(self):
        """Повертає об'єкт Polygon з модуля matplotlib.patches, що відповідає трикутнику."""
        return Polygon(self.vertices, closed=True, fill=None)

    @property
    def vertices(self):
        """Обчислює вершини ромба на основі довжини сторони та кута повороту."""
        x = [0, self.side_length, 0, -self.side_length]
        y = [self.side_length, 0, -self.side_length, 0]
        return [(xi, yi) for xi, yi in zip(x, y)]

    def draw(self):
        """Малює трикутник на осях та показує його за допомогою модуля matplotlib.pyplot."""
        self.ax[0].add_patch(self.rhombus)  # додає полігон до осей
        self.ax[1].add_patch(self.rhombus)  # додає полігон до осей
        super().draw()  # викликає метод draw з базового класу Shape