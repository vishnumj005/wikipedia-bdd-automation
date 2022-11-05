from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver


class Driver(object):
    instance = None

    def __init__(self, context):
        self.browser = context.browser
        self.mode = context.mode

    def get_driver(self):
        web_driver = getattr(self, self.browser)
        return web_driver()

    def chrome(self):
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        desired_capabilities = DesiredCapabilities.CHROME
        options = self.set_chrome_browser_options_arguments(self)
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options,
                                   desired_capabilities=desired_capabilities)
        browser.maximize_window()
        return browser

    @staticmethod
    def firefox():
        from selenium.webdriver.firefox.service import Service
        from webdriver_manager.firefox import GeckoDriverManager

        profile = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(profile, service=Service(GeckoDriverManager().install()))
        return browser

    @staticmethod
    def edge():
        pass
        #TODO

    @staticmethod
    def safari():
        pass
        #TODO

    @staticmethod
    def set_chrome_browser_options_arguments(self):
        options = webdriver.ChromeOptions()
        if self.mode == 'headless':
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
        options.add_argument('--window-size=1366,768')
        options.add_argument('--ignore-certificate-errors')
        return options

