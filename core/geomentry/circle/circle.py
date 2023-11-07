from typing import Tuple

from core.geomentry.shape import Shape
from matplotlib.patches import Circle


class CircleCustom(Shape):
    """Підклас для представлення круга."""

    def __init__(self, center: Tuple[float, float], radius: int = 5):
        """Ініціалізує круг за допомогою координат центра та радіуса."""
        super().__init__()  # Викликає конструктор базового класу
        self.center = center
        self.radius = radius

    @property
    def circle(self):
        """Повертає об'єкт Circle з модуля matplotlib.patches, що відповідає кругу."""
        return Circle(self.center, self.radius)  # Створює та повертає об'єкт Circle

    def draw(self):
        """Малює круг на осях та показує його за допомогою модуля matplotlib.pyplot."""
        self.ax.add_patch(self.circle)  # Додає об'єкт круга до графіку
        super().draw()  # Викликає метод базового класу для відображення

    def init_points(self, point: str):
        x, y = self.center  # розпаковує координати вершини
        self.ax.plot(x, y, marker='o', label=point)  # додає точку та мітку до осі
        self.ax.annotate(point, (x, y))  # додає анотацію до точки

