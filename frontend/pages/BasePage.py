from frontend.web import Web


class BasePage():
    url = None

    def __init__(self, browser):
        self.driver = Web(browser)

    def open(self):
        self.driver.open(self.url)

    def close_all(self):
        self.driver.close_all()
