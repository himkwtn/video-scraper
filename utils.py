from bs4 import BeautifulSoup


def parse(text):
    return BeautifulSoup(text, "html.parser")


def go_to_link(session, link):
    result = session.get(link)
    page = parse(result.text)
    return page
