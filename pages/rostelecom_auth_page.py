from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RostelecomAuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://lk.rt.ru/'

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def open(self):
        """Открытие главной страницы"""
        self.driver.get(self.base_url)

    def wait_for_element(self, by, value, timeout=10):
        """Ожидание загрузки определённого элемента"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def wait_for_element_visible(self, by, value, timeout=10):
        """Ожидание загрузки и видимости определённого элемента"""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))

    def get_current_url(self):
        """URL текущей страницы"""
        return self.driver.current_url

    def click_standard_auth_button(self):
        """Нажатие на кнопку 'Войти с паролем'"""
        standard_auth_button = self.wait_for_element(By.XPATH, '//button[@id="standard_auth_btn"]')
        standard_auth_button.click()

    def hint_message(self):
        """Ожидание появления подсказки/сообщения об ошибке ввода"""
        return self.wait_for_element(By.XPATH, '//div/span[@class="rt-input-container__meta rt-input-container__meta--error"]')

    def error_message(self):
        """Ожидание появления ошибки 'Неверный логин или пароль'"""
        return self.wait_for_element_visible(By.ID, 'form-error-message')

    def mail_tab(self):
        """Вкладка 'Почта'"""
        return self.wait_for_element(By.XPATH, '//div[@id="t-btn-tab-mail"]')

    def active_tab_class(self):
        """Когда вкладка телефон/почта/логин/лиц.счёт активна, она имеет класс:"""
        active_tab_class = "rt-tab--active"
        return active_tab_class

    def login_tab(self):
        """Вкладка 'Логин'"""
        return self.wait_for_element(By.XPATH, '//div[@id="t-btn-tab-login"]')

    def click_phone_tab(self):
        """Клик по вкладке 'Телефон'"""
        phone_tab = self.wait_for_element(By.XPATH, '//div[@id="t-btn-tab-phone"]')
        phone_tab.click()

    def click_mail_tab(self):
        """Клик по вкладке 'Почта'"""
        mail_tab = self.wait_for_element(By.XPATH, '//div[@id="t-btn-tab-mail"]')
        mail_tab.click()

    def click_login_tab(self):
        """Клик по вкладке 'Логин'"""
        login_tab = self.wait_for_element(By.XPATH, '//div[@id="t-btn-tab-login"]')
        login_tab.click()

    def click_account_number_tab(self):
        """Клик по вкладке 'Лицевой счёт'"""
        account_number_tab = self.wait_for_element(By.XPATH, '//div[@id="t-btn-tab-ls"]')
        account_number_tab.click()

    def input_username(self, keyword):
        """Ввод телефона/почты/логина/лиц.счёта в зависимости от выбранной вкладки"""
        username = self.wait_for_element(By.XPATH, '//input[@id="username"]')
        username.clear()
        username.send_keys(keyword)

    def input_password(self, keyword):
        """Ввод пароля"""
        password = self.wait_for_element(By.XPATH, '//input[@id="password"]')
        password.clear()
        password.send_keys(keyword)

    def click_password(self):
        """Установить курсор в поле ввода пароля"""
        password = self.wait_for_element(By.XPATH, '//input[@id="password"]')
        password.click()

    def click_login_button(self):
        """Нажатие на кнопку 'Войти'"""
        login_button = self.wait_for_element(By.XPATH, '//button[@id="kc-login"]')
        login_button.click()

