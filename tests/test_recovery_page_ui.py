from locators.password_recovery_page_locators import *
from pages.password_recovery_page import *
from expected.password_recovery_page_expected import ExpectedResults
import time
import pytest



#Test_1
@pytest.mark.parametrize('tab_locator, expected_result', ExpectedResults.hovered_colors)
def test_hovering_over_tabs_should_change_color(browser, screenshot_on_failure, tab_locator, expected_result):
    """Tests if hovering over tabs results in a change of color to orange"""
    page = PasswordRecoveryPage(browser, 10)
    page.hover_over((tab_locator,))
    time.sleep(5)
    final_color = page.get_color((tab_locator,))
    assert final_color == expected_result

#Test_2
@pytest.mark.parametrize('tab_locator, expected_result', ExpectedResults.hovered_colors)
def test_clicking_on_tabs_should_change_color(browser, screenshot_on_failure, tab_locator, expected_result):
    """Tests if clicking on tabs results in a change of color to orange"""
    page = PasswordRecoveryPage(browser, 10)
    page.click_on_element((tab_locator,))
    time.sleep(5)
    final_color = page.get_color((tab_locator,))
    assert final_color == expected_result

#Test_3
@pytest.mark.parametrize('tab_locator, placeholder_locator, expected_result', ExpectedResults.username_placeholders)
def test_username_field_placeholder_should_change(browser, screenshot_on_failure, tab_locator, placeholder_locator, expected_result):
    """Tests if the username field placeholder changes when different tabs are pressed"""
    page = PasswordRecoveryPage(browser, 20)
    page.click_on_element((tab_locator,))
    placeholder = page.get_placeholder((placeholder_locator,))
    assert placeholder == expected_result

#Test_4
@pytest.mark.parametrize('field_locator, placeholder_locator, expected_result, color', ExpectedResults.placeholders)
def test_placeholder_should_move_up_when_clicked_on(browser, screenshot_on_failure, field_locator, placeholder_locator,
                                                    expected_result, color):
    """Tests if the username and captcha entry fields placeholders move up when the fields are clicked on"""
    page = PasswordRecoveryPage(browser, 20)
    page.click_on_element((field_locator,))
    placeholder_class = page.get_class_name((placeholder_locator,))
    assert expected_result in placeholder_class

#Test_5
@pytest.mark.parametrize('field_locator, placeholder_locator, class_name, expected_result', ExpectedResults.placeholders)
def test_placeholder_should_change_color_when_clicked_on(browser, screenshot_on_failure, field_locator,
                                                         placeholder_locator, class_name, expected_result):
    """Tests if the username and captcha entry fields placeholders change color when the fields are clicked on"""
    page = PasswordRecoveryPage(browser, 20)
    page.click_on_element((field_locator,))
    time.sleep(5)
    placeholder_color = page.get_color((placeholder_locator,))
    assert placeholder_color == expected_result

#Test_6
def test_reload_captcha(browser, screenshot_on_failure):
    """Tests if reloading captcha results in a new image"""
    page = PasswordRecoveryPage(browser, 20)
    initial_image = page.locate_element(PasswordRecoveryPageLocators.captcha_image)
    page.click_on_element((PasswordRecoveryPageLocators.captcha_reload,))
    time.sleep(5)
    final_image = page.locate_element(PasswordRecoveryPageLocators.captcha_image)
    assert initial_image != final_image

#Test_7
@pytest.mark.parametrize('tab_locator, username_value, expected_result', ExpectedResults.invalid_username)
def test_unauthorized_recovery_attempt(browser, screenshot_on_failure, tab_locator, username_value, expected_result):
    """Tests if it is possible to recover password using invalid usernames"""
    page = PasswordRecoveryPage(browser, 20)
    page.click_on_element((tab_locator,))
    page.send_credentials((tab_locator,), username_value)
    page.click_on_element((PasswordRecoveryPageLocators.continue_button,))
    error = page.locate_element(PasswordRecoveryPageLocators.error_message).text
    assert error == expected_result

#Test_8
@pytest.mark.parametrize('expected_result', ExpectedResults.redirected_url_path)
def test_back_button(browser, screenshot_on_failure, expected_result):
    """Tests if the 'go back' button returns a user to the 'authorization' page"""
    page = PasswordRecoveryPage(browser, 20)
    page.click_on_element((PasswordRecoveryPageLocators.back_button,))
    page.wait_for_url_change()
    new_url = page.get_current_url_path()
    assert new_url == expected_result

