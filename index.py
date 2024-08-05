import os
from datetime import datetime

def run():
    name = os.environ['INPUT_NAME']
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f'Hello, {name}! The current time is {time}.')