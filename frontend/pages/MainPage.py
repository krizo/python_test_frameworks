from frontend.page_object import PageObject
# from frontend.pages.BasePage import BasePage


class MainPage(PageObject):
    root_uri = 'https://www.themoviedb.org/'
    # discover = element(tag_name='href')

    def test(self):
        return self.driver.get_element_by_css('.logo')



# class TopMenu(MainPage):



