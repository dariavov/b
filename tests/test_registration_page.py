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
def test_open_registration_page_by_url():
    """Tests if Authorization header is present on the page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration')
    header = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'card-container__title'))).text
    assert header == "Регистрация", f"Upon attempting to open the registration page by its url, the automated test encountered the message: {header}"

#Test_0.2
def test_registration_header_presence():
    """Tests if Authorization header is present on the page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    header = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'card-container__title'))).text
    assert header == "Регистрация"

#Test_0.3
def test_personal_data_text_presence():
    """Tests if the 'personal data' text is present on the page prompting 
    a user to enter it"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    personal_data_text = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'register-form__desc'))).text
    assert personal_data_text == 'Личные данные'

#Test_0.4
def test_sign_in_data_text_presence():
    """Tests if the 'sign in data' text is present on the page prompting 
    a user to enter it"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    sign_in_data_text = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                                            '//*[@id="page-right"]/div/div[1]/div/form/p[2]'))).text
    assert sign_in_data_text == 'Данные для входа'

#Test_0.5
def test_name_entry_field_presence():
    """Tests if the name entry field is present on the page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    name_entry_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'firstName')))
    assert name_entry_field is not None

#Test_0.6
def test_last_name_entry_field_presence():
    """Tests if the last name entry field is present on the page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    last_name_entry_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'lastName')))
    assert last_name_entry_field is not None

#Test_0.7
def test_select_region_field_presence():
    """Tests if the region selection field is present on the page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    select_region_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'rt-select__rt-input')))
    assert select_region_field is not None

#Test_0.8
def test_email_phone_entry_field_presence():
    """Tests if the email or phone entry field is present on the page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    email_phone_entry_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'address')))
    assert email_phone_entry_field is not None

#Test_0.9
def test_password_entry_field_presence():
    """Tests if the password entry field is present on the page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    password_entry_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'password')))
    assert password_entry_field is not None

#Test_0.10
def test_password_confirm_entry_field_presence():
    """Tests if the password confrimation entry field is present on the page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    password_confirm_entry_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    assert password_confirm_entry_field is not None

#Test_0.11
def test_register_button_presence():
    """Tests if the register button is present on the page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    register_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'register')))
    assert register_button is not None

#Test_0.12
def test_user_agreement_presence():
    """Tests if the user agreement link is present on the page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    user_agreement = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'rt-auth-agreement-link')))
    assert user_agreement is not None

#Test_0.13
def test_help_button_presence():
    """Tests if the help button is present on the page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    help_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'faq-open')))
    assert help_button is not None

#Test_1.1
def test_name_entry_field_clickability():
    """Tests if the name entry field is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    name_entry_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'firstName')))
    name_entry_field.click()
    name_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/span[2]')
    assert 'active' in name_placeholder.get_attribute("class")

#Test_1.2
def test_last_name_entry_field_clickability():
    """Tests if the last name entry field is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    last_name_entry_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'lastName')))
    last_name_entry_field.click()
    last_name_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/span[2]')
    assert 'active' in last_name_placeholder.get_attribute("class")

#Test_1.3
def test_select_region_field_clickability():
    """Tests if the region selection field is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    select_region_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'rt-select__rt-input')))
    select_region_field.click()
    region_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div')
    assert 'active' in region_placeholder.get_attribute("class")

#Test_1.4
def test_email_phone_entry_field_clickability():
    """Tests if the email or phone entry field is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    email_phone_entry_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'address')))
    email_phone_entry_field.click()
    email_phone_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/div/span[2]')
    assert 'active' in email_phone_placeholder.get_attribute("class")

#Test_1.5
def test_password_entry_field_clickability():
    """Tests if the password entry field is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    password_entry_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'password')))
    password_entry_field.click()
    password_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/div/span[2]')
    assert 'active' in password_placeholder.get_attribute("class")

#Test_1.6
def test_password_confirm_entry_field_clickability():
    """Tests if the password confrimation entry field is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    password_confirm_entry_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    password_confirm_entry_field.click()
    password_confirm_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[2]/div/span[2]')
    assert 'active' in password_confirm_placeholder.get_attribute("class")

#Test_1.7
def test_register_button_clickability():
    """Tests if the register button is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'register')))
    register_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'register')))
    assert register_button is not None

#Test_1.8
def test_user_agreement_clickability():
    """Tests if the user agreement link is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'rt-auth-agreement-link')))
    user_agreement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'rt-auth-agreement-link')))
    assert user_agreement is not None

#Test_1.9
def test_help_button_clickability():
    """Tests if the help button is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'faq-open')))
    help_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'faq-open')))
    assert help_button is not None

#Test_1.10
def test_password_eye_icon_clickability():
    """Tests if the password eye icon is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    time.sleep(10)
    eye_icon = driver.find_element(By.CLASS_NAME, 'rt-input__eye')
    eye_icon.click()
    isOpen_attribute = driver.execute_script("return arguments[0].getAttribute('isOpen');", eye_icon)
    assert isOpen_attribute == 'true'

#Test_2.1
def test_name_entry_field_placeholder():
    """Tests if the name entry field has a correct placeholder"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    name_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/span[2]')
    assert name_placeholder.text == 'Имя'

#Test_2.2
def test_last_name_entry_field_placeholder():
    """Tests if the last name entry field has a correct placeholder"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    last_name_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/span[2]')
    assert last_name_placeholder.text == 'Фамилия'

#Test_2.3
def test_select_region_field_placeholder():
    """Tests if the region selection field has a correct placeholder"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    region_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div')
    assert region_placeholder.text == 'Регион'

#Test_2.4
def test_email_phone_entry_field_placeholder():
    """Tests if the email or phone entry field has a correct placeholder"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    email_phone_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/div/span[2]')
    assert email_phone_placeholder.text == 'E-mail или мобильный телефон'

#Test_2.5
def test_password_entry_field_placeholder():
    """Tests if the password entry field has a correct placeholder"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    password_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/div/span[2]')
    assert password_placeholder.text == 'Пароль'

#Test_2.6
def test_password_confirm_entry_field_placeholder():
    """Tests if the password confrimation entry field has a correct placeholder"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    password_confirm_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[2]/div/span[2]')
    assert password_confirm_placeholder.text == 'Подтверждение пароля'

#Test_3.1
def test_blank_name():
    """Tests if the error message shows up  
    when attempting to leave the name field blank"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span').text
    assert message == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Test_3.2
def test_blank_last_name():
    """Tests if the error message shows up  
    when attempting to leave the last name field blank"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span').text
    assert message == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Test_3.3
def test_blank_email_phone():
    """Tests if the error message shows up  
    when attempting to leave the email or telephone field blank"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span').text
    assert message == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

#Test_3.4
def test_blank_password():
    """Tests if the error message shows up  
    when attempting to leave the password field blank"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span').text
    assert message == 'Длина пароля должна быть не менее 8 символов'

#Test_3.5
def test_blank_password_confirm():
    """Tests if the error message shows up  
    when attempting to leave the password confirmation field blank"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[2]/span').text
    assert message == 'Длина пароля должна быть не менее 8 символов'

#Test_4.1
def test_new_user_registration():
    """Tests a positive case of a new user registration"""
    faker = Faker('ru_RU')
    name = faker.first_name()
    last_name = faker.last_name()
    email = faker.email()
    password = faker.password(length=10)
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(name)
    driver.find_element(By.NAME, 'lastName').send_keys(last_name)
    driver.find_element(By.NAME, 'lastName').send_keys(last_name)
    driver.find_element(By.ID, 'address').send_keys(email)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'password-confirm').send_keys(password)
    os.system(f'security add-generic-password -a "{email}" -s "Safari" -w "{password}"')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 
                                                        'register-confirm-form-container__desc'))).text
    assert message == f'Kод подтверждения отправлен на адрес  {email}'

#Test_4.2
def test_registration_english__first_name():
    """Tests a new user registration with a name written in English"""
    name = 'Kirill'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span'))).text
    assert message == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Test_4.3
def test_registration_japanese__first_name():
    """Tests a new user registration with a name written in Japanese"""
    faker = Faker('ja_JP')
    name = faker.first_name()
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span'))).text
    assert message == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Test_4.4
def test_registration_symblos_first_name():
    """Tests a new user registration with a name consisting of symbols"""
    faker = Faker()
    name = faker.password(length=6)
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span'))).text
    assert message == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Test_4.5
def test_registration_1_letter_first_name():
    """Tests a new user registration with a name consisting of 1 letter"""
    name = 'б'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span'))).text
    assert message == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Test_4.6
def test_registration_2_letters_first_name():
    """Tests a new user registration with a name consisting of 2 letters"""
    name = 'бг'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    placeholder = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/span[2]')))
    assert placeholder.value_of_css_property("color") == 'rgba(45, 31, 37, 0.533)'
    
#Test_4.7
def test_registration_3_letters_first_name():
    """Tests a new user registration with a name consisting of 3 letters"""
    name = 'фтч'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    placeholder = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/span[2]')))
    assert placeholder.value_of_css_property("color") == 'rgba(45, 31, 37, 0.533)'

#Test_4.8
def test_registration_29_letters_first_name():
    """Tests a new user registration with a name consisting of 29 letters"""
    name = 'фтччепснтихчсяертнбгдффкисцхз'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    placeholder = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/span[2]')))
    assert placeholder.value_of_css_property("color") == 'rgba(45, 31, 37, 0.533)'

#Test_4.9
def test_registration_30_letters_first_name():
    """Tests a new user registration with a name consisting of 30 letters"""
    name = 'фтччепснтихчсяертнбгдффкисцхзк'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    placeholder = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/span[2]')))
    assert placeholder.value_of_css_property("color") == 'rgba(45, 31, 37, 0.533)'

#Test_4.10
def test_registration_31_letters_first_name():
    """Tests a new user registration with a name consisting of 31 letters"""
    name = 'фтччепснтихчсяертнбгдффкисцхзкп'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span'))).text
    assert message == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Test_4.11
def test_registration_english_last_name():
    """Tests a new user registration with a last name written in English"""
    faker = Faker()
    last_name = faker.last_name()
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(last_name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span'))).text
    assert message == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Test_4.12
def test_registration_japanese_last_name():
    """Tests a new user registration with a last name written in Japanese"""
    faker = Faker('ja_JP')
    name = faker.last_name()
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span'))).text
    assert message == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Test_4.13
def test_registration_symblos_last_name():
    """Tests a new user registration with a last name consisting of symbols"""
    faker = Faker()
    name = faker.password(length=6)
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span'))).text
    assert message == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Test_4.14
def test_registration_1_letter_last_name():
    """Tests a new user registration with a last name consisting of 1 letter"""
    name = 'б'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span'))).text
    assert message == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Test_4.15
def test_registration_2_letters_last_name():
    """Tests a new user registration with a last name consisting of 2 letters"""
    name = 'бг'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    placeholder = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/span[2]')))
    assert placeholder.value_of_css_property("color") == 'rgba(45, 31, 37, 0.533)'
    
#Test_4.16
def test_registration_3_letters_last_name():
    """Tests a new user registration with a last name consisting of 3 letters"""
    name = 'фтч'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    placeholder = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/span[2]')))
    assert placeholder.value_of_css_property("color") == 'rgba(45, 31, 37, 0.533)'

#Test_4.17
def test_registration_29_letters_last_name():
    """Tests a new user registration with a last name consisting of 29 letters"""
    name = 'фтччепснтихчсяертнбгдффкисцхз'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    placeholder = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/span[2]')))
    assert placeholder.value_of_css_property("color") == 'rgba(45, 31, 37, 0.533)'

#Test_4.18
def test_registration_30_letters_last_name():
    """Tests a new user registration with a last name consisting of 30 letters"""
    name = 'фтччепснтихчсяертнбгдффкисцхзк'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    placeholder = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/span[2]')))
    assert placeholder.value_of_css_property("color") == 'rgba(45, 31, 37, 0.533)'

#Test_4.19
def test_registration_31_letters_last_name():
    """Tests a new user registration with a last name consisting of 31 letters"""
    name = 'фтччепснтихчсяертнбгдффкисцхзкп'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span'))).text
    assert message == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#Test_4.20
def test_registration_format_7_phone():
    """Tests a new user registration with a phone in the format 7ХХХХХХХХХХ"""
    faker = Faker()
    name = faker.numerify('7ХХХХХХХХХХ')
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'address'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span'))).text
    assert message == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

#Test_4.21
def test_registration_format_375_phone():
    """Tests a new user registration with a phone in the format 375XXXXXXXXX"""
    faker = Faker()
    name = faker.numerify('375XXXXXXXXX')
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'address'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span'))).text
    assert message == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

#Test_4.22
def test_registration_format_8_phone():
    """Tests a new user registration with a phone in the format 8ХХХХХХХХХХ"""
    faker = Faker()
    name = faker.numerify('8ХХХХХХХХХХ')
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'address'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span'))).text
    assert message == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

#Test_4.23
def test_registration_foreign_email():
    """Tests a new user registration with a foreign email"""
    faker = Faker()
    name = faker.email()
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'address'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span'))).text
    assert message == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

#Test_4.24
def test_registration_existing_email():
    """Tests registration using existing email"""
    faker = Faker('ru_RU')
    name = faker.first_name()
    last_name = faker.last_name()
    email = 'wet05956@zslsz.com'
    password = faker.password(length=10)
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(name)
    driver.find_element(By.NAME, 'lastName').send_keys(last_name)
    driver.find_element(By.NAME, 'lastName').send_keys(last_name)
    driver.find_element(By.ID, 'address').send_keys(email)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'password-confirm').send_keys(password)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 
                                                        'card-modal__title'))).text
    assert message == 'Учётная запись уже существует'

#Test_4.25
def test_registration_english_lowercase_letter_password():
    """Tests a new user registration with a password that consists of only lowercase English letters"""
    name = 'fhgjakdsfdjhg'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'))).text
    assert message == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' or message == 'Пароль должен содержать хотя бы одну заглавную букву'

#Test_4.26
def test_registration_english_uppercase_letter_password():
    """Tests a new user registration with a password that consists of only uppercase English letters"""
    name = 'HFLKEHGKEGKVKBFK'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'))).text
    assert message == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' or message == 'Пароль должен содержать хотя бы одну строчную букву'

#Test_4.27
def test_registration_english_1_uppercase_letter_password():
    """Tests a new user registration with a password that consists of 1 uppercase English letters
    but no special characters"""
    name = 'Hkwbfbke'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'))).text
    assert message == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' 

#Test_4.28
def test_registration_english_1_symbol_letter_password():
    """Tests a new user registration with a password that consists of English letters
    with 1 special charcater but no uppercase letters"""
    name = 'dfkglkehglkaegl@'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'))).text
    assert message == 'Пароль должен содержать хотя бы одну заглавную букву'

#Test_4.29
def test_registration_english_working_password():
    """Tests a new user registration with a password that consists of English letters
    and meets all the criteria"""
    name = 'Hkvkdbvkbfkfvdk1'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    placeholder = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/div/span[2]')))
    assert placeholder.value_of_css_property("color") == 'rgba(45, 31, 37, 0.533)'

#Test_4.30
def test_registration_russian_letter_password():
    """Tests a new user registration with a password that consists of Russian letters"""
    name = 'чгкелйгччргкйрг'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'))).text
    assert message == 'Пароль должен содержать только латинские буквы'

#Test_4.31
def test_registration_legit_russian_letter_password():
    """Tests a new user registration with a password that consists of Russian letters
    but otherwise meets the criteria"""
    name = 'F2гкелйгччргкйрг'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'))).text
    assert message == 'Пароль должен содержать только латинские буквы'

#Test_4.32
def test_registration_legit_japanese_letter_password():
    """Tests a new user registration with a password that consists of Japanese letters 
    but otherwise meets the criteria"""
    name = '百秋瑞原千五百秋瑞Aa1'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'))).text
    assert message is not None

#Test_4.33
def test_registration_7_character_password():
    """Tests a new user registration with a password that contains 7 characters"""
    name = 'Aggggg8'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'))).text
    assert message == 'Длина пароля должна быть не менее 8 символов'

#Test_4.34
def test_registration_8_character_password():
    """Tests a new user registration with a password that contains 8 characters"""
    name = 'Aggggg88'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    placeholder = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/div/span[2]')))
    assert placeholder.value_of_css_property("color") == 'rgba(45, 31, 37, 0.533)'

#Test_4.35
def test_registration_9_character_password():
    """Tests a new user registration with a password that contains 9 characters"""
    name = 'Aggggg88^'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    placeholder = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/div/span[2]')))
    assert placeholder.value_of_css_property("color") == 'rgba(45, 31, 37, 0.533)'

#Test_4.36
def test_registration_19_character_password():
    """Tests a new user registration with a password that contains 19 characters"""
    name = 'A5fhpashnvchwrisjks'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    placeholder = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/div/span[2]')))
    assert placeholder.value_of_css_property("color") == 'rgba(45, 31, 37, 0.533)'

#Test_4.37
def test_registration_20_character_password():
    """Tests a new user registration with a password that contains 20 characters"""
    name = 'A5fhpashnvchwrisjksk'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    placeholder = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/div/span[2]')))
    assert placeholder.value_of_css_property("color") == 'rgba(45, 31, 37, 0.533)'

#Test_4.38
def test_registration_21_character_password():
    """Tests a new user registration with a password that contains 21 characters"""
    name = 'A5fhpashnvchwrisjksfg'
    driver = webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'kc-register'))).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(name)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()
    message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, 
                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'))).text
    assert message == 'Длина пароля должна быть не более 20 символов'

