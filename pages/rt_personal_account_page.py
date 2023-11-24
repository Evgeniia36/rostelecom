from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RtPersonalAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://start.rt.ru/'

    def wait_for_element(self, by, value, timeout=10):
        """Ожидание загрузки определённого элемента"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def wait_for_element_clickable(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
    def wait_while_loading(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="StyledHeaderMenuItem-gjPccJ eCvOFK"]'))
        )

    def click_name(self):
        """Нажатие на имя пользователя"""
        name = self.wait_for_element(By.XPATH, '//div[@class="sc-emDsmM ccJkbA"]')
        name.click()

    def click_log_out(self):
        """Нажатие на кнопку 'Выйти'"""
        log_out_button = self.wait_for_element_clickable(By.XPATH, '//span[@class="sc-dkPtRN lgHXyI sc-dlVxhl bLVPuw"]')
        log_out_button.click()
