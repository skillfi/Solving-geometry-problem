import numpy as np

from core.geomentry.shape import Shape


class Parallelogram(Shape):
    """Підклас класу Shape для паралелограмів."""

    def __init__(self, base, height, angle):
        """Ініціалізує паралелограм з заданими розмірами.

        Параметри:
            base (float): довжина основи паралелограма.
            height (float): висота паралелограма.
            angle (float): кут між основою та бічною стороною паралелограма в радіанах.
        """
        self.base = base
        self.height = height
        self.angle = angle
        self.validate_dimensions()

    def validate_dimensions(self):
        """Перевіряє, чи є розміри паралелограма додатними, інакше піднімає ValueError."""
        if self.base <= 0 or self.height <= 0 or self.angle <= 0 or self.angle >= np.pi:
            raise ValueError(
                "Invalid parallelogram dimensions. Base, height and angle must be positive and angle must be less than pi.")

    def calculate_vertices(self):
        """Обчислює координати вершин паралелограма на основі розмірів."""
        # Визначення довжини бічної сторони за теоремою Піфагора
        side = np.sqrt(self.height ** 2 + self.base ** 2 - 2 * self.height * self.base * np.cos(self.angle))
        # Визначення кута між бічною стороною та висотою за теоремою косинусів
        beta = np.arccos((self.height ** 2 + side ** 2 - self.base ** 2) / (2 * self.height * side))
        # Визначення координат вершин паралелограма
        return np.array([
            [0, 0],  # ліва нижня вершина
            [self.base, 0],  # права нижня вершина
            [self.base - side * np.cos(beta), side * np.sin(beta)],  # права верхня вершина
            [-side * np.cos(beta), side * np.sin(beta)]  # ліва верхня вершина
        ])
