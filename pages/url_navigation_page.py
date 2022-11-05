from pages.base.base_page import BasePage


class UrlNavigationPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def visit_url(self, url):
        self.visit(url)
