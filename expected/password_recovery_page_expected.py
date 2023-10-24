from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from settings.keys import *




class ExpectedResults:
    """Stores conditions and expected results for each of the variables used in the tests"""
    hovered_colors = [
        (PasswordRecoveryPageLocators.email_tab, 'rgba(255, 79, 18, 1)'),
        (PasswordRecoveryPageLocators.phone_tab, 'rgba(255, 79, 18, 1)'),
        (PasswordRecoveryPageLocators.ls_tab, 'rgba(255, 79, 18, 1)')
    ]
    username_placeholders = [
        (PasswordRecoveryPageLocators.phone_tab, PasswordRecoveryPageLocators.username_placeholder, 'Мобильный телефон'),
        (PasswordRecoveryPageLocators.email_tab, PasswordRecoveryPageLocators.username_placeholder, 'Электронная почта'),
        (PasswordRecoveryPageLocators.login_tab, PasswordRecoveryPageLocators.username_placeholder, 'Логин'),
        (PasswordRecoveryPageLocators.ls_tab, PasswordRecoveryPageLocators.username_placeholder, 'Лицевой счёт')
    ]
    placeholders = [
        (PasswordRecoveryPageLocators.username_field, PasswordRecoveryPageLocators.username_placeholder,
         'rt-input__placeholder--top', 'rgba(255, 79, 18, 1)'),
        (PasswordRecoveryPageLocators.captcha_entry, PasswordRecoveryPageLocators.captcha_entry_placeholder,
         'rt-input__placeholder--top', 'rgba(255, 79, 18, 1)')
    ]
    invalid_username = [
        (PasswordRecoveryPageLocators.phone_tab, UsernameKeys.random_telephone, 'Неверный логин или текст с картинки'),
        (PasswordRecoveryPageLocators.email_tab, UsernameKeys.random_email, 'Неверный логин или текст с картинки'),
        (PasswordRecoveryPageLocators.login_tab, UsernameKeys.random_login, 'Неверный логин или текст с картинки'),
        (PasswordRecoveryPageLocators.ls_tab, UsernameKeys.random_ls, 'Неверный логин или текст с картинки')
    ]
    redirected_url_path = [
        ('/auth/realms/b2c/login-actions/authenticate')
    ]