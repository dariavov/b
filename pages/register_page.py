from pages.base_page import BasePage
from locators.register_page_locators import *
from locators.auth_page_locators import *
from settings.keys import *

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class RegisterPage(BasePage):
    """Stores registration-related functions and elements available for use in the tests"""
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru'
        driver.get(url)
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.presence_of_element_located(AuthorizationPageLocators.register_button)).click()
        wait.until(EC.presence_of_element_located(RegisterPageLocators.first_name))

    def send_credentials(self, field_locator, input_value):
        """Sends given credentials to a specified field"""
        field = self.locate_element(field_locator)
        field.send_keys(input_value)

    def send_credentials_to_all_fields(self, first_name, last_name, name_value,
                                       address, address_value, password, password_confirm, password_value):
        """Fills in all registration page fields with given credentials"""
        first_name_field = self.locate_element(first_name)
        first_name_field.send_keys(name_value)
        last_name_field = self.locate_element(last_name)
        last_name_field.send_keys(name_value)
        address_field = self.locate_element(address)
        address_field.send_keys(address_value)
        password_field = self.locate_element(password)
        password_field.send_keys(password_value)
        password_confirm_field = self.locate_element(password_confirm)
        password_confirm_field.send_keys(password_value)

    def select_from_dropdown(self, text):
        """Selects a specific element from the dropdown"""
        self.click_on_element((RegisterPageLocators.region_dropdown,))
        self.driver.find_element(By.XPATH, f"//*[text()='{text}']").click()
        return self.locate_element(RegisterPageLocators.region_dropdown_field).get_attribute("value")
