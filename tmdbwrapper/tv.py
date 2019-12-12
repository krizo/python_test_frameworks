from . import session, handle_request


class TV(object):
    def __init__(self, id):
        self.id = id

    def info(self):
        url = 'https://api.themoviedb.org/3/tv/{}'.format(self.id)
        return handle_request(url=url, method='get')
