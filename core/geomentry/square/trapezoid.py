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

    def draw(self):
        """Малює трикутник на осях та показує його за допомогою модуля matplotlib.pyplot."""
        self.ax[0].add_patch(self.trapezoid)  # додає полігон до осей
        self.ax[1].add_patch(self.trapezoid)  # додає полігон до осей
        # self.ax[1, 0].add_patch(self.triangle)  # додає полігон до осей
        super().draw()  # викликає метод draw з базового класу Shape