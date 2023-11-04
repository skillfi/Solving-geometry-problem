import re
from typing import List, Tuple

import matplotlib
from matplotlib import pylab

from core.geomentry.triangles.triange import Triangle


class Geometry:
    """A class to find shapes and points in a given text using regular expressions."""

    def __init__(self):
        # Define a dictionary of shapes and their regex patterns
        self.shapes = {
            'triangle': re.compile(r'\sTriangle\s([A-Z]{3})\S', re.IGNORECASE),
            'circle': re.compile(r'Circle\s([A-Z]{1})\s', re.IGNORECASE),
            'square': re.compile(r'Square\s([A-Z]{4})\s', re.IGNORECASE),
            'rectangle': re.compile(r'Rectangle\s([A-Z]{4})\s', re.IGNORECASE),
            'hexagon': re.compile(r'\sHexagon\s([A-Z]{6})\S', re.IGNORECASE),
            # Add more shapes and their regex patterns here
        }
        # Define a regex pattern for points
        self.points = re.compile(r'Point\s([A-Z]{1})\sis\son', re.IGNORECASE)
        self.line_segment = re.compile(r'line\ssegment\s([A-Z]{2})')
        self.other_segments = re.compile(r'\s([A-Z]{2})\s=')
        self.height_segment = re.compile(r'\s([1-9]{2})\scm')
        self.parallels = re.compile(r'\s([A-Z]{2})\sis\s(parallel)\sto\sline\ssegment\s([A-Z]{2})')

    def set_height_to_segments(self, text):
        # Find all the line segments and other segments in the text
        line_segments = self.line_segment.findall(text)
        other_segments = self.other_segments.findall(text)
        # Create an empty dictionary for segment heights
        segment_height = {}
        # Loop through all the segments
        for segment in line_segments + other_segments:
            # Compile a regex pattern to find the segment height in the text
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
        # Create an empty dictionary for found shapes
        found_shapes = {}
        # Loop through the shapes dictionary and search for matches in the text
        for shape, pattern in self.shapes.items():
            # Пошук ігноруючи регістр
            matches = pattern.findall(text)
            # If a match is found, add the shape and its name or type to the found shapes dictionary
            for match in matches:
                found_shapes[shape] = match
        # Find all the points in the text and store them in a list
        found_points = self.points.findall(text)
        # Створення порожнього словника для зберігання паралельних рядків
        parallel = {}
        # Знаходження усіх паралельних рядків у тексті за допомогою регулярного виразу
        parallels: List[Tuple[str]] = self.parallels.findall(text)
        # Додавання кожного паралельного рядка до словника як ключа та значення
        for p in parallels:
            # Якщо паралельний рядок складається з двох однакових елементів, то використовуємо перший елемент як значення
            # Інакше, використовуємо None як значення
            p = [i for i in p if i not in ('parallel', )]
            value = p[1]
            # Створюємо словник з ключів та значень з кортежу p
            d = dict.fromkeys(p, value)
            # Оновлюємо словник parallel зі словника d
            parallel.update(d)
        par = {}
        for key in parallel:
            if key == parallel[key]:
                pass
            else:
                par[key] = parallel[key]

        found_segments = self.line_segment.findall(text)
        height_segments = self.set_height_to_segments(text)
        # Return the found shapes and points
        return found_shapes, found_points, found_segments, height_segments, par

    def draw_shape(self, text):
        shape, points, segments, height_segments, parallels = self.find_shapes_and_points(text)
        for key in shape:
            if key in ('triangle',):
                triangle = Triangle(5.0)
                triangle.init_points(shape[key], )
                triangle.draw()


# Example usage:
geometry = Geometry()
shapes, points, segments, height_segments, parallels = geometry.find_shapes_and_points(
    "In triangle XYZ, line segment XY is parallel to line segment ZW. Given that XY = 18 cm, ZW = 12 cm, and ZY = 15 cm, determine the length of XW.")
print(f"Shapes: {shapes}")
print(f"Points: {points}")
print(f"Segments: {segments}")
print(f"Height\tSegments: {height_segments}")
print(f"Parallels: {parallels}")
geometry.draw_shape(
    'In triangle XYZ, line segment XY is parallel to line segment ZW. Given that XY = 18 cm, ZW = 12 cm, and ZY = 15 cm, determine the length of XW.')
