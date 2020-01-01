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
                cls.driver = webdriver.Chrome('chromedriver')

        return cls.driver


class Web:
    driver = None

    def __init__(self, browser, wait_timeout=10):
        self.driver = WebDriver.get_web_driver(browser)
        self.wait = WebDriverWait(self.driver, wait_timeout)

    def get_element_by_css(self, css):
        return self.wait.until(EC.presence_of_element_located(By.CSS_SELECTOR, css))

    def get_elements_by_css(self, css):
        return self.wait.until(EC.presence_of_all_elements_located(By.CSS_SELECTOR, css))

    def open(self, path):
        self.driver.get(path)

    def close_all(self):
        self.driver.quit()



