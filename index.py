import os
from datetime import datetime

def run():
    name = os.environ.get['INPUT_NAME']
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"echo name={name}")
    print(f"echo time={time}")