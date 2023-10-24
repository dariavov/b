from locators.auth_page_locators import *
from pages.auth_page import *
from expected.auth_page_expected import ExpectedResults
import time
import pytest



#Test_1
@pytest.mark.parametrize('tab_locator, expected_result', ExpectedResults.hovered_colors)
def test_hovering_over_tabs_should_change_color(browser, screenshot_on_failure, tab_locator, expected_result):
    """Tests if hovering over tabs results in a change of color to orange"""
    page = AuthorizationPage(browser, 10)
    page.hover_over((tab_locator,))
    time.sleep(5)
    final_color = page.get_color((tab_locator,))
    assert final_color == expected_result

#Test_2
@pytest.mark.parametrize('tab_locator, expected_result', ExpectedResults.hovered_colors)
def test_clicking_on_tabs_should_change_color(browser, screenshot_on_failure, tab_locator, expected_result):
    """Tests if clicking on tabs results in a change of color to orange"""
    page = AuthorizationPage(browser, 10)
    page.click_on_element((tab_locator,))
    time.sleep(5)
    final_color = page.get_color((tab_locator,))
    assert final_color == expected_result

#Test_3
@pytest.mark.parametrize('tab_locator, placeholder_locator, expected_result', ExpectedResults.username_placeholders)
def test_username_field_placeholder_should_change(browser, screenshot_on_failure, tab_locator, placeholder_locator, expected_result):
    """Tests if the username field placeholder changes when different tabs are pressed"""
    page = AuthorizationPage(browser, 20)
    page.click_on_element((tab_locator,))
    placeholder = page.get_placeholder((placeholder_locator,))
    assert placeholder == expected_result

#Test_4
@pytest.mark.parametrize('field_locator, placeholder_locator, expected_result, color', ExpectedResults.placeholders)
def test_placeholder_should_move_up_when_clicked_on(browser, screenshot_on_failure, field_locator, placeholder_locator,
                                                    expected_result, color):
    """Tests if the username and password fields placeholders move up when the fields are clicked on"""
    page = AuthorizationPage(browser, 20)
    page.click_on_element((field_locator,))
    placeholder_class = page.get_class_name((placeholder_locator,))
    assert expected_result in placeholder_class

#Test_5
@pytest.mark.parametrize('field_locator, placeholder_locator, class_name, expected_result', ExpectedResults.placeholders)
def test_placeholder_should_change_color_when_clicked_on(browser, screenshot_on_failure, field_locator,
                                                         placeholder_locator, class_name, expected_result):
    """Tests if the username and password fields placeholders change color when the fields are clicked on"""
    page = AuthorizationPage(browser, 20)
    page.click_on_element((field_locator,))
    time.sleep(5)
    placeholder_color = page.get_color((placeholder_locator,))
    assert placeholder_color == expected_result

#Test_6
@pytest.mark.parametrize('tab_locator, username_value, password_value, expected_result', ExpectedResults.valid_credentials)
def test_authorized_sign_in(browser, screenshot_on_failure, tab_locator,
                                                         username_value, password_value, expected_result):
    """Tests if it is possible to sign in with the authorized username and password"""
    page = AuthorizationPage(browser, 20)
    page.send_credentials((tab_locator,), username_value, password_value)
    signin_button = AuthorizationPageLocators.signin_button
    page.click_on_element((signin_button,))
    redirected_page = UserPage(browser, 20)
    title = redirected_page.get_element_title(UserPageLocators.username)
    assert title == expected_result

#Test_7
@pytest.mark.parametrize('tab_locator, username_value, password_value, expected_result', ExpectedResults.invalid_credentials)
def test_unauthorized_sign_in(browser, screenshot_on_failure, tab_locator,
                                                         username_value, password_value, expected_result):
    """Tests if it is possible to sign in with the unauthorized username and password"""
    page = AuthorizationPage(browser, 20)
    page.send_credentials((tab_locator,), username_value, password_value)
    signin_button = AuthorizationPageLocators.signin_button
    page.click_on_element((signin_button,))
    text = page.get_element_text(AuthorizationPageLocators.invalid_credentials_popup)
    assert text == expected_result

#Test_8
@pytest.mark.parametrize('button_locator, expected_result', ExpectedResults.social_networks)
def test_authorization_via_social_networks(browser, screenshot_on_failure, button_locator,
                                                         expected_result):
    """Tests if it is possible to get authorized via social networks"""
    page = AuthorizationPage(browser, 20)
    page.click_on_element((button_locator,))
    page.wait_for_url_change()
    new_url = page.get_current_url_hostname()
    assert new_url == expected_result

#Test_9
@pytest.mark.parametrize('condition, field_locator, input_value, eye_icon_locator, expected_result', ExpectedResults.eye_icon)
def test_password_visibility_in_DOM(browser, screenshot_on_failure, condition, field_locator, input_value, eye_icon_locator, expected_result):
    """Tests whether the 'show password' function works properly for the password entry field"""
    page = AuthorizationPage(browser, 10)
    password = page.locate_element(field_locator)
    page.send_keys_to_password(field_locator, input_value)
    if condition == 'visible':
        page.click_on_element((eye_icon_locator,))
    assert password.get_attribute("value") == expected_result

