import sys
from gunicorn.app.wsgiapp import run
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == '__main__':
    sys.argv = "gunicorn --bind 0.0.0.0:5151 app:app".split()
    sys.exit(run())
