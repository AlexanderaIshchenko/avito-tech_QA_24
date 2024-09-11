class MainPageSelectors:
    CATEGORY_DROPDOWN = ('xpath', '(//span[@class="ant-select-selection-item"])[2]')

    GAME_CARD_FIRST = ('xpath', '(//div[@class="ant-card-body"])[1]')
    BUTTON_BACK_TO_MAIN = ('xpath', '//button[@type="button"]')

    BUTTON_LIST_3 = ('xpath', '//li[@title=3]')
    BUTTON_NEXT_PAGE = ('xpath', '//ul[@class="ant-pagination css-17a39f8"] //li[9]')
    GAME_CARD_TITLES = ('xpath', '//div[@class="_container_vlg32_23"]/div[1]/h1')
    GAME_CARD_CATEGORY = ('xpath', '(//span[@class = "ant-descriptions-item-content"])[5]')
