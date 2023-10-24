from selenium.webdriver.common.by import By

class PasswordRecoveryPageLocators:
    """Stores all locators present on the Password Recovery page"""
    phone_tab = (By.ID, "t-btn-tab-phone")
    email_tab = (By.ID, "t-btn-tab-mail")
    login_tab = (By.ID, "t-btn-tab-login")
    ls_tab = (By.ID, "t-btn-tab-ls")
    username_field = (By.ID, "username")
    username_placeholder = (By.CSS_SELECTOR, "form .tabs-input-container__login .rt-input__placeholder")
    captcha_image = (By.CLASS_NAME, "rt-captcha__image")
    captcha_reload = (By.CLASS_NAME, "rt-captcha__reload")
    captcha_entry = (By.ID, "captcha")
    captcha_entry_placeholder = (By.CSS_SELECTOR, "div.rt-captcha__input span.rt-input__placeholder")
    continue_button = (By.ID, "reset")
    back_button = (By.ID, "reset-back")
    error_message = (By.ID, "form-error-message")