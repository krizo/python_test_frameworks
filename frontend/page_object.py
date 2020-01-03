import traceback
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By

# Map PageElement constructor arguments to webdriver locator enums
from selenium.webdriver.support.wait import WebDriverWait

from frontend.web import WebDriver

_LOCATOR_MAP = {'css': By.CSS_SELECTOR,
                'id_': By.ID,
                'name': By.NAME,
                'xpath': By.XPATH,
                'link_text': By.LINK_TEXT,
                'partial_link_text': By.PARTIAL_LINK_TEXT,
                'tag_name': By.TAG_NAME,
                'class': By.CLASS_NAME,
                }


class PageObject(object):
    root_uri = None

    """Page Object pattern.

    :param root_uri: `str`
        Root URI to base any calls to the ``PageObject.get`` method. If not defined
        in the constructor it will try and look it from the webdriver object.
    """

    def __init__(self, browser='Chrome', timeout=10, maximaze_window=False):
        self.driver = WebDriver.get_web_driver(browser)
        if maximaze_window:
            self.driver.maximize_window()
        self.timeout = timeout

    def open(self):
        """
        :param root_uri:  URI to GET, based off of the root_uri sattribute.
        """
        self.driver.get(self.root_uri)

    def close_all(self):
        self.driver.quit()

    def element(self, selector):
        locator = _parse_locators(selector)
        self.wait_until_present(locator)
        return self.driver.find_element(*locator)

    def elements(self, selector):
        locator = _parse_locators(selector)
        self.wait_until_present(locator)
        return self.driver.find_elements(*locator)

    def wait_until_present(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(_parse_locators(locator))
            )
        except(TimeoutException, StaleElementReferenceException):
            print("Element not found: {}".format(locator))
            traceback.print_exc()
        return True


def _parse_locators(locator):
    if isinstance(locator, dict):
        k, v = next(iter(locator.items()))
        return _LOCATOR_MAP[k], v
    else:
        return locator


class Section(object):
    pass


class Element(object):
    """Page Element descriptor.

    :param css:    `str`
        Use this css locator
    :param id_:    `str`
        Use this element ID locator
    :param name:    `str`
        Use this element name locator
    :param xpath:    `str`
        Use this xpath locator
    :param link_text:    `str`
        Use this link text locator
    :param partial_link_text:    `str`
        Use this partial link text locator
    :param tag_name:    `str`
        Use this tag name locator
    :param class_name:    `str`
        Use this class locator

    :param context: `bool`
        This element is expected to be called with context

    Page Elements are used to access elements on a page. The are constructed
    using this factory method to specify the locator for the element.

        >>> from page_objects import PageObject, PageElement
        >>> class MyPage(PageObject):
                elem1 = PageElement(css='div.myclass')
                elem2 = PageElement(id_='foo')
                elem_with_context = PageElement(name='bar', context=True)

    Page Elements act as property descriptors for their Page Object, you can get
    and set them as normal attributes.
    """

    def __init__(self, context=False, **kwargs):
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        k, v = next(iter(kwargs.items()))
        self.locator = (_LOCATOR_MAP[k], v)
        self.has_context = bool(context)

    def find(self, context):
        try:
            return context.find_element(*self.locator)
        except NoSuchElementException:
            return None

    def __get__(self, instance, owner, context=None):
        if not instance:
            return None

        if not context and self.has_context:
            return lambda ctx: self.__get__(instance, owner, context=ctx)

        if not context:
            context = instance.w

        return self.find(context)

    def __set__(self, instance, value):
        if self.has_context:
            raise ValueError("Sorry, the set descriptor doesn't support elements with context.")
        elem = self.__get__(instance, instance.__class__)
        if not elem:
            raise ValueError("Can't set value, element not found")
        elem.send_keys(value)


class Elements(Element):
    """ Like `PageElement` but returns multiple results.

        >>> from page_objects import PageObject, MultiPageElement
        >>> class MyPage(PageObject):
                all_table_rows = MultiPageElement(tag='tr')
                elem2 = PageElement(id_='foo')
                elem_with_context = PageElement(tag='tr', context=True)
    """

    def find(self, context):
        try:
            return context.find_elements(*self.locator)
        except NoSuchElementException:
            return []

    def __set__(self, instance, value):
        if self.has_context:
            raise ValueError("Sorry, the set descriptor doesn't support elements with context.")
        elems = self.__get__(instance, instance.__class__)
        if not elems:
            raise ValueError("Can't set value, no elements found")
        [elem.send_keys(value) for elem in elems]
