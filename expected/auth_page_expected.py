from locators.auth_page_locators import AuthorizationPageLocators
from settings.keys import *




class ExpectedResults:
    """Stores conditions and expected results for each of the variables used in the tests"""
    hovered_colors = [
        (AuthorizationPageLocators.email_tab, 'rgba(255, 79, 18, 1)'),
        (AuthorizationPageLocators.login_tab, 'rgba(255, 79, 18, 1)'),
        (AuthorizationPageLocators.ls_tab, 'rgba(255, 79, 18, 1)')
    ]
    username_placeholders = [
        (AuthorizationPageLocators.phone_tab, AuthorizationPageLocators.username_placeholder, 'Мобильный телефон'),
        (AuthorizationPageLocators.email_tab, AuthorizationPageLocators.username_placeholder, 'Электронная почта'),
        (AuthorizationPageLocators.login_tab, AuthorizationPageLocators.username_placeholder, 'Логин'),
        (AuthorizationPageLocators.ls_tab, AuthorizationPageLocators.username_placeholder, 'Лицевой счёт')
    ]
    placeholders = [
        (AuthorizationPageLocators.username_field, AuthorizationPageLocators.username_placeholder,
         'rt-input__placeholder--top', 'rgba(255, 79, 18, 1)'),
        (AuthorizationPageLocators.password_field, AuthorizationPageLocators.password_placeholder,
         'rt-input__placeholder--top', 'rgba(255, 79, 18, 1)')
    ]
    valid_credentials = [
        (AuthorizationPageLocators.email_tab, UsernameKeys.valid_email, PasswordKeys.valid_password, 'Чегевара'),
        (AuthorizationPageLocators.login_tab, UsernameKeys.valid_login, PasswordKeys.valid_password, 'Чегевара')
    ]
    invalid_credentials = [
        (AuthorizationPageLocators.phone_tab, UsernameKeys.random_telephone, PasswordKeys.valid_password,
         'Неверный логин или пароль'),
        (AuthorizationPageLocators.email_tab, UsernameKeys.random_email, PasswordKeys.valid_password,
         'Неверный логин или пароль'),
        (AuthorizationPageLocators.email_tab, UsernameKeys.valid_email, PasswordKeys.random_password,
         'Неверный логин или пароль'),
        (AuthorizationPageLocators.login_tab, UsernameKeys.random_login, PasswordKeys.valid_password,
         'Неверный логин или пароль'),
        (AuthorizationPageLocators.ls_tab, UsernameKeys.random_ls, PasswordKeys.valid_password,
         'Неверный логин или пароль')
    ]
    social_networks = [
        (AuthorizationPageLocators.vk_button, 'id.vk.com'),
        (AuthorizationPageLocators.ok_button, 'connect.ok.ru'),
        (AuthorizationPageLocators.mail_button, 'connect.mail.ru'),
        (AuthorizationPageLocators.ya_button, 'passport.yandex.ru')
    ]
    eye_icon = [
        ('invisible', AuthorizationPageLocators.password_field, RegistrationInputs.eight_chars_password,
         AuthorizationPageLocators.eye_icon, '........'),
        ('visible', AuthorizationPageLocators.password_field, RegistrationInputs.eight_chars_password,
         AuthorizationPageLocators.eye_icon, RegistrationInputs.eight_chars_password)
        ]
