import pytest
from selenium import webdriver
from pages.rostelecom_auth_page import RostelecomAuthPage
from pages.rt_personal_account_page import RtPersonalAccountPage

@pytest.fixture(scope='session')
def chrome_driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('executable_path=utils\\chromedriver.exe')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver

@pytest.fixture
def chrome_driver_quit(request):
    options = webdriver.ChromeOptions()
    options.add_argument('executable_path=utils\\chromedriver.exe')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver

@pytest.fixture(scope='function')
def rt_auth_page(chrome_driver):
    # Создаем экземпляр класса RostelecomAuthPage
    return RostelecomAuthPage(chrome_driver)

@pytest.fixture(scope='function')
def rt_auth_page_quit(chrome_driver_quit):
    # Создаем экземпляр класса RostelecomAuthPage
    return RostelecomAuthPage(chrome_driver_quit)

@pytest.fixture(scope='function')
def rt_account_page(chrome_driver_quit):
    # Создаем экземпляр класса RtPersonalAccountPage
    return RtPersonalAccountPage(chrome_driver_quit)
