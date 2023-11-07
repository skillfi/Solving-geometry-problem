import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Polygon


class Shape:
    """Базовий клас для різних геометричних фігур."""

    def __init__(self):
        """Ініціалізує фігуру та осі за допомогою модуля matplotlib.pyplot."""
        self.fig, self.ax = plt.subplots()
        self.df: pd.DataFrame = None
        self.points = {}

    @classmethod
    def from_vertices(cls, vertices):
        """Створює екземпляр класу Shape зі списку вершин."""
        obj = cls()  # створює новий об'єкт класу Shape
        obj.vertices = vertices  # зберігає список вершин як атрибут об'єкта
        return obj  # повертає об'єкт

    def init_points(self, points: str):
        """Додає мітки до вершин трикутника за допомогою модуля matplotlib.pyplot."""
        # Додає точки та мітки до вершин трикутника
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

    def convert_to_df(self):
        df = pd.DataFrame(self.points)
        self.df = df

    @classmethod
    def from_side_length(cls, side_length):
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
