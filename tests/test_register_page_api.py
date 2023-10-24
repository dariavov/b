from expected.register_page_expected import ExpectedResults
import pytest
import requests

#Test_1
def test_get_registration_page():
    """Tests if response code is 200 when clicking on the 'register' button"""
    response = requests.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration',
                            headers={
                                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
                                "Content-Type": "application/json"})
    assert response.status_code == 200

#Test_2
@pytest.mark.parametrize('name, region, address, password, expected_result', ExpectedResults.new_registration)
def test_register_new_user(name, region, address, password, expected_result):
    """Tests if response code is 200 when registering a new user"""
    response = requests.post(
        'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration',
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        json={"MIME Type": "application/x-www-form-urlencoded",
              "firstName": name,
              "lastName": name,
              "region": region,
              "address": address,
              "password": password,
              "password-confirm": password
              }
    )
    assert response.status_code == expected_result

