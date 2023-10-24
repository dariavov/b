from pages.base_page import BasePage
from locators.password_recovery_page_locators import *
from locators.auth_page_locators import *
from settings.keys import *

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class PasswordRecoveryPage(BasePage):
    """Stores password recovery-related functions and elements
    available for use in the tests"""
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru'
        driver.get(url)
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.presence_of_element_located(AuthorizationPageLocators.forgot_password_button)).click()
        wait.until(EC.presence_of_element_located(PasswordRecoveryPageLocators.phone_tab))

    def send_credentials(self, tab_locator, username_value):
        """Sends given credentials to the username field depending on the username tab selected"""
        self.click_on_element(tab_locator)
        username_locator = PasswordRecoveryPageLocators.username_field
        username = self.locate_element(username_locator)
        username.send_keys(username_value)
