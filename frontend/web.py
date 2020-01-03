from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class WebDriver:
    driver = None

    @classmethod
    def get_web_driver(cls, browser='chrome'):
        if cls.driver is None:
            if browser.lower() == 'chrome':
                # TODO: handle proper driver names
                cls.driver = webdriver.Chrome('chromedriver')
        return cls.driver
