import os
from dotenv import load_dotenv


# Load environment variables and grab client id and secret key
load_dotenv()
CLIENT_ID = os.environ['CLIENT_ID']
SECRET_KEY = os.environ['SECRET_KEY']
