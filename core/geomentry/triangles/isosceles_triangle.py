import matplotlib.pyplot as plt
import numpy as np

from core.geomentry.shape import Shape


class IsoscelesTriangle(Shape):
    """Клас для представлення та малювання рівнобедреного трикутника.

    Атрибути:
        base (float): довжина основи трикутника.
        legs (float): довжина бічних сторін трикутника.

    Методи:
        __init__(self, base, legs): ініціалізує об'єкт класу з заданими розмірами.
        validate_dimensions(self): перевіряє, чи є розміри трикутника додатними, інакше піднімає ValueError.
        calculate_vertices(self): обчислює координати вершин трикутника на основі розмірів.
        draw(self): малює трикутник на графіку за допомогою модуля matplotlib.pyplot.
    """

    def __init__(self, base, legs):
        super().__init__()
        self.base = base
        self.legs = legs
        self.validate_dimensions()

    def validate_dimensions(self):
        if self.base <= 0 or self.legs <= 0:
            raise ValueError("Invalid triangle dimensions. Both base and legs must be greater than 0.")

    def calculate_vertices(self):
        # Визначення координат вершин трикутника
        return np.array([[0, 0], [self.base / 2, self.legs], [self.base, 0]])

    def draw(self):
        vertices = self.calculate_vertices()
        x, y = vertices[:, 0], vertices[:, 1]

        # Створення графіка трикутника
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, 'bo-')  # 'bo-' означає синій колір, круглі маркери та суцільна лінія
        plt.fill(x, y, 'b', alpha=0.2)  # Заповнення трикутника синім кольором з прозорістю 0.2
        plt.xlim(-1, self.base + 1)
        plt.ylim(-1, self.legs + 1)
        plt.xlabel('X-Axis')
        plt.ylabel('Y-Axis')
        plt.title('Isosceles Triangle')
        plt.grid(True)
        plt.show()