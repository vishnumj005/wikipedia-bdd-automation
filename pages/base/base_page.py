import time

from selenium.common.exceptions import TimeoutException, \
    StaleElementReferenceException, UnexpectedAlertPresentException, JavascriptException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import config.base_config as config


class BasePage(object):

    def __init__(self, context):
        self.browser = context.driver
        self.timeout = config.default_wait

    def visit(self, url):
        self.browser.get(url)
        print("Visiting url: {}".format(url))
        return self

    def find_element(self, locator, visibility=True, timeout=config.default_wait):
        try:
            if visibility:
                return WebDriverWait(self.browser, timeout=timeout).until(ec.visibility_of_element_located(locator),
                                                                          'ELEMENT IS NOT FOUND OR VISIBLE! => {}'.format(
                                                                              locator))
            else:
                return WebDriverWait(self.browser, timeout=timeout).until(ec.presence_of_element_located(locator),
                                                                          'ELEMENT IS NOT FOUND! => {}'.format(locator))
        except TimeoutException as e:
            error = e.args[0]
            raise TimeoutException(error) from e.__cause__
        except StaleElementReferenceException as e:
            error = e.args[0]
            raise StaleElementReferenceException(error) from e.__cause__

    def click_element(self, locator, timeout=None):
        if timeout is None:
            timeout = config.short_wait
        try:
            self.browser.execute_script("arguments[0].click();", WebDriverWait(self.browser, timeout=timeout).until(
                ec.element_to_be_clickable(locator), 'ELEMENT NOT CLICKABLE! => {}'.format(locator)))
        except TimeoutException:
            try:
                WebDriverWait(self.browser, timeout=timeout).until(ec.element_to_be_clickable(locator),
                                                                   'UNABLE TO LOCATE ELEMENT! => {}'.format(
                                                                       locator)).click()
            except TimeoutException as e:
                error = e.args[0]
                raise TimeoutException(error) from e.__cause__
            except UnexpectedAlertPresentException as e:
                error = e.args[0]
                raise UnexpectedAlertPresentException(error) from e.__cause__
        except StaleElementReferenceException as e:
            error = e.args[0]
            raise StaleElementReferenceException(error) from e.__cause__
        except JavascriptException as e:
            error = e.args[0]
            raise JavascriptException(error) from e.__cause__
        except UnexpectedAlertPresentException as e:
            error = e.args[0]
            raise UnexpectedAlertPresentException(error) from e.__cause__
        return self

    def fill_input(self, locator, value, timeout=config.default_wait):
        element = self.find_element(locator, timeout=timeout)
        self.scroll_into_view_by_locator(element)
        try:
            element.send_keys(value)
        except StaleElementReferenceException as e:
            print(f"Failed to fill {value} input on {locator} with {e}")
            time.sleep(1)
            try:
                element.send_keys(value)
            except TimeoutException as e:
                error = e.args[0]
                raise TimeoutException(f"Failed to fill {value} input on {locator} with {error}") from e.__cause__
            except StaleElementReferenceException as e:
                error = e.args[0]
                raise StaleElementReferenceException(
                    f"Failed to fill {value} input on {locator} with {error}") from e.__cause__
        return self

    def verify_element_displayed(self, locator, timeout=config.default_wait, message=""):
        try:
            WebDriverWait(self.browser, timeout=timeout).until(
                ec.visibility_of_element_located(locator),
                f'ELEMENT EXPECTED TO BE VISIBLE IS NOT DISPLAYED! => {locator}\n{message}',
            )
        except TimeoutException as e:
            error = e.args[0]
            raise TimeoutException(error) from e.__cause__
        except UnexpectedAlertPresentException as e:
            error = e.args[0]
            raise UnexpectedAlertPresentException(error) from e.__cause__
        return self

    def scroll_into_view_by_locator(self, locator):
        try:
            self.browser.execute_script("arguments[0].scrollIntoView();", locator)
        except JavascriptException as e:
            error = e.args[0]
            raise JavascriptException(error) from e.__cause__
        return self

