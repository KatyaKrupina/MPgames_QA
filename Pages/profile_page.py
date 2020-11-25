import allure
from selenium.webdriver.common.by import By

from Pages.base import BasePage


class ProfilePage(BasePage):
    user_img = (By.ID, 'avatar')
    user_header = (By.CSS_SELECTOR, '[class="card-header text-center"]')

    first_name_input = (By.ID, 'firstNameInput')
    last_name_input = (By.ID, 'lastNameInput')
    card_number_input = (By.ID, 'cardNumberInput')
    payment_system = (By.ID, 'paymentSystemSelect')

    save_user_info_btn = (By.CSS_SELECTOR, '[onclick="saveUserInfo()"]')

    error = (By.CSS_SELECTOR, '[class ="invalid-feedback"]')

    success_info = (By.ID, 'successUserInfoSaveInfo')
    payment_info = (By.ID, 'v-pills-messages-tab')

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "http://localhost:8080/profile.html"

    def show_profile(self):
        with allure.step('Show profile'):
            self.find_element(self.user_img).click()
            assert self.get_text_in_element(self.user_header) == 'User profile settings'

    def set_user_first_name(self, name):
        with allure.step(f'Setting user first name {name}'):
            self.find_element(self.first_name_input).send_keys(name)

    def set_user_last_name(self, name):
        with allure.step(f'Setting user last name {name}'):
            self.find_element(self.last_name_input).send_keys(name)

    def click_save_button(self):
        with allure.step('Clicking save button'):
            self.find_element(self.save_user_info_btn).click()

    def save_user_info(self):
        with allure.step('Saving info'):
            self.click_save_button()
            success = self.find_element(self.success_info)
            assert success.is_displayed() is True

    def _check_error(self, error_index, error_text):
        errors = self.find_elements(self.error)
        text = errors[error_index].text
        assert text == error_text

    def check_first_name_save_error(self):
        with allure.step('Checking first name save error'):
            self._check_error(0, 'Please set your first name.')

    def check_last_name_save_error(self):
        with allure.step('Checking last name save error'):
            self._check_error(1, 'Please set your last name.')

    def check_card_number_save_error(self):
        with allure.step('Checking card number save error'):
            self._check_error(3, 'Please set your card number.')

    def check_payment_sys_save_error(self):
        with allure.step('Checking payment system save error'):
            self._check_error(4, 'Please select your payment system.')

    def get_saved_name(self, name_type):
        with allure.step('Getting saved name from cookie'):
            return self.driver.get_cookie(name_type)['value']

    def switch_to_payment_info(self):
        with allure.step('Switching to payment info'):
            self.find_element(self.payment_info).click()
