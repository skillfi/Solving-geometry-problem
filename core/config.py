import os


def str_to_bool(key: str):
    if key in ('True',):
        return True
    else:
        return False


config = dict(
    api_key=os.getenv('OPENAI_API_KEY'),
    hugging_key=os.getenv('HUGGING_API_KEY'),
    api=str_to_bool(os.getenv('API')),
    host=os.getenv('host')
)
app = dict(config=config)
