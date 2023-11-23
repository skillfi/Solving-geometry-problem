from core.GPT.gpt import OpenAI
from core.geomentry.geometry import Geometry


class App:

    def __init__(self):
        self.ai = OpenAI()

    def run(self):
        choose = int(input(f'Choose variant:\n\t1.Create\tgeometry\ttasks.\n\t2.Plot\ttask\ton\tmatplotlib.\n3.Create a summary by book and author.'))
        if choose == 1:
            tasks = int(input(f'How many tasks create?\nWrite\there:\t'))
            self.ai.write_to_file(tasks, 'user', 'chat')
        if choose == 2:
            plot_task = str(input(f'Write\ta\ttask\there:\t'))
            g = Geometry(plot_task)
            # df, points = g.send_to_chat_df_data()
            print('Request is sending')
            self.ai.plot(g.text)
        if choose == 3:
            book = str(input(f'Write a book name (for create a summary):\t'))
            author = str(input(f'Write a book author (for create a summary):\t'))
            result = self.ai.summary(book, author)
            print(result)


if __name__ == "__main__":
    App().run()
