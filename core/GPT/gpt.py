import datetime
import random
from functools import lru_cache
from typing import List

import openai

from core.config import api_key

openai.api_key = api_key


class OpenAI:
    def __init__(self):
        # Initialize the class with your API key
        self.api_key = api_key
        openai.api_key = api_key

    @lru_cache(maxsize=None)
    def create_geometry_prompts(self, shape):
        # Create a geometry task using the openai.Completion method
        # Define the prompt for the task
        prompt = f"Create a geometry in-depth study task that involves finding the area of a {shape}.\n\n"
        # Call the openai.Completion method with the prompt and other parameters
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1024,
            temperature=0.5,
            stop=None
        )
        # Return the generated text as the task
        return response["choices"][0].text

    def write_to_file(self, shapes: List[str]):
        # Create a set of questions from the shapes
        questions = {question.strip() for shape in shapes for question in
                     self.create_geometry_prompts(shape).split('\n')}
        # Create a file name with the current date
        file_name = f"prompts_{datetime.date.today().strftime('%Y-%m-%d')}.txt"
        # Open the file in write mode with UTF-8 encoding
        with open(file_name, "w", encoding='utf-8') as f:
            # Write each question with a prompt and a separator
            for q in questions:
                question = f"Prompt: '{q}'"
                f.write(f"\n{question}\n{'-' * 50}\n")
        # Print a message to confirm that the file has been created
        print(f"File {file_name} has been created with {len(questions)} questions.")

    def create_geometry_task(self):
        # Create a geometry task using the openai.ChatCompletion method
        # Define the file name for the prompts
        file_name = f"prompts_{datetime.date.today().strftime('%Y-%m-%d')}.txt"
        # Open the file and read the lines
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # Filter the lines that contain the word 'triangle'
        lines = [line for line in lines]
        # Choose a random line as the prompt
        # prompt = random.choice(lines).split('Prompt:')[1]
        # Call the openai.ChatCompletion method with the prompt and other parameters
        # Create a file name with the current date
        file_name = f"tasks_{datetime.date.today().strftime('%Y-%m-%d')}.txt"
        # Open the file in write mode with UTF-8 encoding
        with open(file_name, "w", encoding='utf-8') as f:
            # Write each question with a prompt and a separator
            for q in lines:
                if 'Prompt:' in q:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "user", "content": q.split('Prompt:')[1]}
                        ]
                    )
                    f.write(f"\n{response.choices[0].message.content}\n{'-' * 50}\n")
        # Print a message to confirm that the file has been created
        print(f"File {file_name} has been created")
        # Return the generated message as the task
        # return response.choices[0].message.content

