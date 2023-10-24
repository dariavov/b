from urllib.parse import urlparse
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

base_url = "https://b2c.passport.rt.ru"

class BasePage:
    """Stores basic functions available for use in the tests"""
    def __init__(self, driver, timeout):
        self.driver = driver
        self.base_url = "https://b2c.passport.rt.ru"
        self.timeout = timeout

    def open_website(self):
        """Opens the page for testing from the base_url"""
        self.driver.get(self.base_url)

    def locate_element(self, locator):
        """Finds an element based on its locator"""
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        """Clicks on any given element described by a unique locator"""
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.element_to_be_clickable(*locator)).click()

    def get_color(self, locator):
        """Gets color of any given element"""
        color = self.locate_element(*locator).value_of_css_property("color")
        return color

    def hover_over(self, locator):
        """Hovers over any given element"""
        action = ActionChains(self.driver)
        action.move_to_element(self.locate_element(*locator)).perform()

    def get_placeholder(self, locator):
        """Returns the placeholder of any given element"""
        element = self.locate_element(*locator)
        return element.text

    def get_class_name(self, locator):
        """Returns the class name of any given element"""
        element = self.locate_element(*locator)
        return element.get_attribute('class')

    def get_element_text(self, locator):
        """Gets element's text"""
        element = self.locate_element(locator)
        return element.text

    def get_current_url_hostname(self):
        """Returns the current url's hostname"""
        url = urlparse(self.driver.current_url)
        return url.hostname

    def get_current_url_path(self):
        """Returns the current url's path"""
        url = urlparse(self.driver.current_url)
        return url.path

    def wait_for_url_change(self):
        """Waits for the url to change"""
        current_url = self.get_current_url_hostname()
        return WebDriverWait(self.driver, self.timeout).until(EC.url_changes(current_url))
