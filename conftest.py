import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, DesiredCapabilities

from Pages.login_page import LoginPage
from Pages.clients_page import ClientsPage


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='Chrome',
        help='Testing browser'
    )
    parser.addoption(
        '--url',
        default='http://localhost:8080/',
        help='Testing url'
    )


@pytest.fixture
def login_page(browser):
    page = LoginPage(browser)
    page.go_to()
    return page


@pytest.fixture
def main_page(login_page):
    return login_page.login('test', 'test')


@pytest.fixture
def clients_page(browser):
    page = ClientsPage(browser)
    page.go_to()
    browser.add_cookie({"name": "secret", "value": "IAmSuperSeleniumMaster"})
    browser.refresh()
    return page


# @pytest.fixture
# def profile_page(browser):
#     page = ProfilePage(browser)
#     page.go_to()
#     return page


@pytest.fixture
def browser_name(request):
    return request.config.getoption('--browser')


@pytest.fixture()
def url(request):
    return request.config.getoption('--url')


@pytest.fixture()
def browser(browser_name):
    driver = ''
    if browser_name == 'Chrome':
        caps = DesiredCapabilities.CHROME
        options = ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--ignore-certificate-errors')
        # options.add_experimental_option('w3c', False)
        caps['loggingPrefs'] = {'performance': 'ALL', 'browser': 'ALL'}
        driver = webdriver.Chrome(options=options, desired_capabilities=caps)
        driver.implicitly_wait(5)

    elif browser_name == 'Firefox':
        options = FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(5)

    elif browser_name == 'Safari':
        driver = webdriver.Safari()
        driver.implicitly_wait(5)

    else:
        pass

    allure.attach(name=driver.session_id,
                  body=str(driver.desired_capabilities),
                  attachment_type=allure.attachment_type.JSON)

    yield driver
    driver.quit()
