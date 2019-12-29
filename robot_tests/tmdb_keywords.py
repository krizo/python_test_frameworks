from tmdbwrapper import TV


def get_movie_info(id):
    tv_instance = TV(id)
    return tv_instance.info()


def get_popular_movies():
    return TV.popular()

