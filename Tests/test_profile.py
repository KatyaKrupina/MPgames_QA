import allure
import pytest

from Pages.profile_page import ProfilePage
from Test_data.profile_data import USER_NAMES, USER_NAMES_SYM, PS_NAMES, PAYMENT_DATA


@allure.feature('Profile')
class TestProfile:

    @allure.title('Open profile from main page')
    def test_open_profile_from_main_page(self, clients_page, browser):
        ProfilePage(browser).show_profile()

    @allure.title('Change user first name')
    def test_change_only_user_first_name(self, profile_page):
        profile_page.set_user_first_name('Ololo')
        profile_page.click_save_button()
        profile_page.check_last_name_save_error()

    @allure.title('Change user last name')
    def test_change_only_user_last_name(self, profile_page):
        profile_page.set_user_last_name('Trololo')
        profile_page.click_save_button()
        profile_page.check_first_name_save_error()

    @allure.title('Change user name with different symbols')
    @pytest.mark.parametrize('first_name, last_name', USER_NAMES)
    def test_save_user_name(self, profile_page, first_name, last_name):
        with allure.step('Changing user first and last name'):
            profile_page.set_user_first_name(first_name)
            profile_page.set_user_last_name(last_name)
            profile_page.save_user_info()

        with allure.step('Refresh page and check info is saved in cookies'):
            profile_page.driver.refresh()
            assert profile_page.get_saved_cookie('firstName') == first_name
            assert profile_page.get_saved_cookie('lastName') == last_name

    @allure.title('Change user name with incorrect symbols')
    @pytest.mark.parametrize('first_name, last_name', USER_NAMES_SYM)
    def test_save_incorrect_user_name(self, profile_page, first_name, last_name):
        with allure.step('Changing user first and last name'):
            profile_page.set_user_first_name(first_name)
            profile_page.set_user_last_name(last_name)
            profile_page.save_user_info()

        with allure.step('Refresh page and check info is not saved'):
            profile_page.driver.refresh()
            profile_page.click_save_button()
            profile_page.check_first_name_save_error()
            profile_page.check_first_name_save_error()

    @allure.title('Change user card number')
    def test_set_only_card_number(self, profile_page):
        with allure.step('Set card number'):
            profile_page.switch_to_payment_info()
            profile_page.set_card_number('1234 5678 9101 1213')

        with allure.step('Try to save and check error'):
            profile_page.click_save_payment_info_button()
            profile_page.check_payment_sys_save_error()

    @allure.title('Set payment system')
    @pytest.mark.parametrize('system_name', PS_NAMES)
    def test_set_only_payment_system(self, profile_page, system_name):
        with allure.step('Set payment system'):
            profile_page.switch_to_payment_info()
            profile_page.choose_payment_system(system_name)

        with allure.step('Try to save and check error'):
            profile_page.click_save_payment_info_button()
            profile_page.check_card_number_save_error()

    @allure.title('Change payment day')
    def test_change_payment_day(self, profile_page):
        profile_page.switch_to_payment_info()
        profile_page.choose_payment_day(10)

    @allure.title('Change and save all payment info')
    @pytest.mark.parametrize('card, payment_sys, payment_sys_idx', PAYMENT_DATA)
    def test_save_payment_info(self, profile_page, card, payment_sys, payment_sys_idx):
        with allure.step('Set all payment info'):
            profile_page.switch_to_payment_info()
            profile_page.set_card_number(card)
            profile_page.choose_payment_system(payment_sys)
            profile_page.choose_payment_day(31)

        with allure.step('Save and refresh page'):
            profile_page.save_payment_info()
            profile_page.driver.refresh()

        with allure.step('Check info is saved in cookies'):
            assert profile_page.get_saved_cookie('cardNumber') == card
            assert profile_page.get_saved_cookie('paymentSystem') == payment_sys_idx
            assert profile_page.get_saved_cookie('paymentDay') == '31'
