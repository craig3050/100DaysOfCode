import uplink
import requests


class MovieSearch(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm')

    @uplink.get('/api/search/{keyword}')
    def search_by_keyword(self, keyword) -> requests.models.Response:
        """Gets all posts"""

# '''
#     Search
#     movies
#     GET/api/search/{keyword}
#
#     Movies
#     by
#     director
#     GET/api/director/{director_name}
#
#     Movie
#     by
#     IMDB
#     code
#     GET/api/movie/{imdb_number}'''
