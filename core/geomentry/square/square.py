from core.geomentry.shape import Shape
import matplotlib.pyplot as plt

class Square(Shape):
    """Підклас класу Shape для квадратів."""

    def __init__(self, side_length):
        """Ініціалізує квадрат з довжиною сторони."""
        super().__init__()  # викликає конструктор базового класу
        self.side_length = side_length  # зберігає довжину сторони як атрибут об'єкта
        self.vertices = self.calculate_vertices()# обчислює та зберігає вершини квадрата
        self.named_vertices = dict(Point=[], X=[], Y=[])
        self.points = {}

    def calculate_vertices(self):
        """Обчислює координати вершин квадрата."""
        # Визначає початкову вершину квадрата
        x0 = 0  # координата x початкової вершини
        y0 = 0  # координата y початкової вершини
        # Обчислює координати інших вершин квадрата
        x1 = x0 + self.side_length  # координата x другої вершини
        y1 = y0  # координата y другої вершини
        x2 = x1  # координата x третьої вершини
        y2 = y1 + self.side_length  # координата y третьої вершини
        x3 = x0  # координата x четвертої вершини
        y3 = y2  # координата y четвертої вершини
        # Повертає список вершин квадрата
        return [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]

    def area(self):
        """Повертає площу квадрата."""
        return self.side_length ** 2  # площа квадрата дорівнює квадрату довжини сторони

    def perimeter(self):
        """Повертає периметр квадрата."""
        return 4 * self.side_length  # периметр квадрата дорівнює сумі довжин чотирьох сторін

    def __repr__(self):
        """Повертає рядкове представлення квадрата."""
        return f"Квадрат зі стороною {self.side_length} та вершинами {self.vertices}"

    def draw(self):
        self.ax.add_patch(self.polygon)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.legend()
        plt.show()  # показує фігуру
