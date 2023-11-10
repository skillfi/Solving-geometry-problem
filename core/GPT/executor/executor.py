import os
import re
import tempfile

from plotai.code.executor import Executor

from core.GPT.prompt.prompt import CustomPrompt

dir = os.getcwd()

class CustomExecutor(Executor):

    def __init__(self, prompt: CustomPrompt):
        super().__init__()
        self.prompt = prompt

    def run(self, code, globals_env=None, locals_env=None):
        try:
            # Використовуємо регулярний вираз для видалення коду, який не є частиною Python
            code = re.sub(r"(?s).*```python(.*?)```.*", r"\1", code).strip()
            # Використовуємо модуль tempfile для створення тимчасового файлу з кодом
            with tempfile.NamedTemporaryFile(mode="w", suffix=".py", encoding="utf-8", delete=False,) as tmp_file:
                # Записуємо код у файл
                code.replace('plt.show()', 'plt.axis("off")\nplt.show()')
                tmp_file.write(code)
                # Закриваємо файл
                tmp_file.close()
                # Виконуємо код з файлу, передаючи глобальні та локальні змінні
                exec(open(tmp_file.name, mode="r", encoding="utf-8").read(), globals_env, locals_env)
                os.remove(tmp_file.name)
        except Exception as e:
            return str(e)
        return None

