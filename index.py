import os
from datetime import datetime

def run():
    name = os.environ.get('INPUT_NAME')
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"echo name={name}")
    print(f"echo time={time}")
    
    print(f"::set-output name=name::{name}")
    print(f"::set-output name=time::{time}")

    # Set the output variable
    # with open(os.environ['GITHUB_ENV'], 'a') as env_file:
    #     env_file.write(f"NAME={name}\n")
    #     env_file.write(f"TIME={time}\n")

run()