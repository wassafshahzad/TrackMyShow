import requests 
from util.constants import BOOK_MARK,CLASS,TEST_STRING
from bs4 import BeautifulSoup

def get_latest_episode(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    episode = soup.findAll('a',rel = BOOK_MARK,class_=CLASS)[0]
    return parser(episode)


def parser(link):
    list_p = link['href'].split("-")
    episode_number  = int(list_p[list_p.index("episode") + 1])
    return episode_number # can be in one line but for readability divided it into two lines
