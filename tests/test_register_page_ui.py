from locators.register_page_locators import *
from pages.register_page import *
from expected.register_page_expected import ExpectedResults
import time
import pytest
from selenium.common.exceptions import TimeoutException


#Test_1
@pytest.mark.parametrize('field_locator, placeholder_locator, expected_result, color', ExpectedResults.placeholders)
def test_placeholder_should_move_up_when_clicked_on(browser, screenshot_on_failure, field_locator, placeholder_locator,
                                                    expected_result, color):
    """Tests if the credentials entry fields placeholders move up when the fields are clicked on"""
    page = RegisterPage(browser, 20)
    page.click_on_element((field_locator,))
    placeholder_class = page.get_class_name((placeholder_locator,))
    assert expected_result in placeholder_class

#Test_2
@pytest.mark.parametrize('field_locator, placeholder_locator, class_name, expected_result', ExpectedResults.placeholders)
def test_placeholder_should_change_color_when_clicked_on(browser, screenshot_on_failure, field_locator,
                                                         placeholder_locator, class_name, expected_result):
    """Tests if the credentials entry fields placeholders change color when the fields are clicked on"""
    page = RegisterPage(browser, 20)
    page.click_on_element((field_locator,))
    time.sleep(5)
    placeholder_color = page.get_color((placeholder_locator,))
    assert placeholder_color == expected_result

#Test_3
@pytest.mark.parametrize('field_locator, input_value', ExpectedResults.negative_inputs)
def test_negative_input(browser, screenshot_on_failure, field_locator, input_value):
    """Tests whether the page responds with an error message if
    the input for any given field does not meet the requirements"""
    page = RegisterPage(browser, 20)
    page.send_credentials(field_locator, input_value)
    page.click_on_element((RegisterPageLocators.page_left,))
    error = page.locate_element(RegisterPageLocators.error_locator)
    assert error is not None

#Test_4
@pytest.mark.parametrize('field_locator, input_value', ExpectedResults.positive_inputs)
def test_positive_input(browser, screenshot_on_failure, field_locator, input_value):
    """Tests whether the page responds with an error message if
    the input for any given field meets the requirements"""
    page = RegisterPage(browser, 10)
    page.send_credentials(field_locator, input_value)
    page.click_on_element((RegisterPageLocators.page_left,))
    try:
        error = page.locate_element(RegisterPageLocators.error_locator)
        assert error is None
    except TimeoutException:
        pass

#Test_5
@pytest.mark.parametrize('first_name, last_name, name_value, address, address_value, password, password_confirm, password_value, expected_result',
                         ExpectedResults.existing_email)
def test_register_with_existing_email(browser, screenshot_on_failure, first_name, last_name, name_value, address,
                                      address_value, password, password_confirm, password_value, expected_result):
    """Tests whether the page responds with an error message if
    registering with an existing email address"""
    page = RegisterPage(browser, 20)
    page.send_credentials_to_all_fields(first_name, last_name, name_value, address, address_value, password,
                                        password_confirm, password_value)
    page.click_on_element((RegisterPageLocators.register_button,))
    error = page.get_element_text(RegisterPageLocators.account_exists_error)
    assert error == expected_result

#Test_6
@pytest.mark.parametrize('first_name, last_name, name_value, address, address_value, password, password_confirm, password_value, expected_result',
                         ExpectedResults.valid_credentials)
def test_register_with_valid_credentials(browser, screenshot_on_failure, first_name, last_name, name_value, address,
                                      address_value, password, password_confirm, password_value, expected_result):
    """Tests whether the page responds with an email confirmation message if
    registering with valid credentials"""
    page = RegisterPage(browser, 20)
    page.send_credentials_to_all_fields(first_name, last_name, name_value, address, address_value, password,
                                        password_confirm, password_value)
    page.click_on_element((RegisterPageLocators.register_button,))
    message = page.get_element_text(RegisterPageLocators.registration_email_confirmation)
    assert message == expected_result

#Test_7
@pytest.mark.parametrize('condition, field_locator, input_value, eye_icon_locator, expected_result', ExpectedResults.eye_icon)
def test_password_visibility_in_DOM(browser, screenshot_on_failure, condition, field_locator, input_value, eye_icon_locator, expected_result):
    """Tests whether the 'show password' function works properly for both password entry fields"""
    page = RegisterPage(browser, 10)
    password = page.locate_element(field_locator)
    page.send_credentials(field_locator, input_value)
    if condition == 'visible':
        page.click_on_element((eye_icon_locator,))
    assert password.get_attribute("value") == expected_result

#Test_8
@pytest.mark.parametrize('text', ExpectedResults.region_dropdown)
def test_region_dropdown(browser, screenshot_on_failure, text):
    """Tests whether the region dropdown selection works"""
    page = RegisterPage(browser, 10)
    selected_dropdown_option = page.select_from_dropdown(text)
    assert selected_dropdown_option == text