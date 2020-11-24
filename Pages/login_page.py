import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from .base import BasePage
from .clients_page import ClientsPage


class LoginPage(BasePage):
    login_field = (By.CSS_SELECTOR, '[onclick="startInputLogin()"]')
    password_field = (By.CSS_SELECTOR, '[onclick="startInputPassword()"]')

    login_input = (By.ID, 'loginInput')
    password_input = (By.ID, 'passwordInput')

    submit_btn = (By.XPATH, '//*[@id="registrationContainer"]/div/div[3]/button[2]')
    sign_in_btn = (By.XPATH, '//*[@id="registrationContainer"]/div/div[3]/div/img')

    welcome = (By.CSS_SELECTOR, '[class="card-header "]')

    def __init__(self, driver):
        super().__init__(driver)

    def _set_username_(self, name):
        with allure.step("Enter name {}".format(name)):
            self.find_element(locator=self.login_field).click()
            self.find_element(locator=self.login_input).send_keys(name)

    def _set_password_(self, password):
        with allure.step("Enter password {}".format(password)):
            self.find_element(locator=self.password_field).click()
            self.find_element(locator=self.password_input).send_keys(password)

    def _accept_all_alerts(self):
        with allure.step("Accepting alerts"):
            Alert(self.driver).accept()
            self.wait_for_alert()
            Alert(self.driver).accept()

    def _click_sign_in_button(self):
        with allure.step("Waiting for sign in button and click"):
            button = self.find_element(locator=self.submit_btn)
            hover = ActionChains(self.driver).move_to_element(button)
            hover.perform()
            self.wait_for_element(self.sign_in_btn).click()

    def check_welcome_login_text(self):
        with allure.step("Checking title of login page"):
            text = self.get_text_in_element(self.welcome)
            assert text == 'Welcome to Propeller Championship!'

    def login(self, username, password):
        with allure.step("Login"):
            self._set_username_(username)
            self._set_password_(password)
            self._click_sign_in_button()
            self._accept_all_alerts()
            return ClientsPage(self.driver)
