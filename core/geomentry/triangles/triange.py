from matplotlib.patches import Polygon

from core.geomentry.shape import Shape


class Triangle(Shape):
    """Підклас класу Shape для трикутників."""

    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length
        self.named_vertices = dict(Point=[], X=[], Y=[])
        self.points = dict()
        self.axes = 0

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
        self.ax[0].add_patch(self.triangle)  # додає полігон до осей
        self.ax[1].add_patch(self.triangle)  # додає полігон до осей
        # self.ax[1, 0].add_patch(self.triangle)  # додає полігон до осей
        super().draw()  # викликає метод draw з базового класу Shape



