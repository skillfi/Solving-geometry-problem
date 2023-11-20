from core.GPT.gpt import OpenAI
from core.geomentry.geometry import Geometry


class App:

    def __init__(self):
        self.ai = OpenAI()

    def run(self):
        choose = int(input(f'Choose variant:\n\t1.Create\tgeometry\ttasks.\n\t2.Plot\ttask\ton\tmatplotlib.'))
        if choose == 1:
            tasks = int(input(f'How many tasks create?\nWrite\there:\t'))
            self.ai.write_to_file(tasks, 'user', 'chat')
        if choose == 2:
            plot_task = str(input(f'Write\ta\ttask\there:\t'))
            g = Geometry(plot_task)
            # df, points = g.send_to_chat_df_data()
            print('Request is sending')
            self.ai.plot(g.text)


if __name__ == "__main__":
    App().run()
