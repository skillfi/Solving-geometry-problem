import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


class Shape:
    """Базовий клас для різних геометричних фігур."""

    def __init__(self):
        """Ініціалізує фігуру та осі за допомогою модуля matplotlib.pyplot."""
        self.fig, self.ax = plt.subplots()

    @classmethod
    def from_vertices(cls, vertices):
        """Створює екземпляр класу Shape зі списку вершин."""
        obj = cls()  # створює новий об'єкт класу Shape
        obj.vertices = vertices  # зберігає список вершин як атрибут об'єкта
        return obj  # повертає об'єкт

    @classmethod
    def from_side_length(cls, side_length):
        """Створює екземпляр класу Shape з довжиною сторони."""
        obj = cls()  # створює новий об'єкт класу Shape
        obj.side_length = side_length  # зберігає довжину сторони як атрибут об'єкта
        return obj  # повертає об'єкт

    @classmethod
    def from_triangle_segments(cls, side_length):
        """Створює екземпляр класу Shape з довжиною сторони."""
        obj = cls()  # створює новий об'єкт класу Shape
        obj.side_length = side_length  # зберігає довжину сторони як атрибут об'єкта
        return obj  # повертає об'єкт

    @property
    def polygon(self):
        """Повертає об'єкт Polygon з модуля matplotlib.patches, що відповідає фігурі."""
        return Polygon(self.vertices, closed=True, fill=None)  # створює та повертає об'єкт Polygon зі списку вершин

    def draw(self):
        """Малює фігуру на осях та показує її за допомогою модуля matplotlib.pyplot."""
        # Set the x and y axis labels
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.legend()
        plt.show()  # показує фігуру
