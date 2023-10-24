from pages.base_page import BasePage
from locators.auth_page_locators import *
from settings.keys import *

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AuthorizationPage(BasePage):
    """Stores authorization-related functions and elements 
    available for use in the tests"""
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru'
        driver.get(url)
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(AuthorizationPageLocators.phone_tab))

    def send_credentials(self, tab_locator, username_value, password_value):
        """Sends given credentials to both username and password fields depending on the username tab selected"""
        self.click_on_element(tab_locator)
        username_locator = AuthorizationPageLocators.username_field
        password_locator = AuthorizationPageLocators.password_field
        username = self.locate_element(username_locator)
        username.send_keys(username_value)
        password = self.locate_element(password_locator)
        password.send_keys(password_value)

    def send_keys_to_username(self, user_input):
        """Sends keys to the username field"""
        if user_input == 'random telephone':
            value = UsernameKeys.random_telephone
        elif user_input == 'random email':
            value = UsernameKeys.random_email
        elif user_input == 'random ls':
            value = UsernameKeys.random_ls
        elif user_input == 'random login':
            value = UsernameKeys.random_login
        elif user_input == 'valid email':
            value = UsernameKeys.valid_email
        elif user_input == 'valid login':
            value = UsernameKeys.valid_login
        wait = WebDriverWait(self.driver, self.timeout)
        element = wait.until(EC.element_to_be_clickable(AuthorizationPageLocators.username_field))
        element.send_keys(value)

    def send_keys_to_password(self, password_locator, password_value):
        """Sends keys to the password field"""
        password = self.locate_element(password_locator)
        password.send_keys(password_value)


class UserPage(BasePage):
    """Stores functions and elements of the page to which a user is redirected after successfully signing in"""
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(UserPageLocators.username))
        self.username = driver.find_element(*UserPageLocators.username)

    def get_element_title(self, locator):
        """Gets title's text of an element"""
        element = self.locate_element(locator)
        return element.text