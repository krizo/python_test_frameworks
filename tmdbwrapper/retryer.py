import requests
import time


class NetworkError(RuntimeError):
    pass


def retryer(func):
    retry_on_exceptions = (
        requests.exceptions.Timeout,
        requests.exceptions.ConnectionError,
        requests.exceptions.HTTPError
    )

    max_retries = 2
    timeout = 1

    def inner(*args, **kwargs):
        for i in range(max_retries):
            try:
                result = func(*args, **kwargs)
            except retry_on_exceptions as e:
                time.sleep(timeout)
                print("Retry request: {}".format(args))
                print("Exception: {}".format(e))
                continue
            else:
                return result
        else:
            raise NetworkError
    return inner
