from core.GPT.gpt import OpenAI
from core.geomentry.geometry import Triangle

shapes = ['triangle', 'square']

# OpenAI().write_to_file(shapes)
response = OpenAI().create_geometry_task()
print(response)