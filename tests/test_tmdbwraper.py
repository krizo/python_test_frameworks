from pytest import fixture
from tbdbclient import TBDBclient
from tmdbwrapper import my_vcr


@fixture
def tv_keys():
    # Responsible only for returning the test data
    return ['id', 'origin_country', 'poster_path', 'name',
            'overview', 'popularity', 'backdrop_path',
            'first_air_date', 'vote_count', 'vote_average']


@fixture
def movie_id():
    return 1396


@my_vcr.use_cassette('tests/vcr_cassettes/tv-info.yml', filter_query_parameters=['api_key'])
def test_tv_info(tv_keys, movie_id):
    """Tests an API call to get a TV show's info"""

    tmdb_client = TBDBclient()
    response = tmdb_client.info(id=movie_id)

    assert isinstance(response, dict)
    assert response['id'] == movie_id
    assert set(tv_keys).issubset(response.keys())


@my_vcr.use_cassette('tests/vcr_cassettes/tv-popular.yml', filter_query_parameters=['api_key'])
def test_tv_popular(tv_keys):
    """Tests an API call to get a popular tv shows"""

    tmdb_client = TBDBclient()
    response = tmdb_client.popular()

    assert isinstance(response, dict)
    assert isinstance(response['results'], list)
    assert isinstance(response['results'][0], dict)
    assert set(tv_keys).issubset(response['results'][0].keys())
