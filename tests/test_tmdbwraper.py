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
def movie_keys():
    return ['popularity', 'vote_count', 'video', 'poster_path', 'id', 'adult', 'backdrop_path', 'original_language',
            'original_title', 'genre_ids', 'title', 'vote_average', 'overview', 'release_date']

@fixture
def movie_id():
    return 1396


@fixture
def movie_name():
    return "Forrest Gump"

tmdb_client = None
if tmdb_client is None:
    tmdb_client = TBDBclient()


@my_vcr.use_cassette('tests/vcr_cassettes/tv-info.yml', filter_query_parameters=['api_key'])
def test_tv_info(tv_keys, movie_id):
    """Tests an API call to get a TV show's info"""

    response = tmdb_client.info(id=movie_id)

    assert isinstance(response, dict)
    assert response['id'] == movie_id
    assert set(tv_keys).issubset(response.keys())


@my_vcr.use_cassette('tests/vcr_cassettes/tv-popular.yml', filter_query_parameters=['api_key'])
def test_tv_popular(tv_keys):
    """Tests an API call to get a popular tv shows"""

    response = tmdb_client.popular()

    assert isinstance(response, dict)
    assert isinstance(response['results'], list)
    assert isinstance(response['results'][0], dict)
    assert set(tv_keys).issubset(response['results'][0].keys())


@my_vcr.use_cassette('tests/vcr_cassettes/movie_search.yml', filter_query_parameters=['api_key'])
def test_movie_search(movie_name, movie_keys):
    response =  tmdb_client.search_movie(movie_name)
    assert isinstance(response, dict)
    assert isinstance(response['results'], list)
    assert isinstance(response['results'][0], dict)
    assert set(movie_keys).issubset(response['results'][0].keys())
