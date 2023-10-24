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
def test_password_recovery_header_presence():
    """Tests if Password Recovery header is present on the page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    header = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'card-container__title'))).text
    assert header == "Восстановление пароля"

#Test_0.2
def test_password_recovery_instructions_presence():
    """Tests if Password Recovery instructions are present on the page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    instructions = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'card-container__desc'))).text
    assert instructions == "Введите данные и нажмите «Продолжить»"

#Test_2.1
def test_email_tab_presence():
    """Tests if email tab is present on the page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    tab = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-mail'))).text
    assert tab == "Почта" 

#Test_2.2
def test_email_tab_clickability():
    """Tests if the email tab is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    email_tab = (By.ID, 't-btn-tab-mail')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(email_tab)).click()
    email_entry_field = driver.find_element(By.ID, 'username')
    email_entry_field.click()
    email_entry_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/span[2]')
    assert 'rt-input__placeholder--top' in email_entry_placeholder.get_attribute("class")

#Test_2.3
def test_email_entry_field_clickability():
    """Tests if email entry field is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-mail'))).click()
    email_field = driver.find_element(By.ID, "username").click()
    email_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/span[2]')
    assert 'active' in email_placeholder.get_attribute("class")

#Test_2.4
def test_email_entry_field_placeholder():
    """Tests if there is a correct email placeholder in the email entry field"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-mail'))).click()
    field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/span[2]'))).text
    assert field == "Электронная почта" 

#Test_2.5
def test_email_tab_hover():
    """Tests if hovering over the email tab results in the change of color"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-mail')))
    email_tab = driver.find_element(By.ID, 't-btn-tab-mail')
    initial_color = email_tab.value_of_css_property("color")
    action = ActionChains(driver)
    action.move_to_element(email_tab).perform()
    hovered_color = email_tab.value_of_css_property("color")
    assert initial_color != hovered_color

#Test_2.6
def test_email_tab_changes_color_when_clicked_on():
    """Tests of the email tab changes color when a user clicks on it"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-mail')))
    email_tab = driver.find_element(By.ID, 't-btn-tab-mail')
    initial_color = email_tab.value_of_css_property("color")
    email_tab.click()
    clicked_color = email_tab.value_of_css_property("color")
    assert initial_color != clicked_color

#Test_2.7
def test_email_captcha_entry_field_placeholder():
    """Tests if captcha entry field has a correct placeholder"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-mail'))).click()
    captcha_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div[2]/div/span[2]')
    assert captcha_placeholder.text == 'Символы'

#Test_2.8
def test_email_captcha_entry_field_clickability():
    """Tests if captcha entry field is clickable"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-mail'))).click()
    captcha_field = driver.find_element(By.ID, "captcha").click()
    captcha_placeholder = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div[2]/div/span[2]')
    assert 'active' in captcha_placeholder.get_attribute("class")

#Test_2.9
def test_email_captcha_instructions_present():
    """Tests if instructions for captcha entry are present"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    instructions = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'rt-input-container__meta'))).text
    assert instructions == "Введите символы с картинки"

#Test_2.10
def test_email_reload_captcha():
    """Tests if reloading captcha results in a new image"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'rt-captcha__image')))
    initial_captcha = driver.find_element(By.CLASS_NAME, 'rt-captcha__image')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'rt-captcha__reload'))).click()
    time.sleep(10)
    new_captcha = driver.find_element(By.CLASS_NAME, 'rt-captcha__image')
    assert initial_captcha != new_captcha 

#Test_2.11
def test_email_unathorized_recovery_attempt():
    """Tests if an unathorized email can be used to recover the password"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-mail'))).click()
    faker = Faker('ru_RU')
    unauthorized_email = faker.email()
    email_entry_field = driver.find_element(By.ID, 'username')
    email_entry_field.send_keys(unauthorized_email)    
    driver.find_element(By.ID, 'reset').click()
    time.sleep(10)
    error_message = driver.find_element(By.ID, 'form-error-message')
    assert error_message.text == 'Неверный логин или текст с картинки'

#Test_2.12
def test_email_blank_field_recovery_attempt():
    """Tests if a blank email field used to recover the password results in the alert message"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-mail'))).click() 
    driver.find_element(By.ID, 'reset').click()
    time.sleep(10)
    alert_message = driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')
    assert alert_message.text == 'Введите адрес, указанный при регистрации'

#Test_2.13
def test_email_go_back_button():
    """Tests if the 'go back' button returns a user to the 'authorization' page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-mail'))).click()
    go_back_button = driver.find_element(By.ID, 'reset-back')
    go_back_button.click()
    time.sleep(10)
    url = urlparse(driver.current_url)
    assert url.path == '/auth/realms/b2c/login-actions/authenticate'

#Test_2.14
def test_email_help_button():
    """Tests if the 'help' button redirects a user to the 'help' page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-mail'))).click()
    help_button = driver.find_element(By.ID, 'faq-open')
    help_button.click()
    time.sleep(10)
    header = driver.find_element(By.CLASS_NAME, 'faq-modal__title')
    assert header.text == 'Ваш безопасный ключ к сервисам Ростелекома'

#Test_2.15
def test_email_help_button_back_to_password_recovery():
    """Tests if going back from the 'help' page opens up the "password recovery' page"""
    driver = webdriver.Safari()
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-mail'))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'forgot_password'))).click()
    help_button = driver.find_element(By.ID, 'faq-open')
    help_button.click()
    time.sleep(10)
    driver.back()
    time.sleep(10)
    url = urlparse(driver.current_url)
    assert url.path == '/auth/realms/b2c/login-actions/reset-credentials'

#Do the same for other tabs in addition to the email tab