from core.GPT.gpt import OpenAI
from core.geomentry.geometry import Geometry

gpt = OpenAI()
task = input('Write a task here: \n')
g = Geometry(task)
df, points = g.send_to_chat_df_data()
gpt.plot(g.text, df, True)