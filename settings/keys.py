from faker import Faker

faker = Faker('ru_RU')

class UsernameKeys:
    """Stores all usernames available for testing"""
    random_telephone = faker.numerify('7##########')
    random_email = faker.email()
    random_ls = faker.numerify('############')
    random_login = faker.user_name()
    valid_email = "wet05956@zslsz.com"
    valid_login = "Romario"

class PasswordKeys:
    """Stores all passwords available for testing"""
    random_password = faker.password()
    valid_password = 'B/#-ds4wS3Mg-GK'

class RegistrationInputs:
    """Stores inputs for the Registration page"""
    one_letter_russian_name = 'й'
    two_letters_russian_name = 'ое'
    three_letters_russian_name = 'йки'
    twenty_nine_letters_russian_name = 'фсцбуийфгбнмлпойчгфсшыгчтдрсп'
    thirty_letters_russian_name = 'фсцбуийфгбнмлпойчгфсшыкгчтдрсп'
    thirty_one_letter_russian_name = 'фсцбуийфгбнмлпойчгфсшыгчтдрсппл'
    four_letters_english_name = 'Toni'
    four_letters_hebrew_name = 'נועם'
    four_letters_chinese_name = '淑兰俊畅'
    ten_special_chars_name = '#$%^##$*(!'
    ten_numbers_name = faker.numerify('##########')
    blank_space_name = ' '
    correct_number_one = faker.numerify('+7##########')
    correct_number_two = faker.numerify('+375#########')
    incorrect_number_one = faker.numerify('7##########')
    incorrect_number_two = faker.numerify('8##########')
    incorrect_number_three = faker.numerify('375#########')
    twelve_special_chars_number = '#$%^##$*(!*@'
    blank_space_number = ' '
    correct_email = faker.email()
    russian_email = 'дйгфкадф@email.ru'
    numbered_email = '58356379693@email.ru'
    chinese_email = '淑兰俊畅@email.ru'
    five_chars_password = 'hfkH1'
    seven_chars_password = 'hfkH1kq'
    eight_chars_password = 'hfkH1kqa'
    nine_chars_password = 'hfkH1kqal'
    nineteen_chars_password = 'hfkH1kqa567gsrfcnpg'
    twenty_chars_password = 'hfkH1kqa567gsrfcnpgk'
    twenty_one_chars_password = 'hfkH1kqa567gsrfcnpgk2'
    all_lower_case_password = 'hfkh1kqagfjf'
    all_capital_letters_password = 'HFKH1KQAGFJF'
    no_special_chars_password = 'hfkhGkqagfjf'
    russian_password = 'кфгчкфгЧ00'
    chinese_password = '淑兰俊畅淑兰俊畅56'
    hebrew_password = 'נועםנועם547'





