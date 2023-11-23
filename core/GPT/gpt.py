import datetime
import json
import json
import re
import time
from typing import List, Literal

import openai
from openai.openai_object import OpenAIObject
from openai.openai_response import OpenAIResponse
from plotai.code.logger import Logger

from core.GPT.executor.executor import CustomExecutor
from core.GPT.prompt.prompt import CustomPrompt
from core.config import app


class OpenAI:
    """Клас для використання OpenAI API для генерації геометричних завдань."""

    def __init__(self):
        # Ініціалізує клас з вашим API-ключем
        self.api_key = app['config'].get('api_key')
        openai.api_key = self.api_key

    def api(self):
        openai.api_key = app['config'].get('hugging_key')
        openai.api_base = app['config'].get('host')

    # Метод для генерації геометричних завдань
    def generate_geometry_tasks(self, role: Literal['assistant', 'user', 'teacher'],
                                oai: Literal['chat', 'Completion']) -> List[str]:
        """Генерує список геометричних завдань за допомогою моделі gpt-4-0613.

        Модель gpt-4-0613 є новітньою версією моделі gpt-3.5-turbo, яка використовує нейронну мережу з 4 мільярдами параметрів і здатна генерувати складні та цікаві геометричні завдання на різні теми.

        Параметри:
            api (bool): чи використовувати api для зв'язку з моделлю. За замовчуванням береться з конфігурації додатку.
            role (str): роль користувача, яка впливає на стиль та складність завдань. Можливі значення: 'user', 'teacher', 'student'. За замовчуванням 'user'.

        Повертає:
            List[str]: список рядків, що містять геометричні завдання. Кожне завдання має формат: 'Тема. Номер. Текст.'.

        Приклади:
            >>> generate_geometry_tasks(api=True, role='teacher')
            ['Трикутники. 1] Знайдіть кут між бісектрисою та висотою, проведеними з вершини прямого кута прямокутного трикутника.',
             'Кола. 2] Знайдіть радіус кола, якщо відомо, що довжина дуги, що відповідає центральному куту 60 градусів, дорівнює 5 см.',
             'Площі фігур. 3] Знайдіть площу трапеції, якщо відомо, що її основи дорівнюють 8 см і 12 см, а висота дорівнює 6 см.']
        """
        # Використовуємо регулярний вираз для витягування теми, номера і тексту задачі
        pattern = re.compile(r'\d+\S+\s*(.*)')
        prompt = CustomPrompt.geometry_value_2()
        if app['config'].get('api'):
            self.api()
        if oai == 'Completion':
            response = self.completention(prompt)
        elif oai == 'chat':
            response = self.chat(prompt, False, role)
        # Використовуємо функцію findall для знаходження всіх задач у відповіді
        problems = pattern.findall(response)
        if problems:
            # Повертаємо список задач без додаткового словника
            return problems

    def completention(self, prompt):
        start_time = time.time()
        response = openai.Completion.create(model='text-davinci-002', prompt=prompt, temperature=0.5)
        # calculate the time it took to receive the response
        response_time = time.time() - start_time
        # extract the text from the response
        completion_text = response['choices'][0]['text']
        print(f"Full response received {response_time:.2f} seconds after request")
        return completion_text

    def chat(self, prompt, stream: Literal[True, False], role: Literal['assistant', 'user', 'teacher']):
        param: Literal[
            dict(content=prompt, role=role),
            dict(content=prompt, role=role),
            dict(content=prompt, role=role)] = None
        if role == 'user':
            param = dict(content=prompt, role=role)
        if role == 'assistant':
            param = dict(content=prompt, role=role)
        start_time = time.time()
        response = openai.ChatCompletion.create(model="gpt-4-0613",
                                                messages=[param],
                                                stream=stream,
                                                presence_penalty=0.5)
        response_time = time.time() - start_time
        print(f"Full response received {response_time:.2f} seconds after request")
        if isinstance(response, OpenAIObject) or isinstance(response, OpenAIResponse) or isinstance(response, dict):
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

    def plot(self, task, df=None, points=[]):
        p = CustomPrompt(task, df, points=points)
        # streamed completion
        if app['config'].get('api'):
            self.api()
        chat_completion = self.chat(p.custom_value, False, 'assistant')
        executor = CustomExecutor(p)
        error = executor.run(chat_completion, globals(), locals())
        if error is not None:
            # Logger().log({"title": "Error in code execution", "details": error})
            p_again = CustomPrompt(task, df, previous_code=chat_completion, previous_error=error, points=points)

            Logger().log({"title": "Prompt with fix", "details": p_again.value})

            response = self.chat(p_again.custom_value, False, 'assistant')

            # Logger().log({"title": "Response", "details": response})

            executor = CustomExecutor(p_again)
            error = executor.run(response, globals(), locals())
            if error is not None:
                Logger().log({"title": "Error in code execution", "details": error})

    def write_to_file(self, input: int, role: Literal['assistant', 'user', 'teacher'],
                      oai: Literal['chat', 'Completion']) -> None:
        """Записує список геометричних завдань у текстовий файл.

        Параметри:
            tasks (int): кількість завдань, які потрібно згенерувати та записати.

        Повертає:
            None: нічого не повертає, але створює файл 'geometry_tasks.json' у поточній директорії.
        """
        # Створює список завдань з використанням методу generate_geometry_tasks
        tasks = {}
        for i in range(1, input):
            task = self.generate_geometry_tasks(role=role, oai=oai)
            tasks[i] = task
        # Записує завдання у json
        with open(f"geometry_hard_tasks_{role}.json", "w", encoding='utf-8') as file:
            j_obj = json.dumps(tasks, ensure_ascii=True, indent=3)
            file.write(j_obj)
            file.close()
            print(f"Завдання збережено у файлі '{file.name}'.")

    def summary(self, book, author):
        p = CustomPrompt.teacher_summary(book, author)
        if app['config'].get('api'):
            self.api()
        chat_completion = self.chat(p, False, 'user')
        return chat_completion
