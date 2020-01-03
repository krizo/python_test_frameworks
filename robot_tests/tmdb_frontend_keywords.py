from frontend.pages.MainPage import MainPage

main_page = MainPage()


def go_to_discover():
    return main_page.elements({'class': 'logo'})[0].click()
