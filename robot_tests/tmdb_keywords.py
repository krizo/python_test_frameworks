from tbdbclient import TBDBclient

tmdb_client = None
if tmdb_client is None:
    tmdb_client = TBDBclient()


def get_movie_info(id):
    return tmdb_client.info(id)


def get_popular_movies():
    return tmdb_client.popular()

