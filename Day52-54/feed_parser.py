#!python3

import feedparser
import requests

def parse_the_feed():
    FEED_FILE = "newreleases.xml"

    feed = feedparser.parse(FEED_FILE)

    if 'title' in feed.entries[0]:
        for entry in feed.entries:
            print(f'{entry.published} - {entry.title} - {entry.description}')


def get_the_feed():
    URL = 'https://hackaday.com/blog/feed/'
    r = requests.get(URL)
    with open('newreleases.xml', 'wb') as f:
        f.write(r.content)



if __name__ == '__main__':
    get_the_feed()
    parse_the_feed()

