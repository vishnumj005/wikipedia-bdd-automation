from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, context):
        self.context = context
        BasePage.__init__(self, context)

    SEARCH_INPUT = (By.XPATH, "//input[@title='Search Wikipedia']")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(span/text(), 'Search')]")
    SEARCH_RESULT = (By.XPATH, "//p[contains(.,'There is a page named')]")
    ARTICLE_TAB = (By.XPATH, "//a/span[text()='Article']")
    WIKIPEDIA_LABEL = (By.XPATH, "//div[text()='From Wikipedia, the free encyclopedia']")

    def search_with_keyword(self, keyword):
        self.fill_input(self.SEARCH_INPUT, keyword)\
            .click_element(self.SEARCH_BUTTON)

    def verify_search_result(self):
        self.verify_element_displayed(self.SEARCH_RESULT)

    def click_search_result(self):
        self.click_element((By.XPATH, f"//a/span[text()='{self.context.keyword}']"))

    def verify_wikipedia_page(self):
        self.verify_element_displayed(self.ARTICLE_TAB)
        self.verify_element_displayed(self.WIKIPEDIA_LABEL)