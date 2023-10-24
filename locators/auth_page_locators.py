from selenium.webdriver.common.by import By

class AuthorizationPageLocators:
    """Stores all locators present on the
    Authorization page"""
    phone_tab = (By.ID, "t-btn-tab-phone")
    email_tab = (By.ID, "t-btn-tab-mail")
    login_tab = (By.ID, "t-btn-tab-login")
    ls_tab = (By.ID, "t-btn-tab-ls")
    username_field = (By.ID, "username")
    username_placeholder = (By.CSS_SELECTOR, "form .tabs-input-container__login .rt-input__placeholder")
    password_field = (By.ID, "password")
    password_placeholder = (By.CSS_SELECTOR, "#page-right > div > div.card-container__wrapper > div > form > div.rt-input-container > div > span.rt-input__placeholder")
    eye_icon = (By.CLASS_NAME, "rt-input__eye")
    remember_me_checkbox = (By.CLASS_NAME, "rt-checkbox__check-icon")
    forgot_password_button = (By.ID, "forgot_password")
    signin_button = (By.ID, "kc-login")
    user_agreement_button = (By.ID, "rt-auth-agreement-link")
    vk_button = (By.ID, "oidc_vk")
    ok_button = (By.ID, "oidc_ok")
    mail_button = (By.ID, "oidc_mail")
    ya_button = (By.ID, "oidc_ya")
    register_button = (By.ID, "kc-register")
    invalid_credentials_popup = (By.ID, "form-error-message")

class UserPageLocators:
    """Stores a username locator present on the
        page to which a user is redirected after successfully signing in"""
    username = (By.CLASS_NAME, "user-name__last-name")