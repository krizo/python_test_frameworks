from tbdbclient import TBDBclient

tmdb_client = None
if tmdb_client is None:
    tmdb_client = TBDBclient()


def get_tv_show_info(id):
    return tmdb_client.info(id)


def get_popular_shows():
    return tmdb_client.popular()


def search_movie(name):
    return tmdb_client.search_movie(name)
