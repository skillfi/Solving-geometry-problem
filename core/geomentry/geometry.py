import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle


class Shape:
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def draw(self):
        plt.show()


class Triangle(Shape):
    def __init__(self, vertices):
        super().__init__()
        self.vertices = vertices
        self.triangle = Polygon(self.vertices, closed=True, fill=None)
        self.ax.add_patch(self.triangle)


class Square(Shape):
    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length
        self.vertices = [
            (0, 0),
            (self.side_length, 0),
            (self.side_length, self.side_length),
            (0, self.side_length)
        ]
        self.square = Polygon(self.vertices, closed=True, fill=None)
        self.ax.add_patch(self.square)
