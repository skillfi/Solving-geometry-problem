from core.geomentry.shape import Shape


class Square(Shape):
    """Підклас класу Shape для квадратів."""

    @property
    def vertices(self):
        """Повертає список вершин квадрата на основі довжини сторони."""
        return [
            (0, 0), # ліва нижня вершина
            (self.side_length, 0), # права нижня вершина
            (self.side_length, self.side_length), # права верхня вершина
            (0, self.side_length) # ліва верхня вершина
        ]