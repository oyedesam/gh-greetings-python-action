import os
from datetime import datetime

def run():
    name = os.environ.get['INPUT_NAME']
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"::set-output name={name}")
    print(f"::set-output time={time}")