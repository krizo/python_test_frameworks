import os
import requests
from retryer import retryer


class APIKeyMissingError(Exception):
    pass


class TBDBclient(object):
    def __init__(self):
        self.api_key = os.environ.get('TMDB_API_KEY', None)

        if self.api_key is None:
            raise APIKeyMissingError(
                "All methods require an API key. See "
                "https://developers.themoviedb.org/3/getting-started/introduction "
                "for how to retrieve an authentication token from "
                "The Movie Database")

        self.session = requests.Session()
        self.session.params = {'api_key': self.api_key}

    @retryer
    def handle_request(self, url, method, data=None, params=None):
        if method.lower() == 'get':
            return self.session.get(url, params=params).json()
        elif method.lower == 'post':
            return self.session.post(url, data).json()
        else:
            raise ValueError('Unknown method: {}'.format(method))

    def info(self, id):
        url = 'https://api.themoviedb.org/3/tv/{}'.format(id)
        return self.handle_request(url=url, method='get')

    def popular(self):
        url = 'https://api.themoviedb.org/3/tv/popular'
        return self.handle_request(url=url, method='get')

    def search_movie(self, movie_name):
        url = 'https://api.themoviedb.org/3/search/movie'
        return self.handle_request(url=url, method='get', params={"query": movie_name})