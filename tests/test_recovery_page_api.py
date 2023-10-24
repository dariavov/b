import requests

#Test_1
def test_get_password_recovery_page():
    """Tests if response code is 200 when opening the Password Recovery page"""
    response = requests.get(
        'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    assert response.status_code == 200