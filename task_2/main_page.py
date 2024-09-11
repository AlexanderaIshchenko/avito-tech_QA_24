from locators import MainPageSelectors

from asserts import Asserts


class MainPage:
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, url):
        self.browser.get(url)
        Asserts(self.browser).should_be_open_url(url)

    def button_click(self, selector):
        Asserts(self.browser).should_be_element_to_be_clickable(selector)
        self.find(selector).click()

    def find(self, selector):
        Asserts(self.browser).should_be_form(selector)
        return self.browser.find_element(*selector)

    def choosing_category(self, category):
        selector = ('xpath', f'//div[contains(@class, "ant-select-item") and text()="{category}"]')
        self.button_click(selector)

    def comparison_game(self, method):
        first_game_first_list = self.browser.find_element(*MainPageSelectors.GAME_CARD_TITLES).text
        self.button_click(method)
        first_game_second_list = self.browser.find_element(*MainPageSelectors.GAME_CARD_TITLES).text
        assert first_game_first_list != first_game_second_list, "Didn't go to the second page"
