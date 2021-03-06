import allure
import pytest

incorrect_data_for_login = [('test1', 'test'),
                            ('test', 'test1'),
                            ('test1', 'test1')]


@allure.feature('Login')
class TestLogin:

    @allure.title('Check login title')
    def test_login_title(self, browser, login_page):
        # тест падает из-за опечатки в заголовке
        title = login_page.driver.title
        assert title == 'Welcome to Propeller Automated Testing Championship'

    @allure.title('Login with correct data')
    def test_login_with_correct_data(self, login_page):
        client_page = login_page.login('test', 'test')
        client_page.check_articles_exist()

    @allure.title('Login with incorrect data')
    @pytest.mark.parametrize('login, password', incorrect_data_for_login)
    def test_login_with_incorrect_login(self, login_page, browser, login, password):
        login_page.login(login, password)
        browser.refresh()
        login_page.check_welcome_login_text()
