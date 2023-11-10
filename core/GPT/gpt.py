import datetime
import random
from functools import lru_cache
from typing import List

import openai
from plotai.code.logger import Logger

from core.GPT.executor.executor import CustomExecutor
from core.GPT.prompt.prompt import CustomPrompt
from core.config import api_key

openai.api_key = api_key


class OpenAI:
    """Клас для використання OpenAI API для генерації геометричних завдань."""

    def __init__(self):
        # Ініціалізує клас з вашим API-ключем
        self.api_key = api_key
        openai.api_key = api_key

    def api(self):
        openai.api_key = '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'
        openai.api_base = 'http://127.0.0.1:8090/v1'

    # Метод для генерації геометричних завдань
    def generate_geometry_tasks(self, num_tasks: int, api=False) -> List[str]:
        """Генерує список геометричних завдань за допомогою моделі gpt-3.5-turbo.

        Параметри:
            num_tasks (int): кількість завдань, які потрібно згенерувати.

        Повертає:
            List[str]: список рядків, що містять геометричні завдання.
        """
        tasks = []
        for i in range(num_tasks):
            prompt = CustomPrompt.geometry_value()
            if api:
                self.api()
            response = self.chat(prompt)
            task = response
            tasks.append(task)
        return tasks

    @lru_cache(maxsize=None)
    def chat(self, prompt, stream=False):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[dict(role='user', content=prompt)],
            stream=stream
        )
        if isinstance(response, dict):
            # Not streaming
            return response.choices[0].message.content
        else:
            text = ''
            # Streaming
            for token in response:
                content = token["choices"][0]["delta"].get("content")
                if content is not None:
                    text = text + content
            return text

    def plot(self, task, df, api=False, points=[]):
        p = CustomPrompt(task, df, points=points)
        # streamed completion
        if api:
            self.api()
        chat_completion = self.chat(p.custom_value, True)
        executor = CustomExecutor(p)
        error = executor.run(chat_completion, globals(), locals())
        if error is not None:
            # Logger().log({"title": "Error in code execution", "details": error})
            p_again = CustomPrompt(task, df, previous_code=chat_completion, previous_error=error, points=points)

            # Logger().log({"title": "Prompt with fix", "details": p_again.value})

            response = self.chat(p_again.custom_value, True)

            # Logger().log({"title": "Response", "details": response})

            executor = CustomExecutor(p_again)
            error = executor.run(response, globals(), locals())
            if error is not None:
                Logger().log({"title": "Error in code execution", "details": error})

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
