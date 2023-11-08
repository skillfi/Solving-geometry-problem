import re
from typing import List, Tuple

from core.geomentry.circle.circle import CircleCustom
from core.geomentry.square.hexagon import Hexagon
from core.geomentry.square.square import Square
from core.geomentry.square.trapezoid import Trapezoid
from core.geomentry.triangles.right_triangle import RightTriangle
from core.geomentry.triangles.triange import Triangle
from core.geomentry.square.paralelogram import Parallelogram
from core.GPT.gpt4free import OpenAi4Free


class Geometry:
    """A class to find shapes and points in a given text using regular expressions."""

    def __init__(self, text):
        self.text = text
        # Define a dictionary of shapes and their regex patterns
        self.shapes = self.find_shapes()
        self.SubElements = self.subElements()
        self.Task = self.task()
        # Define a regex pattern for points

    def find_shapes(self):
        return {
            'triangle': re.compile(r'Triangle\s([A-Z]{3})', re.IGNORECASE).search(self.text),
            'right_triangle': self.triangle_types(),
            'circle': re.compile(r'Circle\s([A-Z]{1})\S', re.IGNORECASE).search(self.text),
            'square': re.compile(r'Square\s([A-Z]{4})\S', re.IGNORECASE).search(self.text),
            'parallelogram': re.compile(r'parallelogram\s([A-Z]{4})\S', re.IGNORECASE).search(string=self.text),
            'rectangle': re.compile(r'Rectangle\s([A-Z]{4})\S', re.IGNORECASE).search(self.text),
            'trapezoid': re.compile(r'trapezoid\s([A-Z]{4})', re.IGNORECASE).search(self.text),
            'hexagon': re.compile(r'\sHexagon\s([A-Z]{6})\S', re.IGNORECASE).search(string=self.text),
        }

    def subElements(self):
        return {
            'points': self.points(),
            'lines': re.compile(r'\s([A-Z]\d+)\s').search(self.text),
            'height': re.compile(r'\s([A-Z]{2})\s=').search(self.text) if re.compile(r'\s([A-Z]{2})\s=').search(
                self.text) else re.compile(r'\s(\d{2})\scm').search(self.text),
            'parallels': self.parallel_regex(),
            'angle': re.compile(r'\s(angle)\s([A-Z]{1})\smeasuring\s(\d+)\s(degrees)', re.IGNORECASE).search(self.text)
        }

    def points(self):
        regex_1 = re.compile(r'Point\s([A-Z]{1})\sis\son', re.IGNORECASE).search(self.text)
        regex_2 = re.compile(r'Point\s([A-Z]{1})\sis\son\ssegment\s([A-Z]{2})', re.IGNORECASE).search(self.text)
        if regex_2:
            result = re.compile(r'Point\s(([A-Z]{1})\sis\son\ssegment\s([A-Z]{2}))\ssuch\sthat\s([A-Z]{2})\s=\s([A-Z]{2})/(\d)\S', re.IGNORECASE).search(self.text)
            if result:
                return result
            return regex_2
        else:
            return regex_1

    def parallel_regex(self):
        first_regex = re.compile(r'\ssegment\s([A-Z]{2})\sis\sparallel\sto\sline\ssegment\s([A-Z]{2})',
                                 re.IGNORECASE).search(self.text)
        second_regex = re.compile(r'\s(parallel)\ssides\s([A-Z]{2})\sand\s([A-Z]{2})', re.IGNORECASE).search(self.text)
        third_regex = re.compile(r'\s([A-Z]{2})\sis\s(parallel)\sto\s([A-Z]{2})', re.IGNORECASE).search(self.text)
        parallels = (first_regex, second_regex, third_regex)
        for regex in parallels:
            if regex:
                return regex

    def task(self):
        def length(text):
            regex_1 = re.compile(r'find\sthe\slength\s(of\sthe\sother\sside|of\ssides([A-Z]{2})\sand\s([A-Z]{2})|of\s([A-Z]{2})|of\sside\s([A-Z]{2}))',
                                 re.IGNORECASE).search(text)
            regex_4 = re.compile(r'find\sthe\slength\s(of\sside\s([A-Z]{2}))',
                                 re.IGNORECASE).search(text)
            regex_5 = re.compile(r'calculate\sthe\slength\s(of\sside\s([A-Z]{2}))',
                                 re.IGNORECASE).search(text)
            regex_2 = re.compile(
                r'determine\sthe\slength\s(of\sthe\sother\sside|of\ssides([A-Z]){2}\sand\s([A-Z]{2})|of\s([A-Z]{2})|of\sside\s([A-Z]{2}))\S',
                re.IGNORECASE).search(text)
            regex_3 = re.compile(
                r'\swhat\sis\sthe\s(length|measure)\sof\s(side|segment)\s([A-Z]{2})',
                re.IGNORECASE).search(text)
            result = ''
            for r in (regex_1, regex_2, regex_3, regex_4, regex_5):
                if r:
                    for i in r.groups():
                        result = i
                        for expr in ('of\tthe\tother\tside', 'of\tsides', 'of\t', 'of\tside\t', 'length\t', 'side\t', 'segment\t', 'measure\t'):
                            if isinstance(i, str) and expr in i:
                                result.replace(expr, '\t')
            return result

        return {
            'measure': re.compile(r'\sfind\sthe\smeasure\sof\sangles\s([A-Z]{1})\S([A-Z]{1})\sand([A-Z]{1})\S',
                                  re.IGNORECASE).search(self.text),
            'length': length(self.text)
        }

    def triangle_types(self):
        first_regular = re.compile(r'\s(right)\sTriangle\s([A-Z]{3})\S', re.IGNORECASE).search(self.text)
        second_regular = re.compile(r'Triangle\s([A-Z]{3})\sis\sa\s(right)', re.IGNORECASE).search(self.text)
        return {1: first_regular, 2: second_regular}

    def lenght_segments(self, segment):
        return re.compile(segment + r'\shas\sa\slength\sof\s(\d+)\s')

    def set_height_to_segments(self):
        # Find all the line segments and other segments in the text
        line_segments = self.SubElements['lines']
        other_segments = self.SubElements['height']
        # Create an empty dictionary for segment heights
        segment_height = {}
        # Loop through all the segments
        for segment in line_segments + other_segments:
            # Compile a regex pattern to find the segment height in the text
            length = self.lenght_segments(segment).search(self.text)
            if length:
                for s in length.groups():
                    segment_height[segment] = int(s)
            compile_text = f'{segment}'
            pattern = re.compile(compile_text + r'\s=\s([1-9]{2})\scm\S')
            # Search for the pattern in the text
            match = pattern.search(self.text)
            # If a match is found, add the segment and its height to the dictionary
            if match:
                segment_height[segment] = int(match.group(1))
        # Return the segment height dictionary
        return segment_height

    def find_shapes_and_points(self):
        """A function to find shapes and points in a given text and return them as a dictionary and a list.

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
                matches = pattern
                # Якщо знайдено співпадіння, додаємо фігуру та її назву або тип до словника знайдених фігур
                if matches:
                    # Беремо перше співпадіння з групи
                    match = matches.group(1)
                    # Додаємо фігуру та співпадіння до словника
                    found_shapes[shape] = match

        # Find all the points in the text and store them in a list
        found_points = None
        if self.SubElements['points']:
            if self.SubElements['points'].groups().__len__() > 5:
                found_points = {}
                for g in self.SubElements['points'].groups():
                    pass
            found_points = self.SubElements['points'].groups()
        # Створення словника для зберігання паралельних рядків
        parallel = {}
        # Знаходження усіх паралельних рядків у тексті
        if self.SubElements['parallels']:
            parallels = self.SubElements['parallels'].groups()
            # Додавання кожного паралельного рядка до словника
            parallels = [p for p in parallels if p != 'parallel']
            i = 0
            for p in range(0, len(parallels)):
                # Видалення слова 'parallel' з кортежу
                # Якщо кортеж містить два різних елементи, додаємо їх до словника
                arg_0 = parallels[p]
                arg_1 = parallels[i]
                d = dict.fromkeys(parallels, arg_1)
                parallel = d
                i += 1

        # Якщо кортеж містить однакові елементи, ігноруємо їх
        # Знаходження потрібної інформації у тексті
        need = self.Task
        found_segments = None
        if self.SubElements['lines']:
            found_segments = self.SubElements['lines'].groups()
        # height_segments = self.set_height_to_segments()
        angles = self.SubElements['angle']

        # Повертає знайдені фігури, точки, сегменти, висоти, паралелi, потрібну інформацію та кути
        return (
            found_shapes,  # словник знайдених фігур
            found_points,  # список знайдених точок
            found_segments,  # список знайдених сегментів
            # height_segments,  # словник знайдених висот
            parallel,  # словник знайдених паралельних рядків
            need,  # потрібна інформація або None, якщо не знайдена
            {angles.group(2): int(angles.group(3))} if angles else None
        # словник знайденого кута або None, якщо не знайдений
        )

    def draw_shape(self):
        shape, points, segments, parallels, need, angle = self.find_shapes_and_points()
        # Створює словник, що відображає назви фігур на їх класи
        shape_classes = {
            'triangle': Triangle,
            'right_triangle': RightTriangle,
            'hexagon': Hexagon,
            'parallelogram': Parallelogram,
            'trapezoid': Trapezoid,
            'circle': CircleCustom,
            'square': Square
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
                    if len(parallels) > 1:
                        shape_obj.parallels(parallels)
                    if need['length'] != '':
                        shape_obj.task(need['length'], points=points)
                elif key == 'right_triangle':
                    shape_obj = shape_class(10, 3, angle)
                    shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        shape_obj.parallels(parallels)
                    if need['length'] != '':
                        shape_obj.task(need['length'])
                elif key == 'hexagon':
                    shape_obj = shape_class(5)
                    shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        shape_obj.parallels(parallels)
                    if need['length'] != '':
                        shape_obj.task(need['length'])
                elif key == 'parallelogram':
                    shape_obj = shape_class(5, 10, 110)
                    shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        shape_obj.parallels(parallels)
                    if need['length'] != '':
                        shape_obj.task(need['length'])
                elif key == 'trapezoid':
                    shape_obj = shape_class(top_length=5, bottom_length=10, height=10)
                    shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        shape_obj.parallels(parallels)
                    if need['length'] != '':
                        shape_obj.task(need['length'])
                elif key == 'square':
                    shape_obj = shape_class(side_length=5)
                    shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        shape_obj.parallels(parallels)
                    if need['length'] != '':
                        shape_obj.task(need['length'])
                elif key == 'circle':
                    shape_obj = shape_class(center=[5.0, 5.0])
                    shape_obj.init_points(shape[key])
                # Малює фігуру
                shape_obj.draw()

# response = OpenAi4Free().generate_geometry_tasks('In triangle XYZ, line segment XY is parallel to line segment ZW. Given that XY = 18 cm, ZW = 12 cm, and ZY = 15 cm, determine the length of XW.')
# Example usage:
geometry = Geometry(
    'In trapezoid ABCD, AB || CD, and angle A measures 80 degrees. If AB = 12 cm and CD = 8 cm, calculate the length of side BC.')
shapes, points, segments, parallels, need, angle = geometry.find_shapes_and_points()
print(f"Shapes: {shapes}")
print(f"Points: {points}")
print(f"Segments: {segments}")
# print(f"Height\tSegments: {height_segments}")
print(f"Parallels: {parallels}")
print(f"Find: {need}")
geometry.draw_shape()
