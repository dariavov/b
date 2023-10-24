from locators.register_page_locators import RegisterPageLocators
from settings.keys import *




class ExpectedResults:
    """Stores conditions and expected results for each of the variables used in the tests"""
    placeholders = [
        (RegisterPageLocators.first_name, RegisterPageLocators.first_name_placeholder,
         'rt-input__placeholder--top', 'rgba(255, 79, 18, 1)'),
        (RegisterPageLocators.last_name, RegisterPageLocators.last_name_placeholder,
         'rt-input__placeholder--top', 'rgba(255, 79, 18, 1)'),
        (RegisterPageLocators.address, RegisterPageLocators.address_placeholder,
         'rt-input__placeholder--top', 'rgba(255, 79, 18, 1)'),
        (RegisterPageLocators.password, RegisterPageLocators.password_placeholder,
         'rt-input__placeholder--top', 'rgba(255, 79, 18, 1)'),
        (RegisterPageLocators.password_confirm, RegisterPageLocators.password_confirm_placeholder,
         'rt-input__placeholder--top', 'rgba(255, 79, 18, 1)')
        ]
    negative_inputs = [
        (RegisterPageLocators.first_name, RegistrationInputs.one_letter_russian_name),
        (RegisterPageLocators.first_name, RegistrationInputs.thirty_one_letter_russian_name),
        (RegisterPageLocators.first_name, RegistrationInputs.four_letters_english_name),
        (RegisterPageLocators.first_name, RegistrationInputs.four_letters_hebrew_name),
        (RegisterPageLocators.first_name, RegistrationInputs.four_letters_chinese_name),
        (RegisterPageLocators.first_name, RegistrationInputs.ten_special_chars_name),
        (RegisterPageLocators.first_name, RegistrationInputs.ten_numbers_name),
        (RegisterPageLocators.first_name, RegistrationInputs.blank_space_name),
        (RegisterPageLocators.last_name, RegistrationInputs.one_letter_russian_name),
        (RegisterPageLocators.last_name, RegistrationInputs.thirty_one_letter_russian_name),
        (RegisterPageLocators.last_name, RegistrationInputs.four_letters_english_name),
        (RegisterPageLocators.last_name, RegistrationInputs.four_letters_hebrew_name),
        (RegisterPageLocators.last_name, RegistrationInputs.four_letters_chinese_name),
        (RegisterPageLocators.last_name, RegistrationInputs.ten_special_chars_name),
        (RegisterPageLocators.last_name, RegistrationInputs.ten_numbers_name),
        (RegisterPageLocators.last_name, RegistrationInputs.blank_space_name),
        (RegisterPageLocators.address, RegistrationInputs.incorrect_number_one),
        (RegisterPageLocators.address, RegistrationInputs.incorrect_number_two),
        (RegisterPageLocators.address, RegistrationInputs.incorrect_number_three),
        (RegisterPageLocators.address, RegistrationInputs.twelve_special_chars_number),
        (RegisterPageLocators.address, RegistrationInputs.blank_space_number),
        (RegisterPageLocators.address, RegistrationInputs.russian_email),
        (RegisterPageLocators.address, RegistrationInputs.numbered_email),
        (RegisterPageLocators.address, RegistrationInputs.chinese_email),
        (RegisterPageLocators.password, RegistrationInputs.five_chars_password),
        (RegisterPageLocators.password, RegistrationInputs.seven_chars_password),
        (RegisterPageLocators.password, RegistrationInputs.twenty_one_chars_password),
        (RegisterPageLocators.password, RegistrationInputs.all_lower_case_password),
        (RegisterPageLocators.password, RegistrationInputs.all_capital_letters_password),
        (RegisterPageLocators.password, RegistrationInputs.no_special_chars_password),
        (RegisterPageLocators.password, RegistrationInputs.russian_password),
        (RegisterPageLocators.password, RegistrationInputs.chinese_password),
        (RegisterPageLocators.password, RegistrationInputs.hebrew_password)
    ]
    positive_inputs = [
        (RegisterPageLocators.first_name, RegistrationInputs.three_letters_russian_name),
        (RegisterPageLocators.first_name, RegistrationInputs.twenty_nine_letters_russian_name),
        (RegisterPageLocators.first_name, RegistrationInputs.thirty_letters_russian_name),
        (RegisterPageLocators.last_name, RegistrationInputs.three_letters_russian_name),
        (RegisterPageLocators.last_name, RegistrationInputs.twenty_nine_letters_russian_name),
        (RegisterPageLocators.last_name, RegistrationInputs.thirty_letters_russian_name),
        (RegisterPageLocators.address, RegistrationInputs.correct_number_one),
        (RegisterPageLocators.address, RegistrationInputs.correct_number_two),
        (RegisterPageLocators.address, RegistrationInputs.correct_email),
        (RegisterPageLocators.password, RegistrationInputs.eight_chars_password),
        (RegisterPageLocators.password, RegistrationInputs.nine_chars_password),
        (RegisterPageLocators.password, RegistrationInputs.nineteen_chars_password),
        (RegisterPageLocators.password, RegistrationInputs.twenty_chars_password)
    ]
    existing_email = [
        (RegisterPageLocators.first_name, RegisterPageLocators.last_name, RegistrationInputs.three_letters_russian_name,
         RegisterPageLocators.address, UsernameKeys.valid_email, RegisterPageLocators.password,
         RegisterPageLocators.password_confirm, RegistrationInputs.eight_chars_password, 'Учётная запись уже существует')
    ]
    valid_credentials = [
        (RegisterPageLocators.first_name, RegisterPageLocators.last_name, RegistrationInputs.three_letters_russian_name,
         RegisterPageLocators.address, RegistrationInputs.correct_email, RegisterPageLocators.password,
         RegisterPageLocators.password_confirm, RegistrationInputs.eight_chars_password, 'Подтверждение email')
    ]
    eye_icon = [
        ('invisible', RegisterPageLocators.password, RegistrationInputs.eight_chars_password,
         RegisterPageLocators.eye_icon_password, '........'),
        ('visible', RegisterPageLocators.password, RegistrationInputs.eight_chars_password,
         RegisterPageLocators.eye_icon_password, RegistrationInputs.eight_chars_password),
        ('invisible', RegisterPageLocators.password_confirm, RegistrationInputs.eight_chars_password,
         RegisterPageLocators.eye_icon_password_confirm, '........'),
        ('visible', RegisterPageLocators.password_confirm, RegistrationInputs.eight_chars_password,
         RegisterPageLocators.eye_icon_password_confirm, RegistrationInputs.eight_chars_password)
    ]
    region_dropdown = [
        ('Амурская обл'),
        ('Свердловская обл'),
        ('Чукотский АО')
    ]
    new_registration = [
        (RegistrationInputs.three_letters_russian_name, 5200048, RegistrationInputs.correct_email,
         RegistrationInputs.eight_chars_password, 200)
    ]
