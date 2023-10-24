from selenium.webdriver.common.by import By

class RegisterPageLocators:
    """Stores all locators present on the Registration page"""
    first_name = (By.NAME, "firstName")
    first_name_placeholder = (By.CSS_SELECTOR,
    "#page-right > div > div.card-container__wrapper > div > form > div.name-container > div:nth-child(1) > div > span.rt-input__placeholder")
    last_name = (By.NAME, "lastName")
    last_name_placeholder = (By.CSS_SELECTOR,
    "#page-right > div > div.card-container__wrapper > div > form > div.name-container > div:nth-child(2) > div > span.rt-input__placeholder")
    region_dropdown = (By.CLASS_NAME, "rt-select__arrow")
    region_dropdown_field = (By.CSS_SELECTOR,
    "#page-right > div > div.card-container__wrapper > div > form > div.rt-select.rt-select--search.register-form__dropdown > div > div > input")
    address = (By.ID, "address")
    address_placeholder = (By.CSS_SELECTOR,
    "#page-right > div > div.card-container__wrapper > div > form > div.register-form__address > div > div > span.rt-input__placeholder")
    password = (By.ID, "password")
    password_placeholder = (By.CSS_SELECTOR,
    "#page-right > div > div.card-container__wrapper > div > form > div.new-password-container > div.rt-input-container.new-password-container__password > div > span.rt-input__placeholder")
    password_confirm = (By.ID, "password-confirm")
    password_confirm_placeholder = (By.CSS_SELECTOR,
    "#page-right > div > div.card-container__wrapper > div > form > div.new-password-container > div.rt-input-container.new-password-container__confirmed-password > div > span.rt-input__placeholder")
    eye_icon_password = (By.CSS_SELECTOR,
    "#page-right > div > div.card-container__wrapper > div > form > div.new-password-container > div.rt-input-container.rt-input-container--error.new-password-container__password > div > div.rt-input__action > svg")
    eye_icon_password_confirm = (By.CSS_SELECTOR,
    "#page-right > div > div.card-container__wrapper > div > form > div.new-password-container > div.rt-input-container.rt-input-container--error.new-password-container__confirmed-password > div > div.rt-input__action > svg")
    register_button = (By.CLASS_NAME, "register-form__reg-btn")
    error_locator = (By.CLASS_NAME, "rt-input-container__meta--error")
    page_left = (By.ID, "page-left")
    account_exists_error = (By.CSS_SELECTOR,
    "#page-right > div > div.card-container__wrapper > div > form > div.base-modal-wrapper.card-modal > div > div > h2")
    registration_email_confirmation = (By.CSS_SELECTOR, '#page-right > div > div > h1')