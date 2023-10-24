from expected.auth_page_expected import ExpectedResults
import pytest
import requests


#Test_1
def test_get_authorization_page():
    """Tests if response code is 200 when opening the authorization page"""
    response = requests.get('https://b2c.passport.rt.ru')
    assert response.status_code == 200

#Test_2
@pytest.mark.parametrize('tab_locator, username_value, password_value, expected_result', ExpectedResults.valid_credentials)
def test_authorized_sign_in_response_code(screenshot_on_failure, tab_locator,
                                                         username_value, password_value, expected_result):
    """Tests if response code is 200 when signing in with the authorized credentials"""
    response = requests.post(
        'https://b2c.passport.rt.ru',
        headers={"Content-Type": "application/json"},
        json={"username": username_value,
              "password": password_value})
    assert response.status_code == 200

#Test_3
@pytest.mark.parametrize('tab_locator, username_value, password_value, expected_result', ExpectedResults.invalid_credentials)
def test_unauthorized_sign_in_response_code(screenshot_on_failure, tab_locator,
                                                         username_value, password_value, expected_result):
    """Tests if response code is 400 when signing in with the unauthorized credentials"""
    response = requests.post(
        'https://b2c.passport.rt.ru',
        headers={"Content-Type": "application/json"},
        json={"username": username_value,
              "password": password_value})
    assert response.status_code == 400













