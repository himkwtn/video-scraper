import datetime
from utils import parse, go_to_link
from functools import partial
from concurrent.futures import ThreadPoolExecutor as PoolExecutor


def courses(session, page, callback):
    print("finding courses")
    links = page.find_all(attrs={"data-role": "course-box-link"})
    base = "https://chinesezerotohero.teachable.com/"
    links = [base+link['href'] for link in links][1:]
    get_courses = partial(go_to_link, session)
    with PoolExecutor(max_workers=8) as executor:
        result = executor.map(get_courses, links)
        result = [i for i in result]
        callback(result)
