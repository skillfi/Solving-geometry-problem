from matplotlib.patches import Polygon

from core.geomentry.shape import Shape


class Trapezoid(Shape):
    """Підклас, який представляє трапецію."""

    def __init__(self, top_length, bottom_length, height):
        super().__init__() # Викликаємо конструктор батьківського класу
        self.top_length = top_length  # Довжина верхньої сторони трапеції
        self.bottom_length = bottom_length  # Довжина нижньої сторони трапеції
        self.height = height  # Висота трапеції
        self.named_vertices = dict(Point=[], X=[], Y=[])
        self.points = {}

    @property
    def trapezoid(self):
        """Повертає об'єкт Polygon з модуля matplotlib.patches, що відповідає трикутнику."""
        return Polygon(self.vertices, closed=True, fill=None)

    @property
    def vertices(self):
        """Повертає вершини трапеції."""
        x0 = 0
        x1 = self.top_length
        x2 = x1 + (self.bottom_length - self.top_length) / 2
        x3 = x2 - (self.bottom_length - self.top_length)
        y0 = 0
        y1 = 0
        y2 = self.height
        y3 = self.height
        return [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]

    def draw(self):
        """Малює трикутник на осях та показує його за допомогою модуля matplotlib.pyplot."""
        self.ax[0].add_patch(self.trapezoid)  # додає полігон до осей
        self.ax[1].add_patch(self.trapezoid)  # додає полігон до осей
        # self.ax[1, 0].add_patch(self.triangle)  # додає полігон до осей
        super().draw()  # викликає метод draw з базового класу Shape