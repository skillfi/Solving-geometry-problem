import re

import pandas

from core.geomentry.circle.circle import CircleCustom
from core.geomentry.square.hexagon import Hexagon
from core.geomentry.square.paralelogram import Parallelogram
from core.geomentry.square.rectangle import Rectangle
from core.geomentry.square.rhombus import Rhombus
from core.geomentry.square.square import Square
from core.geomentry.square.trapezoid import Trapezoid
from core.geomentry.triangles.right_triangle import RightTriangle
from core.geomentry.triangles.triange import Triangle


class Geometry:
    """A class to find shapes and points in a given text using regular expressions."""

    def __init__(self, text):
        self.text = text
        # Define a dictionary of shapes and their regex patterns
        self.shapes = self.find_shapes()
        self.SubElements = self.subElements()
        self.Task = self.task()
        self.diagonals = self.diagonals_regex()
        # Define a regex pattern for points

    def __repr__(self):
        return f'<Geometry: (task: {self.text})>'

    def find_shapes(self):
        return {
            'triangle': re.compile(r'Triangle\s([A-Z]{3})', re.IGNORECASE).search(self.text),
            'right_triangle': self.triangle_types(),
            'circle': re.compile(r'Circle\s([A-Z]{1})\S', re.IGNORECASE).search(self.text),
            'square': re.compile(r'([A-Z]{4})', re.IGNORECASE).search(self.text),
            'parallelogram': re.compile(r'parallelogram\s([A-Z]{4})', re.IGNORECASE).search(string=self.text),
            'rectangle': re.compile(r'rectangle\s([A-Z]{4})', re.IGNORECASE).search(self.text),
            'trapezoid': re.compile(r'trapezoid\s([A-Z]{4})', re.IGNORECASE).search(self.text),
            'hexagon': re.compile(r'\sHexagon\s([A-Z]{6})\S', re.IGNORECASE).search(string=self.text),
            'rhombus': re.compile(r'\srhombus\s([A-Z]{4})\S', re.IGNORECASE).search(string=self.text),
        }

    def square_types(self, types: str):
        pass

    def subElements(self):
        return {
            'points': self.points(),
            'lines': re.compile(r'\s([A-Z]\d+)\s').search(self.text),
            'height': re.compile(r'\s([A-Z]{2})\s=').search(self.text) if re.compile(r'\s([A-Z]{2})\s=').search(
                self.text) else re.compile(r'\s(\d{2})\scm').search(self.text),
            'parallels': self.parallel_regex(),
            'angle': re.compile(r'\s(angle)\s([A-Z]{1})\smeasuring\s(\d+)\s(degrees)', re.IGNORECASE).search(self.text)
        }

    def diagonals_regex(self):
        # Компілюємо регулярний вираз
        reg_1 = re.compile(r'\sdiagonals\s([A-Z]{2})\sand\s([A-Z]{2})\s', re.IGNORECASE)
        match = reg_1.search(self.text)  # Використовуємо скомпільований об'єкт для пошуку
        if match:
            # Використовуємо спискове включення для створення списку результатів
            result = [group for group in match.groups() if group.isupper()]
            return result

    def points(self):
        regex_1 = re.compile(r'Point\s([A-Z]{1})\s\S+\s\S+\s', re.IGNORECASE).search(self.text)
        regex_2 = re.compile(r'Point\s([A-Z]{1})\s\S+\s\S+\ssegment\s([A-Z]{2})', re.IGNORECASE).search(self.text)
        if regex_2:
            result = re.compile(
                r'Point\s(([A-Z]{1})\sis\son\ssegment\s([A-Z]{2}))\s\S+\s\S+\s([A-Z]{2})\s=\s([A-Z]{2})/(\d)\S',
                re.IGNORECASE).search(self.text)
            if result:
                return result
            return regex_2
        else:
            return regex_1

    def parallel_regex(self):
        # Компілюємо регулярні вирази
        first_regex = re.compile(r'\ssegment\s([A-Z]{2})\s\S+\sparallel\s\S+\s\S+\s\S+\s([A-Z]{2})',
                                 re.IGNORECASE)
        second_regex = re.compile(r'\s(parallel)\s\S+\s([A-Z]{2})\sand\s([A-Z]{2})', re.IGNORECASE)
        third_regex = re.compile(r'\s([A-Z]{2})\s\S+\s(parallel)\s\S+\s([A-Z]{2})', re.IGNORECASE)
        parallels = (first_regex, second_regex, third_regex)
        for regex in parallels:
            match = regex.search(self.text)  # Використовуємо скомпільовані об'єкти для пошуку
            if match:
                return match  # Використовуємо ранній вихід з циклу

    def task(self):
        def length(text, diagonals: bool):
            # Компілюємо регулярні вирази з ефективними шаблонами
            regex_1 = re.compile(r'find\s\S+\slength\sof(\s|\s\S+)\s([A-Z]{2})', re.IGNORECASE)
            regex_2 = re.compile(r'determine\s\S+\slength\s\S+\s([A-Z]{2})\S', re.IGNORECASE)
            regex_3 = re.compile(r'\swhat\s\S+\s(length|measure)\s\S+\s([A-Z]{2})', re.IGNORECASE)
            regex_4 = re.compile(r'(calculate|find)\s\S+\slength\s\S+\s\S+\s([A-Z]{2})', re.IGNORECASE)
            regex_5 = re.compile(r'find\s\S+\slength\s\S+\s\S+\s(diagonals)\s([A-Z]{2})\sand\s([A-Z]{2})\S',
                                 re.IGNORECASE)
            result = ''
            diagonal = []
            # Використовуємо ранній вихід з циклів
            for r in (regex_1, regex_2, regex_3, regex_4, regex_5):
                match = r.search(text)  # Використовуємо скомпільовані об'єкти для пошуку
                if match:
                    # Використовуємо спискове включення для створення списку результатів
                    result = [group for group in match.groups() if group.isupper()]
                    if 'diagonals' in match.group() and diagonals:
                        diagonal = result  # Зберігаємо діагоналі в окремому списку
                        break
                    elif result.__len__() > 0 and 'diagonals' not in match.group():
                        result = result[0]  # Повертаємо першу групу, яка відповідає літерам
                        break
                    elif result.__len__() == 0:
                        continue
            return [result, diagonal]

        return {
            'measure': re.compile(r'\sfind\s\S+\smeasure\s\S+\s([A-Za-z]{1})\S([A-Za-z]{1})\sand([A-Za-z]{1})\S',
                                  re.IGNORECASE).search(self.text),
            'length': length(self.text, False)[0],
            'diagonals': length(self.text, True)[1],
        }

    def triangle_types(self):
        first_regular = re.compile(r'\s(right)\sTriangle\s([A-Z]{3})\S', re.IGNORECASE).search(self.text)
        second_regular = re.compile(r'Triangle\s([A-Z]{3})\s\S+\s\S+\s(right)', re.IGNORECASE).search(self.text)
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
        diagonals = self.diagonals

        # Повертає знайдені фігури, точки, сегменти, висоти, паралелi, потрібну інформацію та кути
        return (
            found_shapes,  # словник знайдених фігур
            found_points,  # список знайдених точок
            found_segments,  # список знайдених сегментів
            # height_segments,  # словник знайдених висот
            parallel,  # словник знайдених паралельних рядків
            need,  # потрібна інформація або None, якщо не знайдена
            {angles.group(2): int(angles.group(3))} if angles else None,
            # словник знайденого кута або None, якщо не знайдений
            diagonals
        )

    def send_to_chat_df_data(self):
        shape, points, segments, parallels, need, angle, diagonals = self.find_shapes_and_points()
        print(f"1.\tShapes: {shape}\n"
              f"2.\tPoints: {points}\n"
              f"3.\tSegments: {segments}\n"
              f"4.\tOthers:\n\t1)Parallels: {parallels}\n2)\tDiagonals: {diagonals}\n"
              f"5.\tNeed to find:\n\t1)\tMeasure: {need['measure']}\n\t2)\tFind of side(s): {need['length']}\n\t"
              f"3)\tFind diagonals: {need['diagonals']}")
        shape_classes = {
            'triangle': Triangle,
            'right_triangle': RightTriangle,
            'hexagon': Hexagon,
            'parallelogram': Parallelogram,
            'trapezoid': Trapezoid,
            'circle': CircleCustom,
            'square': Square,
            'rectangle': Rectangle,
            'rhombus': Rhombus,
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
                    df: pandas.DataFrame = shape_obj.init_points(shape[key])
                    # if len(parallels) > 1:
                    #     df = shape_obj.parallels(parallels, df, True)
                    return df, [point for point in shape[key]]
                    # df = shape_obj.add_lines_to_df(df)
                elif key == 'right_triangle':
                    shape_obj = shape_class(10, 3, angle)
                    df = shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        df = shape_obj.parallels(parallels, df, True)
                    return df, [point for point in shape[key]]
                elif key == 'hexagon':
                    shape_obj = shape_class(5)
                    df = shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        df = shape_obj.parallels(parallels, df, True)
                    return df, [point for point in shape[key]]
                elif key == 'parallelogram':
                    shape_obj = shape_class(5, 10, 110)
                    df = shape_obj.__init_points__(shape[key])
                    if len(parallels) > 1:
                        df = shape_obj.parallels(parallels, df, True)
                    return df, [point for point in shape[key]]
                elif key == 'trapezoid':
                    shape_obj = shape_class(top_length=5, bottom_length=10, height=10)
                    df = shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        df = shape_obj.parallels(parallels, df, True)
                    return df, [point for point in shape[key]]
                elif key == 'square':
                    shape_obj = shape_class(side_length=5)
                    df = shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        df = shape_obj.parallels(parallels, df, True)
                    return df, [point for point in shape[key]]
                elif key == 'rectangle':
                    shape_obj = shape_class(6, 4)
                    df = shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        df = shape_obj.parallels(parallels, df, True)
                    return df, [point for point in shape[key]]
                elif key == 'rhombus':
                    shape_obj = shape_class(10, 60)
                    df = shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        df = shape_obj.parallels(parallels, df, True)
                    return df, [point for point in shape[key]]
                elif key == 'circle':
                    shape_obj = shape_class(center=[5.0, 5.0])
                    df = shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        df = shape_obj.parallels(parallels, df, True)
                    return df, [point for point in shape[key]]

    def draw_shape(self):
        shape, points, segments, parallels, need, angle, diagonals = self.find_shapes_and_points()

        # Створює словник, що відображає назви фігур на їх класи
        shape_classes = {
            'triangle': Triangle,
            'right_triangle': RightTriangle,
            'hexagon': Hexagon,
            'parallelogram': Parallelogram,
            'trapezoid': Trapezoid,
            'circle': CircleCustom,
            'square': Square,
            'rectangle': Rectangle,
            'rhombus': Rhombus,
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
                    df = shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        shape_obj.parallels(parallels, df)
                    if need['length'] != '' and isinstance(need['length'], str):
                        shape_obj.task(need['length'], points=points)
                elif key == 'right_triangle':
                    shape_obj = shape_class(10, 3, angle)
                    df = shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        shape_obj.parallels(parallels, df)
                    if need['length'] != '' and isinstance(need['length'], str):
                        shape_obj.task(need['length'])
                elif key == 'hexagon':
                    shape_obj = shape_class(5)
                    df = shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        shape_obj.parallels(parallels, df)
                    if need['length'] != '' and isinstance(need['length'], str):
                        shape_obj.task(need['length'])
                elif key == 'parallelogram':
                    shape_obj = shape_class(5, 10, 110)
                    df = shape_obj.__init_points__(shape[key])
                    if len(parallels) > 1:
                        shape_obj.parallels(parallels, df)
                    if need['length'] != '' and isinstance(need['length'], str):
                        shape_obj.task(need['length'])
                    if diagonals.__len__() > 1:
                        shape_obj.diagonals(diagonals, df)
                elif key == 'trapezoid':
                    shape_obj = shape_class(top_length=5, bottom_length=10, height=10)
                    df = shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        shape_obj.parallels(parallels, df)
                    if need['length'] != '' and isinstance(need['length'], str):
                        shape_obj.task(need['length'])
                elif key == 'square':
                    shape_obj = shape_class(side_length=5)
                    df = shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        shape_obj.parallels(parallels, df)
                    if need['length'] != '' and isinstance(need['length'], str):
                        shape_obj.task(need['length'])
                elif key == 'rectangle':
                    shape_obj = shape_class(6, 4)
                    df = shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        shape_obj.parallels(parallels, df)
                    if need['length'] != '' and isinstance(need['length'], str):
                        shape_obj.task(need['length'])
                elif key == 'rhombus':
                    shape_obj = shape_class(10, 60)
                    df = shape_obj.init_points(shape[key])
                    if len(parallels) > 1:
                        shape_obj.parallels(parallels, df)
                    if need['length'] != '' and isinstance(need['length'], str):
                        shape_obj.task(need['length'], df)
                    if need['diagonals'] != '':
                        shape_obj.task(None, df, need['diagonals'])
                elif key == 'circle':
                    shape_obj = shape_class(center=[5.0, 5.0])
                    df = shape_obj.init_points(shape[key])
                # Малює фігуру
                shape_obj.draw()
