import pandas
from plotai.plotai import Prompt


class CustomPrompt(Prompt):
    def __init__(self, prompt="", df: pandas.DataFrame = None, x=None, y=None, z=None, previous_code="",
                 previous_error="", data={}, points=[]):
        super().__init__(prompt, df, x, y, z, previous_code, previous_error)
        self.df: pandas.DataFrame = df
        self.points = points

    def input_data_str(self):
        # Використовуємо ранній вихід з функції, якщо df є None
        if self.df is None:
            return None
        # Використовуємо f-рядок для форматування вхідних даних
        return f"""
            ```python
            # pandas DataFrame
            '''
            {self.df.head(5)}
            '''
            # DataFrame columns
            '''
            {self.df.columns.to_list()}
            '''

            # pandas data frame variable is df

        ```
            """

    @property
    def value(self):
        # Використовуємо f-рядок для форматування вхідних даних і завдання
        v = f"""Create a plot in Python with matplotlib package. 

        Use this pandas dataframe data:

        {self.input_data_str()}


        Plot should contain: {self.prompt}
        
        Add plt.axes('off') to code
        Save plot

        Initial python code to be updated        

        ```python
        # TODO import required dependencies
        # TODO Provide the plot
        ```

        Output only Python code.
        """

        if self.previous_code != "":
            # Використовуємо f-рядок для додавання попереднього коду і помилки
            v += f"""

            You generated previously below code:
            {self.previous_code}

            It returned below error:
            {self.previous_error}

            Fix it. Do not return the same code again.
            """
        return v

    @property
    def custom_value(self):
        v = f""" 
        Create a plot in Python using matplotlib and pandas packages.
         1.\tMake pandas dataframe based on points (vertices) coordinates, get it from problem bellow:\n
         \t1)\t{self.prompt};
         \t2)\tFrom created dataframe plot figure (if figure is shape use Polygon from matplotlib) based on problem;\n
         \t3)(if figure is shape Connect not connected vertices) else draw condition and annotate only points, angles without formulas and solution;
         \t4)\tGet all determine conditions from task without solution.\n
        2.\tUse:\t\nplt.axes('off');
        3.\tSave\tplot\t.
         
             
        Initial python code to be updated        

        ```python
        # TODO import required dependencies
        # TODO Provide the plot
        ```

        Output only Python code.
        """
        if self.previous_code != "":
            # Використовуємо f-рядок для додавання попереднього коду і помилки
            v += f"""

            You generated previously below code:
            {self.previous_code}

            It returned below error:
            {self.previous_error}

            Fix it and optimize. Do not return the same code again.
            """
        return v

    @classmethod
    def geometry_value(cls):
        return "Generate geometry problems similar to those in textbooks (without solution) " \
               "points have coordinates example: A<x, y> and numerate problem by example: 1]. problem text ."

    @classmethod
    def geometry_value_2(cls):
        return "Generate geometry problems for profile level similar to those in textbooks  (without solution) " \
               "points have coordinates example: A<x, y> and numerate problem by example: 1]. problem text ."

    @classmethod
    def teacher_summary(cls, book_name, author):
        """
        Generate a teacher's summary and discussion instructions
        :param book_name:
        :param author:
        :return:
        """
        return f"Create a teacher's summary page for the book '{book_name}' by {author}. Provide a brief summary and instructions on how to discuss it."
