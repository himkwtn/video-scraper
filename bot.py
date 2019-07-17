import requests
from functools import partial
from login import login
from courses import courses
from videos import videos
from dotenv import load_dotenv
from os import environ
load_dotenv()

session = requests.session()
username = environ.get('USERNAME')
password = environ.get('PASSWORD')

login_page = login(session, username, password)
get_videos = partial(videos, session)
courses(session, login_page, get_videos)
