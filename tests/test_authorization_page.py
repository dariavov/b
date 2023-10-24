import time
import pytest
import selenium

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
import os
import requests 
from urllib.parse import urlparse



#Test_0.1
def test_open_authorization_page():
    """Tests if Authorization page opens"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    time.sleep(5)
    url = urlparse(driver.current_url)
    assert url.path == '/auth/realms/b2c/protocol/openid-connect/auth' or url.path == '/account_b2c/page'

#Test_0.2
def test_authorization_header_visibility():
    """Tests if Authorization header is visible on the page"""
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    header = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'card-container__title'))).click()
    #assert header == "Авторизация"

#Test_0.2
def test_authorization_header_visibility():
    """Tests if Authorization header is visible on the page"""
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    header = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'card-container__title')))
    #assert header == "Авторизация"

#Test_1.1
def test_telephone_tab_presence():
    """Tests if telephone tab is present on the page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    tab = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).text
    assert tab == "Телефон" 

#Test_1.2
def test_telephone_tab_clickability():
    """Tests if the telephone tab is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    telephone_tab = (By.ID, 't-btn-tab-phone')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(telephone_tab))
    email_entry_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/span[2]')
    assert email_entry_placeholder.text == 'Мобильный телефон'

#Test_1.3
def test_telephone_field_clickability():
    """Tests if telephone entry field is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    telephone_field = driver.find_element(By.ID, "username").click()
    telephone_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/span[2]')
    assert 'active' in telephone_placeholder.get_attribute("class")

#Test_1.4
def test_telephone_placeholder():
    """Tests if there is a correct telephone placeholder in the telephone entry field"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/span[2]'))).text
    assert field == "Мобильный телефон" 

#Test_1.5
def test_telephone_tab_hover():
    """Tests if hovering over the telephone tab results in the change of color"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-mail'))).click()
    phone_tab = driver.find_element(By.ID, 't-btn-tab-phone')
    initial_color = phone_tab.value_of_css_property("color")
    action = ActionChains(driver)
    action.move_to_element(phone_tab).perform()
    hovered_color = phone_tab.value_of_css_property("color")
    assert initial_color != hovered_color

#Test_1.6
def test_telephone_tab_changes_color_when_clicked_on():
    """Tests of the telephone tab changes color when a user clicks on it"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-mail'))).click()
    phone_tab = driver.find_element(By.ID, 't-btn-tab-phone')
    initial_color = phone_tab.value_of_css_property("color")
    phone_tab.click()
    clicked_color = phone_tab.value_of_css_property("color")
    assert initial_color != clicked_color

#Test_1.7
def test_tel_password_clickability():
    """Tests is password field is clickable when attempting to sign in with phone number"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    password_field = driver.find_element(By.ID, "password").click()
    password_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/span[2]')
    assert 'active' in password_placeholder.get_attribute("class")

#Test_1.8
def test_tel_password_placeholder():
    """Tests if password placeholder is present when attempting to sign in with phone number"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/span[2]'))).text
    assert field == "Пароль" 

#Test_1.9
def test_tel_password_visibility():
    """Tests if password becomes visible when clicking on the eye icon while 
    attempting to sign in with phone number"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    eye_icon = driver.find_element(By.CLASS_NAME, 'rt-input__eye')
    eye_icon.click()
    
    #When .get_attribute('attribute_name') wouldn't work:
    isOpen_attribute = driver.execute_script("return arguments[0].getAttribute('isOpen');", eye_icon)
    assert isOpen_attribute == 'true'

#Test_1.10
def test_tel_remember_me_chekbox():
    """Tests if 'remember me' checkbox works"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    checkbox = driver.find_element(By.CLASS_NAME, 'rt-checkbox')
    checkbox.click()
    time.sleep(5)
    assert "rt-checkbox--checked" in checkbox.get_attribute("class") 

#Test_1.11
def test_tel_hover_forgot_password():
    """Tests if a hover effect on the 'forgot pasword' button works"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    forgot_password = driver.find_element(By.ID, 'forgot_password')
    initial_color = forgot_password.value_of_css_property("color")
    action = ActionChains(driver)
    action.move_to_element(forgot_password).perform()
    hovered_color = forgot_password.value_of_css_property("color")
    assert initial_color != hovered_color

#Test_1.12
def test_tel_forgot_password_redirect():
    """Tests if the 'forgot password' button redirects to the 'password recovery' page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'forgot_password'))).click()
    time.sleep(5)
    url = urlparse(driver.current_url)
    assert url.path == '/auth/realms/b2c/login-actions/reset-credentials'

#Test_1.13
def test_tel_forgot_password_back_button():
    """Tests if the back button works properly after being redirected to the 
    'forgot password' page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'forgot_password'))).click()
    WebDriverWait(driver, 20).until(EC.url_changes)
    driver.back()
    url = urlparse(driver.current_url)
    assert url.path == '/auth/realms/b2c/protocol/openid-connect/auth'


#Test_1.14
def test_tel_unauthorized_signin():
    """Tests if an error message is displayed when signing in using unauthorized credentials"""
    faker = Faker('ru_Ru')
    unauthorized_telephone = faker.numerify('7##########')
    unauthorized_password = faker.password()
    
    #Store the credentials in the Keychain to avoid the popup window:
    os.system(f'security add-generic-password -a "{unauthorized_telephone}" -s "Safari" -w "{unauthorized_password}"')
    
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    telephone = driver.find_element(By.ID, 'username').send_keys(unauthorized_telephone)
    password = driver.find_element(By.ID, 'password')
    password.send_keys(unauthorized_password)
    eye_icon = driver.find_element(By.CLASS_NAME, 'rt-input__eye')
    #eye_icon.click()
    #assert password.get_attribute('type') == 'text'
    assert password.get_attribute('value') == unauthorized_password
    #driver.find_element(By.ID, 'kc-login').click()
    #error_message = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'form-error-message')))
    #assert error_message.is_displayed()

#Test_1.15
def test_tel_notelephone_signin():
    """Tests if an error message is displayed when attempting to sign in without a password"""
    faker = Faker('ru_Ru')
    unauthorized_password = faker.password()
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    password = driver.find_element(By.ID, 'password').send_keys(unauthorized_password)
    driver.find_element(By.ID, 'kc-login').click()
    error_message = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'rt-input-container__meta--error')))
    assert error_message.is_displayed()

#Test_1.16
def test_tel_user_agreement_clickability():
    """Tests if the 'user agreement' button is clickable"""
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    user_agreement = driver.find_element(By.ID, 'rt-auth-agreement-link')
    
    # assert user_agreement.get_attribute('disabled') == 'false' is not executed correctly
    disabled_attribute = driver.execute_script("return arguments[0].getAttribute('disabled');", user_agreement)
    assert disabled_attribute == 'false'

#Test_1.17
def test_tel_sign_in_via_vk():
    """Tests if a user can successfully sign in via vk"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    driver.find_element(By.ID, 'oidc_vk').click()
    time.sleep(10)
    url = urlparse(driver.current_url)
    assert url.hostname == 'id.vk.com'

#Test_1.18
def test_tel_sign_in_via_vk_back_button():
    """Tests if the back button works properly after being redirected to the 
    'vk signin' page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'oidc_vk'))).click()
    WebDriverWait(driver, 20).until(EC.url_changes)
    driver.back()
    url = urlparse(driver.current_url)
    assert url.path == '/auth/realms/b2c/protocol/openid-connect/auth'   

#Test_1.19
def test_tel_sign_in_via_ok():
    """Tests if a user can successfully sign in via ok"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    driver.find_element(By.ID, 'oidc_ok').click()
    time.sleep(10)
    url = urlparse(driver.current_url)
    assert url.hostname == 'connect.ok.ru'

#Test_1.20
def test_tel_sign_in_via_ok_back_button():
    """Tests if the back button works properly after being redirected to the 
    'ok signin' page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'oidc_ok'))).click()
    time.sleep(10)
    driver.back()
    url = urlparse(driver.current_url)
    assert url.path == '/auth/realms/b2c/protocol/openid-connect/auth' 

#Test_1.21
def test_tel_sign_in_via_mailru():
    """Tests if a user can successfully sign in via mailru"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    driver.find_element(By.ID, 'oidc_mail').click()
    time.sleep(10)
    url = urlparse(driver.current_url)
    assert url.hostname == 'connect.mail.ru' 

#Test_1.22
def test_tel_sign_in_via_mailru_back_button():
    """Tests if the back button works properly after being redirected to the 
    'mailru signin' page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'oidc_mail'))).click()
    time.sleep(10)
    driver.back()
    url = urlparse(driver.current_url)
    assert url.path == '/auth/realms/b2c/protocol/openid-connect/auth' 

#Test_1.23
def test_tel_sign_in_via_yandex():
    """Tests if a user can successfully sign in via yandex"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    driver.find_element(By.ID, 'oidc_ya').click()
    time.sleep(10)
    url = urlparse(driver.current_url)
    assert url.hostname == 'passport.yandex.ru' 

#Test_1.24
def test_tel_sign_in_via_yandex_back_button():
    """Tests if the back button works properly after being redirected to the 
    'yandex signin' page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'oidc_ya'))).click()
    time.sleep(10)
    driver.back()
    url = urlparse(driver.current_url)
    assert url.path == '/auth/realms/b2c/protocol/openid-connect/auth' 

#Test_1.25
def test_tel_register_button_clickability():
    """Tests if the 'register' button is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    register_button = driver.find_element(By.ID, 'kc-register')
    disabled_attribute = driver.execute_script("return arguments[0].getAttribute('disabled');", register_button)
    assert disabled_attribute == 'false'

#Test_1.26
def test_tel_register_button_redirect():
    """Tests if clicking on the 'register' button takes a user to the 'registartion' page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    time.sleep(5)
    url = urlparse(driver.current_url)
    assert url.path == '/auth/realms/b2c/login-actions/registration'
    
#Test_1.27
def test_tel_register_button_back_button():
    """Tests if the back button works properly after being redirected to the 
    'registration' page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    time.sleep(10)
    driver.back()
    url = urlparse(driver.current_url)
    assert url.path == '/auth/realms/b2c/protocol/openid-connect/auth' 

#Test_1.28
def test_tel_help_button_clickability():
    """Tests if the 'help' button is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-phone'))).click()
    help_button = driver.find_element(By.CLASS_NAME, 'faq-modal-tip__btn')
    disabled_attribute = driver.execute_script("return arguments[0].getAttribute('disabled');", help_button)
    assert disabled_attribute == 'false'

#Test_1.29
def test_tel_get_request_authorization_page():
    """Tests if response code is 200 when opening the authorization page"""
    response = requests.get('https://b2c.passport.rt.ru')
    assert response.status_code == 200

#Test_1.30
def test_tel_post_request_unauthorized_sign_in():
    """Tests if response code is 400 when signing in with the unauthorized credentials"""
    faker = Faker('ru_Ru')
    unauthorized_telephone = faker.numerify('7##########')
    unauthorized_password = faker.password()
    response = requests.post('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=M2ApBGEykP0',
                             headers={"Content-Type": "application/json"}, 
                             json={"username": unauthorized_telephone, 
                                   "password": unauthorized_password})
    assert response.status_code == 400

#Test_1.31
def test_tel_get_request_password_recovery():
    """Tests if response code is 200 when clicking on the 'forgot password' button"""
    response = requests.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=M2ApBGEykP0')
    assert response.status_code == 200

#Test_1.32
def test_tel_get_request_registration():
    """Tests if response code is 200 when clicking on the 'register' button"""
    response = requests.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration',
                            headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
                                     "Content-Type": "application/json"})
    assert response.status_code == 200

#Do te same for other tabs in addition to the tel tab
 
