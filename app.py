from flask import Flask
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'

load_dotenv(verbose=True, dotenv_path=env_path)

print('boop')
print('boop', os.environ['APP_SETTINGS'])

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
