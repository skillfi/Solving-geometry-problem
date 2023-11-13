import os

config = dict(
    api_key=os.getenv('OPEN_API_KEY'),
    hugging_key=os.getenv('HUGGING_API_KEY'),
    api=os.getenv('API'),
    host=os.getenv('host')
)
app = dict(config=config)
