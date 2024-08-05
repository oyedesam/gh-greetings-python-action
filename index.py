import os
from datetime import datetime

def run():
    name = os.environ.get['INPUT_NAME']
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"echo name={name}")
    print(f"echo time={time}")
    
    with open(os.environ['GITHUB_ENV'], 'a') as env_file:
        env_file.write(f"NAME={name}\n")
        env_file.write(f"TIME={time}\n")