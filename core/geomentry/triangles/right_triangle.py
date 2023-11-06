import math

from core.geomentry.triangles.triange import Triangle


class RightTriangle(Triangle):
    """Підклас класу Triangle для прямокутних трикутників."""

    def __init__(self, base, height, angle):
        super().__init__(base)  # викликає конструктор базового класу з довжиною основи
        self.height = height  # зберігає висоту трикутника
        self.angle = angle

    @property
    def vertices(self):
        """Повертає список вершин прямокутного трикутника на основі основи та висоти."""
        return [
            [0, 0],  # ліва нижня вершина
            [self.side_length, 0],  # права нижня вершина
            [0, self.height],  # ліва верхня вершина
        ]

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

    def init_points(self, points: str, **kwargs):
        for i, point in enumerate(points):
            x, y = self.vertices[i]  # розпаковує координати вершини
            # Оновлює словник та датафрейм з іменами вершин та їх координатами
            self.named_vertices['Point'].append(point)
            self.named_vertices['X'].append(x)
            self.named_vertices['Y'].append(y)
            self.points[point] = [x, y]
            self.convert_to_df()
            # Якщо кут дорівнює 90 градусам, то змінює координати точки на протилежну вершину
            if self.angle.get(point) == 90:
                opposite_index = (i + 2) % 3  # знаходить індекс протилежної вершини
                opposite_point = points[opposite_index+1]  # знаходить ім'я протилежної вершини
                self.points[point], self.points[opposite_point] = self.points[opposite_point], self.points[
                    point]  # обмінює координати точок
                self.convert_to_df()  # оновлює датафрейм з новими координатами
                x, y = self.vertices[i]
            self.ax.plot(x, y, marker='o', label=point)  # додає точку та мітку до осі
            self.ax.annotate(point, (x, y))  # додає анотацію до точки
