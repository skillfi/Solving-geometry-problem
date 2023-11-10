import pandas
from plotai.plotai import Prompt


class CustomPrompt(Prompt):
    def __init__(self, prompt="", df: pandas.DataFrame=None, x=None, y=None, z=None, previous_code="", previous_error="", data={}, points=[]):
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
        Create a plot in Python with matplotlib package.
         1.\tDraw the entire figure based on the problem below, plot show contain:\n
         \t1) Problem:\n\t{self.prompt}
         \t2)\tGet\tshape\tpoints\tfrom\tproblem;\n
         \t3)\tGet\tsides,parallels,diagonals,perpendicular and other sides from task;\n
         \t4)\tGet\tangles\tfrom\tproblem;\n
         \t5)\tGet\tmidpoints\tfrom\tproblem\t\tand\tadd\tannotation\tif\nnot\texist;\n
         \t6)\tGet\twhat needs to be found\tfrom\tproblem.\n
         2.\tUse\tthis\tdataframe:\n\t{self.input_data_str()};
        3.\tUse:\t\nplt.axes('off');
        4.\tSave\tplot\t.
         
             
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
        return "Generate geometry problems similar to those in textbooks."
