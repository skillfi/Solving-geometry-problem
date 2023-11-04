import datetime
import random
from functools import lru_cache
from typing import List

import openai

from core.config import api_key

openai.api_key = api_key


class OpenAI:
    """Клас для використання OpenAI API для генерації геометричних завдань."""

    def __init__(self):
        # Ініціалізує клас з вашим API-ключем
        self.api_key = api_key
        openai.api_key = api_key

    @lru_cache(maxsize=None)
    # Метод для генерації геометричних завдань
    def generate_geometry_tasks(self, num_tasks: int) -> List[str]:
        """Генерує список геометричних завдань за допомогою моделі gpt-3.5-turbo.

        Параметри:
            num_tasks (int): кількість завдань, які потрібно згенерувати.

        Повертає:
            List[str]: список рядків, що містять геометричні завдання.
        """
        tasks = []
        for i in range(num_tasks):
            prompt = "Generate geometry problems similar to those in textbooks."
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo', messages=[dict(role='user', content=prompt)]
            )
            task = response.choices[0].message.content
            tasks.append(task)
        return tasks

    def write_to_file(self, tasks: int) -> None:
        """Записує список геометричних завдань у текстовий файл.

        Параметри:
            tasks (int): кількість завдань, які потрібно згенерувати та записати.

        Повертає:
            None: нічого не повертає, але створює файл 'geometry_tasks.txt' у поточній директорії.
        """
        # Створює список завдань з використанням методу generate_geometry_tasks
        tasks = self.generate_geometry_tasks(tasks)
        # Записує завдання у текстовий файл
        with open("geometry_tasks.txt", "w", encoding='utf-8') as file:
            for i, task in enumerate(tasks, 1):
                file.write(f"Task {i}:\n{task}\n\n")

        print("Завдання збережено у файлі 'geometry_tasks.txt'.")

