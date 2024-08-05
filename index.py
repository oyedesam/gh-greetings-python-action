import os
from datetime import datetime

def run():
    name = os.environ.get('INPUT_NAME')
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # print(f"echo name={name}")
    # print(f"echo time={time}")
    
    # Set the outputs
    with open(os.environ['GITHUB_OUTPUT'], 'a') as output_file:
        output_file.write(f"name={name}\n")
        output_file.write(f"time={time}\n")

run()