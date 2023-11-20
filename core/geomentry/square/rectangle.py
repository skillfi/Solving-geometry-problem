from matplotlib.patches import Polygon

from core.geomentry.shape import Shape


class Rectangle(Shape):
    """Підклас класу Shape для прямокутників."""

    def __init__(self, length, width):
        """Ініціалізує прямокутник з довжиною та шириною."""
        super().__init__()  # викликає конструктор батьківського класу
        self.length = length  # зберігає довжину як атрибут
        self.width = width  # зберігає ширину як атрибут
        self.named_vertices = dict(Point=[], X=[], Y=[])
        self.points = {}

    @property
    def rectangle(self):
        """Повертає об'єкт Polygon з модуля matplotlib.patches, що відповідає трикутнику."""
        return Polygon(self.vertices, closed=True, fill=None)

    @property
    def area(self):
        """Повертає площу прямокутника."""
        return self.length * self.width  # обчислює площу за допомогою довжини та ширини

    @property
    def perimeter(self):
        """Повертає периметр прямокутника."""
        return 2 * (self.length + self.width)  # обчислює периметр за допомогою довжини та ширини

    def draw(self):
        """Малює трикутник на осях та показує його за допомогою модуля matplotlib.pyplot."""
        self.ax[0].add_patch(self.rectangle)  # додає полігон до осей
        self.ax[1].add_patch(self.rectangle)  # додає полігон до осей
        super().draw()  # викликає метод draw з базового класу Shape