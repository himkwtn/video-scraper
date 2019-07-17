from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from itertools import chain
from functools import partial
from utils import parse
from os import makedirs, environ, path


def go_to_download(session, link):
    result = session.get(link)
    page = parse(result.text)
    get_download_links(session, page)


def get_videos_links(course):
    video_tags = course.find_all("a", class_="item")

    base = "https://chinesezerotohero.teachable.com/"
    video_links = [base + tag["href"] for tag in video_tags]
    return video_links


def get_download_links(session, page):
    tag = page.find("a", class_="download")
    sideBar = page.find("div", id="courseSidebar")
    title = sideBar.find("h2").string
    title = title.replace(" ", "")
    link = tag["href"] if tag else False
    if link:
        download(session, link, title)
    return link


def videos(session, courses):
    print("finding videos")
    links = [get_videos_links(course) for course in courses]
    links = list(chain.from_iterable(links))
    get_videos = partial(go_to_download, session)
    with PoolExecutor(max_workers=32) as executor:
        executor.map(get_videos, links)


def download(session, link, title):
    print("Downloding from "+link)
    base = environ.get("DOWNLOAD_PATH", "./videos")
    folder = path.join(base, title)
    makedirs(folder, exist_ok=True)
    result = session.get(link)
    name = result.headers["X-File-Name"]
    print("download " + name)
    with open(path.join(folder, name), 'wb') as f:
        f.write(result.content)
