# settings.py
import dotenv
from dotenv import load_dotenv, find_dotenv
import os 
SECRET_KEY = os.getenv("TEST")
DATABASE_PASSWORD = os.getenv("PASSWORD")


load_dotenv(find_dotenv())

load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path 
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)