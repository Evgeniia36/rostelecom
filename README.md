### Автоматизированное тестирование формы авторизации [Ростелеком](https://lk.rt.ru/)
Папка *tests* содержит файл с тестами - **test_rostelecom.py**. Файл содержит позитивные и негативные тесты для полей формы авторизации. Первые три теста осуществляют успешную авторизацию на сайте, поэтому после них браузер закрывается (чтобы очистить данные для следующего теста). Негативные тесты проходят одном браузере, который закрывается по выполнении всех тестов. Файл **conftest.py** содержит фикстуры.

В папке *utils* хранится вебдрайвер для браузера GoogleChrome
В папке *pages* содержатся объекты страницы авторизации и страницы личного кабинета. Внутри заданы класс и методы для взаимодействия с элементами страницы, используемые при тестировании.

Для запуска тестов потребуется установить на компьютер Python3.

Далее необходимо установить фреймворк Pytest для тестирования: `pip3 install pytest`

и Selenium для автоматизации: `pip3 install selenium`

Запуск тестов осуществляется с помощью команды: `pytest test_rostelecom.py` из каталога, где находится файл с тестами и pytest.

### Возможные проблемы:
Сайт может заблокировать выполнение тестов из-за большого количества обращений за короткий промежуток времени.
