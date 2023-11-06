from core.geomentry.shape import Shape


class Circle(Shape):
    """Підклас для представлення круга."""

    def __init__(self, center, radius):
        """Ініціалізує круг за допомогою координат центра та радіуса."""
        super().__init__()  # Викликає конструктор базового класу
        self.center = center
        self.radius = radius

    @property
    def circle(self):
        """Повертає об'єкт Circle з модуля matplotlib.patches, що відповідає кругу."""
        return Circle(self.center, self.radius, fill=None)  # Створює та повертає об'єкт Circle

    def draw(self):
        """Малює круг на осях та показує його за допомогою модуля matplotlib.pyplot."""
        self.ax.add_patch(self.circle)  # Додає об'єкт круга до графіку
        super().draw()  # Викликає метод базового класу для відображення