import os
import requests
import vcr
from .retryer import retryer

TMDB_API_KEY = os.environ.get('TMDB_API_KEY', None)


class APIKeyMissingError(Exception):
    pass


if TMDB_API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "https://developers.themoviedb.org/3/getting-started/introduction "
        "for how to retrieve an authentication token from "
        "The Movie Database"
    )

session = requests.Session()
session.params = {'api_key': TMDB_API_KEY}

my_vcr = vcr.VCR(
    record_mode='all',
    decode_compressed_response=True
)


@retryer
def handle_request(url, method, data=None):
    if method.lower() == 'get':
        return session.get(url).json()
    elif method.lower == 'post':
        return session.post(url, data).json()
    else:
        raise ValueError('Unknown method: {}'.format(method))


from .tv import TV
