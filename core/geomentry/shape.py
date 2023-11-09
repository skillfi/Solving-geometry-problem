import re
from typing import List

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Polygon


class Shape:
    DataFrame: pd.DataFrame
    """Базовий клас для різних геометричних фігур."""

    def __init__(self):
        """Ініціалізує фігуру та осі за допомогою модуля matplotlib.pyplot."""
        self.fig, self.ax = plt.subplots(1, 2)
        self.df: pd.DataFrame = pd.DataFrame()
        self.points = {}
        self.base_points = None

    def diagonals(self, name: List[str], df: pd.DataFrame, mark: str='g-'):
        for line in name:
            xy = []
            new_df = df
            self.ax[1].plot([new_df.loc[0, line[0]], new_df.loc[0, line[1]]],
                            [new_df.loc[1, line[0]], new_df.loc[1, line[1]]], mark, label=line)


    @classmethod
    def from_vertices(cls, vertices):
        """Створює екземпляр класу Shape зі списку вершин."""
        obj = cls()  # створює новий об'єкт класу Shape
        obj.vertices = vertices  # зберігає список вершин як атрибут об'єкта

    @classmethod
    def parallels(cls, lines, df: pd.DataFrame):
        for parallel in lines:
            to_parallel = lines[parallel]
            for point in to_parallel:
                points_t = cls.list_to_tuple(cls.named_vertices['Point'])
                if point not in points_t:
                    cls.named_vertices['Point'].append(point)
                    x = cls.points[parallel[0]][0]
                    y = cls.points[to_parallel[0]][1]
                    cls.named_vertices['X'].append(x)
                    cls.named_vertices['Y'].append(y)
                    cls.points[point] = [x, y]
                    x, y = df[point]  # розпаковує координати точки
                    cls.ax[1].plot(x, y, marker='o', label=point)  # додає точку та мітку до осі
                    cls.ax[1].plot([df.loc[0, point], df.loc[0, to_parallel[0]]],
                                   [df.loc[1, point], df.loc[1, to_parallel[0]]], 'g-', label=to_parallel)
                    cls.ax[1].annotate(point, (x, y))  # додає анотацію до точки

    def task(self, need, df: pd.DataFrame, diagonals: List[str], **kwargs):
        if diagonals:
            self.diagonals(diagonals, df, 'g--')
        if need:
            points = need
            point = kwargs.get('points')
            if point:
                for p in point:
                    if 'is on segment' in p:
                        point, segment = re.compile(r'([A-Z]{1})\sis\son\ssegment\s([A-Z]{2})').search(p).groups()
                        if df.loc[0, segment[0]] == 0:
                            df[point.strip()] = [0, df.loc[1, segment[0]] / 2]
                        if df.loc[1, segment[0]] == 0:
                            df[point.strip()] = [df.loc[0, segment[0]] / 2, 0]
                        if df.loc[0, segment[0]] == 0 and df.loc[1, segment[0]] == 0:
                            df[point.strip()] = [df.loc[0, segment[1]] / 2,
                                                             df.loc[1, segment[1]]]
                        # Використовуємо локальні змінні для зберігання значень x і y
                        x, y = df[point.strip()]
                        # Використовуємо генератор списків для створення списку осей
                        axes = [self.ax[0], self.ax[1]]
                        # Використовуємо функцію map() для застосування функції plot до кожної осі
                        list(map(lambda ax: ax.plot(x, y, marker='o', label=point), axes))
                        # Використовуємо функцію map() для застосування функції annotate до кожної осі
                        list(map(lambda ax: ax.annotate(point, (x, y)), axes))
            groups = re.compile(r'([A-Z]{1})').search(need).groups()
            for group in groups:
                if self.points.get(group):
                    # Використовуємо генератор списків для створення списку осей
                    axes = [self.ax[0], self.ax[1]]
                    # Використовуємо функцію map() для застосування функції plot до кожної осі
                    list(map(lambda ax: ax.plot([df.loc[0, points[0]], df.loc[0, points[1]]],
                                                [df.loc[1, points[0]], df.loc[1, points[1]]],
                                                'r-.',
                                                label=points + '?'), axes))


    def ploting(self, x, y, point):
        # Використовуємо генератор списків для створення списку осей
        axes = [self.ax[0], self.ax[1]]
        # Використовуємо функцію map() для застосування функції plot до кожної осі
        list(map(lambda ax: ax.plot(x, y, marker='o', label=point), axes))
        # Використовуємо функцію map() для застосування функції annotate до кожної осі
        list(map(lambda ax: ax.annotate(point, (x, y)), axes))

    def init_points(self, points: str):
        """Додає мітки до вершин трикутника за допомогою модуля matplotlib.pyplot."""
        # Додає точки та мітки до вершин трикутника
        self.base_points = points
        for i, point in enumerate(points):
            x, y = self.vertices[i]  # розпаковує координати вершини
            self.ploting(x, y, point)
            # Оновлює словник та датафрейм з іменами вершин та їх координатами
            self.named_vertices['Point'].append(point)
            self.named_vertices['X'].append(x)
            self.named_vertices['Y'].append(y)
            self.points[point] = [x, y]
        return self.convert_to_df()

    def convert_to_df(self):
        df = pd.DataFrame(self.points)
        return df

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
        self.ax[0].set_xlabel('X')
        self.ax[0].set_ylabel('Y')
        self.ax[0].legend()
        plt.show()  # показує фігуру
