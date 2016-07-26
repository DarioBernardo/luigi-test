import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
WEBSERVER_KEY = os.path.join(BASE_DIR, 'data', 'webserver_key', 'key.txt')
DATA_FOLDER = os.path.join(BASE_DIR, 'data')