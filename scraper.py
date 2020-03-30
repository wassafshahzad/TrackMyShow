import requests 
from util.constants import BOOK_MARK,CLASS,TEST_STRING
from bs4 import BeautifulSoup

def get_latest_episode(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    episode = soup.findAll('a',rel = BOOK_MARK,class_=CLASS)[0]
    print(episode)


def parser(link):
    episode_number = link['href'].split(-)