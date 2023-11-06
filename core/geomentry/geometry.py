import re
from typing import List, Tuple

from core.geomentry.square.hexagon import Hexagon
from core.geomentry.triangles.right_triangle import RightTriangle
from core.geomentry.triangles.triange import Triangle
from core.geomentry.square.paralelogram import Parallelogram


class Geometry:
    """A class to find shapes and points in a given text using regular expressions."""

    def __init__(self):
        # Define a dictionary of shapes and their regex patterns
        self.shapes = {
            'triangle': re.compile(r'\sTriangle\s([A-Z]{3})\S', re.IGNORECASE),
            'right_triangle': self.triangle_types(),
            'circle': re.compile(r'Circle\s([A-Z]{1})\S', re.IGNORECASE),
            'square': re.compile(r'Square\s([A-Z]{4})\S', re.IGNORECASE),
            'parallelogram': re.compile(r'parallelogram\s([A-Z]{4})\S', re.IGNORECASE),
            'rectangle': re.compile(r'Rectangle\s([A-Z]{4})\S', re.IGNORECASE),
            'hexagon': re.compile(r'\sHexagon\s([A-Z]{6})\S', re.IGNORECASE),
            # Add more shapes and their regex patterns here
        }
        # Define a regex pattern for points
        self.points = re.compile(r'Point\s([A-Z]{1})\sis\son', re.IGNORECASE)
        self.line_segment = re.compile(r'\s([A-Z]\d+)\s')
        self.other_segments = re.compile(r'\s([A-Z]{2})\s=')
        self.height_segment = re.compile(r'\s(\d{2})\scm')
        self.parallels = re.compile(r'\s([A-Z]{2})\sis\s(parallel)\sto\sline\ssegment\s([A-Z]{2})')
        self.need_to_found = re.compile(r'\sdetermine\sthe\slength\sof\s([A-Z]{2})')
        self.angle = re.compile(r'\s(angle)\s([A-Z]{1})\smeasuring\s(\d+)\s(degrees)')

    def triangle_types(self):
        first_regular = re.compile(r'\s(right)\sTriangle\s([A-Z]{3})\S', re.IGNORECASE)
        second_regular = re.compile(r'Triangle\s([A-Z]{3})\sis\sa\s(right)', re.IGNORECASE)
        return {1: first_regular, 2: second_regular}

    def lenght_segments(self, segment):
        return re.compile(segment + r'\shas\sa\slength\sof\s(\d+)\s')

    def set_height_to_segments(self, text):
        # Find all the line segments and other segments in the text
        line_segments = self.line_segment.findall(text)
        other_segments = self.other_segments.findall(text)
        # Create an empty dictionary for segment heights
        segment_height = {}
        # Loop through all the segments
        for segment in line_segments + other_segments:
            # Compile a regex pattern to find the segment height in the text
            length = self.lenght_segments(segment).search(text)
            if length:
                for s in length.groups():
                    segment_height[segment] = int(s)
            compile_text = f'{segment}'
            pattern = re.compile(compile_text + r'\s=\s([1-9]{2})\scm\S')
            # Search for the pattern in the text
            match = pattern.search(text)
            # If a match is found, add the segment and its height to the dictionary
            if match:
                segment_height[segment] = int(match.group(1))
        # Return the segment height dictionary
        return segment_height

    def find_shapes_and_points(self, text):
        """A function to find shapes and points in a given text and return them as a dictionary and a list.

        Args:
            text (str): The text to search for shapes and points.

        Returns:
            found_shapes (dict): A dictionary of found shapes and their corresponding names or types.
            found_points (list): A list of found points.
        """
        # Створення порожнього словника для зберігання знайдених фігур
        found_shapes = {}
        # Цикл по словнику фігур та пошук співпадінь у тексті
        for shape, pattern in self.shapes.items():
            # Пошук ігноруючи регістр
            if not isinstance(pattern, dict):
                matches = pattern.search(text)
                # Якщо знайдено співпадіння, додаємо фігуру та її назву або тип до словника знайдених фігур
                if matches:
                    # Беремо перше співпадіння з групи
                    match = matches.group(1)
                    # Додаємо фігуру та співпадіння до словника
                    found_shapes[shape] = match

        # Find all the points in the text and store them in a list
        found_points = self.points.findall(text)
        # Створення словника для зберігання паралельних рядків
        parallel = {}
        # Знаходження усіх паралельних рядків у тексті
        parallels = self.parallels.findall(text)
        # Додавання кожного паралельного рядка до словника
        for p in parallels:
            # Видалення слова 'parallel' з кортежу
            p = tuple(filter(lambda x: x != 'parallel', p))
            # Якщо кортеж містить два різних елементи, додаємо їх до словника
            if len(p) == 2 and p[0] != p[1]:
                parallel[p[0]] = p[1]
        # Якщо кортеж містить однакові елементи, ігноруємо їх
        # Знаходження потрібної інформації у тексті
        need = self.need_to_found.search(text)
        found_segments = self.line_segment.findall(text)
        height_segments = self.set_height_to_segments(text)
        angles = self.angle.search(text)

        # Повертає знайдені фігури, точки, сегменти, висоти, паралелi, потрібну інформацію та кути
        return (
            found_shapes,  # словник знайдених фігур
            found_points,  # список знайдених точок
            found_segments,  # список знайдених сегментів
            height_segments,  # словник знайдених висот
            parallel,  # словник знайдених паралельних рядків
            need.group(1) if need else None,  # потрібна інформація або None, якщо не знайдена
            {angles.group(2): int(angles.group(3))} if angles else None # словник знайденого кута або None, якщо не знайдений
        )

    def draw_shape(self, text):
        shape, points, segments, height_segments, parallels, need, angle = self.find_shapes_and_points(text)
        # Створює словник, що відображає назви фігур на їх класи
        shape_classes = {
            'triangle': Triangle,
            'right_triangle': RightTriangle,
            'hexagon': Hexagon,
            'parallelogram': Parallelogram
        }
        # Ітерує по ключах словника shape
        for key in shape:
            # Перевіряє, чи є назва фігури великими літерами
            if shape[key].isupper():
                # Знаходить відповідний клас для фігури
                shape_class = shape_classes[key]
                # Створює екземпляр класу з потрібними параметрами
                if key == 'triangle':
                    shape_obj = shape_class(5.0)
                    shape_obj.init_points(shape[key])
                elif key == 'right_triangle':
                    shape_obj = shape_class(10, 3, angle)
                    shape_obj.init_points(shape[key])
                elif key == 'hexagon':
                    shape_obj = shape_class(5)
                    shape_obj.init_points(shape[key])
                elif key == 'parallelogram':
                    shape_obj = shape_class(5, 10, 110)
                    shape_obj.init_points(shape[key])
                # Малює фігуру
                shape_obj.draw()


# Example usage:
geometry = Geometry()
shapes, points, segments, height_segments, parallels, need, angle = geometry.find_shapes_and_points(
    "In triangle XYZ, line segment XY is parallel to line segment ZW. Given that XY = 18 cm, ZW = 12 cm, and ZY = 15 cm, determine the length of XW.")
print(f"Shapes: {shapes}")
print(f"Points: {points}")
print(f"Segments: {segments}")
print(f"Height\tSegments: {height_segments}")
print(f"Parallels: {parallels}")
geometry.draw_shape(
    'In triangle XYZ, line segment XY is parallel to line segment ZW. Given that XY = 18 cm, ZW = 12 cm, and ZY = 15 cm, determine the length of XW.')
