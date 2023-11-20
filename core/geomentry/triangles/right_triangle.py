import math

from core.geomentry.triangles.triange import Triangle


class RightTriangle(Triangle):
    """Підклас класу Triangle для прямокутних трикутників."""

    def __init__(self, base, height, angle):
        super().__init__(base)  # викликає конструктор базового класу з довжиною основи
        self.height = height  # зберігає висоту трикутника
        self.angle = angle

    @property
    def hypotenuse(self):
        """Повертає довжину гіпотенузи прямокутного трикутника за теоремою Піфагора."""
        return math.sqrt(self.side_length ** 2 + self.height ** 2)  # корінь квадратний з суми квадратів катетів

    def area(self):
        """Повертає площу прямокутного трикутника за формулою S = (a * h) / 2."""
        return (self.side_length * self.height) / 2  # добуток основи та висоти, поділений на два

    def perimeter(self):
        """Повертає периметр прямокутного трикутника за формулою P = a + b + c."""
        return self.side_length + self.height + self.hypotenuse  # сума всіх сторін трикутника
