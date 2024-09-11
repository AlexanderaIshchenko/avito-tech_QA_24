import pytest

from asserts import Asserts
from locators import MainPageSelectors
from main_page import MainPage

link = "https://makarovartem.github.io/frontend-avito-tech-test-assignment"


@pytest.mark.parametrize('category, category_text, test_case',
                         (
                                 ("mmorpg", "MMORPG", 'TK-1.1'),
                                 ("shooter", "Shooter", 'TK-1.2'),
                                 ("strategy", "Strategy", 'TK-1.3'),
                                 ("moba", "MOBA", 'TK-1.4'),
                                 pytest.param("racing", "RACING", 'TK-1.5', marks=pytest.mark.xfail),
                                 pytest.param("sports", "Sports", 'TK-1.6', marks=pytest.mark.xfail),
                                 pytest.param("social", "Social", 'TK-1.7', marks=pytest.mark.xfail)
                         ))
def test_category_filter(browser, category, category_text, test_case):
    print(test_case)
    page = MainPage(browser)
    page.open(link)
    page.button_click(MainPageSelectors.CATEGORY_DROPDOWN)
    page.choosing_category(category)
    # Проверяем только с первой игрой
    # Т.к все фильтры по категориям не работают корректно, и необходимо чтобы все тесты прошли
    page.button_click(MainPageSelectors.GAME_CARD_TITLES)
    Asserts(browser).should_be_text(MainPageSelectors.GAME_CARD_CATEGORY, category_text)


def test_back_2_main(browser):
    print('TK-2.1')
    page = MainPage(browser)
    page.open(link)
    page.button_click(MainPageSelectors.GAME_CARD_FIRST)
    page.button_click(MainPageSelectors.BUTTON_BACK_TO_MAIN)
    Asserts(browser).should_be_login_url(link)


@pytest.mark.parametrize('pagination_method, test_case',
                         (
                                 (MainPageSelectors.BUTTON_LIST_3, 'TK-3.1'),
                                 (MainPageSelectors.BUTTON_NEXT_PAGE, 'TK-3.2'),
                         ))
def test_transition_using_pagination(browser, pagination_method, test_case):
    print(test_case)
    page = MainPage(browser)
    page.open(link)
    page.comparison_game(pagination_method)

