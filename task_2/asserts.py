from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Asserts:
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def should_be_form(self, selector):
        assert self.is_element_present(selector), f'WebElement not found {selector}'

    def should_be_open_url(self, url):
        assert url in self.browser.current_url, 'Link is not current url'

    def should_be_login_url(self, url):
        assert url == self.browser.current_url, 'Not go back to main page'

    def should_be_element_to_be_clickable(self, selector):
        assert self.is_element_to_be_clickable(selector), f'Sample selector {selector} not clickable'

    def should_be_text(self, selector, text):
        assert self.is_text_to_be_present_in_element(selector, text), f'Text {text} not found in WebElement {selector}'

    def is_element_present(self, selector):
        try:
            self.browser.find_element(*selector)
        except NoSuchElementException:
            return False
        return True

    def is_text_to_be_present_in_element(self, selector, text, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.text_to_be_present_in_element(selector, text))
        except TimeoutException:
            return False
        return True

    def is_presence_of_element_located(self, selector, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(selector))
        except TimeoutException:
            return False
        return True

    def is_element_to_be_clickable(self, selector, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable(selector))
        except TimeoutException:
            return False
        return True
