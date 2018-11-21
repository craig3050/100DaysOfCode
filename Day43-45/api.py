from typing import List
import requests
import collections

headers = collections.namedtuple('headers', 'category, id, url, title, description')


def search_talk_python(keyword: str) -> List[headers]:
    url = f'http://search.talkpython.fm/api/search?q={keyword}'

    response = requests.get(url)
    response.raise_for_status()

    results = response.json()

    long_list = []
    for r in results.get('results'):
        long_list.append(headers(**r))

    return long_list
