import os
import urllib
import bs4
import re
import time


CURRENT_PLAYERS = "http://www.basketball-reference.com/leagues/NBA_2017_per_game.html"
BASE_URL = "http://www.basketball-reference.com"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PLAYER_DIR = BASE_DIR+"/html/players/"

def get_current_player_urls(url=CURRENT_PLAYERS):
    html = urllib.urlopen(url)
    soup = bs4.BeautifulSoup(html, "lxml")
    player_links = set(soup.findAll("a", href=re.compile("/players/\S/")))
    return player_links

def fetch_player(url):
    url = BASE_URL+url
    file_name = PLAYER_DIR+url.split('/')[-1]
    f = urllib.URLopener()
    f.retrieve(url, file_name)

def fetch_player_data(links):
    print len(links)
    for l in links:
        try:
            time.sleep(1)
            href = l['href']
            print href
            fetch_player(href)
        except ValueError:
            print "missing href for %s" % l
        except Exception as e:
            print e




if __name__ == "__main__":
    links = get_current_player_urls()
    fetch_player_data(links)
