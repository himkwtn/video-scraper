from bs4 import BeautifulSoup
from utils import parse, go_to_link


def getToken(session):
    login_url = "https://sso.teachable.com/secure/133035/users/sign_in?clean_login=true&reset_purchase_session=1"
    page = go_to_link(session, login_url)
    token = page.find(attrs={"name": "authenticity_token"})["value"]
    return token


def login(session, username, password):
    print("logging in")
    login_url = "https://sso.teachable.com/secure/133035/users/sign_in?clean_login=true&reset_purchase_session=1"
    token = getToken(session)
    payload = {
        "user[email]": username,
        "user[password]": password,
        "authenticity_token": token
    }
    result = session.post(login_url, data=payload,
                          headers={"referer": login_url})
    page = parse(result.text)
    return page
