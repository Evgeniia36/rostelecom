import time
import pytest
from pages.rostelecom_auth_page import RostelecomAuthPage
from pages.rt_personal_account_page import RtPersonalAccountPage
from selenium.webdriver.common.by import By

def test_successful_auth_by_email(chrome_driver_quit, rt_auth_page_quit, rt_account_page):
    """Проверка успешной авторизации по почте и паролю"""
    rt_auth_page_quit.open()
    rt_auth_page_quit.click_standard_auth_button()
    rt_auth_page_quit.click_mail_tab()
    rt_auth_page_quit.input_username('testuser.vers2@gmail.com')
    rt_auth_page_quit.input_password('Testuser2')
    rt_auth_page_quit.click_login_button()

    # Ожидание загрузки личного кабинета
    rt_account_page.wait_while_loading()

    assert rt_account_page.base_url in rt_auth_page_quit.get_current_url()

def test_successful_auth_by_email_uppercase(chrome_driver_quit, rt_auth_page_quit, rt_account_page):
    """Проверка успешной авторизации по почте, написанной заглавными буквами"""
    rt_auth_page_quit.open()
    rt_auth_page_quit.click_standard_auth_button()
    rt_auth_page_quit.click_mail_tab()
    rt_auth_page_quit.input_username('TESTUSER.VERS2@GMAIL.COM')
    rt_auth_page_quit.input_password('Testuser2')
    rt_auth_page_quit.click_login_button()

    # Ожидание загрузки личного кабинета
    rt_account_page.wait_while_loading()
    assert rt_account_page.base_url in rt_auth_page_quit.get_current_url()

def test_successful_auth_by_login(chrome_driver_quit, rt_auth_page_quit, rt_account_page):
    """Проверка успешной авторизации по логину и паролю"""
    rt_auth_page_quit.open()
    rt_auth_page_quit.click_standard_auth_button()
    rt_auth_page_quit.click_login_tab()
    rt_auth_page_quit.input_username('rtkid_1697706924566')
    rt_auth_page_quit.input_password('Testuser2')
    rt_auth_page_quit.click_login_button()

    # Ожидание загрузки личного кабинета
    rt_account_page.wait_while_loading()

    assert rt_account_page.base_url in rt_auth_page_quit.get_current_url()


# Негативное тестирование вкладки Телефон

def test_empty_phone(chrome_driver, rt_auth_page):
    """Пустое значение в поле Мобильный телефон вызывает появление подсказки ввода"""

    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_phone_tab()
    rt_auth_page.input_username('')
    rt_auth_page.input_password('Testuser2')
    rt_auth_page.click_login_button()

    # Ожидание появления подсказки и получение его текста
    error_text = rt_auth_page.hint_message().text

    assert "телефон" or "символ" or "введите" in error_text.lower(), f"Cообщение об ошибке: {error_text}"

def test_invalid_phone_cyrillic(chrome_driver, rt_auth_page):
    """Кириллица в поле Мобильный телефон активирует вкладку входа по логину и паролю"""

    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_phone_tab()
    rt_auth_page.input_username('76впыЙу')
    rt_auth_page.click_password()

    # Проверка, что теперь вкладка Логин активна
    login_tab = rt_auth_page.login_tab()
    login_tab_class = login_tab.get_attribute("class")

    assert rt_auth_page.active_tab_class() in login_tab_class.split()

def test_invalid_phone_latin(chrome_driver, rt_auth_page):
    """Лотиница в поле Мобильный телефон активирует вкладку входа по логину и паролю"""

    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_phone_tab()
    rt_auth_page.input_username('ki89urD')
    rt_auth_page.click_password()

    # Проверка, что теперь вкладка Логин активна
    login_tab = rt_auth_page.login_tab()
    login_tab_class = login_tab.get_attribute("class")

    assert rt_auth_page.active_tab_class() in login_tab_class.split()

def test_invalid_phone_email(chrome_driver, rt_auth_page):
    """Адрес электронной почты в поле Мобильный телефон активирует вкладку входа по почте и паролю"""

    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_phone_tab()
    rt_auth_page.input_username('testuser.vers2@gmail.com')
    rt_auth_page.click_password()

    # Проверка, что теперь вкладка Почта активна
    mail_tab_class = rt_auth_page.mail_tab().get_attribute("class")

    assert rt_auth_page.active_tab_class() in mail_tab_class.split()

def test_invalid_phone_short(chrome_driver, rt_auth_page):
    """При вводе слишком короткого значения в поле Мобильный телефон выводится подсказка/сообщение
    об ошибке ввода"""

    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_phone_tab()
    rt_auth_page.input_username('0')
    rt_auth_page.click_password()

    # Ожидание появления подсказки и получение его текста
    error_text = rt_auth_page.hint_message().text

    assert "телефон" or "символ" or "введите" in error_text.lower(), f"Cообщение об ошибке: {error_text}"


# Негативное тестирование вкладки Почта

def test_unsuccessful_auth_by_email_wrong_password(chrome_driver, rt_auth_page, rt_account_page):
    """Проверка, что ввод неверного пароля вызывает сообщение об ошибке"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_mail_tab()
    rt_auth_page.input_username('testuser.vers2@gmail.com')
    rt_auth_page.input_password('testuser')
    rt_auth_page.click_login_button()

    # Ожидание сообщения об ошибке
    error_message = rt_auth_page.error_message()

    assert error_message.is_displayed()

def test_unsuccessful_auth_by_email_wrong_email(chrome_driver, rt_auth_page, rt_account_page):
    """Проверка, что ввод неверной электронной почты вызывает сообщение об ошибке"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_mail_tab()
    rt_auth_page.input_username('testuser@gmail.com')
    rt_auth_page.input_password('Testuser2')
    rt_auth_page.click_login_button()

    # Ожидание сообщения об ошибке
    error_message = rt_auth_page.error_message()

    assert error_message.is_displayed()

def test_empty_password(chrome_driver, rt_auth_page):
    """Пустое значение в поле пароль вызывает подсказку/сообщение об ошибке ввода.
    'Длина пароля от 8 до 20 символов' или 'Введите действующий пароль'"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_mail_tab()
    rt_auth_page.input_username('testuser@gmail.com')
    rt_auth_page.input_password('')
    rt_auth_page.click_login_button()

    # Ожидание появления подсказки и получение его текста
    error_text = rt_auth_page.hint_message().text

    assert "парол" or "введите" or "символ" in error_text.lower(), f"Cообщение об ошибке: {error_text}"

def test_invalid_password_too_long(chrome_driver, rt_auth_page):
    """Слишком длинное значение в поле пароль вызывает подсказку/сообщение об ошибке ввода.
    'Превышена допустимая длина пароля' или 'Введите действующий пароль'"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_mail_tab()
    rt_auth_page.input_username('testuser@gmail.com')
    rt_auth_page.input_password('ierxtvcmbxtikpsqcgnqytysihpximclmfgoxncgyxigotpwtuxdxcoeukookxoxbifhhgaycrbboryrbdiqthpqzadlabsnaqwqzrjjsvvfnyishfslyfrdqzvgegznzyjvtcuuazoxbkccmqvrsceempqmlfbkjmeafszncpafxsvviodxbplnjcvqnoyatrtaygujhqyltrtgkkbbwcfanlstnjvqxndusbdjemgxeeqggpxludltccknvksnmpazxvkjdhcjbukoociesrcghtwjuedvtqdtcdnbeozhjqntnomyifjwwlzmxxfyprvadfgxknig')
    rt_auth_page.click_login_button()

    # Ожидание появления подсказки и получение его текста
    error_text = rt_auth_page.hint_message().text

    assert "парол" or "превышен" or "лимит" in error_text.lower(), f"Cообщение об ошибке: {error_text}"

def test_empty_email(chrome_driver, rt_auth_page):
    """Пустое значение в поле почты вызывает подсказку/сообщение об ошибке ввода"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_mail_tab()
    rt_auth_page.input_username('')
    rt_auth_page.input_password('Testuser2')
    rt_auth_page.click_login_button()

    # Ожидание появления подсказки и получение его текста
    error_text = rt_auth_page.hint_message().text

    assert "почт" or "адрес" in error_text.lower(), f"Cообщение об ошибке: {error_text}"

def test_valid_email_symbols(chrome_driver, rt_auth_page):
    """Валидное значение в поле почты - разрешённые символы. Пользователь остаётся на вкладке Почта"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_mail_tab()
    rt_auth_page.input_username('!#$%&*+_.98@b-1.0-h.c')
    rt_auth_page.click_password()

    # Проверка, что вкладка Почта активна
    mail_tab = rt_auth_page.mail_tab()
    mail_tab_class = mail_tab.get_attribute("class")

    assert rt_auth_page.active_tab_class() in mail_tab_class.split()

def test_invalid_email_no_username(chrome_driver, rt_auth_page):
    """Невалидное значение в поле почты - нет username. Автоматический переход на вкладку Логин"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_mail_tab()
    rt_auth_page.input_username('@b.c')
    rt_auth_page.click_password()

    # Проверка, что теперь вкладка Логин активна
    login_tab = rt_auth_page.login_tab()
    login_tab_class = login_tab.get_attribute("class")

    assert rt_auth_page.active_tab_class() in login_tab_class.split()

def test_invalid_email_no_at(chrome_driver, rt_auth_page):
    """Невалидное значение в поле почты - нет @. Автоматический переход на вкладку Логин"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_mail_tab()
    rt_auth_page.input_username('ab.c')
    rt_auth_page.click_password()

    # Проверка, что теперь вкладка Логин активна
    login_tab = rt_auth_page.login_tab()
    login_tab_class = login_tab.get_attribute("class")

    assert rt_auth_page.active_tab_class() in login_tab_class.split()

def test_invalid_email_no_hostname(chrome_driver, rt_auth_page):
    """Невалидное значение в поле почты - нет hostname. Автоматический переход на вкладку Логин"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_mail_tab()
    rt_auth_page.input_username('a@.c')
    rt_auth_page.click_password()

    # Проверка, что теперь вкладка Логин активна
    login_tab = rt_auth_page.login_tab()
    login_tab_class = login_tab.get_attribute("class")

    assert rt_auth_page.active_tab_class() in login_tab_class.split()

def test_invalid_email_no_dot(chrome_driver, rt_auth_page):
    """Невалидное значение в поле почты - нет точки. Автоматический переход на вкладку Логин"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_mail_tab()
    rt_auth_page.input_username('a@bc')
    rt_auth_page.click_password()

    # Проверка, что теперь вкладка Логин активна
    login_tab = rt_auth_page.login_tab()
    login_tab_class = login_tab.get_attribute("class")

    assert rt_auth_page.active_tab_class() in login_tab_class.split()

def test_invalid_email_no_dom(chrome_driver, rt_auth_page):
    """Невалидное значение в поле почты - нет домена первого уровня. Автоматический переход на вкладку Логин"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_mail_tab()
    rt_auth_page.input_username('a@b.')
    rt_auth_page.click_password()

    # Проверка, что теперь вкладка Логин активна
    login_tab = rt_auth_page.login_tab()
    login_tab_class = login_tab.get_attribute("class")

    assert rt_auth_page.active_tab_class() in login_tab_class.split()

def test_invalid_email_space(chrome_driver, rt_auth_page):
    """Невалидное значение в поле почты - пробел. Автоматический переход на вкладку Логин"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_mail_tab()
    rt_auth_page.input_username('a@b 1.c')
    rt_auth_page.click_password()

    # Проверка, что теперь вкладка Логин активна
    login_tab = rt_auth_page.login_tab()
    login_tab_class = login_tab.get_attribute("class")

    assert rt_auth_page.active_tab_class() in login_tab_class.split()

def test_invalid_email_cyrillic(chrome_driver, rt_auth_page):
    """Невалидное значение в поле почты - кириллица. Автоматический переход на вкладку Логин"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_mail_tab()
    rt_auth_page.input_username('дерево@b.c')
    rt_auth_page.click_password()

    # Проверка, что теперь вкладка Логин активна
    login_tab = rt_auth_page.login_tab()
    login_tab_class = login_tab.get_attribute("class")

    assert rt_auth_page.active_tab_class() in login_tab_class.split()

def test_invalid_email_symbols(chrome_driver, rt_auth_page):
    """Невалидное значение в поле почты - запрещённые символы. Автоматический переход на вкладку Логин"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_mail_tab()
    rt_auth_page.input_username('a<>d@b.c')
    rt_auth_page.click_password()

    # Проверка, что теперь вкладка Логин активна
    login_tab = rt_auth_page.login_tab()
    login_tab_class = login_tab.get_attribute("class")

    assert rt_auth_page.active_tab_class() in login_tab_class.split()

def test_invalid_email_too_long(chrome_driver, rt_auth_page):
    """Слишком длинное значение в поле почты вызывает подсказку/сообщение об ошибке ввода.
    'Превышена допустимая длина электронной почты' или 'Неверная электронная почта'"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_mail_tab()
    rt_auth_page.input_username('ierxtvcmbxtikpsqcgnqytysihpximclmfgoxncgyxigotpwtuxdxcoeukookxoxbifhhgaycrbboryrbdiqthpqzadlabsnaqwqzrjjsvvfnyishfslyfrdqzvgegznzyjvtcuuazoxbkccmqvrsceempqmlfbkjmeafszncpafxsvviodxbplnjcvqnoyatrtaygujhqyltrtgkkbbwcfanlstnjvqxndusbdjemgxeeqggpxludltccknvksnmpazxvkjdhcjbukoociesrcghtwjuedvtqdtcdnbeozhjqntnomyifjwwlzmxxfyprvagxknig@b.com')
    rt_auth_page.click_password()

    # Ожидание появления подсказки и получение его текста
    error_text = rt_auth_page.hint_message().text

    assert "почт" or "адрес" or "превышен" or "лимит" in error_text.lower(), f"Cообщение об ошибке: {error_text}"

# Негативное тестирование вкладки Логин

def test_unsuccessful_auth_by_login_wrong_password(chrome_driver, rt_auth_page, rt_account_page):
    """Проверка, что ввод неверного пароля вызывает сообщение об ошибке"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_login_tab()
    rt_auth_page.input_username('rtkid_1697706924566')
    rt_auth_page.input_password('testuser')
    rt_auth_page.click_login_button()

    # Ожидание сообщения об ошибке
    error_message = rt_auth_page.error_message()

    assert error_message.is_displayed()

def test_unsuccessful_auth_by_login_wrong_login(chrome_driver, rt_auth_page, rt_account_page):
    """Проверка, что ввод неверного логина вызывает сообщение об ошибке"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_login_tab()
    rt_auth_page.input_username('rtkid_16')
    rt_auth_page.input_password('Testuser2')
    rt_auth_page.click_login_button()

    # Ожидание сообщения об ошибке
    error_message = rt_auth_page.error_message()

    assert error_message.is_displayed()

def test_empty_login(chrome_driver, rt_auth_page):
    """Пустое значение в поле логина вызывает подсказку/сообщение об ошибке ввода"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_login_tab()
    rt_auth_page.input_username('')
    rt_auth_page.input_password('Testuser2')
    rt_auth_page.click_login_button()

    # Ожидание появления подсказки и получение его текста
    error_text = rt_auth_page.hint_message().text

    assert "введите" or "логин" in error_text.lower(), f"Cообщение об ошибке: {error_text}"

def test_invalid_login_too_long(chrome_driver, rt_auth_page):
    """Слишком длинное значение в поле логин вызывает подсказку/сообщение об ошибке ввода.
    'Превышена допустимая длина' или 'Неверный логин' или 'Превышен лимит символов'"""
    rt_auth_page.open()
    rt_auth_page.click_standard_auth_button()
    rt_auth_page.click_login_tab()
    rt_auth_page.input_username('ierxtvcmbxtikpsqcgnqytysihpximclmfgoxncgyxigotpwtuxdxcoeukookxoxbifhhgaycrbboryrbdiqthpqzadlabsnaqwqzrjjsvvfnyishfslyfrdqzvgegznzyjvtcuuazoxbkccmqvrsceempqmlfbkjmeafszncpafxsvviodxbplnjcvqnoyatrtaygujhqyltrtgkkbbwcfanlstnjvqxndusbdjemgxeeqggpxludltccknvksnmpazxvkjdhcjbukoociesrcghtwjuedvtqdtcdnbeozhjqntnomyifjwwlzmxxfyprvadfgxknig')
    rt_auth_page.click_password()

    # Ожидание появления подсказки и получение его текста
    error_text = rt_auth_page.hint_message().text

    assert "логин" or "превышен" or "лимит" in error_text.lower(), f"Cообщение об ошибке: {error_text}"


